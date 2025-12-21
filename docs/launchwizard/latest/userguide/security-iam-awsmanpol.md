# AWS managed policies for AWS Launch Wizard

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

###### Managed policies:

- [AmazonLaunchWizardFullAccessV2](#security-iam-awsmanpol-AmazonLaunchWizardFullAccessV2 "#security-iam-awsmanpol-AmazonLaunchWizardFullAccessV2")
- [AmazonEC2RolePolicyForLaunchWizard](#security-iam-awsmanpol-AmazonEC2RolePolicyForLaunchWizard "#security-iam-awsmanpol-AmazonEC2RolePolicyForLaunchWizard")
- [Policy updates](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS

managed policy: AmazonLaunchWizardFullAccessV2

You can attach the `AmazonLaunchWizardFullAccessV2` policy to your
IAM identities.

This policy grants administrative permissions that allow full access to AWS Launch Wizard
and other required services. To view the managed policy content, see the [AmazonLaunchWizardFullAccessV2](../../../aws-managed-policy/latest/reference/AmazonLaunchWizardFullAccessV2.md "../../../aws-managed-policy/latest/reference/AmazonLaunchWizardFullAccessV2.md") page in the _AWS Managed
Policy Reference Guide_.

**Permissions details**

This policy includes the following permissions.

- `launchwizard` – Allows all Launch Wizard actions.
- `applicationinsights` – Allows all CloudWatch Application Insights actions. This
  permission is required so that an application can be tracked and configured
  by CloudWatch Application Insights, which provides Launch Wizard with more visibility and insight into the
  service through functionality such as monitoring and data analysis.
- `route53` – Allows changing and listing resource record
  sets, listing hosted zones, and listing hosted zones by name. This is
  required so that scripts running on instances in your account for SAP
  deployments can perform these actions.
- `s3` – Allows all get or list operations for all
  resources, and allows for creation, deletion, and getting objects from a
  bucket, and putting objects in a bucket for certain Launch Wizard and SAP resources.
  This is required so that the Launch Wizard service can both view and update buckets
  and contents in Amazon S3 for tasks such as reading and storing scripts that are
  run on instances in its deployments.
- `kms` – Allows listing all AWS KMS keys and aliases. This
  is required so that Launch Wizard can view keys and aliases in your account.
- `cloudwatch` – Allows all get, list, or describe actions
  for all resources, and allows Launch Wizard alarms and instance profiles to be
  created, updated, deleted, or described. This is required so that Launch Wizard can
  create and manage alarms to track metrics.
- `ec2` – Allows creation of all security groups,
  authorization of ingress rules for all security groups, all get or describe
  operations, and creation of all VPCs, NAT/internet gateways, subnets,
  routes/route tables, and key pairs. Allows instances from the CloudFormation stacks
  in Launch Wizard deployments to be stopped or terminated. Allows anything called from
  the Launch Wizard endpoint to perform other Amazon EC2 actions. This is required so that
  all EC2-related resources deployed from the Launch Wizard CloudFormation stacks can be
  appropriately created and managed.
- `cloudformation` – Allows all Launch Wizard and CloudWatch Application Insights CloudFormation
  stacks to be described and listed. Allows all get operations, all resources
  to be signaled, and all Launch Wizard stacks to be deleted. Allows all stacks to be
  created, and allows describe account limits, describe stack drift detection
  status, all list operations, and tagging of resources with all tag keys,
  starting with "LaunchWizard". This is required so that Launch Wizard can create
  CloudFormation stacks in your account, so that the stacks are appropriately
  signaled, and so that you can view and delete those stacks.
- `iam` – Allows Launch Wizard EC2 roles and instance profiles to
  be created and deleted and attached/detached. Allows Launch Wizard EC2 and AWS Lambda
  roles and instance profiles to be passed a role as long as it is passed to
  Lambda or EC2. Allows get operations for all roles or policies, all list
  operations, and all roles linked to Amazon EC2 Auto Scaling, CloudWatch Application Insights, or
  Amazon EventBridge to be created. This is required so that Launch Wizard can create necessary
  roles and attach the appropriatepolicies to them to ensure that resources in
  the Launch Wizard CloudFormation stacks and elsewhere in the service have the appropriate
  permissions.
- `autoscaling` – Allows Launch Wizard Auto Scaling groups, launch
  configurations, and associated tags, to be created, deleted, and updated.
  This is required so that the Launch Wizard SQL CloudFormation stacks can perform these
  actions for the RDGW nodes in its deployments.
- `logs` – Allows log groups with names beginning with
  `LaunchWizard` to be created and deleted. Allows log streams,
  log events, and tags to be created, listed, and deleted for log groups with
  names that begin with `LaunchWizard`. This is required so that
  Launch Wizard can publish logs to your account so that a you can view the events from
  their deployments.
- `sns` – Allows Launch Wizard Amazon SNS topics to be created, deleted,
  subscribed to, and unsubscribed from. Allows all Amazon SNS subscriptions to be
  listed and messages to be published. This is required so that the Launch Wizard Amazon SNS
  queues to send signals between resources and Launch Wizard Lambda functions know when
  to proceed with steps in their event-based workflows.
- `resource-groups` – Allows resource groups whose names
  begin with "LaunchWizard" to be created, deleted, or listed. This is
  required so that Launch Wizard resources can be grouped together in a resource group,
  and so that the groups can be viewed or deleted.
- `ds` – Allows creation and deletion of a Microsoft
  Active Directory, adding IP routes, and all describe operations. This is
  required so that Active Directories can be created, deleted, and viewed in
  Launch Wizard SQL Server deployments, and so that IP routes can be added to
  them.
- `sqs` – Allows all queues with "SQS" in the name to be
  tagged, listed, created, and deleted. Allows any queue attributes to be set
  and read, and for the queue URL to be read and permissions added. This is
  required so that Launch Wizard SAP deployments can have a queue in the deployment on
  which these actions can be performed.
- `elasticfilesystem` – Allows all Amazon Elastic File System (Amazon EFS)
  resources, and associated tags, to be created, deleted, and described.
  Allows mount targets to be created, deleted, and described. This is required
  so that Launch Wizard SAP deployments can create file systems in your account with
  the appropriate mount targets.
- `lambda` – Allows AWS Lambda functions with
  "LaunchWizard" in the name to be created, deleted, read, and invoked. This
  is required so that Launch Wizard SAP deployments can perform some Lambda functions at
  the end of CloudFormation stacks for configuration in your account or for
  parameter validation.
- `dynamodb` – Allows all tables with a name starting with
  "LaunchWizard" to be created, deleted, or described. This is required so
  that Launch Wizard scripts for SAP can publish events and metadata from the events of
  the running threads into a Amazon DynamoDB table in your account.
- `secretsmanager` – Allows all secrets with a name
  starting with "LaunchWizard" to be created, deleted, retrieved, and
  restored, all resources to be tagged or untagged, all resource policies to
  be created and deleted, secret version IDs to be listed, and secret values
  to be updated. Allows all random passwords to be generated and all secrets
  to be listed. This is required so that secrets can be created in your
  account to perform operations, such as decrypting a password in order to RDP
  into an instance from their deployment.
- `fsx` – Allows Amazon FSx file systems to be created by Launch Wizard.
  Allows describing file system properties, listing all tags on the Amazon FSx file
  share, adding and removing tags. Allows deleting file systems and volumes
  where tags include `LaunchWizard` in the CloudFormation stack-id
  tag.
- `servicecatalog` – Allows for the creation of
  AWS Service Catalog portfolios, products, and launch constraints.
  Allows for associated tags to be created and deleted. Allows for the
  association between a product and portfolio, and also the association
  between the IAM principal of a user and a portfolio.
- `ssm` – Allows for all get, list, tag, execute, and
  delete operations for all SSM resources. This is required so that Launch Wizard can
  create, run, and delete SSM resources on your behalf to configure your Amazon EC2
  instances for application provisioning. Allows Launch Wizard to create and delete
  associations using the `AWS-ConfigureAWSPackage` document, which
  allows AWS Data Provider for SAP installations.

###### Note

`arn:aws:s3:::launchwizard*` and
`“arn:aws:s3:::launchwizard*/*` are redundant permissions. Both
permissions are present for historical purposes and do not impact
security.

## AWS

managed policy: AmazonEC2RolePolicyForLaunchWizard

This policy grants administrative permissions that allow all AWS Launch Wizard actions to
be performed. To view the managed policy content, see the [AmazonEC2RolePolicyForLaunchWizard](../../../aws-managed-policy/latest/reference/AmazonEC2RolePolicyForLaunchWizard.md "../../../aws-managed-policy/latest/reference/AmazonEC2RolePolicyForLaunchWizard.md") page in the _AWS Managed
Policy Reference Guide_.

**Permissions details**

This policy includes the following permissions.

- `launchwizard` – Allows all Launch Wizard actions.
- `ec2` – Allows starting, stopping, and rebooting
  instances, and attaching volumes to all instances with the
  `LaunchWizardResourceGroupID` tag. Allows replacing route
  table for all instances with the `LaunchWizardApplicationType`
  resource tag. Allows all resources to describe and associate IP addresses,
  describe instances, images, Regions, volumes, and route tables, and modify
  instance attributes for all resources. Allows creating tags and volumes for
  all resources with the `LaunchWizardResourceType` or
  `LaunchWizardResourceGroupID` tags.
- `cloudwatch` – Allows for getting and writing metrics to
  CloudWatch. This is required so that CloudWatch can write logs for all resources.
- `s3` – Allows all get or list operations for all
  resources, and allows for creation, deletion, and getting objects from a
  bucket, and putting objects in a bucket for certain Launch Wizard and SAP resources.
  This is required so that the Launch Wizard service can both view and update buckets
  and contents in Amazon S3 for tasks such as reading and storing scripts that are
  run on instances in its deployments.
- `ssm` – Allows send commands to all Amazon EC2 instances with
  the `LaunchWizardApplicationType` resource tag. Allows getting a
  document. These actions are required to run the Backint install agent SSM
  document for SAP.
- `logs` – Allows all log groups or log streams for all
  write and read log events. This is required so that Launch Wizard can publish logs to
  your account so that you can view the events from their deployments.
- `cloudformation` – Allows all Launch Wizard and CloudWatch Application Insights CloudFormation
  stacks to be described and listed. Allows all get operations and for all
  resources to be signaled. This is required so that the stacks are
  appropriately signaled by CloudFormation.
- `dynamodb` – Allows all tables with a name starting with
  "LaunchWizard" to be created, deleted, or described. This is required so
  that Launch Wizard scripts for SAP can publish events and metadata from the events of
  the running threads into a Amazon DynamoDB table in your account.
- `sqs` – Allows sending and receiving messages from Amazon SQS
  queues. This is required so that Launch Wizard SAP deployments can have a queue in
  the deployment on which these actions can be performed.
- `iam` – Allows Launch Wizard EC2 roles and instance profiles to
  be created and deleted and attached/detached. Allows Launch Wizard EC2 and AWS Lambda
  roles and instance profiles to be passed a role as long as it is passed to
  Lambda or EC2. Allows get operations for all roles or policies, all list
  operations, and all roles linked to Amazon EC2 Auto Scaling, CloudWatch Application Insights, or
  Amazon EventBridge to be created. This is required so that Launch Wizard can create necessary
  roles and attach the appropriate policies to them to ensure that resources
  in the Launch Wizard CloudFormation stacks and elsewhere in the service have the
  appropriate permissions.
- `fsx` – Allows describing file systems and listing tags
  on file systems on any Amazon FSx resource tagged with the
  `LaunchWizard` tag. This is required so that Launch Wizard can
  retrieve the FSX DNS and administration endpoints to create the FCI SQL
  cluster.

## AWS Launch Wizard updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Launch Wizard since this
service began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the AWS Launch Wizard Document history page.

| Change                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Date               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AmazonEC2RolePolicyForLaunchWizard](../../../aws-managed-policy/latest/reference/AmazonEC2RolePolicyForLaunchWizard.md "../../../aws-managed-policy/latest/reference/AmazonEC2RolePolicyForLaunchWizard.md") – Policy<br>update | AWS Launch Wizard added a new permission to the policy for the<br>`InstallBackintForAWSBackup` Systems Manager document. It<br>enables the Systems Manager document to install AWS Backint agent for<br>AWS Backup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | September 25, 2024 |
| [AmazonLaunchWizardFullAccessV2](#security-iam-awsmanpol-AmazonLaunchWizardFullAccessV2 "#security-iam-awsmanpol-AmazonLaunchWizardFullAccessV2") – New<br>policy                                                                | AWS Launch Wizard added this new policy to replace the<br>`AmazonLaunchWizard_Fullaccess` policy. This policy<br>grants administrative permissions that allow full access to Launch Wizard and<br>other required services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | September 1, 2023  |
| AmazonLaunchWizard_Fullaccess – Policy<br>deprecation                                                                                                                                                                            | This policy has been replaced by<br>`AmazonLaunchWizardFullAccessV2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | August 23, 2023    |
| AmazonLaunchWizard_Fullaccess<br>– Update to an existing policy                                                                                                                                                                  | • AWS Launch Wizard added permissions to create or update tags<br>for Auto Scaling groups with the<br>`arn:aws:autoscaling:*:*:autoScalingGroup:*:autoScalingGroupName/LaunchWizard*`<br>resource.<br>• AWS Launch Wizard added new permissions to support creating and<br>deleting tags for Amazon Elastic File System (Amazon EFS) resources called<br>through `launchwizard.amazonaws.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | February 23, 2023  |
| AmazonLaunchWizard_Fullaccess<br>– Update to an existing policy                                                                                                                                                                  | • AWS Launch Wizard added new policies to support creating and<br>deleting tags for log groups with the<br>`arn:aws:logs:*:*:log-group:LaunchWizard*`<br>resource, called through<br>`launchwizard.amazonaws.com`.<br>• AWS Launch Wizard added new policies to support creating and<br>deleting tags for AWS Service Catalog resources with the<br>`arn:aws:servicecatalog:*:*:*/*` or<br>`arn:aws:catalog:*:*:*/*` resource,<br>called through<br>`launchwizard.amazonaws.com`.<br>• AWS Launch Wizard added permissions to create and delete<br>associations that run the<br>`AWS-ConfigureAWSPackage` document when<br>they are called through<br>`launchwizard.amazonaws.com`. This allows<br>Launch Wizard to create associations that will install the AWS<br>Data Provider for SAP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | January 12, 2023   |
| [AmazonEC2RolePolicyForLaunchWizard](#security-iam-awsmanpol-AmazonEC2RolePolicyForLaunchWizard "#security-iam-awsmanpol-AmazonEC2RolePolicyForLaunchWizard") – Update<br>to an existing policy                                  | • AWS Launch Wizard added new policies to support FSx creation<br>with Launch Wizard to support SQL Server ONTAP. AWS Launch Wizard will<br>perform the<br>`fsx:DescribeStorageVirtualMachines`<br>action on all resources created by Launch Wizard with<br>`LaunchWizard*` in the tag when they are<br>called via `launchwizard.amazonaws.com` to<br>enable this support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | May 17, 2022       |
| AmazonLaunchWizard_Fullaccess<br>– Update to an existing policy                                                                                                                                                                  | • AWS Launch Wizard restricted `ssm` actions to only<br>documents containing the `LaunchWizard`<br>prefix and called by the Launch Wizard service to<br>improve the security of this managed policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | April 12, 2022     |
| AmazonLaunchWizard_Fullaccess<br>– Update to an existing policy                                                                                                                                                                  | • AWS Launch Wizard restricted `ssm:sendCommand`<br>actions to only the<br>`arn:aws:ec2:*:*:instance/*` resource and<br>to resources with the tag keys<br>`aws:cloudformation:stack-id` to improve<br>the security of this managed policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | February 9, 2022   |
| \*_AmazonLambdaRoleForLaunchWizard_<br>• – Policy<br>deprecation                                                                                                                                                                 | • AWS Launch Wizard deprecated the<br>`AmazonLambdaRoleForLaunchWizard` policy<br>because it is no longer used by the service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | February 7, 2022   |
| [AmazonEC2RolePolicyForLaunchWizard](#security-iam-awsmanpol-AmazonEC2RolePolicyForLaunchWizard "#security-iam-awsmanpol-AmazonEC2RolePolicyForLaunchWizard") – Update<br>to an existing policy                                  | • AWS Launch Wizard restricted the `ec2:CreateTags`<br>and `ec2:CreateVolume` actions to the<br>`arn:aws:ec2:*:*:volume/*` resource to<br>prohibit tagging of other resources with the tag keys<br>`LaunchWizardResourceGroupID` and<br>`LaunchWizardApplicationType` to improve<br>the security of the managed policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | February 7, 2022   |
| AmazonLaunchWizard_Fullaccess<br>– Update to an existing policy                                                                                                                                                                  | • AWS Launch Wizard added new policies to support the creation of<br>AWS Service Catalog portfolios and products<br>with Launch Wizard. AWS Launch Wizard will perform<br>`servicecatalog:CreatePortfolio`,<br>`servicecatalog:DescribePortfolio`,<br>`servicecatalog:CreateConstraint`,<br>`servicecatalog:CreateProduct`,<br>`servicecatalog:AssociatePrincipalWithPortfolio`,<br>`servicecatalog:CreateProvisioningArtifact`,<br>and `servicecatalog:AssociateProductWithPortfolio` actions on AWS Service Catalog<br>resources when they are called by Launch Wizard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | August 30, 2021    |
| [AmazonEC2RolePolicyForLaunchWizard](#security-iam-awsmanpol-AmazonEC2RolePolicyForLaunchWizard "#security-iam-awsmanpol-AmazonEC2RolePolicyForLaunchWizard") – Update<br>to an existing policy                                  | • AWS Launch Wizard added new policies to support FSx creation<br>with Launch Wizard. AWS Launch Wizard will perform<br>`fsx:DescribeFileSystems` and<br>`fsx:ListTagsforResource` actions on all<br>resources created by Launch Wizard with<br>`LaunchWizard*` in the tag when they are<br>called via `launchwizard.amazonaws.com` to<br>enable this support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | May 21 2021        |
| AmazonLaunchWizard_Fullaccess<br>– Update to an existing policy                                                                                                                                                                  | • AWS Launch Wizard added new permissions to allow<br>`PlacementGroup` for SAP HANA scale-out<br>scenarios. AWS Launch Wizard will perform<br>`ec2:ModifyInstancePlacement`,<br>`ec2:DeletePlacementGroup`, and<br>`ec2CreatePlacementGroup` actions on the<br>database instances (in HANA and NetWeaver on HANA<br>scenarios) in your account when they are called via<br>`launchwizard.amazonaws.com` to enable<br>this support.<br>• AWS Launch Wizard added new permissions to create an SNS topic<br>in your account, and subscribe to it, unsubscribe from<br>it, and delete it. Permissions are restricted only to<br>resources whose names begin with "Launch Wizard."<br>AWS Launch Wizard will perform `sns:CreateTopic`,<br>`sns:DeleteTopic`,<br>`sns:Subscribe`, and<br>`sns:Unsubscribe` actions in your account<br>when they are called via<br>`launchwizard.amazonaws.com` to enable<br>this support.<br>• AWS Launch Wizard added new permissions to perform FSx<br>operations to support SQL Server FCI on AWS Launch Wizard. Launch Wizard<br>will perform `fsx:CreateFileSystem`,<br>`fsx:DescribeFileSystem`,<br>`fsx:ListTagsForResource`,<br>`fsx:TagResource`, and<br>`fsx:UntagResource` actions in your<br>account when they are called via<br>`launchwizard.amazonaws.com` to enable<br>this support.<br>• AWS Launch Wizard added a new permission to perform AWS Secrets Manager<br>operations to support retrieving secret values from<br>Secrets Manager on AWS Launch Wizard. Launch Wizard will perform the<br>`arn:aws:secretsmanager:*:secret:LaunchWizard*`<br>action in your account when they are called via<br>`launchwizard.amazonaws.com` to enable<br>this support. | April 30, 2021     |
| AWS Launch Wizard started tracking<br>changes                                                                                                                                                                                    | AWS Launch Wizard started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | April 30, 2021     |
