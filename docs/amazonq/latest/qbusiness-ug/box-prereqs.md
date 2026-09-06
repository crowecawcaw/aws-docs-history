

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites for connecting Amazon Q Business to Box
<a name="box-prereqs"></a>

Before you begin, make sure that you have completed the following prerequisites.

**In Box, make sure you have:**
+ A Box Enterprise or Box Enterprise Plus account.
+ Created a Box custom app in the Box Developer Console and configured it to use **Server Authentication (with JWT)**. 
+ Set your **App Access Level** to **App \+ Enterprise Access** and allowed it to **Make API calls using the as-user header**.
+ Used the admin user to add the following **Application Scopes** in your Box app:
  + Write all files and folders stored in a Box
  + Manage users
  + Manage groups
  + Manage enterprise properties
+ Generated and downloaded Public/Private key pair including a client ID, a client secret, a public key ID, private key ID, a pass phrase, and an enterprise ID to use as authentication credentials. See [Public and private keypair](https://developer.box.com/guides/authentication/jwt/jwt-setup/#public-and-private-key-pair) for more details.
+ Copied your Box enterprise ID either from your Box Developer Console settings or from your Box app. For example, {{801234567}}.

**In your AWS account, make sure you have:**
+ Created a Amazon Q Business application.
+ Created a [Amazon Q Business retriever and added an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html).
+ Created an [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html#iam-roles-ds) for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
+ Stored your Box authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret.
**Note**  
If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [ Data source connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).

**Note**  
For more information on connecting Box to Amazon Q Business, see [Discover insights from Box with the Amazon Q Box connector](https://aws.amazon.com/blogs/machine-learning/discover-insights-from-box-with-the-amazon-q-box-connector/) in the *AWS Machine Learning Blog*.