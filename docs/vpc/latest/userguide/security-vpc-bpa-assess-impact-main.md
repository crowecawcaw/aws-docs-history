

# Assess impact of VPC BPA and monitor VPC BPA
<a name="security-vpc-bpa-assess-impact-main"></a>

This section contains information on you can assess the impact of VPC BPA before you turn it on and how you monitor if traffic is being blocked after you turn it on.

**Topics**
+ [Assess the impact of VPC BPA using Network Access Analyzer](#security-vpc-bpa-assess-impact)
+ [Monitor VPC BPA impact with flow logs](#security-vpc-bpa-fl)
+ [Track exclusion deletion with CloudTrail](#security-vpc-bpa-cloudtrail)
+ [Verify connectivity is blocked with Reachability Analyzer](#security-vpc-bpa-verify-RA)

## Assess the impact of VPC BPA using Network Access Analyzer
<a name="security-vpc-bpa-assess-impact"></a>

In this section, you'll use Network Access Analyzer to view the resources in your account that use an internet gateway *before* you enable VPC BPA and block access. Use this analysis to understand the impact of turning on VPC BPA in your account and blocking traffic.

**Note**  
Network Access Analyzer does not support IPv6; so you will not be able to use it to view the potential impact of VPC BPA on egress-only internet gateway outbound IPv6 traffic.
You are charged for the analyses you perform with Network Access Analyzer. For more information, see [Pricing](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html#pricing) in the *Network Access Analyzer Guide*.
For information about the regional availability of Network Access Analyzer, see [Limitations](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/how-network-access-analyzer-works.html#analyzer-limitations) in the *Network Access Analyzer Guide*.

------
#### [ AWS Management Console ]

1. Open the AWS Network Insights console at [https://console.aws.amazon.com/networkinsights/](https://console.aws.amazon.com/networkinsights/).

1. Choose **Network Access Analyzer**.

1. Choose **Create Network Access Scope**.

1. Choose **Assess impact of VPC Block Public Access** and choose **Next**.

1. The template is already configured to analyze traffic to and from the internet gateways in your account. You can view this under **Source** and **Destination**.

1. Choose **Next**.

1. Choose **Create Network Access Scope**.

1. Choose the scope you just created and choose **Analyze**.

1. Wait for the analysis to complete.

1. View the findings of the analysis. Each row under **Findings** shows a network path that a packet can take in a network to or from an internet gateway in your account. In this case, if you turn on VPC BPA and none of the VPCs and or subnets that appear in these findings are configured as VPC BPA exclusions, traffic to those VPCs and subnets will be restricted.

1. Analyze each finding to understand the impact of VPC BPA on resources in your VPCs.

The impact analysis is complete.

------
#### [ AWS CLI ]

1. Create a network access scope:

   ```
   aws ec2 create-network-insights-access-scope --region us-east-2 --match-paths "Source={ResourceStatement={ResourceTypes=["AWS::EC2::InternetGateway"]}}" "Destination={ResourceStatement={ResourceTypes=["AWS::EC2::InternetGateway"]}}"
   ```

1. Start the scope analysis:

   ```
   aws ec2 start-network-insights-access-scope-analysis  --region us-east-2 --network-insights-access-scope-id nis-id
   ```

1. Get the results of the analysis:

   ```
   aws ec2 get-network-insights-access-scope-analysis-findings  --region us-east-2 --network-insights-access-scope-analysis-id nisa-0aa383a1938f94cd1 --max-items 1
   ```

   The results show the traffic to and from the internet gateways in all the VPCs in your account. The results are organized as "findings". "FindingId": "AnalysisFinding-1" indicates that this is the first finding in the analysis. Note that there are multiple findings and each indicates a traffic flow that will be impacted by turning on VPC BPA. The first finding will show that traffic started at an internet gateway ("SequenceNumber": 1), passed to an NACL ("SequenceNumber": 2) to a security group ("SequenceNumber": 3) and ended at an instance ("SequenceNumber": 4).

1. Analyze the findings to understand the impact of VPC BPA on resources in your VPCs.

The impact analysis is complete.

------

## Monitor VPC BPA impact with flow logs
<a name="security-vpc-bpa-fl"></a>

VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from Elastic network interfaces in your VPC. You can use this feature to monitor traffic that is blocked by VPC BPA from reaching your instance network interfaces.

Create a flow log for your VPC using the steps in [Work with flow logs](working-with-flow-logs.md). 

When you create the flow log, make sure you use a custom format that includes the field `reject-reason`.

When you view the flow logs, if traffic to an ENI is rejected due to VPC BPA, you'll see a `reject-reason` of `BPA` in the flow log entry.

In addition to the standard [limitations](flow-logs-limitations.md) for VPC flow logs, note the following limitations specific to VPC BPA:
+ Flow logs for VPC BPA do not include [skipped records](flow-logs-records-examples.md#flow-log-example-no-data).
+ Flow logs for VPC BPA do not include [`bytes`](flow-log-records.md#flow-logs-fields) even if you include the `bytes` field in your flow log.

## Track exclusion deletion with CloudTrail
<a name="security-vpc-bpa-cloudtrail"></a>

This section explains how you can use AWS CloudTrail to monitor and track the deletion of VPC BPA exclusions.

------
#### [ AWS Management Console ]

You can view any deleted exclusions in the **CloudTrail Event history** by looking up **Resource type** > `AWS::EC2::VPCBlockPublicAccessExclusion` in the AWS CloudTrail console at [https://console.aws.amazon.com/cloudtrailv2/](https://console.aws.amazon.com/cloudtrailv2/).

------
#### [ AWS CLI ]

You can use the `lookup-events` command to view the events related to deleting exclusions:

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::EC2::VPCBlockPublicAccessExclusion
```

------

## Verify connectivity is blocked with Reachability Analyzer
<a name="security-vpc-bpa-verify-RA"></a>

[VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) can be used to evaluate whether or not certain network paths can be reached given your network configuration, including VPC BPA settings.

For information about the regional availability of Reachability Analyzer, see [Considerations](https://docs.aws.amazon.com/vpc/latest/reachability/how-reachability-analyzer-works.html#considerations) in the *Reachability Analyzer Guide*.

------
#### [ AWS Management Console ]

1. Open the AWS Network Insights console at [https://console.aws.amazon.com/networkinsights/home#ReachabilityAnalyzer](https://console.aws.amazon.com/networkinsights/home#ReachabilityAnalyzer).

1. Choose **Create and analyze path**.

1. For the **Source Type**, choose **Internet Gateways** and select the internet gateway you want to block traffic from the **Source dropdown**.

1. For the **Destination Type**, choose **Instances** and select the instance you want to block traffic to from the **Destination** dropdown.

1. Choose **Create and analyze path**.

1. Wait for the analysis to complete. It could take a few minutes.

1. Once complete, you should see that the **Reachability Status** is **Not reachable** and that the **Path details** shows that `VPC_BLOCK_PUBLIC_ACCESS_ENABLED `is the cause of this reachability issue.

------
#### [ AWS CLI ]

1. Create a network path using the ID of the Internet Gateway you want to block traffic from (source) and the ID of the instance you want to block traffic to (destination):

   ```
   aws ec2 --region us-east-2 create-network-insights-path --source igw-id --destination instance-id --protocol TCP
   ```

1. Start an analysis on the network path:

   ```
   aws ec2 --region us-east-2 start-network-insights-analysis --network-insights-path-id nip-id
   ```

1. Retrieve the results of the analysis:

   ```
   aws ec2 --region us-east-2 describe-network-insights-analyses --network-insights-analysis-ids nia-id
   ```

1. Verify that `VPC_BLOCK_PUBLIC_ACCESS_ENABLED` is the `ExplanationCode` for the lack of reachability.

------