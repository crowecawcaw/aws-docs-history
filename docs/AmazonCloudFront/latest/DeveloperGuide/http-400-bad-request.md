# HTTP 400 status code (Bad Request)

CloudFront returns a 400 bad request when the client sends some invalid data in the
 request such as missing or incorrect content in the payload or parameters. This
 could also represent a generic client error.


## Amazon S3 origin returns a 400 error


If you're using an Amazon S3 origin with your CloudFront distribution, your distribution
 might send error responses with HTTP status code 400 Bad Request, and a message
 similar to the following:


*The authorization header is malformed; the region
 '`<AWS Region>`' is wrong; expecting
 '`<AWS Region>`'*


For example:


*The authorization header is malformed; the region
 'us-east-1' is wrong; expecting 'us-west-2'*


This problem can occur in the following scenario:



1. Your CloudFront distribution's origin is an Amazon S3 bucket.
2. You moved the S3 bucket from one AWS Region to another. That is, you
 deleted the S3 bucket, then later you created a new bucket with the same
 bucket name, but in a different AWS Region than where the original S3
 bucket was located.

To fix this error, update your CloudFront distribution so that it finds the S3
 bucket in the bucket's current AWS Region.


###### To update your CloudFront distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose the distribution that produces this error.
3. Choose **Origins and Origin Groups**.
4. Find the origin for the S3 bucket that you moved. Select the check box
 next to this origin, then choose **Edit**.
5. Choose **Yes, Edit**. You do not need to change any
 settings before choosing **Yes, Edit**.

When you complete these steps, CloudFront redeploys your distribution. While the
 distribution is deploying, you see the **Deploying** status
 under the **Last modified** column. Some time after the
 deployment is complete, you should stop receiving the
 `AuthorizationHeaderMalformed` error responses.


## Application Load Balancer origin returns a 400 error


If you're using an Application Load Balancer origin with your CloudFront distribution, possible causes
 of a 400 error include the following:



* The client sent a malformed request that does not meet the HTTP
 specification.
* The request header exceeds 16 KB per request line, 16 KB per single
 header, or 64 KB for the entire request header.
* The client closed the connection before sending the full request
 body.
