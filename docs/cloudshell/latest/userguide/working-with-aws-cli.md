# Manage AWS services from CLI in CloudShell

A key benefit of AWS CloudShell is that you can use it to manage your AWS services from the
 command line interface. This means that you don't need to download and install tools or
 configure your credentials locally beforehand. When you launch AWS CloudShell, a compute environment
 is created that has the following AWS command line tools already installed:


* [AWS CLI](#aws-cli-section "#aws-cli-section")
* [AWS Elastic Beanstalk CLI](#eb-command-line "#eb-command-line")
* [Amazon ECS CLI](#ecs-command-line "#ecs-command-line")
* [AWS SAM](#sam-cli-command-line "#sam-cli-command-line")
And because you’ve already signed into AWS, there's no requirement to configure your
 credentials locally before using services. The credentials you used to sign in to the
 AWS Management Console are forwarded to AWS CloudShell.

If you want to change the default AWS Region used for AWS CLI, you can change the value
 assigned to the `AWS_REGION` environment variable. (For more information, see [Specifying your default AWS Region
 for AWS CLI](working-with-aws-cloudshell.md#environment-variaiables-regions "working-with-aws-cloudshell.md#environment-variaiables-regions").)

The rest of this topic demonstrates how you can start using AWS CloudShell to interact with
 selected AWS services from the command line.


## AWS CLI command line examples for selected AWS
 services


The following examples represent only some of the numerous AWS services that you can
 work with using commands available from AWS CLI Version 2. For a full listing, see the [AWS CLI
 Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/index.html").



* [DynamoDB](#dynamo-example "#dynamo-example")
* [Amazon EC2](#ec2-example "#ec2-example")
* [Amazon Glacier](#s3-glacier-example "#s3-glacier-example")

### DynamoDB


DynamoDB is a fully managed NoSQL database service that provides fast and predictable
 performance with seamless scalability. This service's implementation of the NoSQL mode
 supports key-value and document data structures.


The following `create-table` command creates a NoSQL-style table that's
 named `MusicCollection` in your AWS account.



```
aws dynamodb create-table \
    --table-name MusicCollection \
    --attribute-definitions AttributeName=Artist,AttributeType=S AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --tags Key=Owner,Value=blueTeam
```

For more information, see [Using
 DynamoDB with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-dynamodb.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-services-dynamodb.html") in the *AWS Command Line Interface User Guide*.


### Amazon EC2


Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure and resizable compute
 capacity in the cloud. It's designed to make web-scale cloud computing easier and more
 accessible. 


The following `run-instances` command launches a t2.micro instance in the
 specified subnet of a VPC:



```
aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e
```

For more information, see [Using Amazon EC2
 with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html") in the *AWS Command Line Interface User Guide*.


### Amazon Glacier


Amazon Glacier and Amazon Glacier Deep Archive are a secure, durable, and extremely low-cost Amazon S3
 cloud storage classes for data archiving and long-term backup. 


The following `create-vault` command creates a vault—a container
 for storing archives:



```
aws glacier create-vault --vault-name my-vault --account-id -
```

For more information, see [Using
 Amazon Glacier with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-glacier.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-services-glacier.html") in the *AWS Command Line Interface User Guide*.


## AWS Elastic Beanstalk CLI


The AWS Elastic Beanstalk CLI provides a command line interface made to simplify creating, updating,
 and monitoring environments from a local repository. In this context, an
 *environment* refers to a collection of AWS resources running an
 application version. 


The following `create` command creates a new environment in a custom
 Amazon Virtual Private Cloud (VPC).



```
$ eb create dev-vpc --vpc.id vpc-0ce8dd99 --vpc.elbsubnets subnet-b356d7c6,subnet-02f74b0c --vpc.ec2subnets subnet-0bb7f0cd,subnet-3b6697c1 --vpc.securitygroup sg-70cff265
```

For more information, see the [EB CLI
 command reference](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-commands.html "https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-commands.html") in the *AWS Elastic Beanstalk Developer Guide*.


## Amazon ECS CLI


The Amazon Elastic Container Service (Amazon ECS) command line interface (CLI) provides several high-level commands.
 These are designed to simplify the processes of creating, updating, and monitoring clusters
 and tasks from a local development environment. (An Amazon ECS cluster is a logical grouping of
 tasks or services.) 


The following `configure` command configures the Amazon ECS CLI to create a
 cluster configuration named `ecs-cli-demo`. This cluster configuration uses
 `FARGATE` as the default launch type for the `ecs-cli-demo`
 cluster in the `us-east-1 region`.



```
ecs-cli configure --region us-east-1 --cluster ecs-cli-demo --default-launch-type FARGATE --config-name ecs-cli-demo
```

For more information, see the [Amazon ECS
 Command Line Reference](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html") in the *Amazon Elastic Container Service Developer Guide*.


## AWS SAM CLI


AWS SAM CLI is a command line tool that operates on an AWS Serverless Application Model template and application
 code. You can perform several tasks using it. These include invoking Lambda functions
 locally, creating a deployment package for your serverless application, and deploying your
 serverless application to the AWS Cloud.


The following `init` command initializes a new SAM project with required
 parameters passed as parameters:



```
sam init --runtime python3.9 --dependency-manager pip --app-template hello-world --name sam-app
```

For more information, see the [AWS SAM CLI command
 reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html") in the *AWS Serverless Application Model Developer Guide*.
