# Using drift-aware change sets

Drift-aware change sets are enhanced CloudFormation change sets that allow you to identify and
manage stack drift in a safe manner. Stacks drift from their expected template configuration
when stack resources are changed outside CloudFormation, using the AWS Management Console, AWS CLI, or SDK of
underlying services. Drift-aware change sets compare templates with the actual state of your
stack resources and bring drifted resources in line with their template definitions. When the
template definition of a resource is updated to match its actual state, drift-aware change sets
reset the drift status of the resource without modifying the resource.

The benefits of using drift-aware change sets include:

- Preview overwrites of drift – Detect whether a
  deployment will revert critical out-of-band changes made during incident response.
- Systematic drift reconciliation – Safely align
  drifted resources with compliant template definitions, either by overwriting drifted
  properties with template values or updating the template to match actual resource
  state.
- Enhanced rollback capabilities – If a deployment
  fails, restore resources to their actual pre-deployment state, not the previous template
  state.
- Complete visibility – See exactly how your
  deployment will affect actual resource configurations before making changes.
  Traditional change sets provide a comparison of your new template with the previous template
  for a stack, but do not account for stack drift. Drift-aware change sets solve this problem by
  providing a three-way comparison between:

- **Actual state** – The live configuration of your resources.
  CloudFormation will read the configuration of resources in your account at the time of change
  set creation via underlying service APIs.
- **Previous deployment state** – The configuration defined in the
  template from your last CloudFormation deployment.
- **Desired state** – The configuration defined in your new
  template.
  Drift-aware change sets will update the actual state of all stack resources to match the
  desired state, even if a resource was not explicitly changed in the template.

## Considerations

- Resource type support – Drift-aware change sets
  support a comparison of the desired state with the actual state for hundreds of resource
  types. For unsupported resource types, drift-aware change sets fall back to comparing the
  previous deployment state with the desired state. See the Supported Resource Types section
  for details.
- Write-only properties – For properties
  containing sensitive data (passwords, secrets), drift-aware change sets compare against
  previous deployment values rather than actual values.
- AWS-managed properties – Drift-aware change
  sets preserve out-of-band changes made by AWS services to managed properties, such as
  the desired capacity of an Auto Scaling group. See the AWS-managed properties section for
  details.
- External tag keys – Drift-aware change sets do
  not remove or modify tag keys that were not specified in the template, preventing
  conflicts with attribute-based access control (ABAC) systems.
- Replacement of drifted resources – Drift-aware
  change sets do not support drift reconciliation for immutable properties.
- Cross-stack attachments – Some resource types,
  such as `AWS::IAM::Policy`, can influence the actual state of other resource
  types, such as `AWS::IAM::Role`. Drift-aware change sets handle attachment of
  resources within a stack. If a resource is modified via attachment of a secondary resource
  from a different stack, drift-aware change sets will detect the modification as drift and
  can revert the attachment. Popular attachable resources include
  `AWS::IAM::Policy`, `AWS::IAM::ManagedPolicy`,
  `AWS::EC2::SecurityGroupIngress`, and
  `AWS::EC2::SecurityGroupEgress`.

## AWS-managed properties

You can configure specific resource properties for active AWS management. For example,
you can allow Amazon Relational Database Service (Amazon RDS) to automatically upgrade the minor engine version of an Amazon RDS
table. These changes can show up as stack drift in CloudFormation. Drift-aware change sets
recognize that drift is expected for AWS-managed properties and leave their actual value
untouched if you have not modified the property in their template. Top examples of
AWS-managed properties are:

- Enabling the `AutoMinorVersionUpgrade` property of an Amazon RDS table to allow
  automatic updates of engine version.
- Using the `AWS::ApplicationAutoScaling::ScalableTarget` resource to enable
  auto-scaling for properties such as the read/write capacity units of an Amazon DynamoDB table
  and the desired count of an Amazon Elastic Container Service cluster.
- Using the `AWS::AutoScaling::ScalingPolicy` for Auto Scaling groups.

Drift-aware change sets clarify the properties which were identified as AWS-managed. See
the AWS CLI section for details.

## Using drift-aware change sets

(console)

You can create and manage drift-aware change sets through the CloudFormation console using the
same workflow as traditional change sets, with additional options for deployment modes.

### Creating drift-aware change

sets

###### To create a drift-aware

change set (console)

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **Stacks** page, select the stack that you want to
   update.
3. Choose **Stack actions**, and then choose **Create change
   set for current stack**.
4. On the **Create change set** page, for **Change set
   type**, choose **Drift aware change set**.
5. Choose **Create change set**.
6. On the change set details page, review the three-way comparison showing actual,
   previous deployment, and desired state for each affected resource.
7. If you're satisfied with the changes, choose **Execute change
   set**.

### Reviewing drift-aware change

sets

When you view a drift-aware change set in the console, you'll see enhanced information
compared to traditional change sets:

