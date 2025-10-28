# Referencing access points with ARNs, access point aliases, or virtual-hosted-style URIs

After you create an access point attached to an FSx for OpenZFS volume, you can access your data via the AWS CLI and S3 API, as well as S3-compatible
AWSand third-party services and applications. When referring to an access point in an AWS service or application you can use the Amazon Resource Name (ARN),
the access point alias, or virtual-hosted–style URI.

###### Topics

- [Access point ARNs](#access-point-arns "#access-point-arns")
- [Access point aliases](#access-point-aliases "#access-point-aliases")
- [Virtual-hosted–style URI](#virtual-hosted-style-uri "#virtual-hosted-style-uri")

## Access point ARNs

Access points have Amazon Resource Names (ARNs). Access point ARNs are similar to S3 bucket ARNs, but they are explicitly
typed and encode the access point's AWS Region and the AWS account ID of the access point's owner. For more information about ARNs, see
[Identify AWS resources with Amazon Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md")
in the _AWS Identity and Access Management User Guide_.

Access point ARNs have the following format:

```
arn:aws::s3:`region`:`account-id`:accesspoint/`resource`
```

`arn:aws:s3:us-west-2:777777777777:accesspoint/`test``
 represents the access point named`test`, owned by account 777777777777 in the
 Region `us-west-2`.

ARNs for objects and files accessed through an access point use the following format:

```
arn:aws::s3:`region`:`account-id`:accesspoint/`access-point-name`/object/`resource`
```

`arn:aws:s3:us-west-2:111122223333:accesspoint/`test`/object/`lions.jpg``
 represents the file`lions.jpg`, accessed through the access point named `test`, owned by account 111122223333
 in the Region `us-west-2`.

For more information about access point ARNs, see
[Access point ARNs](../../../AmazonS3/latest/userguide/access-points-naming.md#access-points-arns "../../../AmazonS3/latest/userguide/access-points-naming.md#access-points-arns")
in the _Amazon Simple Storage Service User Guide_.

## Access point aliases

When you create an access point, Amazon S3 automatically generates an access point alias that you can use anywhere you can use S3 bucket names
to access data.

An access point alias cannot be changed. For an access point attached to an FSx for OpenZFS volume,
the access point alias consists of the following parts:

```
`access point prefix-metadata-`ext-s3alias
```

The following shows the ARN and access point alias for an S3 access point attached to an FSx for OpenZFS volume, returned as part of the response to a
`describe-s3-access-point-attachments` FSx CLI command. The access point in this example
is named `my-openzfs-ap`.

```
...
        "S3AccessPoint": {
            "ResourceARN": "arn:aws:s3:us-east-1:111122223333:accesspoint/my-openzfs-ap",
            "Alias": "my-openzfs-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias",
...
```

###### Note

The `-ext-s3alias` suffix is reserved for the aliases of S3 access points attached to an FSx for OpenZFS volume,
and can't be used for access point names.

You can use the access point alias instead of an Amazon S3 access point ARN in some S3 data plane operations. For a list of the supported operations,
see [Access point compatibility](access-points-object-api-support.md "access-points-object-api-support.md").

For a full set of access point alias limitations, see
[Access point alias limitations](../../../AmazonS3/latest/userguide/access-points-naming.md#access-points-alias "../../../AmazonS3/latest/userguide/access-points-naming.md#access-points-alias") in the _Amazon Simple Storage Service User Guide_.

## Virtual-hosted–style URI

Access points only support virtual-host-style addressing. In a virtual-hosted–style URI, the access point name, AWS account, and AWS Region is
part of the domain name in the URL. To view the S3 URI for an access point attached to an FSx for OpenZFS volume, in the access point details page under
**S3 access point details**, choose the access point name listed for **S3 access point**. This takes you to the access point
details page in the Amazon S3 console. You can find the **S3 URI** under **Properties**.

For more information, see
[Virtual-hosted–style URI](../../../AmazonS3/latest/userguide/access-points-naming.md#accessing-a-bucket-through-s3-access-point "../../../AmazonS3/latest/userguide/access-points-naming.md#accessing-a-bucket-through-s3-access-point")
in the _Amazon Simple Storage Service User Guide_.
