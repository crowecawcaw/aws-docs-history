# Using the AWS Marketplace Commerce Analytics Service with the AWS CLI and AWS SDK for Java

With the AWS Marketplace Commerce Analytics Service, you can programmatically access product and customer data
through AWS Marketplace. The AWS Marketplace Commerce Analytics Service is provided through the [AWS SDK](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/"). You use the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") and the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/") to interact with the Commerce Analytics Service.
These sections show you how to implement the Commerce Analytics Service by using the AWS CLI and SDK for Java.

###### Topics

- [IAM policies for
  Commerce Analytics Service](#aws-marketplace-commerce-analytics-iam-permissions "#aws-marketplace-commerce-analytics-iam-permissions")
- [Making Requests with the AWS CLI](#making-requests-with-aws-cli "#making-requests-with-aws-cli")
- [Making requests with the
  AWS SDK for Java](#making-requests-with-aws-java-sdk "#making-requests-with-aws-java-sdk")

## IAM policies for

Commerce Analytics Service

To allow your users to use the Commerce Analytics Service, the following permissions are required.

Use the following IAM permissions policy to enroll in the AWS Marketplace Commerce Analytics Service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy",
 "aws-marketplace-management:viewReports"
 ],
 "Resource": "*"
 }
 ]
}`

```

Use the following IAM permissions policy to allow an user to make requests to the
AWS Marketplace Commerce Analytics Service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "marketplacecommerceanalytics:GenerateDataSet",
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Creating Policies in the IAM console](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

## Making Requests with the AWS CLI

To get started, download the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). The
following AWS CLI example makes a request for the **Hourly/Monthly
Subscriptions** dataset for October 1, 2017. This dataset is published to the
**demo-bucket** Amazon S3 bucket using the prefix **demo-prefix**, and the notification message is delivered to the
**demo-topic** Amazon SNS topic.

```

aws marketplacecommerceanalytics generate-data-set \
--data-set-type "customer_subscriber_hourly_monthly_subscriptions" \
--data-set-publication-date "2017-10-01T00:00:00Z" \
--role-name-arn "arn:aws:iam::123412341234:role/MarketplaceCommerceAnalyticsRole" \
--destination-s3-bucket-name "demo-bucket" \
--destination-s3-prefix "demo-prefix" \
--sns-topic-arn "arn:aws:sns:us-west-2:123412341234:demo-topic"

```

This request returns an identifier that is unique for each request. You can use this
identifier to correlate requests with notifications published to your Amazon SNS topic. The
following example is an example of this identifier.

```

{
   "dataSetRequestId": "646dd4ed-6806-11e5-a6d8-fd5dbcaa74ab"
}

```

## Making requests with the

AWS SDK for Java

