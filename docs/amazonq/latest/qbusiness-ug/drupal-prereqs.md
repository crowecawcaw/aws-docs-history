# Prerequisites for connecting Amazon Q Business to Drupal

Before you begin, make sure that you have completed the following
prerequisites.

**In Drupal, make sure you have:**

- Created a Drupal (Standard) Suite account and a user with an
  administrator role.
- Install the _Web Services_ modules from Drupal's core
  modules. These include the _HTTP Basic Authentication
  module_, the _JSON:API_ module, the
  _RESTful Web Services_ module, and the
  _Serialization_ module.
- Configure the _JSON:API_ module to accept the JSON:API
  _create_, _read_,
  _update_, and _delete_
  operations.
- Copied your Drupal site name and configured a host URL. For
  example,
  `https://<hostname>/<drupalsitename>`.
- Configured basic authentication credentials containing a username
  (Drupal website login username) and password (Drupal
  website password).
- **Recommended:** Configured an OAuth 2.0
  credential token. Use this token along with your Drupal password
  grant, client id, client secret, username (Drupal website login
  username) and password (Drupal website password) to connect to
  Amazon Q.
- Added the following permissions in your Drupal account using an
  administrator role:
  - administer blocks
  - administer block_content display
  - administer block_content fields
  - administer block_content form display
  - administer views
  - view user email addresses
  - view own unpublished content
  - view page revisions
  - view article revisions
  - view all revisions
  - view the administration theme
  - access content
  - access content overview
  - access comments
  - search content
  - access files overview
  - access contextual links

###### Note

If there are user defined content types or user defined block types, or
any views and blocks are added to the Drupal website, they must
be provided with administrator access.
**In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Drupal authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
