# View policy summaries

You can view the policy summaries for any policies that are attached to an IAM user or
role. For managed policies, you can view policy summaries on the **Policies**
page. If your policy does not include a policy summary, see [Missing policy summary](troubleshoot_policies.md#missing-policy-summary "troubleshoot_policies.md#missing-policy-summary") to learn why.

## Viewing policy summaries

from the **Policies** page

You can view the policy summary for managed policies on the **Policies**
page.

###### To view the policy summary from the **Policies** page

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, choose the name of the policy that you want to view.
4. On the **Policy details** page for the policy, view the
   **Permissions** tab to see the policy summary.

## Viewing a policy

summary for a policy attached to a user

You can view the policy summary for any policies that are attached to an
IAM user.

###### To view the summary for a policy attached to a user

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Users** from the navigation pane.
3. In the list of users, choose the name of the user whose policy you want to
   view.
4. On the **Summary** page for the user, view the
   **Permissions** tab to see the list of policies that are attached to
   the user directly or from a group.
5. In the table of policies for the user, expand the row of the policy that you want to
   view.

## Viewing a policy

summary for a policy attached to a role

You can view the policy summary for any policies that are attached to a role.

###### To view the summary for a policy attached to a role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. In the list of roles, choose the name of the role whose policy you want to
   view.
4. On the **Summary** page for the role, view the
   **Permissions** tab to see the list of policies that are attached to
   the role.
5. In the table of policies for the role, expand the row of the policy that you want to
   view.

## Editing policies to fix warnings

While viewing a policy summary, you might find a typo or notice that the policy does not
provide the permissions that you expected. You cannot edit a policy summary directly. However,
you can edit a customer managed policy using the visual policy editor, which catches many of
the same errors and warnings that the policy summary reports. You can then view the changes in
the policy summary to confirm that you fixed all of the issues. To learn how to edit an inline
policy, see [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md"). You cannot edit AWS managed
policies.

You can edit a policy for your policy summary using the **Visual**
option.

###### To edit a policy for your policy summary using the **Visual**

option

1. Open the policy summary as explained in the previous procedures.
2. Choose **Edit**.

If you are on the **Users** page and choose to edit a customer
managed policy that is attached to that user, you are redirected to the
**Policies** page. You can edit customer managed policies only on the
**Policies** page. 3. Choose the **Visual** option to view the editable visual
representation of your policy. IAM might restructure your policy to optimize it for the
visual editor and to make it easier for you to find and fix any problems. The warnings and
error messages on the page can guide you to fix any issues with your policy. For more
information about how IAM restructures policies, see [Policy restructuring](troubleshoot_policies.md#troubleshoot_viseditor-restructure "troubleshoot_policies.md#troubleshoot_viseditor-restructure"). 4. Edit your policy and choose **Next** to see your changes reflected in
the policy summary. If you still see a problem, choose **Previous** to
return to the editing screen. 5. Choose **Save changes** to save your changes.

You can edit a policy for your policy summary using the **JSON**
option.

###### To edit a policy for your policy summary using the **JSON**

option

1. Open the policy summary as explained in the previous procedures.
2. You can use the **Summary** and **JSON** buttons to
   compare the policy summary to the JSON policy document. You can use this information to
   determine which lines in the policy document you want to change.
3. Choose **Edit** and then choose the **JSON** option
   to edit the JSON policy document.

###### Note

You can switch between the **Visual** and **JSON**
editor options any time. However, if you make changes or choose
**Next** in the **Visual** editor option, IAM
might restructure your policy to optimize it for the visual editor. For more
information, see [Policy restructuring](troubleshoot_policies.md#troubleshoot_viseditor-restructure "troubleshoot_policies.md#troubleshoot_viseditor-restructure").

If you are on the **Users** page and choose to edit a customer
managed policy that is attached to that user, you are redirected to the
**Policies** page. You can edit customer managed policies only on the
**Policies** page. 4. Edit your policy.
Resolve any security warnings, errors, or general warnings generated during [policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md"), and then choose **Next**.
If you still see a problem, choose
**Previous** to return to the editing screen. 5. Choose **Save changes** to save your changes.
