# 1-click setup for AWS Config

AWS Config **1-click setup** helps simplify the getting started process for
AWS Config console customers by reducing the number of manual selections. To go through all the
manual selections of the setup process, see [Manual setup](detailed-setup.md "detailed-setup.md").

###### To set up AWS Config with the console using **1-click setup**

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **1-click setup**.
   The set up page includes three steps, but through the **1-click setup**
   workflow, you are automatically directed to Step 3 (Review). The following provides a
   breakdown of that procedure.

- **Settings**: To select the manner by which the AWS Config console
  records resources and roles, and choose where configuration history and
  configuration snapshot files are sent.
- **Rules**: For AWS Regions that support AWS Config rules, this step
  is available for you to configure initial managed rules that you can add to your
  account. After setting up, AWS Config will evaluate your AWS resources against the rules
  that you chose. Additional rules can be created and existing ones can be updated in
  your account after setup.
- **Review**: To verify your setup details.

## Step 1: Settings

### Recording

strategy

The option to record **All resource types with customizable
overrides** is selected for you. AWS Config will record all current and
future supported resource types in this Region. For more information, see [Supported Resource
Types](resource-config-reference.md "resource-config-reference.md").

- **Default settings**

The default recording frequency is set to **Continuous**
for you. This means AWS Config records configuration changes continuously whenever
a change occurs.

AWS Config also supports the option to set the recording frequency to
**Daily**. If you select this option after setup, you
will receive a configuration item (CI) representing the most recent state of
your resources over the last 24-hour period, only if it’s different from the
previous CI recorded. For more information see, [Recording Frequency](select-resources.md#select-resources-recording-frequency "select-resources.md#select-resources-recording-frequency").

###### Note

AWS Firewall Manager depends on continuous recording to monitor your resources.
If you are using Firewall Manager, it is recommended that you set the recording
frequency to Continuous.

- **Override settings –
  _optional_**

Optionally, after setup you can override the record frequency for specific
resource types, or exclude specific resource types from recording. To
override the default settings, choose **Settings** in the
left navigation of the AWS Config console, and then choose
**Edit**.

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
If you want to avoid the increased activity from running ephemeral workloads,
you can set up the configuration recorder to exclude these resource types from
being recorded, or run these types of workloads in a separate account with AWS Config
turned off to avoid increased configuration recording and rule
evaluations.

**Global resource types | Aurora global clusters are initially
included in recording**

The `AWS::RDS::GlobalCluster` resource type will be recorded in all
supported AWS Config Regions where the configuration recorder is enabled.

If you do not want to record `AWS::RDS::GlobalCluster` in all
enabled Regions, you can exclude this resource type from recording after setup.
Choose **Settings** in the left navigation bar, and then
choosing **Edit**. From **Edit**, go to
**Override settings** in the **Recording
method** section, choose `AWS::RDS::GlobalCluster`, and
choose the override "Exclude from recording".

**Global resource types | IAM resource types are initially excluded
from recording**

"All globally recorded IAM resource types" are initially excluded from
recording to help you reduce costs. This bundle includes IAM users, groups,
roles, and customer managed policies. Choose **Remove** to
remove the override and include these resources in your recording.

Additionally, the global IAM resource types (`AWS::IAM::User`,
`AWS::IAM::Group`, `AWS::IAM::Role`, and
`AWS::IAM::Policy`) cannot be recorded in Regions supported by
AWS Config after February 2022. For a list of those Regions, see [Recording AWS Resources | Global Resources](select-resources.md#select-resources-all "select-resources.md#select-resources-all").

### Data governance

The default data retention period to retain AWS Config data for 7 years (2557 days) is
selected for you in this section.

The option to **Use an existing AWS Config service-linked role** is
selected for you and set to the **AWS Config role**. Service-linked roles
are predefined by AWS Config and include all the permissions that the service requires to
call other AWS services.

### Delivery method

The option to **Choose a bucket from your account** is selected for you in this section. This selection will default to the
bucket in your account that is named in the format
`config-bucket-`accountid``. For
 example, `config-bucket-012345678901`. If you don't have a bucket created
in that format, one will be created for you. If you want to create your own bucket,
see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in
the _Amazon Simple Storage Service User Guide_.

For more information about S3
buckets,
see [Buckets overview](../../../AmazonS3/latest/userguide/UsingBucket.md "../../../AmazonS3/latest/userguide/UsingBucket.md") in the
_Amazon Simple Storage Service User Guide_.

## Step 2: Rules

Under **AWS Managed Rules**, no rules are selected for you at this
step. Instead, you are encouraged to create and update rules after you have finished setting
up your account.

## Step 3: Review

Review your AWS Config setup details. You can go back to edit changes for each section.
Choose **Confirm** to finish setting up AWS Config.
