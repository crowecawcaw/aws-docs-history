# Get a reference to a
 key value store

To work with the key value stores programmatically, you need the `ETag`
 and the name of the key value store. 

To get both values, you can use the AWS Command Line Interface (AWS CLI) or the CloudFront API.


AWS CLI
###### To get the key value store reference

1. To return a list of key value stores, run the following
 command Find the name of the key value store that you want to
 change.



```
aws cloudfront list-key-value-stores
```
2. From the response, find the name of the key value store that
 you want.


**Response**



```
{
    "KeyValueStoreList": {
        "Items": [
            {
                "Name": "keyvaluestore3",
                "Id": "37435e19-c205-4271-9e5c-example3",
                "ARN": "arn:aws:cloudfront::123456789012:key-value-store/37435e19-c205-4271-9e5c-example3",
                "Status": "READY",
                "LastModifiedTime": "2024-05-08T14:50:18.876000+00:00"
            },
            {
                "Name": "keyvaluestore2",
                "Id": "47970d59-6408-474d-b850-example2",
                "ARN": "arn:aws:cloudfront::123456789012:key-value-store/47970d59-6408-474d-b850-example2",
                "Status": "READY",
                "LastModifiedTime": "2024-05-30T21:06:22.113000+00:00"
            },
            {
                "Name": "keyvaluestore1",
                "Id": "8aa76c93-3198-462c-aaf6-example",
                "ARN": "arn:aws:cloudfront::123456789012:key-value-store/8aa76c93-3198-462c-aaf6-example",
                "Status": "READY",
                "LastModifiedTime": "2024-08-06T22:19:30.510000+00:00"
            }
        ]
    }
}
```
3. Run the following command to return the `ETag` for
 the specified key value store.



```
aws cloudfront describe-key-value-store \
    --name=keyvaluestore1
```

**Response**



```
{
    "ETag": "E3UN6WX5RRO2AG",
    "KeyValueStore": {
        "Name": "keyvaluestore1",
        "Id": "8aa76c93-3198-462c-aaf6-example",
        "Comment": "This is an example KVS",
        "ARN": "arn:aws:cloudfront::123456789012:key-value-store/8aa76c93-3198-462c-aaf6-example",
        "Status": "READY",
        "LastModifiedTime": "2024-08-06T22:19:30.510000+00:00"
    }
}
```


API
###### To get the key value store reference

1. Use the [CloudFront
 ListKeyValueStores](../../../cloudfront/latest/APIReference/API_ListKeyValueStores.md "../../../cloudfront/latest/APIReference/API_ListKeyValueStores.md") API operation to return a
 list of key value stores. Find the name of the key value store
 that you want to change.
2. Use the [CloudFront
 DescribeKeyValueStore](../../../cloudfront/latest/APIReference/API_DescribeKeyValueStore.md "../../../cloudfront/latest/APIReference/API_DescribeKeyValueStore.md") API operation and
 specify the name of the key value store that you returned from
 the previous step.


The response includes a UUID, the ARN of the key value store, and the
 `ETag` of the key value store.


* An `ETag`, such as `E3UN6WX5RRO2AG`
* The UUID is 128 bits, such as
 `8aa76c93-3198-462c-aaf6-example`
* The ARN includes the AWS account number, the constant
 `key-value-store`, and the UUID, like the following
 example:


`arn:aws:cloudfront::123456789012:key-value-store/8aa76c93-3198-462c-aaf6-example`
For more information about the `DescribeKeyValueStore` operation, see
 [About the CloudFront KeyValueStore](kvs-with-functions-kvp.md#kvs-with-functions-api-describe "kvs-with-functions-kvp.md#kvs-with-functions-api-describe").
