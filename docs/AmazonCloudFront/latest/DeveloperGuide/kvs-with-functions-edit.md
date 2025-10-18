# Update a key value store

When you update a key value store, you can change the key-value pairs, or change
 the association between the key value store and the function.


Console
###### To update a key value store

1. Sign in to the AWS Management Console and open the
 **Functions** page in the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions").
2. Choose the **KeyValueStores** tab.
3. Select the key value store that you want to update. 


	* To update the key-value pairs, choose
	 **Edit** in the **Key value
	 pairs** section. You can add or delete any
	 key-value pairs. You can also change the value for an
	 existing key-value pair. When you're finished, choose
	 **Save changes**.
	* To update the association for this key value store,
	 choose **Go to functions**. For more
	 information, see [Associate a key value store with a
	 function](kvs-with-functions-associate.md "kvs-with-functions-associate.md").


AWS CLI
###### To update a key value store

1. **Change the key-value pairs**
 – You can add more key-value pairs, delete one or more
 key-value pairs, and change the value of an existing key-value
 pair. For more information, see [Work with key value data](kvs-with-functions-kvp.md "kvs-with-functions-kvp.md").
2. **Change the function association for the
 key value store**  – To update the function
 the association for the key value store, see [Associate a key value store with a
 function](kvs-with-functions-associate.md "kvs-with-functions-associate.md"). 


###### Tip

You will need the ARN of the key value store. For more
 information, see [Get a reference to a
 key value store](kvs-with-functions-get-reference.md "kvs-with-functions-get-reference.md").


API
###### To update a key value store

1. **Change the key-value pairs**
 – You can add more key-value pairs, delete one or more
 key-value pairs, and change the value of an existing key-value
 pair. For more information, see [Work with key value data](kvs-with-functions-kvp.md "kvs-with-functions-kvp.md").
2. **Change the function association for the
 key value store** – To update the function
 association for the key value store, use the [UpdateFunction](../../../cloudfront/latest/APIReference/API_UpdateFunction.md "../../../cloudfront/latest/APIReference/API_UpdateFunction.md") API operation. For more information,
 see [Update functions](update-function.md "update-function.md"). 


###### Tip

You will need the ARN of the key value store. For more
 information, see [Get a reference to a
 key value store](kvs-with-functions-get-reference.md "kvs-with-functions-get-reference.md").
