# Engineering Toolchain and Initial Build Plan

**Repository:** `C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills`  
**Responsibility:** Intelligence Skills  
**Status:** Initial executable foundation in this branch; specialized candidates remain proposed pending verification.  
**Boundary:** Open UNIVERSALIS / independently operable. No C2O-private credentials, policies, authority state, or restricted operational data.

## Universal engineering foundation

- Least-privilege GitHub Actions CI, automated tests, and JSON contract/config validation.
- CodeQL/static analysis, secret scanning, dependency review, Dependabot, actionlint, and SBOM generation after settings, ownership, and outputs are confirmed.
- CycloneDX/SPDX, OSV-Scanner, Trivy/Grype, Gitleaks, SLSA provenance, in-toto attestations, cosign signing, and immutable releases as staged assurance capabilities.
- Pin toolchain versions and action references; preserve specifications, fixtures, execution logs, provenance, limitations, and version history.

**Foundation candidates:** Secure SDLC Evidence Collector; repo-assurance; Chainguard Actions; cnspec SBOM Cataloger; CodeQL; actionlint; OSV-Scanner; Trivy/Grype; Gitleaks; SLSA/in-toto; cosign. These are candidates, not verified integrations.

## Domain-specific candidate tools

SkillSandbox as the proposed open capability-enforcement runtime; hackmyagent for skill scanning/red-team simulation; Cisco DefenseClaw and Sandlock as alternatives requiring independent assessment. SandyClaw is primarily the C2O-private dynamic-vetting candidate and is not assumed as a UNIVERSALIS dependency. Define manifests, declared capabilities, least-privilege execution, sandbox tests, and structured audit trails.

Verify each candidate's canonical source, license, maintainer, release activity, security, compatibility, data flow, and claims before adoption. Advertised capabilities are not evidence of repository implementation.

## Initial executable implementation

- `.github/workflows/repository-quality.yml` runs on pushes and pull requests with read-only repository permissions.
- `.github/scripts/repository_quality_baseline.py` provides a dependency-free self-test and validates JSON in schema/manifest/contract/capability/skill directories plus `package.json` and `tsconfig.json`.
- This narrow baseline does not replace formal ontology validation, skill sandboxing, CodeQL, secret scanning, SBOMs, or domain-specific conformance.

## Next increments

1. Audit current source, schemas, graph fixtures, workflow permissions, and dependencies.
2. Add positive/negative domain fixtures and deterministic contract tests.
3. Integrate the domain harness after source/license/security review.
4. Preserve validation outputs, dependency/SBOM evidence, provenance, and unresolved findings.

## Evidence status

| Item | Status |
|---|---|
| Tool candidates recorded | Documented |
| Baseline validator and CI authored | Implemented in this branch |
| GitHub Actions execution | Pending |
| Domain candidate verification | Pending |
| Specialized integration | Not yet implemented |

## Cross-repository architecture register — 2026-11-12

The following are the canonical working records for the latest owner-supplied toolchain proposals. This repository records the references and boundary rules; implementation belongs in the domain-owning repositories.

### Human Knowledge
- [C2O Human Knowledge architecture](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/HUMAN_KNOWLEDGE_ARCHITECTURE.md), [shared MCP interface contracts](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/MCP_INTERFACE_CONTRACTS.md), and [validation evidence](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/HUMAN_KNOWLEDGE_VALIDATION.md).
- [UNIVERSALIS Human Knowledge architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/HUMAN_KNOWLEDGE_ARCHITECTURE.md), [shared MCP interface contracts](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/MCP_INTERFACE_CONTRACTS.md), and [validation evidence](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/HUMAN_KNOWLEDGE_VALIDATION.md).

### OS provisioning and virtualization
- [C2O private provisioning architecture](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem/blob/implementation/repository-foundation-2026-11-12/OS_PROVISIONING_ARCHITECTURE.md).
- [UNIVERSALIS open provisioning architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/OS_PROVISIONING_ARCHITECTURE.md).

### UNIVERSALIN Grid, Guardian, and Golden Compass
- [C2O boundary and verifier architecture](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem/blob/implementation/repository-foundation-2026-11-12/UNIVERSALIN_GUARDIAN_GOLDEN_COMPASS.md).
- [UNIVERSALIS Grid / Guardian / Compass architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/UNIVERSALIN_GUARDIAN_GOLDEN_COMPASS.md).

### Boundary and evidence status
C2O-private credentials, policies, identity state, authority tokens, private source text, and operational evidence remain inside authorized C2O environments. UNIVERSALIS remains public, local-first, inspectable, and independently operable. Only versioned, explicitly approved interface schemas and evidence packages may cross the boundary; an interface does not grant authority.

