# Manual setup for AWS Config

With the **Get started** workflow, you can go through all the manual
selections of the setup process to get started with the AWS Config console. For a simplified
getting started process, see [1-click
setup](1-click-setup.md "1-click-setup.md").

###### To set up AWS Config with the console using **Get started**

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Get started**.
   The setup page includes three steps. The following provides a breakdown of that procedure
   after you choose **Get started**.

- **Settings**: To select the manner by which the AWS Config console
  records resources and roles, and choose where configuration history and
  configuration snapshot files are sent.
- **Rules**: For AWS Regions that support AWS Config rules, this step
  is available for you to configure initial managed rules that you can add to your
  account. After setting up, AWS Config will evaluate your AWS resources against the rules
  that you chose. Additional rules can be created and existing ones can be updated and
  in your account after setup.
- **Review**: To verify your setup details.

## Step 1: Settings

### Recording

strategy

In the **Recording method** section, choose a recording strategy.
You can specify the AWS resources that you want AWS Config to record.

All resource types with customizable overrides
Set up AWS Config to record configuration changes for all current and future
supported resource types in this Region. You can override the recording
frequency for specific resource types or exclude specific resource types
from recording. For more information, see [Supported Resource
Types](resource-config-reference.md "resource-config-reference.md").

- **Default settings**

