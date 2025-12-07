# Removing the delegated administrator account in Security Hub

You can remove the delegated administrator account in the Security Hub console at any time.
However, this action not only removes the delegated administrator from Security Hub, but also Security Hub CSPM.
We recommend only performing this action when you have confirmed this operation with your security account.

###### Note

If you're using an account other than the organization management account as the Security Hub CSPM delegated administrator,
removing it through either the CSPM Console or AWS Organizations API will also remove it from Security Hub.

Similarly, if you remove the Security Hub delegated administrator through either the Security Hub Console or AWS Organizations API,
it will also be removed from Security Hub CSPM. When the delegated administrator is removed from CSPM, Central Configuration will automatically opt out.

###### To remove the delegated administrator account

1. Sign in to your AWS account with your organization management account credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home? "https://console.aws.amazon.com/securityhub/v2/home?").
2. From the navigation pane, choose **General**.
3. In **Delegated administrator**, choose **Remove delegated administrator**.
   In the pop-up window, enter _remove_, and choose **Remove**.
