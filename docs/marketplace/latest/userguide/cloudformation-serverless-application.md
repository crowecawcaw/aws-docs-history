# Adding serverless application

components

###### Important

AWS Marketplace no longer supports publishing new products with CloudFormation templates that deploy
resources from AWS Serverless Application Repository. Sellers can continue to publish existing products with CloudFormation
templates that deploy resources from AWS Serverless Application Repository until a future date to be announced.

You can create a product that includes an Amazon Machine Image (AMI), delivered
using a AWS CloudFormation template, with serverless components incorporated into the product.
For example, you can create a product with an AMI configured as a controller server and deliver it as a AWS CloudFormation stack.
The AWS CloudFormation template used to create the stack can include the definition to set up an AWS Lambda function that is triggered by an event
in the server. When you use this approach to design your product, you can simplify the architecture and
make it easier for your buyers to launch. This approach can also make it easier for you to
update your product. Thes following sections show you how to create and offer this type of product.

For information about creating an AMI for your product, see [AMI-based products in AWS Marketplace](ami-products.md "ami-products.md"). For information about completing AWS CloudFormation templates for your
product, see [Add CloudFormation templates to your product](cloudformation.md "cloudformation.md").

When you define your serverless application, you use an AWS Serverless Application Model (AWS SAM) template that you
store in the AWS Serverless Application Repository. AWS SAM is an open-source framework for building serverless applications.
During deployment, AWS SAM transforms and expands the AWS Serverless Application Model syntax into AWS CloudFormation syntax. The
AWS Serverless Application Repository is a managed repository for serverless applications. It makes it possible for you to store
and share reusable applications so buyers can assemble and deploy serverless architectures.

###### Note

- AWS Marketplace reviews and validates your product before your listing is created. If there are issues
  you must resolve before the offer is listed, we will send you an email message.
- As part of fulfilling a subscription, we copy the AMIs, serverless applications, and AWS CloudFormation
  templates to an AWS Marketplace-owned repository in each AWS Region. When a buyer subscribes to your
  product, we give them access, and also notify them when you update your software.

###### Topics

