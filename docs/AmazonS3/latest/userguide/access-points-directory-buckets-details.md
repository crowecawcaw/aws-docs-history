# View details for your access points for directory buckets

This section explains how to view details for your access point for directory buckets using the AWS Management Console, AWS CLI, AWS SDKs, or REST API.

View details of an access point for directory buckets to see the following information about the access point and the associated directory bucket:

- Properties:
  - Directory bucket name
  - Directory bucket owner account ID
  - AWS Region
  - Directory bucket location type
  - Directory bucket location name
  - Creation date of access point
  - Network origin
  - VPC ID
  - S3 URI
  - Access point ARN
  - Access point alias

- Permissions:
  - IAM external access analyzer findings
  - Access point scope
  - Access point policy

###### To view details for your access point in your AWS account

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the Region that you want to
   list access points for.
3. In the navigation pane on the left side of the console, choose
   **Access points for directory buckets**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage.
6. Choose the **Properties** tab or the **Permissions** tab.
   The following `get-access-point` example command shows how you can use
   the AWS CLI to view details for your access point.

The following command lists details for the access point ``my-access-point`--`zoneID`--xa-s3`for AWS account`111122223333`.

```
aws s3control get-access-point --name ``my-access-point``--`zoneID`--xa-s3 --account-id `111122223333`
```

###### Example of output of `get-access-point` command

```

{
    "Name": "example-access-point--zoneID--xa-s3",
    "Bucket": "`amzn-s3-demo-bucket`--`zone-id`--x-s3",
    "NetworkOrigin": "Internet",
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
    },
    "CreationDate": "2025-04-23T18:26:22.146000+00:00",
    "Alias": "example-access-point--zoneID--xa-s3",
    "AccessPointArn": "arn:aws:s3express:region:111122223333:accesspoint/example-access-point--zoneID--xa-s3",
    "BucketAccountId": "296805379465"
}

```

For more information and examples, see [get-access-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point.html") in the
_AWS CLI Command Reference_.

You can use the REST API to view details for your access point. For more information, see [GetAccessPoint](../API/API_control_GetAccessPoint.md "../API/API_control_GetAccessPoint.md") in the _Amazon Simple Storage Service API Reference_.

You can use the AWS SDKs to view details of your access points. For more information, see [list of supported SDKs](../API/API_control_GetAccessPoint.md#API_control_GetAccessPoint_SeeAlso "../API/API_control_GetAccessPoint.md#API_control_GetAccessPoint_SeeAlso") in the Amazon Simple Storage Service API Reference.
