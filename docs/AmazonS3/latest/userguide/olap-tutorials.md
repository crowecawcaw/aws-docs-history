# S3 Object Lambda tutorials

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on November 7th, 2025. If you would like to use the service, please sign up prior to November 7th, 2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](amazons3-ol-change.md "amazons3-ol-change.md").

The following tutorials present complete end-to-end procedures for some S3 Object Lambda tasks.

With S3 Object Lambda, you can add your own code to process data retrieved from S3 before returning it
 to an application. Each of the following tutorials will modify data as it is retrieved from
 Amazon S3, without changing the existing object or maintaining multiple copies of the data. The
 first tutorial will walk through how to add an AWS Lambda function to a S3 GET request
 to modify an object retrieved from S3. The second tutorial demonstrates how to use a prebuilt
 Lambda function powered by Amazon Comprehend to protect personally identifiable information (PII) retrieved from S3 before
 returning it to an application. The third tutorial uses S3 Object Lambda to add a watermark to an image as it is retrieved from Amazon S3.


* [Tutorial: Transforming data for your
 application with S3 Object Lambda](tutorial-s3-object-lambda-uppercase.md "tutorial-s3-object-lambda-uppercase.md")
* [Tutorial:
 Detecting and redacting PII data with S3 Object Lambda and Amazon Comprehend](tutorial-s3-object-lambda-redact-pii.md "tutorial-s3-object-lambda-redact-pii.md")
* [Tutorial: Using S3 Object Lambda to dynamically watermark images as they are retrieved](https://aws.amazon.com/getting-started/hands-on/amazon-s3-object-lambda-to-dynamically-watermark-images/?ref=docs_gateway/amazons3/olap-tutorials.html "https://aws.amazon.com/getting-started/hands-on/amazon-s3-object-lambda-to-dynamically-watermark-images/?ref=docs_gateway/amazons3/olap-tutorials.html")
