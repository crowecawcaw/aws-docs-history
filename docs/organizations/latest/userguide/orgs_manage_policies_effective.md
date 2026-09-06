

# Viewing effective declarative policies
<a name="orgs_manage_policies_effective"></a>

Determine the effective declarative policy for an account in your organization.

## What is an effective declarative policy?
<a name="effective-policy-defined"></a>

The *effective policy* specifies the final rules that apply to an AWS account for a declarative policy type. It is the aggregation for a declarative policy that the account inherits, plus any policies for that declarative policy type that are directly attached to the account. When you attach a declarative policy to the organization's root, it applies to all accounts in your organization. When you attach a declarative policy to an organizational unit (OU), it applies to all accounts and OUs that belong to the OU. When you attach a declarative policy directly to an account, it applies only to that one AWS account.

For information about how policies are combined into the final effective policy, see [Understanding declarative policy inheritance](orgs_manage_policies_inheritance_mgmt.md).

**Backup policy example**

The backup policy attached to the organization root might specify that all accounts in the organization back up all Amazon DynamoDB tables with a default backup frequency of once per week. A separate backup policy attached directly to one member account with critical information in a table can override the frequency with a value of once per day. The combination of these backup policies comprises the effective backup policy. This effective backup policy is determined for each account in the organization individually. In this example, the result is that all accounts in the organization back up their DynamoDB tables once per week, with the exception of one account that backs up its tables daily.

**Tag policy example**

The tag policy attached to the organization root might define a `CostCenter` tag with four compliant values. A separate tag policy attached to the account may restrict the `CostCenter` key to only two of the four compliant values. The combination of these tag policies comprises the effective tag policy. The result is that only two of the four compliant tag values defined in the organization root tag policy are compliant for the account.

**Chat applications policy example**

Amazon Q Developer in chat applications will reevaluate any previously created Amazon Q Developer in chat applications configurations against the effective chat applications policies and deny any previously allowed actions if they are consistent with the permitted settings and guardrails in the effective policy. The effective policy for a member account defines the permitted settings and guardrails. For example, if a chat applications policy with deny access for public Slack channels is applied to a member account, then the existing Amazon Q Developer in chat applications configurations for public Slack channels in the member account will be disabled. Amazon Q Developer in chat applications will not deliver notifications and channel members will not be able to run any tasks in the blocked channel. The Amazon Q Developer in chat applications console will mark the affected channels as disabled with an appropriate error messaging next to it.

**AI services opt-out example**

The AI services opt-out policy attached to the organization root might specify that all accounts in the organization opt out of content use by all AWS machine learning services. A separate AI services opt-out policy attached directly to one member account specifies that it opts in to content use for only Amazon Rekognition. The combination of these AI services opt-out policies comprises the effective AI services opt-out policy. The result is that all accounts in the organization are opted out of all AWS services, with the exception of one account that opts in to Amazon Rekognition.

## How to view the effective declarative policy
<a name="how-to-view-effective-policies"></a>

You can view the effective policy of a declarative policy type for an account from the AWS Management Console, AWS API, or AWS Command Line Interface.

**Minimum permissions**  
To view the effective policy of a declarative policy type for an account, you must have permission to run the following actions:  
`organizations:DescribeEffectivePolicy`
`organizations:DescribeOrganization` – required only when using the Organizations console

------
#### [ AWS Management Console ]

**To view the effective policy of a declarative policy type for an account**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts)** page, choose the name of the account for which you want to view the effective policy. You might have to expand OUs (choose the ![Gray cloud icon representing cloud computing or storage services.](http://docs.aws.amazon.com/organizations/latest/userguide/images/console-expand.png)) to find the account that you want.

1. On the **Policies** tab, choose the declarative policy type for which you want to view the effective policy.

1. Choose **View the effective policy for this AWS account**.

   The console displays the effective policy applied to the specified account.
**Note**  
You can't copy and paste an effective policy and use it as the JSON for another policy without significant changes. Policy documents must include the [inheritance operators](policy-operators.md) that specify how each setting is merged into the final effective policy. 

------
#### [ AWS CLI & AWS SDKs ]

**To view the effective policy of a declarative policy type for an account**  
You can use one of the following to view the effective policy:
+ AWS CLI: [describe-effective-policy](https://docs.aws.amazon.com/cli/latest/reference/organizations/describe-effective-policy.html)

  The following example shows the effective AI services opt-out policy for an account.

  ```
  $ aws organizations describe-effective-policy \
      --policy-type AISERVICES_OPT_OUT_POLICY \
      --target-id 123456789012
  {
      "EffectivePolicy": {
          "PolicyContent": "{\"services\":{\"comprehend\":{\"opt_out_policy\":\"optOut\"},   ....TRUNCATED FOR BREVITY....   "opt_out_policy\":\"optIn\"}}}",
          "LastUpdatedTimestamp": "2020-12-09T12:58:53.548000-08:00",
          "TargetId": "123456789012",
          "PolicyType": "AISERVICES_OPT_OUT_POLICY"
      }
  }
  ```
+ AWS SDKs: [DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html) 

------

For information about situations in which an effective policy could become invalid, see [Viewing invalid policy alerts](https://docs.aws.amazon.com/organizations/latest/userguide/invalid-policy-alerts.html). 