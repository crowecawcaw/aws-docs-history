# Publish functions

When you publish your function, this copies the function from the `DEVELOPMENT`
 stage to the `LIVE` stage.

If cache behaviors aren't associated with the function, publishing it enables you to
 associate it with a cache behavior. You can only associate cache behaviors with functions
 that are in the `LIVE` stage.

###### Important


* Before you publish, we recommend that you [test
 the function](test-function.md "test-function.md").
* After you publish the function, all cache behaviors that are associated with
 that function automatically start using the newly published copy, as soon as the
 distributions finish deploying.
You can publish a function in the CloudFront console or with the
 AWS CLI.


Console
###### To publish a function

1. Sign in to the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions") and choose the
 **Functions** page.
2. Choose the function to update.
3. Choose the **Publish** tab and then choose
 **Publish**. If your function is already attached
 to one or more cache behaviors, choose **Publish and
 update**.
4. (Optional) To see the distributions that are associated with the
 function, choose **Associated CloudFront distributions** to
 expand that section.

When successful, a banner appears at the top of the page that says
 **`Function name` published
 successfully**. You can also choose the **Build**
 tab and then choose **Live** to see the live version of the
 function code.



CLI
###### To publish a function

1. Open a command line window.
2. Run the following **aws cloudfront publish-function**
 command. In the example, line breaks are provided to make the example
 more readable.



```
aws cloudfront publish-function \
    --name MaxAge \
    --if-match ETVXYZEXAMPLE
```

When the command is successful, you see output like the
 following.



```
FunctionSummary:
  FunctionConfig:
    Comment: Max Age 2 years
    Runtime: cloudfront-js-2.0
  FunctionMetadata:
    CreatedTime: '2021-04-18T21:24:21.314000+00:00'
    FunctionARN: arn:aws:cloudfront::111122223333:function/ExampleFunction
    LastModifiedTime: '2023-12-19T23:41:15.389000+00:00'
    Stage: LIVE
  Name: MaxAge
  Status: UNASSOCIATED
```
