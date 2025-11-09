# Plugin for Unreal: Set up an AWS user

profile

After installing the plugin, set up a user profile with a valid AWS account. You can
maintain multiple profiles in the plugin, but you can have only one profile selected at
a time. Whenever you work in the plugin, select a profile to use. Each workflow page
displays the currently selected profile.

Maintaining multiple profiles gives you the ability to switch between different
hosting deployments. For example, you might set up profiles that use the same AWS
account but deploy to different AWS Regions. Or you might set up profiles with
different AWS accounts or users and permission sets.

###### Note

If you've installed the AWS CLI on your workstation and have a profile already configured,
the Amazon GameLift Servers plugin will detect it and list it as an existing profile. The plugin
automatically selects any profile named `[default]`. You can use
an existing profile or create a new one.

All profiles must be bootstrapped to set up some required AWS resources under
your account user.

###### To manage your AWS profiles

1. In the Unreal editor main toolbar, choose the Amazon GameLift Servers menu, and select **AWS Access Credentials**. This action opens the Amazon GameLift Servers plugin to
   the page **Set up your user profile**.
2. Use the buttons to create a new AWS account or set up a user profile for an AWS account
   that you already have.
3. If you don't already have a user profile, you're prompted to enter profile details
   and create a new profile. Provide the following information:
   - An AWS account. If you create a new AWS account, use the link to the
     AWS Management Console and follow the prompts. See [Create an
     AWS account](../../../accounts/latest/reference/manage-acct-creating.md "../../../accounts/latest/reference/manage-acct-creating.md") for more details.
   - An AWS user with permissions to use Amazon GameLift Servers
     and other required AWS services. See
     [Set up an AWS user account](setting-up-aws-login.md "setting-up-aws-login.md")
     for instructions on setting up an AWS Identity and Access Management (IAM) user with Amazon GameLift Servers permissions
     and programmatic access with long-term credentials.
   - Credentials for your AWS user. These credentials
     consist of an AWS access key ID and AWS secret key.
     See [Get your access keys](../../../cli/latest/userguide/cli-authentication-user.md#cli-authentication-user-get "../../../cli/latest/userguide/cli-authentication-user.md#cli-authentication-user-get") for more details.
   - AWS region. This is a geographic location where you want to create your
     AWS resources for hosting. During development, we recommend using a
     region close to your physical location. Choose a region from the list of
     [supported AWS regions](../../../general/latest/gr/gamelift.md "../../../general/latest/gr/gamelift.md").

4. If the plugin detects existing profiles, it displays a list of available profiles.
   Select an existing profile from the list, or choose **Add another profile** to create a new one.

## Bootstrap a user profile

All profiles must be bootstrapped to use with the Amazon GameLift Servers plugin.
Bootstrapping creates an Amazon S3 bucket specific to the profile. It's used
to store project configurations, build artifacts, and other dependencies.
Buckets are not shared between other profiles.

Bootstrapping involves creating new AWS resources and might incur costs.

###### To bootstrap your profile:

1. On the **AWS Access Credentials** page, check the bootstrap
   status of the user profile that you want to use. If the profile's bootstrap
   status is "Inactive" and there's no S3 bucket listed, you need to bootstrap
   the profile.
2. Select the profile you want to use and choose **Bootstrap profile**.
3. Wait for bootstrap status to change to "Active". This can take a few minutes.
