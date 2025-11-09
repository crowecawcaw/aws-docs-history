# Getting started with S3 Access Grants

Amazon S3 Access Grants is an Amazon S3 feature that provides a scalable access control solution for your
S3 data. S3 Access Grants is an S3 credential vendor, meaning that you register with S3 Access Grants your list
of grants and at what level. Thereafter, when users or clients need access to your S3 data,
they first ask S3 Access Grants for credentials. If there is a corresponding grant that authorizes
access, S3 Access Grants vends temporary, least-privilege access credentials. The users or clients can
then use S3 Access Grants vended credentials to access your S3 data. With that in mind, if your S3
data requirements mandate a complex or large permission configuration, you can use S3 Access Grants to
scale S3 data permissions for users, groups, roles, and applications.

For most use cases, you can manage access control for your S3 data by using AWS Identity and Access Management (IAM)
with bucket policies or IAM identity-based policies.

However, if you have complex S3 access control requirements, such as the following, you could
benefit greatly from using S3 Access Grants:

- You are running into the bucket policy size limit of 20 KB.
- You grant human identities, for example, Microsoft Entra ID (formerly
  Azure Active Directory), Okta, or
  Ping users and groups, access to S3 data for analytics and big
  data.
- You must provide cross-account access without making frequent updates to IAM
  policies.
- Your data is unstructured and object-level rather than structured, in row and column format.
  The S3 Access Grants workflow is as
  follows:

| Steps | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | [Create an S3 Access Grants instance](access-grants-instance.md "access-grants-instance.md")<br>To get started, initiate an S3 Access Grants instance that will contain your<br>individual access grants.                                                                                                                                                                                                                                                                                      |
| 2     | [Register a location](access-grants-location.md "access-grants-location.md")<br>Second, register an S3 data location (such as the default,<br>`s3://`) and then specify a default IAM role that<br>S3 Access Grants assumes when providing access to the S3 data location. You can<br>also add custom locations to specific buckets or prefixes and map those<br>to custom IAM roles.                                                                                                          |
| 3     | [Create grants](access-grants-grant.md "access-grants-grant.md")<br>Create individual permission grants. Specify in these permission<br>grants the registered S3 location, the scope of data access within the<br>location, the identity of the grantee, and their access level<br>(`READ`, `WRITE`, or<br>`READWRITE`).                                                                                                                                                                       |
| 4     | [Request<br>access to S3 data](access-grants-credentials.md "access-grants-credentials.md")<br>When users, applications, and AWS services want to access S3 data,<br>they first make an access request. S3 Access Grants determines if the request<br>should be authorized. If there is a corresponding grant that authorizes<br>access, S3 Access Grants uses the registered location's IAM role that's<br>associated with that grant to vend temporary credentials back to the<br>requester. |
| 5     | [Access S3 data](access-grants-get-data.md "access-grants-get-data.md")<br>Applications use the temporary credentials vended by S3 Access Grants to access<br>S3 data.                                                                                                                                                                                                                                                                                                                         |
