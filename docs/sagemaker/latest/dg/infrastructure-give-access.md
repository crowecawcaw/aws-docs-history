# Give SageMaker AI Access to Resources in your Amazon VPC

SageMaker AI runs the following job types in an Amazon Virtual Private Cloud by default.

- Processing
- Training
- Model hosting
- Batch transform
- Amazon SageMaker Clarify
- SageMaker AI Compilation
  However, containers for these jobs access AWS resources—such as the Amazon Simple Storage Service
  (Amazon S3) buckets where you store training data and model artifacts—over the
  internet.

To control access to your data and job containers, we recommend that you create a private
VPC and configure it so that they aren't accessible over the internet. For information about
creating and configuring a VPC, see [Getting
Started With Amazon VPC](../../../AmazonVPC/latest/UserGuide/getting-started-ipv4.md "../../../AmazonVPC/latest/UserGuide/getting-started-ipv4.md") in the _Amazon VPC User Guide_. Using a VPC helps to protect your job containers and data
because you can configure your VPC so that it is not connected to the internet. Using a VPC
also allows you to monitor all network traffic in and out of your job containers by using
VPC flow logs. For more information, see [VPC Flow Logs](../../../AmazonVPC/latest/UserGuide/flow-logs.md "../../../AmazonVPC/latest/UserGuide/flow-logs.md") in
the _Amazon VPC User Guide_.

You specify your private VPC configuration when you create jobs by specifying subnets and
security groups. When you specify the subnets and security groups, SageMaker AI creates _elastic network interfaces_ that are associated with your
security groups in one of the subnets. Network interfaces allow your job containers to
connect to resources in your VPC. For information about network interfaces, see [Elastic Network Interfaces](../../../AmazonVPC/latest/UserGuide/VPC_ElasticNetworkInterfaces.md "../../../AmazonVPC/latest/UserGuide/VPC_ElasticNetworkInterfaces.md") in the _Amazon VPC User Guide_.

You specify a VPC configuration within the `VpcConfig` object of the [CreateProcessingJob](../APIReference/API_CreateProcessingJob.md "../APIReference/API_CreateProcessingJob.md") operation
or [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") operation. Specifying a VPC configuration when you create a training job gives your model access to resources within your VPC.

Specifying a VPC configuration alone doesn't change the invocation path. To connect to Amazon SageMaker AI within a VPC, create a VPC endpoint and invoke it. For more information, see [Connect to SageMaker AI Within your VPC](interface-vpc-endpoint.md "interface-vpc-endpoint.md").

###### Topics

- [Give SageMaker AI Processing Jobs Access to Resources in Your
  Amazon VPC](process-vpc.md "process-vpc.md")
- [Give SageMaker AI Training Jobs Access to Resources in Your
  Amazon VPC](train-vpc.md "train-vpc.md")
- [Give SageMaker AI Hosted Endpoints Access to Resources in Your
  Amazon VPC](host-vpc.md "host-vpc.md")
- [Give Batch Transform Jobs Access to Resources in Your
  Amazon VPC](batch-vpc.md "batch-vpc.md")
- [Give Amazon SageMaker Clarify Jobs Access to Resources in Your
  Amazon VPC](clarify-vpc.md "clarify-vpc.md")
- [Give SageMaker AI Compilation Jobs Access to Resources in Your
  Amazon VPC](neo-vpc.md "neo-vpc.md")
- [Give Inference Recommender Jobs Access to Resources in Your
  Amazon VPC](inference-recommender-vpc-access.md "inference-recommender-vpc-access.md")
