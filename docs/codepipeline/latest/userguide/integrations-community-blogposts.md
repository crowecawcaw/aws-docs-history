# Integration examples: Blog posts

- [Tracking the AWS CodePipeline build status from the third-party Git
  repository](https://aws.amazon.com/blogs/devops/aws-codepipeline-build-status-in-a-third-party-git-repository/ "https://aws.amazon.com/blogs/devops/aws-codepipeline-build-status-in-a-third-party-git-repository/")

Learn how to set up resources that will display your pipeline and build action
status in your third-party repository, making it easy for the developer to track status
without switching context.

_Published March 2021_

- [Complete CI/CD with AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/ "https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/")

Learn how to set up a pipeline that uses the CodeCommit, CodePipeline, CodeBuild, and CodeDeploy services
to compile, build, and install a version-controlled Java application onto a set of
Amazon EC2 Linux instances.

_Published September 2020_

- [Testing and creating CI/CD pipelines for AWS Step Functions](https://aws.amazon.com/blogs/devops/testing-and-creating-ci-cd-pipelines-for-aws-step-functions-using-aws-codepipeline-and-aws-codebuild/?nc1=b_rp "https://aws.amazon.com/blogs/devops/testing-and-creating-ci-cd-pipelines-for-aws-step-functions-using-aws-codepipeline-and-aws-codebuild/?nc1=b_rp")

Learn how to set up resources that will coordinate your Step Functions state machine
and your pipeline.

_Published March 2020_

- [Implementing DevSecOps Using CodePipeline](https://aws.amazon.com/blogs/devops/implementing-devsecops-using-aws-codepipeline/ "https://aws.amazon.com/blogs/devops/implementing-devsecops-using-aws-codepipeline/")

Learn how to use a CI/CD pipeline in CodePipeline to automate preventive and detective
security controls. This post covers how to use a pipeline to create a simple security
group and perform security checks during the source, test, and production stages to
improve the security posture of your AWS accounts.

_Published March 2017_

- [Continuous Deployment to Amazon ECS Using CodePipeline, CodeBuild, Amazon ECR, and CloudFormation](https://aws.amazon.com/blogs/compute/continuous-deployment-to-amazon-ecs-using-aws-codepipeline-aws-codebuild-amazon-ecr-and-aws-cloudformation/ "https://aws.amazon.com/blogs/compute/continuous-deployment-to-amazon-ecs-using-aws-codepipeline-aws-codebuild-amazon-ecr-and-aws-cloudformation/")

Learn how to create a continuous deployment pipeline to Amazon Elastic Container Service (Amazon ECS). Applications are
delivered as Docker containers using CodePipeline, CodeBuild, Amazon ECR, and CloudFormation.

    + Download a sample CloudFormation template and instructions for using it to create your
     own continuous deployment pipeline from the [ECS Reference
     Architecture: Continuous Deployment](https://github.com/awslabs/ecs-refarch-continuous-deployment "https://github.com/awslabs/ecs-refarch-continuous-deployment") repo on GitHub.

_Published January 2017_

- [Continuous Deployment for Serverless Applications](https://aws.amazon.com/blogs/compute/continuous-deployment-for-serverless-applications/ "https://aws.amazon.com/blogs/compute/continuous-deployment-for-serverless-applications/")

Learn how to use a collection of AWS services to create a continuous deployment
pipeline for your serverless applications. You'll use the Serverless Application Model
(SAM) to define the application and its resources and CodePipeline to orchestrate your
application deployment.

    + [View a sample application](https://gist.github.com/SAPessi/246b278b6b7502b157a9fbaf3981d103 "https://gist.github.com/SAPessi/246b278b6b7502b157a9fbaf3981d103") written in Go with the Gin framework and an API
     Gateway proxy shim.

_Published December 2016_

- [Scaling DevOps Deployments with CodePipeline and Dynatrace](https://www.dynatrace.com/blog/scaling-devops-deployments-with-aws-codepipeline-dynatrace/ "https://www.dynatrace.com/blog/scaling-devops-deployments-with-aws-codepipeline-dynatrace/")

Learn how use Dynatrace monitoring solutions to scale pipelines in CodePipeline,
automatically analyze test executions before code is committed, and maintain optimal
lead times.

_Published November 2016_

- [Create a Pipeline for AWS Elastic Beanstalk in CodePipeline Using AWS CloudFormation and
  CodeCommit](http://www.stelligent.com/automation/create-a-pipeline-for-elastic-beanstalk-in-codepipeline-using-cloudformation-and-codecommit/ "http://www.stelligent.com/automation/create-a-pipeline-for-elastic-beanstalk-in-codepipeline-using-cloudformation-and-codecommit/")

Learn how to implement continuous delivery in a CodePipeline pipeline for an application in
AWS Elastic Beanstalk. All AWS resources are provisioned automatically through the use of an CloudFormation
template. This walkthrough also incorporates CodeCommit and AWS Identity and Access Management (IAM).

_Published May 2016_

- [Automate CodeCommit and CodePipeline in CloudFormation](http://www.stelligent.com/automation/automate-codecommit-and-codepipeline-in-aws-cloudformation/ "http://www.stelligent.com/automation/automate-codecommit-and-codepipeline-in-aws-cloudformation/")

Use CloudFormation to automate the provisioning of AWS resources for a continuous delivery
pipeline that uses CodeCommit, CodePipeline, CodeDeploy, and AWS Identity and Access Management.

_Published April 2016_

- [Create a Cross-Account Pipeline in AWS CodePipeline](http://www.stelligent.com/automation/create-a-cross-account-pipeline-in-aws-cloudformation/ "http://www.stelligent.com/automation/create-a-cross-account-pipeline-in-aws-cloudformation/")

Learn how to automate the provisioning of cross-account access to pipelines in
AWS CodePipeline by using AWS Identity and Access Management. Includes examples in an CloudFormation template.

_Published March 2016_

- [Exploring ASP.NET Core Part 2: Continuous Delivery](https://blogs.aws.amazon.com/net/post/Tx2EHIJAM9LIW8G/Exploring-ASP-NET-Core-Part-2-Continuous-Delivery "https://blogs.aws.amazon.com/net/post/Tx2EHIJAM9LIW8G/Exploring-ASP-NET-Core-Part-2-Continuous-Delivery")

Learn how to create a full continuous delivery system for an ASP.NET Core
application using CodeDeploy and AWS CodePipeline.

_Published March 2016_

- [Create a Pipeline Using the AWS CodePipeline Console](http://www.stelligent.com/cloud/create-a-pipeline-using-the-aws-codepipeline-console/ "http://www.stelligent.com/cloud/create-a-pipeline-using-the-aws-codepipeline-console/")

Learn how to use the AWS CodePipeline console to create a two-stage pipeline in a
walkthrough based on the AWS CodePipeline [Tutorial: Create a four-stage pipeline](tutorials-four-stage-pipeline.md "tutorials-four-stage-pipeline.md").

_Published March 2016_

- [Mocking AWS CodePipeline Pipelines with AWS Lambda](http://www.stelligent.com/automation/mocking-aws-codepipeline-pipelines-with-lambda/ "http://www.stelligent.com/automation/mocking-aws-codepipeline-pipelines-with-lambda/")

Learn how to invoke a Lambda function that lets you visualize the actions and stages
in a CodePipeline software delivery process as you design it, before the pipeline is
operational. As you design your pipeline structure, you can use the Lambda function to
test whether your pipeline will complete successfully.

_Published February 2016_

- [Running AWS Lambda Functions in CodePipeline Using AWS CloudFormation](http://www.stelligent.com/automation/aws-lambda-functions-aws-codepipeline-cloudformation/ "http://www.stelligent.com/automation/aws-lambda-functions-aws-codepipeline-cloudformation/")

Learn how to create an AWS CloudFormation stack that provisions all the AWS resources used
in the user guide task [Invoke an AWS Lambda function in a pipeline
in CodePipeline](actions-invoke-lambda-function.md "actions-invoke-lambda-function.md").

_Published February 2016_

- [Provisioning Custom CodePipeline Actions in AWS CloudFormation](http://www.stelligent.com/automation/provisioning-custom-codepipeline-actions-in-cloudformation/ "http://www.stelligent.com/automation/provisioning-custom-codepipeline-actions-in-cloudformation/")

Learn how to use AWS CloudFormation to provision custom actions in CodePipeline.

_Published January 2016_

- [Provisioning CodePipeline with AWS CloudFormation](http://www.stelligent.com/automation/provisioning-aws-codepipeline-with-cloudformation/ "http://www.stelligent.com/automation/provisioning-aws-codepipeline-with-cloudformation/")

Learn how to provision a basic continuous delivery pipeline in CodePipeline using
AWS CloudFormation.

_Published December 2015_

- [Deploying from CodePipeline to OpsWorks Using a Custom Action and AWS Lambda](http://hipsterdevblog.com/blog/2015/07/28/deploying-from-codepipeline-to-opsworks-using-a-custom-action-and-lambda/ "http://hipsterdevblog.com/blog/2015/07/28/deploying-from-codepipeline-to-opsworks-using-a-custom-action-and-lambda/")

Learn how to configure your pipeline and the AWS Lambda function to deploy to
AWS OpsWorks using CodePipeline.

_Published July 2015_
