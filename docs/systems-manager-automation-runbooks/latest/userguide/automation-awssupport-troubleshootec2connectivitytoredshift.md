

# `AWSSupport-TroubleshootEC2ConnectivityToRedshift`
<a name="automation-awssupport-troubleshootec2connectivitytoredshift"></a>

The `AWSSupport-TroubleshootEC2ConnectivityToRedshift` runbook provides comprehensive troubleshooting for Amazon Elastic Compute Cloud (Amazon EC2) instances that cannot connect to Amazon Redshift clusters. It systematically analyzes network connectivity paths, security configurations, and provides detailed remediation recommendations.

The runbook supports the following connectivity scenarios:
+ **Same Amazon VPC connectivity** - Direct connection within the same Amazon Virtual Private Cloud (Amazon VPC).
+ **Cross-Amazon VPC connectivity** - Connection across different VPCs using Amazon VPC peering or AWS Transit Gateway.
+ **Public vs private Amazon Redshift clusters** - Different connectivity patterns based on cluster accessibility.
+ **Internet-based access** - Amazon EC2 instances connecting to publicly accessible Amazon Redshift clusters via Internet Gateway or NAT Gateway.

The runbook uses Amazon VPC Reachability Analyzer as the primary diagnostic tool to quickly identify connectivity issues between the Amazon EC2 instance and the Amazon Redshift cluster. If Reachability Analyzer is not supported in your AWS Region or fails for any reason, the runbook automatically falls back to comprehensive standard connectivity checks covering security groups, network ACLs, route tables, and DNS configuration.

**Important**  
Running this runbook creates a Reachability Analyzer analysis in your account, which incurs a per-analysis charge. For more information, see the **Network Analysis** section in [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/).  
This runbook creates a network insights path and network insights analysis in your account using Reachability Analyzer. If the runbook completes successfully, these resources are deleted. If the cleanup step fails, the network insights path is not deleted and you must delete it manually. If you don't delete the network insights path manually, it continues to count towards the quota for your AWS account. For more information, see [Quotas for Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/reachability-analyzer-limits.html).  
Operating system-level configurations such as the use of a firewall, proxy, local DNS resolver, or hosts file can affect connectivity even if the Reachability Analyzer returns a status of `PASS`.  
Review the evaluation of all checks performed by the analyzer. If any check returns a status of `FAIL`, that might affect connectivity even if the overall reachability check returns a status of `PASS`.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEC2ConnectivityToRedshift) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:CreateNetworkInsightsPath`
+ `ec2:DeleteNetworkInsightsAnalysis`
+ `ec2:DeleteNetworkInsightsPath`
+ `ec2:DescribeInstances`
+ `ec2:DescribeInternetGateways`
+ `ec2:DescribeNatGateways`
+ `ec2:DescribeNetworkAcls`
+ `ec2:DescribeNetworkInsightsAnalyses`
+ `ec2:DescribeNetworkInsightsPaths`
+ `ec2:DescribeNetworkInterfaces`
+ `ec2:DescribeRouteTables`
+ `ec2:DescribeSecurityGroups`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeTransitGatewayVpcAttachments`
+ `ec2:DescribeTransitGateways`
+ `ec2:DescribeVpcAttribute`
+ `ec2:DescribeVpcEndpoints`
+ `ec2:DescribeVpcPeeringConnections`
+ `ec2:DescribeVpcs`
+ `ec2:StartNetworkInsightsAnalysis`
+ `redshift:DescribeClusterSubnetGroups`
+ `redshift:DescribeClusters`

