

# Managing your identity authorization policies in Amazon SES
<a name="managing-policies"></a>

In addition to creating and attaching policies to identities, you can edit, remove, list, and retrieve an identity's policies as described in the following sections.

## Managing policies using the Amazon SES console
<a name="managing-policies-console"></a>

Managing Amazon SES polices entails viewing, editing, or deleting a policy attached to an identity by using the Amazon SES console.

**To manage policies using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Verified identities**. 

1. In the list of identities, choose the identity you want to manage.

1. On the identity's detail page, navigate to the **Authorization** tab. Here you’ll find a list of all the policies attached to this identity.

1. Select the policy you want to manage by choosing its checkbox.

1. Depending on the desired management task, choose the respective button as follows:

   1. To view the policy, choose **View policy**. If you need a copy of it, choose the **Copy** button and it will be copied to your clipboard.

   1. To edit the policy, choose **Edit**. In the **Policy document** pane, edit the policy, and then choose **Save changes**.
**Note**  
To revoke permissions, you can either edit the policy or remove it.

   1. To remove the policy, choose **Delete**.
**Important**  
Removing a policy is permanent. We recommend that you back up the policy by copying and pasting it into a text file before you remove it.

## Managing policies using the Amazon SES API
<a name="managing-policies-api"></a>

Managing Amazon SES polices entails viewing, editing, or deleting a policy attached to an identity by using the Amazon SES API. 

**To list and view policies using the Amazon SES API**
+ You can list the policies that are attached to an identity by using the [ListIdentityPolicies API operation](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentityPolicies.html). You can also retrieve the policies themselves by using the [GetIdentityPolicies API operation](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityPolicies.html).

**To edit a policy using the Amazon SES API**
+ You can edit a policy that's attached to an identity by using the [PutIdentityPolicy API operation](https://docs.aws.amazon.com/ses/latest/APIReference/API_PutIdentityPolicy.html).

**To delete a policy using the Amazon SES API**
+ You can delete a policy that's attached to an identity by using the [DeleteIdentityPolicy API operation](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentityPolicy.html).