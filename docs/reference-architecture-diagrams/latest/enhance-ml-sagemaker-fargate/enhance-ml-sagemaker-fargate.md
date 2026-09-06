

# Enhance Existing ML Lifecycles with Amazon SageMaker AI and AWS Fargate
<a name="enhance-ml-sagemaker-fargate"></a>

Publication date: **March 28, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to enhance your existing ML workflow. With [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) model training and AWS Fargate endpoints, you can preserve custom serverless inference while benefiting from managed training.

## Enhance Existing ML Lifecycles with Amazon SageMaker AI and AWS Fargate
<a name="diagram1"></a>

![Architecture diagram showing ML lifecycle enhancement with SageMaker AI and AWS Fargate.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/enhance-ml-sagemaker-fargate/images/enhance-ml-sagemaker-fargate.png)


The following steps describe the architecture:

1. SageMaker AI provides Jupyter Notebook instances for data scientists to prepare their data and launch SageMaker AI training jobs.

1. By selecting the desired algorithm, SageMaker AI image, and configuring the appropriate parameters, you can run multiple SageMaker AI training jobs. You can also benefit from features such as automated hyperparameter tuning.

1. If you need additional algorithms or have pre-existing code, you can build your own SageMaker AI Docker images.

1. A trained model artifact is generated and stored in a dedicated [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket. When the data scientist is satisfied with performance, the model is uploaded to a dedicated path in the bucket.

1. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) connects to the rest of the ML lifecycle and initiates the remaining lifecycle tasks outside of SageMaker AI.

1. The [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) workflow orchestrates all steps of the remaining ML pipeline by using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions. [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) generates custom Docker images with the correct algorithm, framework, and model.

1. The new container image is tested and deployed into AWS Fargate through [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) by using blue/green deployment.

1. The SageMaker AI-trained model can now run in your pre-existing compute environment. In this case, Docker containers are deployed in AWS Fargate with Amazon Elastic Container Service (Amazon ECS) automatic scaling.

1. An Application Load Balancer fronts Fargate to balance the incoming load with automatic horizontal scaling based on model endpoint latency.

1. You consume the model through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) from your browser or mobile application.

1. [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) user pool integrated with API Gateway manages authentication and authorization of the endpoint.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon SageMaker AI product page](https://aws.amazon.com/sagemaker/)
+ [AWS Fargate product page](https://aws.amazon.com/fargate/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 28, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.