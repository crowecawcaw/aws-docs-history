

# Working in the summary dashboard in Security Hub
<a name="dashboard-v2"></a>

 The **Summary** dashboard in the Security Hub console displays an overview of your exposures, threats, resources, and security coverage across security widgets. You can customize the dashboard by adding and removing widgets and by creating and applying filter sets to retrieve data in each widget. 

## Considerations
<a name="dashboard-v2-considerations"></a>

 Consider the following before interacting with the dashboard: 
+  Customizations like saved filter sets or changes to the layout of widgets are saved automatically. 
+  Data automatically refreshes every time you open the dashboard. 
+  If you configure cross-Region aggregation, the dashboard includes findings from all of your linked Regions (when viewing the dashboard in your home Region). 

 Consider the following if your account is a delegated administrator account for an organization, member account in an organization, or standalone account. 
+  Customizations made by a delegated administrator account will be saved independently from customizations made by member accounts. Customizations might include saved filter sets or changes to the layout of widgets. 
+  If your account is the delegated administrator account for an organization, data includes findings for your account and member accounts. 
+  If your account is a member account in an organization or a standalone account, data includes findings only for your account. 

 As a best practice, do not include confidential, sensitive, or personally identifiable information (PII) in saved filter sets, custom widgets, or other related free-form text fields. 

## Available widgets
<a name="dashboard-v2-widgets"></a>

 You can interact with different widgets in the **Executive** and **Triage** tabs of the **Summary** dashboard. The **Executive** tab includes widgets that display trends data for your exposures, threats, and resources and the **Security Coverage** widget to help track your account coverage across different security capabilities. The **Triage** tab includes widgets that display a summary of your exposures, threats, and resources. However, you can add widgets, remove widgets, and manage the position of each widget in both tabs to customize your experience. 

### Trends widgets
<a name="w2aab7c29b7b5"></a>

 The following widgets display trends data for your exposures, threats, and resources, so you can analyze them over time. 

#### Trends overview widget
<a name="w2aab7c29b7b5b5"></a>

![Example of trends overview widget.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/trends-overview-widget.png)


 This widget displays an overview of your exposures, threats, resources, and findings in the following time periods: 
+  **Month-over-month** reflects the period-over-period count for the last two months. 
+  **Week-over-week** reflects the period-over-period count for the past two weeks. 
+  **Day-over-day** reflects the period-over-period count for the past 2 days. 

 The number next to the percentage reflects the average period-over-period count to date. Choosing this number directs you to its corresponding dashboard in the console. If you navigate to another dashboard that displays trends data, the dashboard only displays trends data for the last 90 days or in a best-fit time period if your account does not contain findings or resources older than 30 days. 

**Note**  
 To receive data in this widget, you must enable the following security services:   
 **AWS Security Hub CSPM** – To receive data about exposures 
 **Amazon Inspector** – To receive data about exposures 
 **GuardDuty** – To receive data about threats 

#### Exposure finding trends widget
<a name="w2aab7c29b7b5b7"></a>

![Example of exposure finding trends widget.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/exposure-finding-trends-widget.png)


 This widget displays the severity of your exposure findings in the following time periods: 
+  **5 days** 
+  **30 days** 
+  **90 days** 
+  **6 months** 
+  **1 year** 

 The visualization displays the average count of your findings over the selected time period. 

**Severity filters**  
 You can update the graph by including or excluding the following severity filters: 
+  **Fatal** 
+  **Critical** 
+  **High** 
+  **Medium** 
+  **Low** 
+  **Informational** 
+  **Other** 
+  **Unknown** 

 Applied severity filters show at the bottom of the visualization in different boxes. You can hover over the visualization to review the average count of findings for specific points in time. You can also review the average count of findings that match each applied severity filter. 

 You can choose **View all current exposure findings** to be directed to the **Exposure** dashboard. By default, the **Exposure** dashboard only displays trends data for the last 90 days. If your account does not contain exposure findings older than 30 days, the dashboard displays trends data based on a best-fit time period. 

