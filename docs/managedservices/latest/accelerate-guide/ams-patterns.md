# AMS patterns

An AWS Managed Services (AMS) pattern is a generalized solution that solves for a family of use cases in the AMS managed environment.

As you operate on the AMS platform, AMS cloud architects (CAs) work with you to meet your business and operational requirements.
While AMS customers operate in a unique way, we notice that customers have similar use-cases. In such cases, CAs create general solution templates,
or "patterns", that are used in multiple customer environments with minimal configuration and deployment effort.

AMS patterns are built to help deliver features to AMS customers and usually built by the account CA of the customer that requests it.

## How AMS patterns work

To request more details about each pattern including cloudformation templates required so you can deploy the pattern, submit an AMS service request
with the **Subject** "Request for additional details about pattern `Pattern_Name`" (substitute the pattern that you want)
and add your AMS cloud architect (CA) to the **Additional contacts** option.

AMS patterns are classified into two (2) categories:

- General Use: Patterns are considered stable as they have been deployed and being utilized by multiple AMS customers
- Preview Mode: AMS recommends deploying Preview Mode patterns in your non-production environments for validation,
  and engaging with your Cloud Architect to discuss the use case before deployment.

###### Important

AMS patterns do not adhere to your default AMS Service Level Agreements
[Service Level Agreements (SLAs)](acc-supp-ex.md "acc-supp-ex.md") and
[Service Level Objectives (SLOs)](acc-supp-ex.md "acc-supp-ex.md").
Support and updates to the pattern are done on a best-effort basis.

This AWS content is provided subject to the terms of the [AWS Customer Agreement](https://aws.amazon.com/agreement "https://aws.amazon.com/agreement")
or other written agreement between the customer and either Amazon Web Services, Inc. or Amazon Web Services EMEA SARL ("AWS Europe") or both.

The material embodied in this software is provided to you "as-is" and without warranty of any kind, express, implied or otherwise, including
without limitation, any warranty of fitness for a particular purpose.

## AMS patterns

AMS patterns.

| AMS patterns                                      | Name                                                                                                                                                                                                                                             | Overview                                                                                                                                                                                                                                                                               | Benefits                                                                  | Category |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------- |
| Customize CloudWatch Alarm Notifications          | Customize CloudWatch alarm notifications to include information from instance tags such as instance name, application ID,<br>and so forth.                                                                                                       | Adding contextual information to the alarm notifications will make them more meaningful and provides actionable information.                                                                                                                                                           | Monitoring                                                                |
| Disk Usage Reporting                              | The Disk Usage Reporting pattern collects consumption space of volumes across multiple app accounts and present<br>result as a centralized report in Amazon S3 with Athena table querying capability.                                            | Provide insights into account volumes' actual usage to determine cost saving opportunities.                                                                                                                                                                                            | Cost optimization                                                         |
| Prowler Stack                                     | Runs Prowler checks on accounts using Amazon EC2 where CloudShell can’t be used.                                                                                                                                                                 | Help unblock the Accelerate onboarding (Prowler) in cases where CloudShell<br>can't be used either due to permissions or timeout issues without any impact to their current security posture.                                                                                          | Security                                                                  |
| AMS Amazon S3 Replication with Custom Object Keys | Make copies of Amazon S3 objects and retain all metadata and object keys (folders).<br>Strips part of the source object keys, or creates custom destination object keys during replication.                                                      | Customize the object keys (folders) during Amazon S3 replication<br>without requiring additional scripts to move objects to required folders.                                                                                                                                          | Reliability                                                               |
| Amazon EBS Snapshot Deletion                      | Automation based on Lambda and CloudWatch Events to automate deletion of Amazon EBS snapshots taken outside of AWS Backup, based on retention.                                                                                                   | Help purge individual snapshots taken outside of AWS Backup orchestrator, saving added cost over time.                                                                                                                                                                                 | Cost optimization                                                         |
| AMS Amazon RDS Secrets Rotation                   | Using a CloudFormation template, automatically deploy all required resources (Lambda function, Security groups, elastic network interfaces or ENIs)<br>needed for rotating secrets for supported Amazon RDS databases, Redshift, and DocumentDB. | Automate database secrets rotation, and provide a notification mechanism when rotation failure occurs.                                                                                                                                                                                 | Security                                                                  |
| Automated Key Rotation                            | Automatically rotate access and secret keys for IAM users based, on CloudWatch Events and Lambda.                                                                                                                                                | Easier rotation of access and secret keys for IAM users.                                                                                                                                                                                                                               | Security                                                                  |
| Amazon EBS Volume Snapshot Tagger                 | Tag all Amazon EBS volumes and snapshots using the tags in the Amazon EC2 instances.                                                                                                                                                             | Help categorize and track costs with meaningful, relevant business information making it easier to validate where<br>money is being spent, and enable the use of automation for tagged volumes and snapshots. Highly recommended best practice<br>by the AWS Cost Optimization pillar. | Tagging (cost optimization, Security, incident management and automation) |
