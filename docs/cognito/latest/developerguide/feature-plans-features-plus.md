

# Plus plan features
<a name="feature-plans-features-plus"></a>

The Plus feature plan has advanced security features for Amazon Cognito user pools. These features log and analyze user context at runtime for potential security issues in devices, locations, request data, and passwords. They then mitigate potential risks with automatic responses that block or add security safeguards to user accounts. You can also export your security logs to Amazon S3, Amazon Data Firehose, or Amazon CloudWatch Logs for further analysis.

When you switch from the Essentials to the Plus plan, you get all the features in Essentials and the additional features that follow. These include the threat protection set of security options also known as *advanced security features*. To configure your user pools to automatically adapt to threats in your authentication front end, choose the Plus plan for your user pools.

The sections that follows present a brief overview of the features that you can add to your application with the Plus plan. For detailed information, see the following pages.

**Additional resources**
+ Adaptive authentication: [Working with adaptive authentication](cognito-user-pool-settings-adaptive-authentication.md)
+ Compromised credentials: [Working with compromised-credentials detection](cognito-user-pool-settings-compromised-credentials.md)
+ Log export: [Exporting logs from Amazon Cognito user pools](exporting-quotas-and-usage.md)

**Topics**
+ [Threat protection: adaptive authentication](#features-adaptive-authentication)
+ [Threat protection: compromised-credentials detection](#features-compromised-credentials)
+ [Threat protection: user activity logging](#features-user-logs)

## Threat protection: adaptive authentication
<a name="features-adaptive-authentication"></a>

The Plus plan includes an *adaptive authentication* feature. When you activate this feature, your user pool makes a risk assessment of every user authentication session. From the resulting risk ratings, you can block authentication or push MFA for users who sign in with a risk level above a threshhold that you determine. With adaptive authentication, your user pool and application automatically block or set up MFA for users whose accounts you suspect are being attacked. You can also provide feedback on the risk ratings from your user pool to adjust future ratings.

**To set up adaptive authentication in the Amazon Cognito console**

1. Select the Plus feature plan.

1. From the **Threat protection** menu of your user pool, edit **Standard and custom authentication** under **Threat protection**.

1. Set the **enforcement mode** for standard or custom authentication to **Full-function**.

1. Under **Adaptive authentication**, configure automatic risk responses for different levels of risk.

**Learn more**
+ [Working with adaptive authentication](cognito-user-pool-settings-adaptive-authentication.md)
+ [Collecting data for threat protection in applications](user-pool-settings-viewing-threat-protection-app.md)

## Threat protection: compromised-credentials detection
<a name="features-compromised-credentials"></a>

The Plus plan includes a *compromised-credentials detection* feature. This feature guards against the use of insecure passwords and the threat of unintended application access that this practice creates. When you permit your users to sign in with username and password, they might reuse a password that they've used elsewhere. That password might have been leaked, or just be commonly guessed. With compromised-credentials detection, your user pool reads the passwords your users submit and compares them to password databases. If the operation results in a decision that the password is likely compromised, you can configure your user pool to block sign-in and then initiate a password reset for the user in your application.

Compromised-credentials detection can react to insecure passwords when new users sign up, when existing users sign in, and when users attempt to reset their passwords. With this feature, your user pool can prevent or warn about sign-in with insecure passwords wherever users enter them.

**To set up compromised-credentials detection in the Amazon Cognito console**

1. Select the Plus feature plan.

1. From the **Threat protection** menu of your user pool, edit **Standard and custom authentication** under **Threat protection**.

1. Set the **enforcement mode** for standard or custom authentication to **Full-function**.

1. Under **Compromised credentials**, configure the types of authentication operations that you want to check, and the automated response that you want from your user pool.

**Learn more**
+ [Working with compromised-credentials detection](cognito-user-pool-settings-compromised-credentials.md)

## Threat protection: user activity logging
<a name="features-user-logs"></a>

The Plus plan adds a logging feature that gives security analysis and details of user authentication attempts. You can see risk assessments, user IP addresses, user agents, and other information about the device that connected to your application. You can act on this information with the built-in threat protection features, or you can analyze your logs in your own systems and take appropriate action. You can export the logs from threat protection to Amazon S3, CloudWatch Logs, or Amazon DynamoDB.

**To set up user activity logging in the Amazon Cognito console**

1. Select the Plus feature plan.

1. From the **Threat protection** menu of your user pool, edit **Standard and custom authentication** under **Threat protection**.

1. Set the **enforcement mode** for standard or custom authentication to **Audit-only**. This is the minimum setting for logs. You can also activate it in **Full-function** mode and configure other threat protection features.

1. To export your logs to another AWS service for third-party analysis, go to the **Log streaming** menu of your user pool and set up an export destination.

**Learn more**
+ [Exporting user authentication events](cognito-user-pool-settings-adaptive-authentication.md#user-pool-settings-adaptive-authentication-event-user-history-exporting)
+ [Exporting logs from Amazon Cognito user pools](exporting-quotas-and-usage.md)