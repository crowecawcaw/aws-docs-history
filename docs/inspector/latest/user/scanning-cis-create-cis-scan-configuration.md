# Creating a CIS scan configuration

This topic describes how to create a CIS scan configuration.

###### To run a CIS scan

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Use the AWS Region dropdown to select the AWS Region where you want to run a CIS scan.
3. From the navigation pane, choose **On-demand scans**, and then choose **CIS scans**.
4. Choose **Create new scan**.
5. For **Scan configuration name**, enter a **Scan configuration name**.
6. For **Target resource tags**, enter a **Key** and corresponding **Value** for the instances you want to scan.
   You can specify up to five different values for each key and a total of 25 tags to include in the scan.
7. For **CIS Benchmark level**, you can select **Level 1** for basic security configurations or **Level 2** for advanced security configurations.
8. For **Target accounts**, specify which accounts to include in the CIS scan.
   For more information, see [Considerations for managing Amazon Inspector CIS scans with AWS Organizations](scanning-cis.md#CIS-organizations "scanning-cis.md#CIS-organizations").

If your account is the delegated administrator account, you can select **All accounts** or **Specify accounts**.
The **All accounts** option targets all accounts in your organization.
The **Specify accounts** only targets individual accounts in your organization.
If you choose this option, you can specify more than one account by separating the account numbers with a comma.
You can also enter `SELF` instead of an account ID to create a scan configuration for your account

If your account is a standalone account or member account in an organization, you can select **Self** to create a scan configuration for your account. 9. For **Schedule**, choose **One time scan**, which runs as soon as you finish creating your scan configuration, or **Recurring scans**, which runs at the time you specify. 10. Confirm your choices, and then choose **Create**.
