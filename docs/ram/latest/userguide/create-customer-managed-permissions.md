# Creating and using customer managed

permissions in AWS RAM

AWS Resource Access Manager (AWS RAM) provides at least one AWS managed permission for every resource type that you can
share. However, those managed permissions might not provide [least privilege
access](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") for your sharing use case. When one of the provided AWS managed permissions doesn't
work, you can create your own _customer managed permission_.

Customer managed permissions are managed permissions that you author and maintain by precisely specifying which actions can be performed under which conditions with resources shared using AWS RAM. For example, you want to limit read access for your Amazon VPC IP Address Manager (IPAM) pools, which help you manage your IP addresses at scale. You can create customer managed permissions for your developers to assign IP addresses, but not view the range of IP addresses other developer accounts assign. You can follow the best practice of least privilege, granting only the permissions required to perform tasks on shared resources.

In addition, you can update or delete customer managed permissions as needed.

###### Topics

- [Create a customer managed permission](#create_cmp "#create_cmp")
- [Create a new version of a customer managed permission](#update_mp "#update_mp")
- [Choose a different version to be the
  default for a customer managed permission](#set_new_mp_default_version "#set_new_mp_default_version")
- [Delete a customer managed permission version](#delete_mp_version "#delete_mp_version")
- [Delete a customer managed permission](#delete_mp "#delete_mp")

## Create a customer managed permission

Customer managed permissions are specific to an AWS Region. Make sure that you create this customer managed permission in the
appropriate Region.

Console

###### To create a customer managed permission

1. Do one of the following:
   - Navigate to the **[Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions: "https://console.aws.amazon.com/ram/home#Permissions:")**, and choose
     **Create a customer managed
     permission**.
   - Navigate directly to the **[Create a customer managed permission](https://console.aws.amazon.com/ram/home#CreatePermission: "https://console.aws.amazon.com/ram/home#CreatePermission:")** page
     in the console.

2. For **Customer managed permission details**, enter a customer managed
   permission name.
3. Choose the resource type to which this managed permission
   applies.
4. For **Policy template**, you define which
   operations are allowed to be performed on this resource type.
   - You can choose **Import managed
     permission** to use actions from an existing
     managed permission.
   - Select or deselect access level information to meet your
     requirements in the visual editor.
   - Add or modify conditions using the **JSON
     editor**.

5. (Optional) To attach tags to the managed permission, for
   **Tags**, enter a tag key and value. Add
   additional tags by choosing **Add new tag**. Repeat
   this step as needed.
6. When you're done, choose **Create customer managed permission**.

AWS CLI

###### To create a customer managed permission

- Run the command [create-permission](../../../cli/latest/reference/ram/create-permission.md "../../../cli/latest/reference/ram/create-permission.md") and specify a name, the resource type
  that the customer managed permission applies to, and the policy template body text.

The following example command creates a managed permission for the
`imagebuilder:Component` resource type.

```
`$` `aws ram create-permission \
 --name TestCMP \
 --resource-type imagebuilder:Component \
 --policy-template "{\"Effect\":\"Allow\",\"Action\":[\"imagebuilder:ListComponents\"]}"``{
 "permission": {
 "arn": "arn:aws:ram:us-east-1:123456789012:permission/TestCMP",
 "version": "1",
 "defaultVersion": true,
 "isResourceTypeDefault": false,
 "name": "TestCMP",
 "resourceType": "imagebuilder:Component",
 "status": "ATTACHABLE",
 "creationTime": 1680033769.401,
 "lastUpdatedTime": 1680033769.401
 }
}`
```

## Create a new version of a customer managed permission

If the use case for your customer managed permission changes, you can create a new version of the managed
permission. This doesn't affect your existing resource shares, only the new resource
shares going forward that use this customer managed permission.

Each managed permission can have up to five versions, but you can associate only the
default version.

Console

###### To create a new version of a customer managed permission

1. Navigate to the **[Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions: "https://console.aws.amazon.com/ram/home#Permissions:")**.
2. Filter the list of managed permissions by **Customer
   managed**, or search for the name of the customer managed permission that you
   want to change.
3. From the managed permission details page, under the
   **Managed permission versions** section, choose
   **Create version**.
4. For **Policy template**, you can add or remove
   actions and conditions with the visual editor or JSON editor.

You also have the option to choose **Import managed
permission** to use an existing policy template. 5. When you're finished, choose **Create version**
at the bottom of the page.

AWS CLI

###### To create a new version of a customer managed permission

1. Find the Amazon Resource Name (ARN) of the managed permission for
   which you want create a new version. Do this by calling [list-permissions](../../../cli/latest/reference/ram/list-permissions.md "../../../cli/latest/reference/ram/list-permissions.md") with the `--permission-type
CUSTOMER_MANAGED` parameter to include only customer managed permissions.

```
`$` `aws ram-cmp list-permissions --permission-type CUSTOMER_MANAGED``{
 "permissions": [
 {
 "arn": "arn:aws:ram:us-east-1:123456789012:permission/TestCMP",
 "version": "2",
 "defaultVersion": true,
 "isResourceTypeDefault": false,
 "name": "TestCMP",
 "permissionType": "CUSTOMER_MANAGED",
 "resourceType": "imagebuilder:Component",
 "status": "ATTACHABLE",
 "creationTime": 1680035597.346,
 "lastUpdatedTime": 1680035597.346
 }
 ]
}`
```

2. After you have the ARN, you can call the [create-permission-version](../../../cli/latest/reference/ram/create-permission-version.md "../../../cli/latest/reference/ram/create-permission-version.md") operation and provide the
   updated policy template.

```
`$` `aws ram create-permission-version \
 --permission-arn arn:aws:ram:us-east-1:123456789012:permission/TestCMP \
 --policy-template {"Effect":"Allow","Action":["imagebuilder:ListComponents"]}`
`{
 "permission": {
 "arn": "arn:aws:ram:us-east-1:123456789012:permission/TestCMP",
 "version": "2",
 "defaultVersion": true,
 "isResourceTypeDefault": false,
 "name": "TestCMP",
 "status": "ATTACHABLE",
 "resourceType": "imagebuilder:Component",
 "permission": "{\"Effect\":\"Allow\",\"Action\":[\"imagebuilder:ListComponents\"]}",
 "creationTime": 1680038973.79,
 "lastUpdatedTime": 1680038973.79
 }
}`
```

The output includes the version number of the new version.

## Choose a different version to be the

default for a customer managed permission

You can set another customer managed permission version as the new default version.

Console

###### To set a new default version for a customer managed permission

1. Navigate to the **[Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions: "https://console.aws.amazon.com/ram/home#Permissions:")**.
2. Filter the list of managed permissions by **Customer
   managed**, or search for the name of the customer managed permission that you
   want to change.
3. From the Customer managed permission details page, under the **Managed
   permission versions** section, use the dropdown list to
   choose the version that you want to set as the new default.
4. Choose **Set as default version**.
5. When the dialog box appears, confirm that you want this version to
   be the default for all new resource shares that use this customer managed permission. If
   you agree, choose **Set as default
   version**.

AWS CLI

###### To set a new default version for a customer managed permission

1. Find the version number that you want to set as the default
   version by calling [list-permission-versions](../../../cli/latest/reference/ram/list-permission-versions.md "../../../cli/latest/reference/ram/list-permission-versions.md").

The following example command retrieves the current versions for
the specified managed permission.

```
`$` `aws ram list-permission-versions \
 --permission-arn arn:aws:ram:us-east-1:123456789012:permission/TestCMP``{
 "permissions": [
 {
 "arn": "arn:aws:ram:us-east-1:123456789012:permission/TestCMP",
 "version": "1",
 "defaultVersion": false,
 "isResourceTypeDefault": false,
 "name": "TestCMP",
 "permissionType": "CUSTOMER_MANAGED",
 "featureSet": "STANDARD",
 "resourceType": "imagebuilder:Component",
 "status": "UNATTACHABLE",
 "creationTime": 1680033769.401,
 "lastUpdatedTime": 1680035597.345
 },
 {
 "arn": "arn:aws:ram:us-east-1:123456789012:permission/TestCMP",
 "version": "2",
 "defaultVersion": true,
 "isResourceTypeDefault": false,
 "name": "TestCMP",
 "permissionType": "CUSTOMER_MANAGED",
 "featureSet": "STANDARD",
 "resourceType": "imagebuilder:Component",
 "status": "ATTACHABLE",
 "creationTime": 1680035597.346,
 "lastUpdatedTime": 1680035597.346
 }
 ]
}`
```

2. After you have the version number to set as default, you can call
   the [set-default-permission-version](../../../cli/latest/reference/ram/set-default-permission-version.md "../../../cli/latest/reference/ram/set-default-permission-version.md") operation.

```
`$` `aws ram-cmp set-default-permission-version \
 --permission-arn arn:aws:ram:us-east-1:123456789012:permission/TestCMP \
 --version 2`
```

This command returns no output if successful. You can run [list-permission-versions](../../../cli/latest/reference/ram/list-permission-versions.md "../../../cli/latest/reference/ram/list-permission-versions.md") again and verify that the
`defaultVersion` field of the chosen version is now
set to `true`.

## Delete a customer managed permission version

You can have up to five versions of each customer managed permission. When a version is no longer needed,
and not in use, you can delete it. You can't delete the default version of a customer managed permission.
Deleted versions remain visible in the console for up to two hours with a deleted status
before they are completely removed.

Console

**To delete a customer managed permission version**

1. Navigate to the **[Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions: "https://console.aws.amazon.com/ram/home#Permissions:")**.
2. Filter the list of managed permissions by **Customer
   managed**, or search for the name of the customer managed permission with the
   version that you want to delete.
3. Make sure that the version you want to delete isn't currently the
   default.
4. For the **Versions** section of the page, choose
   the **Associated resource shares** tab to see if
   any shares use this version.

If there are any shares associated, you must change the customer managed permission
version before you can delete this version. 5. Choose **Delete version** on the right side of
the **Version** section. 6. In the confirmation dialog box, select **Delete**
to confirm that you want to delete this version of your
customer managed permission.

Choose **Cancel** if you don't want to delete
this version of your customer managed permission.

AWS CLI

###### To delete one version of a customer managed permission

1. Call the [list-permission-versions](../../../cli/latest/reference/ram/list-permission-versions.md "../../../cli/latest/reference/ram/list-permission-versions.md") operation to retrieve the
   available version numbers.
2. After you have the version number, provide it as a parameter to
   [delete-permission-version](../../../cli/latest/reference/ram/delete-permission-version.md "../../../cli/latest/reference/ram/delete-permission-version.md").

```
`$` `aws ram-cmp delete-permission-version \
 --permission-arn arn:aws:ram:us-east-1:123456789012:permission/TestCMP \
 --version 1`
```

This command returns no output if successful. You can run [list-permission-versions](../../../cli/latest/reference/ram/list-permission-versions.md "../../../cli/latest/reference/ram/list-permission-versions.md") again and verify that the
version is no longer included in the output.

## Delete a customer managed permission

If a customer managed permission is no longer needed, and not in use, you can delete it. You can't delete a
customer managed permission that is associated with a resource share. The deleted customer managed permission disappears after two
hours. Until then, it remains visible in the **Managed permission
library** with a deleted status.

Console

**To delete a customer managed permission**

1. Navigate to the **[Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions: "https://console.aws.amazon.com/ram/home#Permissions:")**.
2. Filter the list of managed permissions by **Customer
   managed**, or search for the name of the customer managed permission that you
   want to delete.
3. Confirm there are 0 associated shares from the managed permissions
   list before selecting the customer managed permission.

If there are still resource shares associated with the managed
permission, you must assign another managed permission to all
resource shares before you can continue. 4. In the top right corner of the Customer managed permission details page, choose
**Delete managed permission**. 5. When the confirmation dialog box appears, choose
**Delete** to delete the managed
permission.

AWS CLI

###### To delete a customer managed permission

1. Find the ARN of the managed permission you want to delete by
   calling [list-permissions](../../../cli/latest/reference/ram/list-permissions.md "../../../cli/latest/reference/ram/list-permissions.md") with the `--permission-type
CUSTOMER_MANAGED` parameter to include only customer managed permissions.

```
`$` `aws ram-cmp list-permissions --permission-type CUSTOMER_MANAGED``{
 "permissions": [
 {
 "arn": "arn:aws:ram:us-east-1:123456789012:permission/TestCMP",
 "version": "2",
 "defaultVersion": true,
 "isResourceTypeDefault": false,
 "name": "TestCMP",
 "permissionType": "CUSTOMER_MANAGED",
 "resourceType": "imagebuilder:Component",
 "status": "ATTACHABLE",
 "creationTime": 1680035597.346,
 "lastUpdatedTime": 1680035597.346
 }
 ]
}`
```

2. After you have the ARN of the managed permission to delete,
   provide it as a parameter to [delete-permission](../../../cli/latest/reference/ram/delete-permission.md "../../../cli/latest/reference/ram/delete-permission.md").

```
`$` `aws ram delete-permission \
 --permission-arn arn:aws:ram:us-east-1:123456789012:permission/TestCMP``{
 "returnValue": true,
 "permissionStatus": "DELETING"
}`
```
