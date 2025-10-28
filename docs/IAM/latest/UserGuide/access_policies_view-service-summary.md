# View service summaries

You can view a service summary for each service listed in the policy summary that grants
permissions.

## Viewing service summaries

from the **Policies** page

You can view the service summary for managed policies on the **Policies**
page.

###### To view the service summary for a managed policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, choose the name of the policy that you want to view.
4. On the **Policy details** page for the policy, view the
   **Permissions** tab to see the policy summary.
5. In the policy summary list of services, choose the name of the service that you want
   to view.

## Viewing a service

summary for a policy attached to a user

You can view the service summary for any policies that are attached to an
IAM user.

###### To view the service summary for a policy attached to a user

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. In the list of users, choose the name of the user whose policy you want to
   view.
4. On the **Summary** page for the user, view the
   **Permissions** tab to see the list of policies that are attached to
   the user directly or from a group.
5. In the table of policies for the user, choose the name of the policy that you want to
   view.

If you are on the **Users** page and choose to view the service
summary for a policy that is attached to that user, you are redirected to the
**Policies** page. You can view service summaries only on the
**Policies** page. 6. Choose **Summary**. In the policy summary list of services, choose
the name of the service that you want to view.

###### Note

If the policy that you select is an inline policy that is attached directly to the
user, then the service summary table appears. If the policy is an inline policy attached
from a group, then you are taken to the JSON policy document for that group. If the
policy is a managed policy, then you are taken to the service summary for that policy on
the **Policies** page.

## Viewing a service

summary for a policy attached to a role

You can view the policy summary for any policies that are attached to a role.

###### To view the service summary for a policy attached to a role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** from the navigation pane.
3. In the list of roles, choose the name of the role whose policy you want to
   view.
4. On the **Summary** page for the role, view the
   **Permissions** tab to see the list of policies that are attached to
   the role.
5. In the table of policies for the role, choose the name of the policy that you want to
   view.

If you are on the **Roles** page and choose to view the service
summary for a policy that is attached to that user, you are redirected to the
**Policies** page. You can view service summaries only on the
**Policies** page. 6. In the policy summary list of services, choose the name of the service that you want
to view.
