# Transition to using

Instance Metadata Service Version 2

If you want to migrate your instances so that local code or users must use Instance Metadata Service Version 2
(IMDSv2), we recommend that you use the following tools and transition
path.

###### Topics

- [Tools for helping with the
  transition to IMDSv2](#tools-for-transitioning-to-imdsv2 "#tools-for-transitioning-to-imdsv2")
- [Recommended path to
  requiring IMDSv2](#recommended-path-for-requiring-imdsv2 "#recommended-path-for-requiring-imdsv2")

## Tools for helping with the

transition to IMDSv2

If your software uses IMDSv1, use the following tools to help
reconfigure your software to use IMDSv2.

**AWS software**

The latest versions of the AWS CLI and AWS SDKs support IMDSv2. To use
IMDSv2, make sure that your EC2 instances have the latest
versions of the CLI and SDKs. For information about updating the CLI,
see [Installing or
updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
_AWS Command Line Interface User Guide_.

All Amazon Linux 2 and Amazon Linux 2023 software packages support
IMDSv2. In Amazon Linux 2023, IMDSv1 is disabled by
default.

For the minimum AWS SDK versions that support IMDSv2,
see [Use a supported AWS
SDK](configuring-instance-metadata-service.md#use-a-supported-sdk-version-for-imdsv2 "configuring-instance-metadata-service.md#use-a-supported-sdk-version-for-imdsv2").

**IMDS Packet Analyzer**

The IMDS Packet Analyzer is an open-sourced tool that identifies and logs
IMDSv1 calls from your instance’s boot phase. This can assist in
identifying the software making IMDSv1 calls on EC2 instances,
allowing you to pinpoint exactly what you need to update to get your
instances ready to use IMDSv2 only. You can run IMDS Packet
Analyzer from a command line or install it as a service. For more
information, see [AWS
ImdsPacketAnalyzer](https://github.com/aws/aws-imds-packet-analyzer "https://github.com/aws/aws-imds-packet-analyzer") on _GitHub_.

**CloudWatch**

IMDSv2 uses token-backed sessions, while IMDSv1
does not. The `MetadataNoToken` CloudWatch metric tracks the
number of calls to the Instance Metadata Service (IMDS) that are using
IMDSv1. By tracking this metric to zero, you can determine
if and when all of your software has been upgraded to use
IMDSv2.

After you've disabled IMDSv1, you can use the
`MetadataNoTokenRejected` CloudWatch metric to track the
number of times an IMDSv1 call was attempted and rejected.
By tracking this metric, you can ascertain whether your software
needs to be updated to use IMDSv2.

For more information, see [Instance metrics](viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics "viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics").

**Updates to EC2 APIs and CLIs**

For new instances, you can use the [RunInstances](../APIReference/API_RunInstances.md "../APIReference/API_RunInstances.md")
API to launch new instances that require the use of IMDSv2.
For more information, see [Configure instance metadata options
for new instances](configuring-IMDS-new-instances.md "configuring-IMDS-new-instances.md").

For existing instances, you can use the [ModifyInstanceMetadataOptions](../APIReference/API_ModifyInstanceMetadataOptions.md "../APIReference/API_ModifyInstanceMetadataOptions.md") API to require the use of
IMDSv2. For more information, see [Modify instance metadata
options for existing instances](configuring-IMDS-existing-instances.md "configuring-IMDS-existing-instances.md").

To require the use of IMDSv2 on all new instances launched
by Amazon EC2 Auto Scaling groups, your Amazon EC2 Auto Scaling groups can use either a launch template or
a launch configuration. When you [create a launch template](../../../cli/latest/reference/ec2/create-launch-template.md "../../../cli/latest/reference/ec2/create-launch-template.md") or [create a launch configuration](../../../cli/latest/reference/autoscaling/create-launch-configuration.md "../../../cli/latest/reference/autoscaling/create-launch-configuration.md"), you must configure the
`MetadataOptions` parameters to require the use of
IMDSv2. The Amazon EC2 Auto Scaling group launches new instances using the new
launch template or launch configuration, but existing instances are
not affected. For existing instances in an Amazon EC2 Auto Scaling group, you can use
the [ModifyInstanceMetadataOptions](../APIReference/API_ModifyInstanceMetadataOptions.md "../APIReference/API_ModifyInstanceMetadataOptions.md") API to require the use of
IMDSv2 on the existing instances, or terminate the instances
and the Amazon EC2 Auto Scaling group will launch new replacement instances with the
instance metadata options settings that are defined in the new
launch template or launch configuration.

**Use an AMI that configures IMDSv2 by
default**

When you launch an instance, you can automatically configure it to
use IMDSv2 by default (the `HttpTokens` parameter
is set to `required`) by launching it with an AMI that is
configured with the `ImdsSupport` parameter set to
`v2.0`. You can set the `ImdsSupport`
parameter to `v2.0` when you register the AMI using the
[register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") CLI command, or you can modify an
existing AMI by using the [modify-image-attribute](../../../cli/latest/reference/ec2/modify-image-attribute.md "../../../cli/latest/reference/ec2/modify-image-attribute.md") CLI command. For more
information, see [Configure
the AMI](configuring-IMDS-new-instances.md#configure-IMDS-new-instances-ami-configuration "configuring-IMDS-new-instances.md#configure-IMDS-new-instances-ami-configuration").

**IAM policies and SCPs**

You can use an IAM policy or AWS Organizations service control policy (SCP)
to control users as follows:

- Can't launch an instance using the [RunInstances](../APIReference/API_RunInstances.md "../APIReference/API_RunInstances.md") API unless the instance is
  configured to use IMDSv2.
- Can't modify a running instance using the [ModifyInstanceMetadataOptions](../APIReference/API_ModifyInstanceMetadataOptions.md "../APIReference/API_ModifyInstanceMetadataOptions.md") API to re-enable
  IMDSv1.

The IAM policy or SCP must contain the following IAM condition
keys:

- `ec2:MetadataHttpEndpoint`
- `ec2:MetadataHttpPutResponseHopLimit`
- `ec2:MetadataHttpTokens`

If a parameter in the API or CLI call does not match the state
specified in the policy that contains the condition key, the API or
CLI call fails with an `UnauthorizedOperation`
response.

Furthermore, you can choose an additional layer of protection to
enforce the change from IMDSv1 to IMDSv2. At the
access management layer with respect to the APIs called via EC2 Role
credentials, you can use a new condition key in either IAM
policies or AWS Organizations service control policies (SCPs). Specifically,
by using the condition key `ec2:RoleDelivery` with a
value of `2.0` in your IAM policies, API calls made with
EC2 Role credentials obtained from IMDSv1 will receive an
`UnauthorizedOperation` response. The same thing can
be achieved more broadly with that condition required by an SCP.
This ensures that credentials delivered via IMDSv1 cannot
actually be used to call APIs because any API calls not matching the
specified condition will receive an
`UnauthorizedOperation` error.

For example IAM policies, see [Work with instance metadata](ExamplePolicies_EC2.md#iam-example-instance-metadata "ExamplePolicies_EC2.md#iam-example-instance-metadata"). For more
information on SCPs, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.

## Recommended path to

requiring IMDSv2

Using the above tools, we recommend that you follow this path for
transitioning to IMDSv2.

### Step 1: At the start

Update the SDKs, CLIs, and your software that use Role credentials on
their EC2 instances to versions compatible with IMDSv2. For more
information about updating the CLI, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
in the _AWS Command Line Interface User Guide_.

Then, change your software that directly accesses instance metadata (in
other words, that does not use an SDK) using the IMDSv2 requests.
You can use the [IMDS Packet Analyzer](https://github.com/aws/aws-imds-packet-analyzer "https://github.com/aws/aws-imds-packet-analyzer") to identify the software that you need to
change to use IMDSv2 requests.

### Step 2: Track your transition progress

Track your transition progress by using the CloudWatch metric
`MetadataNoToken`. This metric shows the number of
IMDSv1 calls to the IMDS on your instances.
For more information, see [Instance metrics](viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics "viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics").

### Step 3: When there is zero IMDSv1

usage

When the CloudWatch metric `MetadataNoToken` records zero
IMDSv1 usage, your instances are
ready to be fully transitioned to using IMDSv2. At this stage, you
can do the following:

- **Account default**

You can set IMDSv2 to be required as an account default.
When an instance is launched, the instance configuration is
automatically set to the account default.

To set the account default, do the following:

    + Amazon EC2 console: On the EC2 Dashboard, under
     **Account attributes**, **Data
     protection and security**, for **IMDS
     defaults**, set **Instance metadata
     service**  to **Enabled** and
     **Metadata version** to **V2
     only (token required)**. For more information,
     see [Set IMDSv2 as the
     default for the account](configuring-IMDS-new-instances.md#set-imdsv2-account-defaults "configuring-IMDS-new-instances.md#set-imdsv2-account-defaults").
    + AWS CLI: Use the [modify-instance-metadata-defaults](../../../cli/latest/reference/ec2/modify-instance-metadata-defaults.md "../../../cli/latest/reference/ec2/modify-instance-metadata-defaults.md") CLI command
     and specify `--http-tokens required` and
     `--http-put-response-hop-limit
     `2``.

- **New instances**

When launching a new instance, you can do the following:

    + Amazon EC2 console: In the launch instance wizard, set
     **Metadata accessible** to
     **Enabled** and **Metadata
     version** to **V2 only (token
     required)**. For more information, see [Configure
     the instance at launch](configuring-IMDS-new-instances.md#configure-IMDS-new-instances-instance-settings "configuring-IMDS-new-instances.md#configure-IMDS-new-instances-instance-settings").
    + AWS CLI: Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command and specify that
     IMDSv2 is required.

- **Existing instances**

For existing instances, you can do the following:

    + Amazon EC2 console: On the **Instances** page,
     select your instance, choose **Actions**,
     **Instance settings**, **Modify
     instance metadata options**, and for
     **IMDSv2**, choose
     **Required**. For more information, see
     [Require the use of IMDSv2](configuring-IMDS-existing-instances.md#modify-require-IMDSv2 "configuring-IMDS-existing-instances.md#modify-require-IMDSv2").
    + AWS CLI: Use the [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") CLI command to
     specify that only IMDSv2 is to be used.

You can modify the instance metadata options on running instances,
and you don't need to restart the instances after modifying the
instance metadata options.

### Step 4: Check if your instances are

transitioned to IMDSv2

You can check if any instances are not yet configured to require the use
of IMDSv2, in other words, IMDSv2 is still configured as
`optional`. If any instances are still configured as
`optional`, you can modify the instance metadata options to
make IMDSv2 `required` by repeating the preceding [Step 3](#path-step-3 "#path-step-3").

To filter your instances:

- Amazon EC2 console: On the **Instances** page, filter
  your instances by using the **IMDSv2 = optional**
  filter. For more information about filtering, see [Filter resources using the console](Using_Filtering.md#console-filter "Using_Filtering.md#console-filter"). You
  can also view whether IMDSv2 is required or optional for
  each instance: In the **Preferences** window,
  toggle on **IMDSv2** to add the
  **IMDSv2** column to the
  **Instances** table.
- AWS CLI: Use the [describe-instances](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") command and filter by
  `metadata-options.http-tokens = optional`, as
  follows:

```
aws ec2 describe-instances --filters "Name=metadata-options.http-tokens,Values=optional" --query "Reservations[*].Instances[*].[InstanceId]" --output text
```

### Step 5: When all of your instances are

transitioned to IMDSv2

The `ec2:MetadataHttpTokens`,
`ec2:MetadataHttpPutResponseHopLimit`, and
`ec2:MetadataHttpEndpoint` IAM condition keys can be used to
control the use of the [RunInstances](../APIReference/API_RunInstances.md "../APIReference/API_RunInstances.md") and the [ModifyInstanceMetadataOptions](../APIReference/API_ModifyInstanceMetadataOptions.md "../APIReference/API_ModifyInstanceMetadataOptions.md") APIs and corresponding CLIs. If a
policy is created, and a parameter in the API call does not match the state
specified in the policy using the condition key, the API or CLI call fails
with an `UnauthorizedOperation` response. For example IAM
policies, see [Work with instance metadata](ExamplePolicies_EC2.md#iam-example-instance-metadata "ExamplePolicies_EC2.md#iam-example-instance-metadata").

Furthermore, after you've disabled IMDSv1, you can use the
`MetadataNoTokenRejected` CloudWatch metric to track the number of
times an IMDSv1 call was attempted and rejected. If, after disabling
IMDSv1, you have software that is not working properly and the
`MetadataNoTokenRejected` metric records IMDSv1
calls, it's likely that this software needs to be updated to use
IMDSv2.
