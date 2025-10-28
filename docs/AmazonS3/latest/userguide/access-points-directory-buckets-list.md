# List your access points for directory buckets

This section explains how to list access points for a directory bucket using the AWS Management Console, AWS Command Line Interface (AWS CLI), REST API, or AWS SDKs.

###### To list access points in your AWS account

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the Region that you want to
   list access points for.
3. In the navigation pane on the left side of the console, choose
   **Access points for directory buckets**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage.
   The following `list-access-points-for-directory-buckets` example command shows how you can use
   the AWS CLI to list the access points owned by an AWS account and associated with a directory bucket.

The following command lists access points for AWS account `111122223333` that are attached to bucket ``amzn-s3-demo-bucket`--`zone-id`--x-s3`.

```
aws s3control list-access-points-for-directory-buckets --account-id `111122223333` --directory-bucket ``amzn-s3-demo-bucket`--`zone-id`--x-s3`
```

For more information and examples, see [list-access-points-for-directory-buckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points-for-directory-buckets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points-for-directory-buckets.html") in the AWS CLI Command Reference.

The following example shows how you can use the REST API to list your access points.

```

GET /v20180820/directoryaccesspoint?directoryBucket=``amzn-s3-demo-bucket`--`zone-id`--x-s3`
&maxResults=`maxResults` HTTP/1.1
Host: s3express-control.`region`.amazonaws.com
x-amz-account-id: `111122223333`

```

###### Example of `ListAccessPointsForDirectoryBuckets` response

```

HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListDirectoryAccessPointsResult>
    <AccessPointList>
        <AccessPoint>
            <AccessPointArn>arn:aws:s3express:region:111122223333:accesspoint/example-access-point--zoneID--xa-s3</AccessPointArn>
            <Alias>example-access-point--zoneID--xa-s3</Alias>
            <Bucket>`amzn-s3-demo-bucket`--`zone-id`--x-s3</Bucket>
            <BucketAccountId>111122223333</BucketAccountId>
            <Name>example-access-point--zoneID--xa-s3</Name>
            <NetworkOrigin>VPC</NetworkOrigin>
            <VpcConfiguration>
                <VpcId>VPC-1</VpcId>
            </VpcConfiguration>
        </AccessPoint>
    </AccessPointList>
</ListDirectoryAccessPointsResult>

```

You can use the AWS SDKs to list your access points. For more information, see [list of supported SDKs](../API/API_control_ListAccessPointsForDirectoryBuckets.md#API_control_ListAccessPointsForDirectoryBuckets_SeeAlso "../API/API_control_ListAccessPointsForDirectoryBuckets.md#API_control_ListAccessPointsForDirectoryBuckets_SeeAlso") in the Amazon Simple Storage Service API Reference.
