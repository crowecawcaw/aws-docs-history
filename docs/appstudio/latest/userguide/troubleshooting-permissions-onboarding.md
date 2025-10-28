# Troubleshooting App Studio setup, permissions, and onboarding

This topic includes information about troubleshooting common issues when setting up or onboarding to App Studio, and managing permissions.

## App Studio setup failed when choosing the **Create an account instance for me** option

**Problem:** Setting up App Studio with the **Create an account instance for me** will fail if you
have an account-level IAM Identity Center instance in any AWS Region, as IAM Identity Center only supports one instance.

**Solution:** Navigate to the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/") to check if you
have an IAM Identity Center instance. Check every supported AWS Region until you locate the instance. You can either use that instance when
setting up App Studio, or delete the IAM Identity Center instance and try again with the **Create an account instance for me** option.

###### Warning

Deleting the IAM Identity Center instance will affect any existing use cases. Ensure the instance isn't being used before deleting, or use the instance to set
up App Studio.

## Unable to access App Studio after setting up

**Problem:** When setting up App Studio, you may have provided IAM Identity Center groups that you are not a member of. You
must be a member of at least one group to access App Studio.

**Solution:** Navigate to the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/") to add yourself to a group that was
added to App Studio when setting up.

## Not sure what username or password to use when logging into App Studio

**Problem:** You may not be sure how to log into App Studio, either because you haven't set up your IAM Identity Center
credentials, or you have forgotten your IAM Identity Center username or password.

**Solution:** When setting up App Studio without an IAM Identity Center instance,
an email and username was provided for each user that would be used to create IAM Identity Center users. Each of the email addresses
provided were sent an email with an invitation to join IAM Identity Center. Each user must accept the invitation and create a password
for their IAM Identity Center user credentials. Each user can then use the IAM Identity Center username and password to log into App Studio.

If you have already set up credentials and have forgotten your username or password, you must ask your administrator to
use the IAM Identity Center console to view and provide your username, or reset your password.

## I am getting a System error when setting up App Studio

**Problem:** You are getting the following error when setting up App Studio:

```
System error. We encountered a problem. Report the issue and the App Studio service team will get back to you.
```

This error occurs when the service has encountered an unknown error.

**Solution:** Contact the support team by joining the community Slack by choosing **Join us on Slack** in the
**Learn** section of the left-hand navigation, or in the top banner while editing an app.

## I can't locate my App Studio instance URL

If you can't find the URL to access your App Studio instance, reach out to the administrator that set up App Studio. The administrator
can view the URL in App Studio console in the the AWS Management Console.

## I can't modify groups or roles in App Studio

**Problem:** You cannot see the **Roles** link in the left-hand navigation. This is because
only users with the Admin role can modify groups and roles in App Studio.

**Solution:** Reach out to a user with the Admin role to change groups or roles, or reach out to your
administrator to be added to an Admin group.

## How do I offboard from App Studio

You cannot offboard from App Studio at this moment. It is recommended to
remove all resources such as apps and connectors, and change the role of groups to App User to prevent access or use. You should also delete third-party resources that
are used exclusively for App Studio, such as IAM roles or database tables.
