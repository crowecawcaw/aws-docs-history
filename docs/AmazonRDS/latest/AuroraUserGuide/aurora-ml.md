

# Using Amazon Aurora machine learning
<a name="aurora-ml"></a>

By using Amazon Aurora machine learning, you can integrate your Aurora DB cluster with one of the following AWS machine learning services, depending on your needs. They each support specific machine learning use cases.

**Amazon Bedrock**  
Amazon Bedrock is a fully managed service that makes leading foundation models from AI companies available through an API, along with developer tooling to help build and scale generative AI applications. With Amazon Bedrock, you pay to run inference on any of the third-party foundation models. Pricing is based on the volume of input tokens and output tokens, and on whether you have purchased provisioned throughput for the model. For more information, see [What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) in the *Amazon Bedrock User Guide*. 

**Amazon Comprehend**  
Amazon Comprehend is a managed natural language processing (NLP) service that's used to extract insights from documents. With Amazon Comprehend, you can deduce sentiment based on the content of documents, by analyzing entities, key phrases, language, and other features. To learn more, see [What is Amazon Comprehend?](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) in the *Amazon Comprehend Developer Guide*. 

**SageMaker AI**  
Amazon SageMaker AI is a fully managed machine learning service. Data scientists and developers use Amazon SageMaker AI to build, train, and test machine learning models for a variety of inference tasks, such as fraud detection and product recommendation. When a machine learning model is ready for use in production, it can be deployed to the Amazon SageMaker AI hosted environment. For more information, see [What Is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) in the *Amazon SageMaker AI Developer Guide*.   
Using Amazon Comprehend with your Aurora DB cluster has less preliminary setup than using SageMaker AI. If you're new to AWS machine learning, we recommend that you start by exploring Amazon Comprehend.

**Topics**
+ [Using Amazon Aurora machine learning with Aurora MySQL](mysql-ml.md)
+ [Using Amazon Aurora machine learning with Aurora PostgreSQL](postgresql-ml.md)