Example IAM policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInsightsPath",
                "ec2:DeleteNetworkInsightsAnalysis",
                "ec2:DeleteNetworkInsightsPath",
                "ec2:DescribeInstances",
                "ec2:DescribeInternetGateways",
                "ec2:DescribeNatGateways",
                "ec2:DescribeNetworkAcls",
                "ec2:DescribeNetworkInsightsAnalyses",
                "ec2:DescribeNetworkInsightsPaths",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeTransitGatewayVpcAttachments",
                "ec2:DescribeTransitGateways",
                "ec2:DescribeVpcAttribute",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeVpcPeeringConnections",
                "ec2:DescribeVpcs",
                "ec2:StartNetworkInsightsAnalysis",
                "redshift:DescribeClusterSubnetGroups",
                "redshift:DescribeClusters"
            ],
            "Resource": "*"
        }
    ]
}
```

Follow these steps to configure the automation:

1. Open [AWSSupport-TroubleshootEC2ConnectivityToRedshift](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEC2ConnectivityToRedshift/description) in Systems Manager under Documents.

1. Choose Execute automation.

1. For the input parameters, enter the following:
   + **AutomationAssumeRole (Optional):**

     The AWS Identity and Access Management (IAM) role ARN that allows Systems Manager Automation to perform actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.

     Type: `AWS::IAM::Role::Arn`
   + **SourceInstance (Required):**

     The Amazon EC2 instance ID experiencing connectivity issues with the Amazon Redshift cluster.

     Type: `AWS::EC2::Instance::Id`

     Allowed pattern: `^i-[0-9a-f]{8,17}$`
   + **ClusterIdentifier (Required):**

     The Amazon Redshift cluster identifier for connectivity troubleshooting.

     Type: String

     Allowed pattern: `^[a-z][a-z0-9-]*[a-z0-9]$`

1. Choose Execute.

1. The automation initiates.

1. The document performs the following steps:
   + **`CollectEC2Metadata`**: Collects comprehensive metadata about the Amazon EC2 instance including Amazon VPC configuration, subnet details, IP addresses, security groups, and instance state.
   + **`InitializeInstanceIP`**: Initializes the source IP variable with the Amazon EC2 instance's private IP address. This variable is updated dynamically throughout the troubleshooting process based on the determined connectivity path.
   + **`AnalyzeEC2SubnetType`**: Analyzes the Amazon EC2 instance's subnet routing configuration to determine subnet type and internet connectivity capabilities. Identifies NAT Gateway public IP addresses if present.
   + **`CollectRedshiftMetadata`**: Retrieves comprehensive Amazon Redshift cluster configuration including Amazon VPC details, endpoint information, port configuration, public accessibility settings, security groups, and network interface details.
   + **`CollectRedshiftSubnetInfo`**: Retrieves detailed information about the Amazon Redshift cluster's subnet group configuration including all associated subnets and Amazon VPC details.
   + **`RunReachabilityAnalysis`**: Executes Amazon VPC Reachability Analyzer as the primary diagnostic tool to perform comprehensive network path analysis between the Amazon EC2 instance and Amazon Redshift cluster. Analyzes security groups, network ACLs, route tables, and network interfaces. If this step fails, the runbook falls back to manual connectivity checks starting at `AnalyzeRedshiftSubnetType`.
   + **`BranchOnReachabilityResults`**: Determines the troubleshooting path based on Reachability Analyzer results. If analysis succeeds and finds a network path, proceeds directly to DNS validation. Otherwise, continues with manual troubleshooting.
   + **`AnalyzeRedshiftSubnetType`**: Analyzes the Amazon Redshift cluster's subnet routing configuration to determine subnet type and internet connectivity capabilities.
   + **`BranchOnCompareVpcIds`**: Compares the Amazon VPC IDs of the Amazon EC2 instance and Amazon Redshift cluster. Routes to same-Amazon VPC troubleshooting if both resources share an Amazon VPC; otherwise, proceeds to cross-Amazon VPC analysis.
   + **`ValidateSameVpcRequirements`**: (Same-Amazon VPC path) Validates connectivity requirements by checking that both Amazon EC2 and Amazon Redshift subnets have proper local routing configuration.
   + **`DetectCrossVpcConnectivity`**: (Cross-Amazon VPC path) Detects and analyzes cross-Amazon VPC connectivity methods. Searches for active Amazon VPC peering connections and AWS Transit Gateway attachments.
   + **`ValidateVpcPeeringRouting`**: (VPC peering path) Validates bidirectional routing between the Amazon EC2 and Amazon Redshift VPCs via the peering connection.
   + **`ValidateTransitGatewayRouting`**: (AWS Transit Gateway path) Validates Transit Gateway route configuration by analyzing route tables, associations, and propagations for both Amazon VPC attachments.
   + **`UpdateInstanceIPForPublicAccess`**: (Public access path) Updates the source IP variable with the correct public IP or NAT Gateway IP for security group validation in public access scenarios.
   + **`CheckSecurityGroups`**: Validates security group rules for both the Amazon EC2 instance and Amazon Redshift cluster. Checks inbound rules on Amazon Redshift security groups and outbound rules on Amazon EC2 security groups.
   + **`CheckNetworkACLs`**: Validates network ACL rules for connectivity between Amazon EC2 and Amazon Redshift subnets. Analyzes both inbound and outbound rules including ephemeral port ranges for return traffic.
   + **`ValidateDNSConfiguration`**: Validates DNS configuration settings for both Amazon EC2 and Amazon Redshift VPCs including DNS support, DNS hostnames, and DHCP options sets.
   + **`GenerateFinalReport`**: Generates a comprehensive diagnostic report consolidating all findings, including categorized issue summaries, prioritized remediation steps, network topology analysis, and detailed recommendations.

1. After the automation completes, review the **Outputs** section for the detailed results of the execution.
+ `GenerateFinalReport.DiagnosticReport` - A comprehensive diagnostic report with all findings and remediation recommendations.
+ `GenerateFinalReport.OverallStatus` - The overall connectivity status result.
+ `GenerateFinalReport.IssuesSummary` - A categorized summary of all identified issues.
+ `GenerateFinalReport.InstanceIPFinalValue` - The final source IP address used during the analysis.
+ `GenerateFinalReport.ConnectivityMethod` - The detected connectivity method between the Amazon EC2 instance and Amazon Redshift cluster.

AWS Systems Manager Automation
+  [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEC2ConnectivityToRedshift/description) 
+  [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html) 
+  [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html) 
+  [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/) 