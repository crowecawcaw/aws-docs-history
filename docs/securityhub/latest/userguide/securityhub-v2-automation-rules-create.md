

# Creating automation rules in Security Hub
<a name="securityhub-v2-automation-rules-create"></a>

 This topic describes how to create automation rules. You can use automation rules to update details for a finding or create a ticket for a third-party integration. You must create automation rules individually and in the AWS Region where you want them applied. However, if you create an automation rule in an aggregation Region, it is applied in all Regions. Otherwise, if you create an automation rule in a non-linked Region, it is applied only in that Region. 

## Creating a rule that updates finding details
<a name="update-details"></a>

 The following procedure describes how to create a rule that updates finding details. 

1.  Sign in to your AWS account. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, under **Management**, choose **Automations**. 

1.  Choose **Create rule**. 

1.  Under **Details**, enter a name for your automation rule. 

   1.  (Optional) Enter a description for your automation rule. 

1.  Under **Actions**, choose **Update findings details**. You can search for criteria and add criteria in the search bar. To check if any findings match your criteria, choose **Preview matching findings**. 

1.  Under **Update finding details**, choose at least one finding detail to update when a finding matches your criteria. You can choose **Severity**, **Status**, or **Comment**. 

1.  Under **Rule settings**, select **Enabled** or **Disabled**. If you select **Enabled**, the automation rule is enabled and processes new findings. If you select **Disabled**, the automation rule is disabled and does not process any findings. 

1.  (Optional) Under **Tags**, choose **Add new tag** to enter a key-value pair to be applied to your automation rule. 

1.  Choose **Create rule**. 

## Creating a rule for a third-party integration
<a name="integration"></a>

 The following procedure describes how to create a rule that creates a ticket for a third-party integration. For information about the integrations Security Hub CSPM supports, see [Third-party integrations for Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/security-hub-adv-catalog-integrations.html). 

1.  Sign in to your AWS account. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, under **Management**, choose **Automations**. 

1.  Choose **Create rule**. 

1.  Under **Details**, enter a name for your automation rule. 

   1.  (Optional) Enter a description for your automation rule. 

1.  Under **Actions**, choose **Create ticket**. You can search for criteria and add criteria in the search bar. To check if any findings match your criteria, choose **Preview matching findings**. 

1.  Under **Create a ticket**, choose an IT ticketing integration from the dropdown, and then choose **Add integration**. 

1.  Under **Rule settings**, select **Enabled** or **Disabled**. If you select **Enabled**, the automation rule is enabled and processes new findings. If you select **Disabled**, the automation rule is disabled and does not process any findings. 

1.  (Optional) Under **Tags**, choose **Add new tag** to enter a key-value pair to be applied to your automation rule. 

1.  Choose **Create rule**. 