To start, download the [AWS Java
SDK](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/"). The following AWS SDK for Java example makes a request for the **Hourly/Monthly Subscriptions** dataset for October 1, 2015. This
dataset is published to the **demo-bucket** Amazon S3 bucket using
the prefix **demo-prefix**, and the notification message is
delivered to the **demo-topic** Amazon SNS topic.

```

/*
* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
*
* Licensed under the Apache License, Version 2.0 (the "License").
* You may not use this file except in compliance with the License.
* A copy of the License is located at
*
* http://aws.amazon.com/apache2.0
*
* or in the "license" file accompanying this file. This file is distributed
* on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
* express or implied. See the License for the specific language governing
* permissions and limitations under the License.
*/
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;
import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Region;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.marketplacecommerceanalytics.AWSMarketplaceCommerceAnalyticsClient;
import com.amazonaws.services.marketplacecommerceanalytics.model.GenerateDataSetRequest;
import com.amazonaws.services.marketplacecommerceanalytics.model.GenerateDataSetResult;
/**
* This sample demonstrates how to make basic requests to the AWS Marketplace Commerce
* Analytics service using the AWS SDK for Java.
* <p>
* <b>Prerequisites:</b> Follow the on-boarding guide: {URL OR SOMETHING}
* <p>
* Fill in your AWS access credentials in the provided credentials file
* template, and be sure to move the file to the default location
* (~/.aws/credentials) where the sample code will load the credentials from.
* <p>
* <b>WARNING:</b> To avoid accidental leakage of your credentials, DO NOT keep
* the credentials file in your source directory.
* <p>
* http://aws.amazon.com/security-credentials
*/
public class MarketplaceCommerceAnalyticsSample {
public static void main(String[] args) throws ParseException {
/*
* The ProfileCredentialsProvider will return your [default]
* credential profile by reading from the credentials file located at
* (~/.aws/credentials).
*/
AWSCredentials credentials = null;
try {
credentials = new ProfileCredentialsProvider().getCredentials();
} catch (Exception e) {
throw new AmazonClientException("Cannot load the credentials from the credential profiles "
+ "file. Make sure that your credentials file is at the correct "
+ "location (~/.aws/credentials), and is in valid
format.", e);
}
AWSMarketplaceCommerceAnalyticsClient client = new AWSMarketplaceCommerceAnalyticsClient(credentials);
Region usEast1 = Region.getRegion(Regions.US_EAST_1);
client.setRegion(usEast1);
System.out.println("===============================================================");
System.out.println("Getting Started with AWS Marketplace Commerce Analytics Service");
System.out.println("===============================================================\n");
// Create a data set request with the desired parameters
GenerateDataSetRequest request = new GenerateDataSetRequest();
request.setDataSetType("customer_subscriber_hourly_monthly_subscriptions");
request.setDataSetPublicationDate(convertIso8601StringToDateUtc("2014-06-09T00:00:00Z"));
request.setRoleNameArn("arn:aws:iam::864545609859:role/MarketplaceCommerceAnalyticsRole");
request.setDestinationS3BucketName("awsmp-goldmine-seller");
request.setDestinationS3Prefix("java-sdk-test");
request.setSnsTopicArn("arn:aws:sns:us-west-2:864545609859:awsmp-goldmine-seller-topic");
System.out.println(
String.format("Creating a request for data set %s for publication date %s.",
request.getDataSetType(), request.getDataSetPublicationDate()));
try {
// Make the request to the service
GenerateDataSetResult result = client.generateDataSet(request);
// The Data Set Request ID is a unique identifier that you can use to correlate the
// request with responses on your Amazon SNS topic
System.out.println("Request successful, unique ID: " + result.getDataSetRequestId());
} catch (AmazonServiceException ase) {
System.out.println("Caught an AmazonServiceException, which means your request made it "
+ "to the AWS Marketplace Commerce Analytics service, but was rejected with an "
+ "error response for some reason.");
System.out.println("Error Message: " + ase.getMessage());
System.out.println("HTTP Status Code: " + ase.getStatusCode());
System.out.println("AWS Error Code: " + ase.getErrorCode());
System.out.println("Error Type: " + ase.getErrorType());
System.out.println("Request ID: " + ase.getRequestId());
} catch (AmazonClientException ace) {
System.out.println("Caught an AmazonClientException, which means the client encountered "
+ "a serious internal problem while trying to communicate with the AWS Marketplace"
+ "Commerce Analytics service, such as not being able to access the "
+ "network.");
System.out.println("Error Message: " + ace.getMessage());
}
}
private static Date convertIso8601StringToDateUtc(String dateIso8601) throws ParseException {
TimeZone utcTimeZone = TimeZone.getTimeZone("UTC");
DateFormat utcDateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssX");
utcDateFormat.setTimeZone(utcTimeZone);
return utcDateFormat.parse(dateIso8601);
}
}

```

You should expect results similar to this example.

```

===============================================================
Getting Started with AWS Marketplace Commerce Analytics Service
===============================================================
Creating a request for data set customer_subscriber_hourly_monthly_subscriptions for publication
date Sun Jun 08 17:00:00 PDT 2014.
Request successful, unique ID: c59aff81-6875-11e5-a6d8-fd5dbcaa74ab

```
