# Data encryption in Amazon WorkSpaces Secure Browser

Amazon WorkSpaces Secure Browser collects portal customization data, such as browser settings, user settings,
network settings, identity provider information, trust store data, and trust store certificate
data. WorkSpaces Secure Browser also collects browser policy data, user preferences (for browser settings), and
session logs. Collected data is stored in Amazon DynamoDB and Amazon S3. WorkSpaces Secure Browser uses AWS Key Management Service for
encryption.

To secure your content, follow these guidelines:

- Implement least privilege access and create specific roles to be used for WorkSpaces Secure Browser
  actions. Use IAM templates to create a Full Access role or Read Only role. For more
  information, see [AWS managed policies for WorkSpaces Secure Browser](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
- Protect data end to end by providing a customer managed key, so WorkSpaces Secure Browser can encrypt your
  data at rest with the keys you supply.
- Be careful with sharing portal domains and user credentials:
  - Admins are required to log into the Amazon WorkSpaces console, and users are required to
    log into the WorkSpaces Secure Browser portal.
  - Anyone on the internet can access the web portal, but they can't start a session
    unless they have valid user credentials to the portal.

- Users can explicitly end their sessions by choosing **End Session**.
  This discards the instance hosting the browser session, and results in browser
  isolation.
  WorkSpaces Secure Browser secures content and metadata by default by encrypting all sensitive data with AWS KMS.
  It collects browser policy and user preferences to enforce policy and settings during WorkSpaces Secure Browser
  sessions. If there is an error applying existing settings, a user can't access new sessions
  and can't access the company's internal sites and SaaS applications.
