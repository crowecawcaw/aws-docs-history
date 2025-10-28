# Edit IAM policies (console)

A [policy](access_policies.md "access_policies.md") is an entity that, when attached to an
identity or resource, defines their permissions. You can use the AWS Management Console to edit _customer managed policies_ and _inline
policies_ in IAM. AWS managed policies cannot be edited.
The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

For more information about policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md") and the [IAM JSON policy element reference](reference_policies_elements.md "reference_policies_elements.md").

## Prerequisites

Before you change the permissions for a policy, you should review its recent service-level
activity. This is important because you don't want to remove access from a principal (person
or application) who is using it. For more information about viewing last accessed information,
see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Editing customer managed policies

(console)

You can edit customer managed policies to change the permissions that are defined in the
policy from the AWS Management Console. A customer managed policy can have up to five versions. This is
important because if you make changes to a managed policy beyond five versions, the AWS Management Console
prompts you to decide which version to delete. You can also change the default version or
delete a version of a policy before you edit it to avoid being prompted. To learn more about
versions, see [Versioning IAM policies](access_policies_managed-versioning.md "access_policies_managed-versioning.md").

Console

###### To edit a customer managed policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, choose the policy name of the policy to edit. You can
   use the search box to filter the list of policies.
4. Choose the **Permissions** tab, and then choose
   **Edit**.
5. Do one of the following:
   - Choose the **Visual** option to change your policy without
     understanding JSON syntax. You can make changes to the service, actions,
     resources, or optional conditions for each permission block in your policy. You
     can also import a policy to add additional permissions to the bottom of your
     policy. When you are finished making changes, choose **Next**
     to continue.
   - Choose the **JSON** option to modify your policy by typing
     or pasting text in the JSON text box. You can also import a policy to add
     additional permissions to the bottom of your policy.
     Resolve any security warnings, errors, or general warnings generated during [policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md"), and then choose **Next**.

   ###### Note

   You can switch between the **Visual** and
   **JSON** editor options any time. However, if you make
   changes or choose **Next** in the **Visual**
   editor, IAM might restructure your policy to optimize it for the visual
   editor. For more information, see [Policy restructuring](troubleshoot_policies.md#troubleshoot_viseditor-restructure "troubleshoot_policies.md#troubleshoot_viseditor-restructure").

6. On the **Review and save** page, review **Permissions
   defined in this policy** and then choose **Save
   changes** to save your work.
7. If the managed policy already has the maximum of five versions, choosing
   **Save changes** displays a dialog box. To save your new version,
   the oldest non-default version of the policy is removed and replaced with this new
   version. Optionally, you can set the new version as the default policy
   version.

Choose **Save changes** to save your new policy version.

## Setting the

default version of a customer managed policy (console)

You can set a default version of a customer managed policy from the AWS Management Console. You can use
this policy to establish a consistent baseline configuration for permissions across your
organization. All new attachments of the policy will use this standardized set of
permissions.

Console

###### To set the default version of a customer managed policy (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, choose the policy name of the policy to set the default
   version of. You can use the search box to filter the list of policies.
4. Choose the **Policy versions** tab. Select the check box next
   to the version that you want to set as the default version, and then choose
   **Set as default**.

## Deleting a

version of a customer managed policy (console)

You might need to delete a version of a customer managed policy to remove outdated or
incorrect permissions that are no longer needed or pose potential security risks. By
maintaining only necessary versions, you can help ensure that you stay within the limit of
five managed policy versions, allowing room for future updates and refinements. You can delete
a version of a customer managed policy from the AWS Management Console.

Console

###### To delete a version of a customer managed policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose the name of the customer managed policy that has a version you want to
   delete. You can use the search box to filter the list of policies.
4. Choose the **Policy versions** tab. Select the check box next
   to the version that you want to delete. Then choose
   **Delete**.
5. Confirm that you want to delete the version, and then choose
   **Delete**.

## Editing inline policies (console)

You might need to edit a customer managed policy to update or refine the permissions
granted, ensuring they remain aligned with your organization's evolving security requirements
and access control needs. Editing allows you to adjust the policy's JSON document, adding,
modifying, or removing specific actions, resources, or conditions to maintain the principle of
least privilege and adapt to changes in your environment or processes. You can edit an inline
policy from the AWS Management Console.

Console

###### To edit an inline policy for a user, user group, or role

1. In the navigation pane, choose **Users**, **User
   groups**, or **Roles**.
2. Choose the name of the user, user group, or role with the policy that you want
   to modify. Then choose the **Permissions** tab and expand the
   policy.
3. To edit an inline policy, choose **Edit Policy**.
4. Do one of the following:
   - Choose the **Visual** option to change your policy without
     understanding JSON syntax. You can make changes to the service, actions,
     resources, or optional conditions for each permission block in your policy. You
     can also import a policy to add additional permissions to the bottom of your
     policy. When you are finished making changes, choose **Next**
     to continue.
   - Choose the **JSON** option to modify your policy by typing
     or pasting text in the JSON text box. You can also import a policy to add
     additional permissions to the bottom of your policy.
     Resolve any security warnings, errors, or general warnings generated during [policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md"), and then choose **Next**.
     To save your
     changes without affecting the currently attached entities, clear the check box
     for **Save as default version**.

###### Note

You can switch between the **Visual** and
**JSON** editor options any time. However, if you make changes
or choose **Next** in the **Visual** editor,
IAM might restructure your policy to optimize it for the visual editor. For more
information, see [Policy restructuring](troubleshoot_policies.md#troubleshoot_viseditor-restructure "troubleshoot_policies.md#troubleshoot_viseditor-restructure"). 5. On the **Review** page, review the policy summary and then
choose **Save changes** to save your work.
