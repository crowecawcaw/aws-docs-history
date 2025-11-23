# How Amazon AppFlow uses

AWS Secrets Manager

Amazon AppFlow is a fully-managed integration service that enables you to securely
exchange data between software as a service (SaaS) applications, such as Salesforce, and
AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Redshift.

In Amazon AppFlow, when you configure an SaaS application as a source or destination, you
create a connection. This includes information required for connecting to the SaaS
applications, such as authentication tokens, user names, and passwords. Amazon AppFlow
stores your connection data in a Secrets Manager [managed
secret](service-linked-secrets.md "service-linked-secrets.md") with the prefix `appflow`. The cost of storing the secret
is included with the charge for Amazon AppFlow. For more information, see [Data protection
in Amazon AppFlow](../../../appflow/latest/userguide/data-protection.md#encryption-rest "../../../appflow/latest/userguide/data-protection.md#encryption-rest") in the _Amazon AppFlow User Guide_.
