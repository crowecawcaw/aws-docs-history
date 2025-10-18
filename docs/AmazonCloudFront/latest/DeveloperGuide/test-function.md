# Test functions

Before you deploy the function to the live stage (production), you can test your function
 to verify that it works as intended. To test a function, you specify an *event object* that represents an HTTP request or response that
 your CloudFront distribution could receive in production. 

CloudFront Functions does the following:


1. Runs the function, using the provided event object as input.
2. Returns the function's result (the modified event object) along with any function
 logs or error messages and the function's *compute
 utilization*. For more information about compute utilization, see
 [Understand compute utilization](#compute-utilization "#compute-utilization").
###### Note

When you test a function, CloudFront only validates against function execution errors. CloudFront
 doesn't validate whether the request will flow through successfully once published. For
 example, if your function deletes a required header, the test will succeed because there
 isn't an issue with the code. However, if you publish the function and associate it with
 a distribution, the function will fail when a request was made through CloudFront.

###### Contents

* [Set up the event object](test-function.md#test-function-create-event "test-function.md#test-function-create-event")
* [Test the function](test-function.md#test-function-step-test "test-function.md#test-function-step-test")
* [Understand compute utilization](test-function.md#compute-utilization "test-function.md#compute-utilization")

## Set up the event object


Before you test a function, you must set up the event object to test it with. There
 are several options.




**Option 1: Set up an event object without saving it**

You can set up an event object in the visual editor in the CloudFront console
 and not save it. 


You can use this event object to test the function from the CloudFront console,
 even though it's not saved.



**Option 2: Create an event object in the visual editor**

You can set up an event object in the visual editor in the CloudFront console
 and not save it. You can create 10 event objects for each function so that
 you can, for example, test different possible inputs.


When you create the event object in this way, you can use the event object
 to test the function in the CloudFront console. You can't use it to test the
 function using an AWS API or SDK. 






**Option 3: Create an event object using a text editor**

You can use a text editor to create an event object in JSON format. For
 information about the structure of an event object, see [Event structure](functions-event-structure.md "functions-event-structure.md"). 


You can use this event object to test the function using the CLI. But you
 can't use it to test the function in the CloudFront console.




###### To create an event object (option 1 or 2)

1. Sign in to the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions") and choose the
 **Functions** page.


Choose the function that you want to test.
2. On the function details page, choose the **Test** tab.
3. For **Event type**, choose one of the following
 options:




	* Choose **Viewer request** if the function modifies an
	 HTTP request or generates a response based on the request. The
	 **Request** section appears.
	* Choose **Viewer response**. The
	 **Request** and the **Response**
	 sections appear.
4. Complete the fields to include in the event. You can choose **Edit
 JSON** to view the raw JSON.
5. (Optional) To save the event, choose **Save** and in the
 **Save test event**, enter a name and then choose
 **Save**.


You can also choose **Edit JSON** and copy the raw JSON, and
 save it in your own file, outside of CloudFront.

**To create an event object (option 3)**


Create the event object using a text editor. Store the file in a directory that your
 computer can connect to. 


Verify that you follow these guidelines:



* Omit the `distributionDomainName`, `distributionId`, and
 `requestId` fields.
* The names of headers, cookies, and query strings must be lowercase.

One option for creating an event object in this way is to create a sample using the
 visual editor. You can be sure that the sample is correctly formatted. You can then copy
 the raw JSON and paste it into a text editor and save the file.


For more information about the structure of an event, see [Event structure](functions-event-structure.md "functions-event-structure.md"). 


## Test the function


You can test a function in the CloudFront console or with the AWS Command Line Interface (AWS CLI).



Console
###### To test the function

1. Sign in to the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions") and choose the
 **Functions** page.
2. Choose the function that you want to test.
3. Choose the **Test** tab.
4. Make sure that the correct event is displayed. To switch from the
 currently displayed event, choose another event in the
 **Select test event** field.
5. Choose **Test function**. The console shows the
 output of the function, including function logs and compute
 utilization.


CLI
You can test a function by using the **aws cloudfront
 test-function** command. 


###### To test the function

1. Open a command line window.
2. Run the following command from the same directory that contains
 the specified file.


This example uses the `fileb://` notation to
 pass in the event object file. It also includes line breaks to make
 the command more readable. 



```
aws cloudfront test-function \
    --name MaxAge \
    --if-match ETVABCEXAMPLE \
    --event-object fileb://event-maxage-test01.json \
    --stage DEVELOPMENT
```

###### Notes



	* You reference the function by its name and ETag (in
	 the `if-match` parameter). You reference the
	 event object by its location in your file system.
	* The stage can be `DEVELOPMENT` or
	 `LIVE`.
When the command is successful, you see output like the
 following.



```
TestResult:
  ComputeUtilization: '21'
  FunctionErrorMessage: ''
  FunctionExecutionLogs: []
  FunctionOutput: '{"response":{"headers":{"cloudfront-functions":{"value":"generated-by-CloudFront-Functions"},"location":{"value":"https://aws.amazon.com/cloudfront/"}},"statusDescription":"Found","cookies":{},"statusCode":302}}'
  FunctionSummary:
    FunctionConfig:
      Comment: MaxAge function
      Runtime: cloudfront-js-2.0
      KeyValueStoreAssociations= \
      {Quantity=1, \
      Items=[{KeyValueStoreARN='arn:aws:cloudfront::111122223333:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111'}]} \
    FunctionMetadata:
      CreatedTime: '2021-04-18T20:38:56.915000+00:00'
      FunctionARN: arn:aws:cloudfront::111122223333:function/MaxAge
      LastModifiedTime: '2023-17-20T10:38:57.057000+00:00'
      Stage: DEVELOPMENT
    Name: MaxAge
    Status: UNPUBLISHED
```



###### Notes


* `FunctionExecutionLogs` contains a list of log lines that the
 function wrote in `console.log()` statements (if any).
* `ComputeUtilization` contains information about running your
 function. See [Understand compute utilization](#compute-utilization "#compute-utilization").
* `FunctionOutput` contains the event object that the function
 returned.

## Understand compute utilization


**Compute utilization** is the amount of time
 that the function took to run as a percentage of the maximum allowed time. For example, a value
 of 35 means that the function completed in 35% of the maximum allowed time.


If a function continuously exceeds the maximum allowed time, CloudFront throttles the
 function. The following list explains the likelihood of a function getting throttled
 based on the compute utilization value.


**Compute utilization value:**



* **1 – 50** – The function is comfortably below
 the maximum allowed time and should run without throttling.
* **51 – 70** – The function is nearing the maximum
 allowed time. Consider optimizing the function code.
* **71 – 100** – The function is very close to or
 exceeds the maximum allowed time. CloudFront is likely to throttle this function if
 you associate it with a distribution.
