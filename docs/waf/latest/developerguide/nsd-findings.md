**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Exploring resources and findings

The AWS Shield network security director dashboard provides a summary of the most severe findings, a comparison of findings by included regions, a table of accounts that have been analyzed, a panel that appears when an account is selected, and a network topology that populates once a resource within that panel is selected.

###### Note

You must sign in with delegated administrator credentials to view resources and findings on the network security director dashboard.

## To identify which accounts have findings

1. Sign in with your delegated administrator account and open the AWS Shield network security director console at [https://console.aws.amazon.com/wafv2/network-security-director/](https://console.aws.amazon.com/wafv2/network-security-director/ "https://console.aws.amazon.com/wafv2/network-security-director/").
2. In the navigation pane, under network security director, choose **Dashboard**.
3. The Summary dashboard displays with the following widgets.

### Regions Widget

The Regions widget highlights the **most critical findings**, which are a representation of all the findings on resources and their combined severity. Next to it is a chart that includes the current region and provides a comparative summary of finding severities across all enabled regions. This allows for quick identification of critical issues by region and an indicator that you may need to switch regions if there are findings in that region to review.

### Accounts Widget

Accounts that are analyzed in the current region appear in the table with the default sort set to show accounts with resources by the highest composite finding severities. You can select an account to open a panel that displays resources by their composite finding severity.

### To identify which resources have findings

1. From the network security director Dashboard, navigate to the **Accounts** widget.
2. Select the account which shows the number of composite severity findings.
3. This will open the resources in the **Account and topology explorer** panel widget.

To identify your affected resources and find specific remediation recommendations, see the following sections.

When a network analysis completes, network security director provides detailed recommendations to remediate vulnerabilities identified in resource findings. You can filter for any vulnerable resource based on **Resource ID**, **Severity level**, **Resource type**, or associated **Findings**. By default, the **Resources** table displays resources in order of highest to lowest severity.

### Account and topology explorer panel widget

When an account is selected the account and topology explorer panel widget opens to display the resources and findings within that account. Filter the table within to find specific resources or findings or remove filters to see a summary of resources types and finding types.

AWS Shield network security director assigns severity levels to each finding from the most recent network analysis. Resources can be assigned **None**, **Informational**, **Low**, **Medium**, **High**, or **Critical**. This severity level represents the severity level of the most severe finding identified on a resource. For example, if your latest network analysis determines that your Amazon Amazon EC2 instance has one Medium severity finding and two Low severity findings, that resource is assigned a Medium composite finding severity level.

The **Findings overview** widget inside the **Account and topology explorer panel widget**, which can be accessed by removing any resource or finding type filters, provides two ways to understand the findings that network security director found in your resources:

- From **Highest severity resources**, you can quickly understand which severity level is the most severe across all your networking resources. You can also see a list of how many of your resources are affected and the number of resources assigned each severity level by network security director.
- From **Severity distribution**, you can view the number of resources with a specific severity level for each resource type and compare it with those of other resource types.

### To explore your network topology

1. In the navigation pane, under network security director, choose **Dashboard**.
2. From the network security director Dashboard, navigate to the **Accounts** widget.
3. Select the account which shows the number of composite severity findings.
4. This will open the resources in the **Account and topology explorer** panel widget.

AWS Shield network security director maps the connections of your resources during its analyses. These connections are visualized in a network topology that is shown in a widget on the dashboard below the **Accounts** widget. When you select an account, and then select a resource in the **Account and topology explorer** panel widget, the network topology visualization appears in the context of the selected resource.

### Network topology widget

The network topology exists in an empty state until a specific resource has been selected in the Account and topology explorer panel widget which appears when an account has been selected in the **Accounts** table widget. The network topology can be navigated by dragging the canvas, or by using the zoom controls in the lower right corner of the container. There are also controls for resetting the zoom and location of the canvas along with exporting its contents. The topology can be refreshed in the case of updated analysis findings and can also expand its view to display the topology across the entire screen. Select a resource in the topology to view its details in the **Account and topology explorer** panel widget. Select a resource edge connection to learn more about the nature of the relationship between two resources in the topology.

###### Note

The network topology is built by traversing from the selected resource to its connected network resources. Only the first 100 connected resources are displayed in the topology visualization, sorted by severity. This sorting is applied only to the initial set of 100 fetched results, not the complete dataset.

### To find recommendations for improving your security

1. From the network security director Dashboard, navigate to the **Accounts** widget.
2. Select the account which shows the number of composite severity findings.
3. This will open the resources in the **Account and topology explorer** panel widget.
4. Selecting a resource in the widget displays its details, with an option to navigate directly to the full **Resource Details page** for deeper investigation.

A resource can have multiple findings identified by network security director. Each finding represents a security issue found during your most recent network analysis.

- Expand the **Remediation recommendations** for the finding to learn more about it.
- Follow the steps suggested by network security director or choose the documentation link included to learn more.

After reviewing and implementing the remediation recommendations for your affected resources, you may want to get additional insights about your overall security configuration. Continue to [Analyze network security with Amazon Q Developer](nsd-security-insights.md "nsd-security-insights.md") to learn how to use Amazon Q Developer for further analysis.
