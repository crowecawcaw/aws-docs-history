

# Using CloudFormation to Create a Lambda Function to Use in Neptune
<a name="get-started-cfn-lambda"></a>

You can use an CloudFormation template to create an AWS Lambda function that can access Neptune.

1. To launch the Lambda function stack on the CloudFormation console, choose one of the **Launch Stack** buttons in the following table.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/neptune/latest/userguide/get-started-cfn-lambda.html)

1.  On the **Select Template** page, choose **Next**.

1. On the **Specify Details** page, set the following options:

   1. Choose the Lambda runtime, depending on what language you want to use in your Lambda function. These CloudFormation templates currently support the following languages:
      + **Python 3.9** (maps to `python39` in the Amazon S3 URL)
      + **NodeJS 18** (maps to `nodejs18x` in the Amazon S3 URL)
      + **Ruby 2.5** (maps to `ruby25` in the Amazon S3 URL)

   1. Provide the appropriate Neptune cluster endpoint and port number.

   1. Provide the appropriate Neptune security group.

   1. Provide the appropriate Neptune subnet parameters.

1. Choose **Next**.

1. On the **Options** page, choose **Next**.

1. On the **Review** page, select the first check box to acknowledge that CloudFormation will create IAM resources.

   Then choose **Create**.

If you need to make your own changes to the Lambda runtime, you can download a generic one from an Amazon S3 location in your Region:

```
https://s3.{{Amazon region}}.amazonaws.com/aws-neptune-customer-samples-{{Amazon region}}/lambda/{{runtime-language}}/lambda_function.zip.
```

For example:

```
https://s3.us-west-2.amazonaws.com/aws-neptune-customer-samples-us-west-2/lambda/python36/lambda_function.zip
```