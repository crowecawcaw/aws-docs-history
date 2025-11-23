# How AWS Transfer Family uses AWS Secrets Manager secrets

AWS Transfer Family is a secure transfer service that enables you to transfer files into and out
of AWS storage services.

Transfer Family now supports using Basic authentication for servers that use the Applicability
Statement 2 (AS2) protocol. You can create a new Secrets Manager secret or choose an existing
secret for your credentials. For more information, see [Basic
authentication for AS2 connectors](../../../transfer/latest/userguide/as2-connectors-details.md#as2-basic-auth "../../../transfer/latest/userguide/as2-connectors-details.md#as2-basic-auth") in the _AWS Transfer Family User
Guide_.

To authenticate Transfer Family users, you can use AWS Secrets Manager as an identity provider. For more
information, see [Working with
custom identity providers](../../../transfer/latest/userguide/custom-identity-provider-users.md "../../../transfer/latest/userguide/custom-identity-provider-users.md") in the _AWS Transfer Family User Guide_
and the blog article [Enable password authentication for AWS Transfer Family using AWS Secrets Manager](https://aws.amazon.com/blogs/storage/enable-password-authentication-for-aws-transfer-family-using-aws-secrets-manager-updated/ "https://aws.amazon.com/blogs/storage/enable-password-authentication-for-aws-transfer-family-using-aws-secrets-manager-updated/").

You can use Pretty Good Privacy (PGP) decryption with the files that Transfer Family processes
with workflows. To use decryption in a workflow step, you provide a PGP key that you
manage in Secrets Manager. For more information, see [Generate and
manage PGP keys](../../../transfer/latest/userguide/key-management.md#pgp-key-management "../../../transfer/latest/userguide/key-management.md#pgp-key-management") in the _AWS Transfer Family User Guide_.