**Note**  
 To receive data in this widget, you must enable [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting_started.html) and [Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html). 

#### Threat finding trends widget
<a name="w2aab7c29b7b5b9"></a>

![Example of threat finding trends widget.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/threat-finding-trends-widget.png)


 This widget displays the severity of your threat findings in the following time periods: 
+  **5 days** 
+  **30 days** 
+  **90 days** 
+  **6 months** 
+  **1 year** 

 The visualization displays the average count of your findings over the selected time period. 

**Severity filters**  
 You can update the graph by including or excluding the following severity filters: 
+  **Fatal** 
+  **Critical** 
+  **High** 
+  **Medium** 
+  **Low** 
+  **Informational** 
+  **Other** 
+  **Unknown** 

 Applied severity filters show at the bottom of the visualization in different boxes. You can hover over the visualization to review the average count of findings for specific points in time. You can also review the average count of findings that match each applied severity filter. 

 You can choose **View all current threat findings** to be directed to the **Exposure** dashboard. By default, the **Threats** dashboard only displays trends data for the last 90 days. If your account does not contain threat findings older than 30 days, the dashboard displays trends data based on a best-fit time period. 

**Note**  
 To receive data in this widget, you must enable [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html). 

#### Resource trends widget
<a name="w2aab7c29b7b5c11"></a>

![Example of resource trends widget.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/resource-trends-widget.png)


 This widget displays an inventory of your resources in the following time periods: 
+  **5 days** 
+  **30 days** 
+  **90 days** 
+  **6 months** 
+  **1 year** 

 The visualization displays the average count of your resources over the selected time period. You can hover over the visualization to review the average count of resources for specific points in time. 

 You can choose **View current resources** to be directed to the **Resources** dashboard. By default, the **Resources** dashboard only displays trends data for the last 90 days. If your account does not contain resources older than 30 days, the dashboard displays trends data based on a best-fit time period. 

 This widget displays an inventory of your resources in the following time periods: 
+  **5 days** 
+  **30 days** 
+  **90 days** 
+  **6 months** 
+  **1 year** 

#### Data retention for trends
<a name="w2aab7c29b7b5c13"></a>

 Security Hub retains trends data for one year for all AWS accounts where Security Hub is enabled. After trends data has been retained for one year, it is deleted from Security Hub. 

 Trends data for delegated administrator and standalone accounts is deleted after Security Hub is disabled, or if the accounts are terminated. 

 Trends data retention scenarios for member accounts with Security Hub enabled: 
+  If a member account leaves its organization, Security Hub still stores the trends data, up to when the account left the organization, for a year. 
+  If Security Hub is disabled for a member account, Security Hub retains the trends data, up to when the account was disabled, for a year. 
+  If a member account is terminated, Security Hub disassociates the trends data from the terminated account (for example, scrubbing the terminated account ID) and retains the rest of the trends data for one year. 

### Summary widgets
<a name="w2aab7c29b7b7"></a>

 The following widgets display a summary of your exposures, threats, and resources. 

#### Exposure summary widget
<a name="security-hub-v2-dashboard-exposure-widget"></a>

![Example of exposure summary coverage widget.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/exposure-summary-widget-operations.png)


 This widget displays your exposures by severity. An exposure is based on an analysis of findings and traits from Security Hub and other AWS security services, such as Amazon Inspector. The list of exposures in this widget is limited to the eight exposures with the highest severity. Exposures with greater severity appear first in the list. If two or more exposures are of equal severity, the list automatically groups those exposures behind more recent exposures. Choosing **View all exposures** directs you to the **Exposure** dashboard. 

**Note**  
 To receive data in this widget, you must enable [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting_started.html) and [Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html). 

#### Threat summary widget
<a name="security-hub-v2-dashboard-threat-widget"></a>

