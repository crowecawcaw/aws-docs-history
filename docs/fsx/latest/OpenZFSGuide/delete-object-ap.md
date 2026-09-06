

# Deleting a file using an S3 access point
<a name="delete-object-ap"></a>

The following `delete-object` example command shows how you can use the AWS CLI to delete a file through an access point.

```
$ aws s3api delete-object --bucket {{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias --key {{my-image.jpg}} 
```

You can also use the REST API to delete an object through an access point. For more information, see [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) in the *Amazon Simple Storage Service API Reference*.