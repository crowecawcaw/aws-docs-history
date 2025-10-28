# Refreshing Amazon S3 bucket object

cache

As your NFS or SMB client performs file system operations, your gateway maintains an
inventory of the objects in the Amazon S3 object cache associated with your file share. Your
gateway uses this cached inventory to reduce the latency and frequency of Amazon S3 requests.
This operation does not import files into the S3 File Gateway cache storage. It only updates
the cached inventory to reflect changes in the inventory of the objects in the Amazon S3
object cache.

To refresh the S3 bucket object cache for your file share, select the method that best
fits your use case from the following list, then complete the corresponding procedure
below.

###### Note

Regardless of the method you use, listing a directory for the first time
initializes it, which causes the gateway to list the directory's meta data contents
from Amazon S3. The time required to initialize a directory is proportional to the number
of entries in that directory.

###### Topics

- [Configure an automated cache
  refresh schedule using the Storage Gateway console](#auto-refresh-console-procedure "#auto-refresh-console-procedure")
- [Configure an automated cache refresh
  schedule using AWS Lambda with an Amazon CloudWatch rule](#auto-refresh-lambda-procedure "#auto-refresh-lambda-procedure")
- [Perform a manual cache refresh
  using the Storage Gateway console](#manual-refresh-console-procedure "#manual-refresh-console-procedure")
- [Perform a manual cache refresh using
  the Storage Gateway API](#manual-refresh-api-procedure "#manual-refresh-api-procedure")

## Configure an automated cache

refresh schedule using the Storage Gateway console

The following procedure configures an automatic cache refresh schedule based on a
Time To Live (TTL) value that you specify. Before you configure a TTL-based cache
refresh schedule, consider the following:

- TTL is measured as the length of time since the last cache refresh for a
  given directory.
- TTL-based cache refresh occurs only when a given directory is accessed
  after the specified TTL period has expired.
- The refresh is non-recursive. It occurs only on the specific directories
  being accessed.
- The refresh incurs Amazon S3 API costs only on directories that have not been
  synchronized since TTL expiration.
  - Directories are only synchronized if they are accessed by NFS or
    SMB activity.
  - Synchronization does not occur more frequently than the TTL period
    that you specify.

- Configuring TTL-based cache refresh is recommended only if you frequently
  update the contents of your Amazon S3 bucket directly, outside of the workflow
  between the gateway and the Amazon S3 bucket.
- NFS and SMB operations that access directories with expired TTLs will be
  blocked while the gateway refreshes the contents of the directory.

###### Note

Because cache refresh can block directory access operations, we
recommend configuring the longest TTL period that is practical for your
deployment.

###### To configure an automated cache refresh schedule using the Storage Gateway

console

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **File shares**.
3. Choose the file share for which you want to configure the refresh
   schedule.
4. For **Actions**, choose **Edit file share
   settings**.
5. For **Automated cache refresh from S3 after**, select the
   check box and set the time in days, hours, and minutes to refresh the file
   share's cache using Time To Live (TTL). TTL is the length of time since the
   last refresh after which access to the directory would cause the
   File Gateway to first refresh that directory's contents from the Amazon S3
   bucket.
6. Choose **Save changes**.

## Configure an automated cache refresh

schedule using AWS Lambda with an Amazon CloudWatch rule

###### To configure an automated cache refresh schedule using AWS Lambda with an

Amazon CloudWatch rule

1. Identify the S3 bucket used by the S3 File Gateway.
2. Check that the _Event_ section is blank. It populates
   automatically later.
3. Create an IAM role, and allow Trust Relationship for Lambda
   `lambda.amazonaws.com`.
4. Use the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "StorageGatewayPermissions",
 "Effect": "Allow",
 "Action": "storagegateway:RefreshCache",
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchLogsPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:CreateLogGroup",
 "logs:PutLogEvents"
 ],
 "Resource": "*"
 }
 ]
}`

```

5. Create a Lambda function from the Lambda console.
6. Use the following function for your Lambda task.

```
import json
import boto3
client = boto3.client('storagegateway')
def lambda_handler(event, context):
    print(event)
    response = client.refresh_cache(
        FileShareARN='`arn:aws:storagegateway:ap-southeast-2:672406474878:share/share-E51FBS9C`'
    )
    print(response)
    return 'Your FileShare cache has been refreshed'
```

7. For **Execution role**, choose the IAM role you
   created.
8. Optional: add a trigger for Amazon S3 and select the event
   **ObjectCreated** or
   **ObjectRemoved**.

###### Note

`RefreshCache` needs to complete one process before
starting another. When you create or delete many objects in a bucket,
performance might degrade. Therefore, we recommend against using S3
triggers. Instead, use the Amazon CloudWatch rule described following. 9. Create a CloudWatch rule on the CloudWatch console and add a schedule. Generally, we
recommend a _fixed rate_ of 30 minutes. However, you can
use 1–2 hours on large S3 bucket. 10. Add a new trigger for CloudWatch events and choose the rule you just
created. 11. Save your Lambda configuration. Choose **Test**. 12. Choose **S3 PUT** and customize the test to your
requirements. 13. The test should succeed. If not, modify the JSON to your requirements and
retest. 14. Open the Amazon S3 console, and verify that the event you created and the Lambda
function ARN are present. 15. Upload an object to your S3 bucket using the Amazon S3 console or the
AWS CLI.

The CloudWatch console generates a CloudWatch output similar to the following.