Configure the default recording frequency for all current and
future supported resource types. For more information see,
[Recording Frequency](select-resources.md#select-resources-recording-frequency "select-resources.md#select-resources-recording-frequency").

    + Continuous recording – AWS Config will record
     configuration changes continuously whenever a change
     occurs.
    + Daily recording – You will receive a
     configuration item (CI) representing the most recent
     state of your resources over the last 24-hour period,
     only if it’s different from the previous CI recorded.

###### Note

AWS Firewall Manager depends on continuous recording to monitor your
resources. If you are using Firewall Manager, it is recommended that
you set the recording frequency to Continuous.

- **Override settings**

Override the recording frequency for specific resource types,
or exclude specific resource types from recording. If you change
the recording frequency for a resource type or stop recording a
resource type, the configuration items that were already
recorded will remain unchanged.

Specific resource types
Set AWS Config to record configuration changes for only the resource types
that you specify.

- **Specific resource types**

Choose a resource type to record and its frequency. For more
information see, [Recording Frequency](select-resources.md#select-resources-recording-frequency "select-resources.md#select-resources-recording-frequency").

    + Continuous recording – AWS Config will record
     configuration changes continuously whenever a change
     occurs.
    + Daily recording – You will receive a
     configuration item (CI) representing the most recent
     state of your resources over the last 24-hour period,
     only if it’s different from the previous CI
     recorded.

###### Note

AWS Firewall Manager depends on continuous recording to monitor your
resources. If you are using Firewall Manager, it is recommended that
you set the recording frequency to Continuous.

If you change the recording frequency for a resource type or
stop recording a resource type, the configuration items that
were already recorded will remain unchanged.

#### Considerations When Recording

Resources

**High Number of AWS Config Evaluations**

You might notice increased activity in your account during your initial month
recording with AWS Config when compared to subsequent months. During the
initial bootstrapping process, AWS Config runs evaluations on all the resources in
your account that you have selected for AWS Config to record.

If you are running ephemeral workloads, you may see increased activity from
AWS Config as it records configuration changes associated with creating and deleting
these temporary resources. An _ephemeral workload_ is a
temporary use of computing resources that are loaded and run when needed.
Examples include Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances, Amazon EMR jobs, and AWS Auto Scaling.
. If you want to avoid the increased activity from running ephemeral workloads,
you can set up the configuration recorder to exclude these resource types from
being recorded, or run these types of workloads in a separate account with AWS Config
turned off to avoid increased configuration recording and rule
evaluations.

Considerations: All resource types with customizable
overrides
**Globally recorded resource types | Aurora global
clusters are initially included in recording**

The `AWS::RDS::GlobalCluster` resource type will be
recorded in all supported AWS Config Regions where the configuration
recorder is enabled.

If you do not want to record `AWS::RDS::GlobalCluster`
in all enabled Regions, choose "AWS RDS
GlobalCluster", and choose the override "Exclude from
recording".

**Global resource types | IAM resource types are initially
excluded from recording**

The global IAM resource types are initially excluded from
recording to help you reduce costs. This bundle includes IAM
users, groups, roles, and customer managed policies. Choose
**Remove** to remove the override and include
these resources in your recording.

Additionally, the global IAM resource types
(`AWS::IAM::User`, `AWS::IAM::Group`,
`AWS::IAM::Role`, and `AWS::IAM::Policy`)
cannot be recorded in Regions supported by AWS Config after February 2022.
For a list of those Regions, see [Recording AWS Resources | Global Resources](select-resources.md#select-resources-all "select-resources.md#select-resources-all").

**Limits**

You can add up to 100 frequency overrides and 600 exclusion
overrides.

Daily recording cannot be specified for the following resource
types:

- `AWS::Config::ResourceCompliance`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ConfigurationRecorder`

Considerations: Specific resource types
**Region Availability**

Before specifying a resource type for AWS Config to track, check [Resource
Coverage by Region Availability](what-is-resource-config-coverage.md "what-is-resource-config-coverage.md") to see if the resource
type is supported in the AWS Region where you set up AWS Config. If a
resource type is supported by AWS Config in at least one Region, you can
enable the recording of that resource type in all Regions supported
by AWS Config, even if the specified resource type is not supported in the
AWS Region where you set up AWS Config.

**Limits**

No limits if all resource types have the same frequency. You can
add up to 100 resource types with Daily frequency if at least one
resource type is set to Continuous.

The Daily frequency is not supported for the following resource
types:

- `AWS::Config::ResourceCompliance`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ConfigurationRecorder`

### Data governance

- For **Data retention period**, choose either the default
  retention period to retain AWS Config data for 7 years (2557) or set a custom
  rentention period for items recorded by AWS Config.

AWS Config allows you to delete your data by specifying a retention period for
your `ConfigurationItems`. When you specify a retention period,
AWS Config retains your `ConfigurationItems` for that specified period.
You can choose a period between a minimum of 30 days and a maximum of 7
years (2557 days). AWS Config deletes data older than your specified retention
period.

- For **IAM role for AWS Config**, choose either an existing
  AWS Config service-linked role or an IAM role from your account.
  - Service-linked roles are predefined by AWS Config and include all the
    permissions that the service requires to call other AWS
    services.

  ###### Note

  **Recommended: Use the Service-linked
  role**

  It is recommended that you use the service-linked role. A
  service-linked role adds all the necessary permissions for AWS Config
  to run as expected.
  - Otherwise, choose an IAM role from one of your pre-existing
    roles and permission policies.

  ###### Note

  **Policies and compliance results**

  [IAM
  policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") and [other policies managed in AWS Organizations](../../../organizations/latest/userguide/orgs_manage_policies.md "../../../organizations/latest/userguide/orgs_manage_policies.md") can impact
  whether AWS Config has permissions to record configuration changes for
  your resources. Additionally, rules directly evaluate the
  configuration of a resource and rules don't take into account
  these policies when running evaluations. Make sure that the
  policies in effect align with how you intend to use AWS Config.

  **Keep Minimum Permisions When Reusing an IAM
  role**

  If you use an AWS service that uses AWS Config, such as AWS Security Hub
  or AWS Control Tower, and an IAM role has already been created,
  make sure that the IAM role that you use when setting up AWS Config
  keeps the same minimum permissions as the pre-existing IAM
  role. You must do this to ensure that the other AWS service
  continues to run as expected.

  For example, if AWS Control Tower has an IAM role that allows
  AWS Config to read S3 objects, make sure that the same permissions are
  granted to the IAM role you use when setting up AWS Config.
  Otherwise, it may interfere with how AWS Control Tower
  operates.

### Delivery method

- For **Delivery method**, choose the S3 bucket to which
  AWS Config sends configuration history and configuration snapshot files:
  - **Create a bucket** – For **S3
    bucket name**, type a name for your S3 bucket.

  The name that you type must be unique across all existing bucket
  names in Amazon S3. One way to help ensure uniqueness is to include a
  prefix; for example, the name of your organization. You can't change
  the bucket name after it is created. For more information, see
  [Bucket
  Restrictions and Limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the
  _Amazon Simple Storage Service User Guide_.
  - **Choose a bucket from your account** –
    For **S3 bucket name**, choose your preferred
    bucket.
  - **Choose a bucket from another account** –
    For **S3 bucket name**, type the bucket
    name.

  ###### Note

  **Bucket Permissions**

  If you choose a bucket from another account, that bucket must
  have policies that grant access permissions to AWS Config. For more
  information, see [Permissions for the Amazon S3 Bucket for the AWS Config Delivery
  Channel](s3-bucket-policy.md "s3-bucket-policy.md").

- For **Amazon SNS topic**, choose **Stream
  configuration changes and notifications to an Amazon SNS topic** to
  have AWS Config send notifications such as configuration history delivery,
  configuration snapshot delivery, and compliance.
- If you chose to have AWS Config stream to an Amazon SNS topic, choose the target
  topic:
  - **Create a topic** – For
    **Topic Name**, type a name for your SNS topic.
  - **Choose a topic from your account** – For
    **Topic Name**, select your preferred topic.
  - **Choose a topic from another account** – For
    **Topic ARN**, type the Amazon Resource Name (ARN) of the topic.
    If you choose a topic from another account, the topic must have
    policies that grant access permissions to AWS Config. For more
    information, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md "sns-topic-policy.md").

  ###### Note

  **Region for the Amazon SNS Topic**

  The Amazon SNS topic must exist in the same Region as the Region in
  which you set up AWS Config.

## Step 2: Rules

If you are setting up AWS Config in a Region that supports rules, choose
**Next**.

## Step 3: Review

Review your AWS Config set up details. You can go back to edit changes for each section.
Choose **Confirm** to finish setting up AWS Config.

## For more information

For information about looking up the existing resources in your account and
understanding the configurations of your resources, see [Looking up
Resources](looking-up-discovered-resources.md "looking-up-discovered-resources.md"), [Viewing
Compliance Informance](evaluate-config_view-compliance.md "evaluate-config_view-compliance.md"), and [Viewing
Compliance History](view-manage-resource-console.md "view-manage-resource-console.md").

You can also use Amazon Simple Queue Service to monitor AWS resources programmatically. For more
information, see [Monitoring AWS Resource Changes with
Amazon SQS](monitor-resource-changes.md "monitor-resource-changes.md").
