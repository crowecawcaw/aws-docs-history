**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Identify resources with security issues

AWS Shield network security director assigns severity levels to each finding from the most recent network analysis. Resources can be assigned NONE, INFORMATIONAL, LOW, MEDIUM, HIGH, or CRITICAL.
This severity level represents the severity level of the most severe finding identified on a resource.
For example, if your latest network analysis determines that your Amazon EC2 instance has one Medium level finding and two Low severity findings, that resource is assigned a Medium severity level.

The results of your network analysis are available for you to view in the network security director console using various data visualization options.

The **Findings overview** widget provides two ways to understand the findings that network security director found in your resources:

- From **Highest severity resources**, you can quickly understand which severity level is the most severe across all your networking resources. You can also see a list of how many of your resources are affected and the number of resources assigned each severity level by network security director.
- From **Severity distribution**, you can view the number of resources with a specific severity level for each resource type and compare it with those of other resource types.

###### To identify which resources have findings

1. Sign in to the AWS Management Console and open the AWS Shield network security director console at [https://console.aws.amazon.com/wafv2/network-director/](https://console.aws.amazon.com/wafv2/network-director/ "https://console.aws.amazon.com/wafv2/network-director/").
2. From the network security director Dashboard, navigate to the **Findings overview** widget.
3. Note the severity level displayed and the number of findings assigned that severity level.
4. From the list of findings identified, choose the item that matches what you noted in the previous step.

The **Resources** page opens for you to begin further investigation into your highest severity resources.
After identifying your affected resources, proceed to [Find remediation steps for your highest severity resources](nsd-remediation-steps.md "nsd-remediation-steps.md") to learn how to find specific remediation recommendations for your most impacted resources.
