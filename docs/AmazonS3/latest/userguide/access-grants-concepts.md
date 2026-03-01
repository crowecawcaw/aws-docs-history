# S3 Access Grants concepts

###### S3 Access Grants workflow

The S3 Access Grants workflow is:

1. Create an S3 Access Grants instance. See [Working with S3 Access Grants instances](access-grants-instance.md "access-grants-instance.md").
2. Within your S3 Access Grants instance, register locations in your Amazon S3 data, and map these locations to AWS Identity and Access Management (IAM) roles. See [Register a location](access-grants-location-register.md "access-grants-location-register.md").
3. Create grants for grantees, which give grantees access to your S3 resources. See [Working with grants in S3 Access Grants](access-grants-grant.md "access-grants-grant.md").
4. The grantee requests temporary credentials from S3 Access Grants. See [Request access to Amazon S3 data through S3 Access Grants](access-grants-credentials.md "access-grants-credentials.md").
5. The grantee accesses the S3 data using those temporary credentials. See [Accessing S3 data using credentials vended by S3 Access Grants](access-grants-get-data.md "access-grants-get-data.md").
   For more information, see [Getting started with S3 Access Grants](access-grants-get-started.md "access-grants-get-started.md").

**S3 Access Grants instances**

An _S3 Access Grants instance_ is a logical container for
individual _grants_. When you create an S3 Access Grants instance, you must specify an AWS Region. Each AWS Region in your AWS account can have one S3 Access Grants instance. For more information, see [Working with S3 Access Grants instances](access-grants-instance.md "access-grants-instance.md").

If you want to use S3 Access Grants to grant access to user and group identities from your corporate directory, you must also associate your S3 Access Grants instance with an AWS IAM Identity Center instance. For more information, see [S3 Access Grants and corporate directory identities](access-grants-directory-ids.md "access-grants-directory-ids.md").

A newly created S3 Access Grants instance is empty. You must register a location in the instance, which can be the S3 default path (`s3://`), a bucket, or a prefix within a bucket. After you register at least one location, you can create access grants that give access to data in this registered location.

**Locations**

An S3 Access Grants _location_ maps buckets or prefixes to an AWS Identity and Access Management (IAM) role. S3 Access Grants assumes this IAM role to vend temporary credentials to the grantee that's accessing that particular location. You must first register at least one location in your S3 Access Grants instance before you can create an access grant.

We recommend that you register the default location (`s3://`) and map it to an IAM role. The location at the default S3 path (`s3://`) covers access to all of your S3 buckets in the AWS Region of your account. When you create an access grant, you can narrow the grant scope to a bucket, a prefix, or an object within the default location.

More complex access-management use cases might require you to register more than the default location. Some examples of such use cases are:

- Suppose that the `amzn-s3-demo-bucket` is a registered location in your S3 Access Grants instance with an IAM role mapped to it, but this IAM role is denied access to a particular prefix within the bucket. In this case, you can register the prefix that the IAM role does not have access to as a separate location and map that location to a different IAM role with the necessary access.
- Suppose that you want to create grants that restrict access to only the users within a virtual private cloud (VPC) endpoint. In this case, you can register a location for a bucket in which the IAM role restricts access to the VPC endpoint. Later, when a grantee asks S3 Access Grants for credentials, S3 Access Grants assumes the location’s IAM role to vend the temporary credentials. This credential will deny access to the specific bucket unless the caller is within the VPC endpoint. This deny permission is applied in addition to the regular READ, WRITE, or READWRITE permission specified in the grant.

If your use case requires you to register multiple locations in your S3 Access Grants instance, you can register any of the following:

- The default S3 location (`s3://`)
- A bucket (for example, `amzn-s3-demo-bucket`) or multiple buckets
- A bucket and a prefix (for example, ``amzn-s3-demo-bucket`/prefix\*`) or multiple prefixes

For the maximum number of locations that you can register in your S3 Access Grants instance, see [S3 Access Grants limitations](access-grants-limitations.md "access-grants-limitations.md"). For more information about registering an S3 Access Grants location, see [Register a location](access-grants-location-register.md "access-grants-location-register.md").

After you register the first location in your S3 Access Grants instance, your instance still does not have any individual access grants in it. So, no access has been granted yet to any of your S3 data. You can now create access grants to give access. For more information about creating grants, see [Working with grants in S3 Access Grants](access-grants-grant.md "access-grants-grant.md").

**Grants**

