# Downloading a file using an S3 access point

The following `get-object` example command shows how you can
use the AWS CLI to download a file through an access point. You must include an outfile, which
is a file name for the downloaded object.

The example requests the file `my-image.jpg`
through the access point `my-ontap-ap` and saves the
downloaded file as `download.jpg`.

```
`$` `aws s3api get-object --key `my-image.jpg` --bucket `my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b`-ext-s3alias `download.jpg``
`{
 "AcceptRanges": "bytes",
 "LastModified": "Mon, 14 Oct 2024 17:01:48 GMT",
 "ContentLength": 141756,
 "ETag": "\"00751974dc146b76404bb7290f8f51bb-1\"",
 "ContentType": "binary/octet-stream",
 "ServerSideEncryption": "SSE_FSX",
 "Metadata": {},
 "StorageClass": "FSX_ONTAP"
}`
```

You can also use the REST API to download an object through an access point. For more information, see [GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md") in the _Amazon Simple Storage Service API Reference_.
