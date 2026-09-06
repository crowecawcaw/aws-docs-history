

# Analyzing stateless rule groups in AWS Network Firewall
<a name="stateless-rule-group-analyzer"></a>

Network Firewall can analzye stateless rule groups for rules that might adversely effect your firewall's functionality. For example, Network Firewall can identify rules that route traffic asymmetrically, which can impact the service's ability to properly process traffic. During analysis, the service includes any identfied rules in a list of analysis results. You can analyze your stateless rule groups and view the analysis results using the console or API.

------
#### [ Console ]

**To analyze a stateless rule group**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.

1. During stateless rule group creation, after you add one or more rules to the rule group, if you select **Analyze**, Network Firewall analyzes the rules in the rule group. If the service determines that any of the rules have the behavior outlined in the following section, Network Firewall displays the identified rule's priority number and the type of identified behavior.

------
#### [ API ]

Include `AnalyzeRuleGroup` in your [CreateRuleGroupRequest](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateRuleGroup.html), [DescribeRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroup.html), or [UpdateRuleGroupRequest](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroup.html) request. Network Firewall lists the results in `AnalysisResults` in the response.

To analyze the rule group without creating, describing, or updating the rule group, use the `DryRun` parameter.

------
#### [ CLI ]

Include `--analyze-rule-group` in your [create-rule-group](https://docs.aws.amazon.com/cli/latest/reference/network-firewall/create-rule-group.html), [describe-rule-group](https://docs.aws.amazon.com/cli/latest/reference/network-firewall/describe-rule-group.html), or [update-rule-group](https://docs.aws.amazon.com/cli/latest/reference/network-firewall/update-rule-group.html) request. Network Firewall lists the results in `AnalysisResults` in the response.

To analyze the rule group without creating, describing, or updating the rule group, use the `--dry-run` parameter.

------

The following table lists the types of rule behavior that Network Firewall analyzes your rule groups for, as well as the details about the cause and solution.


| Rule behavior | Cause | Mitigation | 
| --- | --- | --- | 
| Forwarding asymmetrically | One or more stateless rules with the action `pass` or `forward` are forwarding traffic asymmetrically. Specifically, the rule's set of source IP addresses or their associated port numbers, don't match the set of destination IP addresses or their associated port numbers. | Make sure that there's an existing return path. For example, if the rule allows traffic from source 10.1.0.0/24 to destination 20.1.0.0/24, you should allow return traffic from source 20.1.0.0/24 to destination 10.1.0.0/24. | 
| Contains TCP flags | At least one stateless rule with the action `pass` or `forward` contains TCP flags that are inconsistent in the forward and return directions. | Prevent asymmetric routing issues caused by TCP flags by following these actions:+ Remove unnecessary TCP flag inspections from the rules.<br />+ If you need to inspect TCP flags, check that the rules correctly account for changes in TCP flags throughout the TCP connection cycle, for example `SYN` and `ACK` flags used in a 3-way TCP handshake. | 