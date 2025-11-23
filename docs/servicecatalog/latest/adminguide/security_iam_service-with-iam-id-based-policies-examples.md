# Identity-based policy examples for AWS Service Catalog

###### Topics

- [Console access for end users](#permissions-end-users-console "#permissions-end-users-console")
- [Product access for end users](#permissions-end-users-product "#permissions-end-users-product")
- [Example policies for managing provisioned
  products](#example-policies "#example-policies")

## Console access for end users

The \***\*`AWSServiceCatalogEndUserFullAccess`\*\*** and \***\*`AWSServiceCatalogEndUserReadOnlyAccess`\*\*** policies grant access to the AWS Service Catalog
end user console view. When a user who has either of these policies chooses AWS Service Catalog in
the AWS Management Console, the end user console view displays the products they have permission
to launch.

Before end users can successfully launch a product from AWS Service Catalog to
which you give access, you must provide them additional IAM permissions to allow
them to use each of the underlying AWS resources in a product's AWS CloudFormation template.
For example, if a product template includes Amazon Relational Database Service (Amazon RDS), you must grant the
users Amazon RDS permissions to launch the product.

To learn about how to enable end users to launch products while
enforcing least-access permissions to AWS resources, see [Using AWS Service Catalog Constraints](constraints.md "constraints.md").

If you apply the **`AWSServiceCatalogEndUserReadOnlyAccess`** policy, your users have
access to the end user console, but they won't have the permissions that they need
to launch products and manage provisioned products. You can grant these permissions
directly to an end user using IAM, but if you want to limit the access that end
users have to AWS resources, you should attach the policy to a launch role. You then
use AWS Service Catalog to apply the launch role to a launch constraint for the product. For more
information about applying a launch role, launch role limitations, and a sample
launch role, see [AWS Service Catalog Launch Constraints](constraints-launch.md "constraints-launch.md").

###### Note

If you grant users IAM permissions for AWS Service Catalog administrators, the
administrator console view displays instead. Don't grant end users these
permissions unless you want them to have access to the administrator console
view.

## Product access for end users

Before end users can use a product to which you give access, you
must provide them additional IAM permissions to allow them to use each of the
underlying AWS resources in a product's CloudFormation template. For example, if a product
template includes Amazon Relational Database Service (Amazon RDS), you must grant the users Amazon RDS permissions to
launch the product.

If you apply the **`AWSServiceCatalogEndUserReadOnlyAccess`**
policy, your users have access to the end user console view, but they won't have the
permissions that they need to launch products and manage provisioned products. You
can grant these permissions directly to an end user in IAM, but if you want to
limit the access that end users have to AWS resources, you should attach the
policy to a launch role. You then use AWS Service Catalog to apply the launch role to a launch
constraint for the product. For more information about applying a launch role,
launch role limitations, and a sample launch role, see [AWS Service Catalog Launch Constraints](constraints-launch.md "constraints-launch.md").

## Example policies for managing provisioned

products

You can create custom policies to help meet the security requirements of your
organization. The following examples describe how to customize the access level for
each action with support for user, role, and account levels. You can grant users
access to view, update, terminate, and manage provisioned products created only by
that user or created by others also under their role or the account to which they
are logged in. This access is hierarchical — granting account level access
also grants role level access and user level access, while adding role level access
also grants user level access but not account level access. You can specify these in
the policy JSON using a `Condition` block as `accountLevel`,
`roleLevel`, or `userLevel`.

These examples also apply to access levels for AWS Service Catalog API write
operations: `UpdateProvisionedProduct` and
`TerminateProvisionedProduct`, and read operations:
`DescribeRecord`, `ScanProvisionedProducts`, and
`ListRecordHistory`. The `ScanProvisionedProducts` and
`ListRecordHistory` API operations use
`AccessLevelFilterKey` as input, and that key's values correspond to
the `Condition` block levels discussed here (`accountLevel` is
equivalent to an `AccessLevelFilterKey` value of "Account",
`roleLevel` to "Role", and `userLevel` to "User"). For
more information, see the [Service Catalog Developer Guide](../dg.md "../dg.md").

###### Examples

- [Full admin access to provisioned
  products](#full-admin "#full-admin")
- [End-user access to provisioned
  products](#examples-end-user "#examples-end-user")
- [Partial admin access to provisioned
  products](#partial-admin "#partial-admin")

### Full admin access to provisioned

products

The following policy allows full read and write access to provisioned products
and records within the catalog at the account level.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "servicecatalog:*"
 ],
 "Resource":"*",
 "Condition": {
 "StringEquals": {
 "servicecatalog:accountLevel": "self"
 }
 }
 }
 ]
}`

```

This policy is functionally equivalent to the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "servicecatalog:*"
 ],
 "Resource":"*"
 }
 ]
}`

```

Not specifying a `Condition` block
in any policy for AWS Service Catalog is treated as the same as specifying
`"servicecatalog:accountLevel"` access. Note that
`accountLevel` access includes `roleLevel` and
`userLevel` access.

### End-user access to provisioned

products

The following policy restricts access to read and write operations to only the
provisioned products or associated records that the current user created.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:DescribeProduct",
 "servicecatalog:DescribeProductView",
 "servicecatalog:DescribeProvisioningParameters",
 "servicecatalog:DescribeRecord",
 "servicecatalog:ListLaunchPaths",
 "servicecatalog:ListRecordHistory",
 "servicecatalog:ProvisionProduct",
 "servicecatalog:ScanProvisionedProducts",
 "servicecatalog:SearchProducts",
 "servicecatalog:TerminateProvisionedProduct",
 "servicecatalog:UpdateProvisionedProduct"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "servicecatalog:userLevel": "self"
 }
 }
 }
 ]
 }`

```

### Partial admin access to provisioned

products

The two policies below, if both applied to the same user, allow what might be
called a type of "partial admin access" by providing full read-only access and
limited write access. This means the user can see any provisioned product or
associated record within the catalog's account but cannot perform any actions on
any provisioned products or records that aren't owned by that user.

The first policy allows the user access to write operations on the provisioned
products that the current user created, but no provisioned products created by
others. The second policy adds full access to read operations on provisioned
products created by all (user, role, or account).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:DescribeProduct",
 "servicecatalog:DescribeProductView",
 "servicecatalog:DescribeProvisioningParameters",
 "servicecatalog:ListLaunchPaths",
 "servicecatalog:ProvisionProduct",
 "servicecatalog:SearchProducts",
 "servicecatalog:TerminateProvisionedProduct",
 "servicecatalog:UpdateProvisionedProduct"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "servicecatalog:userLevel": "self"
 }
 }
 }
 ]
 }`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:DescribeRecord",
 "servicecatalog:ListRecordHistory",
 "servicecatalog:ScanProvisionedProducts"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "servicecatalog:accountLevel": "self"
 }
 }
 }
 ]
 }`

```
