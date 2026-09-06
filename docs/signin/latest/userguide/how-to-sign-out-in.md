

# Sign out of your AWS account
<a name="how-to-sign-out-in"></a>

How you sign out of your AWS account depends on what type of AWS user you are. You can be an account root user, an IAM user, a user in IAM Identity Center, a federated identity, or an AWS Builder ID user. If you're not sure what kind of user you are, see [Determine your user type](user-types-list.md).

**Topics**
+ [Sign out of a project](#sign-out-project)
+ [Sign out of AWS Settings](#sign-out-aws-settings)
+ [Sign out of the AWS Management Console](#console-signing-out-root-IAM-users)
+ [Sign out of your AWS access portal](#aws-access-portal-signing-out-iam-identity-center-user)
+ [Sign out of AWS Builder ID](#sign-out-all-aws_builder_id)

## Sign out of a project
<a name="sign-out-project"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can sign out of projects if you signed up for AWS using our new AWS experience. If you created an AWS account using [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html), you don't have a project.

**To sign out of a project**

1. After you're signed in to the AWS Management Console, your project name is shown in the upper right corner.

1. In the navigation bar on the upper right, choose your project name.

1. Choose **Sign out**.

1. You are returned to the AWS Management Console webpage.

## Sign out of AWS Settings
<a name="sign-out-aws-settings"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can sign out of AWS Settings if you signed up for AWS using our new AWS experience. If you created an AWS account using [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html), you don't have access to AWS Settings.

**To sign out of AWS Settings**

1. In the left navigation pane, choose **Sign Out**.

1. You are returned to the AWS sign in page.

## Sign out of the AWS Management Console
<a name="console-signing-out-root-IAM-users"></a>

**To sign out of the AWS Management Console**

1. After you're signed in to the AWS Management Console, you arrive at a page similar to the one shown in the following image. Your account name or IAM user name is shown in the upper right corner.  
![User signed in to the AWS Management Console.](http://docs.aws.amazon.com/signin/latest/userguide/images/console-signing-out-step-1.png)

1. In the navigation bar on the upper right, choose your user name.  
![Signed in user's account name is highlighted in the AWS Management Console.](http://docs.aws.amazon.com/signin/latest/userguide/images/console-signing-out-step-2.png)

1. Choose a **Sign out** option. The button options differ based on how many accounts you are signed in to.
   + Select **Sign out** if you are signed in to only one account.
   + Select **Sign out of all sessions** to sign out of all your identities simultaneously.
   + Select **Sign out of current session** to sign out of the identity you have selected.

1. You are returned to the AWS Management Console webpage.

For more information about signing in to multiple accounts, see [Signing in to multiple accounts](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/multisession.html) in the *AWS Management Console Getting Started Guide*.

## Sign out of your AWS access portal
<a name="aws-access-portal-signing-out-iam-identity-center-user"></a>

**To sign out of your AWS access portal**

1. In the navigation bar on the upper right, choose your user name.

1. Select **Sign out** as shown in the following image.  
![User signed in to your AWS access portal.](http://docs.aws.amazon.com/signin/latest/userguide/images/sign-out-access-portal-screenshot.png)

1. If you successfully sign out, you now see your AWS access portal sign in page.

If you use an external identity provider (IdP) as your identity source, the active session for your credentials is not terminated when you sign out. If you navigate back to the AWS access portal, you may be automatically signed in without having to provide your credentials.

## Sign out of AWS Builder ID
<a name="sign-out-all-aws_builder_id"></a>

To sign out of an AWS service that you've accessed using your AWS Builder ID, you must sign out of the service. If you want to sign out of your AWS Builder ID profile, see the following procedure.

**To sign out of your AWS Builder ID profile**

1. After you have signed in to your AWS Builder ID profile at [https://profile.aws.amazon.com/](https://profile.aws.amazon.com/), you arrive at **My details**.

1. In the top right of your AWS Builder ID profile page, choose **Sign out**.  
![AWS Builder ID profile page that highlights Sign out in top right corner.](http://docs.aws.amazon.com/signin/latest/userguide/images/sign-out.png)

1. You're signed out when you no longer see your AWS Builder ID profile.