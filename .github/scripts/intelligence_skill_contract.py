#!/usr/bin/env python3
"""Validate Intelligence Skills JSON Schema 2020-12 contracts and fixtures."""
from __future__ import annotations
import copy, json, re, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SD = ROOT / "schemas" / "intelligence-skills"
FIXTURE = json.loads((ROOT / "examples/intelligence_skills/contracts.v1.json").read_text())
FILES = {
 "skill_frontmatter":"agent-skills-frontmatter.v1.schema.json",
 "plugin_manifest":"agent-plugins-1.0.0-plugin.schema.json",
 "mcp_config":"agent-plugins-1.0.0-mcp.schema.json",
 "capability_declaration":"skill-supply-chain.v1.schema.json",
 "sandbox_policy":"skill-supply-chain.v1.schema.json",
 "execution_trace":"skill-supply-chain.v1.schema.json",
 "scanner_verdict":"skill-supply-chain.v1.schema.json",
 "functional_evidence":"skill-supply-chain.v1.schema.json",
 "skill_bundle_attestation":"skill-supply-chain.v1.schema.json",
 "skill_release":"skill-supply-chain.v1.schema.json",
 "registry_descriptor":"skill-supply-chain.v1.schema.json",
 "boundary_evidence":"skill-supply-chain.v1.schema.json"
}
DEFS = {
 "capability_declaration":"capabilityDeclaration","sandbox_policy":"sandboxPolicy",
 "execution_trace":"executionTrace","scanner_verdict":"scannerVerdict",
 "functional_evidence":"functionalEvidence","skill_bundle_attestation":"skillBundleAttestation",
 "skill_release":"skillRelease","registry_descriptor":"registryDescriptor","boundary_evidence":"boundaryEvidence"
}
CACHE = {f: json.loads((SD/f).read_text()) for f in set(FILES.values())}

def schema_for(key):
    schema = CACHE[FILES[key]]
    if key in DEFS:
        return {"$schema":"https://json-schema.org/draft/2020-12/schema",
                "$ref":"#/$defs/"+DEFS[key],
                "$defs":schema["$defs"]}
    return schema

def validate(obj, schema, label):
    Draft202012Validator.check_schema(schema)
    errors = list(Draft202012Validator(schema).iter_errors(obj))
    if errors:
        e=errors[0]
        raise AssertionError(f"{label}: {list(e.path)} {e.message}")

def safe_path(p):
    if not p or p.startswith("/") or p.startswith(chr(92)) or re.match(r"^[A-Za-z]:",p):
        return False
    normalized = p.replace(chr(92), "/")
    return all(x not in ("", ".", "..") for x in normalized.split("/"))

def main():
    for key in FILES:
        validate(FIXTURE[key],schema_for(key),key)
    att=FIXTURE["skill_bundle_attestation"]
    assert att["fixture_only"] is True and att["verification_status"]=="not-verified"
    assert FIXTURE["capability_declaration"]["default_effect"]=="deny"
    assert FIXTURE["sandbox_policy"]["network"]["default_effect"]=="deny"
    assert "authority_token" not in json.dumps(FIXTURE).lower()
    cases=[]
    x=copy.deepcopy(FIXTURE); x["skill_frontmatter"]["name"]="../escape"; cases.append(("invalid name","skill_frontmatter",x))
    x=copy.deepcopy(FIXTURE); x["skill_frontmatter"].pop("description"); cases.append(("missing description","skill_frontmatter",x))
    x=copy.deepcopy(FIXTURE); x["skill_frontmatter"].pop("caps_profile"); cases.append(("unprofiled caps","skill_frontmatter",x))
    x=copy.deepcopy(FIXTURE); x["plugin_manifest"]["unexpected"]="x"; cases.append(("closed plugin manifest","plugin_manifest",x))
    x=copy.deepcopy(FIXTURE); x["mcp_config"]["mcpServers"]["runner"]["type"]="unknown"; cases.append(("unknown transport","mcp_config",x))
    x=copy.deepcopy(FIXTURE); x["sandbox_policy"]["network"]["default_effect"]="allow"; cases.append(("network default allow","sandbox_policy",x))
    x=copy.deepcopy(FIXTURE); x["execution_trace"]["events"][0]["environment_value"]="secret"; cases.append(("raw env value","execution_trace",x))
    x=copy.deepcopy(FIXTURE); x["scanner_verdict"]["verdict"]="safe"; cases.append(("scanner safety claim","scanner_verdict",x))
    x=copy.deepcopy(FIXTURE); x["skill_bundle_attestation"]["signature_algorithm"]="plaintext"; cases.append(("invalid signature algorithm","skill_bundle_attestation",x))
    x=copy.deepcopy(FIXTURE); x["skill_release"]["package_sha256"]="not-a-hash"; cases.append(("invalid package digest","skill_release",x))
    for label,key,obj in cases:
        try: validate(obj[key],schema_for(key),label)
        except AssertionError: continue
        raise AssertionError("negative case passed unexpectedly: "+label)
    assert safe_path("skills/example/SKILL.md")
    for p in ("../outside","skills/../../secret","/etc/passwd","C:\\\\Windows\\\\secret"):
        assert not safe_path(p), "package path escape accepted: "+p
    print(f"PASS: {len(FILES)} positive contracts; {len(cases)} negative cases; 5 package path cases")
    print("LIMIT: no skill execution, runtime sandbox, scanner, or cryptographic verification")
if __name__=="__main__":
    try: main()
    except Exception as exc:
        print("FAIL:",exc,file=sys.stderr); raise SystemExit(1)
