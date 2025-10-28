# Managing cross-account permissions using both

AWS Glue and Lake Formation

It's possible to grant cross-account access to Data Catalog resources and underlying data by
using either AWS Glue or AWS Lake Formation.

In AWS Glue, you grant cross-account permissions by creating or updating a
Data Catalog resource policy. In Lake Formation, you grant cross-account permissions by using the Lake Formation
`GRANT/REVOKE` permissions model and the `Grant Permissions` API
operation.

###### Tip

We recommend that rely solely on Lake Formation permissions to secure your data lake.

You can view Lake Formation cross-account grants by using the Lake Formation console or the AWS Resource Access Manager (AWS RAM)
console. However, those console pages don't show cross-account permissions granted by the
AWS Glue Data Catalog resource policy. Similarly, you can view the cross-account
grants in the Data Catalog resource policy using the **Settings** page of the
AWS Glue console, but that page doesn't show the cross-account permissions
granted using Lake Formation.

To ensure that you don't miss any grants when viewing and managing cross-account
permissions, Lake Formation and AWS Glue require you to perform the following actions to
indicate that you are aware of and are permitting cross-account grants by both Lake Formation and
AWS Glue.

###### When granting cross-account permissions using the AWS Glue Data Catalog resource

policy

If your account (grantor account or producer account) has made no cross-account grants that uses
AWS RAM to share the resources, you can save a Data Catalog resource policy as usual in
AWS Glue. However, if grants that involve AWS RAM resource shares have already
been made, you must do one of the following to ensure that saving the resource policy
succeeds:

- When you save the resource policy on the **Settings** page of the
  AWS Glue console, the console issues an alert stating that the permissions
  in the policy will be in addition to any permissions granted using the Lake Formation console. You
  must choose **Proceed** to save the policy.
- When you save the resource policy using the `glue:PutResourcePolicy` API
  operation, you must set the `EnableHybrid` field to '`TRUE`' (type =
  string).

To update an existing resource policy, use the `glue:GetResourcePolicy`
API operation to retrieve your current policy first, then modify it as needed before
calling `glue:PutResourcePolicy`.

###### Note

When creating AWS Glue resource policies for cross-account access, grant only the minimum permissions required for your specific use case.

For more information, see [PutResourcePolicy Action (Python: put_resource_policy)](../../../glue/latest/dg/aws-glue-api-jobs-security.md#aws-glue-api-jobs-security-PutResourcePolicy "../../../glue/latest/dg/aws-glue-api-jobs-security.md#aws-glue-api-jobs-security-PutResourcePolicy") in
the _AWS Glue Developer Guide_.

###### When granting cross-account permissions using the Lake Formation named resources method

If there is no Data Catalog resource policy in your account (producer account), Lake Formation cross-account grants that
you make proceed as usual. However, if a Data Catalog resource policy exists, you must add the
following statement to it to permit your cross-account grants to succeed if they are made
with the named resource method. Replace `<region>` with a valid
Region name and `<account-id>` with your AWS account
ID (producer account ID).

```
    {
      "Effect": "Allow",
      "Action": [
        "glue:ShareResource"
      ],
      "Principal": {"Service": [
        "ram.amazonaws.com"
      ]},
      "Resource": [
        "arn:aws:glue:`<region>`:`<account-id>`:table/*/*",
        "arn:aws:glue:`<region>`:`<account-id>`:database/*",
        "arn:aws:glue:`<region>`:`<account-id>`:catalog"
      ]
    }
```

Without this additional statement, the Lake Formation grant succeeds, but becomes blocked in AWS RAM,
and the recipient account can't access the granted resource.

###### Important

When using the Lake Formation tag-based access control (LF-TBAC) method to make cross-account
grants, you must have a Data Catalog resource policy with at least the permissions specified in
[Prerequisites](cross-account-prereqs.md "cross-account-prereqs.md").

###### See Also:

- [Metadata access control](access-control-metadata.md "access-control-metadata.md")
  (for a discussion of the named resource method versus the Lake Formation tag-based access control
  (LF-TBAC) method).
- [Viewing shared Data Catalog tables and
  databases](viewing-available-shared-resources.md "viewing-available-shared-resources.md")
- [Working with Data Catalog Settings on the AWS Glue Console](../../../glue/latest/dg/console-data-catalog-settings.md "../../../glue/latest/dg/console-data-catalog-settings.md") in the
  _AWS Glue Developer Guide_
- [Granting
  Cross-Account Access](../../../glue/latest/dg/cross-account-access.md "../../../glue/latest/dg/cross-account-access.md") in the _AWS Glue Developer Guide_
  (for sample Data Catalog resource policies)
