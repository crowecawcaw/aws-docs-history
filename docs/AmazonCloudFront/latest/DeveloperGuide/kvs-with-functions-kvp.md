

# Work with key value data
<a name="kvs-with-functions-kvp"></a>

This topic describes how to add key-value pairs to an existing key value store. To include key-value pairs when you initially create the key value stores, see [Create a key value store](kvs-with-functions-create.md).

**Topics**
+ [Work with key-value pairs (console)](#kvs-with-functions-kvp-using-console)
+ [About the CloudFront KeyValueStore](#kvs-with-functions-api-describe)
+ [Work with key-value pairs (AWS CLI)](#work-with-kvs-cli-keys)
+ [Work with key-value pairs (API)](#kvs-with-functions-kvp-using-api)

## Work with key-value pairs (console)
<a name="kvs-with-functions-kvp-using-console"></a>

You can use the CloudFront console to work with your key-value pairs.

**To work with key-value pairs**

1. Sign in to the AWS Management Console and open the **Functions** page in the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions).

1. Choose the **KeyValueStores** tab. 

1. Select the key value store that you want to change.

1. In the **Key value pairs** section, choose **Edit**. 

1. You can add a key-value pair, delete a key-value pair, or change the value for an existing key-value pair. 

1. When you're finished, choose **Save changes**.

## About the CloudFront KeyValueStore
<a name="kvs-with-functions-api-describe"></a>

**Tip**  
The CloudFront KeyValueStore API is a global service that uses Signature Version 4A (SigV4A) for authentication. Using temporary credentials with SigV4A requires version 2 session tokens. For more information, see [Using temporary credentials with the CloudFront KeyValueStore API](cloudfront-function-restrictions.md#regional-endpoint-for-key-value-store).

If you're using the AWS Command Line Interface (AWS CLI) or your own code to call the CloudFront KeyValueStore API, see the following sections. 

When you work with a key value store and its key-value pairs, the service that you call depends on your use case:
+ To work with key-value pairs in an *existing* key value store, use the CloudFront KeyValueStore service. 
+ To include key-value pairs in the key value store when you *initially* create the key value store, use the CloudFront service.

Both the CloudFront API and the CloudFront KeyValueStore API have a `DescribeKeyValueStore` operation. You call them for different reasons. To understand the differences, see the following table.


|  | CloudFront DescribeKeyValueStore API | CloudFront KeyValueStore DescribeKeyValueStore API | 
| --- | --- | --- | 
| Data about the key value store | Returns data, such as the status and the date that the key value store itself was last modified. | Returns data about the *contents* of the storage resource – the key-value pairs in the store, and the size of the contents. | 
| Data that identifies the key value store | Returns an `ETag`, the UUID, and the ARN of the key value store. | Returns an `ETag` and the ARN of the key value store. | 

**Notes**  
Each DescribeKeyValueStore operation returns a *different * `ETag`. The `ETags` aren't interchangeable.
When you call an API operation to complete an action, you must specify the `ETag` from the appropriate API. For example, in the CloudFront KeyValueStore [ DeleteKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_DeleteKey.html) operation, you specify the `ETag` that you returned from the CloudFront KeyValueStore [DescribeKeyValueStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_DescribeKeyValueStore.html) operation.
When you invoke your CloudFront Functions by using CloudFront KeyValueStore, the values in the key value store aren't updated or changed during the invocation of the function. Updates are processed in between invocations of a function.

## Work with key-value pairs (AWS CLI)
<a name="work-with-kvs-cli-keys"></a>

You can run the following AWS Command Line Interface commands for CloudFront KeyValueStore.

**Contents**
+ [List key-value pairs](#kvs-cli-list-keys)
+ [Get key-value pairs](#kvs-cli-get-keys)
+ [Describe a key value store](#kvs-cli-describe-keys)
+ [Create a key-value pair](#kvs-cli-create-keys)
+ [Delete a key-value pair](#kvs-cli-delete-keys)
+ [Update key-value pairs](#kvs-cli-update-key)

### List key-value pairs
<a name="kvs-cli-list-keys"></a>

To list key-value pairs in your key value store, run the following command.

```
aws cloudfront-keyvaluestore list-keys \
    --kvs-arn=arn:aws:cloudfront::123456789012:key-value-store/37435e19-c205-4271-9e5c-example
```

**Response**

```
{
    "Items": [
        {
            "Key": "key1",
            "Value": "value1"
        }
    ]
}
```

### Get key-value pairs
<a name="kvs-cli-get-keys"></a>

To get a key-value pair in your key value store, run the following command.

```
aws cloudfront-keyvaluestore get-key \
    --key=key1 \
    --kvs-arn=arn:aws:cloudfront::123456789012:key-value-store/37435e19-c205-4271-9e5c-example
```

**Response**

```
{
    "Key": "key1",
    "Value": "value1",
    "ItemCount": 1,
    "TotalSizeInBytes": 11
}
```

### Describe a key value store
<a name="kvs-cli-describe-keys"></a>

To describe a key value store, run the following command.

```
aws cloudfront-keyvaluestore describe-key-value-store \
    --kvs-arn=arn:aws:cloudfront::123456789012:key-value-store/37435e19-c205-4271-9e5c-example
```

**Response**

```
{
    "ETag": "KV1F83G8C2ARO7P",
    "ItemCount": 1,
    "TotalSizeInBytes": 11,
    "KvsARN": "arn:aws:cloudfront::123456789012:key-value-store/37435e19-c205-4271-9e5c-example",
    "Created": "2024-05-08T07:48:45.381000-07:00",
    "LastModified": "2024-08-05T13:50:58.843000-07:00",
    "Status": "READY"
}
```

### Create a key-value pair
<a name="kvs-cli-create-keys"></a>

To create a key-value pair in your key value store, run the following command.

```
aws cloudfront-keyvaluestore put-key \
    --if-match=KV1PA6795UKMFR9 \
    --key=key2 \
    --value=value2 \
    --kvs-arn=arn:aws:cloudfront::123456789012:key-value-store/37435e19-c205-4271-9e5c-example
```

**Response**

```
{
    "ETag": "KV13V1IB3VIYZZH",
    "ItemCount": 3,
    "TotalSizeInBytes": 31
}
```

### Delete a key-value pair
<a name="kvs-cli-delete-keys"></a>

To delete a key-value pair, run the following command.

```
aws cloudfront-keyvaluestore delete-key \
    --if-match=KV13V1IB3VIYZZH \
    --key=key1 \
    --kvs-arn=arn:aws:cloudfront::123456789012:key-value-store/37435e19-c205-4271-9e5c-example
```

**Output**

```
{
    "ETag": "KV1VC38T7YXB528",
    "ItemCount": 2,
    "TotalSizeInBytes": 22
}
```

### Update key-value pairs
<a name="kvs-cli-update-key"></a>

You can use the `update-keys` command to update more than one key-value pair. For example, to delete an existing key-value pair and create another one, run the following command.

```
aws cloudfront-keyvaluestore update-keys \
    --if-match=KV2EUQ1WTGCTBG2 \
    --kvs-arn=arn:aws:cloudfront::123456789012:key-value-store/37435e19-c205-4271-9e5c-example \
    --deletes '[{"Key":"key2"}]' \
    --puts '[{"Key":"key3","Value":"value3"}]'
```

**Response**

```
{
    "ETag": "KV3AEGXETSR30VB",
    "ItemCount": 3,
    "TotalSizeInBytes": 28
}
```

## Work with key-value pairs (API)
<a name="kvs-with-functions-kvp-using-api"></a>

Follow this section to work with your key-value pairs programatically. 

**Contents**
+ [Get a reference to a key value store](#kvs-with-functions-api-ref)
+ [Change key-value pairs in a key value store](#kvs-with-functions-api-actions)
+ [Example code for CloudFront KeyValueStore](#example-code-key-value-store)

### Get a reference to a key value store
<a name="kvs-with-functions-api-ref"></a>

When you use the CloudFront KeyValueStore API to call a write operation, you need to specify the ARN and the `ETag` of the key value store. To get this data, do the following:

**To get a reference to a key value store**

1. Use the [CloudFront ListKeyValueStores](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListKeyValueStores.html) API operation to get a list of key value stores. Find the key value store that you want to change. 

1. Use the [CloudFrontKeyValueStore DescribeKeyValueStore API operation](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_DescribeKeyValueStore.html) and specify the key value store from the previous step.

   The response includes the ARN and the `ETag` of the key value store. 
   + The ARN includes the AWS account number, the constant `key-value-store`, and the UUID, such as the following example:

     `arn:aws:cloudfront::123456789012:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
   + An `ETag` that looks like the following example: 

     `ETVABCEXAMPLE2`

### Change key-value pairs in a key value store
<a name="kvs-with-functions-api-actions"></a>

You can specify the key value store that contains the key-value pair that you want to update. 

See the following CloudFront KeyValueStore API operations:
+ [CloudFrontKeyValueStore DeleteKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_DeleteKey.html) – Deletes a key-value pair
+ [CloudFrontKeyValueStore GetKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_GetKey.html) – Returns a key-value pair
+ [CloudFrontKeyValueStore ListKeys](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_ListKeys.html) – Returns a list of key-value pairs 
+ [CloudFrontKeyValueStore PutKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_PutKey.html) – You can perform the following tasks:
  + Create a key-value pair in one key value store by specifying a new key name and value.
  + Set a different value in an existing key-value pair by specifying an existing key name, and a new key value.
+ [CloudFrontKeyValueStore UpdateKeys](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_UpdateKeys.html) – You can perform one or more of the following actions in one all-or-nothing operation:
  + Delete one or more key-value pairs
  + Create one or more new key-value pairs
  + Set a different value in one or more existing key-value pairs

### Example code for CloudFront KeyValueStore
<a name="example-code-key-value-store"></a>

**Example**  
The following code shows you how to call the `DescribeKeyValueStore` API operation for a key value store.  

```
const {
  CloudFrontKeyValueStoreClient,
  DescribeKeyValueStoreCommand,
} = require("@aws-sdk/client-cloudfront-keyvaluestore");

require("@aws-sdk/signature-v4-crt");

(async () => {
  try {
    const client = new CloudFrontKeyValueStoreClient({
      region: "us-east-1"
    });
    const input = {
      KvsARN: "arn:aws:cloudfront::123456789012:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    };
    const command = new DescribeKeyValueStoreCommand(input);

    const response = await client.send(command);
  } catch (e) {
    console.log(e);
  }
})();
```