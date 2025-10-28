# AWS services used by AWS ParallelCluster

The following Amazon Web Services (AWS) services are used by AWS ParallelCluster.

###### Topics

- [Amazon API Gateway](#aws-api-gateway-v3 "#aws-api-gateway-v3")
- [AWS Batch](#aws-batch-v3 "#aws-batch-v3")
- [AWS CloudFormation](#aws-services-cloudformation-v3 "#aws-services-cloudformation-v3")
- [Amazon CloudWatch](#amazon-cloudwatch-v3 "#amazon-cloudwatch-v3")
- [Amazon CloudWatch Events](#amazon-cloudwatch-events-v3 "#amazon-cloudwatch-events-v3")
- [Amazon CloudWatch Logs](#amazon-cloudwatch-logs-v3 "#amazon-cloudwatch-logs-v3")
- [AWS CodeBuild](#aws-codebuild-v3 "#aws-codebuild-v3")
- [Amazon DynamoDB](#amazon-dynamodb-v3 "#amazon-dynamodb-v3")
- [Amazon Elastic Block Store](#amazon-elastic-block-store-ebs-v3 "#amazon-elastic-block-store-ebs-v3")
- [Amazon Elastic Compute Cloud](#amazon-ec2-v3 "#amazon-ec2-v3")
- [Amazon Elastic Container Registry](#amazon-elastic-container-registry-ecr-v3 "#amazon-elastic-container-registry-ecr-v3")
- [Amazon EFS](#amazon-efs-v3 "#amazon-efs-v3")
- [Amazon FSx for Lustre](#amazon-fsx-for-lustre-v3 "#amazon-fsx-for-lustre-v3")
- [Amazon FSx for NetApp ONTAP](#amazon-fsx-ontap-v3 "#amazon-fsx-ontap-v3")
- [Amazon FSx for OpenZFS](#amazon-fsx-openzfs-v3 "#amazon-fsx-openzfs-v3")
- [AWS Identity and Access Management](#aws-identity-and-access-management-iam-v3 "#aws-identity-and-access-management-iam-v3")
- [AWS Lambda](#aws-lambda-v3 "#aws-lambda-v3")
- [Amazon RDS](#aws-rds-v3 "#aws-rds-v3")
- [Amazon Route 53](#amazon-route-53-v3 "#amazon-route-53-v3")
- [Amazon Simple Notification Service](#aws-sns-v3 "#aws-sns-v3")
- [Amazon Simple Storage Service](#amazon-s3-v3 "#amazon-s3-v3")
- [Amazon VPC](#amazon-vpc-v3 "#amazon-vpc-v3")
- [Elastic Fabric Adapter](#aws-efa-v3 "#aws-efa-v3")
- [EC2 Image Builder](#aws-image-builder-v3 "#aws-image-builder-v3")
- [Amazon DCV](#nice-dcv-v3 "#nice-dcv-v3")

## Amazon API Gateway

Amazon API Gateway is an AWS service that makes it possible to create, publish, maintain, monitor,
and secure REST, HTTP, and WebSocket APIs at any scale

AWS ParallelCluster uses API Gateway to host the AWS ParallelCluster API.

For more information about Amazon API Gateway, see [https://aws.amazon.com/api-gateway/](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") and [https://docs.aws.amazon.com/apigateway/](../../../apigateway.md "../../../apigateway.md").

## AWS Batch

AWS Batch is an AWS managed job scheduler service. It dynamically provisions the optimal quantity
and type of compute resources (for example, CPU or memory-optimized instances) in AWS Batch clusters.
These resources are provisioned based on the specific requirements of your batch jobs, including
volume requirements. With AWS Batch, you don't need to install or manage additional batch computing
software or server clusters to run your jobs effectively.

AWS Batch is used only with AWS Batch clusters.

For more information about AWS Batch, see [https://aws.amazon.com/batch/](https://aws.amazon.com/batch/ "https://aws.amazon.com/batch/")
and [https://docs.aws.amazon.com/batch/](../../../batch.md "../../../batch.md").

## AWS CloudFormation

AWS CloudFormation is an infrastructure-as-code service that provides a common language to model and provision
AWS and third-party application resources in your cloud environment. It is the main service used
by AWS ParallelCluster. Each cluster in AWS ParallelCluster is represented as a stack, and all resources
required by each cluster are defined within the AWS ParallelCluster CloudFormation template. In most cases,
AWS ParallelCluster CLI commands directly correspond to AWS CloudFormation stack commands, such as create, update,
and delete. Instances that are launched within a cluster make HTTPS calls to the AWS CloudFormation endpoint in
the AWS Region where the cluster is launched.

For more information about AWS CloudFormation, see [https://aws.amazon.com/cloudformation/](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") and [https://docs.aws.amazon.com/cloudformation/](../../../cloudformation.md "../../../cloudformation.md").

## Amazon CloudWatch

Amazon CloudWatch (CloudWatch) is a monitoring and observability service that provides you with data and
actionable insights. These insights can be used to monitor your applications, respond to
performance changes and service exceptions, and optimize resource utilization. In AWS ParallelCluster,
CloudWatch is used for a dashboard, to monitor and log Docker image build steps and the output of
the AWS Batch jobs.

Before AWS ParallelCluster version 2.10.0, CloudWatch was used only with AWS Batch clusters.

For more information about CloudWatch, see [https://aws.amazon.com/cloudwatch/](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") and [https://docs.aws.amazon.com/cloudwatch/](../../../cloudwatch.md "../../../cloudwatch.md").

## Amazon CloudWatch Events

Amazon CloudWatch Events (CloudWatch Events) delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources.
Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams.
In AWS ParallelCluster, CloudWatch Events is used for AWS Batch jobs.

For more information about CloudWatch Events, see [https://docs.aws.amazon.com//eventbridge/latest/userguide/eb-cwe-now-eb](../../../eventbridge/latest/userguide/eb-cwe-now-eb.md "../../../eventbridge/latest/userguide/eb-cwe-now-eb.md").

## Amazon CloudWatch Logs

Amazon CloudWatch Logs (CloudWatch Logs) is one of the core features of Amazon CloudWatch. You can use it to monitor, store, view, and search
the log files for many of the components used by AWS ParallelCluster.

Before AWS ParallelCluster version 2.6.0, CloudWatch Logs was only used with AWS Batch clusters.

For more information, see [Integration with Amazon CloudWatch Logs](cloudwatch-logs-v3.md "cloudwatch-logs-v3.md").

## AWS CodeBuild

AWS CodeBuild (CodeBuild) is an AWS managed continuous integration service that compiles source code, runs tests, and
produces software packages that are ready to deploy. In AWS ParallelCluster, CodeBuild is used to automatically and
transparently build Docker images when clusters are created.

CodeBuild is used only with AWS Batch clusters.

For more information about CodeBuild, see [https://aws.amazon.com/codebuild/](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/") and [https://docs.aws.amazon.com/codebuild/](../../../codebuild.md "../../../codebuild.md").

## Amazon DynamoDB

Amazon DynamoDB (DynamoDB) is a fast and flexible NoSQL database service. It is used to store the minimal state
information of the cluster. The head node tracks provisioned instances in a DynamoDB table.

DynamoDB is not used with AWS Batch clusters.

For more information about DynamoDB, see [https://aws.amazon.com/dynamodb/](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
and [https://docs.aws.amazon.com/dynamodb/](../../../dynamodb.md "../../../dynamodb.md").

## Amazon Elastic Block Store

Amazon Elastic Block Store (Amazon EBS) is a high-performance block storage service that provides persistent storage for shared
volumes. All Amazon EBS settings can be passed through the configuration. Amazon EBS volumes can either be initialized empty or
from an existing Amazon EBS snapshot.

For more information about Amazon EBS, see [https://aws.amazon.com/ebs/](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") and [https://docs.aws.amazon.com/ebs/](../../../ebs.md "../../../ebs.md").

## Amazon Elastic Compute Cloud

Amazon Elastic Compute Cloud (Amazon EC2 ) provides the computing capacity for AWS ParallelCluster. The head and compute nodes
are Amazon EC2 instances. Any instance type that supports hardware virtual machine (HVM) can be selected.
The head and compute nodes can be different instance types. Moreover, if multiple queues are used,
some or all of compute nodes can also be launched as a Spot Instance. Instance store volumes found
on the instances are mounted as striped Logical Volume Manager (LVM) volumes.

For more information about Amazon EC2 , see [https://aws.amazon.com/ec2/](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") and [https://docs.aws.amazon.com/ec2/](../../../ec2.md "../../../ec2.md").

## Amazon Elastic Container Registry

Amazon Elastic Container Registry (Amazon ECR) is a fully managed Docker container registry that makes it easy to store, manage, and deploy
Docker container images. In AWS ParallelCluster, Amazon ECR stores the Docker images that are built when clusters are
created. The Docker images are then used by AWS Batch to run the containers for the submitted jobs.

Amazon ECR is used only with AWS Batch clusters.

For more information, see [https://aws.amazon.com/ecr/](https://aws.amazon.com/ecr/ "https://aws.amazon.com/ecr/") and [https://docs.aws.amazon.com/ecr/](../../../ecr.md "../../../ecr.md").

## Amazon EFS

Amazon Elastic File System (Amazon EFS) provides a simple, scalable, and fully managed elastic NFS file system for use with AWS Cloud
services and on-premises resources. Amazon EFS is used when the [EfsSettings](SharedStorage-v3.md#SharedStorage-v3-EfsSettings "SharedStorage-v3.md#SharedStorage-v3-EfsSettings") are specified. Support for Amazon EFS was added in AWS ParallelCluster version 2.1.0.

For more information about Amazon EFS, see [https://aws.amazon.com/efs/](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") and [https://docs.aws.amazon.com/efs/](../../../efs.md "../../../efs.md").

## Amazon FSx for Lustre

FSx for Lustre provides a high-performance file system that uses the open-source Lustre file system. FSx for Lustre is
used when the [FsxLustreSettings properties](SharedStorage-v3.md#SharedStorage-v3-FsxLustreSettings.properties "SharedStorage-v3.md#SharedStorage-v3-FsxLustreSettings.properties")
are specified. Support for FSx for Lustre was added in AWS ParallelCluster version 2.2.1.

For more information about FSx for Lustre, see [https://aws.amazon.com/fsx/lustre/](https://aws.amazon.com/fsx/lustre/ "https://aws.amazon.com/fsx/lustre/") and [https://docs.aws.amazon.com/fsx/](../../../fsx.md "../../../fsx.md").

## Amazon FSx for NetApp ONTAP

FSx for ONTAP provides a fully managed shared storage system built on NetApp's popular ONTAP file system. FSx for ONTAP is
used when [FsxOntapSettings
properties](SharedStorage-v3.md#SharedStorage-v3-FsxOntapSettings.properties "SharedStorage-v3.md#SharedStorage-v3-FsxOntapSettings.properties")
are specified. Support for FSx for ONTAP was added in AWS ParallelCluster version 3.2.0.

For more information about FSx for ONTAP, see [https://aws.amazon.com/fsx/netapp-ontap/](https://aws.amazon.com/fsx/netapp-ontap/ "https://aws.amazon.com/fsx/netapp-ontap/") and [https://docs.aws.amazon.com/fsx/](../../../fsx.md "../../../fsx.md").

## Amazon FSx for OpenZFS

FSx for OpenZFS provides a fully managed shared storage system built on the popular OpenZFS file system. FSx for OpenZFS is
used when the [FsxOpenZfsSettings properties](SharedStorage-v3.md#SharedStorage-v3-FsxOpenZfsSettings.properties "SharedStorage-v3.md#SharedStorage-v3-FsxOpenZfsSettings.properties")
are specified. Support for FSx for OpenZFS was added in AWS ParallelCluster version 3.2.0.

For more information about FSx for OpenZFS, see [https://aws.amazon.com/fsx/openzfs/](https://aws.amazon.com/fsx/openzfs/ "https://aws.amazon.com/fsx/openzfs/") and [https://docs.aws.amazon.com/fsx/](../../../fsx.md "../../../fsx.md").

## AWS Identity and Access Management

AWS Identity and Access Management (IAM) is used within AWS ParallelCluster to provide a least privileged IAM role for Amazon EC2 for the
instance that is specific to each individual cluster. AWS ParallelCluster instances are given access only to the
specific API calls that are required to deploy and manage the cluster.

With AWS Batch clusters, IAM roles are also created for the components that are involved with the Docker image
building process when clusters are created. These components include the Lambda functions that are allowed to add and
delete Docker images to and from the Amazon ECR repository. They also include the functions allowed to delete the Amazon S3
bucket that is created for the cluster and CodeBuild project. There are also roles for AWS Batch resources, instances,
and jobs.

For more information about IAM, see [https://aws.amazon.com/iam/](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") and [https://docs.aws.amazon.com/iam/](../../../iam.md "../../../iam.md").

## AWS Lambda

AWS Lambda (Lambda) runs the functions that orchestrate the creation of Docker images. Lambda also manages the
cleanup of custom cluster resources, such as Docker images stored in the Amazon ECR repository and on Amazon S3.

For more information about Lambda, see [https://aws.amazon.com/lambda/](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") and
[https://docs.aws.amazon.com/lambda/](../../../lambda.md "../../../lambda.md").

## Amazon RDS

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud.

AWS ParallelCluster uses Amazon RDS for AWS Batch and Slurm.

For more information about Amazon RDS, see [https://aws.amazon.com/rds/](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") and [https://docs.aws.amazon.com/rds/](../../../rds.md "../../../rds.md").

## Amazon Route 53

Amazon Route 53 (Route 53) is used to create hosted zones with hostnames and fully qualified domain names for each of the
compute nodes.

For more information about Route 53, see [https://aws.amazon.com/route53/](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/")
and [https://docs.aws.amazon.com/route53/](../../../route53.md "../../../route53.md").

## Amazon Simple Notification Service

(Amazon SNS) is a managed service that provides message delivery from publishers to subscribers (also known as producers and consumers).

AWS ParallelCluster uses Amazon SNS for API hosting.

For more information about Amazon SNS, see [https://aws.amazon.com/sns/](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") and [https://docs.aws.amazon.com/sns/](../../../sns.md "../../../sns.md").

## Amazon Simple Storage Service

Amazon Simple Storage Service (Amazon S3) stores AWS ParallelCluster templates located in each AWS Region. AWS ParallelCluster can be configured
to allow CLI/SDK tools to use Amazon S3.

AWS ParallelCluster also creates an Amazon S3 bucket in your AWS account to store resources that are used
by your clusters, such as the cluster configuration file. AWS ParallelCluster maintains one Amazon S3 bucket in each AWS Region
that you create clusters in.

When you use AWS Batch cluster, an Amazon S3 bucket in your account is used for storing related data. For example, the
bucket stores artifacts created when a Docker image and scripts are created from submitted jobs.

For more information, see [https://aws.amazon.com/s3/](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") and [https://docs.aws.amazon.com/s3/](../../../s3.md "../../../s3.md").

## Amazon VPC

An Amazon Virtual Private Cloud (VPC) defines a network used by the nodes in your cluster.

For more information about Amazon VPC, see [https://aws.amazon.com/vpc/](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") and [https://docs.aws.amazon.com/vpc/](../../../vpc.md "../../../vpc.md").

## Elastic Fabric Adapter

Elastic Fabric Adapter (EFA) is a network interface for instances that you can use to run applications
requiring high levels of inter-node communications at scale on AWS.

For more information about Elastic Fabric Adapter, see [https://aws.amazon.com/hpc/efa/](https://aws.amazon.com/hpc/efa/ "https://aws.amazon.com/hpc/efa/").

## EC2 Image Builder

EC2 Image Builder is a fully managed AWS service that helps you to automate the creation, management, and deployment of
customized, secure, and up-to-date server images.

AWS ParallelCluster uses Image Builder to create and manage AWS ParallelCluster images.

For more information about EC2 Image Builder, see [https://aws.amazon.com/image-builder/](https://aws.amazon.com/image-builder/ "https://aws.amazon.com/image-builder/") and [https://docs.aws.amazon.com/imagebuilder/](../../../imagebuilder.md "../../../imagebuilder.md").

## Amazon DCV

Amazon DCV is a high-performance remote display protocol that provides a secure way to deliver remote desktops and
application streaming to any device over varying network conditions. Amazon DCV is used when the [HeadNode section](HeadNode-v3.md "HeadNode-v3.md") / [Dcv](HeadNode-v3.md#HeadNode-v3-Dcv "HeadNode-v3.md#HeadNode-v3-Dcv")
settings are specified. Support for Amazon DCV was added in AWS ParallelCluster version 2.5.0.

For more information about Amazon DCV, see [https://aws.amazon.com/hpc/dcv/](https://aws.amazon.com/hpc/dcv/ "https://aws.amazon.com/hpc/dcv/")
and [https://docs.aws.amazon.com/dcv/](../../../dcv.md "../../../dcv.md").
