# Helper methods for key value stores

###### Note

Key value store helper method calls from CloudFront Functions don't trigger an AWS CloudTrail
 data event. These events aren't logged in the CloudTrail event history. For more
 information, see [Logging Amazon CloudFront API calls using AWS CloudTrail](logging_using_cloudtrail.md "logging_using_cloudtrail.md").

This section applies if you use the [CloudFront Key Value
 Store](kvs-with-functions.md "kvs-with-functions.md") to include key values in the function that you create. CloudFront Functions
 has a module that provides three helper methods to read values from the
 key value store.

To use this module in the function code, make sure that you have [associated a key value store](kvs-with-functions-associate.md "kvs-with-functions-associate.md") with the
 function. 

Next, include the following statements in the first lines of the function code:


```
import cf from 'cloudfront';
const kvsHandle = cf.kvs();
```

## `get()` method


Use this method to return the key value for the key name that you specify. 


**Request**



```
get("`key`", `options`);
```


* `key`: The name of the key whose value needs to be
 fetched
* `options`: There is one option, `format`. It ensures
 that the function parses the data correctly. Possible values:




	+ `string`: (Default) UTF8 encoded
	+ `json`
	+ `bytes`: Raw binary data buffer

**Request example**



```
const value = await kvsHandle.get("myFunctionKey", { format: "string"});
```

**Response**


The response is a `promise` that resolves to a value in the format
 requested by using `options`. By default, the value is returned as a
 string.


### Error handling


The `get()` method will return an error when the key that you
 requested doesn't exist in the associated key value store. To manage this use
 case, you can add a `try` and `catch` block to your
 code.


###### Warning

Using promise combinators (for example, `Promise.all`,
 `Promise.any`, and promise chain methods (for example,
 `then` and `catch`) can require high function memory
 usage. If your function exceeds the [maximum
 function memory](cloudfront-limits.md#limits-functions "cloudfront-limits.md#limits-functions") quota, it will fail to execute. To avoid this error,
 we recommend that you use the `await` syntax sequentially or in loops
 to request multiple values.

**Example**


```
var value1 = await kvs.get('key1');
var value2 = await kvs.get('key2');
```
Currently, using promise combinators to get multiple values won't improve
 performance, such as the following example.


```
var values = await Promise.all([kvs.get('key1'), kvs.get('key2'),]);
```

## `exists()`
 method


Use this method to identify whether or not the key exists in the
 key value store.


**Request**



```
exists("`key`");
```

**Request example**



```
const exist = await kvsHandle.exists("myFunctionkey");
```

**Response**


The response is a `promise` that returns a Boolean (`true`
 or `false`). This value specifies whether or not the key exists in the
 key value store.


## `meta()` method


Use this method to return metadata about the key value store.


**Request**



```
meta();
```

**Request example**



```
const meta = await kvsHandle.meta();
```

**Response**


The response is a `promise` that resolves to an object with the
 following properties:



* `creationDateTime`: The date and time that the key value store
 was created, in ISO 8601 format.
* `lastUpdatedDateTime`: The date and time that the key value
 store was last synced from the source, in ISO 8601 format. The value doesn't
 include the propagation time to the edge.
* `keyCount`: The total number of keys in the KVS after the last
 sync from the source.

**Response example**



```
{keyCount:3,creationDateTime:2023-11-30T23:07:55.765Z,lastUpdatedDateTime:2023-12-15T03:57:52.411Z}
```