All named external tools remain owner-supplied candidates or reference patterns pending canonical-source, license, maintainer, release, security, compatibility, and claim verification. No candidate is represented as installed or adopted merely because it appears in these records.

## Powers energy architecture register — 2026-11-12

Powers treat energy efficiency as a measurable, enforceable, auditable capacity—not only a permission or evaluation. In the current UNIVERSALIS repository set, the canonical implementation is maintained in the Intelligence Powers repository.

- **Canonical open architecture:** [UNIVERSALIS Powers energy architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/POWERS_ENERGY_ARCHITECTURE.md).
- **Shared v1 contract:** [Powers energy schema](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/schemas/powers/powers-energy-contracts.v1.schema.json).
- **Executed checks and limitations:** [Powers validation record](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/POWERS_ENERGY_VALIDATION.md).

The open implementation is local-first and independently operable. Measurement, forecasting, receipts, and synergy calculation do not require a central database or truth authority. It keeps actual workload telemetry and local policy in the operator's chosen environment. The shared contract excludes private credentials and policy values. PDU/RAPL/Kepler/GPU layers require overlap reconciliation; synergy comparisons require matched workload cohorts and SLO profiles. External tools and their advertised savings remain candidates until independently verified.

## Four-document source coverage — 2026-11-12

The complete owner-supplied tool inventory and status matrix for Human Knowledge, Powers, Human Capabilities, and Mapping/Matrix/Organization/Ecosystem Mapping is maintained in the UNIVERSALIS research register: https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/FOUR_DOCUMENT_TOOLCHAIN_COVERAGE.md.

Treat every third-party name in that register as a proposed candidate/reference pattern until canonical source, license, maintenance, security, compatibility, and behavior are reviewed. The register distinguishes documented tools, basic contracts, passing CI, and actual integrations. This repository owns only the parts assigned to its domain. No C2O-private repository links or policy values are part of this public register.

## Master toolchain coverage register — 2026-11-12

The current public inventory for the original four toolchain documents plus Intelligence Capabilities and Intelligence Skills is maintained in the UNIVERSALIS research register: https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/TOOLCHAIN_COVERAGE_REGISTER.md. It distinguishes documentation, basic contracts, passing CI, and actual integrations. This public register contains no links to C2O-private owner repositories or policy values.


## Sixth toolchain source — Intelligence Skills — 2026-11-12

The sixth owner-supplied inventory defines the open UNIVERSALIS skill artifact and execution layer. The canonical taxonomy remains in `Intelligence_Skills.md`; this toolchain does not replace it.

- [UNIVERSALIS open skill toolchain architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/blob/implementation/repository-foundation-2026-11-12/INTELLIGENCE_SKILLS_TOOLCHAIN_ARCHITECTURE.md)
- [Portable supply-chain schemas](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/tree/implementation/repository-foundation-2026-11-12/schemas/intelligence-skills)
- [Synthetic package example](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/tree/implementation/repository-foundation-2026-11-12/examples/plugin)
- [Validation and limitations](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/blob/implementation/repository-foundation-2026-11-12/INTELLIGENCE_SKILLS_VALIDATION.md)

Candidate inventory: Agent Skills Specification; Agent Plugins 1.0.0; MCP Skill Registry; SkillDock.io; OpenSpace; SkillSandbox; Skillbox; SkillSeal; Cisco Skill Scanner; Zenity Labs AI Total; Tencent skill-scan; hybrid static/dynamic/agentic analysis; NVIDIA signed skills; formal verification of agent skills; Cupel. These are research candidates/patterns, not installed integrations.

The common contracts are registry-neutral: manifest profile, package schemas, requested capability declaration, default-deny sandbox policy, execution trace, scanner verdict, functional-evidence report, SBA, release/dependency record, discovery descriptor, and boundary-evidence record. Each operator controls its own registry and acceptance policy. No C2O private authority, registry, credentials, permit, trust store or operational data is part of the public implementation.

The research [public master toolchain coverage register](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/TOOLCHAIN_COVERAGE_REGISTER.md) records all six source inventories and their evidence state.


## Security and Cybersecurity — eleventh owner-supplied source — 2026-11-12

Canonical public architecture: [UNIVERSALIS Security and Cybersecurity](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/SECURITY_CYBERSECURITY_ARCHITECTURE.md). The public security contract, synthetic fixtures and validation evidence are linked from that architecture. The [UNIVERSALIS eleven-source master toolchain register](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/TOOLCHAIN_COVERAGE_REGISTER.md) preserves candidate provenance, verification caveats and integration limits.

Public repositories contain only portable contracts and synthetic examples: no C2O-private policies, keys, incident data, authority records or target inventories. External security tools remain candidates until source, license, release, data flow, platform and enforcement behavior are reviewed. No security product or offensive assessment system is claimed integrated.
