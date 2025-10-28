# Managing LF-Tags for metadata access control

To use the Lake Formation tag-based access control (LF-TBAC) method to secure Data Catalog objects such as
catalogs, databases, tables, views, and columns, you create LF-Tags, assign them to resources,
and grant LF-Tag permissions to principals.

Before you can assign LF-Tags to Data Catalog objects or grant permissions to
principals, you need to define LF-Tags. Only a data lake administrator or a principal with
LF-Tag creator permissions can create LF-Tags.

###### LF-Tag creators

LF-Tag creator is a non-admin principal who has permissions to create and manage LF-Tags.
Data lake administrators can add LF-Tag creators using the Lake Formation console or CLI.
LF-Tag creators have implicit Lake Formation permissions to update, and delete LF-Tags, to
assign LF-Tags to resources, and to grant LF-Tag permissions and LF-Tag value permissions to
other principals.

With LF-Tag creator roles, data lake administrators can delegate tag management tasks such
as creating and updating tag keys and values to non-admin principals. Data lake administrators
can also grant LF-Tag creators grantable `Create LF-Tag` permissions. Then, the
LF-Tag creator can grant the permission to create LF-Tags to other principals.

You can grant two types of permissions on LF-Tags:

- LF-Tag permissions - `Create LF-Tag`, `Alter`, and `Drop`.
  These permissions are required to create, update, and delete LF-Tags.

Data lake administrators and LF-Tag creators implicitly have these permissions on the
LF-Tags they create and can grant these permissions explicitly to principals to manage tags
in the data lake.

- LF-Tag key-value pair permissions - `Assign`, `Describe`, and
  `Grant with LF-Tag expressions`. These permissions are required to
  assign LF-Tags to Data Catalog objects, and to grant permissions on the resources to
  principals using Lake Formation tag-based access control. LF-Tag creators implicitly receive these
  permissions when creating LF-Tags.
  After receiving the `Create LF-Tag` permission and successfully creating
  LF-Tags, the LF-Tag creator can assign LF-Tags to resources and grant LF-Tag
  permissions (`Create LF-Tag`, `Alter`, `Drop`, and ) to other
  non-administrative principals to manage tags in the data lake. You can manage LF-Tags by
  using the Lake Formation console, the API, or the AWS Command Line Interface (AWS CLI).

###### Note

Data lake administrators have implicit Lake Formation permissions to create, update, and delete LF-Tags, to assign LF-Tags to resources, and to grant LF-Tag permissions to principals.

For best practices and considerations, see [Lake Formation tag-based access control best
practices and considerations](lf-tag-considerations.md "lf-tag-considerations.md")

###### Topics

- [Adding LF-Tag creators](TBAC-adding-tag-creator.md "TBAC-adding-tag-creator.md")
- [Creating LF-Tags](TBAC-creating-tags.md "TBAC-creating-tags.md")
- [Updating LF-Tags](TBAC-updating-tags.md "TBAC-updating-tags.md")
- [Deleting LF-Tags](TBAC-deleting-tags.md "TBAC-deleting-tags.md")
- [Listing LF-Tags](TBAC-listing-tags.md "TBAC-listing-tags.md")
- [Assigning LF-Tags to Data Catalog resources](TBAC-assigning-tags.md "TBAC-assigning-tags.md")
- [Viewing LF-Tags assigned to a
  resource](TBAC-view-resource-tags.md "TBAC-view-resource-tags.md")
- [Viewing the resources that a LF-Tag is
  assigned to](TBAC-view-tag-resources.md "TBAC-view-tag-resources.md")
