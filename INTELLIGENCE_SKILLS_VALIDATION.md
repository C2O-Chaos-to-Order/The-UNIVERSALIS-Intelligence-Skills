# Intelligence Skills Validation Record

Branch: implementation/repository-foundation-2026-11-12  
Contract version: 1.0.0  
Status: Implementation files and CI authored; exact-commit workflow result pending.

## Implemented checks

- Draft 2020-12 meta-validation of the shared schemas.
- Positive fixture validation for Agent Skills frontmatter, Agent Plugins plugin/MCP manifests, capabilities, sandbox policy, execution trace, scanner verdict, functional evidence, SBA, release, registry discovery, and boundary evidence.
- Negative cases for invalid names, missing descriptions, unprofiled caps extension, unknown plugin fields, unsupported MCP transport, allow-by-default networking, raw environment values in traces, unsafe scanner verdict vocabulary, invalid signature algorithm, and malformed package digest.
- Package traversal and absolute-path rejection.
- Fixture attestation is explicitly marked fixture_only and not-verified. Its signature bytes are synthetic.

## C2O-only checks

The private repository adds a distinct authority-decision record and checks that requested capabilities are a subset of declared capabilities, granted capabilities are a subset of requested capabilities, high/critical allowed runs carry a human permit reference, budgets are not exceeded, and egress remains deny-by-default. This schema and fixture are not copied to UNIVERSALIS.

## Limits

These tests do not execute skills, enforce a sandbox, operate a registry, run third-party scanners, prove a skill benign, cryptographically verify Ed25519, validate trust-chain authorization, or issue permits. A schema-valid record does not prove that its described event occurred. External tools remain proposed candidates pending canonical-source, license, security, compatibility, and independent behavior review.
