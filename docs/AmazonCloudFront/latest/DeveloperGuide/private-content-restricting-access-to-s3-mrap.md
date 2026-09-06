

# Restrict access to an Amazon S3 Multi-Region Access Point origin
<a name="private-content-restricting-access-to-s3-mrap"></a>

You can use origin access control (OAC) to restrict access to an Amazon S3 Multi-Region Access Point origin. S3 Multi-Region Access Points provide a global endpoint that routes requests to the closest S3 bucket based on network latency.

**Note**  
OAC with S3 Multi-Region Access Points is not supported for MRAP endpoints backed by buckets in opt-in Regions. Requests routed to a bucket in an opt-in Region will fail. All buckets associated with the Multi-Region Access Point must be in Regions that are enabled by default.

For information about using OAC with a standard Amazon S3 bucket origin, see [Restrict access to an Amazon S3 origin](private-content-restricting-access-to-s3.md).

## Prerequisites
<a name="oac-prerequisites-s3-mrap"></a>

Before you create and set up OAC, you must have a CloudFront distribution with an Amazon S3 Multi-Region Access Point origin. The origin domain name must use the S3 Multi-Region Access Point hostname format:

`{{multi-region-access-point-alias}}.accesspoint.s3-global.amazonaws.com`

For more information about creating an S3 Multi-Region Access Point, see [Creating Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html) in the *Amazon Simple Storage Service User Guide*.

## Grant CloudFront permission to access the S3 Multi-Region Access Point
<a name="oac-permission-to-access-s3-mrap"></a>

Update the Multi-Region Access Point policy to allow the CloudFront service principal (`cloudfront.amazonaws.com`) to access the Multi-Region Access Point. Use a `Condition` element in the policy to allow CloudFront to access the Multi-Region Access Point only when the request is on behalf of the CloudFront distribution that contains the origin.

For information about adding or modifying a Multi-Region Access Point policy, see [Multi-Region Access Point policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointPermissions.html) in the *Amazon Simple Storage Service User Guide*.

**Example Multi-Region Access Point policy for CloudFront OAC**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCloudFrontOACAccess",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3::{{111122223333}}:accesspoint/{{Multi-Region-Access-Point-Alias}}.mrap/object/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:cloudfront::{{111122223333}}:distribution/{{CloudFront distribution ID}}"
                }
            }
        }
    ]
}
```

## Grant CloudFront permission to access the underlying S3 buckets
<a name="oac-permission-to-access-s3-mrap-buckets"></a>

In addition to the Multi-Region Access Point policy, you must also grant CloudFront permission to access each of the underlying S3 buckets that are associated with the Multi-Region Access Point. You can do this in one of two ways:

**Important**  
You must add this bucket policy to every S3 bucket that is associated with the Multi-Region Access Point. If any bucket is missing the policy, CloudFront requests routed to that bucket will be denied.

### Option 1: Grant access only to CloudFront
<a name="oac-s3-mrap-bucket-option1"></a>

Add a bucket policy to each S3 bucket that allows the CloudFront service principal to access the bucket. Use this option when you also need to allow direct access to the bucket from other sources.

**Example S3 bucket policy for an underlying bucket**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCloudFrontOACAccessViaMRAP",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket-us-east-1}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:cloudfront::{{111122223333}}:distribution/{{CloudFront distribution ID}}"
                }
            }
        }
    ]
}
```

### Option 2: Delegate full bucket access to the Multi-Region Access Point
<a name="oac-s3-mrap-bucket-option2"></a>

Grant the Multi-Region Access Point full access to each underlying bucket. With this approach, all access to the bucket is controlled by the Multi-Region Access Point policy, which simplifies access management. We recommend this option for use cases that don't require direct access to the bucket.

