# Retain AWS CloudTrail trails during landing zone update

You can choose to retain your account-level AWS CloudTrail trails when you upgrade your AWS Control Tower landing zone version.

**Prerequisites**

- Your landing zone version is less than 3.0.
- Your most recent **Create** or **Update** operation succeeded.

###### To retain the account-level trail and opt in to organization-level CloudTrail trails

1. Contact AWS Support with a request to allowlist your account.
2. The support team confirms when the target account is allowlisted.
3. After confirmation, update your landing zone to version 3.1 or greater, and choose **AWS CloudTrail configuration - Enabled**.

###### To retain the account-level trail and opt out of CloudTrail trails managed by AWS Control Tower

1. Contact AWS Support with a request to allowlist your account.
2. The support team confirms when the target account is allowlisted.
3. After confirmation, update your landing zone to version 3.1 or greater and choose **AWS CloudTrail configuration - Not Enabled**.

###### Important

After the account-level CloudTrail trails are retained, we cannot remove trails or remove your accounts from the allow list.

**How to make a support request to retain your account-level trails**

If you need to retain account-level trails during a Landing Zone update, you must contact AWS Support to add your account to the AWS Control Tower allow list. Follow these steps to submit a support ticket:

1. Sign in to the AWS Management Console.
2. Navigate to the AWS Support Center.
3. Choose **Create case**.
4. For **Case type**, select **Technical support**.
5. For **Service**, choose **AWS Control Tower**.
6. For **Category**, select **General Guidance**.
7. In the **Subject** line, include the following phrase:

`Allow retention of account-level trails during Landing Zone update` 8. In the **Description** field, provide the following details:

    * Your AWS Management account number
    * The selected home Region for your AWS Control Tower environment

9. Complete any other required fields in the support case form.
10. Choose **Submit** to create the support case.
    After you submit the ticket, AWS Support reviews your request and adds your account to the allow list, if appropriate. You will receive further instructions and confirmation through the support case communication channel.

###### Note

To delete the account-level trail after it is allowlisted, use the management account to delete the AWS CloudFormation stack set or specific stack instance. All resources in the stack are deleted.
