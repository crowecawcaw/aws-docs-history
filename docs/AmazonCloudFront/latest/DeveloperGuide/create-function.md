# Create functions

You create a function in two stages: 


1. Create the function code as JavaScript. You can use the default example from the
 CloudFront console or write your own. For more information, see the following
 topics:




	* [Write function code](writing-function-code.md "writing-function-code.md")
	* [CloudFront Functions event structure](functions-event-structure.md "functions-event-structure.md")
	* [CloudFront Functions examples for CloudFront](service_code_examples_cloudfront_functions_examples.md "service_code_examples_cloudfront_functions_examples.md")
2. Use CloudFront to create the function and include your code. The code exists inside the
 function (not as a reference).

Console
###### To create a function

1. Sign in to the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions") and choose the
 **Functions** page.
2. Choose **Create function**.
3. Enter a function name that is unique within the AWS account, choose
 the JavaScript version, and then choose **Continue**.
 The details page for the new function appears.


###### Note

To use [key-value pairs](kvs-with-functions.md "kvs-with-functions.md")
 in the function, you must choose JavaScript runtime 2.0.
4. In the **Function code** section, choose the
 **Build**  tab and enter your function code. The
 sample code that is included in the **Build** tab
 illustrates the basic syntax for the function code.
5. Choose **Save changes**.
6. If the function code uses key-value pairs, you must associate a key
 value store. 


You can associate the key value store when you first create the
 function. Or, you can associate it later, by [updating the function](update-function.md "update-function.md"). 


To associate a key value store now, follow these steps:


	* Go to the **Associate KeyValueStore** section
	 and choose **Associate existing
	 KeyValueStore**.
	* Select the key value store that contains the key-value pairs
	 in the function, and then choose **Associate
	 KeyValueStore**.CloudFront immediately associates the store with the function. You don't
 need to save the function.


CLI
If you use the CLI, you typically first create the function code in a file,
 and then create the function with the AWS CLI.


###### To create a function

1. Create the function code in a file, and store it in a directory that
 your computer can connect to.
2. Run the command as shown in the example. This example uses the
 `fileb://` notation to pass in the file. It also
 includes line breaks to make the command more readable. 



```
aws cloudfront create-function \
    --name MaxAge \
    --function-config '{"Comment":"Max Age 2 years","Runtime":"cloudfront-js-2.0","KeyValueStoreAssociations":{"Quantity":1,"Items":[{"KeyValueStoreARN":"arn:aws:cloudfront::111122223333:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}]}}' \
    --function-code fileb://function-max-age-v1.js

```

###### Notes



	* `Runtime` – The version of JavaScript.
	 To use [key value
	 pairs](kvs-with-functions.md "kvs-with-functions.md") in the function, you must specify version
	 2.0.
	* `KeyValueStoreAssociations` – If your
	 function uses key-value pairs, you can associate the key
	 value store when you first create the function. Or, you can
	 associate it later, by using `update-function`.
	 The `Quantity` is always `1` because
	 each function can have only one key value store associated
	 with it.
When the command is successful, you see output like the
 following.



```
ETag: ETVABCEXAMPLE
FunctionSummary:
  FunctionConfig:
    Comment: Max Age 2 years
    Runtime: cloudfront-js-2.0
    KeyValueStoreAssociations= \
      {Quantity=1, \
      Items=[{KeyValueStoreARN='arn:aws:cloudfront::111122223333:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111'}]} \
  FunctionMetadata:
    CreatedTime: '2021-04-18T20:38:56.915000+00:00'
    FunctionARN: arn:aws:cloudfront::111122223333:function/MaxAge
    LastModifiedTime: '2023-11-19T20:38:56.915000+00:00'
    Stage: DEVELOPMENT
  Name: MaxAge
  Status: UNPUBLISHED
Location: https://cloudfront.amazonaws.com/2020-05-31/function/arn:aws:cloudfront:::function/MaxAge
```

Most of the information is repeated from the request. Other
 information is added by CloudFront.


###### Notes



	* `ETag` – This value changes each time
	 you modify the key value store. You use this value and the
	 function name to reference the function in the future. Make
	 sure that you always use the current
	 `ETag`.
	* `FunctionARN` – The ARN for your CloudFront
	 function.
	* 111122223333 – The AWS account.
	* `Stage` – The stage of the function
	 (`LIVE` or `DEVELOPMENT`).
	* `Status` – The status of the function
	 (`PUBLISHED` or
	 `UNPUBLISHED`).


After you create the function, it's added to the `DEVELOPMENT` stage. We
 recommend that you [test your function](test-function.md "test-function.md") before you [publish it](publish-function.md "publish-function.md"). After you publish your function, the
 function changes to the `LIVE` stage.
