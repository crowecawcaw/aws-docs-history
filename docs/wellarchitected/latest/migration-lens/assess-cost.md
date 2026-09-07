

# Assess
<a name="assess-cost"></a>

 In the assess phase, prioritizing cost-effectiveness is essential. This phase involves a comprehensive evaluation of existing infrastructure usage and a thorough analysis of application dependencies. By assessing these aspects, you can pinpoint opportunities for optimizing costs throughout the migration journey. To expedite this cost-effective assessment, consider leveraging AWS programs and workshops designed to remove common blockers and accelerate migrations. By incorporating these best practices, you not only ensure a well-informed migration strategy, but also lay the groundwork for maximizing cost efficiency in your cloud migration. 


| MIG-COST-01: Are you collecting the right information about your source resources to create cost-optimized destination architectures? | 
| --- | 
|   | 

 Successful migrations require high-quality data about the source environment and thorough analysis of technology, people, and processes to move quickly and safely. 

## MIG-COST-BP-1.1: Thoroughly assess existing infrastructure usage and application dependencies prior to migration
<a name="mig-cost-bp-1.1-thoroughly-assess-existing-infrastructure-usage-and-application-dependencies-prior-to-migration"></a>

 This BP applies to the following best practice areas: Cost-effective resources 

### Implementation guidance
<a name="implementation-guidance-76"></a>

 **Suggestion 1.1.1:** Use discovery tools or existing data to gather enough data about your source infrastructure to make informed decisions about your target architecture. 

 Collect a complete inventory of assets to be migrated and analyze dependencies between servers, databases, and applications to create migration wave plans that minimize network chatter and latency between source and target infrastructure. Collect fine-grained infrastructure usage data, including CPU, memory, and disk reads and writes. It's important to understand actual usage from your source servers, not just how many resources are allocated, in order to right-size the target infrastructure in AWS. 

 These data should be gathered with frequent samples in order to understand the minimum, average, and maximum usage over time, typically at least two weeks. AWS and our partners offer several tools that can help collect the required information, such as [Application Discovery Service](https://aws.amazon.com/application-discovery/) and [Migration Evaluator](https://aws.amazon.com/migration-evaluator/). Some customers already have this information in their change management databases (CMDB) or observability tools. 

 For more detail, see the following: 
+  [AWS Prescriptive Guidance regarding migration tool selection](https://aws.amazon.com/prescriptive-guidance/migration-tools/) 
+  [AWS Prescriptive Guidance regarding Application portfolio assessment](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/introduction.html) 
+  [AWS Prescriptive Guidance for Wave Planning](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/wave-planning.html) 

## MIG-COST-BP-1.2: Leverage AWS programs and workshops designed to remove common blockers and accelerate migrations
<a name="mig-cost-bp-1.2-leverage-programs-and-workshops-designed-to-remove-common-blockers-and-accelerate-migrations"></a>

 This BP applies to the following best practice areas: Cost-effective resources 

### Implementation guidance
<a name="implementation-guidance-77"></a>

 **Suggestion 1.2.1:** Leverage AWS and partner programs and experience to improve assessments and identify and remove costly blockers early. 

 The [Migration Acceleration Program (MAP)](https://aws.amazon.com/migration-acceleration-program/) provides tools that reduce costs and automate and accelerate migration assessment and implementation. In some cases AWS invests in customer migrations in the form of service credits or [partner investments](https://aws.amazon.com/migration/partner-solutions/). MAP also leverages proven workshops such as Migration Readiness Assessments, [Experience-Based Accelerators (EBA)](https://aws.amazon.com/blogs/mt/level-up-your-cloud-transformation-with-experience-based-acceleration-eba/), and [AWS Learning and Needs Analysis (LNA)](https://aws.amazon.com/training/teams/learning-needs-analysis/) to assess and address technology, people, and processes that may create costly blockers or reduce migration velocity. 

 **Suggestion 1.2.2:** Use the [AWS Optimization and Licensing Assessment (OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/) program to conduct thorough discovery of existing Windows license footprints and cost optimization exercises. 

 The AWS OLA delivers a comprehensive report that models your deployment options based on actual resource use and your existing licensing entitlements, helping you uncover potential cost savings through our flexible licensing options, including Bring-Your-Own-License (BYOL) and license-included options. 