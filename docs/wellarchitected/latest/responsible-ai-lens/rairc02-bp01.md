

# RAIRC02-BP01 Select metrics to measure the properties tested by the release criteria
<a name="rairc02-bp01"></a>

 For each release criterion you defined, choose specific metrics that can reliably measure the information needed to answer the question. A single criterion may require multiple metrics to properly measure it. Consider both automated metrics (like accuracy scores and toxicity detection) and human evaluation methods (like expert reviews and user feedback) depending on what you're measuring and explore open-source libraries as well as proprietary services that provide pre-built metrics. Document which metrics map to which criteria so you have a clear measurement plan for every release question you need to answer. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation considerations
<a name="implementation-considerations-28"></a>

1.  Take each yes or no release criterion and identify what specific measurements you need to answer that question. For example, if your criterion is "Does the system respond to queries quickly?", you need response time metrics, or if it's "Does the system block toxic content?", you need toxicity detection scores. Break down abstract criteria into concrete, measurable criteria. 

1.  Look for existing automated metrics that can measure what you need, such as accuracy scores, response time tracking, or toxicity detection tools. Check open source options like [scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html) or [Hugging Face](https://huggingface.co/) libraries as well as paid services such as [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html). Automated metrics save time and provide consistent measurements you can run repeatedly. 

1.  Consider using [LLM-as-a-judge](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/) for criteria that require understanding context, quality, or appropriateness. For example, you can prompt an LLM to evaluate whether responses are helpful, coherent, or follow specific guidelines by giving it examples and scoring rubrics. LLM judges work well for subjective assessments that are too complex for simple automated metrics and are more scalable than human review. 

1.  Identify which criteria need human evaluation because neither automated metrics nor LLM judges can capture what you're trying to measure. For example, measuring whether user interface designs are intuitive may require actual users to test the interface to better capture the real user experience and preferences. Human evaluation catches the most nuanced issues and is more representative of your user experience but is slower and more expensive. 

1.  If you find yourself needing multiple different metrics to test one criterion because the criterion itself is complex, consider splitting the criterion into separate yes or no questions. For example, change "Does the system provide a good user experience?" into "Does the system respond quickly?", "Does the system give accurate results?", and "Does the system have an intuitive interface?" This makes each criterion simple to measure definitively. 

1.  Track which metric you'll use for each release criterion. This gives you a clear testing plan and creates a mapping from your measurements to your release criteria. 

## Resources
<a name="resources-26"></a>

 **Related documents:** 

 [Amazon SageMaker AI AI : Metrics and Validation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html) 

 [Amazon SageMaker AI Canvas : Metrics reference](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-metrics.html) 

 [Evaluating your SageMaker AI AI-trained model](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-evaluation.html#nova-model-evaluation-benchmark) 

 [Evaluation metrics and statistical tests for machine learning](https://www.nature.com/articles/s41598-024-56706-x) 

 [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and validation 

 **Related tools:** 

 [Metrics and scoring: quantifying the quality of predictions](https://scikit-learn.org/stable/modules/model_evaluation.html) 

 [LLM-as-a-judge on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/) 

 [Hugging Face](https://huggingface.co/) 

 [Amazon Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/) 