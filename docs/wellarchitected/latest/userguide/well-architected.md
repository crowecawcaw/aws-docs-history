

AWS Well-Architected Agent is in preview release and is subject to change.

# What is AWS Well-Architected?
<a name="well-architected"></a>

Last updated: **October 1, 2026** ([Release notes](release-notes.md))

 AWS Well-Architected provides two distinct ways to review your cloud architecture: 
+ **AWS Well-Architected Agent:** An AI-powered service that delivers contextual, personalized optimization recommendations based on your specific architecture and business goals. It provides ready-to-use automation scripts and infrastructure as code (IaC) template updates that align with AWS best practices.

  To get started with the AWS Well-Architected Agent, see [What is AWS Well-Architected Agent (preview)?](agent.md)
+ **AWS Well-Architected Tool:** A service that provides a consistent process for reviewing and measuring your architecture using the AWS Well-Architected Framework. You can document decisions, identify areas for improvement, and track progress over time using workloads, lenses, and milestones.

  To get started with the AWS Well-Architected Tool, see [What is AWS Well-Architected Tool?](tool.md)

The following table summarizes the differences between the two services:


**Comparison of AWS Well-Architected Agent and AWS Well-Architected Tool**  

|  | AWS Well-Architected Agent | AWS Well-Architected Tool | 
| --- | --- | --- | 
| Approach | Automated, AI-powered analysis of your deployed resources and IaC templates. | Manual, guided self-review of your workloads against the AWS Well-Architected Framework. | 
| Primary entity | Profile (defines the accounts, AWS Regions, pillars, and goals to analyze). | Workload (documents a set of components that deliver business value). | 
| Output | Prioritized recommendations with trade-off analysis, automation scripts, and updated IaC templates. | Identified risks (HRIs and MRIs) and an improvement plan based on your review answers. | 
| When to use | Continuous, goal-driven optimization of your environment with ready-to-act remediation. | Structured architecture reviews, governance, and tracking improvements over time with milestones. | 

The two services complement each other, and you can use both at the same time from the AWS Well-Architected console.