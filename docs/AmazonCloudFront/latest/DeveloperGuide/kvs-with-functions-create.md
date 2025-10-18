# Create a key value store

You can create a key value store and its key-value pairs at the same time. You can
 also create an empty key value store now and then add the key-value pairs later. 

###### Note

If you specify your data source from an Amazon S3 bucket, you must have the
 `s3:GetObject` and `s3:GetBucketLocation` permissions
 to that bucket. If you don't have these permissions, CloudFront can't successfully
 create your key value store.

Decide if you want to add key-value pairs at the same time when you create the
 key value store. You can import your key-value pairs by using the CloudFront console, CloudFront
 API, or AWS SDKs. However, you can only import your file of key-value pairs when
 you *initially* create the key value store. 

To create a file of key-value pairs, see [File format for key-value
 pairs](kvs-with-functions-create-s3-kvp.md "kvs-with-functions-create-s3-kvp.md"). 


Console
###### To create a key value store

1. Sign in to the AWS Management Console and open the
 **Functions** page in the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions").
2. Choose the **KeyValueStores** tab, and then
 choose **Create KeyValueStore**.
3. Enter a name and optional description for the key value store.
4. Complete **S3 URI**: 




	* If you have a file of key-value pairs, enter the path
	 to the Amazon S3 bucket where you stored the file.
	* Leave this field blank if you plan to enter the
	 key-value pairs manually.
5. Choose **Create**. The key value store now
 exists.


The details page for the new key value store appears. The
 information on the page includes the ID and the ARN of the key
 value store. 




	* The ID is a random string of characters that is unique
	 in your AWS account.
	* The ARN has this syntax:
	
	
	`AWS account``:key-value-store/``the
	 key value stores ID`
6. Look at the **Key value pairs** section. If
 you imported a file, this section shows some key-value pairs.
 You can do the following:




	* If you imported a file, you can also add more values
	 manually.
	* If you didn't import a file from an Amazon S3 bucket, and
	 if you want to add key-value pairs now, you can complete
	 the next step.
	* You can skip this step and add the key-value pairs
	 later.
7. To add the pairs now:


	1. Choose **Add key-value pairs**.
	2. Choose **Add pair** and enter a name
	 and value. Repeat this step to add more pairs.
	3. When you're finished, choose **Save
	 changes** to save all the key-value pairs
	 in the key value store. On the dialog box that appears,
	 choose **Done**.
8. To associate the key value store with a function now, complete
 the **Associated functions** section. For more
 information, see [Create functions](create-function.md "create-function.md") or [Update functions](update-function.md "update-function.md"). 


You can also associate the function later, either from this
 key value store details page, or from the function's details
 page.


AWS CLI
###### To create a key value store

* Run the following command to create a key value store and
 import the key-value pairs from an Amazon S3 bucket.



```
aws cloudfront create-key-value-store \
    --name=`keyvaluestore1` \
    --comment="This is my key value store file" \
    --import-source=SourceType=S3,SourceARN=arn:aws:s3:::`amzn-s3-demo-bucket1`/`kvs-input`.json
```

**Response**



```
{
    "ETag": "ETVABCEXAMPLE",
    "Location": "https://cloudfront.amazonaws.com/2020-05-31/key-value-store/arn:aws:cloudfront::123456789012:key-value-store/8aa76c93-3198-462c-aaf6-example",
    "KeyValueStore": {
        "Name": "keyvaluestore1",
        "Id": "8aa76c93-3198-462c-aaf6-example",
        "Comment": "This is my key value store file",
        "ARN": "arn:aws:cloudfront::123456789012:key-value-store/8aa76c93-3198-462c-aaf6-example",
        "Status": "PROVISIONING",
        "LastModifiedTime": "2024-08-06T22:19:10.813000+00:00"
    }
}
```


API

###### To create a key value store


1. Use the [CloudFront
 CreateKeyValueStore](../../../cloudfront/latest/APIReference/API_CreateKeyValueStore.md "../../../cloudfront/latest/APIReference/API_CreateKeyValueStore.md") operation. The
 operation takes several parameters:




	* A `name` of the key value store.
	* A `comment` parameter that includes a
	 comment.
	* An `import-source` parameter that lets you
	 import key-value pairs from a file that is stored in an
	 Amazon S3 bucket. You can import from a file only when you
	 first create the key value store. For information about
	 the file structure, see [File format for key-value
	 pairs](kvs-with-functions-create-s3-kvp.md "kvs-with-functions-create-s3-kvp.md").

The operation response includes the following information:



* The values passed in the request, including the name that you
 assigned.
* Data such as the creation time.
* An `ETag` (for example,
 `ETVABCEXAMPLE`), the ARN that includes the name of
 the key value store (for example,
 `arn:aws:cloudfront::123456789012:key-value-store/keyvaluestore1`). 


You will use some combination of the `ETag`, the
 ARN, and the name to work with the key value store
 programmatically.



## Key value store statuses


When you create a key value store, the data store can have the following status
 values.




| Value | Description |
| --- | --- |
| **Provisioning** | The key value store was created and CloudFront is processing the data source that you specified. |
| **Ready** | The key value store was created and CloudFront successfully processed the data source that you specified. |
| **Import failed** | CloudFront wasn't able to process the data source that you specified. This status can appear if your file format isn't valid or that it exceeds the size limit. For more information, see [File format for key-value pairs](kvs-with-functions-create-s3-kvp.md "kvs-with-functions-create-s3-kvp.md"). |
