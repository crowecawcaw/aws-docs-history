# Delete an approval rule template

You can delete an approval rule template if you are not using it in any repositories.
Deleting unused approval rule templates helps keep your templates organized and makes it
easier to find templates that make sense for your workflows.

For more information about managed policies and permissions for approval rule
templates, see [Permissions for actions on approval rule templates](auth-and-access-control-permissions-reference.md#aa-art "auth-and-access-control-permissions-reference.md#aa-art") and [AWS managed policies for
CodeCommit](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

###### Topics

- [Delete an approval rule template
  (console)](#how-to-delete-template-console "#how-to-delete-template-console")
- [Delete an approval rule template
  (AWS CLI)](#how-to-delete-template-cli "#how-to-delete-template-cli")

## Delete an approval rule template

(console)

You can delete an approval rule template if it is no longer relevant to your
development work. When you use the console to delete an approval rule template, it
is disassociated from any repositories during the deletion process.

## To delete an approval rule template

1. Open the CodeCommit console at [https://console.aws.amazon.com/codesuite/codecommit/home](https://console.aws.amazon.com/codesuite/codecommit/home "https://console.aws.amazon.com/codesuite/codecommit/home").
2. Choose **Approval rule templates**. Choose the template
   you want to delete, and then choose **Delete**.

## Delete an approval rule template

(AWS CLI)

You can use the AWS CLI to delete an approval rule if it has been disassociated from
all repositories. For more information, see [Disassociate an approval rule
template (AWS CLI)](how-to-disassociate-template.md#how-to-disassociate-template-cli "how-to-disassociate-template.md#how-to-disassociate-template-cli").

## To delete an approval rule template

1. At a terminal or command line, run the
   **delete-approval-rule-template** command, specifying the
   name of the approval rule template you want to delete:

```
aws codecommit delete-approval-rule-template --approval-rule-template-name `1-approver-for-all-pull-requests`
```

2. If successful, this command returns output similar to the following. If
   the approval rule template has already been deleted, this command returns
   nothing.

```
{
    "approvalRuleTemplateId": "41de97b7-EXAMPLE"
}
```
