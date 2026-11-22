

# AWS Well-Architected Framework

 Last updated: **November 16, 2026** ([Release notes](release-notes.md)) 

 The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS. Using the Framework helps you learn architectural best practices for designing and operating secure, reliable, efficient, cost-effective, and sustainable workloads in the AWS Cloud. It provides a way for you to consistently measure your architectures against best practices and identify areas for improvement. The process for reviewing an architecture is a constructive conversation about architectural decisions, and is not an audit mechanism. We believe that having well-architected systems greatly increases the likelihood of business success. 

 AWS Solutions Architects have years of experience architecting solutions across a wide variety of business verticals and use cases. We have helped design and review thousands of customers' architectures on AWS. From this experience, we have identified best practices and core strategies for architecting systems in the cloud. 

 The AWS Well-Architected Framework documents a set of foundational questions that help you to understand if a specific architecture aligns well with cloud best practices. The framework provides a consistent approach to evaluating systems against the qualities you expect from modern cloud-based systems, and the remediation that would be required to achieve those qualities. As AWS continues to evolve, and we continue to learn more from working with our customers, we will continue to refine the definition of well-architected. 

 This framework is intended for those in technology roles, such as chief technology officers (CTOs), architects, developers, and operations team members. It describes AWS best practices and strategies to use when designing and operating a cloud workload, and provides links to further implementation details and architectural patterns. For more information, see [AWSAWS Well-Architected Documentation](https://docs.aws.amazon.com/wellarchitected).

 AWS also provides services for reviewing your workloads. For more detail, see [What is AWS Well-Architected?](https://docs.aws.amazon.com/wellarchitected/latest/userguide/well-architected.html) 

## Architecture
<a name="on-architecture"></a>

### From centralized to distributed
<a name="architecture-traditional-vs-cloud"></a>

 In traditional environments, organizations often have a centralized architecture team that acts as an overlay to product or feature teams. These teams verify that other teams follow best practices and maintain standards across the organization. 

 In cloud environments, this model does not scale. The pace of change, the breadth of available services, and the need for teams to move independently require a different approach. Instead of centralizing architecture decisions, distribute architectural capability to the teams that build and operate workloads. 

 This shift requires two things to work: 
+  *Practices* that enable each team to make sound architectural decisions. Practices include shared standards, design patterns, reference architectures, and access to subject matter experts who can review designs and raise the bar. 
+  *Mechanisms* that verify standards are being met without requiring manual oversight. Mechanisms include automated compliance checks, architecture fitness functions, and infrastructure-as-code policies that enforce guardrails. 

 When you distribute architectural ownership, every team is responsible for creating architectures that follow best practices. To help teams gain and maintain this capability, provide access to experts who can review designs and share knowledge across the organization. 

### Architecture governance at scale
<a name="architecture-governance"></a>

 Effective governance in a distributed model relies on automation rather than manual review. Consider the following approaches: 
+  Use infrastructure as code to define and enforce architectural patterns. Infrastructure definitions become reviewable, testable, and versionable like application code. 
+  Implement automated guardrails through service control policies, permission boundaries, and configuration rules that prevent non-compliant deployments rather than detecting them after the fact. 
+  Record architectural decisions using a lightweight, consistent format (such as architecture decision records) so that teams can understand the context behind past choices. This preserves institutional knowledge and reduces repeated debates. 
+  Conduct Well-Architected reviews at key milestones in the workload lifecycle. These reviews are constructive conversations about architectural decisions, not audits. Use them to identify risks, share knowledge across teams, and track improvements over time. 

### Evolutionary architecture
<a name="architecture-evolutionary"></a>

 Cloud architectures are not static. They evolve as business requirements change, new services become available, and teams learn from operating their workloads. Design for change rather than designing for a fixed end state. 

 An evolutionary approach to architecture means: 
+  Making decisions reversible where possible. Prefer approaches that allow you to change direction without significant rework. 
+  Using data to inform architectural decisions. Collect metrics on how your workload performs and use that data to validate or challenge your assumptions. 
+  Testing architectural changes through experimentation. Use canary deployments, feature flags, and A/B testing to validate changes incrementally before full commitment. 
+  Treating your architecture as a living artifact. Update documentation, diagrams, and decision records as the architecture evolves. Mark milestones at key changes to track how the architecture has developed over time. 

### The role of the Well-Architected Framework
<a name="architecture-wa-role"></a>

 The AWS Well-Architected Framework provides a consistent approach for evaluating architectures against the qualities you expect from cloud-based systems. It codifies best practices that have emerged from designing, building, and reviewing thousands of workloads on AWS. 

 Use the Framework to: 
+  Establish a common language for discussing architectural decisions across teams. 
+  Identify risks in your technology portfolio by reviewing workloads against best practices. 
+  Find themes across teams that can be addressed through shared mechanisms, training, or organizational changes. 
+  Track improvements over time by conducting reviews at milestones and comparing results across review cycles. 

 Technology leaders carrying out Well-Architected reviews across workloads gain visibility into the risks in their technology portfolio and can identify where investment in shared capabilities will have the greatest impact. 

## Lens availability
<a name="custom-lens-availability"></a>

 Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own [custom lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-custom.html), or to use lenses created by others that have been shared with you. 

There are two custom lenses provided for the AWS Well-Architected Framework.

**Note**  
 The Cloud Foundations custom lens contains the best practices in the [Foundations](reliability.md#foundations) section.   
 The Cloud Workloads custom lens contains the updated Well-Architected Framework pillars. 
+  [Well-Architected Cloud Foundations](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/well-architected-framework/cloud-foundations.json) 
+  [Well-Architected Cloud Workloads](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/well-architected-framework/well-architected-framework.json) 

To begin reviewing your workloads, download and import either custom lens into AWS Well-Architected Tool from the public [AWS Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens).