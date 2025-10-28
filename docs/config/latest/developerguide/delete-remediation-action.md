# Deleting Remediation Actions for AWS Config

You can use the AWS Config console or the AWS CLI to delete remediation actions.

Deleting remediation actions (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Rules** on the left and then on the
   **Rules** page, select the rule from the rule list and
   choose **View details**.
3. On the `name of the rule` page, go to the
   **Remediation action** section. Expand the section to view
   additional details.
4. In the **Remediation action** section, choose
   **Delete** and confirm your delete action.

###### Note

If remediation is in progress, a remediation action won't be deleted. Once
you choose delete a remediation action, you cannot retrieve the remediation
action. Deleting a remediation action does not delete the associated
rule.

If a remediation action is deleted, the **Resource ID
parameter** will be empty and display N/A. On the
**Rules** page, the remediation action column displays
**Not set** for the associated rule.

Deleting remediation actions (API)
Use the following AWS Config API operation to set up auto remediation:

- [DeleteRemediationConfiguration](../APIReference/API_DeleteRemediationConfiguration.md "../APIReference/API_DeleteRemediationConfiguration.md"), deletes the remediation configuration.
- [DeleteRemediationExceptions](../APIReference/API_DeleteRemediationExceptions.md "../APIReference/API_DeleteRemediationExceptions.md"), deletes one or more remediation exceptions mentioned in the resource keys.