- Stack drift status – Indicates whether the
  stack has drifted from its last deployment.
- Property comparison – Shows a JSON diff
  between the actual and desired state of an affected resource.
- Drift indicators – Clearly marks properties
  within the JSON diff that have drifted. Click on **View drift** to see
  the previous deployment value for a property.
- Value source indicators – Shows whether before
  values for a property come from actual state or previous deployment state.

## Using drift-aware change sets (AWS CLI)

You can create and manage drift-aware change sets using the AWS CLI by adding the
`--deployment-mode REVERT_DRIFT` parameter to the
**create-change-set** command.

### Creating drift-aware change

sets

###### To create a drift-aware change set

Use the [create-change-set](../../../cli/latest/reference/cloudformation/create-change-set.md "../../../cli/latest/reference/cloudformation/create-change-set.md") command with the `--deployment-mode REVERT_DRIFT`
parameter to create a drift-aware change set.

```
aws cloudformation create-change-set \
  --stack-name `my-stack` \
  --change-set-name `my-drift-aware-changeset` \
  --template-body `file://updated-template.yaml` \
  --deployment-mode REVERT_DRIFT \
  --capabilities `CAPABILITY_IAM`
```

### Reviewing drift-aware change

sets

###### To review the details of a drift-aware change set

Use the [describe-change-set](../../../cli/latest/reference/cloudformation/describe-change-set.md "../../../cli/latest/reference/cloudformation/describe-change-set.md") command to review the details of a drift-aware change
set:

```
aws cloudformation describe-change-set \
  --change-set-name `my-drift-aware-changeset` \
  --stack-name `my-stack`
```

The response includes enhanced information for drift-aware change sets:

- `StackDriftStatus` – Shows whether the stack has drifted
  (`DRIFTED`, `IN_SYNC`, `NOT_CHECKED`, or
  `UNKNOWN`).
- `ResourceDriftStatus` – Shows the drift status for each resource
  (`DELETED`, `MODIFIED`, `IN_SYNC`, or
  `NOT_CHECKED`).
- `BeforeValueFrom` – Indicates whether the before value for a
  property comes from `ACTUAL_STATE` or
  `PREVIOUS_DEPLOYMENT_STATE`.
- `Drift` – Contains the drift details for a property including
  `PreviousValue`, `ActualValue`, and
  `DriftDetectionTimestamp`.
- `ResourceDriftIgnoredProperties` – Contains the properties of a
  resource for which the change set will not revert drift and the reasons for ignoring
  drift.

For more information, see [DescribeChangeSet](../APIReference/API_DescribeChangeSet.md "../APIReference/API_DescribeChangeSet.md") in the _AWS CloudFormation API Reference_.

### Executing drift-aware change

sets

###### To execute a drift-aware change set

After reviewing the change set, use the [execute-change-set](../../../cli/latest/reference/cloudformation/execute-change-set.md "../../../cli/latest/reference/cloudformation/execute-change-set.md")
command to apply the changes:

```
aws cloudformation execute-change-set \
  --change-set-name `my-drift-aware-changeset` \
  --stack-name `my-stack`
```

If the deployment fails, CloudFormation will roll back resources to their actual
pre-deployment state and preserve out-of-band changes made since the last deployment.

## Supported resource types

Drift-aware change sets support a three-way comparison of actual state, previous
deployment state, and desired state for all [resource types](resource-import-supported-resources.md "resource-import-supported-resources.md") that support drift
detection, except the following resource types:

- `AWS::SageMaker::MlflowTrackingServer`
- `AWS::Route53Resolver::FirewallRuleGroup`
- `AWS::MediaLive::Multiplexprogram`
- `AWS::VpcLattice::ResourceConfiguration`
- `AWS::S3::StorageLensGroup`
- `AWS::Bedrock::AgentAlias`
- `AWS::MSK::Cluster`
- `AWS::RDS::DBProxy`
- `AWS::Redshift::ClusterParameterGroup`
- `AWS::QBusiness::Index`
- `AWS::NetworkManager::CoreNetwork`
- `AWS::IAM::OIDCProvider`
- `AWS::Organizations::ResourcePolicy`
- `AWS::SNS::TopicInlinePolicy`
- `AWS::Route53::KeySigningKey`
- `AWS::DataZone::PolicyGrant`
- `AWS::Transfer::Certificate`
- `AWS::SageMaker::ImageVersion`
- `AWS::Neptune::DBParameterGroup`
- `AWS::ODB::CloudVmCluster`
- `AWS::RolesAnywhere::TrustAnchor`
- `AWS::Detective::Graph`
- `AWS::Maester::DocumentType`
- `AWS::SageMaker::ModelPackageGroup`
- `AWS::S3Express::BucketPolicy`
- `AWS::Panorama::PackageVersion`
- `AWS::S3Tables::TableBucketPolicy`

Drift-aware change sets fall back to a comparison of previous deployment state and desired
state for resources that do not support the three-way comparison.
