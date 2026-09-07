

# ADVSEC05-BP01 Validate and sanitize content before running a campaign
<a name="advsec05-bp01"></a>

 Content validation is essential to mitigate ad fraud and block unwanted content from reaching ad audience. 

## Implementation guidance
<a name="implementation-guidance-advsec05-bp01"></a>

Consider using Amazon S3 which can serve as a secure, scalable storage solution for advertising content. It allows for simple management and distribution of assets. S3 can be configured with strict access controls and encryption to maintain the security of the advertisement files. Additionally, Amazon Rekognition can be utilized to analyze images and videos in advertisements, verifying they meet solution standards and don't contain inappropriate content. This AI-powered service can detect objects, scenes, and activities in visual content. For additional monitoring and auditing, consider using AWS CloudTrail to provide a record of actions taken by users, roles, or AWS services in the ad serving solution, which is essential for security analysis and compliance audits.

## Key AWS services
<a name="key-aws-services-8"></a>
+  Amazon S3 
+  Amazon Rekognition 
+  AWS CloudTrail 

## Resources
<a name="resources-13"></a>
+  [Checking object integrity in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) 
+  [Amazon Rekognition](https://aws.amazon.com/rekognition/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 