![Example of threat summary widget.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/threat-summary-widget-operations.png)


 This widget displays your threats by severity. A threat refers to malicious activity or suspicious activity that can compromise the security of your environment. The list of threats in this widget is limited to the eight threats with the highest severity. Threats with greater severity appear first in the list. If two or more threats are of equal severity, the list automatically groups those threats behind more recent threats. Choosing **View all threats** directs you to the **Threats** dashboard. 

**Note**  
 To receive data in this widget, you must [enable GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html). 

#### Resource summary widget
<a name="security-hub-v2-dashboard-resource-widget"></a>

![Example of resource summary widget.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/resource-summary-widget-operations.png)


 This widget displays resources by type and findings associated with resources. Resources are prioritized by exposures and attack sequences. Choosing **View all resources** directs you to the **Resource** dashboard. 

#### Security coverage widget
<a name="security-hub-v2-dashboard-coverage-widget"></a>

![Screenshot of the Security Hub Advanced security coverage widget showing account coverage percentages by security capability.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/security-coverage-widget2.png)


 The widget displays a summary of your account coverage for the following security capabilities: 
+  Vulnerability management by Amazon Inspector 
+  Threat detection by Amazon GuardDuty 
+  Sensitive data discovery by Amazon Macie 
+  Posture management by AWS Security Hub CSPM 

 In delegated administrator accounts, the widget also displays account coverage for Security Hub enablement. 

 Each coverage item shows a percentage representing that capability's enablement across your accounts. Choosing a percentage displays details about coverage for that capability. Choosing the **Security Hub enablement** percentage displays a side panel. The panel shows how many accounts are enabled in each Region across your organization. 

 In the **Services coverage** section, percentages represent the proportion of coverage checks that passed for each security capability. These checks span the accounts and Regions where Security Hub is enabled. Choosing a coverage percentage displays a popover that breaks down each feature as **Covered** (check passed) or **Not covered** (check failed). Percentages are rounded down to the nearest whole number. Choosing any percentage in the popover opens the coverage findings page with details about the findings that make up that percentage. Choose **Configure** to open the individual service where you can manage the configuration for that capability, or to open the Security Hub configurations page where you can update your configurations for security services. 

 If any of your coverage findings in Security Hub are suppressed, the widget displays a message informing you that coverage has been excluded: *Coverage for security capabilities has been excluded through suppressed coverage findings*. 

 For more information about viewing and suppressing coverage findings, see [Coverage findings in Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/coverage-findings.html). 

## Available filters
<a name="w2aab7c29b9"></a>

 You can apply filters to security widgets using the **Add filter bar**. 

![Example of summary filters.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/summary-filters.png)


 Filters are organized in the following categories: 
+  **Shared filters** – applies to all security widgets 
+  **Finding filters** – applies to security widgets that display finding data 
+  **Resource filters** – applies to security widgets that display resource data 

 You can create a filter set by connecting filters using the **and**/**or** operators and then choosing **Save new filter set** in the dropdown. 

### Filters applied to the Exposure finding trends widget and Threat finding trends widget
<a name="w2aab7c29b9c13"></a>

 Currently, the filters supported for these widgets include the following: 
+  **Account ID** 
+  **Finding class name** 
+  **Finding type** 
+  **Product name** 
+  **Region** 
+  **Status** 

### Filters applied to the Resource trends widget
<a name="w2aab7c29b9c15"></a>

 Currently, the filters supported for this widget include the following: 
+  **Account ID** 
+  **Region** 
+  **Resource category** 
+  **Resource type** 

### Filters not applied to widgets
<a name="w2aab7c29b9c17"></a>

![Example of summary filter that cannot be applied.](http://docs.aws.amazon.com/securityhub/latest/userguide/images/filter-not-applied.png)


 If a widget does not support a filter, the filter is not applied to the widget. In this case, the widget displays a warning message letting you know how many filters were not applied and lists the names of which filters it does not support. 