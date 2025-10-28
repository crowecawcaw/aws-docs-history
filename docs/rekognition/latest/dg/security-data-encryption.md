# Data encryption

The following information explains where Amazon Rekognition uses data encryption to protect your data.

## Encryption at rest

### Amazon Rekognition Image

#### Images

Images passed to Amazon Rekognition API operations may be stored and used to improve the service
unless you have opted out by visiting the
[AI services opt-out policy page](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") and following the process explained there.
The stored images are encrypted at rest (Amazon S3) using AWS Key Management Service
(SSE-KMS).

#### Collections

For face comparison operations that store information in a collection, the underlying
detection algorithm first detects the faces in the input image, extracts a vector for each
face, and then stores the facial vectors in the collection. Amazon Rekognition uses these facial
vectors when performing face comparison. Facial vectors are stored as an array of floats and encrypted at rest.

### Amazon Rekognition Video

#### Videos

To analyze a video, Amazon Rekognition copies your videos into the service for processing. The
video may be stored and used to improve the service unless you have opted out by
visiting the [AI services opt-out policy page](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") and following the process explained there.
The videos are encrypted at rest (Amazon S3) using AWS Key Management Service (SSE-KMS).

### Amazon Rekognition Custom Labels

Amazon Rekognition Custom Labels encrypts your data at rest.

#### Images

To train your model, Amazon Rekognition Custom Labels makes a copy of your
source training and test images. The copied images are
encrypted at rest in Amazon Simple Storage Service (S3) using server-side
encryption with an AWS KMS key that you provide or an AWS owned KMS key.
Amazon Rekognition Custom Labels only supports symmetric KMS keys.
Your source images are unaffected.
For more information, see [Training an Amazon Rekognition Custom Labels Model](../customlabels-dg/tm-train-model.md "../customlabels-dg/tm-train-model.md").

#### Models

By default, Amazon Rekognition Custom Labels encrypts trained models
and manifest files stored in Amazon S3 buckets using server-side encryption with an AWS owned key.
For more information, see [Protecting Data Using Server-Side Encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md"). Training results are written
to the bucket specified in the `OutputConfig` input parameter to
[CreateProjectVersion](../APIReference/API_CreateProjectVersion.md "../APIReference/API_CreateProjectVersion.md").
The training results are encrypted using the configured encryption settings for the bucket
(`OutputConfig`).

#### Console bucket

The Amazon Rekognition Custom Labels console creates an Amazon S3 bucket (console bucket) that you can use
to manage your projects. The console bucket is encrypted using the default Amazon S3 encryption.
For more information, see [Amazon Simple Storage Service default encryption for S3 buckets](../../../AmazonS3/latest/dev/bucket-encryption.md "../../../AmazonS3/latest/dev/bucket-encryption.md").
If you are using your own KMS key, configure the console bucket after it is created.
For more information, see [Protecting Data Using Server-Side Encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md"). Amazon Rekognition Custom Labels blocks public access to
the console bucket.

### Rekognition Face Liveness

All session related data stored in Rekognition Face Liveness service’s account is
fully encrypted at rest. By default, reference and audit images are encrypted using an AWS
owned key in the service account. However, you can choose to provide your own AWS KMS keys for
encrypting these images.

## Encryption in transit

Amazon Rekognition API endpoints only support secure connections over HTTPS. All communication
is encrypted with Transport Layer Security (TLS).

## Key management

You can use AWS Key Management Service (KMS) to manage keys for the input images and videos
you store in Amazon S3 buckets. For more information, see [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys").

### Customer Managed Key Encryption for Face Liveness

The [CreateFaceLivenessSession](../APIReference/API_CreateFaceLivenessSession.md "../APIReference/API_CreateFaceLivenessSession.md") API takes in an optional `KmsKeyId`
parameter. You can provide the `id` of the KMS key you have created in your
account. This key will be used to encrypt reference and audit images obtained during
[StartFaceLivenessSession](../APIReference/API_StartFaceLivenessSession.md "../APIReference/API_StartFaceLivenessSession.md") API, and during [GetFaceLivenessSessionResults](../APIReference/API_GetFaceLivenessSessionResults.md "../APIReference/API_GetFaceLivenessSessionResults.md") API the images will be decrypted using this key
before returning the results. If CreateFaceLivenessSession request included an
OutputConfig, the reference and audit images will be uploaded to the specified Amazon S3 paths.
We recommend enabling Server Side Encryption ([SSE-S3](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md")) in your Amazon S3 buckets so that the data continues to remain encrypted at
rest.

When you provide your own AWS KMS key id, Rekognition Face Liveness service gets permission to
use the customer managed key on behalf of the principal that invokes the APIs. The
principals (users or roles) used to invoke the APIs from customer backend (APIs
`CreateFaceLivenessSession` and `GetFaceLivenessSessionResults`)
must have access to perform the following:

- kms:DescribeKey
- kms:GenerateDataKey
- kms:Decrypt