**Example S3 bucket policy that delegates access to the Multi-Region Access Point**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DelegateAccessToMRAP",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket-us-east-1}}",
                "arn:aws:s3:::{{amzn-s3-demo-bucket-us-east-1}}/*"
            ],
            "Condition": {
                "StringEquals": {
                    "s3:DataAccessPointArn": "arn:aws:s3::{{111122223333}}:accesspoint/{{Multi-Region-Access-Point-Alias}}.mrap"
                }
            }
        }
    ]
}
```

For more information, see [Multi-Region Access Point policy example](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointPermissions.html#MultiRegionAccessPointPolicyExamples) in the *Amazon Simple Storage Service User Guide*.

### SSE-KMS
<a name="oac-s3-mrap-sse-kms"></a>

If the objects in the underlying S3 buckets are encrypted using server-side encryption with AWS KMS (SSE-KMS), you must make sure that the CloudFront distribution has permission to use the AWS KMS key. Because S3 Multi-Region Access Points can route requests to buckets in multiple Regions, you must add a statement to the KMS key policy in each Region where an underlying bucket uses SSE-KMS. For information about how to modify a key policy, see [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) in the *AWS Key Management Service Developer Guide*.

**Example KMS key policy statement**  
The following example shows a KMS key policy statement that allows the CloudFront distribution with OAC to access a KMS key for SSE-KMS.  

```
{
    "Sid": "AllowCloudFrontServicePrincipalSSE-KMS",
    "Effect": "Allow",
    "Principal": {
        "Service": "cloudfront.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:SourceArn": "arn:aws:cloudfront::{{111122223333}}:distribution/{{CloudFront distribution ID}}"
        }
    }
}
```

**Important**  
You must add this key policy statement to the KMS key in every Region where an underlying S3 bucket uses SSE-KMS encryption.

## Create the origin access control
<a name="create-oac-s3-mrap"></a>

To create an origin access control (OAC), you can use the AWS Management Console, CloudFormation, the AWS CLI, or the CloudFront API.

**Note**  
Lambda@Edge origin triggers (both origin request and origin response) are incompatible with origins that use a SigV4a OAC, whether the origin is accessed directly or through an origin group.

------
#### [ Console ]

**To create an origin access control**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Origin access**.

1. Choose **Create control setting**.

1. On the **Create control setting** form, do the following:

   1. In the **Details** pane, enter a **Name** and (optionally) a **Description** for the origin access control.

   1. In the **Settings** pane, we recommend that you leave the default setting (**Sign requests (recommended)**). For more information, see [Advanced settings for origin access control](private-content-restricting-access-to-s3.md#oac-advanced-settings-s3).

1. Choose **S3** from the **Origin type** dropdown and select the **Use SigV4a signing protocol** option.

1. Choose **Create**.

   After the OAC is created, make note of the **Name**. You need this in the following procedure.

**To add an origin access control to an S3 Multi-Region Access Point origin in a distribution**

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. Choose a distribution with an S3 Multi-Region Access Point origin that you want to add the OAC to, then choose the **Origins** tab.

1. Select the S3 Multi-Region Access Point origin that you want to add the OAC to, then choose **Edit**.

1. For **Origin access**, choose **Origin access control settings (recommended)**.

1. From the **Origin access control** dropdown menu, choose the OAC that you want to use.

1. Choose **Save changes**.

The distribution starts deploying to all of the CloudFront edge locations. When an edge location receives the new configuration, it signs all requests that it sends to the S3 Multi-Region Access Point origin.

------
#### [ CLI ]

Use the **create-origin-access-control** command:

```
aws cloudfront create-origin-access-control \
    --origin-access-control-config '{
        "Name": "my-s3-mrap-oac",
        "Description": "OAC for S3 Multi-Region Access Point",
        "SigningProtocol": "sigv4a",
        "SigningBehavior": "always",
        "OriginAccessControlOriginType": "s3"
    }'
```

------
#### [ CloudFormation ]

Specify the following values in the `OriginAccessControlConfig`:
+ `SigningProtocol`: `sigv4a`
+ `SigningBehavior`: `always`, `never`, or `no-override`
+ `OriginAccessControlOriginType`: `s3`

**Example CloudFormation template**  

```
Type: AWS::CloudFront::OriginAccessControl
Properties:
  OriginAccessControlConfig:
    Description: An optional description for the origin access control
    Name: my-s3-mrap-oac
    OriginAccessControlOriginType: s3
    SigningBehavior: always
    SigningProtocol: sigv4a
```

------

## Signing behavior
<a name="oac-signing-behavior-s3-mrap"></a>

The signing behavior options for S3 Multi-Region Access Point origins are the same as those for regular Amazon S3 bucket origins. For more information, see [Advanced settings for origin access control](private-content-restricting-access-to-s3.md#oac-advanced-settings-s3) in *Restrict access to an Amazon S3 origin*.