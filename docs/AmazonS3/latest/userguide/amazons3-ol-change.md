# Amazon S3 Object Lambda availability change

After careful consideration, we have made the decision to only allow existing customers to
 utilize Amazon S3 Object Lambda starting on November 7th, 2025. Existing customers of S3 Object Lambda can continue to
 use the service as usual. AWS will continue to to invest in security and availability
 improvements for S3 Object Lambda, but we do not plan to introduce new capabilities.

There are several alternative services and designs that allow you to modify and process
 data accessed from S3 to meet the needs of various client applications or users who are
 accessing the data. Those alternatives include the AWS Solution Dynamic Image Transformation
 for Amazon CloudFront, invoking AWS Lambda by other means (via CloudFront, API Gateway, or
 function URLs), or processing data in the client application. All of these alternatives
 continue to use Amazon S3 for the underlying storage, so no data migration is
 necessary.

In this post, we discuss how to choose the best option for your use case.


**Dynamic Image Transformation for Amazon CloudFront**


This AWS solution enables real-time image processing through the global content delivery
 network (CDN) of Amazon CloudFront using API Gateway and Lambda. It supports a variety of
 transformations such as format changes, dimensions, fit methods, rotations, and filters. If
 you are using S3 Object Lambda today for image transformation, this can be a good alternative. The
 [solution overview](https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/solution-overview.html "https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/solution-overview.html") has more details on capabilities and how to get started using
 it. Be sure to modify the Enable S3 Object Lambda template parameter to "No" when deploying the solution
 to your account.

For more information, see [Dynamic Image Transformation for Amazon CloudFront](https://aws.amazon.com/solutions/implementations/dynamic-image-transformation-for-amazon-cloudfront/ "https://aws.amazon.com/solutions/implementations/dynamic-image-transformation-for-amazon-cloudfront/").


**Data processing in AWS Lambda**


You can continue to use AWS Lambda for your data processing, but invoke it directly or
 through other AWS services. Your data processing logic can remain the same, but your Lambda
 function will need to be updated based on how you choose to invoke it. This option is best
 for use cases such as sensitive data redaction, format changes, or situations where the
 application that invokes S3 Object Lambda relies on receiving processed data. This option also
 minimizes the changes required if you choose to migrate off S3 Object Lambda.

If you are using an S3 Object Lambda access point as the origin of a CloudFront
 distribution, you can create a new origin using either Lambda Function URLs or API Gateway. 
 [This blog](https://aws.amazon.com/blogs/networking-and-content-delivery/using-amazon-cloudfront-with-aws-lambda-as-origin-to-accelerate-your-web-applications/ "https://aws.amazon.com/blogs/networking-and-content-delivery/using-amazon-cloudfront-with-aws-lambda-as-origin-to-accelerate-your-web-applications/") details how you can setup a Lambda Function URL to act as an origin for your
 CloudFront distribution.

If you directly invoke S3 Object Lambda from your client code today, you can use Lambda
 Function URLs to directly invoke your Lambda function or you can use API Gateway. If you're
 not sure which is the best method for your use case, see [Select a method to invoke your
 Lambda function using an HTTP request](https://docs.aws.amazon.com/lambda/latest/dg/apig-http-invoke-decision.html "https://docs.aws.amazon.com/lambda/latest/dg/apig-http-invoke-decision.html") in the *AWS Lambda Developer Guide*. After you have decided which method for invoking
 Lambda is best for your use case and have setup your Lambda function accordingly, you will
 also need to update your calling application to invoke your Lambda function rather than
 calling S3 Object Lambda.


**Data processing in the client application**


You also have the option of moving your data processing logic from S3 Object Lambda into
 your client application. This works best if you are using S3 Object Lambda as part of an
 application that already performs further processing or analysis of the data returned by S3 Object Lambda. For example, if your S3 Object Lambda access point was responsible for
 redirecting to particular objects or object versions, that redirect logic can be moved into
 the calling application which would then directly access data in the S3 bucket.

If you need assistance or have feedback, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").
