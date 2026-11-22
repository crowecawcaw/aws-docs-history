

# Sign up for AWS (new)

**Note**  
Our new AWS experience lets you build using AWS accounts created with preconfigured defaults. If you have regulated workloads, want complete control over where your content is stored, or require advanced features right away, such as networking and security services, [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). [Compare sign-up options](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws.html#compare-sign-up-options).

When you use Sign up for AWS (new), you create a preconfigured AWS environment that lets you use a login that you already own like Google or GitHub to access your AWS resources. Your resources are organized in projects. A project contains an AWS account and settings for sharing with other collaborators. If you use the paid plan, your project can also have a set monthly pre-tax cost, called a spend limit. All of the projects you own make up your organization. You manage your organization, access your projects, and add team members in AWS Settings.

![Structure of your organization and projects.](https://docs.aws.amazon.com/accounts/latest/reference/images/sign-up-aws-new-org.png)


When you sign up for AWS using Sign up for AWS (new), AWS also creates a AWS Builder ID account, which is a personal profile that represents you as an individual. You can only have one AWS Builder ID for each email address. If you've created a AWS Builder ID but have not created an AWS account, you might have some settings already made for you and you'll have to modify those later.

For more information about Sign up for AWS (new), see the following documentation:
+ [Compare sign-up options](sign-up-for-aws.md)
+ [Supported AWS services for Sign up for AWS (new)](supported-services-sign-up-new.md)

## Sign up using Sign up for AWS (new)
<a name="sign-up-social-login-procedure"></a>

When you sign up for AWS, we might request payment information. Our verification process holds USD $1 (or equivalent) for 3-5 days to verify your account and prevent fraud. You will not incur charges until you upgrade to a paid plan. You can manage your payment method or close your accounts at any time through AWS Settings. In addition, when you sign up for AWS, you might be ineligible for the Free Tier. In that case, you'll need to provide your payment information, and you'll be placed on the Paid Plan. When you're on the Paid Plan, you can set spend limits to operate within a predictable and controlled budget.

Sign up for AWS (new) supports using Google, GitHub, Apple, or Amazon for your account. If you're already signed into a Google account in your browser, that account will be used when you sign up for AWS.

To start sign-up from the AWS Command Line Interface (AWS CLI) instead, see [Sign up using the AWS CLI](#sign-up-cli).

**To sign up for AWS using Sign up for AWS (new)**

1. Open the [Sign up for AWS](https://signin.aws.amazon.com/signup?request_type=builderId) page.

1. Enter your email or choose a login such as Google, Apple, GitHub, or Amazon.

1. If you use a login you already own, you'll be directed to the login for your provider. After you log in, you'll be redirected to AWS sign up.

1. Enter your name and choose **Continue**.

   This name is shared with team members when you give them access to your projects.

1. Verify the email associated with your login by entering a verification code. When you've verified your email, choose **Continue**.

   This email is shared with team members when you give them access to your projects.

1. Enter a strong password for your account and choose **Continue**.

   AWS requires that your password meet the following conditions:
   + It must have a minimum of 8 characters and a maximum of 128 characters.
   + It must include a minimum of three of the following mix of character types: uppercase, lowercase, numbers, and \! @ \# $ % ^ & \* () <> [] {} \| \_\+-= symbols.
   + It must not be identical to your AWS account name or email address.

1. Enter your contact details and choose **Continue**.

1. AWS will provision your first project in one of three AWS Regions with a new name. For more information, see [AWS Regions for your projects](project-regions.md). You can change the name at any time.

You can now access the AWS Management Console. To access AWS Settings, choose **Manage projects** from the AWS Management Console. In AWS Settings, you can invite team members, create new projects, and modify your billing and other settings.

## Sign up using the AWS CLI
<a name="sign-up-cli"></a>

You can also start Sign up for AWS (new) from the AWS Command Line Interface (AWS CLI), for example, in a terminal or from an AI coding tool. You complete sign-up in your browser. When you finish, the AWS CLI receives credentials for your new project, so you don't need to sign in again or create access keys.

These are the same kind of temporary credentials that the `aws login` command provides. The AWS CLI saves them to your AWS CLI profile and refreshes them automatically. For more information, see [Login for AWS local development using console credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) in the *AWS Command Line Interface User Guide*.

Before you begin, install or update the AWS CLI. The `aws signup` command requires AWS CLI version 2.41.0 or later. With an earlier version, starting with 2.32.0, you can use the `aws login` command instead. For installation steps, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

**To sign up for AWS using the AWS CLI**

1. In your terminal, run the following command.

   ```bash
   aws signup
   ```

   To save the credentials to a named profile instead of your default profile, add `--profile {{profile-name}}` to this command and to the commands that follow.

   If your version of the AWS CLI doesn't include `aws signup`, run `aws login` instead.

1. The AWS CLI opens the sign-up page in your default browser. If the browser doesn't open, open the URL that the AWS CLI displays. Keep the command running while you sign up. Sign-up can take several minutes.

   If you ran `aws login`, choose **Continue to sign in** on the page that opens, and then choose **Sign up** in the upper-right corner of the sign-in page.

   If you're already signed in with an AWS Builder ID in this browser, the **AWS sign-ins** page opens instead and lists your existing projects. To sign up with a different AWS Builder ID, choose **Sign out of AWS**, and then run the command again. To add a project to your current AWS Builder ID instead, see [Create a project in AWS Settings](create-project.md).

1. Sign up in your browser. The steps are the same as in [Sign up using Sign up for AWS (new)](#sign-up-social-login-procedure). If you already have an AWS Builder ID, sign in with it. If AWS asks whether you want to create a new AWS account or sign in to an existing one, choose to create a new account.

1. When sign-up is complete, the **AWS sign-ins** page opens. Choose your new project. This grants the AWS CLI access to your project. You can have up to five active sessions in one browser. If you already have five, sign out of one of them to make room for your new project.

1. Return to your terminal and wait for the command to finish. To confirm that the credentials work, run the following command. The output shows the AWS account ID of your new project.

   ```bash
   aws sts get-caller-identity
   ```

AWS hosts your project's Regional resources in one AWS Region. AWS assigns this Region based on the country in your contact address. When you sign up with `aws signup`, the AWS CLI sets the Region in your profile to your project's Region. It also displays the Region that it set. If your profile already uses a different Region, the AWS CLI asks before it changes the Region. If the AWS CLI can't determine your project's Region, it displays the command to set it. If you sign up after you run `aws login`, your profile keeps the Region that you chose for `aws login`.

Before you create Regional resources from the AWS CLI, confirm that your profile uses your project's Region. To see the Region in your profile, run `aws configure list`. To find your project's Region, see [Find the selected AWS Region for your projects](project-regions.md#project-regions-find). If the Regions are different, run the following command. Replace {{project-region}} with your project's Region code, such as `us-east-2`. If you use a named profile, add `--profile {{profile-name}}`.

```bash
aws configure set region {{project-region}}
```

In some cases, you finish signing up, but the AWS CLI doesn't receive credentials, and your browser opens the AWS Management Console with your new account instead. For example, this can happen in the following cases:
+ Sign-up takes longer than the AWS CLI waits.
+ You choose to sign in to an existing account instead of creating a new one.
+ You leave sign-up and finish it later in AWS Settings.

Your account works. To get credentials for it, run `aws login`, and then choose your new project on the **AWS sign-ins** page. Then confirm that your profile uses your project's Region. For other errors, see [Troubleshoot logging in using console credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in-troubleshoot.html) in the *AWS Command Line Interface User Guide*.

If you already signed up for our new AWS experience, you don't need to sign up again. Run `aws login` to get credentials for your existing projects. To add a project, see [Create a project in AWS Settings](create-project.md).

Your AI coding tool can run these commands for you. You still complete sign-up and choose your project in your browser. You are responsible for any actions that your AI coding tool takes on your behalf in your projects. For more information, see [Connect an AI coding tool](connect-ai-coding-tool.md). To install the Agent Toolkit for AWS and have your AI coding tool start sign-up for you, see [Getting started](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/quick-start.html) in the *Agent Toolkit for AWS User Guide*.

## Next steps
<a name="sign-up-social-login-next-steps"></a>

After you sign up for AWS, you can connect an AI coding tool, add team members to collaborate, and if you have a paid plan, create a spend limit.
+ [Connect an AI coding tool](connect-ai-coding-tool.md)
+ [Invite team members to collaborate in AWS Settings](invite-team-members.md)
+ [Create a spend limit in AWS Settings](create-spend-limit.md)