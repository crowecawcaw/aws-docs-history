# Creating HealthOmics annotation store versions

###### Important

AWS HealthOmics variant stores and annotation stores are no longer open to new customers.
Existing customers can continue to use the service as normal.
For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

You can create new versions of annotation stores to collect different versions of your
annotation databases. This helps you organize your annotation data, which is updated
regularly.

To create a new version of an existing annotation store, use the

**create-annotation-store-version** API as shown in the following
example.

```
aws omics create-annotation-store-version \
     --name my_annotation_store \
     --version-name my_version
```

You will get the following response with the annotation store version ID, confirming
that a new version of your annotation has been created.

```
{
     "creationTime": "2023-07-21T17:15:49.251040+00:00",
     "id": "3b93cdef69d2",
     "name": "my_annotation_store",
     "reference": {
         "referenceArn": "arn:aws:omics:us-west-2:555555555555:referenceStore/6505293348/reference/5987565360"
     },
     "status": "CREATING",
     "versionName": "my_version"
}
```

To update the description of an annotation store version, you can use
**update-annotation-store-version** to add updates to an annotation store
version.

```
aws omics update-annotation-store-version \
    --name my_annotation_store \
    --version-name my_version \
    --description "New Description"
```

You will receive the following response, confirming that the annotation store version
has been updated.

```
{
     "storeId": "4934045d1c6d",
     "id": "2a3f4a44aa7b",
     "description":"New Description",
     "status": "ACTIVE",
     "name": "my_annotation_store",
     "versionName": "my_version",
     "creation Time": "2023-07-21T17:20:59.380043+00:00",
     "updateTime": "2023-07-21T17:26:17.892034+00:00"
}
```

To view the details of an annotation store version, use **get-annotation-store-version**.

```
aws omics get-annotation-store-version --name my_annotation_store --version-name my_version
```

You will receive a response with the version name, status, and other details.

```
{
     "storeId": "4934045d1c6d",
     "id": "2a3f4a44aa7b",
     "status": "ACTIVE",
     "versionArn": "arn:aws:omics:us-west-2:555555555555:annotationStore/my_annotation_store/version/my_version",
     "name": "my_annotation_store",
     "versionName": "my_version",
     "creationTime": "2023-07-21T17:15:49.251040+00:00",
     "updateTime": "2023-07-21T17:15:56.434223+00:00",
     "statusMessage": "",
     "versionSizeBytes": 0
    }

```

To view all versions of an annotation store, you can use
**list-annotation-store-versions**, as shown in the following
example.

```
aws omics list-annotation-store-versions --name my_annotation_store
```

You will receive a response with the following information

```
{
  "annotationStoreVersions": [
    {
     "storeId": "4934045d1c6d",
     "id": "2a3f4a44aa7b",
     "status": "CREATING",
     "versionArn": "arn:aws:omics:us-west-2:555555555555:annotationStore/my_annotation_store/version/my_version_2",
     "name": "my_annotation_store",
     "versionName": "my_version_2",
     "creation Time": "2023-07-21T17:20:59.380043+00:00",
     "versionSizeBytes": 0
    },
    {
     "storeId": "4934045d1c6d",
     "id": "4934045d1c6d",
     "status": "ACTIVE",
     "versionArn": "arn:aws:omics:us-west-2:555555555555:annotationStore/my_annotation_store/version/my_version_1",
     "name": "my_annotation_store",
     "versionName": "my_version_1",
     "creationTime": "2023-07-21T17:15:49.251040+00:00",
     "updateTime": "2023-07-21T17:15:56.434223+00:00",
     "statusMessage": "",
     "versionSizeBytes": 0
    }
}
```

If you no longer need an annotation store version, you can use
**delete-annotation-store-versions** to delete an annotation store
version, as shown in the following example.

```
aws omics delete-annotation-store-versions --name my_annotation_store --versions my_version
```

If the store version is deleted without errors, you will receive the following response.

```
{
  "errors": []
}
```

If there are errors, you will receive a response with the details of the errors, as shown.

```
{
  "errors": [
    {
      "versionName": "my_version",
      "message": "Version with versionName: my_version was not found."
    }
  ]
}
```

If you try to delete an annotation store version that has an active import job, you will receive a response with an error, as shown.

```
{
  "errors": [
    {
      "versionName": "my_version",
      "message": "version has an inflight import running"
    }
  ]
}
```

In this case, you can force deletion of the annotation store version, as shown in the following example.

```
aws omics delete-annotation-store-versions --name my_annotation_store --versions my_version --force
```
