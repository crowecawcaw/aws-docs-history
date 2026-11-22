

# SEC05-BP04 Automate network protection

 Automate deployment of network protections with infrastructure as code and continuous integration and delivery pipelines. With automation, you can version network changes, deploy them faster, detect drift from intended configuration, and make protections repeatable across teams and accounts. 

 **Desired outcome:** 
+  You define your network protections as templates held in a version control system. 
+  Your automated pipelines test and deploy changes whenever a template is updated. 
+  Your policy checks and static tests validate changes before they deploy. 
+  You promote changes through a staging environment and then to production after the controls are approved. 

 **Common anti-patterns:** 
+  Each workload team defines its complete network stack and protections independently, with no standard components published centrally to reuse. 
+  A central team defines every aspect of the network and protections and delegates nothing to the workload teams that understand their own requirements. 
+  Teams balance central and delegated ownership well but apply inconsistent testing and deployment standards across templates and pipelines. 
+  Teams leave required configurations out of the tooling that checks templates for adherence. 

 **Benefits of establishing this best practice:** 
+  Version-controlled templates let you track and compare protection changes over time. 
+  Automated testing and deployment produce predictable, repeatable releases. 
+  Standardized pipelines reduce repetitive manual configuration and the errors it introduces. 
+  Drift detection surfaces unintended changes before they weaken your protections. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [AWS WAF managed rules](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html), [AWS Shield Advanced automatic application layer DDoS mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html), and [AWS Network Firewall managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-managed-rule-groups.html) keep signatures and low-reputation domain lists current without your intervention. For the protections you define yourself, use infrastructure as code and pipelines. 

 Capture VPCs, security groups, firewall deployments, resolver rules, and DNS firewall configurations as templates in [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or another infrastructure-as-code tool. You get predictable releases, automated policy checks with tools such as [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html), and drift detection between deployed and intended state. 

 Decide how to split ownership of network controls between central and workload teams. If every workload team builds its own complete network stack, effort duplicates and protection is inconsistent. If a central team owns everything, it becomes a bottleneck and loses touch with workload-specific needs. A hybrid model usually works best: a central team publishes standard components, and each workload team maintains the parts specific to its application. Whichever split you choose, apply consistent testing and deployment standards across all templates. 

 To centralize network protections, use a dedicated network account. The [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture) describes a [network infrastructure account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) that holds VPCs for ingress, egress, and inspection. Define the VPCs your workloads use in that account, along with their security groups, firewall deployments, and resolver rules. Share them to other accounts with [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html). Your automation then has a single target to test and deploy against. Workload teams still own other controls in their own accounts. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assign ownership of controls:** Decide which network components and protections are defined centrally and which each workload team maintains. Document this split so the boundary between central and delegated ownership is explicit. 

1.  **Create test and production environments:** Set up separate environments for validating and running your network protections, such as a network testing account and a network production account. Use the test environment to confirm controls behave as expected before promotion. 

1.  **Store templates in version control:** Keep central templates in a repository separate from workload repositories, and store workload-specific templates in repositories owned by each workload. Use the version control system to track and review every change. 

1.  **Build pipelines to test and deploy templates:** Create CI/CD pipelines that run static checks for misconfigurations and confirm templates meet your company standards, then deploy approved changes. Use tools such as [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) to enforce policy before deployment. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC05-BP02 Control traffic flow within your network layers](sec05-bp02.md) 
+  [SEC05-BP03 Implement inspection-based protection](sec05-bp03.md) 
+  [SEC01-BP05 Automate deployment of standard security controls](sec01-bp05.md) 

 **Related documents:** 
+  [AWS Security Reference Architecture - Network account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Networks at scale and how to automate operations (NET323)](https://www.youtube.com/watch?v=_nOKPOTJqko) 

 **Related examples:** 
+  [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/) 
+  [AWS Cloud WAN blueprints](https://github.com/aws-samples/aws-cloud-wan-blueprints) 

 **Related tools:** 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 
+  [cfn\_nag](https://github.com/stelligent/cfn_nag) 