# Using Multi-Region Access Points with supported API operations

Amazon S3 provides a set of operations to manage Multi-Region Access Points. Amazon S3 processes some of these
operations synchronously and some asynchronously. When you invoke an asynchronous operation,
Amazon S3 first synchronously authorizes the requested operation. If authorization is successful,
Amazon S3 returns a token that you can use to track the progress and results of the requested
operation.

###### Note

Requests that are made through the Amazon S3 console are always synchronous. The console
waits until the request is completed before allowing you to submit another request.

You can view the current status and results of asynchronous operations by using the
console, or you can use `DescribeMultiRegionAccessPointOperation` in the AWS CLI,
AWS SDKs, or REST API. Amazon S3 provides a tracking token in the response to an asynchronous
operation. You include that tracking token as an argument to
`DescribeMultiRegionAccessPointOperation`. When you include the tracking
token, Amazon S3 then returns the current status and results of the specified operation,
including any errors or relevant resource information. Amazon S3 performs
`DescribeMultiRegionAccessPointOperation` operations synchronously.

All control plane requests to create or maintain Multi-Region Access Points must be routed to the
`US West (Oregon)` Region. For Multi-Region Access Point data plane requests, Regions don't need to be
specified. For the Multi-Region Access Point failover control plane, the request must be routed to one of the
five supported Regions. For more information about Multi-Region Access Point supported Regions, see [Multi-Region Access Point restrictions and limitations](MultiRegionAccessPointRestrictions.md "MultiRegionAccessPointRestrictions.md").

In addition, you must grant the `s3:ListAllMyBuckets` permission to the user,
role, or other AWS Identity and Access Management (IAM) entity that makes a request to manage a Multi-Region Access Point.

The following examples demonstrate how to use Multi-Region Access Points with compatible operations in
Amazon S3.

###### Topics

