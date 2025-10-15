# Creating Object Lambda Access Points

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on November 7th, 2025. If you would like to use the service, please sign up prior to November 7th, 2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](amazons3-ol-change.md "amazons3-ol-change.md").

An Object Lambda Access Point is associated with exactly one standard access point, which you specify during creation. To
 create an Object Lambda Access Point, you need the following resources:


* **A standard S3 access point.** When you're working with
 Object Lambda Access Points, this standard access point is known as a *supporting
 access point* and is attached to an S3 bucket or Amazon FSx for OpenZFS volume. For
 information about creating standard access points, see [Creating an access point](creating-access-points.md "creating-access-points.md").
* **An AWS Lambda function.** You can either create your
 own Lambda function, or you can use a prebuilt function. For more information about
 creating Lambda functions, see [Writing Lambda functions for S3 Object Lambda Access Points](olap-writing-lambda.md "olap-writing-lambda.md"). For more
 information about prebuilt functions, see [Using AWS built Lambda functions](olap-examples.md "olap-examples.md").
* **(Optional) An AWS Identity and Access Management (IAM) policy.** Amazon S3 access points support
 IAM resource policies that you can use to control the use of the access point by resource,
 user, or other conditions. For more information about creating these policies, see
 [Configuring IAM policies for Object Lambda Access Points](olap-policies.md "olap-policies.md").
The following sections describe how to create an Object Lambda Access Point by using:


* The AWS Management Console
* The AWS Command Line Interface (AWS CLI)
* An AWS CloudFormation template
* The AWS Cloud Development Kit (AWS CDK)
For information about how to create an Object Lambda Access Point by using the REST API, see [`CreateAccessPointForObjectLambda`](../API/API_control_CreateAccessPointForObjectLambda.md "../API/API_control_CreateAccessPointForObjectLambda.md") in the *Amazon Simple Storage Service API Reference*.


## Create an Object Lambda Access Point


Use one of the following procedures to create your Object Lambda Access Point. 


###### To create an Object Lambda Access Point by using the console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to switch to.
3. In the left navigation pane, choose **Object Lambda Access Points**.
4. On the **Object Lambda Access Points** page, choose **Create
 Object Lambda Access Point**.
5. For **Object Lambda Access Point name**, enter the name that you want to use
 for the access point. 


