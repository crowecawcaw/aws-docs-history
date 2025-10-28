**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Find remediation steps for your highest severity resources

When a network analysis completes, network security director provides detailed recommendations to remediate vulnerabilities identified in resource findings. You can filter for any vulnerable resource based on **Resource ID**, **Severity level**, **Resource type**, or associated **Findings**. By default, the **Resources** table displays resources in order of highest to lowest severity.

###### To find recommendations for improving your security

1. Sign in to the AWS Management Console and open the AWS Shield network security director console at [https://console.aws.amazon.com/wafv2/network-director/](https://console.aws.amazon.com/wafv2/network-director/ "https://console.aws.amazon.com/wafv2/network-director/").
2. From the network security director home page, choose **Resources**.
3. From the table, view and optionally filter your networking resources.
4. Sort resources by **Severity level** from highest to lowest severity.
5. Choose any resource assigned to the highest severity level to open the detailed view for it.
6. In the **Findings** widget, locate any findings with the highest severity level assigned to them.

A resource can have multiple findings identified by network security director. Each finding represents a security issue found during your most recent network analysis. 7. Expand the **Remediation recommendations** for the finding. 8. Follow the steps suggested by network security director or choose the documentation link included to learn more.
After reviewing and implementing the remediation recommendations for your affected resources, you may want to get additional insights about your overall security configuration. Continue to [Analyze network security with Amazon Q Developer](nsd-security-insights.md "nsd-security-insights.md") to learn how to use Amazon Q Developer for further analysis.
