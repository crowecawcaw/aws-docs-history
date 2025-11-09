# Analyzing stateless rule groups in AWS Network Firewall

Network Firewall can analzye stateless rule groups for rules that might adversely effect your firewall's functionality. For example, Network Firewall can identify rules that route traffic asymmetrically, which can impact the service's ability to properly process traffic. During analysis, the service includes any identfied rules in a list of analysis results. You can analyze your stateless rule groups and view the analysis results using the console or API.

Console
**To analyze a stateless rule group**

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.
3. During stateless rule group creation, after you add one or more rules to the rule group, if you select **Analyze**, Network Firewall analyzes the rules in the rule group. If the service determines that any of the rules have the behavior outlined in the following section, Network Firewall displays the identified rule's priority number and the type of identified behavior.

API
Include `AnalyzeRuleGroup` in your [CreateRuleGroupRequest](../APIReference/API_CreateRuleGroup.md "../APIReference/API_CreateRuleGroup.md"), [DescribeRuleGroup](../APIReference/API_DescribeRuleGroup.md "../APIReference/API_DescribeRuleGroup.md"), or [UpdateRuleGroupRequest](../APIReference/API_DescribeRuleGroup.md "../APIReference/API_DescribeRuleGroup.md") request. Network Firewall lists the results in `AnalysisResults` in the response.

To analyze the rule group without creating, describing, or updating the rule group, use the `DryRun` parameter.

CLI
Include `--analyze-rule-group` in your [create-rule-group](../../../cli/latest/reference/network-firewall/create-rule-group.md "../../../cli/latest/reference/network-firewall/create-rule-group.md"), [describe-rule-group](../../../cli/latest/reference/network-firewall/describe-rule-group.md "../../../cli/latest/reference/network-firewall/describe-rule-group.md"), or [update-rule-group](../../../cli/latest/reference/network-firewall/update-rule-group.md "../../../cli/latest/reference/network-firewall/update-rule-group.md") request. Network Firewall lists the results in `AnalysisResults` in the response.

To analyze the rule group without creating, describing, or updating the rule group, use the `--dry-run` parameter.

The following table lists the types of rule behavior that Network Firewall analyzes your rule groups for, as well as the details about the cause and solution.

| Rule behavior             | Cause                                                                                                                                                                                                                                                                          | Mitigation                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Forwarding asymmetrically | One or more stateless rules with the action `pass` or `forward` are forwarding traffic asymmetrically. Specifically, the rule's set of source IP addresses or their associated port numbers, don't match the set of destination IP addresses or their associated port numbers. | Make sure that there's an existing return path. For example, if the rule allows traffic from source 10.1.0.0/24 to destination 20.1.0.0/24, you should allow return traffic from source 20.1.0.0/24 to destination 10.1.0.0/24.                                                                                                                                               |
| Contains TCP flags        | At least one stateless rule with<br>the action `pass` or<br>`forward` contains TCP flags that are<br>inconsistent in the forward and return<br>directions.                                                                                                                     | Prevent asymmetric routing issues<br>caused by TCP flags by following these actions:<br>• Remove unnecessary TCP flag inspections from the<br>rules.<br>• If you need to inspect TCP flags, check<br>that the rules correctly account for changes in<br>TCP flags throughout the TCP connection cycle, for<br>example `SYN` and `ACK`<br>flags used in a 3-way TCP handshake. |
