

# Multi-Model Inference Workflow Orchestration
<a name="multi-model-inference-orchestration"></a>

Publication date: **March 28, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to orchestrate running multiple ML models for complex ML-driven insight. With [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), you can run parallel inference jobs and aggregate results.

## Multi-Model Inference Workflow Orchestration
<a name="diagram1"></a>

![Architecture diagram showing multi-model inference workflow orchestration with AWS Step Functions and SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multi-model-inference-orchestration/images/multi-model-inference-orchestration.png)


The following steps describe the architecture:

1. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) provides a RESTful interface for users and administrators. [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) user pools provide authentication.

1. A new job is created by a `POST` request to `/create-job` on the API, with the data to run insights on. This invokes the create job [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function.

1. The function uploads the data to an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket and adds job information to an [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) table for tracking.

1. Lambda functions provide logic for API methods exposed through API Gateway. These allow jobs to be created, monitored, and facilitate retrieval of results.

1. The new item in the table triggers a DynamoDB stream which in turn triggers the Step Functions workflow for inference.

1. The Step Functions workflow orchestrates all steps required to run multiple ML inference jobs against the provided data object.

1. Metadata information about the ML endpoints is stored in a DynamoDB table for use in the workflow.

1. A map state in the step function calls each ML endpoint and stores the results in parallel. This allows the workflow to scale to any number of ML endpoint invocations.

1. SageMaker AI model endpoints host the ML models. The workflow invokes these endpoints per category.

1. The final results of all the ML insights gathered for the data are stored in Amazon S3.

1. After the workflow completes, you can retrieve the final results through a `GET` request to `/get-job-results`. This invokes the get job results Lambda function, which reads the Amazon S3 bucket.

1. Multi-model endpoints can extend each model type with extra optimizations, such as language-specific inference per category.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon SageMaker AI product page](https://aws.amazon.com/sagemaker/)
+ [AWS Step Functions product page](https://aws.amazon.com/step-functions/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 28, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.