# Data protection

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model "https://aws.amazon.com/compliance/shared-responsibility-model") applies to data protection in the Console Mobile Application.
As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud.
You are responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security
configuration and management tasks for the AWS services that you use.
For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq").

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with
AWS Identity and Access Management (IAM). That way each user is given only the permissions necessary to fulfill their job duties.
We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. The Console Mobile Application does this for you, ensuring a secure connection between the application and your AWS resources.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within AWS services.
  We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into free-form text fields such as a Name field. This includes when you work with Console Mobile Application or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into free form text fields for resource identifiers or similar items related to the management of AWS resources might get picked up for inclusion in diagnostic logs. When you provide a URL to an external server, don’t include credentials information in the URL to validate your request to that server.

## Data privacy

### Diagnostics

By default, the AWS Console Mobile App stores and processes user data such as your device identification number and diagnostic information about the app’s performance. Collected diagnostic information specifically includes: crash logs and performance data. This data helps AWS continuously improve the Console Mobile Application and your experience. Your diagnostic data isn’t shared with any third parties, is anonymized, and is protected using sophisticated controls to prevent unauthorized access and misuse.

If you would like to turn off sharing this diagnostic information, you can do so by turning off sharing of this information in your device’s settings. For more information see [Share analytics, diagnostics, and usage information with Apple](https://support.apple.com/en-us/HT202100 "https://support.apple.com/en-us/HT202100")
for iOS and [Learn more about Google Play services for system diagnostics](https://support.google.com/android/answer/12464559 "https://support.google.com/android/answer/12464559")
for Android.
