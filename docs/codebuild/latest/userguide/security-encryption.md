# Data encryption

Encryption is an important part of CodeBuild security. Some encryption, such as for data
in-transit, is provided by default and does not require you to do anything. Other
encryption, such as for data at-rest, you can configure when you create your project or
build.

- **Encryption of data at-rest** - Build artifacts,
  such as a cache, logs, exported raw test report data files, and build results,
  are encrypted by default using AWS managed keys. If you do not want to use
  these KMS keys, you must create and configure a customer managed key. For more
  information [Creating KMS Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md")
  and [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the _AWS Key Management Service
  User Guide_.

      + You can store the identifier of the AWS KMS key that CodeBuild uses to
       encrypt the build output artifact in the
       `CODEBUILD_KMS_KEY_ID` environment variable. For more
       information, see [Environment variables in build
       environments](build-env-ref-env-vars.md "build-env-ref-env-vars.md")
      + You can specify a customer managed key when you create a build
       project. For more information, see [Set the Encryption Key Using the Console](create-project.md#encryptionkey-console "create-project.md#encryptionkey-console") and [Set the encryption key using the
       CLI](create-project.md#cli.encryptionkey "create-project.md#cli.encryptionkey").

  The Amazon Elastic Block Store volumes of your build fleet are encrypted by default using AWS managed keys.

- **Encryption of data in-transit** - All
  communication between customers and CodeBuild and between CodeBuild and its downstream
  dependencies is protected using TLS connections that are signed using the
  Signature Version 4 signing process. All CodeBuild endpoints use SHA-256
  certificates that are managed by AWS Private Certificate Authority. For more information, see [Signature Version 4 signing
  process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") and [What is ACM PCA](../../../privateca/latest/userguide.md "../../../privateca/latest/userguide.md").
- **Build artifact encryption** - The CodeBuild service
  role associated with the build project requires access to a KMS key in order
  to encrypt its build output artifacts. By default, CodeBuild uses an
  AWS managed key for Amazon S3 in your AWS account. If you do not want to use this
  AWS managed key, you must create and configure a customer managed key. For more
  information, see [Encrypt build outputs](setting-up-kms.md "setting-up-kms.md") and [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in
  the _AWS KMS Developer Guide_.