- [Life cycle of a LF-Tag](#lf-tag-life-cycle "#lf-tag-life-cycle")
- [Comparison of Lake Formation tag-based access control to IAM attribute-based access
  control](#TBAC-comparison-ABAC "#TBAC-comparison-ABAC")

###### See also

- [Managing LF-Tag value
  permissions](TBAC-granting-tags.md "TBAC-granting-tags.md")
- [Granting data lake permissions using the
  LF-TBAC method](granting-catalog-perms-TBAC.md "granting-catalog-perms-TBAC.md")
- [Lake Formation tag-based access control](tag-based-access-control.md "tag-based-access-control.md")

## Life cycle of a LF-Tag

1. The LF-Tag creator Michael creates a LF-Tag
   `module=Customers`.
2. Michael grants `Associate` on the LF-Tag to the data engineer Eduardo.
   Granting `Associate` implicitly grants `Describe`.
3. Michael grants `Super` on the table `Custs` to Eduardo with
   the grant option, so that Eduardo can assign LF-Tags to the table. For more information,
   see [Assigning LF-Tags to Data Catalog resources](TBAC-assigning-tags.md "TBAC-assigning-tags.md").
4. Eduardo assigns the LF-Tag `module=customers` to the table
   `Custs`.
5. Michael makes the following grant to data engineer Sandra (in pseudo-code).

```
GRANT (SELECT, INSERT ON TABLES) ON TAGS module=customers TO Sandra WITH GRANT OPTION
```

6. Sandra makes the following grant to data analyst Maria.

```
GRANT (SELECT ON TABLES) ON TAGS module=customers TO Maria
```

Maria can now run queries on the `Custs` table.

###### See also

- [Metadata access control](access-control-metadata.md "access-control-metadata.md")

## Comparison of Lake Formation tag-based access control to IAM attribute-based access

control

Attribute-based access control (ABAC) is an authorization strategy that defines
permissions based on attributes. In AWS, these attributes are called _tags_. You can attach tags to IAM resources, including IAM entities (users or
roles) and to AWS resources. You can create a single ABAC policy or small set of policies
for your IAM principals. These ABAC policies can be designed to allow operations when the
principal's tag matches the resource tag. ABAC is helpful in environments that are growing
rapidly and helps with situations where policy management becomes cumbersome.

Cloud security and governance teams use IAM to define access policies and security
permissions for all resources including Amazon S3 buckets, Amazon EC2 instances and any
resources you can reference with an ARN. The IAM policies define broad (coarse-grained)
permissions to your data lake resources, for example, to allow or deny access at
Amazon S3 bucket or prefix level or database level. For more information about IAM
ABAC, see [What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

For example, you can create three roles with the `project-access` tag key.
Set the tag value of the first role to `Dev`, the second to
`Marketing`, and the third to `Support`. Assign tags with the
appropriate value to resources. You can then use a single policy that allows access when the
role and the resource are tagged with the same value for `project-access`.

Data governance teams use Lake Formation to define fine-grained permissions to specific data lake
resources. LF-Tags are assigned to Data Catalog resources (databases, tables, and columns) and
are granted to principals. A principal with LF-Tags that match the LF-Tags of a resource
can access that resource. Lake Formation permissions are secondary to IAM permissions. For example,
if IAM permissions don't allow a user access to a data lake, Lake Formation doesn't grant access to
any resource within that data lake to that user, even if the principal and resource have
matching LF-Tags.

Lake Formation tag-based access control (LF-TBAC) works with IAM ABAC to provide additional
levels of permissions for your Lake Formation data and resources.

- **Lake Formation TBAC permissions scale with innovation.** It's
  no longer necessary for an administrator to update existing policies to allow access to
  new resources. For example, assume that you use an IAM ABAC strategy with the
  `project-access` tag to provide access to specific databases within Lake Formation.
  Using LF-TBAC, the LF-Tag `Project=SuperApp` is assigned to specific tables
  or columns, and the same LF-Tag is granted to a developer for that project. Through
  IAM, the developer can access the database, and LF-TBAC permissions grant the
  developer further access to specific tables or columns within tables. If a new table is
  added to the project, the Lake Formation administrator only needs to assign the tag to the new
  table for the developer to be given access to the table.
- **Lake Formation TBAC requires fewer IAM policies.** Because
  you use IAM policies to grant high level access to Lake Formation resources and Lake Formation TBAC for
  managing more precise data access, you create fewer IAM policies.
- **Using Lake Formation TBAC, teams can change and grow quickly.**
  This is because permissions for new resources are automatically granted based on
  attributes. For example, if a new developer joins the project, it's easy to grant this
  developer access by associating the IAM role to the user and then assigning the
  required LF-Tags to the user. You don't have to change the IAM policy to support a new
  project or to create new LF-Tags.
- **Finer-grained permissions are possible using Lake Formation
  TBAC.** IAM policies grant access to the top-level resources, such as
  Data Catalog databases or tables. Using **Lake Formation TBAC**, you can
  grant access to specific tables or columns that contain specific data values.

###### Note

IAM tags are not the same as LF-Tags. These tags are not interchangeable.
LF-Tags are used to grant Lake Formation permissions and IAM tags are used to define IAM
policies.
