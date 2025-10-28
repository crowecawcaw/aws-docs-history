# Update functions

You can update a function at any time. The changes are made only to the version of the
function that is in the `DEVELOPMENT` stage. To copy the updates from the
`DEVELOPMENT` stage to `LIVE`, you must [publish the function](publish-function.md "publish-function.md").

You can update a function's code in the CloudFront console or with the AWS Command Line Interface
(AWS CLI).

Console

###### To update function code

1. Sign in to the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions "https://console.aws.amazon.com/cloudfront/v4/home#/functions") and choose the
   **Functions** page.

Choose the function to update. 2. Choose **Edit** and make the following
changes:

    * Update any fields in the **Details**
     section.


    * Change or remove the associated key value store. For more
     information about key value stores, see [Amazon CloudFront KeyValueStore](kvs-with-functions.md "kvs-with-functions.md").


    * Change the function code. Choose the
     **Build** tab, make changes, then choose
     **Save changes** to save changes to the
     code.

CLI

###### To update the function code

1. Open a command line window.
2. Run the following command.

This example uses the `fileb://` notation to pass
in the file. It also includes line breaks to make the command more
readable.

```
aws cloudfront update-function \
    --name MaxAge \
    --function-config '{"Comment":"Max Age 2 years","Runtime":"cloudfront-js-2.0","KeyValueStoreAssociations":{"Quantity":1,"Items":[{"KeyValueStoreARN":"arn:aws:cloudfront::111122223333:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}]}}' \
    --function-code fileb://function-max-age-v1.js \
    --if-match ETVABCEXAMPLE

```

###### Notes

    * You can identify the function by both its name and ETag
     (in the `if-match` parameter). Make sure that you
     use the current ETag. You can get this value from the [DescribeFunction](../../../cloudfront/latest/APIReference/API_DescribeFunction.md "../../../cloudfront/latest/APIReference/API_DescribeFunction.md") API
     operation.
    * You must include the `function-code`, even if
     you don't want to change it.
    * Be careful with the `function-config`. You
     should pass everything that you want to keep in the
     configuration. Specifically, handle the key value store as
     follows:




    	+ To retain the existing key value store association
    	 (if there is one), specify the name of the *existing* store.
    	+ To change the association, specify the name of the
    	 *new* key value
    	 store.
    	+ To remove the association, omit the
    	 `KeyValueStoreAssociations` parameter.

When the command is successful, you see output like the following.

```
ETag: ETVXYZEXAMPLE
FunctionSummary:
  FunctionConfig:
    Comment: Max Age 2 years \
    Runtime: cloudfront-js-2.0 \
    KeyValueStoreAssociations= \
      {Quantity=1, \
      Items=[{KeyValueStoreARN='arn:aws:cloudfront::111122223333:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111'}]} \
  FunctionMetadata: \
    CreatedTime: '2021-04-18T20:38:56.915000+00:00' \
    FunctionARN: arn:aws:cloudfront::111122223333:function/MaxAge \
    LastModifiedTime: '2023-12-19T23:41:15.389000+00:00' \
    Stage: DEVELOPMENT \
  Name: MaxAge \
  Status: UNPUBLISHED
```

Most of the information is repeated from the request. Other information is added by
CloudFront.

###### Notes

- `ETag` – This value changes each time you modify the key
  value store.
- `FunctionARN` – The ARN for your CloudFront function.
- `Stage` – The stage for the function (`LIVE` or
  `DEVELOPMENT`).
- `Status` – The status of the function
  (`PUBLISHED` or `UNPUBLISHED`).