As with standard access points, there are rules for naming Object Lambda Access Points. For more information,
 see [Naming rules for access points](access-points-restrictions-limitations-naming-rules.md#access-points-names "access-points-restrictions-limitations-naming-rules.md#access-points-names").
6. For **Supporting Access Point**, enter or browse to the standard
 access point that you want to use. The access point must be in the same AWS Region as the objects
 that you want to transform. For information about creating standard access points, see [Creating an access point](creating-access-points.md "creating-access-points.md").
7. Under **Transformation configuration**, you can add a function
 that transforms your data for your Object Lambda Access Point. Do one of the following:




	* If you already have a AWS Lambda function in your account you can choose it
	 under **Invoke Lambda function**. Here you may enter the
	 Amazon Resource Name (ARN) of an Lambda function in your AWS account or
	 choose a Lambda function from the drop-down menu.
	* If you wish to use a AWS built function choose the function name under
	 **AWS built function** and select **Create
	 Lambda function**. This will take you to the Lambda console where
	 you can deploy a built function into your AWS account. For more
	 information about built functions, see [Using AWS built Lambda functions](olap-examples.md "olap-examples.md").
Under **S3 APIs**, choose one or more API operations to invoke.
 For each API selected you must specify a Lambda function to invoke.
8. (Optional) Under **Payload**, add JSON text that you want to
 provide to your Lambda function as input. You can configure payloads with different
 parameters for different Object Lambda Access Points that invoke the same Lambda function, thereby
 extending the flexibility of your Lambda
 function.


###### Important

When you're using Object Lambda Access Points, make sure that the payload does not contain any
 confidential information.
9. (Optional) For **Range and part number**, you must enable this
 option if you want to process `GET` and `HEAD` requests with
 range and part number headers. Enabling this option confirms that your Lambda
 function can recognize and process these requests. For more information about range
 headers and part numbers, see [Working with Range and
 partNumber headers](range-get-olap.md "range-get-olap.md").
10. (Optional) For **Request metrics**, choose
 **Enable** or **Disable** to add Amazon S3
 monitoring to your Object Lambda Access Point. Request metrics are billed at the standard Amazon CloudWatch
 rate.
11. (Optional) Under **Object Lambda Access Point policy**, set a resource policy.
 Resource policies grant permissions for the specified Object Lambda Access Point and can control the use
 of the access point by resource, user, or other conditions. For more information about
 Object Lambda Access Point resource policies see, [Configuring IAM policies for Object Lambda Access Points](olap-policies.md "olap-policies.md").
12. Under **Block Public Access settings for this Object Lambda Access Point**, select the block
 public access settings that you want to apply. All block public
 access settings are enabled by default for new Object Lambda Access Points, and we recommend that
 you leave default settings enabled. Amazon S3 currently doesn't support changing an Object Lambda Access Point's block public
 access settings after the Object Lambda Access Points has been created.


For more information about using Amazon S3 Block Public Access, see
 [Managing public access to access points for general purpose buckets](access-points-bpa-settings.md "access-points-bpa-settings.md").
13. Choose **Create Object Lambda Access Point**.
###### To create an Object Lambda Access Point by using an AWS CloudFormation template

###### Note

To use the following commands, replace the ``user input
 placeholders`` with your own information.

1. Download the AWS Lambda function deployment package
 `s3objectlambda_deployment_package.zip` at [S3 Object Lambda default configuration](https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration "https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration").
2. Run the following `put-object` command to upload the package to an Amazon S3
 bucket.



```
aws s3api put-object --bucket `Amazon S3 bucket name` --key s3objectlambda_deployment_package.zip --body release/s3objectlambda_deployment_package.zip
```
3. Download the AWS CloudFormation template
 `s3objectlambda_defaultconfig.yaml` at [S3 Object Lambda default configuration](https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration "https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration").
4. Run the following `deploy` command to deploy the template to your
 AWS account.



```
aws cloudformation deploy --template-file s3objectlambda_defaultconfig.yaml \
 --stack-name `AWS CloudFormation stack name` \ 
 --parameter-overrides ObjectLambdaAccessPointName=`Object Lambda Access Point name` \
  SupportingAccessPointName=`Amazon S3 access point` S3BucketName=`Amazon S3 bucket` \
  LambdaFunctionS3BucketName=`Amazon S3 bucket containing your Lambda package` \ 
  LambdaFunctionS3Key=`Lambda object key` LambdaFunctionS3ObjectVersion=`Lambda object version` \ 
  LambdaFunctionRuntime=`Lambda function runtime` --capabilities `capability_IAM`
```
You can configure this AWS CloudFormation template to invoke Lambda for `GET`,
 `HEAD`, and `LIST` API operations. For more information about
 modifying the template's default configuration, see [Automate S3 Object Lambda setup with a CloudFormation
 template](olap-using-cfn-template.md "olap-using-cfn-template.md").

###### To create an Object Lambda Access Point by using the AWS CLI

###### Note

To use the following commands, replace the ``user input
 placeholders`` with your own information.

The following example creates an Object Lambda Access Point named
 ``my-object-lambda-ap`` for the bucket
 ``amzn-s3-demo-bucket1`` in the
 account ``111122223333``. This example
 assumes that a standard access point named ``example-ap``
 has already been created. For information about creating a standard access point, see [Creating an access point](creating-access-points.md "creating-access-points.md").

This example uses the AWS prebuilt function `decompress`. For more
 information about prebuilt functions, see [Using AWS built Lambda functions](olap-examples.md "olap-examples.md").

1. Create a bucket. In this example, we will use
 ``amzn-s3-demo-bucket1``.
 For information about creating buckets, see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md").
2. Create a standard access point and attach it to your bucket. In this example, we will use
 ``example-ap``. For information about
 creating standard access points, see [Creating an access point](creating-access-points.md "creating-access-points.md").
3. Do one of the following: 




	* Create a Lambda function in your account that you would like to use to
	 transform your Amazon S3 object. For more information about creating Lambda
	 functions, see [Writing Lambda functions for S3 Object Lambda Access Points](olap-writing-lambda.md "olap-writing-lambda.md"). To use your custom
	 function with the AWS CLI, see [Using Lambda with the
	 AWS CLI](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html "https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html") in the *AWS Lambda Developer Guide*.
	* Use an AWS prebuilt Lambda function. For more information about prebuilt
	 functions, see [Using AWS built Lambda functions](olap-examples.md "olap-examples.md").
