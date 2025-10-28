# Creating automation rules in Security Hub

###### Note

Security Hub is in preview release and is subject to change.

This topic describes how to create automation rules.
You can use automation rules to update details for a finding or create a ticket for a third-party integration.
You must create automation rules individually and in the AWS Region where you want them applied.
However, if you create an automation rule in an aggregation region, it will be applied in all regions.
Otherwise, if you create an automation rule in a non-linked region, it will be applied just in that region.

## Creating a rule that updates finding details

The following procedure describes how to create a rule that updates finding details.

1. Sign in to your AWS account.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the navigation pane, under **Management**, choose **Automations**.
3. Choose **Create rule**.
4. Under **Details**, enter a name for your automation rule.
   1. (Optional) Enter a description for your automation rule.

5. Under **Actions**, choose **Update findings details**.
   You can search for criteria and add criteria in the search bar.
   To check if any findings match your criteria, choose **Preview matching findings**.
6. Under **Update finding details**, choose at least one finding detail to update when a finding matches your criteria.
   You can choose **Severity**, **Status**, or **Comment**.
7. Under **Rule settings**, select **Enabled** or **Disabled**.
   If you select **Enabled**, the automation rule is enabled and will process new findings.
   If you select **Disabled**, the automation rule is disabled and will not process any findings.
8. (Optional) Under **Tags**, choose **Add new tag** to enter a key-value pair to be applied to your automation rule.
9. Choose **Create rule**.

## Creating a rule for a third-party integration

The following procedure describes how to create a rule that creates a ticket for a third-party integration.
For information about the integrations Security Hub CSPM supports, see [Third-party integrations for Security Hub CSPM](security-hub-adv-catalog-integrations.md "security-hub-adv-catalog-integrations.md").

1. Sign in to your AWS account.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the navigation pane, under **Management**, choose **Automations**.
3. Choose **Create rule**.
4. Under **Details**, enter a name for your automation rule.
   1. (Optional) Enter a description for your automation rule.

5. Under **Actions**, choose **Create ticket**.
   You can search for criteria and add criteria in the search bar.
   To check if any findings match your criteria, choose **Preview matching findings**.
6. Under **Create a ticket**, choose an IT ticketing integration from the dropdown, and then choose **Add integration**.
7. Under **Rule settings**, select **Enabled** or **Disabled**.
   If you select **Enabled**, the automation rule is enabled and will process new findings.
   If you select **Disabled**, the automation rule is disabled and will not process any findings.
8. (Optional) Under **Tags**, choose **Add new tag** to enter a key-value pair to be applied to your automation rule.
9. Choose **Create rule**.
