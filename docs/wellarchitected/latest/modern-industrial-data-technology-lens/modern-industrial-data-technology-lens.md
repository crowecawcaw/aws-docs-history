# Modern Industrial Data Technology Lens

Publication date: **October 30, 2025** ([Document revisions](document-revisions.md "document-revisions.md"))

This whitepaper describes the AWS Well-Architected Framework Lens on modern industrial
data technology. It provides guidance to help customers apply the well-architected best
practices in the design, delivery, and maintenance of AWS environments. We address general
design principles as well as specific best practices and implementation guidance in six
conceptual areas that we define as the pillars of the Well-Architected Framework.

The AWS Well-Architected Framework helps you understand and assess the pros and cons of
decisions you make while building systems on AWS. By using the Framework, you can learn
architectural best practices for designing and operating reliable, secure, efficient, and
cost-effective systems in the cloud. It provides a way for you to consistently measure your
architectures against best practices and identify areas for improvement. The process for
reviewing an architecture is a constructive conversation about architectural decisions and is
not an audit mechanism. We believe that having well-architected systems greatly increases the
likelihood of business success.

While the Framework provides foundational guidance, certain workloads, such as those in
modern industrial data (MID), require specialized focus due to their unique challenges and
requirements. MID workloads face distinct challenges including:

- OT and IT convergence and integration requirements
- Real-time data processing needs for production environments
- Industrial IoT device management and edge computing demands
- Complex regulatory compliance across manufacturing operations
- Mission-critical system reliability requirements
  The AWS Well-Architected Framework documents a set of foundational questions that help you
  understand if a specific architecture aligns well with cloud best practices. The Framework
  provides a consistent approach to evaluating systems against the qualities you expect from
  modern cloud-based systems, as well as the remediation that would be required to achieve those
  qualities. As AWS continues to evolve and we continue to learn more from working with our
  customers, we will continue to refine the definition of well-architected.

AWS Solutions Architects (SAs) have extensive experience helping customers architect and
optimize their MID solutions. Through thousands of customer engagements, we've aggregated best
practices specifically focused on manufacturing and industrial workloads. This lens builds
upon the core Well-Architected Framework to provide manufacturing-specific guidance.

This framework is intended for technology leaders in manufacturing, including Chief
Technology Officers (CTOs), industrial automation engineers and architects, manufacturing IT
teams, system integrators, operations technology professionals, and anyone involved in
designing and operating manufacturing systems on AWS. It describes AWS best practices and
strategies to use when designing and operating a cloud workload, and provides links to further
implementation details and architectural patterns. For more information, see the [AWS Well-Architected homepage](https://aws.amazon.com/architecture/well-architected/?ref=wellarchitected-ws "https://aws.amazon.com/architecture/well-architected/?ref=wellarchitected-ws").

AWS also provides a service for reviewing your workloads. The [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/?ref=wellarchitected-ws "https://aws.amazon.com/well-architected-tool/?ref=wellarchitected-ws") (AWS WA Tool) is a service in the cloud user console that
provides a consistent process for you to review and measure your architecture using the AWS
Well-Architected Framework. The AWS WA Tool provides recommendations for making your workloads
more reliable, secure, efficient, and cost-effective.

To help you apply best practices, we have created [AWS Well-Architected
Labs](https://wellarchitectedlabs.com/?ref=wellarchitected-ws "https://wellarchitectedlabs.com/?ref=wellarchitected-ws"), which provide you with a repository of code and documentation to give you
hands-on experience implementing best practices. We also have teamed up with select AWS Partner Network (APN) Partners, who are members of the [AWS Well-Architected
Partner program](https://aws.amazon.com/partners/programs/well-architected/ "https://aws.amazon.com/partners/programs/well-architected/"). These APN Partners have deep AWS knowledge and experience and can
help you review and improve your workloads.

**How to use this lens**

- Review the general design principles for Modern Industrial Data Architecture (MIDA)
- Evaluate your workloads against the manufacturing-specific best practices in each
  pillar
- Use the provided questions and guidance to identify areas for improvement
- Leverage the implementation patterns and examples to optimize your architecture.

## Custom lens availability

Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own
[custom
lenses](../userguide/lenses-custom.md "../userguide/lenses-custom.md"), or to use lenses created by others that have been
shared with you.

To determine if a custom lens is available for the lens described
in this whitepaper, reach out to your Technical Account Manager
(TAM), Solutions Architect (SA), or Support.
