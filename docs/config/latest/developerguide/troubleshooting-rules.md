# Troubleshooting for AWS Config rules

Check the following issues to troubleshoot if you cannot delete an AWS Config rule or
receive an error similair to the following: "An error has occurred with AWS Config."

**The AWS Identity and Access Management (IAM) entity has permissions for the DeleteConfigRule
API**

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane choose **Users** or
   **Roles**.
3. Choose the user or role that you used to delete the AWS Config rule, and expand
   **Permissions policies**.
4. In the **Permissions** tab, choose
   **JSON**.
5. In the JSON preview pane, confirm that the IAM policy allows permissions for
   the [DeleteConfigRule](../APIReference/API_APIDeleteConfigRule.md "../APIReference/API_APIDeleteConfigRule.md") API.
   **The IAM entity permission boundary allows the DeleteConfigRule
   API**

If the IAM entity has a permissions boundary, be sure that it allows permissions for
the the DeleteConfigRule API.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane choose **Users** or
   **Roles**.
3. Choose the user or role that you used to delete the AWS Config rule, expand
   **Permissions boundary**, and then choose
   **JSON**.
4. In the JSON preview pane, confirm that the IAM policy allows permissions for
   the [DeleteConfigRule](../APIReference/API_APIDeleteConfigRule.md "../APIReference/API_APIDeleteConfigRule.md") API.

###### Warning

IAM users have long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed.

**The service control policy (SCP) allows the DeleteConfigRule
API**

1. Open the AWS Organizations console at https://console.aws.amazon.com/organizations/ using the [management account](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") for the organization.
2. In Account name, choose the AWS account.
3. In **Policies**, expand **Service control
   policies** and note the SCP policies that are attached.
4. At the top of the page, choose **Policies**.
5. Select the policy, and then choose **View details**.
6. In the JSON preview pane, confirm that the policy allows the [DeleteConfigRule](../APIReference/API_APIDeleteConfigRule.md "../APIReference/API_APIDeleteConfigRule.md") API.
   **The rule is not a service-linked rule**

When you [enable
a security standard](../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md "../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md"), AWS Security Hub CSPM creates [service-linked rules](service-linked-awsconfig-rules.md "service-linked-awsconfig-rules.md") for you. You can't delete these service-linked rules
using AWS Config, and the delete button is grayed out. To remove a service-linked rule, see
[Disabling a security standard](../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md "../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md") in the _Security Hub CSPM User
Guide_.

**No remediation actions are in progress**

You cannot delete AWS Config rules that have [remediation actions](remediation.md "remediation.md") in
progress. Follow the steps to [delete
the remediation action that is associated with that rule](remediation.md#delete-remediation-action "remediation.md#delete-remediation-action"). Then, try deleting
the rule again.

###### Important

Only delete remediation actions that are in **failed** or
**successful** states.
