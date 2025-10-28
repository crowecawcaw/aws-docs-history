# Use AMS SSP to provision Amazon Rekognition in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Rekognition capabilities directly in your AMS managed account. Amazon Rekognition makes it easy to add image and video analysis to your applications using proven, highly scalable, deep
learning technology that requires no machine learning expertise to use. With Amazon Rekognition, you can identify objects,
people, text, scenes, and activities in images and videos, as well as detect any inappropriate content. Amazon Rekognition also
provides highly accurate facial analysis and facial search capabilities that you can use to detect, analyze, and
compare faces for a wide variety of user verification, people counting, and public safety use cases.

With Amazon Rekognition Custom Labels, you can identify objects and scenes in images that are specific to your business
needs. For example, you can build a model to classify specific machine parts on your assembly line or to detect
unhealthy plants. Amazon Rekognition Custom Labels takes care of the model development heavy lifting for you, so no machine
learning experience is required. You simply need to supply images of objects or scenes you want to identify, and
the service handles the rest.

To learn more, see [Amazon Rekognition](https://aws.amazon.com/rekognition/ "https://aws.amazon.com/rekognition/").

## Amazon Rekognition in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon Rekognition in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_rekognition_console_role & customer_rekognition_service_role`. Once
provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Rekognition in my AMS account?**

Full functionality of Amazon Rekognition is available with the Amazon Rekognition self-provisioned service role.

**Q: What are the prerequisites or dependencies to using Amazon Rekognition in my AMS account?**

If you use Kinesis Video Streams that provide the source streaming video for an Amazon Rekognition Video stream processor or a data
stream as a destination to write data to Kinesis Data Streams, kindly provide AMS with a
`kinesisStreamName` when creating the RFC.
