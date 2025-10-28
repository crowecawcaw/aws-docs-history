# View details for your access point for general purpose buckets

This section explains how to view details for your access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.

###### To view details for your access point in your AWS account

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the Region that you want to
   list access points for.
3. In the navigation pane on the left side of the console, choose
   **Access Points**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage or use.
6. Select the **Properties** tab to view the access point
   data source, account ID, AWS Region, creation date, network origin, S3 URI,
   ARN, and access point alias for the selected access point.
7. Select the **Permissions** tab to view the block
   public access settings and access point policy for the selected access point.

###### Note

You can't change any block public access settings for an access point
after the access point is created.
The following `get-access-point` example command shows how you can use
the AWS CLI to view details for your access point.

The following command lists details for the access point `my-access-point` for AWS account `111122223333` attached to S3 bucket `amzn-s3-demo-bucket`.

```
aws s3control get-access-point --name `my-access-point` --account-id `111122223333`
```

Example output:

```
{
    "Name": "`my-access-point`",
    "Bucket": "`amzn-s3-demo-bucket`",
    "NetworkOrigin": "Internet",
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
    },
    "CreationDate": "2016-08-29T22:57:52Z",
    "Alias": "`my-access-point`-u1ny6bhm7moymqx8cuon8o1g4mwikuse2a-s3alias",
    "AccessPointArn": "arn:aws:s3:`AWS Region`:111122223333:accesspoint/`my-access-point`",
    "Endpoints": {
        "ipv4": "s3-accesspoint.`AWS Region`.amazonaws.com",
        "fips": "s3-accesspoint-fips.`AWS Region`.amazonaws.com",
        "fips_dualstack": "s3-accesspoint-fips.dualstack.`AWS Region`.amazonaws.com",
        "dualstack": "s3-accesspoint.dualstack.`AWS Region`.amazonaws.com"
    },
    "BucketAccountId": "111122223333"
}
```

The following command lists details for the access point `example-fsx-ap` for AWS account `444455556666`. This access point is attached to an Amazon FSx file system.

```
aws s3control get-access-point --name `example-fsx-ap` --account-id `444455556666`
```

Example output:

```
{
    "Name": "`example-fsx-ap`",
    "Bucket": "",
    "NetworkOrigin": "Internet",
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
    },
    "CreationDate": "2025-01-19T14:16:12Z",
    "Alias": "`example-fsx-ap`-qrqbyebjtsxorhhaa5exx6r3q7-ext-s3alias",
    "AccessPointArn": "arn:aws:s3:`AWS Region`:444455556666:accesspoint/`example-fsx-ap`",
    "Endpoints": {
        "ipv4": "s3-accesspoint.`AWS Region`.amazonaws.com",
        "fips": "s3-accesspoint-fips.`AWS Region`.amazonaws.com",
        "fips_dualstack": "s3-accesspoint-fips.dualstack.`AWS Region`.amazonaws.com",
        "dualstack": "s3-accesspoint.dualstack.`AWS Region`.amazonaws.com"
    },
    "DataSourceId": "arn:aws::fsx:`AWS Region`:444455556666:`file-system/fs-5432106789abcdef0/volume/vol-0123456789abcdef0`",
    "DataSourceType": "FSX_OPENZFS"
}
```

For more information and examples, see [get-access-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point.html") in the
_AWS CLI Command Reference_.

You can use the REST API to view details for your access point. For more information, see [GetAccessPoint](../API/API_control_GetAccessPoint.md "../API/API_control_GetAccessPoint.md") in the _Amazon Simple Storage Service API Reference_.
