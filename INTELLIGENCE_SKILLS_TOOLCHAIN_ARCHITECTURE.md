# Intelligence Skills Toolchain Architecture — UNIVERSALIS

Owner: The UNIVERSALIS Intelligence Skills repository  
Boundary: Public UNIVERSALIS / MotherThread  
Status: Open architecture and contract foundation; third-party integrations remain pending  
Version: 1.0.0 proposal, 2026-11-12

## Purpose and independence

UNIVERSALIS treats an intelligence skill as a portable, self-describing artifact: a manifest, package boundary, declarative capability set, execution environment, and evidence that can be independently inspected. Registries and runtimes are operator-controlled. The base system remains usable without a central registry, cloud account, private signing service, or access to C2O.

This public repository contains no C2O-private credentials, authority tokens, agent identities, policy decisions, registry records, budgets, signing keys, or private operational evidence. A signed artifact may be verified using a published trust anchor, but verification does not transfer the producer's authority to the receiver.

## Relationship to the Intelligence Skills taxonomy

The canonical Intelligence_Skills.md taxonomy (I-S-01 through I-S-20) remains the concept/classification layer. This toolchain is the artifact, package, discovery, sandbox, safety-evaluation, evidence, and execution layer. A concept entry is not proof that an agent has demonstrated the skill. Actor assignments require a task, environment, configuration, evaluator, outcome, evidence URI, uncertainty, and limitations.

## Open UNIVERSALIS candidate inventory

### Manifest and package
- Agent Skills Specification: open SKILL.md directory format, required name/description, optional license/compatibility/metadata/experimental allowed-tools, progressive disclosure, scripts/references/assets.
- Agent Plugins 1.0.0: portable package contract with plugin.json, optional skills/, optional root mcp.json, and reverse-domain client extensions.

### Registry and quality
- MCP Skill Registry: candidate self-hostable folder-to-MCP-tool and REST discovery/execution server.
- SkillDock.io: candidate versioned registry, SDK, CLI, dependency resolution, and release management.
- OpenSpace: candidate outcome-based quality hub with lineage, versions, and MCP interfaces.

### Sandbox and execution
- SkillSandbox: candidate capability-policy runtime with default-deny network, environment, filesystem controls, and execution traces.
- Skillbox: candidate self-hosted Python/Node/Bash sandbox execution API.
- SkillSeal: candidate isolated functional/security evaluator and Ed25519 evidence certification.

### Safety scanning
- Cisco Skill Scanner: open static and optional LLM-assisted scanner; best-effort detection, not certification.
- Zenity Labs AI Total: candidate contained runtime observation and threat verdict.
- Tencent skill-scan: candidate LLM-assisted multi-stage static audit pipeline.
- Hybrid static/dynamic/agentic analysis: research pattern combining skill content, scanner, and sandbox evidence.

### Attestation and competence provenance
- NVIDIA signed skills: candidate detached-signature, trust-anchor, governance-card, and benchmark-evidence pattern.
- Formal verification of agent skills: candidate proof-carrying bundle with independent replay and Ed25519 signing.
- Cupel: candidate demonstrated-competence provenance pattern, including VC/Open Badges-compatible records.

All named tools are research candidates. Verify canonical repositories, licenses, maintenance, dependencies, data flows, runtime isolation, signer trust, and evaluation scope before adoption. Candidate names are not installed integrations.

## Shared portable contracts

The contract set is registry-neutral and does not create a central registry:
- Agent Skills frontmatter profile.
- Agent Plugins 1.0.0 plugin.json and mcp.json schema snapshots.
- Versioned capability declaration and optional caps profile extension.
- Skill sandbox policy and execution trace.
- Scanner verdict with static/dynamic/hybrid evidence references.
- Functional-evidence report.
- Skill Bundle Attestation (SBA).
- Skill release/dependency descriptor.
- Registry discovery descriptor for optional MCP-tool and REST interfaces.
- Boundary-evidence record for data, memory, tools, model routing, egress, consent, and actions.

caps is a C2O/UNIVERSALIS profile extension; it is not a base Agent Skills frontmatter field. The base standard requires name and description; allowed-tools is experimental and is not a sandbox or authorization mechanism. The portable capability declaration uses default_effect deny and describes requested capabilities, not granted authority.

Agent Plugins 1.0.0 defines fixed package paths. Its path-containment rule prevents package paths escaping the plugin root, but does not sandbox a running skill. Sandbox isolation, process limits, tool authorization, and egress controls are separate runtime duties.

## Independence and verification rules

- A skill may be installed from a local directory or any compatible registry.
- Validate plugin.json, mcp.json, and skill manifests before exposing components.
- Reject package path traversal and resolved symlink escapes.
- Do not interpret allowed-tools as an authorization grant.
- Enforce sandbox policy outside the skill process: deny-by-default network, environment, filesystem, process, and resource scopes.
- Record explicit execution events and evidence hashes; never record private reasoning or raw secret values.
- Scanner no-known-findings is not a claim of safety; high-risk use requires independent review.
- Functional evidence binds exact hashes of the skill, test suite, sandbox policy, and trace.
- SBA signatures bind a statement to content/evidence hashes and a trust anchor. A signature is not an access grant and does not certify future behavior after a skill changes.
- The receiving operator decides whether to accept a package using its own policy, verification, threat model, and task context.

## Not yet implemented

This branch provides shared schemas, synthetic fixtures, semantic checks, and CI. It does not deploy a production registry, MCP/REST host, sandbox runtime, scanners, signature service, proof verifier, quality hub, skill optimizer, or competence credential issuer. The example signature is synthetic and is not cryptographically verified.

## References

Agent Skills: https://agentskills.io/specification  
Agent Plugins 1.0.0: https://agent-plugins.org/specification  
Agent Plugins manifest schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json  
Agent Plugins MCP schema: https://agent-plugins.org/schemas/1.0.0/mcp.schema.json  
Cisco Skill Scanner: https://github.com/cisco-ai-defense/skill-scanner  
Hybrid static/dynamic/agentic analysis: https://arxiv.org/abs/2611.10830

Remaining product descriptions and performance figures are owner-supplied research claims pending direct source verification and reproduction.


## Expanded evidence and lifecycle contracts

The shared schema registry also provides records for Tool Bill of Materials (TBOM), Tool Security Advisory (TSA), formal-verification evidence bundles, outcome-based skill quality/lineage, demonstrated competence provenance, and correction/revocation propagation. These cover portable evidence shapes for ABA boundary assurance, proof replay, OpenSpace-style outcome lineage, Cupel-style competence provenance, and correction-aware skill lifecycles. These records are registry-neutral and do not introduce a central registry or a C2O authority service.

Additional open-side candidates already recorded in this repository's engineering context—hackmyagent for scan/red-team/behavioral simulation, Cisco DefenseClaw, and Sandlock as alternative security/sandbox candidates—remain candidates pending identity/version, license, security, and compatibility verification. SkillSeal and Cupel also appear in the Human Capabilities proposal; NVIDIA OpenShell appears in Intelligence Capabilities. Reconcile identity and version before deduplicating these cross-domain mentions.

There are eighteen shared schema record families. Current CI validates all eighteen shared fixture objects plus package path traversal and resolved-symlink containment checks. This does not mean actual skills are executed under a production sandbox: runtime enforcement, live scanner execution, cryptographic SBA verification, proof replay, competence credential issuance, advisory propagation, and a production registry remain unimplemented.
