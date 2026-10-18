

# Deploying Web Function code from Amazon S3
<a name="web-functions-code-s3"></a>

You provide Lambda Web Function code as a .zip deployment package in an Amazon S3 bucket. This is the only way to supply code for a Web Function. When you create a Web Function or revision, specify the object in the `s3Object` field, which is nested under `codeConfig` inside the request's `buildConfig`. In `s3Object`, include the bucket, key, and an optional versionId. Lambda references your code directly from your bucket. Because Lambda pins each revision to a specific object version, your deployments are reproducible. You can reuse a single deployment package across accounts and AWS Regions.

**Topics**
+ [Prerequisites](#web-functions-code-s3-requirements)
+ [Required permissions](#web-functions-code-s3-permissions)
+ [Creating a Web Function with code from Amazon S3](#web-functions-code-s3-creating)
+ [Object lifecycle](#web-functions-code-s3-lifecycle)
+ [Multi-Region deployments](#web-functions-code-s3-multi-region)

## Prerequisites
<a name="web-functions-code-s3-requirements"></a>

Before you deploy Web Function code from Amazon S3, make sure that your bucket and deployment package meet the following requirements:

S3 versioning  
The bucket must have [S3 versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) enabled. Lambda uses object versions to track which version of your code a revision uses.

Version ID  
The `versionId` parameter is optional in the request. If you omit it, Lambda uses the latest version of the object at creation time. Either way, Lambda pins the revision to a specific object version.

Maximum deployment package size  
512 MB (unzipped).

Entry file  
The deployment package must contain your application's entry file. By default, the runtime loads `index.js` at the root of the package. To use a different entry file, set the `AWS_LAMBDA_NODEJS_ENTRYPOINT` environment variable on the revision to the file's path relative to the package root. After loading the entry file, the runtime waits for your HTTP server to start listening at the host and port from the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable. If the runtime cannot resolve the entry file, or the server never starts listening, initialization fails and requests to the endpoint fail.  
Lambda does not verify that your server starts listening when it creates or updates an endpoint to use the revision. The revision and endpoint can still show `Active` in these cases. After each deployment, send a test request and check your application logs.

Bucket location  
The bucket can be in a different AWS account and in a different AWS Region from the Web Function. The bucket must be in the same AWS partition as the Web Function. The bucket can't be in an opt-in Region (a Region that is not enabled by default). If either condition isn't met, Lambda rejects the request. Cross-Region object retrieval incurs additional Amazon S3 data transfer costs. For more information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

## Required permissions
<a name="web-functions-code-s3-permissions"></a>

To deploy Web Function code from Amazon S3, you must configure permissions for both the calling identity and the Lambda service principal.

### Caller permissions
<a name="web-functions-code-s3-caller-permissions"></a>

To create the Web Function or revision, your IAM identity needs the following permissions on the S3 object:
+ `s3:GetObject`
+ `s3:GetObjectVersion`

For cross-account buckets, the bucket policy must also grant the calling identity access to the object.

### Bucket policy for Lambda
<a name="web-functions-code-s3-bucket-policy"></a>

The bucket policy must grant the Lambda service principal (`lambda.amazonaws.com`) `s3:GetObject` and `s3:GetObjectVersion` permissions. Scope the policy with an `aws:SourceArn` condition that matches the revision ARN pattern. Use `ArnLike` with a wildcard for the revision ID, because Lambda generates the revision ID when you create the revision.

If the object is encrypted with an AWS KMS key (SSE-KMS), the key policy must also allow `lambda.amazonaws.com` to call `kms:Decrypt` on that key. Lambda checks the service principal's access when you create the revision and rejects the request if access is missing.

The following example bucket policy grants Lambda access to read your deployment packages for any revision of the specified Web Function.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowLambdaWebFunctionCodeAccess",
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::{{my-bucket}}/*",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/revision/*"
                }
            }
        }
    ]
}
```

To limit access to the key prefix that holds your deployment packages, change the `Resource` value to `arn:aws:s3:::{{my-bucket}}/{{my-prefix}}/*`, where {{my-bucket}} is your bucket name and {{my-prefix}} is the key prefix. Keep the `/*` at the end of the prefix. Don't change the `revision/*` wildcard in `aws:SourceArn`.

## Creating a Web Function with code from Amazon S3
<a name="web-functions-code-s3-creating"></a>

You specify your S3 deployment package in the `codeConfig` section of `buildConfig`. The following procedures show how to create a Web Function and how to create a new revision using the AWS CLI.

**To create a Web Function with code from Amazon S3 (AWS CLI)**
+ Run the following command to create a Web Function that references your .zip deployment package in Amazon S3.

  ```
  aws lambda-web create-web-function \
      --function-name {{my-web-app}} \
      --revision-config '{
        "buildConfig": {
          "codeConfig": {
            "s3Object": { "bucket": "{{my-bucket}}", "key": "{{my-app.zip}}" }
          },
          "runtimeConfig": { "runtime": "nodejs24.x" }
        },
        "serviceConfig": {
          "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}"
        }
      }' \
      --endpoint-config '{
        "endpointName": "{{my-endpoint}}",
        "endpointType": "HomeRegion",
        "authType": "ApplicationManaged"
      }'
  ```

  When you omit `versionId`, Lambda uses the latest version of the object at creation time.

**To create a new revision with a specific object version (AWS CLI)**
+ Run the following command to create a new revision that uses a specific version of your deployment package.

  ```
  aws lambda-web create-web-function-revision \
      --function-name {{my-web-app}} \
      --build-config '{
        "codeConfig": {
          "s3Object": {
            "bucket": "{{my-bucket}}",
            "key": "{{my-app.zip}}",
            "versionId": "{{abc123def456}}"
          }
        },
        "runtimeConfig": { "runtime": "nodejs24.x" }
      }' \
      --service-config '{
        "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}"
      }'
  ```

  By specifying `versionId`, you pin the revision to an exact version of the object rather than the latest version.

## Object lifecycle
<a name="web-functions-code-s3-lifecycle"></a>

**Do not delete S3 objects or remove Lambda access for active revisions**  
Lambda references your code from your Amazon S3 bucket. If you delete the S3 object that a revision uses, or the specific object version that the revision uses, the revision moves to the `Failed` state when Lambda next verifies access to the object, and then can no longer serve traffic. Keep the object versions for all revisions that you are still using.  
Removing the Lambda service principal's access to the bucket has the same effect. If you modify the bucket policy to deny or remove `s3:GetObject` and `s3:GetObjectVersion` permissions for `lambda.amazonaws.com`, existing revisions that reference objects in that bucket move to the `Failed` state. Maintain both the objects and the Lambda service principal's read access for as long as any revision references those objects.  
The `Failed` state is permanent. Restoring the deleted object or the bucket permissions does not return a revision to the `Active` state. To recover, create a new revision that references an available object version, and then update your endpoints' revision weights to route traffic to it. For deployment patterns, see [Deployment patterns](web-functions-deployment.md).

Lambda does not automatically shift traffic away from a `Failed` revision. Requests that an endpoint routes to a `Failed` revision are rejected with HTTP status code 409 and a `lambda-web-error-type` response header of `Platform.RevisionNotActive`. If the endpoint weights traffic across multiple revisions, only the share of requests routed to the `Failed` revision is affected; requests routed to healthy revisions are served normally. To stop the failures, update the endpoint's revision weights to remove the `Failed` revision.

Overwriting the object with a new upload creates a new S3 version. This does not affect existing revisions: when you create a revision, Lambda resolves and pins the exact object version, even when you omit `versionId`. However, if you delete an old object version that a revision references, that revision moves to the `Failed` state. Uploading a replacement object does not help, because the replacement is a new version with a different version ID.

## Multi-Region deployments
<a name="web-functions-code-s3-multi-region"></a>

For Web Functions with `MultiRegion` or `PerRegion` endpoints, Lambda reads your source object from the bucket that you specify, in whichever Region the bucket is in. Lambda then replicates the prepared code artifact that it derives from that object to the other Regions. You do not need to copy your deployment package to buckets in other Regions. For more information about what Lambda replicates, see [What Lambda replicates](web-functions-endpoint-replication.md#web-functions-endpoint-replication-what).