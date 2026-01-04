# Life Sciences Lens - AWS Well-Architected

Framework

Publication date: **December 30, 2025** ([Document revisions](document-revisions.md "document-revisions.md"))

This paper describes the Life Sciences Lens for the AWS Well-Architected Framework, which
enables you to review and improve your cloud-based architectures and better understand the
impact of design decisions. We present general design principles and specific best practices
aligned to the six pillars of the Well-Architected Framework.

The life sciences industry includes organizations involved in the research, development,
manufacture, distribution, and tracking of insights related to drug therapies and related
interventions for improving human health and fighting disease.

A key requirement for many life sciences is GxP adherence. GxP refers to the collection of
quality guidelines and regulations that verify that systems, facilities, equipment, and
processes used in regulated industries are designed, monitored, and controlled to produce
consistent, high-quality outcomes while maintaining data integrity and patient safety. The x in
GxP represents different contexts where these practices apply throughout the drug development
life cycle. Beginning with research and discovery, companies identify drug targets, analyze
biological and genomic data, and gather laboratory data to create candidates for new therapies
following Good Laboratory Practices (GLP). Clinical trials validate safety and effectiveness
with regulatory oversight, following Good Clinical Practices (GCP) with in-depth data analysis
and collaboration research and clinical organizations (internal and external).

After approval, Good Manufacturing Practices (GMP) must be followed to manufacture them.
Once drug therapies are available for patients, data must be collected and analyzed to
understand efficacy of their use in treatments and to evaluate adverse events through the use of
real world data (RWD) and real world evidence (RWE).

There are common patterns of regulatory adherence, data strategy and collaboration, and
compute requirements throughout this pipeline of developing drug therapies, bringing them to
market, and gaining insights into their use and efficacy. The Life Sciences Lens addresses these
scenarios and provides guidance for common patterns along with recommendations for services,
architectures, and configurations to incorporate into a life sciences workload in an AWS
environment.

## Lens availability

Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own
[custom
lenses](../userguide/lenses-custom.md "../userguide/lenses-custom.md"), or to use lenses created by others that have been
shared with you.

To begin reviewing your life sciences workload, download and import the [Life Sciences Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/life-sciences-lens/life-sciences-lens.json "https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/life-sciences-lens/life-sciences-lens.json") into AWS Well-Architected Tool from the public [AWS Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens "https://github.com/aws-samples/sample-well-architected-custom-lens").
