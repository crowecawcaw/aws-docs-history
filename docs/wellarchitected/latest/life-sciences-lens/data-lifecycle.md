# Data lifecycle

Life sciences organizations must carefully orchestrate data management across complex
project lifecycles that span years or even decades, from initial research design through
clinical trials to post-market surveillance. This section provides guidance for managing life
sciences data through each critical phase—design, active data collection and analysis, reuse
preparation, and compliant archival. The approach emphasizes regulatory adherence, data
integrity, secure collaboration, and cost-effective storage strategies while keeping valuable
research data accessible and reusable for future scientific endeavors. By following these
lifecycle management practices, organizations can maintain audit readiness, enable
cross-organizational collaboration, and meet stringent regulatory requirements throughout the
entire data journey.

As with most data analytics workloads, begin with the [Data Analytics Lens](../analytics-lens/analytics-lens.md "../analytics-lens/analytics-lens.md").
Designing a data repository for life sciences related projects adds complexity based on the type
of data created, collected, and stored, as well as the lifecycle of that data. The most
straightforward way to approach this is to look at the lifecycle of a project.

## Design phase

A group of documents will be generated to describe the project and decide how the data
will be gathered and who will have access, such as the protocol, manufacture, and distribution
plan, data capture forms, consent forms, and infrastructure as code (IaC) scripts. House these
documents and the supporting material together in an auditable document management system.
Make documents available in an exportable format to facilitate archiving. When the time comes,
they can be transferred alongside other data and infrastructure artifacts to deep storage
systems like Amazon Glacier.

System build outs should be reproducible. Construct environments using infrastructure as
code so that you can create exact test and development replicas as well as take down the
entire environment and archive the solution. Immediately rebuild archived solutions on demand
if required. For example, you can build AWS systems using AWS CloudFormation Stacks.

## Data gathering,

analysis, publication, and manufacturing phases

During the active phase of the project, data will be generated from multiple sources,
including electronic data capture, electronic health records, Internet of Things (IoT) device
logs, and public records. When deciding how to gather and store the data, keep in mind
potential later usage and collaboration with other teams or for use in AI-driven workflows.
Implement standardized data models and formats that promote interoperability and long-term
accessibility.

Adopting industry standards such as CDISC or FHIR for health record data or ISA-95 for
manufacturing records verifies that data can be shared, analyzed, and understood across
different systems and by various stakeholders. Consider this standardization from the outset
when writing project documents and designing data collection processes. For example, you can
store FHIR data in AWS HealthLake to ease interoperability later on by guiding and enforcing the
FHIR model.

During this phase, auditability and access controls are critical. Implementing a
comprehensive data protection impact assessment (DPIA) assist to identify and mitigate
potential risks. It is essential to maintain a clear map of data access, and appropriately
de-identify sensitive information when necessary while still allowing for traceability back to
individuals when required.

The system should maintain comprehensive audit trails using AWS CloudTrail and Amazon CloudWatch,
tracking instances of data access and modifications. The infrastructure must support both
PHI-containing and de-identified datasets, with appropriate security controls. Organizations
can use AWS Glue for data cataloging and AWS Lake Formation for fine-grained access control, limiting
data access to authorized personnel while maintaining the ability to collaborate securely
through AWS Clean Rooms externally and Amazon Data Zone for internal traceable data governance.

As data is produced, determine if it is reusable. Can it be used for future clinical
exploration? Can it be used for improving manufacturing processes in the future? Identify
those data sets and prepare them to be reusable. Export the data into Amazon S3 in a format that
contains the metadata and is offered through AWS Data Exchange, such as Iceberg or Parquet.

Once a study has concluded and the papers have been delivered or a manufacturing line has
been shut down, there are regulations in different countries mandating retention of the
related data. To adhere to these regulations, you can store the artifacts in Amazon Glacier. After the
data is safely archived, remove the entire environment that once collected and housed the
data. This verifies that no one can later access PHI inappropriately. By building out the
AWS environment using AWS CloudFormation stacks, you can delete entire environments (stacks) in a
straightforward and efficient way.
