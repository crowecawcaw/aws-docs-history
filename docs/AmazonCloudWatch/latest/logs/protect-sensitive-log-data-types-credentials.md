# Credentials

CloudWatch Logs data protection can find the following types of credentials.

| Type of data          | Data identifier ID  | Keyword required                                                                                  | Countries and regions |
| --------------------- | ------------------- | ------------------------------------------------------------------------------------------------- | --------------------- |
| AWS secret access key | `AwsSecretKey`      | `aws_secret_access_key`, `credentials`,<br>`secret access key`, `secret key`, `set-awscredential` | All                   |
| OpenSSH private key   | `OpenSSHPrivateKey` | None                                                                                              | All                   |
| PGP private key       | `PgpPrivateKey`     | None                                                                                              | All                   |
| Pkcs Private Key      | `PkcsPrivateKey`    | None                                                                                              | All                   |
| PuTTY private key     | `PuttyPrivateKey`   | None                                                                                              | All                   |

## Data identifier ARNs for credential data types

The following lists the Amazon Resource Names (ARNs) for the data identifiers that you can
add to your data protection policies.

| Credential data identifier ARNs                                 |
| --------------------------------------------------------------- |
| `arn:aws:dataprotection::aws:data-identifier/AwsSecretKey`      |
| `arn:aws:dataprotection::aws:data-identifier/OpenSshPrivateKey` |
| `arn:aws:dataprotection::aws:data-identifier/PgpPrivateKey`     |
| `arn:aws:dataprotection::aws:data-identifier/PkcsPrivateKey`    |
| `arn:aws:dataprotection::aws:data-identifier/PuttyPrivateKey`   |
