

# Transition to using Instance Metadata Service Version 2
<a name="instance-metadata-transition-to-version-2"></a>

If you want to configure your instances to only accept Instance Metadata Service Version 2 (IMDSv2) calls, we recommend that you use the following tools and transition path.

**Topics**
+ [Tools for transitioning to IMDSv2](#tools-for-transitioning-to-imdsv2)
+ [Recommended path to requiring IMDSv2](#recommended-path-for-requiring-imdsv2)

## Tools for transitioning to IMDSv2
<a name="tools-for-transitioning-to-imdsv2"></a>

The following tools can help you identify, monitor, and manage the transition of your software from IMDSv1 to IMDSv2. For the instructions on how to use these tools, see [Recommended path to requiring IMDSv2](#recommended-path-for-requiring-imdsv2).

**AWS software**  
The latest versions of the AWS CLI and AWS SDKs support IMDSv2. To use IMDSv2, update your EC2 instances to use the latest versions. For the minimum AWS SDK versions that support IMDSv2, see [Use a supported AWS SDK](configuring-instance-metadata-service.md#use-a-supported-sdk-version-for-imdsv2).  
All Amazon Linux 2 and Amazon Linux 2023 software packages support IMDSv2. Amazon Linux 2023 disables IMDSv1 by default.

**IMDS Packet Analyzer**  
IMDS Packet Analyzer is an open-source tool that identifies and logs IMDSv1 calls during your instance’s boot phase and runtime operations. By analyzing these logs, you can precisely identify the software making IMDSv1 calls on your instances and determine what needs to be updated to support IMDSv2 only on your instances. You can run IMDS Packet Analyzer from a command line or install it as a service. For more information, see [AWS ImdsPacketAnalyzer](https://github.com/aws/aws-imds-packet-analyzer) on *GitHub*.

**CloudWatch**  
CloudWatch provides the following two metrics for monitoring your instances:  
`MetadataNoToken` – IMDSv2 uses token-backed sessions, while IMDSv1 does not. The `MetadataNoToken` metric tracks the number of calls to the Instance Metadata Service (IMDS) that are using IMDSv1. By tracking this metric to zero, you can determine if and when all of your software has been upgraded to use IMDSv2.  
`MetadataNoTokenRejected` – After you've disabled IMDSv1, you can use the `MetadataNoTokenRejected` metric to track the number of times an IMDSv1 call was attempted and rejected. By tracking this metric, you can ascertain whether your software needs to be updated to use IMDSv2.  
For each EC2 instance, these metrics are mutually exclusive. When IMDSv1 is enabled (`httpTokens = optional`), only `MetadataNoToken` emits. When IMDSv1 is disabled (`httpTokens = required`), only `MetadataNoTokenRejected` emits. For when to use these metrics, see [Recommended path to requiring IMDSv2](#recommended-path-for-requiring-imdsv2).  
For more information, see [Instance metrics](viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics).

**Launch APIs**  
**New instances:** Use the [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API to launch new instances that require the use of IMDSv2. For more information, see [Configure instance metadata options for new instances](configuring-IMDS-new-instances.md).  
**Existing instances:** Use the [ModifyInstanceMetadataOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataOptions.html) API to require the use of IMDSv2 on existing instances. For more information, see [Modify instance metadata options for existing instances](configuring-IMDS-existing-instances.md).  
**New instances launched by Auto Scaling groups:** To require the use of IMDSv2 on all new instances launched by Auto Scaling groups, your Auto Scaling groups can use either a launch template or a launch configuration. When you [create a launch template](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-launch-template.html) or [create a launch configuration](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/create-launch-configuration.html), you must configure the `MetadataOptions` parameters to require the use of IMDSv2. The Auto Scaling group launches new instances using the new launch template or launch configuration, but existing instances are not affected.   
**Existing instances in an Auto Scaling group:** Use the [ModifyInstanceMetadataOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataOptions.html) API to require the use of IMDSv2 on existing instances, or terminate the instances and the Auto Scaling group will launch new replacement instances with the instance metadata options settings that are defined in the new launch template or launch configuration.

**AMIs**  
AMIs configured with the `ImdsSupport` parameter set to `v2.0` will launch instances that require IMDSv2 by default. Amazon Linux 2023 is configured with `ImdsSupport = v2.0`.  
**New AMIs:** Use the [register-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/register-image.html) CLI command to set the `ImdsSupport` parameter to `v2.0` when creating a new AMI.  
**Existing AMIs:** Use the [modify-image-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-image-attribute.html) CLI command to set the `ImdsSupport` parameter to `v2.0` when modifying an existing AMI.  
For more information, see [Configure the AMI](configuring-IMDS-new-instances.md#configure-IMDS-new-instances-ami-configuration).

**Account-level controls**  
You can configure default values for all the instance metadata options at the account level. The default values are automatically applied when you launch an instance. For more information. see [Set IMDSv2 as the default for the account](configuring-IMDS-new-instances.md#set-imdsv2-account-defaults).  
You can also enforce the requirement to use IMDSv2 at the account level. When IMDSv2 enforcement is enabled:  
+ **New instances:** Instances configured to launch with IMDSv1 enabled will fail to launch
+ **Existing instances with IMDSv1 disabled:** Attempts to enable IMDSv1 on existing instances will be prevented.
+ **Existing instances with IMDSv1 enabled:** Existing instances with IMDSv1 already enabled will not be affected.
For more information, see [Enforce IMDSv2 at the account level](configuring-IMDS-new-instances.md#enforce-imdsv2-at-the-account-level).

**IAM policies and SCPs**  
You can use an IAM policy or AWS Organizations service control policy (SCP) to control users as follows:  
+ Can't launch an instance using the [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API unless the instance is configured to use IMDSv2.
+ Can't modify an existing instance using the [ModifyInstanceMetadataOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataOptions.html) API to re-enable IMDSv1.
The IAM policy or SCP must contain the following IAM condition keys:  
+ `ec2:MetadataHttpEndpoint`
+ `ec2:MetadataHttpPutResponseHopLimit`
+ `ec2:MetadataHttpTokens`
If a parameter in the API or CLI call doesn't match the state specified in the policy that contains the condition key, the API or CLI call fails with an `UnauthorizedOperation` response.  
Furthermore, you can choose an additional layer of protection to enforce the change from IMDSv1 to IMDSv2. At the access management layer with respect to the APIs called through EC2 Role credentials, you can use a condition key in either IAM policies or AWS Organizations service control policies (SCPs). Specifically, by using the condition key `ec2:RoleDelivery` with a value of `2.0` in your IAM policies, API calls made with EC2 Role credentials obtained from IMDSv1 will receive an `UnauthorizedOperation` response. The same thing can be achieved more broadly with that condition required by an SCP. This ensures that credentials delivered through IMDSv1 cannot actually be used to call APIs because any API calls not matching the specified condition will receive an `UnauthorizedOperation` error.  
For example IAM policies, see [Work with instance metadata](ExamplePolicies_EC2.md#iam-example-instance-metadata). For more information on SCPs, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.

**Declarative Policies**  
Use Declarative Policies (a feature of AWS Organizations) to centrally set IMDS account defaults, including IMDSv2 enforcement, across your organization. For an example policy, see the **Instance Metadata** tab in the [Supported declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_syntax.html#declarative-policy-examples) section in the *AWS Organizations User Guide*.

## Recommended path to requiring IMDSv2
<a name="recommended-path-for-requiring-imdsv2"></a>

**Topics**
+ [Step 1: Identify instances with IMDSv2=optional and audit IMDSv1 usage](#path-step-1)
+ [Step 2: Update software to IMDSv2](#path-step-2)
+ [Step 3: Require IMDSv2 on instances](#path-step-3)
+ [Step 4: Set IMDSv2=required as the default](#path-step-4)
+ [Step 5: Enforce instances to require IMDSv2](#path-step-5)

### Step 1: Identify instances with IMDSv2=optional and audit IMDSv1 usage
<a name="path-step-1"></a>

To assess your IMDSv2 migration scope, identify instances that are configured to allow either IMDSv1 or IMDSv2, and audit IMDSv1 calls.

1. **Identify instances that are configured to allow either IMDSv1 or IMDSv2:**

------
#### [ Amazon EC2 console ]

   1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. In the navigation pane, choose **Instances**.

   1. To see only the instances that are configured to allow IMDSv1 or IMDSv2, add the filter **IMDSv2 = optional**.

   1. Alternatively, to see whether IMDSv2 is **optional** or **required** for all instances, open the **Preferences** window (gear icon), toggle on **IMDSv2**, and choose **Confirm**. This adds the **IMDSv2** column to the **Instances** table.

------
#### [ AWS CLI ]

   Use the [describe-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-metadata-options.html) command and filter by `metadata-options.http-tokens = optional`, as follows:

   ```
   aws ec2 describe-instances --filters "Name=metadata-options.http-tokens,Values=optional" --query "Reservations[*].Instances[*].[InstanceId]" --output text
   ```

------

1. **Audit IMDSv1 calls on each instance:**

   Use the CloudWatch metric `MetadataNoToken`. This metric shows the number of IMDSv1 calls to the IMDS on your instances. For more information, see [Instance metrics](viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics).

1. **Identify software on your instances making IMDSv1 calls:**

   Use the open source [IMDS Packet Analyzer](https://github.com/aws/aws-imds-packet-analyzer) to identify and log IMDSv1 calls during your instance’s boot phase and runtime operations. Use this information to identify the software to update to get your instances ready to use IMDSv2 only. You can run IMDS Packet Analyzer from a command line or install it as a service.

### Step 2: Update software to IMDSv2
<a name="path-step-2"></a>

Update all SDKs, CLIs, and software that use Role credentials on your instances to IMDSv2-compatible versions. For more information about updating the CLI, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

### Step 3: Require IMDSv2 on instances
<a name="path-step-3"></a>

After confirming zero IMDSv1 calls through the `MetadataNoToken` metric, configure your existing instances to require IMDSv2. Also, configure all new instances to require IMDSv2. In other words, disable IMDSv1 on all existing and new instances.

1. **Configure existing instances to require IMDSv2:**

------
#### [ Amazon EC2 console ]

   1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. In the navigation pane, choose **Instances**.

   1. Select your instance.

   1. Choose **Actions**, **Instance settings**, **Modify instance metadata options**.

   1. For **IMDSv2**, choose **Required**.

   1. Choose **Save**.

------
#### [ AWS CLI ]

   Use the [modify-instance-metadata-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-metadata-options.html) CLI command to specify that only IMDSv2 is to be used. 

------
**Note**  
You can modify this setting on running instances. The change takes effect immediately without needing an instance restart.

   For more information, see [Require the use of IMDSv2](configuring-IMDS-existing-instances.md#modify-require-IMDSv2).

1. **Monitor for issues after disabling IMDSv1:**

   1. Track the number of times an IMDSv1 call was attempted and rejected with the `MetadataNoTokenRejected` CloudWatch metric.

   1. If the `MetadataNoTokenRejected` metric records IMDSv1 calls on an instance that is experiencing software issues, this indicates that the software requires updating to use IMDSv2.

1. **Configure new instances to require IMDSv2:**

------
#### [ Amazon EC2 console ]

   1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. Follow the steps to [launch an instance](ec2-launch-instance-wizard.md).

   1. Expand **Advanced details**, and for **Metadata version**, choose **V2 only (token required)**.

   1. In the **Summary panel**, review your instance configuration, and then choose **Launch instance**.

      For more information, see [Configure the instance at launch](configuring-IMDS-new-instances.md#configure-IMDS-new-instances-instance-settings).

------
#### [ AWS CLI ]

   AWS CLI: Use the [run-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html) command and specify that IMDSv2 is required.

------

### Step 4: Set IMDSv2=required as the default
<a name="path-step-4"></a>

You can set IMDSv2=required as the default configuration at either the account or organization level. This ensures that all newly launched instances are automatically configured to require IMDSv2.

1. **Set account-level default:**

------
#### [ Amazon EC2 console ]

   1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. In the navigation pane, choose **Dashboard**.

   1. On the **Account attributes** card, under **Settings**, choose **Data protection and security**.

   1. Under **IMDS defaults**, choose **Manage**.

   1. For **Instance metadata service **, choose **Enabled**.

   1. For **Metadata version**, choose to **V2 only (token required)**.

   1. Choose **Update**.

------
#### [ AWS CLI ]

   Use the [modify-instance-metadata-defaults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-metadata-defaults.html) CLI command and specify `--http-tokens required` and `--http-put-response-hop-limit {{2}}`.

------

   For more information, see [Set IMDSv2 as the default for the account](configuring-IMDS-new-instances.md#set-imdsv2-account-defaults).

1. **Alternatively, set organization-level default using a Declarative Policy:**

   Use a Declarative Policy to set the organization default for IMDSv2 to required. For an example policy, see the **Instance Metadata** tab in the [Supported declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_syntax.html#declarative-policy-examples) section in the *AWS Organizations User Guide*.

### Step 5: Enforce instances to require IMDSv2
<a name="path-step-5"></a>

After you’ve confirmed that there is no dependency on IMDSv1 on any of your instances, we recommend that you enforce IMDSv2 on all new instances.

Use one of the following options to enforce IMDSv2:

1. **Enforce IMDSv2 with an account property**

   You can enforce the use of IMDSv2 at the account level for each AWS Region. When enforced, instances can only launch if they're configured to require IMDSv2. This enforcement applies regardless of how the instance or AMI is configured. For more information, see [Enforce IMDSv2 at the account level](configuring-IMDS-new-instances.md#enforce-imdsv2-at-the-account-level). To apply this setting at an organization level, set a Declarative Policy. For an example policy, see the **Instance Metadata** tab in the [Supported declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_syntax.html#declarative-policy-examples) section in the *AWS Organizations User Guide*.

   To prevent a reversal of enforcement, you should use an IAM policy to prevent access to the [ModifyInstanceMetadataDefaults](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataDefaults.html) API. For more information, see [Use an IAM policy](configuring-IMDS-new-instances.md#configure-IMDS-new-instances-iam-policy).
**Note**  
This setting does not change the IMDS version of existing instances, but blocks enabling IMDSv1 on existing instances that currently have IMDSv1 disabled.
**Warning**  
If IMDSv2 enforcement is enabled and `httpTokens` is not set to `required` in either the instance configuration at launch, the account settings, or the AMI configuration, the instance launch will fail. For troubleshooting information, see [Launching an IMDSv1-enabled instance fails](troubleshooting-launch.md#launching-an-imdsv1-enabled-instance-fails).

1. **Alternatively, enforce IMDSv2 by using the following IAM or SCP condition keys:**
   + `ec2:MetadataHttpTokens`
   + `ec2:MetadataHttpPutResponseHopLimit`
   + `ec2:MetadataHttpEndpoint`

   These condition keys control the use of the [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) and the [ModifyInstanceMetadataOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataOptions.html) APIs and corresponding CLIs. If a policy is created, and a parameter in the API call does not match the state specified in the policy using the condition key, the API or CLI call fails with an `UnauthorizedOperation` response.

   For example IAM policies, see [Work with instance metadata](ExamplePolicies_EC2.md#iam-example-instance-metadata).