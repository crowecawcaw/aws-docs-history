# Call the API using a REST API client

To provide an end-to-end tutorial, we now show how to call the API using [Postman](https://www.postman.com/ "https://www.postman.com/"), which supports the AWS IAM authorization.

###### To call our Amazon S3 proxy API using Postman

1. Deploy or redeploy the API. Make a note of the base URL of the API that is displayed next to
   **Invoke URL** at the top of the **Stage Editor**.
2. Launch Postman.
3. Choose **Authorization** and then choose `AWS Signature`.
   Enter your IAM user's Access Key ID and Secret Access Key into the **AccessKey** and
   **SecretKey**input fields, respectively. Enter the AWS Region to which your API is
   deployed in the **AWS Region** text box. Enter `execute-api`
   in the **Service Name** input field.

You can create a pair of the keys from the **Security Credentials** tab from your IAM
user account in the IAM Management Console. 4. To add a bucket named `amzn-s3-demo-bucket` to your Amazon S3 account in the `{region}` region:

    1. Choose **PUT** from the drop-down method list and type the method URL (`https://`api-id`.execute-api.`aws-region`.amazonaws.com/`stage`/`folder-name``
    2. Set the `Content-Type` header value as `application/xml`. You may need to delete any existing headers before setting the content
     type.
    3. Choose **Body** menu item and type the following XML fragment as the request
     body:



    ```
    <CreateBucketConfiguration>
      <LocationConstraint>`{region}`</LocationConstraint>
    </CreateBucketConfiguration>
    ```
    4. Choose **Send** to submit the request. If successful, you should receive a `200 OK` response with an empty payload.

5. To add a text file to a bucket, follow the instructions above. If you specify a bucket name of
   `amzn-s3-demo-bucket` for `{folder}` and a file name of
   `Readme.txt` for `{item}` in the URL and provide a text
   string of `Hello, World!` as the file contents (thereby making it the request payload),
   the request becomes

```
PUT /S3/amzn-s3-demo-bucket/Readme.txt HTTP/1.1
Host: 9gn28ca086.execute-api.`{region}`.amazonaws.com
Content-Type: application/xml
X-Amz-Date: 20161015T062647Z
Authorization: AWS4-HMAC-SHA256 Credential=`access-key-id`/20161015/`{region}`/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature=ccadb877bdb0d395ca38cc47e18a0d76bb5eaf17007d11e40bf6fb63d28c705b
Cache-Control: no-cache
Postman-Token: 6135d315-9cc4-8af8-1757-90871d00847e

Hello, World!
```

If everything goes well, you should receive a `200 OK` response with an
empty payload. 6. To get the content of the `Readme.txt` file we just added to the `amzn-s3-demo-bucket` bucket, do a GET request like the following one:

```
GET /S3/amzn-s3-demo-bucket/Readme.txt HTTP/1.1
Host: 9gn28ca086.execute-api.`{region}`.amazonaws.com
Content-Type: application/xml
X-Amz-Date: 20161015T063759Z
Authorization: AWS4-HMAC-SHA256 Credential=`access-key-id`/20161015/`{region}`/execute-api/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=ba09b72b585acf0e578e6ad02555c00e24b420b59025bc7bb8d3f7aed1471339
Cache-Control: no-cache
Postman-Token: d60fcb59-d335-52f7-0025-5bd96928098a
```

If successful, you should receive a `200 OK` response with the `Hello, World!` text string as the payload. 7. To list items in the `amzn-s3-demo-bucket` bucket, submit the following
request:

```
GET /S3/amzn-s3-demo-bucket HTTP/1.1
Host: 9gn28ca086.execute-api.`{region}`.amazonaws.com
Content-Type: application/xml
X-Amz-Date: 20161015T064324Z
Authorization: AWS4-HMAC-SHA256 Credential=`access-key-id`/20161015/`{region}`/execute-api/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=4ac9bd4574a14e01568134fd16814534d9951649d3a22b3b0db9f1f5cd4dd0ac
Cache-Control: no-cache
Postman-Token: 9c43020a-966f-61e1-81af-4c49ad8d1392

```

If successful, you should receive a `200 OK` response with an XML payload
showing a single item in the specified bucket, unless you added more files to the bucket before submitting
this request.

```
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Name>apig-demo-5</Name>
    <Prefix></Prefix>
    <Marker></Marker>
    <MaxKeys>1000</MaxKeys>
    <IsTruncated>false</IsTruncated>
    <Contents>
        <Key>Readme.txt</Key>
        <LastModified>2016-10-15T06:26:48.000Z</LastModified>
        <ETag>"65a8e27d8879283831b664bd8b7f0ad4"</ETag>
        <Size>13</Size>
        <Owner>
            <ID>06e4b09e9d...603addd12ee</ID>
            <DisplayName>`user-name`</DisplayName>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
</ListBucketResult>
```

###### Note

To upload or download an image, you need to set content handling to CONVERT_TO_BINARY.
