# Change management in Direct Change mode

Change management is the process that AMS Advanced uses to implement requests for change. A request for change
(RFC) is a request created by either you, or AMS Advanced through the AMS Advanced interface to make a change to your managed
environment and includes an AMS Advanced change type (CT) ID for a particular operation. For more information, see
[Change management](ex-what-is.md "ex-what-is.md").

###### Note

Direct Change mode does not remove AMS change management RFCs,
you still have full access to AMS RFCs with DCM.

AMS Direct Change mode (DCM) extends AMS Advanced change management by providing native AWS access to AMS Advanced
Plus and Premium accounts to provision and update AWS resources. Users who have been granted Direct Change mode permission
through the IAM roles, can use native AWS API access to provision and make changes to resources in their AMS Advanced accounts.
The users can still use AMS Advanced change management RFCs using the same IAM roles. In both cases the resources and
changes to them are fully supported by AMS, including monitoring, patch, backup, incident response management.
Users who do not have the appropriate role in these accounts must use the AMS Advanced change management RFC process to make changes.

## Change management use cases

For security reasons, some changes in AMS Advanced can only be done through the change management request for change (RFC) process.
The `AWSManagedServicesCloudFormationAdminRole` is restricted to actions taken through CloudFormation (CFN). For more about how to create stacks
through DCM, see
[Creating stacks using Direct Change mode](dcm-creating-stacks.md "dcm-creating-stacks.md").
The `AWSManagedServicesUpdateRole` is restricted for the following actions.

For example walkthroughs for each change type, including the Management | Managed account | Direct Change mode | Enable (ct-3rd4781c2nnhp) change type,
see the "Additional Information" section for the relevant change type in the _AMS Advanced Change Type Reference_
[Change Types by Classification](../ctref/classifications.md "../ctref/classifications.md") section.

| Service                                             | Action                    |
| --------------------------------------------------- | ------------------------- |
| AWS Key Management Service (AWS KMS)                | Update                    |
| AWS Certificate Manager                             | Create                    |
| AWS Identity and Access Management (IAM)            | Any                       |
| Site-to-Site VPN                                    | Any                       |
| AMS Resource Scheduler                              |
| AWS Backup                                          | Create backup plan        |
| AMS Workload Ingestion (WIGs)                       | Any                       |
| AMS Egress Filtering (Managed Palo Alto)            |
| AMS Advanced MALZ account changes                   |
| Amazon GuardDuty                                    |
| AMS Advanced Stack Access                           | Any                       |
| Amazon Elastic Block Store (EBS) volume             | Delete                    |
| Amazon Elastic Block Store (EBS) default encryption | Enable default encryption |
| Amazon Elastic Compute Cloud (Amazon EC2)           | Change hostname           |
| Amazon Machine Images (AMI)                         | Delete, share             |
| Amazon EC2 Security Group                           | Any                       |
| AMS Advanced SSPS                                   |
| AWS Managed Microsoft AD                            |
| AMS Advanced developer mode                         |
| Amazon Simple Storage Service (Amazon S3)           | Create S3 bucket policies |
| AWS Systems Manager                                 | Create                    |
