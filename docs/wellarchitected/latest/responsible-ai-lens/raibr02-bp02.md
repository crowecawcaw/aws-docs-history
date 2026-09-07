

# RAIBR02-BP02 Identify potential harmful events impacting veracity
<a name="raibr02-bp02"></a>

 *Veracity* harms arise when AI systems produce factual errors, as measured against an established base set of facts. Errors include hallucinations, omissions, and misemphases. These errors can propagate through AI systems, affecting downstream decision-making processes. Hallucinations and other veracity-related issues can compound across other responsible AI dimensions to create complex patterns of harm. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation considerations
<a name="implementation-considerations-13"></a>

1.  Consider which facts, if any, will be represented in outputs. 

1.  Consider how you will validate that a fact is true. What are your reference sources? How subject to debate will output facts be? 

1.  Consider the implications of a veracity error propagating through your AI system or the workflow you are trying to improve with the AI system. How does inaccurate information spread through system interactions and user networks? 

1.  Consider how factual inaccuracies interact with other responsible AI considerations, like fairness or safety. For example, an AI system's veracity errors might exacerbate unwanted biases. 

## Resources
<a name="resources-12"></a>

 **Related tools:** 

## Evaluate the performance of Amazon Bedrock Resources
<a name="evaluate-the-performance-of-amazon-bedrock-resources"></a>
+  [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) 