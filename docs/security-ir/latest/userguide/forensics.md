# Forensics on AWS

Concepts from traditional on-premises forensics apply to AWS. The
[Forensic
investigation environment strategies in the AWS Cloud](https://aws.amazon.com/blogs/security/forensic-investigation-environment-strategies-in-the-aws-cloud/ "https://aws.amazon.com/blogs/security/forensic-investigation-environment-strategies-in-the-aws-cloud/") blog post provides
you with key information to start migrating their forensic expertise to AWS.

Once you have your environment and AWS account structure set up for forensics, you’ll
want to define the technologies required to effectively perform forensically sound
methodologies across the four phases:

- **Collection** – Collect relevant AWS logs, such as
  AWS CloudTrail, AWS Config, VPC Flow Logs, and host-level logs. Collect snapshots,
  backups, and memory dumps of impacted AWS resources.
- **Examination** – Examine the data collected by
  extracting and assessing the relevant information.
- **Analysis** – Analyze the data collected in order
  to understand the incident and draw conclusions from it.
- **Reporting** – Present the information resulting
  from the analysis phase.
