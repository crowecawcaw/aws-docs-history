# Protecting data by using client-side encryption

_Client-side encryption_ is the act of encrypting your data
locally to help ensure its security in transit and at rest. To encrypt your objects before
you send them to Amazon S3, use the Amazon S3 Encryption Client. When your objects are encrypted in
this manner, your objects aren't exposed to any third party, including AWS. Amazon S3 receives
your objects already encrypted; Amazon S3 does not play a role in encrypting or decrypting your
objects. You can use both the Amazon S3 Encryption Client and [server-side encryption](serv-side-encryption.md "serv-side-encryption.md") to encrypt your data. When
you send encrypted objects to Amazon S3, Amazon S3 doesn't recognize the objects as being encrypted,
it only detects typical objects.

The Amazon S3 Encryption Client works as an intermediary between you and Amazon S3. After you instantiate the Amazon S3 Encryption Client, your objects are automatically encrypted and decrypted as part of your Amazon S3 `PutObject` and `GetObject` requests. Your objects are all encrypted with a unique data key. The Amazon S3 Encryption Client does not use or interact with bucket keys, even if you specify a KMS key as your wrapping key.

The _Amazon S3 Encryption Client Developer Guide_ focuses on
versions 3.0 and later of the Amazon S3 Encryption Client. For more information, see
[What is the Amazon S3 Encryption Client?](../../../amazon-s3-encryption-client/latest/developerguide/what-is-s3-encryption-client.md "../../../amazon-s3-encryption-client/latest/developerguide/what-is-s3-encryption-client.md") in the _Amazon S3 Encryption Client
Developer Guide_.

For more information about previous versions of the Amazon S3 Encryption client, see the AWS SDK Developer Guide for your programming language.

- [AWS SDK for Java](../../../sdk-for-java/v1/developer-guide/examples-crypto.md "../../../sdk-for-java/v1/developer-guide/examples-crypto.md")
- [AWS SDK for .NET](../../../sdk-for-net/v3/developer-guide/kms-keys-s3-encryption.md "../../../sdk-for-net/v3/developer-guide/kms-keys-s3-encryption.md")
- [AWS SDK for Go](../../../sdk-for-go/v1/developer-guide/welcome.md "../../../sdk-for-go/v1/developer-guide/welcome.md")
- [AWS SDK for PHP](../../../sdk-for-php/v3/developer-guide/s3-encryption-client.md "../../../sdk-for-php/v3/developer-guide/s3-encryption-client.md")
- [AWS SDK for Ruby](../../../sdk-for-ruby/v3/api/Aws/S3/Encryption.md "../../../sdk-for-ruby/v3/api/Aws/S3/Encryption.md")
- [AWS SDK for C++](../../../sdk-for-cpp/v1/developer-guide/welcome.md "../../../sdk-for-cpp/v1/developer-guide/welcome.md")
