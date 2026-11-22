

# Adding serverless application components

**Important**  
AWS Marketplace no longer accepts CloudFormation templates that deploy resources from AWS Serverless Application Repository. You can't publish a new product or add a new version with one of these templates. To update an existing product, remove the serverless applications from its template first. For the steps, see [Step 7: Submit an update to your product](#cloudformation-serverless-application-procedure-step-7).

A product with serverless components delivers an Amazon Machine Image (AMI) with a AWS CloudFormation template that also deploys applications from AWS Serverless Application Repository. For example, the AMI runs a controller server, and the template sets up an AWS Lambda function that an event in the server triggers. The following sections describe how these products are built, and how to update one.

For information about creating an AMI for your product, see [AMI-based products in AWS Marketplace](ami-products.md). For information about completing AWS CloudFormation templates for your product, see [Add CloudFormation templates to your product](cloudformation.md). 

When you define your serverless application, you use an AWS Serverless Application Model (AWS SAM) template that you store in the AWS Serverless Application Repository. AWS SAM is an open-source framework for building serverless applications. During deployment, AWS SAM transforms and expands the AWS Serverless Application Model syntax into CloudFormation syntax. The AWS Serverless Application Repository is a managed repository for serverless applications. It makes it possible for you to store and share reusable applications so buyers can assemble and deploy serverless architectures. 

**Note**  
As part of fulfilling a subscription, we copy the AMIs, serverless applications, and CloudFormation templates to an AWS Marketplace-owned repository in each AWS Region. When a buyer subscribes to your product, we give them access, and also notify them when you update your software.

