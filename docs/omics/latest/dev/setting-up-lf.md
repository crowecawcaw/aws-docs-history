# Configuring Lake Formation to use HealthOmics

###### Important

AWS HealthOmics variant stores and annotation stores are no longer open to new customers.
Existing customers can continue to use the service as normal.
For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

Before you use Lake Formation to manage HealthOmics data stores, perform the following Lake Formation configuration procedures.

###### Topics

- [Creating or verify Lake Formation administrators](#create-lf-admins "#create-lf-admins")
- [Creating resource links using the Lake Formation console](#create-resource-links "#create-resource-links")
- [Configuring permissions for AWS RAM resource shares](#configure-lf-permissions "#configure-lf-permissions")

## Creating or verify Lake Formation administrators

Before you can create a data lake in Lake Formation, you define one or more administrators.

Administrators are users and roles with permissions to create resource links. You set up data lake
administrators per account per region.

###### Create an admin user in the Lake Formation console

1. Open the AWS Lake Formation console: [Lake Formation console](https://console.aws.amazon.com//lakeformation "https://console.aws.amazon.com//lakeformation")
2. If the console displays the **Welcome to Lake Formation** panel, choose **Get started**.

Lake Formation adds you to the **Data lake administrators** table. 3. Otherwise, from the left menu, choose **Administative roles and tasks**. 4. Add any additional administrators as required.

## Creating resource links using the Lake Formation console

To make a shared resource that users can query, the default access controls must be disabled. To learn more
about disabling default access controls, see [Changing the default security
settings for your data lake](../../../lake-formation/latest/dg/change-settings.md "../../../lake-formation/latest/dg/change-settings.md") in the Lake Formation documentation. You can create resource links individually or as
a group, so that you can access data in Amazon Athena or other AWS services (such as Amazon EMR).

###### Creating resource links in the AWS Lake Formation console and sharing them with HealthOmics Analytics

users

1. Open the AWS Lake Formation console: [Lake Formation console](https://console.aws.amazon.com//lakeformation "https://console.aws.amazon.com//lakeformation")
2. In the primary navigation bar, choose **Databases**.
3. In the **Databases** table, select the desired database.
4. From the **Create** menu, choose **Resource link**.
5. Enter a **Resource link name**. If you plan to access the database from Athena, enter a name
   using only lowercase letters (up to 256 characters).
6. Choose **Create**.
7. The new resource link is now listed under **Databases**.

### Grant access to the shared resource using the Lake Formation console

A Lake Formation database administrator can grant access to the shared resource using the following procedure.

1. Open the AWS Lake Formation console: [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com//lakeformation "https://console.aws.amazon.com//lakeformation")
2. In the primary navigation bar, choose **Databases**.
3. On the **Databases** page, select the resource link you previously created.
4. From the **Actions** menu, choose **Grant on target**.
5. On the **Grant data permissions** page under
   **Principals**, choose **IAM users or
   roles**.
6. From the **IAM users or roles** drop-down menu, find the user to which you want to
   grant access.
7. Next, under **LF-Tags or catalog resources** card, select the
   **Named data catalog resources** option.
8. From the **Tables-optional** drop-down menu, select **All Tables** or
   the table that you previously created.
9. In the **Table permissions** card, under **Table
   permissions** choose **Describe** and
   **Select**.
10. Next, choose **Grant**.

To view the Lake Formation permissions, choose **Data lake permissions** from the primary navigation
pane. The table shows the available databases and resource links.

## Configuring permissions for AWS RAM resource shares

In the AWS Lake Formation console, view the permissions by choosing **Data lake
permissions** in the primary navigation bar. On the **Data
permissions** page, you can view a table that shows the **Resource
types**, **Databases**, and `ARN` that's
related to a shared resource under **RAM Resource Share**. If you need to
accept an AWS Resource Access Manager (AWS RAM) resource share, AWS Lake Formation notifies you in the console.

HealthOmics can implicitly accept the AWS RAM resource shares during store creation. To accept
the AWS RAM resource share, the IAM user or role that calls the
`CreateVariantStore` or `CreateAnnotationStore` API operations must
allow the following actions:

- `ram:GetResourceShareInvitations` - This action allows HealthOmics to find
  the invitations.
- `ram:AcceptResourceShareInvitation` - This action allows HealthOmics to
  accept the invitation by using an FAS token.

Without these permissions, you see an authorization error during store creation.

Here is a sample policy that includes these actions. Add this policy to the IAM user or role
that accepts the AWS RAM resource share.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "omics:*",
 "ram:AcceptResourceShareInvitation",
 "ram:GetResourceShareInvitations"
 ],
 "Resource": "*"
 }
 ]
}`

```
