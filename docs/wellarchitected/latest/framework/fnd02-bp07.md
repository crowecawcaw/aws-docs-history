

# FND02-BP07 Implement data perimeter controls to help prevent unintended access

 Data perimeter controls verify that only your trusted identities access trusted resources from expected networks. They are always-on, organization-wide permission guardrails that complement fine-grained access controls. By enforcing a set of security standards across identities, resources, and networks, data perimeter controls help prevent unintended data movement outside your organization's trust boundaries. 

 **Desired outcome:** 
+  You have defined clear trust boundaries for identities, resources, and networks based on your business and security requirements. 
+  You have complete data perimeter controls in place that safeguard your organization's trusted resources. 
+  Your controls enforce these boundaries consistently across accounts, improving your security posture and adherence to data regulation requirements. 

 **Common anti-patterns:** 
+  Using service-specific controls instead of service-agnostic, coarse-grained data perimeter controls. 
+  Implementing all data perimeter controls across the entire organization simultaneously, which can complicate change management and troubleshooting. 
+  Enforcing data perimeter controls without first assessing the potential impacts on your existing workloads. 
+  Building permissions guardrails from scratch rather than using existing samples from data perimeter policy examples repositories. 

 **Benefits of establishing this best practice:** 
+  Data perimeter controls establish [permissions guardrails across multiple accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-permissions-guardrails), providing consistent security enforcement regardless of account structure or ownership. 
+  You can incrementally tighten access controls while maintaining business agility, confident that access patterns conform to organizational guidelines throughout the journey. 
+  These controls work alongside existing infrastructure security controls to guard all potential data access paths completely, creating overlapping layers of protection. 
+  Organization-wide security invariants provide clearer evidence of adherence to regulatory requirements and internal security policies. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Data perimeter controls protect against unintended access to data through AWS service API endpoints. They establish coarse-grained IAM policies that specify the maximum permissions available to identities, resources, and networks within your organization. These security invariants apply across resources and accounts. They complement the fine-grained access controls needed to achieve [least privilege principles](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). Even well-designed fine-grained policies can be undermined by misconfigurations, overly permissive resource policies, or missing controls in a growing organization. 

 The data perimeter model uses three complementary boundaries: 

1.  The *identity perimeter* verifies that only your trusted identities access your resources, preventing external principals from accessing data unless explicitly authorized. 

1.  The *resource perimeter* makes sure that your identities access only trusted resources, reducing the risk of data exfiltration to external accounts or services. 

1.  The *network perimeter* restricts access to expected networks, protecting against unauthorized access from unexpected locations. 

 Data perimeter controls work alongside existing infrastructure security controls. You still use controls such as security groups and strict routing rules to keep internal applications on Amazon EC2 instances off the internet. Data perimeter controls extend this protection to data stored in and accessed through AWS service API endpoints, providing centralized enforcement that scales with your organization. For example, security groups protect EC2 instances, while resource control policies (RCPs) help prevent external access to Amazon S3 buckets across all accounts. 

 Match data perimeter controls to your organization's risk profile and operational patterns. A smaller organization with simple compliance needs might start with identity perimeter controls to prevent unintended data movement to or from locations outside its organization. A larger enterprise with complex partner relationships and regulatory obligations might implement all three data perimeter controls with different scopes across organizational units. 

 Take an iterative approach to understand existing access patterns before enforcing controls. These patterns include legitimate flows that cross your organization's boundaries, such as third-party integrations and data sharing. Identifying these patterns before enforcement helps you avoid service disruptions. 

 Define trust boundaries as narrowly as you can maintain them. Explicit lists of approved services provide stronger, more granular control. Broaden the definition, for example by treating all AWS service principals as trusted, only when maintaining the list becomes prohibitive. 

 Implementing data perimeter controls follows an iterative process of six main phases, shown in Figure 1. <a name="fnd02-bp07-fig1"></a>

![Flow diagram of the six iterative phases a team moves through when implementing data perimeter controls.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/data_perimeter_phases.png)

*Six iterative phases of data perimeter implementation*


### Implementation steps
<a name="implementation-steps"></a>

