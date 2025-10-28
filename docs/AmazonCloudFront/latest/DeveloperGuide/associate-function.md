# Associate functions with distributions

To use a function with a distribution, you associate the function with one or more cache
behaviors in the distribution. You can associate a function with multiple cache behaviors in
multiple distributions.

You can associate a function with any of the following:

- An existing cache behavior
- A new cache behavior in an existing distribution
- A new cache behavior in a new distribution
  When you associate a function with a cache behavior, you must choose an _event type_. The event type determines when CloudFront runs the
  function.

You can choose the following event types:

- **Viewer request** – The function runs when
  CloudFront receives a request from a viewer.
- **Viewer response** – The function runs before
  CloudFront returns a response to the viewer.
  You can't use origin-facing event types (_origin request_
  and _origin response_) with CloudFront Functions. Instead you can
  use Lambda@Edge. For more information, see [CloudFront events that can trigger a
  Lambda@Edge function](lambda-cloudfront-trigger-events.md "lambda-cloudfront-trigger-events.md").

###### Note

Before you associate a function, you must [publish
it](publish-function.md "publish-function.md") to the `LIVE` stage.

You can associate a function with a distribution in the CloudFront console or with the AWS Command Line Interface
(AWS CLI). The following procedure shows how to associate a function with an
existing cache behavior.

Console

###### To associate a function with an existing cache behavior

1. Sign in to the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions") and choose the
   **Functions** page.
2. Choose the function that you want to associate.
3. On the **Function** page, choose the
   **Publish** tab.
4. Choose **Publish function**.
5. Choose **Add association**. On the dialog box that
   appears, choose a distribution, an event type, and/or a cache behavior.

For the event type, choose when you want this function to run:

    * **Viewer Request** – Run the function
     every time CloudFront receives a request.
    * **Viewer Response** – Run the function
     every time CloudFront returns a response.

6. To save the configuration, choose **Add
   association**.

CloudFront associates the distribution with the function. Wait a few minutes for the
associated distribution to finish deploying. You can choose **View
distribution** on the function details page to check the
progress.

CLI

###### To associate a function with an existing cache behavior

1. Open a command line window.
2. Enter the following command to save the distribution configuration for
   the distribution whose cache behavior you want to associate with a
   function. This command saves the distribution configuration to a file
   named `dist-config.yaml`. To use this command, do the
   following:
   - Replace `DistributionID`
     with the distribution's ID.
   - Run the command on one line. In the example, line breaks are
     provided to make the example more readable.

```
aws cloudfront get-distribution-config \
    --id `DistributionID` \
    --output yaml > dist-config.yaml
```

When the command is successful, the AWS CLI returns no output. 3. Open the file named `dist-config.yaml` that you
created. Edit the file to make the following changes.

    1. Rename the `ETag` field to `IfMatch`,
     but don't change the field's value.
    2. In the cache behavior, find the object named
     `FunctionAssociations`. Update this object to add
     a function association. The YAML syntax for a function
     association looks like the following example.




    	* The following example shows a viewer request event
    	 type (trigger). To use a viewer response event type,
    	 replace `viewer-request` with
    	 `viewer-response`.
    	* Replace
    	 ``arn:aws:cloudfront::111122223333:function/ExampleFunction``
    	 with the Amazon Resource Name (ARN) of the function that
    	 you're associating with this cache behavior. To get the
    	 function ARN, you can use the **aws cloudfront
    	 list-functions** command.

    ```
    FunctionAssociations:
      Items:
        - EventType: viewer-request
          FunctionARN: arn:aws:cloudfront::111122223333:function/ExampleFunction
      Quantity: 1
    ```
    3. After making these changes, save the file.

4. Use the following command to update the distribution, adding the
   function association. To use this command, do the following:
   - Replace `DistributionID`
     with the distribution's ID.
   - Run the command on one line. In the example, line breaks are
     provided to make the example more readable.

```
aws cloudfront update-distribution \
    --id `DistributionID` \
    --cli-input-yaml file://dist-config.yaml
```

When the command is successful, you see output like the following that
describes the distribution that was just updated with the function
association. The following example output is truncated for
readability.

```
Distribution:
  ARN: arn:aws:cloudfront::111122223333:distribution/EBEDLT3BGRBBW
  *... truncated ...*
  DistributionConfig:
    *... truncated ...*
    DefaultCacheBehavior:
      *... truncated ...*
      FunctionAssociations:
        Items:
        - EventType: viewer-request
          FunctionARN: arn:aws:cloudfront::111122223333:function/ExampleFunction
        Quantity: 1
      *... truncated ...*
  DomainName: d111111abcdef8.cloudfront.net
  Id: EDFDVBD6EXAMPLE
  LastModifiedTime: '2021-04-19T22:39:09.158000+00:00'
  Status: InProgress
ETag: E2VJGGQEG1JT8S
```

The distribution's `Status` changes to `InProgress` while the
distribution is redeployed. When the new distribution configuration reaches a CloudFront edge
location, that edge location starts using the associated function. When the distribution is
fully deployed, the `Status` changes back to `Deployed`. This
indicates that the associated CloudFront function is live in all CloudFront edge locations worldwide.
This typically takes a few minutes.
