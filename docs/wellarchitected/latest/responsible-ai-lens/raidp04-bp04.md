

# RAIDP04-BP04 Establish governance procedures for managing your datasets
<a name="raidp04-bp04"></a>

 Maintain procedures for managing dataset access, retention, and deletion throughout the AI system lifecycle. Implement mechanisms to handle individual data requests, including the ability to remove individual data points when contributors withdraw consent. Document data lineage and retention policies that specify how long different types of data can be stored and used. Create procedures for handling governance-related dataset updates. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation considerations
<a name="implementation-considerations-59"></a>

1.  Create clear retention policies that specify how long different types of data can be kept and when they need to be deleted. 

1.  Build workflows that let you quickly find and remove specific data points when people request deletion or withdraw their consent. Your system should be able to trace individual data samples across training sets, evaluation datasets, and cached model outputs without disrupting other parts of your data. 

1.  Document the complete journey of your data from collection to deletion, including who accessed it, when it was modified, and which models or evaluations used it. This data lineage assists you to understand the impact when you need to remove or modify datasets for compliance-aligned reasons. 

1.  Consider governance reviews with your legal team where you check that your data handling practices match your policies and legal obligations, including, but not limited to data retention schedules, deletion requests, and access controls. 

## Resources
<a name="resources-56"></a>

 **Related documents:** 
+  [Responsible AI](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/responsible-ai.html) 
+  [Generative AI lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html) 
+  [Responsible AI Best Practices: Promoting Responsible and Trustworthy AI Systems](https://aws.amazon.com/blogs/enterprise-strategy/responsible-ai-best-practices-promoting-responsible-and-trustworthy-ai-systems/) 
+  [AWS Generative AI Best Practices Framework v2](https://docs.aws.amazon.com/audit-manager/latest/userguide/aws-generative-ai-best-practices.html) 
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.7.5 Data provenance 