1.  **Examine your security objectives:** Begin by identifying areas where data perimeter controls can improve your security posture. Consider factors such as compliance requirements, workload types, and your organization's threat model. For example, you might prioritize preventing developers from configuring overly permissive S3 bucket policies or reducing the risk of data disclosure by internal threat actors. Learn more about the security objectives and risks addressed by each perimeter type in the [Blog Post Series: Establishing a Data Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-blog-post-series/). Evaluate current controls' effectiveness and prioritize high-risk areas (specific services or environment segments), then gradually expand coverage. 

1.  **Set your boundaries:** Define your trust boundaries by specifying trusted identities, resources, and expected networks across all intended data access patterns and your AWS environment's unique requirements. Start with elements under your direct control and AWS services, and include trusted partners' identities, resources, or networks if necessary. Evaluate the need for intra-organization boundaries to separate production from non-production environments. To support effective implementation of such boundaries, organize your AWS environment using multiple accounts, strategically placing workloads across accounts and OUs based on data sensitivity and security requirements. See [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) for guidance. 

1.  **Design data perimeter controls:** Design data perimeter authorization controls for enforcing these boundaries and achieving your data perimeter objectives. Use different combinations of IAM policy types and [global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) for each data perimeter control. The policies you use ([service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html), and [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies)) can be managed centrally through [AWS Organizations](https://aws.amazon.com/organizations/) and your account vending mechanisms. The [data perimeter policy examples repository](https://github.com/aws-samples/data-perimeter-policy-examples) provides policy examples that can be a foundation. Tailor and extend the example policies to account for all intended access patterns, including exceptions for resources that are expected to be publicly accessible. 

1.  **Anticipate potential impacts:** Before implementing controls, conduct an assessment to evaluate their potential impact on existing workloads. This helps identify unknown data access patterns missed during initial design. Use [AWS IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) to [identify resources shared with external entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html). Analyze account activity using [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) and analytics capabilities like [Amazon Athena](https://aws.amazon.com/athena/) to query and analyze logs against access patterns that cross your trust boundaries, for instance, API calls made by your identities against resources not belonging to your organization. For detailed guidance, refer to [Analyze your account activity to evaluate impact and refine controls](https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws-analyze-your-account-activity-to-evaluate-impact-and-refine-controls/). 

1.  **Implement data perimeter controls:** Deploy controls using your existing infrastructure as code (IaC) and CI/CD mechanisms to reduce operational overhead and provide deployment consistency. Use [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to deploy SCPs, RCPs, and VPC endpoint policies. Follow [standard CI/CD processes](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/introduction.html) and begin rollout in lower environments by attaching controls to individual test accounts or OUs first. Once controls behave as expected, gradually promote them to upper environments. Deploy to a subset of resources or accounts initially to limit the scope of impact. 

1.  **Monitor data perimeter controls over time:** Establish monitoring processes to verify that data perimeter controls operate as expected. Use [IAM Access Analyzer external access findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-view.html) to understand the impact of your RCPs on resource permissions. Set alerts for occurrences of unintended access patterns in your CloudTrail logs. Enable [Amazon GuardDuty](https://aws.amazon.com/guardduty/) and review [GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html) to detect misconfigurations or anomalous access. Regularly review and update controls to align with evolving business and security objectives, including organizational changes, partner relationship changes, data criticality shifts, and opportunities for expanding coverage. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP05 Grant least privilege access](fnd02-bp05.md) 
+  [FND02-BP06 Define permission guardrails for your organization](fnd02-bp06.md) 
+  [FND01-BP01 Establish management account and organizational structure](fnd01-bp01.md) 
+  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md) 
+  [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) 

 **Related documents:** 
+  [Establish permissions guardrails using data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html) 
+  [Blog Post Series: Establishing a Data Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-blog-post-series/) 
+  [Analyze your account activity to evaluate impact and refine controls](https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws-analyze-your-account-activity-to-evaluate-impact-and-refine-controls/) 
+  [Other technical resources, customer stories, and hands-on activities](https://aws.amazon.com/identity/data-perimeters-on-aws/#Resources) 
+  [IAM Data Perimeters: Conditional Access](https://maturitymodel.security.aws.dev/en/4.-optimized/data-perimeters/) 

 **Related examples:** 
+  [Data perimeter policy examples repository](https://github.com/aws-samples/data-perimeter-policy-examples/tree/main) 

 **Related tools:** 
+  [Data perimeter helper repository](https://github.com/aws-samples/data-perimeter-helper) 