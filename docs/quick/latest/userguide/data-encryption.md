# Data encryption in Amazon Quick

Amazon Quick uses the following data encryption features:

- Encryption at rest
- Encryption in transit
- Key management
  You can find more details about data encryption at rest and data encryption in transit in
  the following topics. For more information about key management in Amazon Quick, see
  [Encrypting your Amazon Quick data with AWS Key Management Service customer managed keys](customer-managed-keys.md "customer-managed-keys.md").

###### Topics

- [Encryption at rest](#data-encryption-at-rest "#data-encryption-at-rest")
- [Encryption in transit](#data-encryption-in-transit "#data-encryption-in-transit")

## Encryption at rest

Amazon Quick securely stores your Amazon Quick metadata. This includes the following:

- Amazon Quick user data, including Amazon Quick user names, email addresses, and passwords. Amazon Quick
  administrators can view user names and emails, but each user's password is completely
  private to each user.
- Minimal data necessary to coordinate user identification with your Microsoft Active
  Directory or identity federation implementation (Federated Single Sign-On (IAM Identity Center)
  through Security Assertion Markup Language 2.0 (SAML 2.0)).
- Data source connection data.
- Amazon Quick encrypts your data source credentials (username and password) and OAuth
  tokens with your default customer managed KMS key when one is registered with Amazon Quick.
  Amazon Quick re-encrypts credentials and tokens with the current default customer managed KMS key
  each time you update the credential or refresh an OAuth token. If you do not register a
  default customer managed KMS key, Amazon Quick encrypts this information with a service-managed
  key.
- Names of your uploaded files, data source names, and data set names.
- Statistics that Amazon Quick uses to populate machine learning (ML) insights.
- Data indexed to support Amazon Q in Quick. This includes the following:

  - Topics
  - Metadata related to your dashboards
  - Your first index capacity purchase
  - Your first chat
  - Your first space creation
  - Your first knowledge base creation

###### Important

Quick protects data indexed to support Amazon Q with the Amazon Q data key.
That key is set the first time Amazon Q data is created in your account and cannot be changed
afterward. To use a customer managed KMS key for Amazon Q data, register it as your account
default key before creating any Amazon Q data. For more information, see
[Amazon Q data key](customer-managed-keys.md#customer-managed-keys-q-data-key "customer-managed-keys.md#customer-managed-keys-q-data-key")
and [Customer managed KMS key scope](customer-managed-keys.md#customer-managed-keys-scope "customer-managed-keys.md#customer-managed-keys-scope").

Amazon Quick securely stores your Amazon Quick data. This includes the following:

- When no customer managed KMS key applies, data at rest in SPICE is
  encrypted using hardware block-level encryption with keys that AWS owns and manages.
  For information about using a customer managed KMS key with SPICE datasets,
  see [Customer managed KMS key scope](customer-managed-keys.md#customer-managed-keys-scope "customer-managed-keys.md#customer-managed-keys-scope").
- When no customer managed KMS key applies, other data at rest is encrypted with a
  service-managed key. This includes the following:

  - Sample values for filters.
  - User feedback on chat responses, including optional free-text comments. User
    feedback is not encrypted with your customer managed KMS key or the Amazon Q data key.
    Report artifacts (including email reports) can be encrypted with your default
    customer managed KMS key when one is registered. For more information, see
    [Customer managed KMS key scope](customer-managed-keys.md#customer-managed-keys-scope "customer-managed-keys.md#customer-managed-keys-scope").

- Amazon Quick encrypts cached query results at rest. Amazon Quick caches query results from a
  SPICE dataset that your customer managed KMS key protects under that same
  key, and encrypts other cached results with a service-managed key.

When you delete a user, Amazon Quick permanently deletes that user's metadata. What happens to
the assets that the user owned, and to data such as the user's conversation history, depends
on how the user is removed. For more information, see
[User lifecycle and data handling in Amazon Quick](user-lifecycle-data-handling.md "user-lifecycle-data-handling.md").

When you unsubscribe from Amazon Quick, all of your Amazon Quick data is completely and permanently
deleted. This includes all metadata, any data you have in SPICE, and Amazon Q
data, including the Quick index. This deletion is immediate; there is no retention period
during which the data can be recovered.

## Encryption in transit

Amazon Quick supports encryption for all data transfers. This includes transfers from the data
source to SPICE, or from SPICE to the user interface. However,
encryption isn't mandatory. For some databases, you can choose whether transfers from the
data source are encrypted or not. Amazon Quick secures all encrypted transfers by using Secure
Sockets Layer (SSL).
