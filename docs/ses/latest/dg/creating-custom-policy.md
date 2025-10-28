# Creating a custom policy

If you want to create a custom policy and attach it to an identity, you have the
following options:

- Using the Amazon SES API – Create a policy in
  a text editor and then attach the policy to the identity by using the
  `PutIdentityPolicy` API described in the [Amazon Simple Email Service API Reference](../APIReference.md "../APIReference.md").
- Using the Amazon SES console – Create a policy
  in a text editor and attach it to an identity by pasting it into the custom
  policy editor in the Amazon SES console. The following procedure describes this
  method.

###### To create a custom policy by using the custom policy editor

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, under **Configuration**, choose
   **Identities**.
3. In the **Identities** container on the **Identities** screen, select the verified identity you wish to
   create an authorization policy for.
4. In the details screen of the verified identity you selected in the previous
   step, choose the **Authorization** tab.
5. In the **Authorization policies** pane, choose
   **Create policy** and select **Create custom
   policy** from the dropdown.
6. In the **Policy document** pane, type or paste the text of
   your policy in JSON format. You can also use the policy generator to quickly
   create the basic structure of a policy and then customize it here.
7. Choose **Apply Policy**. (If you ever need to modify your
   custom policy, just select its check box under the
   **Authorization** tab, choose **Edit**,
   and make your changes in the **Policy document** pane followed
   by **Save changes**).
