# Validate policies with IAM Access Analyzer custom policy

checks

You can use custom policy checks to check for new access based on your security standards.
A charge is associated with each check for new access. For more details about pricing, see
[IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

## Validating policies with

custom policy checks (console)

As an optional step, you can run a custom policy check when editing a policy in the
JSON policy editor in the IAM console. You can check whether the updated policy grants
new access compared to the existing version.

###### To check for new access when editing IAM JSON policies

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.
3. In the list of policies, choose the policy name of the policy that you want to
   edit. You can use the search box to filter the list of policies.
4. Choose the **Permissions** tab, and then choose
   **Edit**.
5. Choose the **JSON** option and make updates to your
   policy.
6. In the policy validation pane below the policy, choose the **Check for
   new access** tab and then choose **Check policy**.
   If the modified permissions grant new access, the statement will be highlighted
   in the policy validation pane.
7. If you don't intend to grant new access, update the policy statement and
   choose **Check policy** until no new access is detected.

###### Note

A charge is associated with each check for new access. For more details
about pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing"). 8. Choose **Next**. 9. On the **Review and save** page, review **Permissions
defined in this policy** and then choose **Save
changes**.

## Validating policies with

custom policy checks (AWS CLI or API)

You can run IAM Access Analyzer custom policy checks from the AWS CLI or the IAM Access Analyzer
API.

### To run IAM Access Analyzer

custom policy checks (AWS CLI)

- To check whether new access is allowed for an updated policy when compared
  to the existing policy, run the following command: [check-no-new-access](../../../cli/latest/reference/accessanalyzer/check-no-new-access.md "../../../cli/latest/reference/accessanalyzer/check-no-new-access.md")
- To check whether the specified access isn't allowed by a policy, run the
  following command: [check-access-not-granted](../../../cli/latest/reference/accessanalyzer/check-access-not-granted.md "../../../cli/latest/reference/accessanalyzer/check-access-not-granted.md")
- To check whether a resource policy can grant public access to a specified
  resource type, run the following command: [check-no-public-access](../../../cli/latest/reference/accessanalyzer/check-no-public-access.md "../../../cli/latest/reference/accessanalyzer/check-no-public-access.md")

### To run IAM Access Analyzer

custom policy checks (API)

- To check whether new access is allowed for an updated policy when compared
  to the existing policy, use the [CheckNoNewAccess](../../../access-analyzer/latest/APIReference/API_CheckNoNewAccess.md "../../../access-analyzer/latest/APIReference/API_CheckNoNewAccess.md") API operation.
- To check whether the specified access isn't allowed by a policy, use the
  [CheckAccessNotGranted](../../../access-analyzer/latest/APIReference/API_CheckAccessNotGranted.md "../../../access-analyzer/latest/APIReference/API_CheckAccessNotGranted.md") API operation.
- To check whether a resource policy can grant public access to a specified
  resource type, use the [CheckNoPublicAccess](../../../access-analyzer/latest/APIReference/API_CheckNoPublicAccess.md "../../../access-analyzer/latest/APIReference/API_CheckNoPublicAccess.md") API operation.
