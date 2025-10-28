# Uploading a file using an S3 access point

The following `put-object` example command shows how you can
use the AWS CLI to upload a file through an access point. You must include an outfile, which
is a file name for the uploaded object.

The example uploads the file `my-new-image.jpg`
through the access point `my-openzfs-ap` and saves the
uploaded file as `my-new-image.jpg`.

```
`$` `aws s3api put-object --bucket `my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b`-ext-s3alias --key `my-new-image.jpg` --body `my-new-image.jpg``
```

You can also use the REST API to upload an object through an access point. For more information, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") in the _Amazon Simple Storage Service API Reference_.
