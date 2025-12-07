# Designating a delegated administrator in Security Hub

In the AWS organization management account, you can designate a delegated administrator for your organization.
As a best practice, we recommend using the same delegated administrator across security services for consistent governance.

The procedure in this topic describes how to designate a delegated administrator in Security Hub.
It assumes you previously enabled Security Hub but did not designate a delegated administrator during the enablement workflow.

###### Considerations

Consider the following when designating a delegated administrator in Security Hub:

- The AWS organization management account can designate itself as the delegated administrator in Security Hub CSPM.
  The AWS organization management account cannot designate itself as the delegated administrator in Security Hub.
  In this scenario, the AWS organization management account must designate another AWS account as the delegated administrator in Security Hub.
  As a best practice, we recommend using the same delegated administrator across security services for consistent governance.
- If the AWS organization management account designates a delegated administrator in Security Hub CSPM, that delegated administrator automatically becomes the delegated administrator in Security Hub.
  In this scenario, Security Hub only allows this particular AWS account to serve as the delegated administrator.

###### Note

If the AWS organization management account uses the same delegated administrator in Security Hub as it does in Security Hub CSPM, removing it through the Security Hub CSPM console or with the AWS Organizations API also removes it in Security Hub.
Similarly, removing it through the Security Hub console or with the AWS Organizations API also removes it in Security Hub CSPM.
When the delegated administrator is removed from Security Hub CSPM, Central Configuration will automatically opt out.

## Designating a delegated administrator after enabling Security Hub

This procedure is for the AWS organization management account to complete.
It assumes the AWS organization management account previously enabled Security Hub but did not designate a delegated administrator during the enablement workflow.

###### Note

After you complete this procedure, you must create a policy allowing the delegated administrator for your organization to configure Security Hub and perform specific actions in AWS Organizations.
For more information, see [Creating the delegated administrator policy in Security Hub](securityhub-v2-policy-statement.md "securityhub-v2-policy-statement.md").

###### To designate a delegated administrator in Security Hub

1. Sign in to your AWS account with your organization management account credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the navigation pane, choose **General**.
3. In **Delegated administrator**, choose **Configure**.
   Select one of the provided AWS accounts, or enter the 12-digit AWS account number for the AWS account that you want to designate as the delegated administrator for your organization.
   Choose **Save**.
