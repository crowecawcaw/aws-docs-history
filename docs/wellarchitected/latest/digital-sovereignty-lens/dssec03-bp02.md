

# DSSEC03-BP02 Verify network security posture through automated analysis
<a name="dssec03-bp02"></a>

 Network misconfigurations can open a path across a jurisdictional boundary that no one intended. Automated network analysis tools examine your configuration to identify which paths are possible, without sending live traffic, so you can find such paths before they are used. For sovereign workloads, this helps you verify that network paths meet your data residency and privacy requirements. 

 **Desired outcome:** 
+  Maintain data sovereignty through continuous automated verification of network paths and boundaries. 

 **Common anti-patterns:** 
+  Relying solely on manual network configuration reviews without automated verification of actual connectivity paths. 
+  Assuming network boundaries are correctly configured without testing reachability scenarios. 
+  Not validating that network configurations block data exfiltration or unauthorized cross-border data flows. 
+  Not verifying that VPC peering, Transit Gateway attachments, or PrivateLink connections don't create unintended cross-jurisdictional network paths. 

 **Benefits of establishing this best practice:** 
+  Identifies network paths that could cross a jurisdictional boundary, so unintended access is found before it is used. 
+  Supports proactive identification of network misconfigurations before they reach production. 
+  Automates complex network analysis that is typically time-intensive and error-prone if performed manually. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Network path verification works across three layers that together produce evidence potentially useful for audits. **Prove** intended paths exist using [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) during design. **Verify** no unintended paths exist using [VPC Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) against the deployed configuration. **Confirm** actual traffic matches intent using [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) at runtime. You can create a flow log for a VPC, a subnet, or a network interface. Each layer's output is retainable audit evidence: a finding from one layer corroborated by the other two is harder to dispute than any single finding alone. 

 Reachability Analyzer and Network Access Analyzer use automated reasoning to analyze the possible network paths from your configuration, rather than by sending packets. Start by defining network access scopes that match your data residency requirements and data export controls. Then establish continuous monitoring for network configuration changes. For compute-layer verification, [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) complements the three layers above with automated network reachability assessments of EC2 instances. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define sovereignty-specific Network Access Scopes:** Use VPC Network Access Analyzer to validate that traffic between a source and destination is blocked as you intended. Create Network Access Scopes that specify prohibited network paths, focusing on cross-jurisdictional data flows. 
   +  Define MatchPaths for network connections that conflict with compliance requirements (for example, cross-border data flows). 
   +  Configure ExcludePaths for legitimate exceptions to security policies. 

    To block unintended traffic leaving a VPC customers may choose to deploy an AWS Network Firewall between their NAT gateway and internet gateway. This pattern is described in [Architecture with an internet gateway and a NAT gateway using AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-igw-ngw.html). Network security controls such as security groups (SGs) and network access control lists (ACLs) provide you with options to control network traffic. However, these controls operate at network and transport layers of the OSI model, and filter traffic based on IP addresses, transport protocols, and ports. With AWS Network Firewall you can inspect traffic and use a list of known bad domains to limit the types of domain names that your applications can access. 

    The following example creates a Network Access Scope that detects any network path from resources in your VPC to internet gateways, without going through NAT Gateway and Network Firewall, which could indicate uncontrolled data egress. It does two things: 
   +  Catches any EC2 instance with a direct path to the IGW, bypassing both the NAT Gateway and Network Firewall entirely (instance in a public subnet or misconfigured route). 
   +  Catches the NAT Gateway reaching the IGW directly. In the correct setup, NAT Gateway traffic should route through the Network Firewall endpoint before reaching the IGW. If the NAT GW subnet route table points directly to the IGW instead of the firewall endpoint, this finding fires. 

   ```
   AWS ec2 create-network-insights-access-scope \
   --match-paths '[
       {
       "Source": {
           "ResourceStatement": {
           "ResourceTypes": ["AWS::EC2::Instance"]
           }
       },
       "Destination": {
           "ResourceStatement": {
           "ResourceTypes": ["AWS::EC2::InternetGateway"]
           }
       }
       },
       {
       "Source": {
           "ResourceStatement": {
           "ResourceTypes": ["AWS::EC2::NatGateway"]
           }
       },
       "Destination": {
           "ResourceStatement": {
           "ResourceTypes": ["AWS::EC2::InternetGateway"]
           }
       }
       }
   ]'
   ```

    After creating the scope, run an analysis to identify any matching paths: 

   ```
   AWS ec2 start-network-insights-access-scope-analysis \
   --network-insights-access-scope-id <scope-id>
   ```

    Review the findings to identify unintended network paths that could allow data to leave your jurisdiction. See [example network access scopes](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/example-scopes.html) for more patterns. 

    **Note:** The code snippet shown above is for illustration only and may not be accurate. Validate against your own network configuration and requirements unique to your workload. 

