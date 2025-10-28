# Deploy a state machine using a starter template for Step Functions

To deploy state machines for a variety of example use cases and patterns, you can choose one of the following starter templates in the [AWS Step Functions
console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/"). These starter templates are ready-to-run sample projects that automatically create the workflow prototype and definition, and all related AWS resources for the project.

You can use these sample projects to deploy and run them as is, or use the workflow prototypes to build on them. If you build upon these projects, Step Functions creates the workflow prototype, but doesn't deploy the resources listed in the workflow definition.

When you deploy the sample projects, they provision a fully functional state machine, and create the
related resources for the state machine to run. When you create a sample project, Step Functions uses AWS CloudFormation to create
the related resources referenced by the state machine.

###### List of starter templates

- [Manage a container task with Amazon ECS and Amazon SNS](sample-project-container-task-notification.md "sample-project-container-task-notification.md")
- [Transfer data records with Lambda, DynamoDB,
  and Amazon SQS](sample-project-transfer-data-sqs.md "sample-project-transfer-data-sqs.md")
- [Poll for job status with Lambda and AWS Batch](sample-project-job-poller.md "sample-project-job-poller.md")
- [Create a task timer with Lambda and Amazon SNS](task-timer-sample.md "task-timer-sample.md")
- [Create a callback pattern example with Amazon SQS, Amazon SNS, and Lambda](callback-task-sample-sqs.md "callback-task-sample-sqs.md")
- [Manage an Amazon EMR job](sample-emr-job.md "sample-emr-job.md")
- [Run an EMR Serverless job](sample-emr-serverless-job.md "sample-emr-serverless-job.md")
- [Start a workflow within a workflow with Step Functions and Lambda](sample-start-workflow.md "sample-start-workflow.md")
- [Process data from a queue with a Map state in Step Functions](sample-map-state.md "sample-map-state.md")
- [Process a CSV file from Amazon S3 using a Distributed Map](sample-dist-map-csv-process.md "sample-dist-map-csv-process.md")
- [Process data in an Amazon S3 bucket with Distributed Map](sample-dist-map-s3data-process.md "sample-dist-map-s3data-process.md")
- [Train a machine learning model using Amazon SageMaker AI](sample-train-model.md "sample-train-model.md")
- [Tune the hyperparameters of a machine learning model in SageMaker AI](sample-hyper-tuning.md "sample-hyper-tuning.md")
- [Perform AI prompt-chaining with Amazon Bedrock](sample-bedrock-prompt-chaining.md "sample-bedrock-prompt-chaining.md")
- [Process high-volume messages from Amazon SQS
  with Step Functions Express workflows](sample-project-express-high-volume-sqs.md "sample-project-express-high-volume-sqs.md")
- [Perform selective checkpointing using Standard and Express workflows](sample-project-express-selective-checkpointing.md "sample-project-express-selective-checkpointing.md")
- [Build an AWS CodeBuild project using Step Functions](sample-project-codebuild.md "sample-project-codebuild.md")
- [Preprocess data and train a machine learning model with Amazon SageMaker AI](sample-preprocess-feature-transform.md "sample-preprocess-feature-transform.md")
- [Orchestrate AWS Lambda functions with Step Functions](sample-lambda-orchestration.md "sample-lambda-orchestration.md")
- [Start an Athena query and send a results notification](sample-athena-query.md "sample-athena-query.md")
- [Execute queries in sequence and parallel using Athena](run-multiple-queries.md "run-multiple-queries.md")
- [Query large datasets using an AWS Glue crawler](sample-query-large-datasets.md "sample-query-large-datasets.md")
- [Keep data in a target table updated with AWS Glue and Athena](sample-keep-data-updated.md "sample-keep-data-updated.md")
- [Create and manage an Amazon EKS cluster with a node group](sample-eks-cluster.md "sample-eks-cluster.md")
- [Interact with an API managed by API Gateway](sample-apigateway-workflow.md "sample-apigateway-workflow.md")
- [Call a microservice running on Fargate using API Gateway integration](sample-apigateway-ecs-workflow.md "sample-apigateway-ecs-workflow.md")
- [Send a custom event to an EventBridge event bus](sample-eventbridge-custom-event.md "sample-eventbridge-custom-event.md")
- [Invoke Synchronous Express Workflows through API Gateway](synchronous-execution.md "synchronous-execution.md")
- [Run an ETL/ELT workflow using Step Functions and the Amazon Redshift API](sample-etl-orchestration.md "sample-etl-orchestration.md")
- [Manage a batch job with AWS Batch and Amazon SNS](batch-job-notification.md "batch-job-notification.md")
- [Fan out batch jobs with Map state](sample-batch-fan-out.md "sample-batch-fan-out.md")
- [Run an AWS Batch job with Lambda](sample-batch-lambda.md "sample-batch-lambda.md")
