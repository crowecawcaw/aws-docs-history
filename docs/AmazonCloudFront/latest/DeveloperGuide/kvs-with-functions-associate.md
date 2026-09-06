

# Associate a key value store with a function
<a name="kvs-with-functions-associate"></a>

After you create your key value store, you can update your function to associate it with your key value store. You must make this association to use the key-value pairs from that store in that function. The following rules apply:
+ A function can have only one key value store
+ You can associate the same key value store with multiple functions

------
#### [ Console ]

**To associate a key value store with a function**

1. Sign in to the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions) and choose the **Functions** page.

1. Choose the function name.

1. Go to the **Associate KeyValueStore** section and choose **Associate existing KeyValueStore**.

1. Select the key value store that contains the key-value pairs in the function, and then choose **Associate KeyValueStore**.

   CloudFront immediately associates the store with the function. You don't need to save the function.

1. To specify a different key value store, choose **Update associated KeyValueStore**, select another key value store name, and then choose **Associate KeyValueStore**.

For more information, see [Update functions](update-function.md).

------
#### [ AWS CLI ]

**To associate a key value store with a function**
+ Run the following command to update the `{{MaxAge}}` function and associate a key value store resource.

  ```
  aws cloudfront update-function \
      --name MaxAge \
      --function-config '{"Comment":"Max Age 2 years","Runtime":"cloudfront-js-2.0","KeyValueStoreAssociations":{"Quantity":1,"Items":[{"KeyValueStoreARN":"arn:aws:cloudfront::123456789012:key-value-store/8aa76c93-3198-462c-aaf6-example"}]}}' \
      --function-code fileb://function-max-age-v1.js \
      --if-match ETVABCEXAMPLE
  ```
+ To associate a key value store with a function, specify the `KeyValueStoreAssociations` parameter and the key value store ARN. 
+ To change the association, specify another key value store ARN. 
+ To remove the association, remove the `KeyValueStoreAssociations` parameter. 

For more information, see [Update functions](update-function.md).

------
#### [ API ]

**To associate a key value store with a function**
+ Use the [UpdateFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateFunction.html) API operation. For more information, see [Update functions](update-function.md).

------

**Notes**  
If you modify a key value store without changing the key-value pairs, or if you only modify the key-value pairs in the key value store, you don't need to associate the key value store again. You also don't need to republish the function.  
However, we recommend that you test the function to verify that it works as expected. For more information, see [Test functions](test-function.md).
You can view all the functions that use specific key value stores. On the CloudFront console, choose the key value store details page. 