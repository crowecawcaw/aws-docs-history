

# ADVSEC08-BP01 Create guardrails and controls to maintain brand safety and content moderation within your workload
<a name="advsec08-bp01"></a>

 Brand reputation protection can block brand association with inappropriate or otherwise harmful content. Having guardrails can maintain customer trust and potential business relationships while avoiding reputational damage and negative publicity. 

## Implementation guidance
<a name="ig-advsec08-bp01"></a>

 Consider implementing Amazon SageMaker AI, with the custom model development capability of SageMaker AI, you can build, train, and deploy custom machine learning models. Designing a guardrail for brand safety could allow you to develop a model that could detect inappropriate imagery in advertisements, classify text within content for sentiment and safety, and predict the likelihood of an ad placement being brand appropriate. With the real time inference capability of SageMaker AI, you can deploy your models deemed brand safe for real time content analysis, allowing for quick decision making for your solution. 

 Additionally, consider using AWS Config, to assess, audit, and evaluate resource configurations within your AWS environment. Config can track changes to underlying resources with your advertising solution to verify that security settings and access controls remain compliance-aligned for brand safety. 

## Key AWS services
<a name="key-aws-services-10"></a>
+  AWS Config 
+  Amazon SageMaker AI 

## Resources
<a name="resources-16"></a>
+  [Examples and More Information: Use Your Own Algorithm or Model](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-notebooks.html) 
+  [Compliance](https://docs.aws.amazon.com/config/latest/APIReference/API_Compliance.html) 