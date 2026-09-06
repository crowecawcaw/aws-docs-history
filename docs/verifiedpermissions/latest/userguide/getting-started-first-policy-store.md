

# Create your first Amazon Verified Permissions policy store
<a name="getting-started-first-policy-store"></a>

For this tutorial, let's assume you're the developer of a photo sharing application and you are looking for a way to control what actions the users of the application can perform. You want to control who can add, delete, or view photos and photo albums. You also want to control what actions a user can take on their account. Can they manage their account, how about the account of a friend? To control these actions you would create policies that permit or forbid these actions based on the identity of the user. Verified Permissions offers [policy stores](terminology.md#term-policy-store), or containers, to house these policies.

In this tutorial we'll walk through creating a sample policy store using the Amazon Verified Permissions console. The console offers a few sample policy store options and we’re going to create a **PhotoFlash** policy store. This policy store allows *principals*, such as users, to perform *actions*, such as sharing, on *resources*, such as photos or albums.

The following diagram illustrates the relationships between a principal, `User::alice`, and the actions she can take on various resources, namely her PhotoFlash account, the `VactionPhoto94.jpg` file, the photo album `alice-favorites-album`, and the user group `alice-friend-group`.

![PhotoFlash entity relationships](http://docs.aws.amazon.com/verifiedpermissions/latest/userguide/images/PhotoFlash.png)


Now that you have an understanding of the **PhotoFlash** policy store, let’s create the policy store and explore it.

## Prerequisites
<a name="getting-started-prerequisites"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Step 1: Create a PhotoFlash policy store
<a name="getting-started-first-sample-policy-store"></a>

In the following procedure you'll create a **PhotoFlash** policy store using the AWS console.

**To create a PhotoFlash policy store**

1. In the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions), choose **Create new policy store**.

1. For **Starting options**, choose **Start from a sample policy store**.

1. For **Sample project**, choose **PhotoFlash**.

1. Choose **Create policy store**.

Once you see the message "Created and configured policy store," choose **Go to overview** to explore your policy store.

## Step 2: Create a policy
<a name="getting-started-creating-policy"></a>

When you created the policy store, a default policy was created that allows users to have full control over their own accounts. This is a useful policy, but for our purposes, let’s create a more restrictive policy to explore the nuances of Verified Permissions. If you remember the diagram we looked at earlier in the tutorial, we had a principal, `User::alice`, who could perform an action, `UpdateAlbum`, on a resource, `alice-favorites-album`. Let's add the policy that will allow Alice, and only Alice, to manage this album.

**To create a policy**

1. In the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions), choose the policy store you created in step 1.

1. In the navigation, choose **Policies**.

1. Choose **Create policy** and then choose **Create static policy**.

1. For **Policy effect**, choose **Permit**.

1. For **Principals scope**, choose **Specific principal**, then for **Specify entity type**, choose **PhotoFlash::User**, and for **Specify entity identifier**, enter **alice**.

1. For **Resources scope**, choose **Specific resource**, then for **Specify entity type**, choose **PhotoFlash::Album**, and for **Specify entity identifier**, enter **alice-favorites-album**.

1. For **Actions scope**, choose **Specific set of actions**, then for **Action(s) this policy should apply to**, select **UpdateAlbum**.

1. Choose **Next**.

1. Under **Details**, for **Policy description - optional** enter **Policy allowing alice to update alice-favorites-album.**.

1. Choose Create policy

Now that you've created a policy you can test it in the Verified Permissions console.

## Step 3: Testing a policy store
<a name="getting-started-testing-first-sample-policy-store"></a>

After creating your policy store and policy, you can test them by running a simulated [authorization request](terminology.md#term-authorization-request) using the Verified Permissions test bench.

**To test policy store policies**

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/). Choose your policy store.

1. In the navigation pane on the left, choose **Test bench**.

1. Choose **Visual mode**.

1. For **Principal**, do the following:

   1. For **Principal taking action** choose **PhotoFlash::User** and for **Specify entity identifier**, enter **alice**.

   1. Under **Attributes**, for **Account: Entity**, make sure that the **PhotoFlash::Account** entity is selected, and for **Specify entity identifier**, enter **alice-account**.

1. Under **Resource**, for **Resource that principal is acting on**, choose the **PhotoFlash::Album** resource type and for **Specify entity identifier**, enter **alice-favorites-album**.

1. For **Action**, choose **PhotoFlash::Action::"UpdateAlbum"** from the list of valid actions.

1. At the top of the page, choose **Run authorization request** to simulate the authorization request for the Cedar policies in the sample policy store. The test bench should display **Decision: Allow** indicating our policy is working as expected.

The following table provides additional values for the principal, resource, and action you can test with the Verified Permissions test bench. The table includes the authorization request decision based on the static policies included with the PhotoFlash sample policy store and the policy you created in step 2.


|  **Principal value**  |  **Principal Account: Entity value**  |  **Resource value**  |  **Resource parent value**  |  **Action**  |  **Authorization decision**  | 
| --- | --- | --- | --- | --- | --- | 
| PhotoFlash::User \| bob | PhotoFlash::Account \| alice-account | PhotoFlash::Album \| alice-favorites-album | N/A | PhotoFlash::Action::"UpdateAlbum" | Deny | 
| PhotoFlash::User \| alice | PhotoFlash::Account \| alice-account | PhotoFlash::Photo \| photo.jpeg | PhotoFlash::Account \| bob-account | PhotoFlash::Action::"ViewPhoto" | Deny | 
| PhotoFlash::User \| alice | PhotoFlash::Account \| alice-account | PhotoFlash::Photo \| photo.jpeg | PhotoFlash::Account \| alice-account | PhotoFlash::Action::"ViewPhoto" | Allow | 
| PhotoFlash::User \| alice | PhotoFlash::Account \| alice-account | PhotoFlash::Photo \| bob-photo.jpeg | PhotoFlash::Album \| Bob-Vacation-Album | PhotoFlash::Action::"DeletePhoto" | Deny | 

## Step 4: Clean up resources
<a name="getting-started-clean-up"></a>

After you have finished exploring your policy store, delete it.

**To delete a policy store**

1. In the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions), choose the policy store you created in step 1.

1. In the navigation, choose **Settings**.

1. Under **Delete policy store**, choose **Delete this policy store**.

1. In the **Delete this policy store?** dialog box, enter *delete*, and then choose **Delete**.