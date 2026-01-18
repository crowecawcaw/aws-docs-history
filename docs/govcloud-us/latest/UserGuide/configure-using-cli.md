# Configure Your Account using AWS CLI

The AWS Management Console for the AWS GovCloud (US) Region provides an easy-to-use graphical interface to manage your AWS resources, similar to the AWS Management Console for the standard Regions. In the AWS GovCloud (US) region, you must create an IAM user and use this user name and password to sign in to the console. You cannot use the AWS GovCloud (US) access keys to log into the console. You also cannot use your sign-in credentials for the standard AWS Management Console to access the AWS GovCloud (US) console. The AWS Management Console for the AWS GovCloud (US) Region is a completely separate console from the standard AWS Management Console.

Follow the directions below to create an administrator user name and password that will allow you to login to the console. You can create additional IAM accounts for all of your users once you sign in.

###### Note

If you are not an AWS GovCloud (US) Customer, please visit [AWS GovCloud (US) Region Overview](https://aws.amazon.com/govcloud-us/ "https://aws.amazon.com/govcloud-us/") to find out about the AWS GovCloud (US) Region and then fill out the contact us form (https://aws.amazon.com/govcloud-us/contact/) to request an AWS GovCloud (US) Account.

## Configure the AWS CLI

To get started, you will need install the AWS CLI on your local machine. To learn how to install the AWS CLI, [visit the AWS CLI documentation.](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md") Next, you will need to configure your local CLI to use your new AWS GovCloud (US) (US) account. To do so, run the following command. This command will prompt for the Access Keys and Secret Keys that are provided in the onboarding email.

###### Note

You can replace `--profile "govcloud"` with a name that is convenient for you.

```
# 1. Configure the cli
aws configure --profile "govcloud"

# 2. Check if the credentials are functioning
aws iam list-users --profile "govcloud"
```

Now that we have the CLI configured with our new AWS GovCloud (US) account, we can configure IAM users for accessing the environment.

## Create an IAM User to Access the Console

To get started, we will create an IAM Group to manage administrator access to the AWS GovCloud (US) account. Then, we will create an IAM user, add them to the group, and configure a password for accessing the environment. Using the profile we configured above, run the following commands on the CLI.

```
# 1. Create an “Administrators” IAM Group so that we can centrally manage Administrator IAM permissions for many users.
aws iam create-group \
    --group-name "Administrators" \
    --profile "govcloud"

# 2. Attach the AdministratorAccess policy to the group
aws iam attach-group-policy \
    --group-name "Administrators" \
    --policy-arn "arn:aws-us-gov:iam::aws:policy/AdministratorAccess" \
    --profile "govcloud"

# 3. Create a new IAM User
aws iam create-user \
    --user-name "username" \
    --profile "govcloud"

# 4. Enable the IAM User to sign in to the AWS Console
aws iam create-login-profile \
    --user-name "username" \
    --password "password" \
    --no-password-reset-required \
    --profile "govcloud"

# 5. Add the User to the Administrators IAM Group
aws iam add-user-to-group \
    --group-name "Administrators" \
    --user-name "username" \
    --profile "govcloud"

# 6. Create Access Keys for accessing AWS via the CLI and SDK
aws iam create-access-key \
    --user-name "username" \
    --profile "govcloud"
```

###### Logging in to the Console

1. Open the [AWS GovCloud (US) console.](https://console.amazonaws-us-gov.com/ "https://console.amazonaws-us-gov.com/")
2. Sign in using your account number and the user name and password you created above.
3. Once you are signed in, navigate to the [IAM console.](https://console.amazonaws-us-gov.com/iam) "https://console.amazonaws-us-gov.com/iam)").
4. You should now see 2 users listed. Administrator and the user name you created above. The Administrator credentials were the ones provided during sign up.
5. Confirm your new user has been added to the Administrators group and has the AdministratorAccess policy associated with the Administrators group.
6. You can now safely delete the administrator IAM user or deactivate the Access Credentials.

###### Customizing the Sign In URL

Creating an account alias is optional, but strongly recommended. If you do not create an account alias, be sure to save your AWS GovCloud (US) sign-in link because your AWS GovCloud (US) account number is different from your AWS account number.

1. Sign in to the AWS
   AWS GovCloud (US) console and open the [IAM console.](https://console.amazonaws-us-gov.com/iam) "https://console.amazonaws-us-gov.com/iam)")
2. Next to the IAM users sign-in link, choose Customize.
3. Type an alias for your account.
4. IAM users can now use either the account alias or account number when signing in to the AWS
   AWS GovCloud (US) console.

## Audit Logging

As part of the automated AWS GovCloud (US) activation process, the CloudTrail service should be enabled for each account and an Amazon S3 bucket should be created to store CloudTrail logs. In the event of any interruptions in the automation process, you can manually enable CloudTrail.