An individual _grant_ in an S3 Access Grants instance allows a specific identity—an IAM principal, or a user or group in a corporate directory—to get access within a location that is registered in your S3 Access Grants instance.

When you create a grant, you don't have to grant access to the entire registered location. You can narrow the grant's scope of access within a location. If the registered location is the default S3 path (`s3://`), you are required to narrow the scope of the grant to a bucket, a prefix within a bucket, or a specific object. If the registered location of the grant is a bucket or a prefix, then you can give access to the entire bucket or prefix, or you can optionally narrow the scope of the grant to a prefix, subprefix, or an object.

In the grant, you also set the access level of the grant to READ, WRITE, or READWRITE. Suppose you have a grant that gives the corporate directory group `01234567-89ab-cdef-0123-456789abcdef` READ access to the bucket `s3://`amzn-s3-demo-bucket`/projects/items/*`. Users in this group can have READ access to every object that has an object key name which starts with the prefix `projects/items/` in the bucket named `amzn-s3-demo-bucket`.

For the maximum number of grants that you can create in your S3 Access Grants instance, see [S3 Access Grants limitations](access-grants-limitations.md "access-grants-limitations.md"). For more information about creating grants, see [Create grants](access-grants-grant-create.md "access-grants-grant-create.md").

**S3 Access Grants temporary credentials**

After you create a grant, an authorized application that utilizes the identity specified in the grant can request _just-in-time access credentials_. To do this, the application calls the [GetDataAccess](../API/API_control_GetDataAccess.md "../API/API_control_GetDataAccess.md") S3 API operation. Grantees can use this API operation to request access to the S3 data you have shared with them.

The S3 Access Grants instance evaluates the `GetDataAccess` request against the grants that it has. If there is a matching grant for the requestor, S3 Access Grants assumes the IAM role that's associated with the registered location of the matching grant. S3 Access Grants scopes the permissions of the temporary credentials to access only the S3 bucket, prefix, or object that's specified by the grant's scope.

The expiration time of the temporary access credentials defaults to 1 hour, but you can set it to any value from 15 minutes to 12 hours. See the maximum duration session in the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API reference.

## How it works

In the following diagram, a default Amazon S3 location with the scope `s3://` is
registered with the IAM role `s3ag-location-role`. This IAM role has
permissions to perform Amazon S3 actions within the account when its credentials are obtained
through S3 Access Grants.

Within this location, two individual access grants are created for two IAM users. The
IAM user Bob is granted both `READ` and `WRITE` access on the
`bob/` prefix in the `DOC-BUCKET-EXAMPLE` bucket. Another
IAM role, Alice, is granted only `READ` access on the `alice/`
prefix in the `DOC-BUCKET-EXAMPLE` bucket. A grant, colored in blue, is
defined for Bob to access the prefix `bob/` in the
`DOC-BUCKET-EXAMPLE` bucket. A grant, colored in green, is defined for
Alice to access the prefix `alice/` in the `DOC-BUCKET-EXAMPLE`
bucket.

When it's time for Bob to `READ` data, the IAM role that's associated
with the location that his grant is in calls the S3 Access Grants [GetDataAccess](../API/API_control_GetDataAccess.md "../API/API_control_GetDataAccess.md") API operation. If Bob tries to
`READ` any S3 prefix or object that starts with
`s3://DOC-BUCKET-EXAMPLE/bob/*`, the `GetDataAccess` request
returns a set of temporary IAM session credentials with permission to
`s3://DOC-BUCKET-EXAMPLE/bob/*`. Similarly, Bob can `WRITE` to
any S3 prefix or object that starts with `s3://DOC-BUCKET-EXAMPLE/bob/*`,
because the grant also allows that.

Similarly, Alice can `READ` anything that starts with
`s3://DOC-BUCKET-EXAMPLE/alice/`. However, if she tries to
`WRITE` anything to any bucket, prefix, or object in `s3://`,
she will get an Access Denied (403 Forbidden) error, because there is no grant that
gives her `WRITE` access to any data. In addition, if Alice requests any
level of access (`READ` or `WRITE`) to data outside of
`s3://DOC-BUCKET-EXAMPLE/alice/`, she will again receive an Access Denied
error.

![How S3 Access Grants works](images/s3ag-how-it-works.png)

This pattern scales to a high number of users and buckets and simplifies management of
those permissions. Rather than editing potentially large S3 bucket policies every time
you want to add or remove an individual user-prefix access relationship, you can add and
remove individual, discrete grants.
