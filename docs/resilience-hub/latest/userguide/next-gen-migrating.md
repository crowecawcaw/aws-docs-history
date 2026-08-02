# Migrating from AWS Resilience Hub

If you're an existing AWS Resilience Hub (v1) customer, this guide helps you understand what changes
with the next generation of Resilience Hub and how to migrate your applications. The following table summarizes key
changes between the two versions.

| Area                      | AWS Resilience Hub v1                       | Next generation Resilience Hub                                          |
| ------------------------- | ------------------------------------------- | ----------------------------------------------------------------------- |
| **Core primitive**        | Application                                 | System + Services                                                       |
| **Assessment engine**     | Static rule-based checks                    | GenAI-powered failure mode analysis                                     |
| **Dependency visibility** | None                                        | Dependency discovery                                                    |
| **Multi-account**         | Limited                                     | Full AWS Organizations integration                                      |
| **Policies**              | Single RTO/RPO policy per application       | Modular, composable policies (DR + Availability + Data recovery)        |
| **Testing**               | AWS FIS experiment templates (manual setup) | Recommended resilience tests (pre-configured, auto-targeted, pass/fail) |
| **API version**           | /v1                                         | /v2                                                                     |

###### Topics

- [What changes with Next generation Resilience Hub](next-gen-what-changes.md "next-gen-what-changes.md")
- [Concept mapping: AWS Resilience Hub v1 to Next generation Resilience Hub](next-gen-concept-mapping.md "next-gen-concept-mapping.md")
- [Step-by-step migration guide](next-gen-migration-guide.md "next-gen-migration-guide.md")
- [Pricing transition](next-gen-billing-transition.md "next-gen-billing-transition.md")
- [Known limitations during migration](next-gen-migration-limitations.md "next-gen-migration-limitations.md")
