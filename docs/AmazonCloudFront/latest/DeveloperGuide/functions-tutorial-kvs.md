# Tutorial: Create a CloudFront function that includes key
 values

This tutorial shows you how to include key values with CloudFront function. Key values are part
 of a key-value pair. You include the name (from the key-value pair) in the function code.
 When the function runs, CloudFront replaces the name with the value. 

Key-value pairs are variables that are stored in a key value store. When you use a key in
 your function (instead of hard-coded values), your function is more flexible. You can change
 the value of the key without having to deploy code changes. Key-value pairs can also reduce
 the size of your function. For more information, see [Amazon CloudFront KeyValueStore](kvs-with-functions.md "kvs-with-functions.md").

###### Contents

* [Prerequisites](functions-tutorial-kvs.md#functions-kvs-tutorial-prerequisites "functions-tutorial-kvs.md#functions-kvs-tutorial-prerequisites")
* [Create the key value store](functions-tutorial-kvs.md#functions-kvs-tutorial-kvs-step "functions-tutorial-kvs.md#functions-kvs-tutorial-kvs-step")
* [Add key-value pairs to the key value
 store](functions-tutorial-kvs.md#add-key-value-pairs-to-store "functions-tutorial-kvs.md#add-key-value-pairs-to-store")
* [Associate the key value store
 with the function](functions-tutorial-kvs.md#functions-kvs-tutorial-functions-step "functions-tutorial-kvs.md#functions-kvs-tutorial-functions-step")
* [Test and publish the function
 code](functions-tutorial-kvs.md#test-and-publish-function-code "functions-tutorial-kvs.md#test-and-publish-function-code")

## Prerequisites


If you're new to CloudFront Functions functions and the key value store, we recommend that
 you follow the tutorial in [Tutorial: Create a simple function with
 CloudFront Functions](functions-tutorial.md "functions-tutorial.md").


After you complete that tutorial, you can follow this tutorial to extend the function
 that you created. For this tutorial, we recommend that you create the key value store
 first. 


## Create the key value store


First, create the key value store to use for your function.


###### To create the key value store

1. Plan the key-value pairs you want to include in the function. Make a note of
 key names. The key-value pairs that you want to use in a function must be in a
 single key value store.
2. Decide about the order of work. There are two ways to proceed:




	* Create a key value store, and add key-value pairs to the store. Then
	 create (or modify) the function and incorporate the key names.
	* Or, create (or modify) the function and incorporate the key names you
	 want to use. Then create a key value store, and add the key-value
	 pairs.
3. Sign in to the AWS Management Console and open the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
4. In the navigation pane, choose **Functions**, and then choose
 the **KeyValueStores** tab.
5. Choose **Create KeyValueStore** and enter the following
 fields:




	* Enter a name and (optional) description for the store.
	* Leave **S3 URI** blank. In this tutorial you will
	 enter the key-value pairs manually.
6. Choose **Create**. The details page for the new key value
 store appears. This page includes a **Key value pairs** section
 that is currently empty.

## Add key-value pairs to the key value
 store


Next, manually add a list of key-value pairs to the key value store that you
 previously created.


###### To add key-value pairs to the key value store

1. In the **Key value pairs** section, choose **Add key
 value pairs**.
2. Choose **Add pair** and then enter a key and value. Choose
 the check mark to confirm your changes and repeat this step to add more.
3. When you're finished, choose **Save changes** to save the
 key-value pairs in the key value store. On the confirmation dialog, choose
 **Done**.

You now have a key value store that contains a group of key-value pairs. 



## Associate the key value store
 with the function


You have now created the key value store. And you have created or modified a function
 that includes the key names from the key value store. You can now associate the key
 value store and the function. You create that association from within the function. 


###### To associate the key value store with the function

1. In the navigation pane, choose **Functions**. The
 **Functions** tab appears on top, by default.
2. Choose the function name and in the **Associated
 KeyValueStore** section, choose **Associate Existing
 KeyValueStore**.
3. Select the key value store and choose **Associate
 KeyValueStore**.

###### Note

You can associate only one key value store with each function.


## Test and publish the function
 code


After you associate the key value store with your function, you can test and publish
 the function code. You should always test the function code every time you modify it,
 including when you do the following:



* Associate a key value store with the function.
* Modify the function and its key value store to include a new key-value
 pair.
* Change the value of a key-value pair.

###### To test and publish the function code

1. For information about how to test a function, see [Test functions](test-function.md "test-function.md"). Make sure that you choose to test the function in
 the `DEVELOPMENT` stage.
2. Publish the function when you're ready to use the function (with the new or
 revised key value pairs) in a `LIVE` environment. 


When you publish, CloudFront copies the version of the function from the
 `DEVELOPMENT` stage over to the live stage. The function has the
 new code and is associated with the key value store. (There is no need to
 perform the association again, in the live stage.)


For information about how to publish the function, see [Publish functions](publish-function.md "publish-function.md").
