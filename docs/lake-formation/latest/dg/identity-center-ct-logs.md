# Including IAM Identity Center user context in CloudTrail logs

Lake Formation uses [credential vending](using-cred-vending.md "using-cred-vending.md") functionality to provide temporary access to Amazon S3 data.
By default, when an IAM Identity Center user submits a query to an integrated analytics service, the CloudTrail logs only include the IAM role assumed by the service to provide short term access.
If you use a user-defined role to register the Amazon S3 data location with Lake Formation,
you can opt in to include the IAM Identity Center user's context in the
CloudTrail events, and then track the users that access your resources.

###### Important

To include object-level Amazon S3 API requests in the CloudTrail, you
need to enable CloudTrail event logging for Amazon S3 bucket and objects. For more inormation, see [Enabling CloudTrail event logging for Amazon S3 buckets and objects](../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md "../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md")
in the Amazon S3 User Guide.

###### To enable credential vending auditing on data lake locations registered with user-defined roles

1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the left-side navigation, expand **Administration**, and choose **Data Catalog settings**.
3. Under **Enhanced auditing**, choose **Propagate provided context.**
4. Choose **Save**.
   You can also enable the enhanced auditing option by setting the `Parameters` attribute in the [PutDataLakeSettings](../APIReference/API_PutDataLakeSettings.md "../APIReference/API_PutDataLakeSettings.md") operation.
   By default, the `SET_CONTEXT"` parameter value is set to "true".

```
{
    "DataLakeSettings": {
        "Parameters": {"SET_CONTEXT": "true"},
    }
}
```

The following is an excerpt from a CloudTrail event with the enhanced auditing option. This log
includes both the IAM Identity Center user's session context and the user-defined IAM role assumed by Lake Formation to access the Amazon S3 data location. See the `onBehalfOf` parameter
in the following excerpt.

```
{
         "eventVersion":"1.09",
         "userIdentity":{
            "type":"AssumedRole",
            "principalId":"AROAW7F7MOX4OYE6FLIFN:access-grants-e653760c-4e8b-44fd-94d9-309e035b75ab",
            "arn":"arn:aws:sts::123456789012:assumed-role/accessGrantsTestRole/access-grants-e653760c-4e8b-44fd-94d9-309e035b75ab",
            "accountId":"123456789012",
            "accessKeyId":"ASIAW7F7MOX4CQLD4JIZN",
            "sessionContext":{
               "sessionIssuer":{
                  "type":"Role",
                  "principalId":"AROAW7F7MOX4OYE6FLIFN",
                  "arn":"arn:aws:iam::123456789012:role/accessGrantsTestRole",
                  "accountId":"123456789012",
                  "userName":"accessGrantsTestRole"
               },
               "attributes":{
                  "creationDate":"2023-08-09T17:24:02Z",
                  "mfaAuthenticated":"false"
               }
            },
            "**onBehalfOf":{
 "userId": "<identityStoreUserId>",
 "identityStoreArn": "arn:aws:identitystore::<restOfIdentityStoreArn>"**
            }
         },
         "eventTime":"2023-08-09T17:25:43Z",
         "eventSource":"s3.amazonaws.com",
         "eventName":"GetObject",
    ....

```
