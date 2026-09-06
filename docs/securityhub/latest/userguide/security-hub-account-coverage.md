

# Account coverage in Security Hub
<a name="security-hub-account-coverage"></a>

 The **Account coverage** page shows which accounts and Regions in your organization have Security Hub and its integrated security capabilities enabled. These capabilities include services such as Amazon Inspector, Amazon GuardDuty, AWS Security Hub CSPM, and Amazon Macie. Use this page to identify coverage gaps and track capability adoption across your organization. 

## Account coverage page
<a name="account-coverage-page"></a>

 With the account coverage page, you can view aggregated coverage metrics. Use the Accounts tab for account-level details and the Coverage findings tab to review specific coverage gaps. 

**To access the Security Hub **Account coverage** page**

1.  Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, under **Settings** choose **Account coverage**. 

### Overview section
<a name="overview-section"></a>

 The **Overview** section displays aggregated security coverage metrics across all monitored accounts. For delegated administrator accounts, this section displays Security Hub enablement details across the organization, providing visibility into coverage for all member accounts. This high-level visualization shows the percentage of accounts with Security Hub and each security capability enabled, offering a comprehensive view of your security posture. You can select the percentage of Security Hub coverage to view a breakdown of enabled accounts by Region. You can select each capability percentage to filter coverage findings by that capability. 

 The percentages in the Overview section are determined using the following calculations: 
+ **Security Hub enablement** = (Number of account and Region pairs where Security Hub is enabled) ÷ (Total accounts in your organization × Regions where Security Hub is available)
+ **Services coverage** = (Number of enabled account and configured Region pairs where the capability is enabled) ÷ (Total number of enabled account and configured Region pairs, in configured Regions where account is enabled, and capability is available)

**Configured Regions**  
 For a home Region setup, configured Regions include the home Region and linked Regions. For all other setups, configured Regions refers to the current Region only. 

### Accounts tab
<a name="accounts-tab"></a>

 This tab is available only in the Security Hub delegated administrator account. Use the **Accounts** tab to analyze account-specific coverage. The Security Hub column shows the number of Regions where Security Hub is enabled for each account. This column is not displayed when viewing the tab in opt-in Regions (Regions that are disabled by default). Each security capability displays a coverage percentage that, when selected, reveals a detailed breakdown of individual features and their coverage percentage within that capability. When you select these percentages, Security Hub filters the results to display coverage for that capability and account. 

 The percentages in the Accounts tab are determined using the following calculation: 

 **Accounts tab coverage** = (Number of Regions where the capability is enabled) ÷ (Regions where the capability is available) 

 There are several cases where the coverage percentage might show as 0%: 
+  Security Hub is not enabled in the account and so no coverage findings are being ingested. 
+  Security Hub is waiting for coverage findings to be generated. 

### Coverage findings tab
<a name="coverage-findings-tab"></a>

 The **Coverage findings** tab lists informational findings for security capabilities that are enabled or disabled across your accounts and Regions. These findings help identify areas where security coverage can be enhanced. Each finding shows the finding title, the affected account and Region, and the current status. Each finding also has a configure link that takes you to the individual service where you can manage the configuration for that capability, or to the Security Hub configurations page where you can update your configurations for security services. 

 You can suppress coverage findings with a **Not covered** status if that security capability is not applicable for the account-Region combination. Security Hub excludes suppressed findings from the security coverage percentage calculation. 

 For more information about coverage findings and how to suppress them, see [Coverage findings in Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/coverage-findings.html). 

## Security coverage widget
<a name="account-coverage-seccov-widget"></a>

 Account coverage can also be viewed via the **Security coverage widget** in the Security Hub summary dashboard. For more information, see [Security coverage widget](https://docs.aws.amazon.com/securityhub/latest/userguide/dashboard-v2.html#security-hub-v2-dashboard-coverage-widget). 