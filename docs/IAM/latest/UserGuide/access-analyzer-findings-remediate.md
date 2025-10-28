# Resolve IAM Access Analyzer findings

## Resolving resource

findings

To resolve external and internal access findings generated from unintended access, you
should modify the policy statement to remove the permissions that allow access to the
identified resource.

For findings related to Amazon S3 buckets, use the Amazon S3 console to configure the
permissions on the bucket.

For IAM roles, use the IAM console to [modify the trust policy](id_roles_manage_modify.md#roles-managingrole_edit-trust-policy "id_roles_manage_modify.md#roles-managingrole_edit-trust-policy") for the listed IAM role.

For other supported resources, use the console to modify the policy statements that
resulted in a generated finding.

After making a change to resolve a resource finding, such as modifying a policy
applied to an IAM role, IAM Access Analyzer will scan the resource again. If the access to
the resource is removed, the status of the finding is changed to
**Resolved**. The finding will then be displayed in the resolved
findings list instead of the active findings list.

###### Note

This does not apply to **Error** findings. When IAM Access Analyzer is
not able to analyze a resource, it will generate an error finding. If you resolve
the issue that prevented IAM Access Analyzer from analyzing the resource, the error
finding will be removed completely instead of changing to a resolved finding. For
more information, see [IAM Access Analyzer error findings](access-analyzer-error-findings.md "access-analyzer-error-findings.md").

If the changes you made resulted in external or internal access to the resource, but
in a different way, such as with a different principal or for a different permission,
IAM Access Analyzer will resolve the original finding and generate a new
**Active** finding. If the changes you made resulted in internal
errors or access denied errors, all active non-error findings linked to the specific
access of the resource are resolved and a new error finding is generated.

###### Note

For external access analyzers, it may take up to 30 minutes after a policy is
modified for IAM Access Analyzer to analyze the resource again and then update the
finding.

For internal access analyzers, it might take several minutes or hours for
IAM Access Analyzer to analyze the resource again and then update the finding.
IAM Access Analyzer automatically rescans all policies every 24 hours.

Resolved findings are deleted 90 days after the last update to the finding
status.

## Resolving unused access

findings

IAM Access Analyzer provides recommended steps to resolve unused access analyzer findings
based on the type of finding.

After you make a change to resolve an unused access finding, the status of the finding
is changed to **Resolved** the next time the unused access analyzer
runs. The finding is no longer displayed in the active findings list and instead is
displayed in the resolved findings list. If you make a change that only partially
addresses an unused access finding, the existing finding is changed to
**Resolved** but a new finding is generated. For example, if you
remove only some of the unused permissions in a finding, but not all of them.

IAM Access Analyzer charges for unused access analysis based on the number of IAM roles
and users analyzed per month. For more details about pricing, see [IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

### Resolving

unused permission findings

For unused permission findings, IAM Access Analyzer can recommend policies to remove
from an IAM user or role and provide new policies to replace existing
permissions policies. Policy recommendation is not supported for the following
scenarios:

- The unused permission finding is for an IAM user that is in a user
  group.
- The unused permission finding is for an IAM role for IAM Identity Center.
- The unused permission finding has an existing permissions policy that
  includes the `notAction` element.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Unused access**.
3. Choose a finding with the **Finding type** of
   **Unused permissions**.
4. In the **Recommendations** section, if there are policies
   listed in the **Recommended policy** column, choose
   **Preview policy** to view the existing policy with the
   recommended policy to replace the existing policy. If there are mutliple
   recommended policies, you can choose **Next policy** and
   **Previous policy** to view each existing and
   recommended policy.
5. Choose **Download JSON** to download a .zip file with
   JSON files of all the recommended policies.
6. Create and attach the recommended policies to the IAM user or role. For
   more information, see [Changing permissions for a user (console)](id_users_change-permissions.md#users_change_permissions-change-console "id_users_change-permissions.md#users_change_permissions-change-console") and [Modifying a role permissions policy (console)](roles-managingrole-editing-console.md#roles-modify_permissions-policy "roles-managingrole-editing-console.md#roles-modify_permissions-policy").
7. Remove the policies listed in the **Existing permissions
   policy** column from the IAM user or role. For more
   information, see [Removing a permissions from a user (console)](id_users_change-permissions.md#users_change_permissions-remove-policy-console "id_users_change-permissions.md#users_change_permissions-remove-policy-console") and [Modifying a role permissions policy (console)](roles-managingrole-editing-console.md#roles-modify_permissions-policy "roles-managingrole-editing-console.md#roles-modify_permissions-policy").

### Resolving unused

role findings

For unused role findings, IAM Access Analyzer recommends deleting the unused IAM
role.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Unused access**.
3. Choose a finding with the **Finding type** of
   **Unused role**.
4. In the **Recommendations** section, review the details of
   the IAM role.
5. Delete the IAM role. For more information, see [Deleting an IAM role (console)](id_roles_manage_delete.md#roles-managingrole-deleting-console "id_roles_manage_delete.md#roles-managingrole-deleting-console").

### Resolving

unused access key findings

For unused access key findings, IAM Access Analyzer recommends deactivating or
deleting the unused access key.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Unused access**.
3. Choose a finding with the **Finding type** of
   **Unused access keys**.
4. In the **Recommendations** section, review the details of
   the access key.
5. Deactivate or delete the access key. For more information, see [Managing access keys (console)](id_credentials_access-keys.md#Using_CreateAccessKey "id_credentials_access-keys.md#Using_CreateAccessKey").

### Resolving

unused password findings

For unused password findings, IAM Access Analyzer recommends deleting the unused
password for the IAM user.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Unused access**.
3. Choose a finding with the **Finding type** of
   **Unused password**.
4. In the **Recommendations** section, review the details of
   the IAM user.
5. Delete the password for the IAM user. For more information, see [Creating, changing, or deleting an IAM user password
   (console)](id_credentials_passwords_admin-change-user.md#id_credentials_passwords_admin-change-user_console "id_credentials_passwords_admin-change-user.md#id_credentials_passwords_admin-change-user_console").
