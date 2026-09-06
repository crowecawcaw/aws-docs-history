

# Reuse code and resources using nested applications in AWS SAM
<a name="serverless-sam-template-nested-applications"></a>

A serverless application can include one or more **nested applications**. A nested application is a part of a larger application and can be packaged and deployed either as a stand-alone artifact or as a component of the larger application. Nested applications allow you to turn frequently used code and into its own application that can then be reused across a larger serverless application or multiple serverless applications.

As your serverless architectures grows, common patterns typically emerge in which the same components are defined in multiple application templates. Nested applications allow you to reuse common code, functionality, resources, and configurations in separate AWS SAM templates, allowing you to only maintain code from a single source. This reduces duplicated code and configurations. Additionally, this modular approach streamlines development, enhances code organization, and facilitates consistency across serverless applications. With nested applications, you can stay more focused on the business logic that's unique to your application.

To define a nested application in your serverless application, use the [AWS::Serverless::Application](sam-resource-application.md) resource type.

You can define nested applications from the following two sources:
+ An **AWS Serverless Application Repository application** – You can define nested applications by using applications that are available to your account in the AWS Serverless Application Repository. These can be *private* applications in your account, applications that are *privately shared* with your account, or applications that are *publicly shared* in the AWS Serverless Application Repository. For more information about the different deployment permissions levels, see [Application Deployment Permissions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverless-app-consuming-applications.html#application-deployment-permissions) and [Publishing Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverless-app-publishing-applications.html) in the *AWS Serverless Application Repository Developer Guide*.
+ A **local application** – You can define nested applications by using applications that are stored on your local file system.

See the following sections for details on how to use AWS SAM to define both of these types of nested applications in your serverless application.

**Note**  
The maximum number of applications that can be nested in a serverless application is 200.  
The maximum number of parameters a nested application can have is 60.

## Defining a nested application from the AWS Serverless Application Repository
<a name="serverless-sam-template-nested-applications-how-to-serverlessrepo"></a>

You can define nested applications by using applications that are available in the AWS Serverless Application Repository. You can also store and distribute applications that contain nested applications using the AWS Serverless Application Repository. To review details of a nested application in the AWS Serverless Application Repository, you can use the AWS SDK, the AWS CLI, or the Lambda console.

To define an application that's hosted in the AWS Serverless Application Repository in your serverless application's AWS SAM template, use the **Copy as SAM Resource** button on the detail page of every AWS Serverless Application Repository application. To do this, follow these steps:

1. Make sure that you're signed in to the AWS Management Console.

1. Find the application that you want to nest in the AWS Serverless Application Repository by using the steps in the [Browsing, Searching, and Deploying Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverless-app-consuming-applications.html#browse-and-search-applications                         ) section of the *AWS Serverless Application Repository Developer Guide*.

1. Choose the **Copy as SAM Resource** button. The SAM template section for the application that you're viewing is now in your clipboard.

1. Paste the SAM template section into the `Resources:` section of the SAM template file for the application that you want to nest in this application.

The following is an example SAM template section for a nested application that's hosted in the AWS Serverless Application Repository:

```
Transform: AWS::Serverless-2016-10-31

Resources:
  {{applicationaliasname}}:
    Type: AWS::Serverless::Application
    Properties:
      Location:
        ApplicationId: arn:aws:serverlessrepo:{{us-east-1}}:{{123456789012}}:applications/{{application-alias-name}}
        SemanticVersion: 1.0.0
      Parameters:
        # Optional parameter that can have default value overridden
        {{# ParameterName1: 15 # Uncomment to override default value}}
        # Required parameter that needs value to be provided
        {{ParameterName2: YOUR_VALUE}}
```

If there are no required parameter settings, you can omit the `Parameters:` section of the template.

**Important**  
Applications that contain nested applications hosted in the AWS Serverless Application Repository inherit the nested applications' sharing restrictions.   
For example, suppose an application is publicly shared, but it contains a nested application that's only privately shared with the AWS account that created the parent application. In this case, if your AWS account doesn't have permission to deploy the nested application, you aren't able to deploy the parent application. For more information about permissions to deploy applications, see [Application Deployment Permissions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverless-app-consuming-applications.html#application-deployment-permissions) and [Publishing Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverless-app-publishing-applications.html) in the *AWS Serverless Application Repository Developer Guide*.

## Defining a nested application from the local file system
<a name="serverless-sam-template-nested-applications-how-to-local-app"></a>

You can define nested applications by using applications that are stored on your local file system. You do this by specifying the path to the AWS SAM template file that's stored on your local file system.

The following is an example SAM template section for a nested local application:

```
Transform: AWS::Serverless-2016-10-31

Resources:
  {{applicationaliasname}}:
    Type: AWS::Serverless::Application
    Properties:
      Location: {{../my-other-app/template.yaml}}
      Parameters:
        # Optional parameter that can have default value overridden
        {{# ParameterName1: 15 # Uncomment to override default value}}
        # Required parameter that needs value to be provided
        {{ParameterName2: YOUR_VALUE}}
```

If there are no parameter settings, you can omit the `Parameters:` section of the template.

## Deploying nested applications
<a name="serverless-sam-templates-nested-applications-deploying"></a>

You can deploy your nested application by using the AWS SAM CLI command `sam deploy`. For more details, see [Deploy your application and resources with AWS SAM](serverless-deploying.md).

**Note**  
When you deploy an application that contains nested applications, you must acknowledge it contains nested applications. You do this by passing `CAPABILITY_AUTO_EXPAND` to the [CreateCloudFormationChangeSet API](https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateCloudFormationChangeSet),or using the [`aws serverlessrepo create-cloud-formation-change-set`](https://docs.aws.amazon.com/cli/latest/reference/serverlessrepo/create-cloud-formation-change-set.html) AWS CLI command.  
For more information about acknowledging nested applications, see [Acknowledging IAM Roles, Resource Policies, and Nested Applications when Deploying Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/acknowledging-application-capabilities.html) in the *AWS Serverless Application Repository Developer Guide*.