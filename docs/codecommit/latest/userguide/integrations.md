AWS CodeCommit is no longer available to new customers. Existing customers of
AWS CodeCommit can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider")

# Product and service integrations with AWS CodeCommit

By default, CodeCommit is integrated with a number of AWS services. You can also use CodeCommit with
products and services outside of AWS. The following information can help you configure CodeCommit
to integrate with the products and services you use.

###### Topics

- [Integration with other AWS services](#integrations-aws "#integrations-aws")
- [Integration examples from the community](#integrations-community "#integrations-community")

## Integration with other AWS services

CodeCommit is integrated with the following AWS services:

|                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AWS Amplify**                        | [AWS Amplify](https://aws.amazon.com/amplify/ "https://aws.amazon.com/amplify/") makes it easy<br>to create, configure, and implement scalable mobile applications powered by AWS.<br>Amplify seamlessly provisions and manages your mobile backend and provides a<br>simple framework to easily integrate your backend with your iOS, Android, Web, and<br>React Native frontends. Amplify also automates the application release process of<br>both your frontend and backend, which makes it possible for you to deliver features<br>faster.<br>You can connect your CodeCommit repository in the Amplify console. After you<br>authorize the Amplify console, Amplify fetches an access token from the<br>repository provider, but it doesn't store the token on the AWS servers. Amplify<br>accesses your repository using deploy keys installed in a specific repository<br>only.<br>Learn more:<br>• [AWS Amplify User Guide](../../../amplify/latest/userguide/welcome.md "../../../amplify/latest/userguide/welcome.md")<br>• [Getting<br>Started](../../../amplify/latest/userguide/getting-started.md "../../../amplify/latest/userguide/getting-started.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **AWS Cloud9**                         | [AWS Cloud9](../../../cloud9/latest/user-guide.md "../../../cloud9/latest/user-guide.md") contains a collection of tools that you<br>use to code, build, run, test, debug, and release software in the cloud. This<br>collection of tools is referred to as the AWS Cloud9 integrated development environment,<br>or IDE.<br>You access the AWS Cloud9 IDE through a web browser. The IDE offers a rich<br>code-editing experience with support for several programming languages and runtime<br>debuggers, and a built-in terminal.<br>Learn more:<br>• [AWS Cloud9 User Guide](../../../cloud9/latest/user-guide/welcome.md "../../../cloud9/latest/user-guide/welcome.md")<br>• [AWS CodeCommit Sample for<br>AWS Cloud9](../../../cloud9/latest/user-guide/sample-codecommit.md "../../../cloud9/latest/user-guide/sample-codecommit.md")<br>• [Integrate AWS Cloud9 with AWS CodeCommit](setting-up-ide-c9.md "setting-up-ide-c9.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **AWS CloudFormation**                 | [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md") is a service that helps you model and<br>set up your AWS resources so that you can spend less time managing those resources<br>and more time focusing on your applications. You create a template that describes<br>resources, including a CodeCommit repository, and AWS CloudFormation takes care of provisioning and<br>configuring those resources for you.<br>Learn more:<br>• [AWS CodeCommit Repository resource page](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **AWS CloudTrail**                     | [CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") captures AWS API calls and related<br>events made by or on behalf of an Amazon Web Services account and delivers log files to an<br>Amazon S3 bucket that you specify. You can configure CloudTrail to capture API calls from the<br>AWS CodeCommit console, CodeCommit commands from the AWS CLI, the local Git client, and from the<br>CodeCommit API.<br>Learn more:<br>• [Logging AWS CodeCommit API calls with AWS CloudTrail](integ-cloudtrail.md "integ-cloudtrail.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Amazon CloudWatch Events**           | [CloudWatch Events](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md") delivers a near real-time stream of<br>system events that describe changes in AWS resources. Using simple rules that you<br>can quickly set up, you can match events and route them to one or more target<br>functions or streams. CloudWatch Events becomes aware of operational changes as they occur.<br>CloudWatch Events responds to these operational changes and takes action as necessary, by<br>sending messages to respond to the environment, activating functions, making<br>changes, and capturing state information.<br>You can configure CloudWatch Events to monitor CodeCommit repositories and respond to repository<br>events by targeting streams, functions, tasks, or other processes in other AWS<br>services, such as Amazon Simple Queue Service, Amazon Kinesis, AWS Lambda, and many more.<br>Learn more:<br>• [CloudWatch Events User<br>Guide](../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md")<br>• [AWS CodeCommit<br>Events](../../../AmazonCloudWatch/latest/events/EventTypes.md#codecommit_event_type "../../../AmazonCloudWatch/latest/events/EventTypes.md#codecommit_event_type")<br>• Blog post: [Build Serverless AWS CodeCommit Workflows using Amazon CloudWatch Events and JGit](https://aws.amazon.com/blogs/devops/build-serverless-aws-codecommit-workflows-using-amazon-cloudwatch-events-and-jgit/ "https://aws.amazon.com/blogs/devops/build-serverless-aws-codecommit-workflows-using-amazon-cloudwatch-events-and-jgit/") |
| **AWS CodeBuild**                      | [CodeBuild](../../../codebuild/latest/userguide/welcome.md "../../../codebuild/latest/userguide/welcome.md") is a fully managed build service in the cloud that compiles your<br>source code, runs unit tests, and produces artifacts that are ready to deploy. You<br>can store the source code to be built and the build specification in a CodeCommit<br>repository. You can use CodeBuild directly with CodeCommit, or you can incorporate both CodeBuild<br>and CodeCommit in a continuous delivery pipeline with CodePipeline.<br>Learn more:<br>• [Plan a Build](../../../codebuild/latest/userguide/planning.md "../../../codebuild/latest/userguide/planning.md")<br>• [Create a Build Project](../../../codebuild/latest/userguide/create-project.md#create-project-console "../../../codebuild/latest/userguide/create-project.md#create-project-console")<br>• [Use CodePipeline with<br>AWS CodeBuild to Run Builds](../../../codebuild/latest/userguide/how-to-create-pipeline.md "../../../codebuild/latest/userguide/how-to-create-pipeline.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Amazon CodeGuru Reviewer**           | Amazon CodeGuru Reviewer is an automated code review service that uses program analysis<br>and machine learning to detect common issues and recommend fixes in your Java or<br>Python code. You can associate repositories in your Amazon Web Services account with CodeGuru Reviewer.<br>When you do, CodeGuru Reviewer creates a service-linked role that allows CodeGuru Reviewer to analyze code<br>in all pull requests created after the association is made. Learn more:<br>• [Associate or disassociate an AWS CodeCommit<br>repository with Amazon CodeGuru Reviewer](how-to-amazon-codeguru-reviewer.md "how-to-amazon-codeguru-reviewer.md")<br>• [Amazon CodeGuru Reviewer User Guide](../../../codeguru/latest/reviewer-ug/welcome.md "../../../codeguru/latest/reviewer-ug/welcome.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **AWS CodePipeline**                   | [CodePipeline](../../../codepipeline/latest/userguide.md "../../../codepipeline/latest/userguide.md") is a continuous delivery service you<br>can use to model, visualize, and automate the steps required to release your<br>software. You can configure CodePipeline to use a CodeCommit repository as a source action in a<br>pipeline, and automate building, testing, and deploying your changes.<br>Learn more:<br>• [Simple Pipeline<br>Walkthrough with CodePipeline and AWS CodeCommit](../../../codepipeline/latest/userguide/getting-started-cc.md "../../../codepipeline/latest/userguide/getting-started-cc.md")<br>• [Migrate to Amazon CloudWatch Events Change Detection for Pipelines with a CodeCommit<br>Repository](../../../codepipeline/latest/userguide/triggering.md#trigger-codecommit-migration-cwe "../../../codepipeline/latest/userguide/triggering.md#trigger-codecommit-migration-cwe")<br>• [Change-Detection Methods Used to Start Pipelines Automatically](../../../codepipeline/latest/userguide/pipelines-about-starting.md#change-detection-methods "../../../codepipeline/latest/userguide/pipelines-about-starting.md#change-detection-methods")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **AWS Elastic Beanstalk**              | [Elastic Beanstalk](../../../elasticbeanstalk/latest/dg.md "../../../elasticbeanstalk/latest/dg.md") is a managed service that makes it easy<br>to deploy and manage applications in the AWS cloud without worrying about the<br>infrastructure that runs those applications. You can use the Elastic Beanstalk command line<br>interface (EB CLI) to deploy your application directly from a new or existing CodeCommit<br>repository.<br>Learn more:<br>• [Using the EB CLI with<br>AWS CodeCommit](../../../elasticbeanstalk/latest/dg/eb-cli-codecommit.md "../../../elasticbeanstalk/latest/dg/eb-cli-codecommit.md")<br>• [Using an Existing AWS CodeCommit Repository](../../../elasticbeanstalk/latest/dg/eb-cli-codecommit.md#eb-cli-codecommit-existing "../../../elasticbeanstalk/latest/dg/eb-cli-codecommit.md#eb-cli-codecommit-existing")<br>• [eb codesource (EB CLI<br>command)](../../../elasticbeanstalk/latest/dg/eb3-codesource.md "../../../elasticbeanstalk/latest/dg/eb3-codesource.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **AWS Key Management Service**         | [AWS KMS](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md") is a managed service that makes it easy<br>for you to create and control the encryption keys used to encrypt your data. By<br>default, CodeCommit uses AWS KMS to encrypt repositories.<br>Learn more:<br>• [AWS KMS and encryption](encryption.md "encryption.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **AWS Lambda**                         | [Lambda](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md") lets you run code without provisioning<br>or managing servers. You can configure triggers for CodeCommit repositories that invoke<br>Lambda functions in response to repository events.<br>Learn more:<br>• [Create a trigger for a Lambda function](how-to-notify-lambda.md "how-to-notify-lambda.md")<br>• [AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Amazon Simple Notification Service** | [Amazon SNS](../../../sns/latest/dg.md "../../../sns/latest/dg.md") is a web service that enables<br>applications, end users, and devices to instantly send and receive notifications<br>from the cloud. You can configure triggers for CodeCommit repositories that send Amazon SNS<br>notifications in response to repository events.<br>You can also use Amazon SNS notifications to<br>integrate with other AWS services. For example, you can use an Amazon SNS notification<br>to send messages to an Amazon Simple Queue Service queue.<br>Learn more:<br>• [Create a trigger for an Amazon SNS topic](how-to-notify-sns.md "how-to-notify-sns.md")<br>• [Amazon Simple Notification Service Developer<br>Guide](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Integration examples from the community

The following sections provide links to blog posts, articles, and community-provided
examples.

###### Note

These links are provided for informational purposes only, and should not be considered
either a comprehensive list or an endorsement of the content of the examples. AWS is not
responsible for the content or accuracy of external content.

###### Topics

- [Blog posts](#integrations-community-blogposts "#integrations-community-blogposts")
- [Code samples](#integrations-community-code "#integrations-community-code")

### Blog posts

- **[Integrating SonarQube as a Pull Request Approver on
  AWS CodeCommit](https://aws.amazon.com/blogs/devops/integrating-sonarqube-as-a-pull-request-approver-on-aws-codecommit/ "https://aws.amazon.com/blogs/devops/integrating-sonarqube-as-a-pull-request-approver-on-aws-codecommit/")**

Learn how to create a CodeCommit repository that requires a successful SonarQube quality
analysis before pull requests can be merged.

Published December 12, 2019

- **[Migration to AWS CodeCommit, AWS CodePipeline, and AWS CodeBuild From
  GitLab](https://aws.amazon.com/blogs/devops/migration-to-aws-codecommit-aws-codepipeline-and-aws-codebuild-from-gitlab/ "https://aws.amazon.com/blogs/devops/migration-to-aws-codecommit-aws-codepipeline-and-aws-codebuild-from-gitlab/")**

Learn how to migrate multiple repositories to AWS CodeCommit from GitLab and set up a
CI/CD pipeline using AWS CodePipeline and AWS CodeBuild.

Published November 22, 2019

- **[Implementing GitFlow Using AWS CodePipeline, AWS CodeCommit, AWS CodeBuild, and
  AWS CodeDeploy](https://aws.amazon.com/blogs/devops/implementing-gitflow-using-aws-codepipeline-aws-codecommit-aws-codebuild-and-aws-codedeploy/ "https://aws.amazon.com/blogs/devops/implementing-gitflow-using-aws-codepipeline-aws-codecommit-aws-codebuild-and-aws-codedeploy/")**

Learn how to implement GitFlow using AWS CodePipeline, AWS CodeCommit, AWS CodeBuild, and
AWS CodeDeploy.

Published February 22, 2019

- **[Using Git with AWS CodeCommit Across Multiple AWS Accounts](https://aws.amazon.com/blogs/devops/using-git-with-aws-codecommit-across-multiple-aws-accounts/ "https://aws.amazon.com/blogs/devops/using-git-with-aws-codecommit-across-multiple-aws-accounts/")**

Learn how to manage your Git configuration across multiple Amazon Web Services
accounts.

Published February 12, 2019

- **[Validating AWS CodeCommit Pull Requests with AWS CodeBuildand
  AWS Lambda](https://aws.amazon.com/blogs/devops/validating-aws-codecommit-pull-requests-with-aws-codebuild-and-aws-lambda/ "https://aws.amazon.com/blogs/devops/validating-aws-codecommit-pull-requests-with-aws-codebuild-and-aws-lambda/")**

Learn how to validate pull requests with AWS CodeCommit, AWS CodeBuild, and AWS Lambda. By
running tests against the proposed changes prior to merging them into the default
branch, you can help ensure a high level of quality in pull requests, catch any
potential issues, and boost the confidence of the developer in relation to their
changes.

Published February 11, 2019

- **[Using Federated Identities with AWS CodeCommit](https://aws.amazon.com/blogs/devops/using-federated-identities-with-aws-codecommit/ "https://aws.amazon.com/blogs/devops/using-federated-identities-with-aws-codecommit/")**

Learn how to access repositories in AWS CodeCommit using the identities used in your
business.

Published October 5, 2018

- **[Refining Access to Branches in AWS CodeCommit](https://aws.amazon.com/blogs/devops/refining-access-to-branches-in-aws-codecommit/ "https://aws.amazon.com/blogs/devops/refining-access-to-branches-in-aws-codecommit/")**

Learn how to restrict commits to repository branches by creating and applying an
IAM policy that uses a context key.

Published May 16, 2018

- **[Replicate AWS CodeCommit Repositories Between Regions Using AWS
  Fargate](https://aws.amazon.com/blogs/devops/replicate-aws-codecommit-repository-between-regions-using-aws-fargate/ "https://aws.amazon.com/blogs/devops/replicate-aws-codecommit-repository-between-regions-using-aws-fargate/")**

Learn how to set up continuous replication of a CodeCommit repository from one AWS
region to another using a serverless architecture.

Published April 11, 2018

- **[Distributing Your AWS OpsWorks for Chef Automate Infrastructure](https://aws.amazon.com/blogs/mt/distributing-your-aws-opsworks-for-chef-automate-infrastructure/ "https://aws.amazon.com/blogs/mt/distributing-your-aws-opsworks-for-chef-automate-infrastructure/")**

Learn how to use CodePipeline, CodeCommit, CodeBuild, and AWS Lambda to ensure that cookbooks and
other configurations are consistently deployed across two or more Chef Servers residing
in one or more AWS Regions.

Published March 9, 2018

- **[Peanut Butter and Chocolate: Azure Functions CI/CD Pipeline with
  AWS CodeCommit](https://get-powershellblog.blogspot.com/2018/02/peanut-butter-and-chocolate-azure.html "https://get-powershellblog.blogspot.com/2018/02/peanut-butter-and-chocolate-azure.html")**

Learn how to create a PowerShell-based Azure Functions CI/CD pipeline where the code
is stored in a CodeCommit repository.

Published February 19, 2018

- **[Continuous Deployment to Kubernetes Using AWS CodePipeline, AWS CodeCommit, AWS CodeBuild, Amazon ECR,
  and AWS Lambda](https://aws.amazon.com/blogs/devops/continuous-deployment-to-kubernetes-using-aws-codepipeline-aws-codecommit-aws-codebuild-amazon-ecr-and-aws-lambda/ "https://aws.amazon.com/blogs/devops/continuous-deployment-to-kubernetes-using-aws-codepipeline-aws-codecommit-aws-codebuild-amazon-ecr-and-aws-lambda/")**

Learn how to use Kubernetes and AWS together to create a fully managed, continuous
deployment pipeline for container based applications.

Published January 11, 2018

- **[Use AWS CodeCommit Pull Requests to Request Code Reviews and Discuss
  Code](https://aws.amazon.com/blogs/devops/using-aws-codecommit-pull-requests-to-request-code-reviews-and-discuss-code/ "https://aws.amazon.com/blogs/devops/using-aws-codecommit-pull-requests-to-request-code-reviews-and-discuss-code/")**

Learn how to use pull requests to review, comment upon, and interactively iterate on
code changes in a CodeCommit repository.

Published November 20, 2017

- **[Build Serverless AWS CodeCommit Workflows Using Amazon CloudWatch Events and
  JGit](https://aws.amazon.com/blogs/devops/build-serverless-aws-codecommit-workflows-using-amazon-cloudwatch-events-and-jgit/ "https://aws.amazon.com/blogs/devops/build-serverless-aws-codecommit-workflows-using-amazon-cloudwatch-events-and-jgit/")**

Learn how to create CloudWatch Events rules that process changes in a repository using CodeCommit
repository events and target actions in other AWS services. Examples include AWS Lambda
functions that enforce Git commit message policies on commits, replicate a CodeCommit
repository, and backing up a CodeCommit repository to Amazon S3.

Published August 3, 2017

- **[Migrating
  to AWS CodeCommit](https://romikoderbynew.com/2016/09/06/migrating-to-aws-codecommit/ "https://romikoderbynew.com/2016/09/06/migrating-to-aws-codecommit/")**

Learn how to push code to two repositories as part of migrating from using another
Git repository to CodeCommit when using SourceTree.

Published September 6, 2016

- **[Set Up Continuous Testing with Appium, AWS CodeCommit, Jenkins, and
  AWS Device Farm](https://aws.amazon.com/blogs/mobile/set-up-continuous-testing-with-appium-aws-codecommit-jenkins-and-aws-device-farm/ "https://aws.amazon.com/blogs/mobile/set-up-continuous-testing-with-appium-aws-codecommit-jenkins-and-aws-device-farm/")**

Learn how to create a continuous testing process for mobile devices using Appium,
CodeCommit, Jenkins, and Device Farm.

Published February 2, 2016

- **[Using AWS CodeCommit with Git
  Repositories in Multiple Amazon Web Services accounts](https://alestic.com/2015/11/aws-codecommit-iam-role/ "https://alestic.com/2015/11/aws-codecommit-iam-role/")**

Learn how to clone your CodeCommit repository and, in one command, configure the
credential helper to use a specific IAM role for connections to that
repository.

Published November 2015

- **[Integrating OpsWorks and AWS CodeCommit](https://aws.amazon.com/blogs/devops/integrating-aws-opsworks-and-aws-codecommit/ "https://aws.amazon.com/blogs/devops/integrating-aws-opsworks-and-aws-codecommit/")**

Learn how OpsWorks can automatically fetch Apps and Chef cookbooks from CodeCommit.

Published August 25, 2015

- **[Using
  AWS CodeCommit and GitHub Credential Helpers](http://jameswing.net/aws/using-codecommit-and-git-credentials.html "http://jameswing.net/aws/using-codecommit-and-git-credentials.html")**

Learn how to configure your gitconfig file to work with both CodeCommit and GitHub
credential helpers.

Published September 2015

- **[Using AWS CodeCommit from Eclipse](https://java.awsblog.com/post/Tx579PWM8RIYV5/Using-AWS-CodeCommit-from-Eclipse "https://java.awsblog.com/post/Tx579PWM8RIYV5/Using-AWS-CodeCommit-from-Eclipse")**

Learn how to use the EGit tools in Eclipse to work with CodeCommit.

Published August 2015

- **[AWS CodeCommit
  with Amazon EC2 Role Credentials](http://jameswing.net/aws/codecommit-with-ec2-role-credentials.html "http://jameswing.net/aws/codecommit-with-ec2-role-credentials.html")**

Learn how to use an instance profile for Amazon EC2 when configuring automated agent
access to a CodeCommit repository.

Published July 2015

- **[Integrating AWS CodeCommit with Jenkins](https://blogs.aws.amazon.com/application-management/post/Tx1C8B98XN0AF2E/Integrating-AWS-CodeCommit-with-Jenkins "https://blogs.aws.amazon.com/application-management/post/Tx1C8B98XN0AF2E/Integrating-AWS-CodeCommit-with-Jenkins")**

Learn how to use CodeCommit and Jenkins to support two simple continuous integration (CI)
scenarios.

Published July 2015

- **[Integrating AWS CodeCommit with Review Board](https://blogs.aws.amazon.com/application-management/post/Tx35O95VQF5I0AT/Integrating-AWS-CodeCommit-with-Review-Board "https://blogs.aws.amazon.com/application-management/post/Tx35O95VQF5I0AT/Integrating-AWS-CodeCommit-with-Review-Board")**

Learn how to integrate CodeCommit into a development workflow using the [Review Board](https://www.reviewboard.org/ "https://www.reviewboard.org/") code review system.

Published July 2015

### Code samples

The following are code samples that might be of interest to CodeCommit users.

- **[Mac OS X Script to
  Periodically Delete Cached Credentials in the OS X Certificate
  Store](https://github.com/nicc777/macaws-codecommit-pwdel "https://github.com/nicc777/macaws-codecommit-pwdel")**

If you use the credential helper for CodeCommit on Mac OS X, you are likely familiar with
the problem with cached credentials. This script demonstrate one solution.

**Author:** Nico Coetzee

Published February 2016
