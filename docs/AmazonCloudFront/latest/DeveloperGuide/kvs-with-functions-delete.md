# Delete a key value store

You can delete your key value store by using the Amazon CloudFront console or API.

Console

###### To delete a key value store

1. Sign in to the AWS Management Console and open the
   **Functions** page in the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions").
2. Choose the function name.
3. Under the **Associated KeyValueStore**
   section, verify if a key value store is associated with the
   function. If it is, remove the association by choosing
   **Disassociate KeyValueStore** and then
   choose **Remove association**.
4. In the navigation pane, choose the
   **Functions** page and then choose the
   **KeyValueStores** tab.
5. Select the key value store that you want to delete and then
   choose **Delete**.

AWS CLI

###### To delete a key value store

1. Get the `ETag` and the name of the key value stores.
   For more information, see [Get a reference to a key value store](kvs-with-functions-get-reference.md "kvs-with-functions-get-reference.md").
2. Verify if the key value stores is associated with a function.
   If it is, remove the association. For more information on both
   these steps, see [Update functions](update-function.md "update-function.md").
3. After you have the name and `ETag` of the
   key value store and it's no longer associated with a function,
   you can delete it.

Run the following command to delete the specified
key value store.

```
aws cloudfront delete-key-value-store \
    --name=keyvaluestore1 \
    --if-match=E3UN6WX5RRO2AG
```

API

###### To delete a key value store

1. Get the `ETag` and the name of the key value stores.
   For more information, see [Get a reference to a key value store](kvs-with-functions-get-reference.md "kvs-with-functions-get-reference.md").
2. Verify if the key value stores is associated with a function.
   If it is, remove the association. For more information on both
   these steps, see [Update functions](update-function.md "update-function.md").
3. To delete the key value store, use the CloudFront [DeleteKeyValueStore](../../../cloudfront/latest/APIReference/API_DeleteKeyValueStore.md "../../../cloudfront/latest/APIReference/API_DeleteKeyValueStore.md") API
   operation.
