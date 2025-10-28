# About invalid effective policy alerts

_Invalid policy alerts_ let you know about invalid effective policies and provide
mechanisms (APIs) to identify accounts with invalid policies. AWS Organizations notifies you
asynchronously when one of your accounts has an invalid effective policy. The notification
appears as a banner in the AWS Organizations console page, and it is recorded as an AWS CloudTrail
event.

## Detect invalid effective management

policies in your organization

There are several ways in which you can view invalid effective management policies in
your organization: from the AWS Management Console, AWS API, AWS Command Line
Interface (CLI), or as an AWS CloudTrail event.

###### Minimum permissions

To find the information related to invalid effective policies of a management policy
type in your organization, you must have permission to run the following actions:

- `organizations:ListAccountsWithInvalidEffectivePolicy`
- `organizations:ListEffectivePolicyValidationErrors`
- `organizations:ListRoots` - required only when using the
  Organizations console

AWS Management Console

###### To view invalid effective management policies from the console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page page, if your organization has invalid effective
   policies, a warning banner is displayed at the top of the page.
3. In the banner, click on **View detected issues** to view the
   list of all accounts in your organization that have invalid effective
   policies.
4. For each account in the list, select **View issues** to get
   more information on errors for each account shown under the **Effective
   policy issues** sections on this page.

AWS CLI & AWS SDKs

###### To view the effective policy of a management policy type for an

account

The following commands help you view accounts with invalid effective policies

- AWS CLI: [list-accounts-with-invalid-effective-policy](../../../cli/latest/reference/organizations/list-accounts-with-invalid-effective-policy.md "../../../cli/latest/reference/organizations/list-accounts-with-invalid-effective-policy.md")
- AWS SDKs: [ListAccountsWithInvalidEffectivePolicy](../APIReference/API_ListAccountsWithInvalidEffectivePolicy.md "../APIReference/API_ListAccountsWithInvalidEffectivePolicy.md")

###### The following commands help you view effective policy errors on an account

- AWS CLI: [list-effective-policy-validation-errors](../../../cli/latest/reference/organizations/list-effective-policy-validation-errors.md "../../../cli/latest/reference/organizations/list-effective-policy-validation-errors.md")
- AWS SDKs: [ListEffectivePolicyValidationErrors](../APIReference/API_ListEffectivePolicyValidationErrors.md "../APIReference/API_ListEffectivePolicyValidationErrors.md")

**AWS CloudTrail**

You can use AWS CloudTrail events to monitor when accounts in your organizations have invalid effective management policies and when the policies are fixed. For more information, see _Effective policy examples_ in [Understanding AWS Organizations log file entries](orgs_cloudtrail-integration.md#understanding-service-name-entries "orgs_cloudtrail-integration.md#understanding-service-name-entries").

If you receive an invalid effective policy notification, you can navigate through the AWS Organizations console or call these APIs from your management or delegated administrator account to find more details about the status of specific accounts and policies:

- `ListAccountsWithInvalidEffectivePolicy` – Returns a list of
  accounts in the organization that have invalid effective policies of a specified type.
- `ListEffectivePolicyValidationErrors` – Returns a list of validation errors for a specified account and management policy type. The validation errors contain details, including the error code, error description, and contributing policies that made the effective policy invalid.

## When an effective management policy might be considered invalid

Effective policies on an account can become invalid if they violate the constraints defined for the particular policy type. For example, a policy might be missing a required parameter in the final effective policy or exceed certain quotas defined for the policy type.

**Backup policy example**

Suppose that you create a backup policy with nine backup rules and attach it to the root of your organization. Later, you create another backup policy for the same backup plan – with two more rules – and attach it to any account in the organization. In that situation, there's an invalid effective policy on the account. It is invalid because the aggregation of the two policies defines 11 rules for the backup plan. The limit is 10 backup rules in a plan.

###### Warning

If any account in the organization has an invalid effective policy, that account will not receive effective policy updates for the particular policy type. It continues with the last applied valid effective policy for the account, unless all the errors are fixed.

**Examples of possible errors for effective policies**

- `ELEMENTS_TOO_MANY` – Occurs when a particular attribute in an effective policy exceeds the allowed limit, such as when more than 10 rules are given for a backup plan.
- `ELEMENTS_TOO_FEW` – Occurs when a particular attribute in an effective policy does not meet the minimum limit, such as when no region is defined for a backup plan.
- `KEY_REQUIRED` – Occurs when a required configuration is missing in the effective policy, such as when a backup plan is missing a backup rule.

AWS Organizations validates effective policies before applying them to the accounts in your organization. This auditing process is especially beneficial if you
have a large organization structure, and if your organization's policies are managed by more
than one team.
