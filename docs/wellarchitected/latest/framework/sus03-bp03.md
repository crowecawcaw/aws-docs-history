

# SUS03-BP03 Use the most resource-efficient computational approach

 Choosing the right computational approach, from simple code to agentic AI, can impact the resource efficiency of your workload. While agentic AI can provide powerful capabilities for complex problems, it often requires more computational resources than traditional algorithmic approaches, which may be more efficient for problems where rules can be explicitly defined. Decide when to use machine learning or traditional algorithms based on the nature of the problem, data availability, and resource implications. By selecting the most appropriate approach for each use case, you minimize unnecessary resource consumption while achieving your desired outcomes. 

 **Desired outcome:** You use the most resource-efficient computational approach for each specific problem. 

 **Common anti-patterns:** 
+  Using complex machine learning algorithms indiscriminately for all problems regardless of intended outcome. 
+  Overlooking simple algorithmic solutions in favor of machine learning (ML) approaches. 
+  Overlooking simpler ML solutions in favor of more complex methods. For example, there are traditional computer vision techniques that are often more efficient than neural networks. 
+  Not balancing the output requirement from generative AI models against the size of the model. 
+  Over-engineering solutions beyond what is required for the business challenge. 
+  Not considering the ongoing operational and training costs of ML models and traditional approaches. 
+  Continuing to use a specific computational approach, without regularly reviewing to see if more efficient options exist. 

 **Benefits of establishing this best practice:** 
+  Lowers the required share on hardware related impacts, from raw material extraction to end of life treatment (Scope 3 emissions). 
+  Lowers the required share on energy for operating infrastructure (Scope 2 emissions). 
+  Deterministic approaches can improve explainability, increase maintainability of outcomes, and remove the risk of hallucinations by generative AI. 
+  Higher transparency and less overhead for responsible AI considerations. 
+  Improved portability of code to different hardware, including lower powered edge devices. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Select the most resource-efficient computational approach by evaluating problem characteristics, comparing computational approaches, and making decisions based on both effectiveness and resource efficiency. 

 As a concrete example of a choice based on solution complexity, consider the task of extracting email addresses from documents. Approaches include: 
+  Regular expressions consume the least memory per document. 
+  Named entity recognition (NER) models consume more memory. 
+  Large language models require the most memory. 

 Given these choices, choose the most resource-efficient approach with regular expressions for well-defined formats, NER models for complex entity types requiring context, and LLMs only when contextual reasoning is essential. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Evaluate your problem characteristics: 
   +  Assess problem complexity, variability of the input and format, and structure (well-defined compared to ambiguous). 
   +  Determine whether rules can be explicitly defined or must be learned from data. Explicitly defined rules (such as data validation, format checking, or mathematical calculations) favor algorithmic approaches. Patterns that must be learned from examples (such as image recognition, natural language understanding, or complex decision boundaries) may require machine learning. 
   +  Consider data availability and quality requirements. Machine learning approaches require substantial training data (thousands to millions of examples) and ongoing data quality maintenance, while algorithmic approaches work with minimal or no training data. Poor data quality forces more complex ML models to compensate, increasing resource consumption. 

1.  Compare computational approaches: 
   +  Research traditional algorithmic solutions for your problem domain (for example, regular expressions in the previous example). 
   +  Identify potential machine learning approaches and their requirements. 
   +  Benchmark resource consumption (compute, memory, or storage) for each approach. 
   +  Determine trade-offs between different approaches. 
   +  Evaluate development effort, maintainability, consistency, reliability, ease of debugging, and explainability. 

1.  Start with the most resource efficient solution: 
   +  Implement rule-based algorithms first when appropriate. 
   +  Consider hybrid approaches that combine algorithmic elements with ML. Given the previous document extraction example, try the extraction of contact information first a with regular expressions. Fall back to an LLM approach only if no contact information can be found. 
   +  Use ML techniques when simpler solutions prove to be inadequate. 

1.  Optimize ML implementations when necessary: 
   +  Select an appropriate [ML service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/ml-guide.html) and model architectures for your specific use case. 
   +  Implement [model pruning, quantization, and distillation](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to reduce resource requirements. 
   +  Determine feature importance to reduce collection, cleansing, and training. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS01-BP01 Understand your resource usage efficiency](sus01-bp01.md) 
+  [SUS03-BP01 Optimize workloads for high resource usage efficiency](sus03-bp01.md) 
+  [PERF01-BP02 Evaluate the trade-offs between performance and other non-functional requirements](perf01-bp02.md) 
+  [MLSUS-01 Define the overall environmental impact or benefit](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus01-bp01.html) 

 **Related documents:** 
+  [Building Sustainable, Efficient, and Cost-Optimized Applications on AWS](https://aws.amazon.com/blogs/compute/building-sustainable-efficient-and-cost-optimized-applications-on-aws/) 
+  [Getting started with Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/getting-started/) 
+  [Model performance optimization with SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) 
+  [Choosing an AWS machine learning service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/ml-guide.html) 

 **Related blog posts:** 
+  [Optimize AI/ML workloads for sustainability: Part 1, identify business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/) 
+  [Choosing the Right Tool: Selecting Machine Learning or Generative AI for Optimal Results](https://aws.amazon.com/blogs/apn/choosing-the-right-tool-selecting-machine-learning-or-generative-ai-for-optimal-results/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Break through AI performance and cost barriers with AWS Trainium (AIM201)](https://www.youtube.com/watch?v=5SgZ3zRJFAY) 

 **Related examples:** 
+  [Guidance for Optimizing Deep Learning Workloads for Sustainability on AWS](https://docs.aws.amazon.com/solutions/optimizing-deep-learning-workloads-for-sustainability-on-aws/) 