**Topics**
+ [Step 1: Create a serverless application](#cloudformation-serverless-application-procedure-step-1)
+ [Step 2: Publish your application to the repository](#cloudformation-serverless-application-procedure-step-2)
+ [Step 3: Create the CloudFormation template](#cloudformation-serverless-application-procedure-step-3)
+ [Step 4: Submit your CloudFormation template and configuration files](#cloudformation-serverless-application-procedure-step-4)
+ [Step 5: Update your AWS Serverless Application Repository application permissions](#cloudformation-serverless-application-procedure-step-5)
+ [Step 6: Share your AMI](#cloudformation-serverless-application-procedure-step-6)
+ [Step 7: Submit an update to your product](#cloudformation-serverless-application-procedure-step-7)

## Step 1: Create a serverless application
<a name="cloudformation-serverless-application-procedure-step-1"></a>

Your first step is to package the AWS Lambda functions used to create your serverless application. Your application is a combination of Lambda functions, event sources, and other resources that work together to perform tasks. A serverless application can be as simple as one Lambda function, or it can contain multiple functions with other resources, such as APIs, databases, and event source mappings.

Use the AWS SAM to define a model for your serverless application. For descriptions of property names and types, see [AWS::Serverless::Application](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication) in AWSLabs on GitHub. The following is an example of an AWS SAM template with a single Lambda function and AWS Identity and Access Management (IAM) role.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: An example of SAM template with Lambda function and IAM role

Resources:
  SampleFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: 'com.sampleproject.SampleHandler::handleRequest'
      Runtime: java8
      CodeUri: 's3://amzn-s3-demo-bucket/{{2EXAMPLE-1234-4b12-ac37-515EXAMPLEe5-lambda.zip}}'
      Description: Sample Lambda function
      Timeout: 120
      MemorySize: 1024
      Role:
        Fn::GetAtt: [SampleFunctionRole, Arn]

  # Role to execute the Lambda function
  SampleFunctionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action: "sts:AssumeRole"
      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
      Policies:
        - PolicyName: SFNXDeployWorkflowDefinitionPolicy
          PolicyDocument:
            Statement:
              - Effect: "Allow"
                Action:
                  - "s3:Get*"
                Resource: "*"
      RoleName: "SampleFunctionRole"
```

## Step 2: Publish your application to the repository
<a name="cloudformation-serverless-application-procedure-step-2"></a>

To publish an application, you first upload the application code. Store your code artifacts (for example, Lambda functions, scripts, configuration files) in an Amazon S3 bucket that your account owns. When you upload your application, it's initially set to private, meaning that it's only available to the AWS account that created it. You must create an IAM policy that grants AWS Serverless Application Repository permissions to access the artifacts you uploaded.

**To publish your serverless application to the serverless application repository**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose the Amazon S3 bucket that you used to package your application.

1. Choose the **Permissions** tab.

1. Choose **Bucket Policy**.

1. Copy and paste the following example policy statement. 
**Note**  
The example policy statement will produce an error until values for `aws:SourceAccount` and `Resource` are updated in following steps.

------
#### [ JSON ]

****  

   ```json
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service":  "serverlessrepo.amazonaws.com"
               },
               "Action": "s3:GetObject",
               "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
               "Condition" : {
                   "StringEquals": {
                       "aws:SourceAccount": "{{123456789012}}"
                   }
               }
           }
       ]
   }
   ```

------

   1. Replace amzn-s3-demo-bucket in the `Resource` property value with the bucket name for your bucket. 

   1. Replace {{123456789012}} in the `Condition` element with your AWS account ID. The `Condition` element ensures that the AWS Serverless Application Repository only has permission to access applications from the specified AWS account.

1. Choose **Save**.

1. Open the AWS Serverless Application Repository console at [https://console.aws.amazon.com/serverlessrepo](https://console.aws.amazon.com/serverlessrepo).

1. On the **My Applications** page, choose **Publish application**.

1. Complete the required fields and any optional field, as appropriate. The required fields are:
   +  **Application name** 
   +  **Author** 
   +  **Description** 
   +  **Source code URL** 
   +  **SAM template** 

1. Choose **Publish Application**. 

**To publish subsequent versions of your application**

1. Open the AWS Serverless Application Repository console at [https://console.aws.amazon.com/serverlessrepo](https://console.aws.amazon.com/serverlessrepo).

1. In the navigation pane, from **My Applications**, choose the application.

1. Choose **Publish new version**.

For more information, see [Publishing serverless Applications Using the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.html).

## Step 3: Create the CloudFormation template
<a name="cloudformation-serverless-application-procedure-step-3"></a>

To build your CloudFormation templates, you must meet the template prerequisites and provide the required input and security parameters. For more information, see [Template anatomy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html) in the *AWS CloudFormation User Guide*.

In your CloudFormation template, you can reference your serverless application and your AMI. You can also use nested CloudFormation templates and reference serverless applications both in the root template and the nested templates. To reference the serverless application, you use the AWS SAM template. You can automatically generate the AWS SAM template for your application from the AWS Serverless Application Repository. The following is an example template.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: An example root template for a SAR application

Resources:
  SampleSARApplication:
    Type: AWS::Serverless::Application
    Properties:
      Location:
         ApplicationId: arn:aws:serverlessrepo:us-east-1:1234567890:applications/TestApplication
         SemanticVersion: 1.0.0
  SampleEC2Instance:
    Type: AWS::EC2::Instance
      Properties: 
        ImageId: "ami-79fd7eee"
        KeyName: "testkey"
        BlockDeviceMappings: 
          - DeviceName: "/dev/sdm"
            Ebs: 
              VolumeType: "io1"
              Iops: "200"
              DeleteOnTermination: "false"
              VolumeSize: "20"
          - DeviceName: "/dev/sdk"
            NoDevice: {}
```

The AWS SAM template contains the following elements:
+  `ApplicationID` – Your application's Amazon Resource Name (ARN). This information is located in the **My Applications** section of the AWS Serverless Application Repository.
+  `SemanticVersion` – The version of your serverless application. You can find this from the **My Applications** section of the AWS Serverless Application Repository.
+  `Parameter` (optional) – Application parameters.

**Note**  
For `ApplicationID` and `SemanticVersion`, [intrinsic functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html) aren't supported. You must hardcode those strings. The `ApplicationID` is updated when it's cloned by AWS Marketplace.

If you're planning to reference configuration and script files in your CloudFormation template, use the following format. For nested templates (`AWS::Cloudformation::Stack`), only `TemplateURLs` without intrinsic functions are supported. Note the `Parameters` content in the template.

```
AWSTemplateFormatVersion: '2010-09-09'
Metadata:
  Name: Seller test product
Parameters:
  CFTRefFilesBucket:
    Type: String
    Default: "seller-bucket"
  CFTRefFilesBucketKeyPrefix:
    Type: String
    Default: "cftsolutionFolder/additionCFfiles"
Resources:
  TestEc2:
    Type: AWS::EC2::Instance
    Metadata:
      AWS::CloudFormation::Init:
        addCloudAccount:
          files:
            /etc/cfn/set-aia-settings.sh:
              source:
                Fn::Sub:
                - https://${CFTRefFilesBucket}.${S3Region}amazonaws.com/${CFTRefFilesBucketKeyPrefix}/{{sampleScript.sh}}
                - S3Region:
                    !If
                    - GovCloudCondition
                    - s3-us-gov-west-1
                    - s3
              owner: root
              mode: '000700'
              authentication: Amazon S3AccessCreds
    ..
    ..
    ..
  SampleNestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: 'https://sellerbucket.s3.amazon.com/sellerproductfolder/nestedCft.template'
      Parameters:
        SampleParameter: 'test'
Transform: AWS::Serverless-2016-10-31
```

## Step 4: Submit your CloudFormation template and configuration files
<a name="cloudformation-serverless-application-procedure-step-4"></a>

To submit your CloudFormation template and configuration and scripts files, grant AWS Marketplace permissions to read the Amazon S3 bucket where these files are stored. To do so, update your bucket policy to include the following permissions.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service":  "assets.marketplace.amazonaws.com"
            },
            "Action": ["s3:GetObject", "s3:ListBucket"],
            "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket",
                         "arn:aws:s3:::amzn-s3-demo-bucket/*"]
        }
    ]
}
```

------

## Step 5: Update your AWS Serverless Application Repository application permissions
<a name="cloudformation-serverless-application-procedure-step-5"></a>

To submit your AWS Serverless Application Repository application to AWS Marketplace, you must grant AWS Marketplace permissions to read your application. To do that, add permissions to a policy associated with your serverless application. There are two ways to update your application policy:
+ Go to the [AWS Serverless Application Repository](https://console.aws.amazon.com/serverlessrepo/home). Choose your serverless application from the list. Select the **Sharing** tab, and choose **Create Statement**. On the **Statement configuration** page, enter the following service principal, **assets.marketplace.amazonaws.com**, in the **Account Ids** field. Then choose **Save**.
+ Use the following AWS CLI command to update your application policy.

  ```
  aws serverlessrepo put-application-policy \
  --region {{region}} \
  --application-id {{application-arn}} \
  --statements Principals=assets.marketplace.amazonaws.com,Actions=Deploy
  ```

## Step 6: Share your AMI
<a name="cloudformation-serverless-application-procedure-step-6"></a>

All AMIs built and submitted to AWS Marketplace must adhere to all product policies. Self-service AMI scanning is available in AWS Partner Central. With this feature, you can initiate scans of your AMIs. You receive scanning results quickly (typically, in less than an hour) with clear feedback in a single location. For more information, see [Scanning your AMI for publishing requirements](best-practices-for-building-your-amis.md#self-service-scanning).

## Step 7: Submit an update to your product
<a name="cloudformation-serverless-application-procedure-step-7"></a>

**To submit an update to your product**

1. Remove the `AWS::Serverless::Application` resources from your CloudFormation template and from its nested templates.

1. Update the template to reference template parameters for the AMI ID and for nested template URLs.

   For the changes, see [Convert CloudFormation templates of existing products](cloudformation.md#convert-cloudformation-templates).

1. Upload the template and its architectural diagram to Amazon S3.

   For the diagram requirements, see [Architectural diagram](cloudformation.md#topology-diagram).

1. Add a new version with the **AMI with CloudFormation** delivery method.

   For instructions, see [Add a new version](single-ami-versions.md#single-ami-adding-version).