4. Create a JSON configuration file named
 `my-olap-configuration.json`. In this configuration, provide
 the supporting access point and the Amazon Resource Name (ARN) for the Lambda function that
 you created in the previous steps or the ARN for the prebuilt function that you're
 using.



```
{
    "SupportingAccessPoint" : "arn:aws:s3:`us-east-1`:`111122223333`:accesspoint/`example-ap`",
    "TransformationConfigurations": [{
        "Actions" : ["GetObject", "HeadObject", "ListObjects", "ListObjectsV2"],
        "ContentTransformation" : {
            "AwsLambda": {
                "FunctionPayload" : "{\"compressionType\":\"gzip\"}",
                "FunctionArn" : "arn:aws:lambda:`us-east-1`:`111122223333`:function/compress"
            }
        }
    }]
}
```
5. Run the `create-access-point-for-object-lambda` command to create your
 Object Lambda Access Point.



```
aws s3control create-access-point-for-object-lambda --account-id `111122223333` --name `my-object-lambda-ap` --configuration file://`my-olap-configuration.json`
```
6. (Optional) Create a JSON policy file named
 `my-olap-policy.json`.


Adding an Object Lambda Access Point resource policy can control the use of the access point by
 resource, user, or other conditions. This resource policy grants the
 `GetObject` permission for account
 ``444455556666`` to the
 specified Object Lambda Access Point.



```
{
    "Version": "2008-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Grant account `444455556666` GetObject access",
            "Effect": "Allow",
            "Action": "s3-object-lambda:GetObject",
            "Principal": {
                "AWS": "arn:aws:iam::`444455556666`:root"
            },
            "Resource": "`your-object-lambda-access-point-arn`"
        }
    ]
}
```
7. (Optional) Run the `put-access-point-policy-for-object-lambda` command
 to set your resource policy.



```
aws s3control put-access-point-policy-for-object-lambda --account-id `111122223333` --name `my-object-lambda-ap` --policy file://`my-olap-policy.json`
```
8. (Optional) Specify a payload.


A payload is optional JSON that you can provide to your AWS Lambda function as
 input. You can configure payloads with different parameters for different Object Lambda Access Points
 that invoke the same Lambda function, thereby extending the flexibility of your Lambda
 function.


The following Object Lambda Access Point configuration shows a payload with two parameters.



```
{
	"SupportingAccessPoint": "`AccessPointArn`",
	"CloudWatchMetricsEnabled": `false`,
	"TransformationConfigurations": [{
		"Actions": ["GetObject", "HeadObject", "ListObjects", "ListObjectsV2"],
		"ContentTransformation": {
			"AwsLambda": {
				"FunctionArn": "`FunctionArn`",
				"FunctionPayload": "{\"res-x\": \"100\",\"res-y\": \"100\"}"
			}
		}
	}]
}
```

The following Object Lambda Access Point configuration shows a payload with one parameter, and with
 `GetObject-Range`, `GetObject-PartNumber`,
 `HeadObject-Range`, and `HeadObject-PartNumber`
 enabled.



```
{
    "SupportingAccessPoint":"`AccessPointArn`",
    "CloudWatchMetricsEnabled": `false`,
    "AllowedFeatures": ["GetObject-Range", "GetObject-PartNumber", "HeadObject-Range", "HeadObject-PartNumber"],        
    "TransformationConfigurations": [{
        "Action": ["GetObject", "HeadObject", "ListObjects", "ListObjectsV2"],
        "ContentTransformation": {
            "AwsLambda": {
                "FunctionArn":"`FunctionArn`",
                "FunctionPayload": "{\"compression-amount\": \"5\"}"
            }
        }
    }]
}
```

###### Important

When you're using Object Lambda Access Points, make sure that the payload does not contain any
 confidential information.
You can create an Object Lambda Access Point by using the default configuration provided by Amazon S3. You can
 download an AWS CloudFormation template and Lambda function source code from the [GitHub repository](https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration "https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration") and deploy these resources to set up a functional
 Object Lambda Access Point.