- [Step 1: Create a serverless
  application](#cloudformation-serverless-application-procedure-step-1 "#cloudformation-serverless-application-procedure-step-1")
- [Step 2: Publish your
  application to the repository](#cloudformation-serverless-application-procedure-step-2 "#cloudformation-serverless-application-procedure-step-2")
- [Step 3: Create the CloudFormation
  template](#cloudformation-serverless-application-procedure-step-3 "#cloudformation-serverless-application-procedure-step-3")
- [Step 4: Submit your
  CloudFormation template and configuration files](#cloudformation-serverless-application-procedure-step-4 "#cloudformation-serverless-application-procedure-step-4")
- [Step 5: Update your AWS Serverless Application Repository
  application permissions](#cloudformation-serverless-application-procedure-step-5 "#cloudformation-serverless-application-procedure-step-5")
- [Step 6: Share your
  AMI](#cloudformation-serverless-application-procedure-step-6 "#cloudformation-serverless-application-procedure-step-6")
- [Step 7: Submit your
  CloudFormation product with AMI and serverless application](#cloudformation-serverless-application-procedure-step-7 "#cloudformation-serverless-application-procedure-step-7")

## Step 1: Create a serverless

application

Your first step is to package the AWS Lambda functions used to create your serverless
application. Your application is a combination of Lambda functions, event sources, and other
resources that work together to perform tasks. A serverless application can be as simple as
one Lambda function, or it can contain multiple functions with other resources, such as APIs,
databases, and event source mappings.

Use the AWS SAM to define a model for your serverless application. For descriptions of
property names and types, see [AWS::Serverless::Application](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication "https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication") in AWSLabs on GitHub. The following is an example of
an AWS SAM template with a single Lambda function and AWS Identity and Access Management (IAM) role.

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
      CodeUri: 's3://amzn-s3-demo-bucket/`2EXAMPLE-1234-4b12-ac37-515EXAMPLEe5-lambda.zip`'
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

## Step 2: Publish your

application to the repository

To publish an application, you first upload the application code. Store your code
artifacts (for example, Lambda functions, scripts, configuration files) in an Amazon S3 bucket that
your account owns. When you upload your application, it's initially set to private, meaning
that it's only available to the AWS account that created it. You must create an IAM
policy that grants AWS Serverless Application Repository permissions to access the artifacts you uploaded.

###### To publish your serverless application to the serverless application repository

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the Amazon S3 bucket that you used to package your application.
3. Choose the **Permissions** tab.
4. Choose **Bucket Policy**.
5. Copy and paste the following example policy statement.

###### Note

The example policy statement will produce an error until values for `aws:SourceAccount` and
`Resource` are updated in following steps.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "serverlessrepo.amazonaws.com"
 },
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "Condition" : {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

    1. Replace amzn-s3-demo-bucket in the `Resource` property value with the
     bucket name for your bucket.
    2. Replace `123456789012` in the `Condition`
     element with your AWS account ID. The `Condition` element ensures that
     the AWS Serverless Application Repository only has permission to access applications from the specified
     AWS account.

6. Choose **Save**.
7. Open the AWS Serverless Application Repository console at [https://console.aws.amazon.com/serverlessrepo](https://console.aws.amazon.com/serverlessrepo "https://console.aws.amazon.com/serverlessrepo").
8. On the **My Applications** page, choose **Publish
   application**.
9. Complete the required fields and any optional field, as appropriate. The required
   fields are:
   - **Application name**
   - **Author**
   - **Description**
   - **Source code URL**
   - **SAM template**

10. Choose **Publish Application**.

###### To publish subsequent versions of your application

1. Open the AWS Serverless Application Repository console at [https://console.aws.amazon.com/serverlessrepo](https://console.aws.amazon.com/serverlessrepo "https://console.aws.amazon.com/serverlessrepo").
2. In the navigation pane, from **My Applications**, choose the
   application.
3. Choose **Publish new version**.

For more information, see [Publishing
serverless Applications Using the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md").

## Step 3: Create the CloudFormation

template

To build your CloudFormation templates, you must meet the template prerequisites and provide
the required input and security parameters. For more information, see [Template anatomy](../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md "../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md") in the
_AWS CloudFormation User Guide_.

In your CloudFormation template, you can reference your serverless application and your AMI.
You can also use nested CloudFormation templates and reference serverless applications both in the
root template and the nested templates. To reference the serverless application, you use the
AWS SAM template. You can automatically generate the AWS SAM template for your application from
the AWS Serverless Application Repository. The following is an example template.

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

- `ApplicationID` – Your application's Amazon Resource Name (ARN). This
  information is located in the **My Applications** section of the
  AWS Serverless Application Repository.
- `SemanticVersion` – The version of your serverless application. You can
  find this from the **My Applications** section of the AWS Serverless Application Repository.
- `Parameter` (optional) – Application parameters.

###### Note

For `ApplicationID` and `SemanticVersion`, [intrinsic
functions](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md") aren't supported. You must hardcode those strings. The
`ApplicationID` is updated when it's cloned by AWS Marketplace.

If you're planning to reference configuration and script files in your CloudFormation
template, use the following format. For nested templates
(`AWS::Cloudformation::Stack`), only `TemplateURLs` without intrinsic
functions are supported. Note the `Parameters` content in the template.

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
                - https://${CFTRefFilesBucket}.${S3Region}amazonaws.com/${CFTRefFilesBucketKeyPrefix}/`sampleScript.sh`
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

## Step 4: Submit your

CloudFormation template and configuration files

To submit your CloudFormation template and configuration and scripts files, grant AWS Marketplace
permissions to read the Amazon S3 bucket where these files are stored. To do so, update your bucket
policy to include the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "assets.marketplace.amazonaws.com"
 },
 "Action": ["s3:GetObject", "s3:ListBucket"],
 "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"]
 }
 ]
}`

```

## Step 5: Update your AWS Serverless Application Repository

application permissions

To submit your AWS Serverless Application Repository application to AWS Marketplace, you must grant AWS Marketplace permissions to read your
application. To do that, add permissions to a policy associated with your serverless
application. There are two ways to update your application policy:

- Go to the [AWS
  Serverless Application Repository](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home"). Choose your serverless application from the
  list. Select the **Sharing** tab, and choose **Create
  Statement**. On the **Statement configuration** page, enter
  the following service principal, `assets.marketplace.amazonaws.com`,
  in the **Account Ids** field. Then choose
  **Save**.
- Use the following AWS CLI command to update your application policy.

```
aws serverlessrepo put-application-policy \
--region `region` \
--application-id `application-arn` \
--statements Principals=assets.marketplace.amazonaws.com,Actions=Deploy
```

## Step 6: Share your

AMI

All AMIs built and submitted to AWS Marketplace must adhere to all product policies. Self-service
AMI scanning is available in the AWS Marketplace Management Portal. With this feature, you can initiate scans of your
AMIs. You receive scanning results quickly (typically, in less than an hour) with clear
feedback in a single location. After your AMI has been successfully scanned, submit the AMI
for processing by the AWS Marketplace Seller Operations team by uploading your product load form.

## Step 7: Submit your

CloudFormation product with AMI and serverless application

Keep the following in mind before you submit your product:

- You must provide an architectural diagram for each template. The diagram must use the AWS
  product icons for each AWS service deployed through the CloudFormation template. Also, the
  diagram must include metadata for the services. To download our official AWS
  architecture icons, see [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons").
- The infrastructure cost estimate for each template displayed to buyers is based on an
  estimate that you provide by using the [AWS Pricing Calculator](https://calculator.s3.amazonaws.com/index.html "https://calculator.s3.amazonaws.com/index.html").
  In the estimate, include the list of services to be deployed as part of the template,
  along with the default values for a typical deployment.
- Complete the product load form. You can find the product load form from the AWS Marketplace Management Portal.
  A different product load form is required for single AMI products and multiple AMI
  products. In the product load form, you will provide a public URL to your CloudFormation
  template. CloudFormation templates must be submitted in the form of a public URL.
- Use the AWS Marketplace Management Portal to submit your listing. From **Assets**, choose
  **File upload**, attach your file, and then choose
  **Upload**. After we receive your template and metadata, AWS starts
  processing your request.

After you submit your listing, AWS Marketplace reviews and validates the product load form.
Additionally, AWS Marketplace regionalizes AMIs and serverless applications, and updates the regional
mapping for your AWS CloudFormation template on your behalf. If any issues occur, the AWS Marketplace Seller Operations team will
contact you by email.
