# AWS Config Linked

Resources

The **AWS Config Linked Resources** field should be set
to the JSON string representation of a list of objects (maps)
corresponding to the linked resources, each with the following
keys:

- _resourceId_: the ID of the resource in AWS Config
- _resourceType_: the type of the resource in AWS Config
- _accountName_: the name or alias of the AWS
  account configured in Jira that should be used to access this
  resource
- _region_: the Region where AWS Config should be
  accessed to get information on this resource
  For example, the following value would show information on the S3
  bucket `my-bucket` in `eu-central-1`, using the
  account and end user credentials specified in Jira for the AWS account
  identified in Jira as `MyAccount1`:

```

                    [ { "resourceId": "my-bucket",
        "resourceType": "AWS::S3::Bucket",
        "accountName": "MyAccount1",
        "region": "eu-central-1" } ]

```