For information about modifying the AWS CloudFormation template's default configuration, see [Automate S3 Object Lambda setup with a CloudFormation
 template](olap-using-cfn-template.md "olap-using-cfn-template.md").

For information about configuring Object Lambda Access Points by using AWS CloudFormation without the template, see [`AWS::S3ObjectLambda::AccessPoint`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.md") in the
 *AWS CloudFormation User Guide*.

###### To upload the Lambda function deployment package

1. Download the AWS Lambda function deployment package
 `s3objectlambda_deployment_package.zip` at [S3 Object Lambda default configuration](https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration "https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration").
2. Upload the package to an Amazon S3 bucket.
###### To create an Object Lambda Access Point by using the AWS CloudFormation console

1. Download the AWS CloudFormation template
 `s3objectlambda_defaultconfig.yaml` at [S3 Object Lambda default configuration](https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration "https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration").
2. Sign in to the AWS Management Console and open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. Do one of the following: 




	* If you've never used AWS CloudFormation before, on the AWS CloudFormation home page, choose
	 **Create stack**.
	* If you have used AWS CloudFormation before, in the left navigation pane, choose
	 **Stacks**. Choose **Create stack**,
	 then choose **With new resources (standard)**.
4. For **Prerequisite - Prepare template**, choose **Template is ready**.
5. For **Specify template**, choose **Upload a template
 file** and upload
 `s3objectlambda_defaultconfig.yaml`.
6. Choose **Next**.
7. On the **Specify stack details** page, enter a name for the
 stack.
8. In the **Parameters** section, specify the following parameters
 that are defined in the stack
 template:


	1. For **CreateNewSupportingAccessPoint**, do one of the
	 following: 
	
	
	
	
		* If you already have a supporting access point for the S3 bucket
		 where you uploaded the template, choose
		 **false**.
		* If you want to create a new access point for this bucket, choose
		 **true**.
	2. For **EnableCloudWatchMonitoring**, choose
	 **true** or **false**, depending on
	 whether you want to enable Amazon CloudWatch request metrics and alarms.
	3. (Optional) For **LambdaFunctionPayload**, add JSON text
	 that you want to provide to your Lambda function as input. You can configure
	 payloads with different parameters for different Object Lambda Access Points that invoke the
	 same Lambda function, thereby extending the flexibility of your Lambda
	 function.
	
	
	###### Important
	
	When you're using Object Lambda Access Points, make sure that the payload does not contain
	 any confidential information.
	4. For **LambdaFunctionRuntime**, enter your preferred
	 runtime for the Lambda function. The available choices are
	 `nodejs14.x`, `python3.9`,
	 `java11`.
	5. For **LambdaFunctionS3BucketName**, enter the Amazon S3 bucket
	 name where you uploaded the deployment package.
	6. For **LambdaFunctionS3Key**, enter the Amazon S3 object key
	 where you uploaded the deployment package.
	7. For **LambdaFunctionS3ObjectVersion**, enter the Amazon S3
	 object version where you uploaded the deployment package.
	8. For **ObjectLambdaAccessPointName**, enter a name for
	 your Object Lambda Access Point.
	9. For **S3BucketName**, enter the Amazon S3 bucket name that
	 will be associated with your Object Lambda Access Point.
	10. For **SupportingAccessPointName**, enter the name of your
	 supporting access point.
	
	
	###### Note
	
	This is an access point that is associated with the Amazon S3 bucket that you chose
	 in the previous step. If you do not have any access points associated
	 with your Amazon S3 bucket, you can configure the template to create one for
	 you by choosing **true** for
	 **CreateNewSupportingAccessPoint**.
9. Choose **Next**.
10. On the **Configure stack options page**, choose **Next**.


For more information about the optional settings on this page, see [Setting
 AWS CloudFormation stack options](../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md") in the
 *AWS CloudFormation User Guide*.
11. On the **Review** page, choose **Create stack**.
For more information about configuring Object Lambda Access Points by using the AWS CDK, see [`AWS::S3ObjectLambda` Construct Library](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-s3objectlambda-readme.html "https://docs.aws.amazon.com/cdk/api/latest/docs/aws-s3objectlambda-readme.html") in the
 *AWS Cloud Development Kit (AWS CDK) API Reference*.
