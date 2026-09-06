

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites for connecting Amazon Q Business to Drupal
<a name="drupal-prereqs"></a>

Before you begin, make sure that you have completed the following prerequisites.

**In Drupal, make sure you have:**
+ Created a Drupal (Standard) Suite account and a user with an administrator role.
+ Install the *Web Services* modules from Drupal's core modules. These include the *HTTP Basic Authentication module*, the *JSON:API* module, the *RESTful Web Services* module, and the *Serialization* module.
+ Configure the *JSON:API* module to accept the JSON:API *create*, *read*, *update*, and *delete* operations.
+ Copied your Drupal site name and configured a host URL. For example, {{https://<hostname>/<drupalsitename>}}.
+ Configured basic authentication credentials containing a username (Drupal website login username) and password (Drupal website password).
+ **Recommended:** Configured an OAuth 2.0 credential token. Use this token along with your Drupal password grant, client id, client secret, username (Drupal website login username) and password (Drupal website password) to connect to Amazon Q.
+ Added the following permissions in your Drupal account using an administrator role:
  + administer blocks
  + administer block\_content display
  + administer block\_content fields
  + administer block\_content form display
  + administer views
  + view user email addresses
  + view own unpublished content
  + view page revisions
  + view article revisions
  + view all revisions
  + view the administration theme
  + access content
  + access content overview
  + access comments
  + search content
  + access files overview
  + access contextual links
**Note**  
If there are user defined content types or user defined block types, or any views and blocks are added to the Drupal website, they must be provided with administrator access.

**In your AWS account, make sure you have:**
+ Created a Amazon Q Business application.
+ Created a [Amazon Q Business retriever and added an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html).
+ Created an [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html#iam-roles-ds) for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
+ Stored your Drupal authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret.
**Note**  
If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [ Data source connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).