# Tagging a file using an S3 access point

The following `put-object-tagging` example command shows how you can
use the AWS CLI to add a tag-set through an access point. Each tag is a key-value pair.
For more information, see
[Categorizing your storage using tags](../../../AmazonS3/latest/userguide/object-tagging.md "../../../AmazonS3/latest/userguide/object-tagging.md")
in the _Amazon Simple Storage Service User Guide_.

The example adds a tag-set to the existing file `my-image.jpg`
using the access point `my-ontap-ap`.

```
`$` `aws s3api put-object-tagging --bucket `my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b`-ext-s3alias --key `my-image.jpg` --tagging TagSet=[{Key="`finance`",Value="`true`"}]`
```

You can also use the REST API to add a tag-set to an object through an access point. For more information, see [PutObjectTagging](../../../AmazonS3/latest/API/API_PutObjectTagging.md "../../../AmazonS3/latest/API/API_PutObjectTagging.md") in the _Amazon Simple Storage Service API Reference_.
