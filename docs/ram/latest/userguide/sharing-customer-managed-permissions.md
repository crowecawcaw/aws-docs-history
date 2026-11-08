

# Sharing and using customer managed permissions across accounts in AWS RAM
<a name="sharing-customer-managed-permissions"></a>

You can share a customer managed permission that you own the same way that you share other resources: add it to a resource share as a resource of type `ram:Permission`. You can share it with other AWS accounts, organizational units (OUs), your entire organization, or IAM roles and users in other accounts. Each account can then use your customer managed permission in its own resource shares instead of creating its own copy.

An account that receives a shared customer managed permission can view it and associate it with its own resource shares. It can't modify, version, deprecate, delete, tag, or reshare the customer managed permission. Only you, the owner, can do those things.

If you share a parameterized managed permission, each receiving account supplies its own parameter values when it associates the permission with its resource shares. For more information, see [Using parameterized managed permissions in AWS RAM](parameterized-managed-permissions.md).

**Topics**
+ [Share a customer managed permission with other accounts](#share-cmp)
+ [Discover and use shared customer managed permissions](#use-shared-cmp)
+ [Stop sharing a customer managed permission](#unshare-cmp)
+ [Considerations for shared customer managed permissions](#shared-cmp-considerations)

## Share a customer managed permission with other accounts
<a name="share-cmp"></a>

To share a customer managed permission, create a resource share that includes the customer managed permission as a resource, or add the customer managed permission to an existing resource share. AWS RAM associates the AWS managed permission `AWSRAMDefaultPermissionRAMCustomerManagedPermission` with the `ram:Permission` resource type. With this managed permission, the receiving accounts can view the customer managed permission and its versions and associate it with their own resource shares.

When you add a customer managed permission to a resource share, AWS RAM updates the resource-based policy of the customer managed permission on your behalf. For this to work:
+ The principal that makes the request needs permission for the `ram:PutCustomerManagedPermissionPolicy` and `ram:DeleteCustomerManagedPermissionPolicy` actions on the customer managed permission.
+ These are permission-only actions. AWS RAM uses them only when it acts on your request, and you can't call them directly.
+ If the principal doesn't have these permissions, the resource association fails with the status message `Association failed because the caller was not authorized.`

------
#### [ Console ]

**To share a customer managed permission with other accounts**

1. Open the **[Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions:)** and choose the customer managed permission that you want to share. On the details page, choose **Create resource share**.

   Alternatively, open **[Shared by me : Resource shares](https://console.aws.amazon.com/ram/home#OwnedResourceShares:)** and choose **Create resource share**.

1. Enter a name for the resource share.

1. Under **Resources**, for **Select resource type**, choose **RAM Permissions**, and then select the customer managed permission that you want to share.

1. On the **Associate managed permissions** page, keep `AWSRAMDefaultPermissionRAMCustomerManagedPermission` for the `ram:Permission` resource type.

1. Under **Principals**, add the AWS accounts, OUs, organization, or IAM roles and users in other accounts that you want to share with.

1. Review your configuration and choose **Create resource share**.

------
#### [ AWS CLI ]

**To share a customer managed permission with other accounts**
+ Run the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command. Specify the ARN of the customer managed permission as a resource, and specify the principals to share it with.

  The following example shares a customer managed permission with another AWS account.

  ```
  $ aws ram create-resource-share \
      --name SharedParameterPermissions \
      --resource-arns arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam \
      --principals 111122223333
  {
      "resourceShare": {
          "resourceShareArn": "arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
          "name": "SharedParameterPermissions",
          "owningAccountId": "123456789012",
          "allowExternalPrincipals": true,
          "status": "ACTIVE",
          "creationTime": 1763300000.000,
          "lastUpdatedTime": 1763300000.000,
          "featureSet": "STANDARD"
      }
  }
  ```

------

You can share a customer managed permission only with other AWS accounts, OUs, your organization, or IAM roles and users in other accounts. You can't share a customer managed permission with service principals, and you can't share AWS managed permissions.

## Discover and use shared customer managed permissions
<a name="use-shared-cmp"></a>

You can find and use a shared customer managed permission after you accept the resource share invitation. If you're in the same organization and sharing with AWS Organizations is turned on, you can use it right away.

------
#### [ Console ]

**To discover and use a shared customer managed permission**

1. Open the **[Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions:)**. Customer managed permissions that are shared with you show **Shared with me** in the **Ownership** column.

1. Choose a shared customer managed permission to view its policy template, versions, and any template parameters.

1. When you create or update one of your resource shares, choose the shared customer managed permission on the **Associate managed permissions** page for its resource type.

------
#### [ AWS CLI ]

**To discover and use a shared customer managed permission**

1. Run the [list-permissions](https://docs.aws.amazon.com/cli/latest/reference/ram/list-permissions.html) command with `--permission-type CUSTOMER_MANAGED` and `--resource-owner OTHER-ACCOUNTS`. The response lists the customer managed permissions that other accounts share with you, with `resourceOwner` set to `OTHER-ACCOUNTS`. The owner's account ID is part of the permission ARN.

   ```
   $ aws ram list-permissions \
       --permission-type CUSTOMER_MANAGED \
       --resource-owner OTHER-ACCOUNTS
   {
       "permissions": [
           {
               "arn": "arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam",
               "version": "2",
               "defaultVersion": true,
               "name": "ParameterReadByTeam",
               "resourceType": "ssm:Parameter",
               "status": "ATTACHABLE",
               "creationTime": 1763400000.000,
               "lastUpdatedTime": 1763400000.000,
               "isResourceTypeDefault": false,
               "permissionType": "CUSTOMER_MANAGED",
               "featureSet": "STANDARD",
               "resourceOwner": "OTHER-ACCOUNTS"
           }
       ]
   }
   ```

1. Run the [associate-resource-share-permission](https://docs.aws.amazon.com/cli/latest/reference/ram/associate-resource-share-permission.html) command to associate the shared customer managed permission with your resource share.
   + If the customer managed permission declares template parameters, include `--permission-template-parameters`.
   + If the resource share already has a managed permission for that resource type, include `--replace`.

   ```
   $ aws ram associate-resource-share-permission \
       --resource-share-arn arn:aws:ram:us-east-1:111122223333:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333 \
       --permission-arn arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam \
       --permission-template-parameters '[{"name":"teams","values":["analytics"]},{"name":"environment","values":["prod"]}]' \
       --replace
   {
       "returnValue": true
   }
   ```

------

## Stop sharing a customer managed permission
<a name="unshare-cmp"></a>

To stop sharing a customer managed permission, remove it or the principals from the resource share, or delete the resource share. After you stop sharing it with an account, the following apply:
+ The account's existing resource shares that use the customer managed permission continue to work.
+ The account no longer sees the customer managed permission in `list-permissions`, and it can't associate the customer managed permission with any more resource shares.
+ The account can still disassociate the customer managed permission from its existing resource shares.

------
#### [ Console ]

**To stop sharing a customer managed permission**

1. Open **[Shared by me : Resource shares](https://console.aws.amazon.com/ram/home#OwnedResourceShares:)**.

1. Choose the resource share that contains the customer managed permission, and choose **Modify**.

1. Remove the customer managed permission or the principals from the resource share, and then complete the wizard. Alternatively, delete the resource share.

------
#### [ AWS CLI ]

**To stop sharing a customer managed permission**
+ Run the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command to remove the customer managed permission or the principals from the resource share.

  ```
  $ aws ram disassociate-resource-share \
      --resource-share-arn arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 \
      --resource-arns arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam
  {
      "resourceShareAssociations": [
          {
              "resourceShareArn": "arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
              "associatedEntity": "arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam",
              "associationType": "RESOURCE",
              "status": "DISASSOCIATING",
              "external": false
          }
      ]
  }
  ```

------

## Considerations for shared customer managed permissions
<a name="shared-cmp-considerations"></a>

**See which resource shares use your customer managed permission**  
To list the resource shares in other AWS accounts that use your customer managed permission, run the [list-permission-associations](https://docs.aws.amazon.com/cli/latest/reference/ram/list-permission-associations.html) command with `--permission-arn` and `--resource-owner OTHER-ACCOUNTS`. Without `--resource-owner OTHER-ACCOUNTS`, the command lists only your own resource shares. In the console, the permission details page shows the same information under **Cross-account usage**.  

```
$ aws ram list-permission-associations \
    --permission-arn arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam \
    --resource-owner OTHER-ACCOUNTS
```

**Deletion is blocked while the customer managed permission is in use**  
You can't delete a customer managed permission while any resource share in any AWS account uses it. The request fails with an `OperationNotPermittedException` error. To retire a shared customer managed permission:  

1. Deprecate it so that no one can associate it with more resource shares. For more information, see [Deprecate a customer managed permission](create-customer-managed-permissions.md#deprecate_cmp).

1. Ask the accounts that use it to disassociate it or to replace it with another managed permission.

1. After the last association is removed, delete it.

**Versions**  
When you create a new version of a shared customer managed permission, it becomes the default version immediately. Accounts that use the customer managed permission can associate only the default version. Their existing resource shares keep the version that they use until they update them.

**Regional scope**  
A customer managed permission exists only in the AWS Region where you create it. You can share it only in that Region, and the receiving accounts can use it only for resource shares in that Region.