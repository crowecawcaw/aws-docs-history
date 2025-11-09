# Registering an Amazon S3 location

You must specify an AWS Identity and Access Management (IAM) role when you register an Amazon Simple Storage Service (Amazon S3) location.
Lake Formation assumes that role when it grants temporary credentials to integrated AWS services that
access the data in that location.

###### Important

Avoid registering an Amazon S3 bucket that has **Requester pays** enabled.
For buckets registered with Lake Formation, the role used to register the bucket is always viewed as
the requester. If the bucket is accessed by another AWS account, the bucket owner is
charged for data access if the role belongs to the same account as the bucket owner.

You can use the AWS Lake Formation console, Lake Formation API, or AWS Command Line Interface (AWS CLI) to register an Amazon S3
location.

###### Before you begin

Review the [requirements for the role used to register
the location](registration-role.md "registration-role.md").

###### To register a location (console)

###### Important

The following procedures assume that the Amazon S3 location is in the same AWS account as
the Data Catalog and that the data in the location is not encrypted. Other sections in this
chapter cover cross-account registration and registration of encrypted locations.

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as the data lake
   administrator or as a user with the `lakeformation:RegisterResource` IAM
   permission.
2. In the navigation pane, under **Administration**, select
   **Data lake locations**.
3. Choose **Register location**, and then choose
   **Browse** to select an Amazon Simple Storage Service (Amazon S3) path.
4. (Optional, but strongly recommended) Select **Review location
   permissions** to view a list of all existing resources in the selected Amazon S3
   location and their permissions.

Registering the selected location might result in your Lake Formation users gaining access to
data already at that location. Viewing this list helps you ensure that existing data
remains secure. 5. For **IAM role**, choose either the
`AWSServiceRoleForLakeFormationDataAccess` service-linked role (the default)
or a custom IAM role that meets the requirements in [Requirements for roles used to register
locations](registration-role.md "registration-role.md").

You can update a registered location or other details only when you register it using
a custom IAM role. To edit a location registered using a service-linked role, you should
deregister the location and register it again. 6. Choose **Enable Data Catalog Federation** option to allow Lake Formation to assume a
role and vend temporary credentials to integrated AWS services to access tables under
federated databases. If a location is registered with Lake Formation, and you want to use the same
location for a table under a federated database, you need to register the same location
with the **Enable Data Catalog Federation** option. 7. Choose **Hybrid access mode** to not enable Lake Formation permissions by default. When you register Amazon S3 location
in hybrid access mode, you can enable Lake Formation permissions by opting in principals for databases and tables under that location. 

For more information on setting up hybrid access mode, see [Hybrid access mode](hybrid-access-mode.md "hybrid-access-mode.md"). 8. Select **Register location**.

###### To register a location (AWS CLI)

1. ###### Register a new location with Lake Formation

This example uses a service-linked role to register the location. You can
use the `--role-arn` argument instead to supply your own role.

Replace `<s3-path>` with a valid Amazon S3 path, account number
with a valid AWS account, and `<s3-access-role>` with an IAM role
that has permissions to register a data location.

###### Note

You can't edit properties of a registered location if it is registered using a service-linked role.

```
aws lakeformation register-resource \
 --resource-arn arn:aws:s3:::`<s3-path>` \
 --use-service-linked-role
```

The following example uses a custom role to register the location.

```
aws lakeformation register-resource \
 --resource-arn arn:aws:s3:::`<s3-path>` \
 --role-arn arn:aws:iam::`<123456789012>`:role/`<s3-access-role>`
```

2. ###### To update a location registered with Lake Formation

You can edit a registered location only if it is registered using a custom IAM
role. For a location registered with service-linked role, you should deregister the
location and register it again. For more information, see [Deregistering an Amazon S3 location](unregister-location.md "unregister-location.md").

```
aws lakeformation update-resource \
 --role-arn arn:aws:iam::`<123456789012>`:role/`<s3-access-role>`\
 --resource-arn arn:aws:s3:::`<s3-path>`

```

```
aws lakeformation update-resource \
 --resource-arn arn:aws:s3:::`<s3-path>` \
 --use-service-linked-role
```

3. ###### Register a data location in hybrid access mode with federation

```
aws lakeformation register-resource \
 --resource-arn arn:aws:s3:::`<s3-path>` \
 --role-arn arn:aws:iam::`<123456789012>`:role/`<s3-access-role>` \
 --hybrid-access-enabled

```

```
aws lakeformation register-resource \
 --resource-arn arn:aws:s3:::`<s3-path>` \
 --role-arn arn:aws:iam::`<123456789012>`:role/`<s3-access-role>` \
 --with-federation
```

```
aws lakeformation update-resource \
 --resource-arn arn:aws:s3:::`<s3-path>` \
 --role-arn arn:aws:iam::`<123456789012>`:role/`<s3-access-role>` \
 --hybrid-access-enabled
```

For more information, see [RegisterResource](../APIReference/API_RegisterResource.md "../APIReference/API_RegisterResource.md") API operation.

###### Note

Once you register an Amazon S3 location, any AWS Glue table pointing to the location (or any
of its child locations) will return the value for the
`IsRegisteredWithLakeFormation` parameter as `true` in the
`GetTable` call. There is a known limitation that Data Catalog API operations
such as `GetTables` and `SearchTables` do not update the value for
the `IsRegisteredWithLakeFormation` parameter, and return the default, which
is false. It is recommended to use the `GetTable` API to view the correct
value for the `IsRegisteredWithLakeFormation` parameter.
