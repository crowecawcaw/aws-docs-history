# Convert an inline policy to a

managed policy

If you have inline policies in your account, you can convert them to managed policies. To
do this, copy the policy to a new managed policy. Next, attach the new policy to the
identity that has the inline policy. Then delete the inline policy.

## Converting an

inline policy to a managed policy

###### To convert an inline policy to a managed policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User groups**,
   **Users**, or **Roles**.
3. In the list, choose the name of the user group, user, or role that has the
   policy you want to remove.
4. Choose the **Permissions** tab.
5. For IAM groups, select the name of the inline policy that you want to remove.
   For users and roles, choose **Show `n`
   more**, if necessary, and then expand the inline policy that you
   want to remove.
6. Choose **Copy** to copy the JSON policy document for the
   policy.
7. In the navigation pane, choose **Policies**.
8. Choose **Create policy** and then choose the
   **JSON** option.
9. Replace the existing text with your JSON policy text, and then choose
   **Next**.
10. Enter a name and optional description for your policy and choose
    **Create policy**.
11. In the navigation pane, choose **User groups**,
    **Users**, or **Roles**, and again choose
    the name of the user group, user, or role that has the policy you want to
    remove.
12. Choose the **Permissions** tab and then choose **Add
    permissions**.
13. For IAM groups, select the checkbox next to the name of your new policy,
    choose **Add permissions**, and then choose **Attach
    policy**. For users or roles, choose **Add
    permissions**. On the next page, choose **Attach existing
    policies directly**, select the checkbox next to the name of your
    new policy, choose **Next**, and then choose **Add
    permissions**.

You are returned to the **Summary** page for your user group,
user, or role. 14. Select the checkbox next to the inline policy that you want to remove and
choose **Remove**.
