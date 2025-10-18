# Delete Lambda@Edge functions and
 replicas

You can delete a Lambda@Edge function only when the replicas of the function have been
 deleted by CloudFront. Replicas of a Lambda function are automatically deleted in the following
 situations:


* After you remove the last association for the function from all of your CloudFront
 distributions. If more than one distribution uses a function, the replicas are
 deleted only after you remove the function association from the last
 distribution.
* After you delete the last distribution that a function was associated
 with.
Replicas are typically deleted within a few hours. You cannot manually delete
 Lambda@Edge function replicas. This helps prevent a situation where a replica is deleted
 that is still in use, which would result in an error.

###### Warning

Don't build applications that use Lambda@Edge function replicas outside of CloudFront.
 These replicas are deleted when their associations with distributions are removed,
 or when distributions themselves are deleted. The replica that an outside
 application depends on might be removed without warning, causing it to fail.

###### To delete a Lambda@Edge function association from a CloudFront distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose the ID of the distribution with the Lambda@Edge function association
 that you want to delete.
3. Choose the **Behaviors** tab.
4. Select the cache behavior that has the Lambda@Edge function association that
 you want to delete, and then choose **Edit**.
5. Under **Function associations**, **Function
 type**, choose **No association** to delete the
 Lambda@Edge function association.
6. Choose **Save changes**.
After you delete a Lambda@Edge function association from a CloudFront distribution, you can
 optionally delete the Lambda function or function version from AWS Lambda. Wait a few
 hours after deleting the function association so that the Lambda@Edge function replicas
 can be cleaned up. After that, you can delete the function by using the Lambda console,
 AWS CLI, Lambda API, or an AWS SDK.

You can also delete a specific *version* of a Lambda function if the
 version doesn't have any CloudFront distributions associated with it. After removing all the
 associations for a Lambda function version, wait a few hours. Then you can delete the
 function version.
