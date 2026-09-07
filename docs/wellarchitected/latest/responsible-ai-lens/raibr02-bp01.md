

# RAIBR02-BP01 Identify potential harmful events impacting fairness
<a name="raibr02-bp01"></a>

 Examine how the proposed AI system might affect different stakeholder groups and subgroups throughout the entire system lifecycle. A fairness assessment may consider harms to individuals (for example, wrongful denials) and to groups (for example, performance variations across demographic groups). 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation considerations
<a name="implementation-considerations-12"></a>

1.  Consider how different demographic groups are represented in the inputs (for example, by geography). 

1.  Consider whether some inputs could unintentionally represent or misrepresent different demographic groups (for example, proxy a demographic attribute). 

1.  Consider whether training data might inappropriately represent the expected users and whether a wider variety of inputs could impact performance. For example, a facial recognition system trained primarily on certain skin tones might not perform as well on other skin tones. 

1.  Assess potential impacts at the levels of individuals, groups, and society. For example, a job candidate screening tool might impact individual candidates, demographic group success rates, and overall workforce representation. 

## Resources
<a name="resources-11"></a>

 **Related documents:** 
+  [Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness](https://arxiv.org/abs/1711.05144) 
+  [Equality Of Odds](https://mlu-explain.github.io/equality-of-odds/) 
+  [Fairness, model explainability and bias detection with SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) 
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.5.4 Assessing AI system impact on individuals or groups of individuals 
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems 

 **Related tools:** 
+  [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/) 