```
{
    u'Records': [
        {u'eventVersion': u'2.0', u'eventTime': u'2018-09-10T01:03:59.217Z', u'requestParameters': {u'sourceIPAddress': u'MY-IP-ADDRESS'},
        u's3': {u'configurationId': u'95a51e1c-999f-485a-b994-9f830f84769f', u'object': {u'sequencer': u'00549CC2BF34D47AED', u'key': u'new/filename.jpeg'},
        u'bucket': {u'arn': u'arn:aws:s3:::amzn-s3-demo-bucket', u'name': u'MY-GATEWAY-NAME', u'ownerIdentity': {u'principalId': u'A3OKNBZ72HVPP9'}}, u's3SchemaVersion': u'1.0'},
        u'responseElements': {u'x-amz-id-2': u'76tiugjhvjfyriugiug87t890nefevbck0iA3rPU9I/s4NY9uXwtRL75tCyxasgsdgfsq+IhvAg5M=', u'x-amz-request-id': u'651C2D4101D31593'},
        u'awsRegion': u'MY-REGION', u'eventName': u'ObjectCreated:PUT', u'userIdentity': {u'principalId': u'AWS:AROAI5LQR5JHFHDFHDFHJ:MY-USERNAME'}, u'eventSource': u'aws:s3'}
    ]
}
```

The Lambda invocation gives you output similar to the following.

```
{
    u'FileShareARN': u'arn:aws:storagegateway:REGION:ACCOUNT-ID:share/MY-SHARE-ID',
        'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '6663236a-b495-11e8-946a-bf44f413b71f',
            'HTTPHeaders': {'x-amzn-requestid': '6663236a-b495-11e8-946a-bf44f413b71f', 'date': 'Mon, 10 Sep 2018 01:03:59 GMT',
                'content-length': '90', 'content-type': 'application/x-amz-json-1.1'
        }
    }
}
```

Your NFS share mounted on your client will reflect this update.

###### Note

For caches updating large object creation or deletion in large buckets
with millions of objects, updates may take hours. 16. Delete your object manually using the Amazon S3 console or AWS CLI. 17. View the NFS share mounted on your client. Verify that your object is gone
(because your cache refreshed). 18. Check your CloudWatch logs to see the log of your deletion with the event
`ObjectRemoved:Delete`.

```
{
    u'account': u'MY-ACCOUNT-ID', u'region': u'MY-REGION', u'detail': {}, u'detail-type': u'Scheduled Event', u'source': u'aws.events',
    u'version': u'0', u'time': u'2018-09-10T03:42:06Z', u'id':  u'6468ef77-4db8-0200-82f0-04e16a8c2bdb',
    u'resources': [u'arn:aws:events:REGION:MY-ACCOUNT-ID:rule/FGw-RefreshCache-CW']
}
```

###### Note

For cron jobs or scheduled tasks, your CloudWatch log event is
`u'detail-type': u'Scheduled Event'`.

## Perform a manual cache refresh

using the Storage Gateway console

###### To perform a manual cache refresh using the Storage Gateway console

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **File shares**, and then choose the file share
   for which you want to perform the refresh.
3. For **Actions**, choose **Refresh
   cache**.

The time that the refresh process takes depends on the number of objects
cached on the gateway and the number of objects that were added to or
removed from the S3 bucket.

## Perform a manual cache refresh using

the Storage Gateway API

The following procedure performs a manual cache refresh using the Storage Gateway API.
Before you perform an API-based cache refresh, consider the following:

- You can specify a recursive or non-recursive refresh.
- A recursive refresh is more resource-intensive, and more expensive.
- The refresh incurs Amazon S3 API costs only on directories that you pass as
  arguments in the request, and descendants of those directories if you
  specify a recursive refresh.
- The refresh executes concurrently with other operations while the gateway
  is in use.
  - NFS and SMB operations generally do not become blocked during
    refreshes, unless a refresh is active for the directory being
    accessed by the operation.
  - The gateway is unable to determine whether current cache contents
    are stale, and uses its current contents for NFS and SMB operations
    regardless of freshness.
  - Because a cache refresh utilizes gateway virtual hardware
    resources, gateway performance might be negatively impacted while
    the refresh is in progress.

- Performing API-based cache refresh is recommended only if you update the
  contents of your Amazon S3 bucket directly, outside of the workflow between the
  gateway and the Amazon S3 bucket.

###### Note

If you know the specific directories where you are updating Amazon S3
content outside of the gateway workflow, we recommend specifying these
directories in your API-based refresh request to reduce Amazon S3 API costs
and gateway performance impact.

###### To perform a manual cache refresh using the Storage Gateway API

- Send an HTTP POST request to invoke the `RefreshCache`
  operation with your desired parameters through the Storage Gateway API. For more
  information, see [RefreshCache](../../../storagegateway/latest/APIReference/API_RefreshCache.md "../../../storagegateway/latest/APIReference/API_RefreshCache.md") in the _AWS Storage Gateway API
  Reference_.

###### Note

Sending the `RefreshCache` request only initiates the cache
refresh operation. When the cache refresh completes, it doesn't
necessarily mean that the file refresh is complete. To determine that
the file refresh operation is complete before you check for new files on
the gateway file share, use the `refresh-complete`
notification. To do this, you can subscribe to be notified through an
Amazon CloudWatch event. For more information, see [Getting notified about file operations](monitoring-file-gateway.md#get-notification "monitoring-file-gateway.md#get-notification").
