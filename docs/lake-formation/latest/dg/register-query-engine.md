# Registering a third-party query engine

Before a third-party query engine can use the application integration API operations,
you need to explicitly enable permissions for the query engine to call the API operations on
your behalf. This is done in a few steps:

1. You need to specify the AWS accounts and IAM session tags that require
   permission to call the application integration API operations through the AWS
   Lake Formation console, the AWS CLI or the API/SDK.
2. When the third-party query engine assumes the execution role in your account,
   the query engine must attach a session tag that is registered with Lake Formation representing the
   third-party engine. Lake Formation uses this tag to validate that if the request is
   coming from an approved engine. For more information about session tags, see [Session
   tags](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md") in the IAM User Guide.
3. When setting up a third-party query engine execution role, you must have the
   following minimum set of permissions in the IAM policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {"Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess",
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:CreateDatabase",
 "glue:GetUserDefinedFunction",
 "glue:GetUserDefinedFunctions",
 "glue:GetPartition",
 "glue:GetPartitions"
 ],
 "Resource": "*"
 }
}`

```

4. Set up a role trust policy on the query engine execution role to have fine access
   control on which session tag key value pair can be attached to this role. In the
   following example, this role is only allowed to have session tag key
   `"LakeFormationAuthorizedCaller"` and session tag value
   `"engine1"` to be attached, and no other session tag key value pair is
   allowed.

```
{
    "Sid": "AllowPassSessionTags",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/query-execution-role"
    },
    "Action": "sts:TagSession",
    "Condition": {
    "StringLike": {
        "aws:RequestTag/`LakeFormationAuthorizedCaller`": `"engine1"`        }
    }
}
```

When `LakeFormationAuthorizedCaller` calls the STS:AssumeRole API
operation to fetch credentials for the query engine to use, the session tag must be included
in the [AssumeRole request](../../../IAM/latest/UserGuide/id_session-tags.md#id_session-tags_adding-assume-role "../../../IAM/latest/UserGuide/id_session-tags.md#id_session-tags_adding-assume-role"). The returned temporary credential can be used to make
Lake Formation application integration API requests.

Lake Formation application integration API operations require the calling principal
to be an IAM role. The IAM role must include a session tag with a predetermined value
that has been registered with Lake Formation. This tag allows Lake Formation to
verify that the role used to call the application integration API operations is allowed to
do so.
