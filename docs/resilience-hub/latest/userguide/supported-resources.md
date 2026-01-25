# AWS Resilience Hub supported resources

Resources that affect application performance in the case of disruption are fully supported
by AWS Resilience Hub top-level resources such as `AWS::RDS::DBInstance` and
`AWS::RDS::DBCluster`.

To learn more about the permissions required for AWS Resilience Hub to include resources from all the
supported services in your assessment, see [AWSResilienceHubAsssessmentExecutionPolicy](security-iam-awsmanpol.md#security_iam_aws-assessment-policy "security-iam-awsmanpol.md#security_iam_aws-assessment-policy").

AWS Resilience Hub supports resources from the following AWS services:

- Compute
  - Amazon Elastic Compute Cloud (Amazon EC2)

  ###### Note

  AWS Resilience Hub does not support the old Amazon Resource Name (ARN) format for accessing
  Amazon EC2 resources. The new ARN format uses your AWS account ID and enables the enhanced
  ability to tag resources in your cluster, and also tracks the cost of services and tasks
  running in your cluster.

      - **Old format (deprecated)** –
       `arn:aws:ec2:<region>::instance/<instance-id>`
      - **New format** –
       `arn:aws:ec2:<region>:<account-id>:instance/<instance-id>`For more information about the new ARN format, see [Migrating your Amazon ECS deployment to the new ARN and resource ID format](https://aws.amazon.com/blogs/compute/migrating-your-amazon-ecs-deployment-to-the-new-arn-and-resource-id-format-2/ "https://aws.amazon.com/blogs/compute/migrating-your-amazon-ecs-deployment-to-the-new-arn-and-resource-id-format-2/").

  - AWS Lambda
  - Amazon Elastic Kubernetes Service (Amazon EKS)
  - Amazon Elastic Container Service (Amazon ECS)
  - AWS Step Functions

- Database
  - Amazon Relational Database Service (Amazon RDS)
  - Amazon DynamoDB
  - Amazon DocumentDB
  - Amazon ElastiCache

- Networking and Content Delivery
  - Amazon Route 53
  - Elastic Load Balancing
  - Network Address Translation (NAT)

- Storage
  - Amazon Elastic Block Store (Amazon EBS)
  - Amazon Elastic File System (Amazon EFS)
  - Amazon Simple Storage Service (Amazon S3)
  - Amazon FSx for Windows File Server

- Others
  - Amazon API Gateway
  - Amazon Application Recovery Controller (ARC) (Amazon ARC)
  - Amazon Simple Notification Service
  - Amazon Simple Queue Service
  - AWS Auto Scaling
  - AWS Backup
  - AWS Elastic Disaster Recovery

###### Note

- AWS Resilience Hub provides additional transparency for your application resources by allowing you
  to view the supported instances of each resource. In addition, AWS Resilience Hub provides more
  accurate resiliency recommendations by identifying unique instance of each resource while
  discovering the resource instances during assessment process. For more information about
  adding resource instances to your application, see [Editing AWS Resilience Hub application resources](application-resources.md "application-resources.md").
- AWS Resilience Hub supports Amazon EKS and Amazon ECS on AWS Fargate.
- AWS Resilience Hub supports assessment of AWS Backup resource as a part of the following
  services:
  - Amazon EBS
  - Amazon EFS
  - Amazon S3
  - Amazon Aurora Global Database
  - Amazon DynamoDB
  - Amazon RDS services
  - Amazon FSx for Windows File Server

- Amazon ARC in AWS Resilience Hub assesses only Amazon DynamoDB global, Elastic Load Balancing, Amazon RDS, and AWS Auto Scaling
  groups.
- For AWS Resilience Hub to assess the cross-Region resources, group the resources under a single
  Application Component. For more information about the resources supported by each of the
  AWS Resilience Hub Application Components and grouping resources, see [Grouping resources in an Application
  Component](AppComponent.md "AppComponent.md").
- Currently, AWS Resilience Hub does not support cross-Region assessments for Amazon EKS clusters if
  either the Amazon EKS cluster is located or if the application is created in an opt-in enabled
  AWS Region.
- Currently, AWS Resilience Hub assesses only the following Kubernetes resource types:
  - Deployments
  - ReplicaSets
  - Pods

- Currently, AWS Resilience Hub supports only the following engine types for ElastiCache resources:

      + Redis OSS engines

  AWS Resilience Hub ignores the following types of resources:

- **Resources that do not affect estimated workload RTO or estimated
  workload RPO** – Resources such as `AWS::RDS::DBParameterGroup`,
  which does not affect estimated workload RTO or estimated workload RPO, is ignored by
  AWS Resilience Hub.
- **Non-top level resources** – AWS Resilience Hub only imports
  top-level resources, because they can derive other properties by querying the properties of
  top-level resources. For example, `AWS::ApiGateway::RestApi` and
  `AWS::ApiGatewayV2::Api` are supported resources for Amazon API Gateway. However,
  `AWS::ApiGatewayV2::Stage` is not a top-level resource. Therefore, it is not
  imported by AWS Resilience Hub.

###### Note

**Unsupported resources**

- You cannot identify multiple resources by using AWS Resource Groups (Amazon Route 53 RecordSets and
  API-GW HTTP) and Amazon Aurora Global resources. If you want to analyze these resources as part of
  your assessment, you must manually add the resource to the application. However, when you add
  Amazon Aurora Global resources for assessment, it must be grouped with the Amazon RDS instance's
  Application Component. For more information about editing resources, see [Editing AWS Resilience Hub application resources](application-resources.md "application-resources.md").
- These resources can affect application recovery, but they aren't fully supported by
  AWS Resilience Hub at this time. AWS Resilience Hub makes an effort to warn users about unsupported resources if
  the application is backed by an AWS CloudFormation stack, Terraform state file, AWS Resource Groups, or
  myApplications application.
- During the import process of an application's resources into AWS Resilience Hub, some resources
  may be ignored. When resources are ignored, it means they cannot be imported at all. However,
  resources marked as unsupported are currently not compatible with AWS Resilience Hub but may be
  supported in the future, allowing them to be included in the application for assessments.
  Additionally, AWS Resilience Hub might ignore certain resources if they are not supported by AWS Resource Groups.
  For more information about the resources supported by AWS Resource Groups, see [Resource types you
  can use with AWS Resource Groups and Tag Editor](../../../ARG/latest/userguide/supported-resources.md "../../../ARG/latest/userguide/supported-resources.md").