- [Multi-Region Access Point compatibility with AWS services and AWS SDKs](#mrap-api-support "#mrap-api-support")
- [Multi-Region Access Point compatibility with S3 operations](#mrap-operations-support "#mrap-operations-support")
- [View your Multi-Region Access Point routing configuration](#query-mrap-routing-configuration "#query-mrap-routing-configuration")
- [Update your underlying Amazon S3 bucket policy](#update-underlying-bucket-policy "#update-underlying-bucket-policy")
- [Update a Multi-Region Access Point route configuration](#update-mrap-route-configuration "#update-mrap-route-configuration")
- [Add an object to a bucket in your Multi-Region Access Point](#add-bucket-mrap "#add-bucket-mrap")
- [Retrieve objects from your Multi-Region Access Point](#get-object-mrap "#get-object-mrap")
- [List objects that are stored in a bucket underlying your Multi-Region Access Point](#list-objects-mrap "#list-objects-mrap")
- [Use a presigned URL with Multi-Region Access Points](#use-presigned-url-mrap "#use-presigned-url-mrap")
- [Use a bucket that's configured with Requester Pays with Multi-Region Access Points](#use-requester-pays-mrap "#use-requester-pays-mrap")

## Multi-Region Access Point compatibility with AWS services and AWS SDKs

To use a Multi-Region Access Point with applications that require an Amazon S3 bucket name, use the Amazon Resource
Name (ARN) of the Multi-Region Access Point when making requests by using an AWS SDK.
To check which AWS SDKs are compatible with Multi-Region Access Points, see [Compatibility with
AWS SDKs](../../../sdkref/latest/guide/feature-s3-mrap.md#s3-mrap-sdk-compat "../../../sdkref/latest/guide/feature-s3-mrap.md#s3-mrap-sdk-compat").

## Multi-Region Access Point compatibility with S3 operations

You can use use the following Amazon S3 data plane API operations to perform actions on
objects in buckets that are associated with your Multi-Region Access Point. The following S3 operations can
accept Multi-Region Access Point ARNs:

- [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")
- [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
- [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
- [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")
- [DeleteObjectTagging](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md")
- [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
- [GetObjectAcl](../API/API_GetObjectAcl.md "../API/API_GetObjectAcl.md")
- [GetObjectLegalHold](../API/API_GetObjectLegalHold.md "../API/API_GetObjectLegalHold.md")
- [GetObjectRetention](../API/API_GetObjectRetention.md "../API/API_GetObjectRetention.md")
- [GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md")
- [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")
- [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")
- [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")
- [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")
- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
- [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md")
- [PutObjectLegalHold](../API/API_PutObjectLegalHold.md "../API/API_PutObjectLegalHold.md")
- [PutObjectRetention](../API/API_PutObjectRetention.md "../API/API_PutObjectRetention.md")
- [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md")
- [RestoreObject](../API/API_RestoreObject.md "../API/API_RestoreObject.md")
- [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")

###### Note

Multi-Region Access Points supports copy operations using Multi-Region Access Points only as a destination when using the Multi-Region Access Point ARN.

You can use the following Amazon S3 control plane operations to create and manage your
Multi-Region Access Points:

- [CreateMultiRegionAccessPoint](../API/API_control_CreateMultiRegionAccessPoint.md "../API/API_control_CreateMultiRegionAccessPoint.md")
- [DescribeMultiRegionAccessPointOperation](../API/API_control_DescribeMultiRegionAccessPointOperation.md "../API/API_control_DescribeMultiRegionAccessPointOperation.md")
- [GetMultiRegionAccessPoint](../API/API_control_GetMultiRegionAccessPoint.md "../API/API_control_GetMultiRegionAccessPoint.md")
- [GetMultiRegionAccessPointPolicy](../API/API_control_GetMultiRegionAccessPointPolicy.md "../API/API_control_GetMultiRegionAccessPointPolicy.md")
- [GetMultiRegionAccessPointPolicyStatus](../API/API_control_GetMultiRegionAccessPointPolicyStatus.md "../API/API_control_GetMultiRegionAccessPointPolicyStatus.md")
- [GetMultiRegionAccessPointRoutes](../API/API_control_GetMultiRegionAccessPointRoutes.md "../API/API_control_GetMultiRegionAccessPointRoutes.md")
- [ListMultiRegionAccessPoints](../API/API_control_ListMultiRegionAccessPoints.md "../API/API_control_ListMultiRegionAccessPoints.md")
- [PutMultiRegionAccessPointPolicy](../API/API_control_PutMultiRegionAccessPointPolicy.md "../API/API_control_PutMultiRegionAccessPointPolicy.md")
- [SubmitMultiRegionAccessPointRoutes](../API/API_control_SubmitMultiRegionAccessPointRoutes.md "../API/API_control_SubmitMultiRegionAccessPointRoutes.md")

## View your Multi-Region Access Point routing configuration

AWS CLI
The following example command retrieves your Multi-Region Access Point route configuration so
that you can see the current routing statuses for your buckets. To use this
example command, replace the `user input
 placeholders` with your own information.

```
aws s3control get-multi-region-access-point-routes
--region `eu-west-1`
--account-id `111122223333`
--mrap arn:aws:s3::`111122223333`:accesspoint/`abcdef0123456`.mrap
```

SDK for Java
The following SDK for Java code retrieves your Multi-Region Access Point route configuration so
that you can see the current routing statuses for your buckets. To use this
example syntax, replace the `user input
 placeholders` with your own information.

```
S3ControlClient s3ControlClient = S3ControlClient.builder()
    .region(Region.`US_EAST_1`)
    .credentialsProvider(credentialsProvider)
    .build();

GetMultiRegionAccessPointRoutesRequest request = GetMultiRegionAccessPointRoutesRequest.builder()
    .accountId("`111122223333`")
    .mrap("arn:aws:s3::`111122223333`:accesspoint/`abcdef0123456`.mrap")
    .build();

GetMultiRegionAccessPointRoutesResponse response = s3ControlClient.getMultiRegionAccessPointRoutes(request);
```

SDK for JavaScript
The following SDK for JavaScript code retrieves your Multi-Region Access Point route configuration so that
you can see the current routing statuses for your buckets. To use this
example syntax, replace the `user input
 placeholders` with your own information.

```
const REGION = '`us-east-1`'

const s3ControlClient = new S3ControlClient({
  region: REGION
})

export const run = async () => {
  try {
    const data = await s3ControlClient.send(
      new GetMultiRegionAccessPointRoutesCommand({
        AccountId: '`111122223333`',
        Mrap: 'arn:aws:s3::`111122223333`:accesspoint/`abcdef0123456`.mrap',
      })
    )
    console.log('Success', data)
    return data
  } catch (err) {
    console.log('Error', err)
  }
}

run()
```

SDK for Python
The following SDK for Python code retrieves your Multi-Region Access Point route configuration so
that you can see the current routing statuses for your buckets. To use this
example syntax, replace the `user input
 placeholders` with your own information.

```
s3.get_multi_region_access_point_routes(
        AccountId=`111122223333`,
        Mrap=arn:aws:s3::`111122223333`:accesspoint/`abcdef0123456`.mrap)['Routes']
```

## Update your underlying Amazon S3 bucket policy

To grant proper access, you must also update the underlying Amazon S3 bucket policy. The
following examples delegate access control to the Multi-Region Access Point policy. After you delegate
access control to the Multi-Region Access Point policy, the bucket policy is no longer used for access
control when requests are made through the Multi-Region Access Point.

Here's an example bucket policy that delegates access control to the Multi-Region Access Point policy. To
use this example bucket policy, replace the `user input
 placeholders` with your own information. To apply this
policy through the AWS CLI `put-bucket-policy` command, as shown in the next
example, save the policy in a file, for example,
`policy.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`444455556666`:root"
 },
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:DataAccessPointAccount": "`444455556666`"
 }
 }
 }
 ]
}`

```

The following `put-bucket-policy` example command associates the updated S3
bucket policy with your S3 bucket:

```
aws s3api put-bucket-policy
  --bucket `amzn-s3-demo-bucket`
  --policy file:`///tmp/policy.json`
```

## Update a Multi-Region Access Point route configuration

The following example command updates the Multi-Region Access Point route configuration. Multi-Region Access Point route
commands can be run against the following five Regions:

- `ap-southeast-2`
- `ap-northeast-1`
- `us-east-1`
- `us-west-2`
- `eu-west-1`

In a Multi-Region Access Point routing configuration, you can set buckets to an active or passive routing
status. Active buckets receive traffic, whereas passive buckets do not. You can set a
bucket's routing status by setting the `TrafficDialPercentage` value for the
bucket to `100` for active or `0` for passive.

AWS CLI
The following example command updates your Multi-Region Access Point routing configuration.
In this example,
`amzn-s3-demo-bucket1`
is set to active status and
`amzn-s3-demo-bucket2`
is set to passive. To use this example command, replace the
`user input placeholders` with
your own information.

```
aws s3control submit-multi-region-access-point-routes
--region `ap-southeast-2`
--account-id `111122223333`
--mrap arn:aws:s3::`111122223333`:accesspoint/`abcdef0123456`.mrap
--route-updates Bucket=`amzn-s3-demo-bucket1`,TrafficDialPercentage=`100`
                Bucket=`amzn-s3-demo-bucket2`,TrafficDialPercentage=`0`
```

SDK for Java
The following SDK for Java code updates your Multi-Region Access Point routing configuration. To
use this example syntax, replace the `user input
 placeholders` with your own information.

```
S3ControlClient s3ControlClient = S3ControlClient.builder()
    .region(Region.`ap-southeast-2`)
    .credentialsProvider(credentialsProvider)
    .build();

SubmitMultiRegionAccessPointRoutesRequest request = SubmitMultiRegionAccessPointRoutesRequest.builder()
    .accountId("`111122223333`")
    .mrap("arn:aws:s3::`111122223333`:accesspoint/`abcdef0123456`.mrap")
    .routeUpdates(
        MultiRegionAccessPointRoute.builder()
            .region("`eu-west-1`")
            .trafficDialPercentage(`100`)
            .build(),
        MultiRegionAccessPointRoute.builder()
            .region("`ca-central-1`")
            .bucket("`111122223333`")
            .trafficDialPercentage(`0`)
            .build()
    )
    .build();

SubmitMultiRegionAccessPointRoutesResponse response = s3ControlClient.submitMultiRegionAccessPointRoutes(request);
```

SDK for JavaScript
The following SDK for JavaScript code updates your Multi-Region Access Point route configuration. To use
this example syntax, replace the `user input
 placeholders` with your own information.

```
const REGION = '`ap-southeast-2`'

const s3ControlClient = new S3ControlClient({
  region: REGION
})

export const run = async () => {
  try {
    const data = await s3ControlClient.send(
      new SubmitMultiRegionAccessPointRoutesCommand({
        AccountId: '`111122223333`',
        Mrap: 'arn:aws:s3::`111122223333`:accesspoint/`abcdef0123456`.mrap',
        RouteUpdates: [
          {
            Region: '`eu-west-1`',
            TrafficDialPercentage: `100`,
          },
          {
            Region: '`ca-central-1`',
            Bucket: '`amzn-s3-demo-bucket1`',
            TrafficDialPercentage: `0`,
          },
        ],
      })
    )
    console.log('Success', data)
    return data
  } catch (err) {
    console.log('Error', err)
  }
}

run()
```

SDK for Python
The following SDK for Python code updates your Multi-Region Access Point route configuration. To
use this example syntax, replace the `user input
 placeholders` with your own information.

```
s3.submit_multi_region_access_point_routes(
        AccountId=`111122223333`,
        Mrap=arn:aws:s3::`111122223333`:accesspoint/`abcdef0123456`.mrap,
        RouteUpdates= [{
            'Bucket': ``amzn-s3-demo-bucket``,
            'Region': `ap-southeast-2`,
            'TrafficDialPercentage': `10`
        }])
```

## Add an object to a bucket in your Multi-Region Access Point

To add an object to the bucket that's associated with the Multi-Region Access Point, you can use the
[PutObject](../API/API_PutObject.md "../API/API_PutObject.md") operation. To keep all
buckets in the Multi-Region Access Point in sync, enable [Cross-Region
Replication](MultiRegionAccessPointBucketReplication.md "MultiRegionAccessPointBucketReplication.md").

###### Note

To use this operation, you must have the `s3:PutObject` permission for
the Multi-Region Access Point. For more information about Multi-Region Access Point permission requirements, see [Permissions](MultiRegionAccessPointPermissions.md "MultiRegionAccessPointPermissions.md").

AWS CLI
The following example
data
plane request uploads
`example.txt` to the specified
Multi-Region Access Point. To use this example, replace the `user input
 placeholders` with your own information.

```
aws s3api put-object --bucket arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap --key `example.txt` --body `example.txt`
```

SDK for Java

```
S3Client s3Client = S3Client.builder()
        .build();

PutObjectRequest objectRequest = PutObjectRequest.builder()
        .bucket("arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap")
        .key("`example.txt`")
        .build();

s3Client.putObject(objectRequest, RequestBody.fromString("`Hello S3!`"));
```

SDK for JavaScript

```
const client = new S3Client({});

async function putObjectExample() {
    const command = new PutObjectCommand({
        Bucket: "arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap",
        Key: "`example.txt`",
        Body: "`Hello S3!`",
    });

    try {
        const response = await client.send(command);
        console.log(response);
    } catch (err) {
        console.error(err);
    }
}
```

SDK for Python

```
import boto3

client = boto3.client('s3')
client.put_object(
    Bucket='arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap',
    Key='`example.txt`',
    Body='`Hello S3!`'
)
```

## Retrieve objects from your Multi-Region Access Point

To retrieve objects from the Multi-Region Access Point, you can use the [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
operation.

###### Note

To use this API operation, you must have the `s3:GetObject` permission
for the Multi-Region Access Point. For more information about Multi-Region Access Point permissions requirements, see
[Permissions](MultiRegionAccessPointPermissions.md "MultiRegionAccessPointPermissions.md").

AWS CLI
The following example
data
plane request retrieves
`example.txt` from the
specified Multi-Region Access Point and downloads it as
`downloaded_example.txt`. To
use this example, replace the `user input
 placeholders` with your own information.

```
aws s3api get-object --bucket arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap --key `example.txt` `downloaded_example.txt`
```

SDK for Java

```
S3Client s3 = S3Client
   .builder()
   .build();

GetObjectRequest getObjectRequest = GetObjectRequest.builder()
    .bucket("arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap")
    .key("`example.txt`")
    .build();

s3Client.getObject(getObjectRequest);
```

SDK for JavaScript

```
const client = new S3Client({})

async function getObjectExample() {
    const command = new GetObjectCommand({
        Bucket: "arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap",
        Key: "`example.txt`"
    });

    try {
        const response = await client.send(command);
        console.log(response);
    } catch (err) {
        console.error(err);
    }
}
```

SDK for Python

```
import boto3

client = boto3.client('s3')
client.get_object(
    Bucket='arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap',
    Key='`example.txt`'
)
```

## List objects that are stored in a bucket underlying your Multi-Region Access Point

To return a list of objects that are stored in a bucket underlying your Multi-Region Access Point, use
the [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")
operation. In the following example command, all objects for the specified Multi-Region Access Point are
listed by using the ARN for the Multi-Region Access Point. In this case, the Multi-Region Access Point ARN is:

`arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap`

###### Note

To use this API operation, you must have the `s3:ListBucket` permission
for the Multi-Region Access Point and the underlying bucket. For more information about Multi-Region Access Point
permissions requirements, see [Permissions](MultiRegionAccessPointPermissions.md "MultiRegionAccessPointPermissions.md").

AWS CLI
The following example
data
plane request lists the objects in the bucket that
underlies the Multi-Region Access Point that's specified by the ARN. To use this example,
replace the `user input placeholders`
with your own information.

```
aws s3api list-objects-v2 --bucket arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap
```

SDK for Java

```
S3Client s3Client = S3Client.builder()
        .build();

String bucketName = "arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap";

ListObjectsV2Request listObjectsRequest = ListObjectsV2Request
    .builder()
    .bucket(bucketName)
    .build();

 s3Client.listObjectsV2(listObjectsRequest);
```

SDK for JavaScript

```
const client = new S3Client({});

async function listObjectsExample() {
    const command = new ListObjectsV2Command({
        Bucket: "arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap",
    });

    try {
        const response = await client.send(command);
        console.log(response);
    } catch (err) {
        console.error(err);
    }
}
```

SDK for Python

```
import boto3

client = boto3.client('s3')
client.list_objects_v2(
    Bucket='arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap'
)
```

## Use a presigned URL with Multi-Region Access Points

You can use a presigned URL to generate a URL that allows others to access your Amazon S3
buckets through an Amazon S3 Multi-Region Access Point. When you create a presigned URL, you associate it with a
specific object action, such as an S3 upload (`PutObject`) or an S3 download
(`GetObject`). You can share the presigned URL, and anyone with access to
it can perform the action embedded in the URL as if they were the original signing
user.

Presigned URLs have an expiration date. When the expiration time is reached, the URL
will no longer work.

Before you use S3 Multi-Region Access Points with presigned URLs, check the [AWS SDK
compatibility](../../../sdkref/latest/guide/feature-s3-mrap.md#s3-mrap-sdk-compat "../../../sdkref/latest/guide/feature-s3-mrap.md#s3-mrap-sdk-compat") with the SigV4A algorithm. Verify that your SDK version
supports SigV4A as the signing implementation that is used to sign the global
AWS Region requests. For more information about using presigned URLs with Amazon S3, see
[Sharing objects by
using presigned URLs](ShareObjectPreSignedURL.md "ShareObjectPreSignedURL.md").

The following examples show how you can use Multi-Region Access Points with presigned URLs. To use these
examples, replace the `user input placeholders`
with your own information.

AWS CLI

```
aws s3 presign arn:aws:s3::`123456789012`:accesspoint/`MultiRegionAccessPoint_alias`/`example-file.txt`
```

SDK for Python

```
import logging
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3',aws_access_key_id='`xxx`',aws_secret_access_key='`xxx`')
s3_client.generate_presigned_url(HttpMethod='`PUT`',ClientMethod="`put_object`", Params={'Bucket':'arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456.mrap`','Key':'`example-file`'})
```

SDK for Java

```
S3Presigner s3Presigner = S3Presigner.builder()
    .credentialsProvider(StsAssumeRoleCredentialsProvider.builder()
        .refreshRequest(assumeRole)
        .stsClient(stsClient)
        .build())
    .build();

GetObjectRequest getObjectRequest = GetObjectRequest.builder()
    .bucket("arn:aws:s3::`123456789012`:accesspoint/`abcdef0123456`.mrap")
    .key("`example-file`")
    .build();

GetObjectPresignRequest preSignedReq = GetObjectPresignRequest.builder()
    .getObjectRequest(getObjectRequest)
    .signatureDuration(Duration.ofMinutes(`10`))
    .build();

PresignedGetObjectRequest presignedGetObjectRequest = s3Presigner.presignGetObject(preSignedReq);
```

###### Note

To use SigV4A with temporary security credentials—for example, when using IAM
roles—make sure that you request the temporary credentials from a Regional endpoint
in AWS Security Token Service (AWS STS), instead of a global endpoint. If you use the global endpoint
for AWS STS (`sts.amazonaws.com`), AWS STS will generate temporary credentials
from a global endpoint, which isn't supported by Sig4A. As a result, you'll get an
error. To resolve this issue, use any of the listed [Regional endpoints for AWS STS](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#id_credentials_region-endpoints "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#id_credentials_region-endpoints").

## Use a bucket that's configured with Requester Pays with Multi-Region Access Points

If an S3 bucket that is associated with your Multi-Region Access Points is [configured to use
Requester Pays](RequesterPaysExamples.md "RequesterPaysExamples.md"), the requester will pay for the
bucket
request, the download, and any Multi-Region Access Points related costs. For more
information, see [Amazon S3
pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

Here's an example of a data plane request to a Multi-Region Access Point that is connected to a Requester
Pays bucket.

AWS CLI
To download objects from a Multi-Region Access Point that is connected to a Requester Pays
bucket, you must specify `--request-payer requester` as part of
your [get-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html") request. You must also specify
the name of the file in the bucket and the location where the downloaded
file should be stored.

```
aws s3api get-object --bucket `MultiRegionAccessPoint_ARN` --request-payer requester --key `example-file-in-bucket`.txt `example-location-of-downloaded-file`.txt
```

SDK for Java
To download objects from a Multi-Region Access Point that is connected to a Requester Pays
bucket, you must specify the `RequestPayer.REQUESTER` as part of
your `GetObject` request. You must also specify the name of the file in the
bucket, as well as the location where it should be stored.

```
GetObjectResponse getObjectResponse = s3Client.getObject(GetObjectRequest.builder()
    .key("`example-file.txt`")
    .bucket("arn:aws:s3::
`123456789012`:accesspoint/`abcdef0123456`.mrap")
    .requestPayer(RequestPayer.REQUESTER)
    .build()
).response();
```