1.  **Verify connectivity paths using Reachability Analyzer:** Use VPC Reachability Analyzer to verify intended connectivity between specific resources. Reachability Analyzer builds a model of the network configuration and analyzes paths without sending packets. 
   +  VPC Reachability Analyzer is especially useful when you are designing your network. For example, it helps you understand the route that a connection would take if it were allowed to reach the destination. You can use this information to make sure data is encrypted in transit, or apply additional traffic filtering conditions. 
   +  You can also include specific intermediate components in the analysis. For example, you can analyze the path between a source and destination through a specific transit gateway. This makes it particularly useful for security audits, policy enforcement, and compliance verification. 

1.  **Monitor network configuration changes:** Use Amazon EventBridge and AWS Config to detect network configuration changes that could violate data residency requirements, and trigger re-analysis. 
   +  Create [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) to detect changes to VPC peering connections, Transit Gateway attachments, route tables, and security groups. 
   +  Configure [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rules to trigger Network Access Analyzer re-analysis when network configuration changes are detected. 
   +  Set up alerts for new VPC peering connections or Transit Gateway attachments that could create cross-jurisdictional paths. 

1.  **Validate actual traffic patterns with VPC Flow Logs:** VPC Flow Logs provide runtime verification that actual traffic patterns match the expected paths validated by Reachability Analyzer. This bridges the gap between configuration analysis and runtime verification. 
   +  Enable [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) on VPCs, subnets, or network interfaces that handle sovereignty-sensitive data. 
   +  Analyze flow logs to verify that traffic stays within approved jurisdictions. Look for unexpected destination IP ranges that fall outside your approved Regions. 
   +  Use [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs.html) or [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to query flow logs for cross-border traffic patterns. 

    Consider traffic volumes and costs before enabling VPC Flow Logs. Limit flow logs to specific network interfaces (ELB, Amazon RDS, Amazon ElastiCache, Amazon Redshift, NAT gateways, Transit gateways). Consider enabling Amazon GuardDuty. The foundational threat detection [includes monitoring the VPC flow logs](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html#guardduty_vpc) associated with your Amazon EC2 instances. 

1.  **Integrate network analysis into CI/CD pipelines:** Automate network verification as part of your infrastructure deployment process to catch sovereignty violations before they reach production. 
   +  Run Network Access Analyzer scope analyses as a gate in your CI/CD pipeline after infrastructure changes are deployed to a staging environment. 
   +  Use VPC Reachability Analyzer to verify that new network configurations maintain expected connectivity paths and don't introduce cross-jurisdictional routes. 
   +  Fail the pipeline if analysis reveals unintended network paths that conflict with data residency requirements. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC05-BP01 Create network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html) 
+  [SEC05-BP02 Control traffic flow within your network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html) 
+  [SEC05-BP03 Implement inspection-based protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_inspection.html) 
+  [SEC05-BP04 Automate network protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_auto_protect.html) 

 **Related examples:** 
+  [Example network access scopes](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/example-scopes.html) in Network Access Analyzer 
+  [Reachability Analyzer source and destination resources](https://docs.aws.amazon.com/vpc/latest/reachability/how-reachability-analyzer-works.html#source-and-destination-resources) 

 **Related documents:** 
+  [VPC Network Access Analyzer User Guide](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) 
+  [VPC Reachability Analyzer User Guide](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) 
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) 
+  [Amazon Inspector Network Reachability Documentation](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html) 
+  [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) 
+  [Network Security on AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-security-best-practices/network-security.html) 
+  [Automated Reasoning for Network Security](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/how-network-access-analyzer-works.html) 
+  [Network Monitoring and Analysis Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/debugging-tool-for-network-connectivity-from-amazon-vpc/) 
+  [An unexpected discovery](https://aws.amazon.com/blogs/security/an-unexpected-discovery-automated-reasoning-often-makes-systems-more-efficient-and-easier-to-maintain/) 

 **Related videos:** 
+  [AWS re:Inforce 2022 - Validate effective network access controls on AWS (NIS202)](https://www.youtube.com/watch?v=aN2P2zeQek0&t=288s) 
+  [AWS re:Invent 2025 - From Reactive to Proactive: Infrastructure governance by design (COP352)](https://www.youtube.com/watch?v=iXor74El2D8) 

 **Related services:** 
+  [VPC Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) 
+  [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) 
+  [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) 
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 
+  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 