# Managing your identity authorization policies in

Amazon SES

In
addition to creating and attaching policies to identities, you can edit, remove, list, and
retrieve an identity's policies as described in the following sections.

## Managing policies using the Amazon SES

console

Managing Amazon SES polices entails viewing, editing, or deleting a policy attached to an
identity by using the Amazon SES console.

###### To manage policies using the Amazon SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Verified identities**.
3. In the list of identities, choose the identity you want to manage.
4. On the identity's detail page, navigate to the
   **Authorization** tab. Here you’ll find a list of all the
   policies attached to this identity.
5. Select the policy you want to manage by choosing its checkbox.
6. Depending on the desired management task, choose the respective button as
   follows:
   1. To view the policy, choose **View policy**. If you
      need a copy of it, choose the **Copy** button and it
      will be copied to your clipboard.
   2. To edit the policy, choose **Edit**. In the
      **Policy document** pane, edit the policy, and then
      choose **Save changes**.

   ###### Note

   To revoke permissions, you can either edit the policy or remove
   it. 3. To remove the policy, choose **Delete**.

   ###### Important

   Removing a policy is permanent. We recommend that you back up the
   policy by copying and pasting it into a text file before you remove
   it.

## Managing policies using the Amazon SES API

Managing Amazon SES polices entails viewing, editing, or deleting a policy attached to an
identity by using the Amazon SES API.

###### To list and view policies using the Amazon SES API

- You can list the policies that are attached to an identity by using the [ListIdentityPolicies API
  operation](../APIReference/API_ListIdentityPolicies.md "../APIReference/API_ListIdentityPolicies.md"). You can also retrieve the policies themselves by using
  the [GetIdentityPolicies
  API operation](../APIReference/API_GetIdentityPolicies.md "../APIReference/API_GetIdentityPolicies.md").

###### To edit a policy using the Amazon SES API

- You can edit a policy that's attached to an identity by using the [PutIdentityPolicy API
  operation](../APIReference/API_PutIdentityPolicy.md "../APIReference/API_PutIdentityPolicy.md").

###### To delete a policy using the Amazon SES API

- You can delete a policy that's attached to an identity by using the [DeleteIdentityPolicy API
  operation](../APIReference/API_DeleteIdentityPolicy.md "../APIReference/API_DeleteIdentityPolicy.md").
