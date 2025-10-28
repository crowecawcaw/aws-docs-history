# Giving Amazon Rekognition Video access to your

resources

You use an AWS Identity and Access Management (IAM) service role to give Amazon Rekognition Video read access to Kinesis
video streams. If you are using a face search stream processor, you use an IAM
service role to give Amazon Rekognition Video write access to Kinesis data streams. If you are using a
security monitoring stream processor, you use IAM roles to give Amazon Rekognition Video access to
your Amazon S3 bucket and to an Amazon SNS topic.

## Giving access for face search stream processors

You can create a permissions policy that allows Amazon Rekognition Video access to individual
Kinesis video streams and Kinesis data streams.

###### To give Amazon Rekognition Video access for a face search stream processor

1. [Create a new permissions policy with the IAM JSON policy
   editor](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor"), and use the following policy. Replace
   `video-arn` with the ARN of the desired Kinesis video stream. If you
   are using a face search stream processor, replace `data-arn`
   with the ARN of the desired Kinesis data stream.
2. [Create an IAM service role](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md"), or update an existing IAM
   service role. Use the following information to create the IAM service
   role:
   1. Choose **Rekognition** for the service
      name.
   2. Choose **Rekognition** for the service role
      use case.
   3. Attach the permissions policy that you created in step
   4.

3. Note the ARN of the service role. You need it to start video analysis
   operations.

## Giving access to streams

using AmazonRekognitionServiceRole

As an alternative option for setting up access to Kinesis video streams and data
streams, you can use the `AmazonRekognitionServiceRole` permissions
policy. IAM provides the _Rekognition_ service role use
case that, when used with the `AmazonRekognitionServiceRole`
permissions policy, can write to multiple Kinesis data streams and read from all
your Kinesis video streams. To give Amazon Rekognition Video write access to multiple Kinesis data
streams, you can prepend the names of the Kinesis data streams with
_AmazonRekognition_—for example,
`AmazonRekognitionMyDataStreamName`.

###### To give Amazon Rekognition Video access to your Kinesis video stream and Kinesis data stream

1. [Create an IAM service role](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md"). Use the following information
   to create the IAM service role:
   1. Choose **Rekognition** for the service
      name.
   2. Choose **Rekognition** for the service role
      use case.
   3. Choose the **AmazonRekognitionServiceRole**
      permissions policy, which gives Amazon Rekognition Video write access to Kinesis
      data streams that are prefixed with
      _AmazonRekognition_ and read access to
      all your Kinesis video streams.

2. To ensure your AWS account is secure, limit the scope of Rekognition's access to
   just the resources you are using. This can be done by attaching a trust
   policy to your IAM service role. For information on how to do this,
   see [Cross-service confused deputy
   prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").
3. Note the Amazon Resource Name (ARN) of the service role. You need it
   to start video analysis operations.
