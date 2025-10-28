# CodeDeploy primary components

Before you start working with the service, you should familiarize yourself with the major
components of the CodeDeploy deployment process.

###### Topics

- [Application](#primary-components-application "#primary-components-application")
- [Compute platform](#primary-components-compute-platform "#primary-components-compute-platform")
- [Deployment configuration](#primary-components-deployment-configuration "#primary-components-deployment-configuration")
- [Deployment group](#primary-components-deployment-group "#primary-components-deployment-group")
- [Deployment type](#primary-components-deployment-type "#primary-components-deployment-type")
- [IAM instance profile](#primary-components-iam-instance-profile "#primary-components-iam-instance-profile")
- [Revision](#primary-components-revision "#primary-components-revision")
- [Service role](#primary-components-service-role "#primary-components-service-role")
- [Target revision](#primary-components-target-revision "#primary-components-target-revision")
- [Other components](#primary-components-other-components "#primary-components-other-components")

## Application

An _application_ is a name that uniquely identifies the
application you want to deploy. CodeDeploy uses this name, which functions as a container, to
ensure the correct combination of revision, deployment configuration, and deployment group
are referenced during a deployment.

## Compute platform

A _compute platform_ is a platform on which CodeDeploy deploys an application. There are three compute platforms:

- **EC2/On-Premises**: Describes instances of physical servers that can be Amazon EC2 cloud instances,
  on-premises servers, or both. Applications created using the EC2/On-Premises compute platform
  can be composed of executable files, configuration files, images, and more.

Deployments that use the EC2/On-Premises compute platform manage the way in which traffic
is directed to instances by using an in-place or blue/green
deployment type. For more information, see [Overview of CodeDeploy deployment types](welcome.md#welcome-deployment-overview "welcome.md#welcome-deployment-overview").

- **AWS Lambda**:
  Used to deploy applications that consist of an updated version of a
  Lambda function. AWS Lambda manages the Lambda function
  in a serverless compute environment made up of a high-availability compute structure. All administration
  of the compute resources is performed by AWS Lambda. For more information,
  see [Serverless Computing and Applications](https://aws.amazon.com/serverless/ "https://aws.amazon.com/serverless/"). For more information
  about AWS Lambda and Lambda functions, see [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/").

You can manage the way in which traffic
is shifted to the updated Lambda function versions during a deployment by choosing a canary,
linear, or all-at-once configuration.

- **Amazon ECS**:
  Used to deploy an Amazon ECS containerized application as a task set.
  CodeDeploy performs a blue/green deployment by installing an updated version of the application
  as a new replacement task set. CodeDeploy reroutes production traffic from the original application task set to the
  replacement task set. The original task set is terminated after a successful deployment. For more information
  about Amazon ECS, see [Amazon Elastic Container Service](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/").

You can manage the way in which traffic
is shifted to the updated task set during a deployment by choosing a canary,
linear, or all-at-once configuration.

###### Note

Amazon ECS blue/green deployments are supported through both CodeDeploy and
AWS CloudFormation. Details for these deployments are described in subsequent sections.

## Deployment configuration

A _deployment configuration_ is a set of deployment rules and
deployment success and failure conditions used by CodeDeploy during a deployment. If your deployment uses the EC2/On-Premises compute platform, you can
specify the minimum number of healthy instances for the deployment. If your deployment uses the AWS Lambda or the Amazon ECS compute platform, you can
specify how traffic is routed to your updated Lambda function or ECS task set.

For more information about specifying the minimum number of healthy hosts for a deployment that uses the EC2/On-Premises compute platform, see [About the minimum number of healthy instances](instances-health.md#minimum-healthy-hosts "instances-health.md#minimum-healthy-hosts").

The following deployment configurations specify how traffic is routed during a deployment that uses the Lambda or the ECS compute platform:

- **Canary**: Traffic is shifted in two
  increments. You can choose from predefined canary options that specify the percentage of traffic shifted to your updated Lambda function or ECS task set in the first increment
  and the interval, in minutes, before the remaining traffic is shifted in the second increment.
- **Linear**: Traffic is shifted in equal increments with
  an equal number of minutes between each increment. You can choose from predefined linear options that specify the percentage of traffic shifted in each
  increment and the number of minutes between each increment.
- **All-at-once**: All traffic is shifted from the
  original Lambda function or ECS task set to the updated function or task set all at once.

## Deployment group

A _deployment group_ is a set of individual instances. A
deployment group contains individually tagged instances, Amazon EC2 instances in Amazon EC2 Auto Scaling groups, or
both. For information about Amazon EC2 instance tags, see [Working with Tags Using the Console](../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_Console "../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_Console"). For information about on-premises
instances, see [Working with On-Premises Instances](instances-on-premises.md "instances-on-premises.md"). For information about Amazon EC2 Auto Scaling, see [Integrating CodeDeploy with Amazon EC2 Auto Scaling](integrations-aws-auto-scaling.md "integrations-aws-auto-scaling.md").

## Deployment type

A _deployment type_ is a method used to make the latest
application revision available on instances in a deployment group. There are two deployment types:

- **In-place deployment**: The application on each instance in
  the deployment group is stopped, the latest application revision is installed, and the new
  version of the application is started and validated. You can use a load balancer
  so that each instance is deregistered during its deployment and then restored to service after
  the deployment is complete. Only deployments that use the EC2/On-Premises compute platform can use in-place deployments.
  For more information about in-place deployments, see [Overview of an in-place
  deployment](welcome.md#welcome-deployment-overview-in-place "welcome.md#welcome-deployment-overview-in-place").
- **Blue/green deployment**: The behavior of your deployment depends on which
  compute platform you use:

      + **Blue/green on an EC2/On-Premises compute platform**:
       The instances in a deployment group (the original environment) are replaced by a different set of instances (the replacement environment) using these steps:




      	- Instances are provisioned for the replacement environment.
      	- The latest application revision is installed on the replacement instances.
      	- An optional wait time occurs for activities such as application testing and system
      	 verification.
      	- Instances in the replacement environment are registered with one or more Elastic Load Balancing load
      	 balancers, causing traffic to be rerouted to them. Instances in the original
      	 environment are deregistered and can be terminated or kept running for other
      	 uses.
      ###### Note

      If you use an EC2/On-Premises compute platform, be aware that blue/green deployments work with Amazon EC2 instances only.
      + **Blue/green on an AWS Lambda or Amazon ECS compute platform**: Traffic is shifted in increments according to a **canary**, **linear**, or **all-at-once** deployment configuration.
      + **Blue/green deployments through AWS CloudFormation**: Traffic is shifted from your current resources to your updated resources as part of an AWS CloudFormation stack update. Currently, only ECS blue/green deployments are supported.

  For more information about blue/green deployments, see [Overview of a blue/green
  deployment](welcome.md#welcome-deployment-overview-blue-green "welcome.md#welcome-deployment-overview-blue-green").

###### Note

Amazon ECS blue/green deployments are supported using both CodeDeploy and AWS CloudFormation.
Details for these deployments are described in subsequent sections.

## IAM instance profile

An _IAM instance profile_ is an IAM role that you attach to
your Amazon EC2 instances. This profile includes the permissions required to access the Amazon S3
buckets or GitHub repositories where the applications are
stored. For more information, see [Step 4: Create an IAM instance
profile for your Amazon EC2 instances](getting-started-create-iam-instance-profile.md "getting-started-create-iam-instance-profile.md").

## Revision

A _revision_ is a version of your application. An AWS Lambda deployment revision
is a YAML- or JSON-formatted file that specifies information about the Lambda function
to deploy. An EC2/On-Premises deployment revision is an archive file that contains source
content (source code, webpages, executable files, and deployment scripts) and an application specification file (AppSpec file). AWS Lambda revisions can be stored in Amazon S3 buckets.
EC2/On-Premises revisions are stored in Amazon S3 buckets or GitHub repositories. For Amazon S3,
a revision is uniquely identified by its Amazon S3 object key and
its ETag, version, or both. For GitHub, a revision is uniquely identified by its commit
ID.

## Service role

A _service role_ is an IAM role that grants permissions to an
AWS service so it can access AWS resources. The policies you attach to the service role
determine which AWS resources the service can access and the actions it can perform with
those resources. For CodeDeploy, a service role is used for the following:

- To read either the tags applied to the instances or the Amazon EC2 Auto Scaling group names
  associated with the instances. This enables CodeDeploy to identify instances to which it
  can deploy applications.
- To perform operations on instances, Amazon EC2 Auto Scaling groups, and Elastic Load Balancing load balancers.
- To publish information to Amazon SNS topics so that notifications can be sent when
  specified deployment or instance events occur.
- To retrieve information about CloudWatch alarms to set up alarm monitoring for
  deployments.

For more information, see [Step 2: Create a service role for
CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md").

## Target revision

A _target revision_ is the most recent version of the
application revision that you have uploaded to your repository and want to deploy to the
instances in a deployment group. In other words, the application revision currently targeted
for deployment. This is also the revision that is pulled for
automatic deployments.

## Other components

For information about other components in the CodeDeploy workflow, see the following
topics:

- [Choose a CodeDeploy repository type](application-revisions-repository-type.md "application-revisions-repository-type.md")
- [Deployments](deployment-steps.md "deployment-steps.md")
- [Application Specification Files](application-specification-files.md "application-specification-files.md")
- [Instance Health](instances-health.md "instances-health.md")
- [Working with the CodeDeploy agent](codedeploy-agent.md "codedeploy-agent.md")
- [Working with On-Premises Instances](instances-on-premises.md "instances-on-premises.md")
