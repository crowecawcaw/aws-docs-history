

# Validate policies with IAM Access Analyzer custom policy checks
<a name="access-analyzer-custom-policy-checks"></a>

You can use custom policy checks to check for new access based on your security standards. A charge is associated with each check for new access. For more details about pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

## Validating policies with custom policy checks (console)
<a name="access-analyzer-custom-policy-checks-console"></a>

As an optional step, you can run a custom policy check when editing a policy in the JSON policy editor in the IAM console. You can check whether the updated policy grants new access compared to the existing version.

**To check for new access when editing IAM JSON policies**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane on the left, choose **Policies**. 

1. In the list of policies, choose the policy name of the policy that you want to edit. You can use the search box to filter the list of policies.

1. Choose the **Permissions** tab, and then choose **Edit**. 

1. Choose the **JSON** option and make updates to your policy.

1. In the policy validation pane below the policy, choose the **Check for new access** tab and then choose **Check policy**. If the modified permissions grant new access, the statement will be highlighted in the policy validation pane.

1. If you don't intend to grant new access, update the policy statement and choose **Check policy** until no new access is detected.
**Note**  
A charge is associated with each check for new access. For more details about pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

1. Choose **Next**.

1. On the **Review and save** page, review **Permissions defined in this policy** and then choose **Save changes**.

## Validating policies with custom policy checks (AWS CLI or API)
<a name="access-analyzer-custom-policy-checks-cli-api"></a>

You can run IAM Access Analyzer custom policy checks from the AWS CLI or the IAM Access Analyzer API.

### To run IAM Access Analyzer custom policy checks (AWS CLI)
<a name="access-analyzer-custom-policy-checks-cli"></a>
+ To check whether new access is allowed for an updated policy when compared to the existing policy, run the following command: [check-no-new-access](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/check-no-new-access.html)
+ To check whether the specified access isn't allowed by a policy, run the following command: [check-access-not-granted](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/check-access-not-granted.html)
+ To check whether a resource policy can grant public access to a specified resource type, run the following command: [check-no-public-access](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/check-no-public-access.html)

### To run IAM Access Analyzer custom policy checks (API)
<a name="access-analyzer-custom-policy-checks-api"></a>
+ To check whether new access is allowed for an updated policy when compared to the existing policy, use the [CheckNoNewAccess](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoNewAccess.html) API operation.
+ To check whether the specified access isn't allowed by a policy, use the [CheckAccessNotGranted](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckAccessNotGranted.html) API operation.
+ To check whether a resource policy can grant public access to a specified resource type, use the [CheckNoPublicAccess](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoPublicAccess.html) API operation.