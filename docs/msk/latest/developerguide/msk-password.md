# Sign-in credentials authentication with AWS Secrets Manager

You can control access to your Amazon MSK clusters using sign-in credentials that are
stored and secured using AWS Secrets Manager. Storing user credentials in Secrets Manager reduces
the overhead of cluster authentication such as auditing, updating, and rotating credentials.
Secrets Manager also lets you share user credentials across clusters.

After you associate a secret with an MSK cluster, MSK syncs the credential data periodically.

###### This topic contains the following sections:

- [How sign-in credentials authentication works](msk-password-howitworks.md "msk-password-howitworks.md")
- [Set up SASL/SCRAM authentication for an Amazon MSK
  cluster](msk-password-tutorial.md "msk-password-tutorial.md")
- [Working with users](msk-password-users.md "msk-password-users.md")
- [Limitations when using SCRAM secrets](msk-password-limitations.md "msk-password-limitations.md")
