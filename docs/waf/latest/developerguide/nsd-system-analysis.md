**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Run a network analysis

###### Note

Network security director only supports up to 300,000 resources per account at this time. See [AWS Shield network security director Quotas](../../../network-director/limits.md "../../../network-director/limits.md")

To begin using network security director, run a network analysis. When you run a network analysis, network security director identifies and retrieves security information relevant to your resources.

###### To run network analysis in network security director

1. Sign in to the AWS Management Console and open the AWS Shield network security director console at [https://console.aws.amazon.com/wafv2/network-director/](https://console.aws.amazon.com/wafv2/network-director/ "https://console.aws.amazon.com/wafv2/network-director/").
2. From the network security director home page, choose **Get started**.
3. In the network security director Getting started page, choose **Start a network analysis**.
   After you start a network analysis, the network security director Dashboard appears. Depending on the number of networking resources in your environment, it may take a few minutes for your network analysis to complete.

During the network analysis, network security director analyzes your compute and networking resources for potential security findings.
AWS Shield network security director uses the results of your most recent network analysis to populate the Dashboard and other parts of the console with relevant security findings.
When you run a new network analysis, network security director displays the newest findings across the console.

After your first network analysis completes, continue to [Identify resources with security issues](nsd-findings.md "nsd-findings.md") to learn how to understand and interpret your results.
