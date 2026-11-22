

# COST10-BP02 Use generative AI services and solutions for efficiency

 Cost management generates a large amount of data that your teams must interpret and act on. Generative AI can shorten that work. It answers questions in natural language, summarizes spend, and surfaces optimization opportunities that would take an analyst hours to find. With clear goals and human review, it makes routine cost analysis faster. 

 **Desired outcome:** 
+  Your teams query cost and usage data in natural language and get answers they can act on, without building reports by hand. 
+  You use generative AI to assist cost analysis and optimization, and people review and approve the decisions it informs. 
+  Each of your generative AI use cases has a defined business objective and success metric before it enters a workflow. 
+  Your routine reporting and visualization run with less manual effort, so analysts focus on interpretation and action. 

 **Common anti-patterns:** 
+  Teams adopt AI tools without a clear business objective or a way to measure success. 
+  Organizations let AI tools drive critical cost decisions without human oversight or validation. 
+  Teams feed AI tools inconsistent or poorly governed data and trust the output without checking it. 
+  Teams adopt AI tooling without accounting for the cost of the tooling itself, so the efficiency case is never proven net of what it consumes. 

 **Benefits of establishing this best practice:** 
+  Operational cost drops as repetitive reporting and analysis take less manual effort. 
+  Teams get insights faster because natural-language queries replace manual data gathering. 
+  Analysts spend more time on interpretation and strategy and less on assembling data. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Cost management data is detailed and constantly changing, which makes manual analysis slow. Generative AI changes the interface to that data. You ask a question in plain language and get a summarized answer with the reasoning behind it. This lowers the skill barrier for cost analysis and shortens the time from question to decision. 

 Use generative AI to support cost decisions. Models can produce confident answers that are wrong, and a cost decision based on an unverified answer can increase spend. Require human review for any decision with financial impact. Prefer tools that show the data and parameters behind each answer so you can check the result. 

 AI applied to inconsistent tags, incomplete cost allocation, or ungoverned data produces answers that look precise but aren't reliable. Before you adopt these tools, assess whether your cost and usage data is complete, consistently tagged, and accessible. 

 Adopt generative AI with a defined objective. Decide what task to make more efficient, what a good result looks like, and how to measure it before adopting a tool. Establish governance for who can use these tools, what data they can access, and how you monitor their use. 

 On AWS, the [AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/what-is.html) can be used to ask questions in plain language to learn about AWS services, analyze historical and forecasted costs, identify optimization opportunities, and understand AWS pricing. It answers cost questions using AWS Cost Explorer, AWS Cost Optimization Hub, and AWS Compute Optimizer, and it [shows the APIs and parameters behind each answer](https://docs.aws.amazon.com/assistant/latest/userguide/costs.html). With [AWS Quick](https://aws.amazon.com/quick/), business users ask questions of cost dashboards in plain language without knowing the underlying data model. During design, cost analysis tooling estimates architecture cost before you deploy it, when changes are cheaper to make. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define the objective and success metric:** Choose one cost task to make more efficient, such as ad hoc cost questions, recurring reports, or design-time estimates. Write down what a good result looks like and how you will measure the saving in time or spend, net of what the tooling itself costs. Confirm your cost and usage data is complete and consistently tagged before you start, because output quality depends on it. 

1.  **Query and investigate costs in natural language:** Use [AI-Powered Cost Analysis in AWS Cost Explorer](https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-ai-powered-cost-analysis-in-aws-cost-explorer/) to ask questions about your AWS spend, investigate anomalies, and generate cost summaries. Review the data and parameters behind each answer before you act on it. This replaces manual report building for common cost questions. 

1.  **Make dashboards self-service for business users:** Use [AWS Quick](https://aws.amazon.com/quick/) with your cost dashboards, so non-technical users ask questions in plain language and get visual answers. Define business terminology so the tool maps questions to the right data. This reduces the reporting load on analysts. The [Generative AI Assistant with CID and AWS Quick](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/generative-ai.html) implementation guide covers this pattern end to end, including the deployment and sample prompts for asking questions of your cost dashboards. 

1.  **Estimate cost during design:** Use design-time cost analysis, such as the [AWS Pricing MCP Server](https://awslabs.github.io/mcp/servers/aws-pricing-mcp-server), to estimate the cost of an architecture before deployment. Compare options and right-size infrastructure while changes are still cheap to make. This helps avoid over-provisioning rather than correcting it after the fact. 

1.  **Review infrastructure as code against best practices:** Use the [Well-Architected IaC Analyzer](https://github.com/aws-samples/well-architected-iac-analyzer) to assess AWS CloudFormation and Terraform templates against the AWS Well-Architected Framework before deployment. Remediate the risks and misconfigurations it flags, including those that drive avoidable cost. Keep a person in the loop to confirm each finding. 

1.  **Keep human oversight and monitor use:** Require human review for any decision with financial impact, and record who can use these tools and what data they reach. Track whether each use case meets the success metric you defined, and retire the ones that do not. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST10-BP01 Perform automation for operations](cost10-bp01.md) 
+  [COST06-BP01 Perform cost modeling](cost06-bp01.md) 
+  [COST02-BP03 Monitor cost proactively](cost02-bp03.md) 

 **Related documents:** 
+  [What is the AWS assistant?](https://docs.aws.amazon.com/assistant/latest/userguide/what-is.html) 
+  [How AWS Quick works](https://docs.aws.amazon.com/quick/latest/userguide/how-quicksuite-works.html) 
+  [Generative AI Assistant with CID and AWS Quick](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/generative-ai.html) 

 **Related examples:** 
+  [Introducing AI-Powered Cost Analysis in AWS Cost Explorer](https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-ai-powered-cost-analysis-in-aws-cost-explorer/) 
+  [Well-Architected IaC Analyzer](https://github.com/aws-samples/well-architected-iac-analyzer) 
+  [AWS Pricing MCP Server](https://awslabs.github.io/mcp/servers/aws-pricing-mcp-server) 
+  [Billing and Cost Management MCP Server](https://github.com/awslabs/mcp/tree/main/src/billing-cost-management-mcp-server) 

 **Related services:** 
+  [AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/what-is.html) 
+  [AWS Quick](https://aws.amazon.com/quick/) 