# Listing files using an S3 access point

The following example lists files through the access point alias
``my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b`-ext-s3alias`
 owned by account ID ``111122223333`in Region
`us-east-2``.

```
`$` `aws s3api list-objects-v2 --bucket `my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b`-ext-s3alias`
`{
 "Contents": [
 {
 "Key": ".hidden-dir-with-data/file.txt",
 "LastModified": "2024-10-29T14:22:05.4359",
 "ETag": "\"88990077ab44cd55ef66aa77-1\"",
 "Size": 18,
 "StorageClass": "FSX_ONTAP"
 },
 {
 "Key": "documents/report.rtf",
 "LastModified": "2024-11-02T10:18:15.6621",
 "ETag": "\"ab12cd34ef56a89219zg6aa77-1\"",
 "Size": 1048576,
 "StorageClass": "FSX_ONTAP"
 },
 ]
}`
```

You can also use the REST API to list your files. For more information, see [ListObjectsV2](../../../AmazonS3/latest/API/API_ListObjectsV2.md "../../../AmazonS3/latest/API/API_ListObjectsV2.md") in the _Amazon Simple Storage Service API Reference_.
