Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Encrypting a repository association in

Amazon CodeGuru Reviewer

All associated repositories in Amazon CodeGuru Reviewer are encrypted by default using a key that AWS
owns and manages for you. You can encrypt an associated repository using an AWS Key Management Service key,
known as a _KMS key_, that you manage. If you want to use a KMS key,
then you must create one in advance using AWS KMS, or create one when you create your
associated repository. For more information, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
_AWS Key Management Service Developer Guide_.

You can encrypt an associated repository with a KMS key only when you create it. If you
want to update how an existing repository is encrypted, you must disassociate it and then
recreate it with the encryption you want. For more information, see [Disassociate a repository in
CodeGuru Reviewer](disassociate-repository-association.md "disassociate-repository-association.md").

The encryption key (either an AWS owned and managed key, or a KMS key you create)
encrypts the associated repository and all of its code reviews. Each code review is a child
of the associated repository that contains the reviewed code.

If you encrypt an associated repository with a KMS key, then revoke access to that key
by disabling it or removing CodeGuru Reviewer access to AWS KMS using the AWS Identity and Access Management AWS CLI or SDK, the
following occurs:

- Recommendations related to the associated repository become unavailable.
- You cannot successfully review code in the associated repository. You can schedule
  a code review, but the code review fails.
  To restore access to an associated repository that is encrypted with a disabled key, you
  can re-enable it. For more information, see [Enabling and disabling keys](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md")
  in the _AWS Key Management Service Developer Guide_.

###### Note

Creation of an AWS KMS key results in charges to your AWS account. For more
information, see [AWS Key Management Service
pricing](https://aws.amazon.com/kms/pricing "https://aws.amazon.com/kms/pricing").

###### Topics

- [Encrypt an associated
  repository using an AWS KMS key](#encrypt-repository-association-how-to-use-cmk "#encrypt-repository-association-how-to-use-cmk")
- [Update how a
  repository association is encrypted](#encrypt-repository-association-how-to-change-cmk "#encrypt-repository-association-how-to-change-cmk")

## Encrypt an associated

repository using an AWS KMS key

You can use the Amazon CodeGuru Reviewer console to specify an AWS Key Management Service key (KMS key) to encrypt
your associated repository. If you don't do this, your associated repository is
encrypted by default using a key that is owned and managed by AWS.

###### Encrypt an associated repository using a KMS key

1. Follow the steps in one of the following topics to create an association with your
   repository type:
   - [Create an
     AWS CodeCommit repository association (console)](create-codecommit-association.md#create-codecommit-association-console "create-codecommit-association.md#create-codecommit-association-console")
   - [Create a
     Bitbucket repository association (console)](create-bitbucket-association.md#create-bitbucket-association-console "create-bitbucket-association.md#create-bitbucket-association-console")
   - [Create a
     GitHub or GitHub Enterprise Cloud repository association (console)](create-github-association.md "create-github-association.md")
   - [Create a
     GitHub Enterprise Server repository association (console)](create-github-enterprise-association.md#create-github-enterprise-association-console "create-github-enterprise-association.md#create-github-enterprise-association-console")

2. Expand **Additional configuration**.
3. Select **Customize encryption settings (advanced)**.
4. Do one of the following:
   - If you already have a KMS key that you manage, enter its Amazon Resource Name (ARN). For information
     about finding the ARN of your key using the console, see
     [Finding the
     key ID and key ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the _AWS Key Management Service Developer Guide_.
   - If you want to create a KMS key, choose **Create an AWS KMS key** and follow
     the steps in the AWS KMS console. For more information, see
     [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
     _AWS Key Management Service Developer Guide_.

5. Complete the rest of the steps to create your repository association.

## Update how a

repository association is encrypted

If you want to update how your associated repository is encrypted, you must
disassociate it, then recreate it. When you recreate the associated repository, specify
the AWS Key Management Service key (KMS key) you want to use. If you don't specify a KMS key, then
your data is encrypted by a key that is managed by AWS.

###### Change how an associated repository is encrypted

1. Disassociate your associated repository by following the steps in [Disassociate a repository
   in CodeGuru Reviewer (console)](disassociate-repository-association.md#disassociate-repository-association-console "disassociate-repository-association.md#disassociate-repository-association-console").
2. Follow the steps in one of the following topics to create an association with
   your repository type. Specify the KMS key you want to use or don't specify any
   KMS key if you want to encrypt your data using an AWS owned and managed key.
   - [Create an
     AWS CodeCommit repository association (console)](create-codecommit-association.md#create-codecommit-association-console "create-codecommit-association.md#create-codecommit-association-console")
   - [Create a
     Bitbucket repository association (console)](create-bitbucket-association.md#create-bitbucket-association-console "create-bitbucket-association.md#create-bitbucket-association-console")
   - [Create a
     GitHub or GitHub Enterprise Cloud repository association (console)](create-github-association.md "create-github-association.md")
   - [Create a
     GitHub Enterprise Server repository association (console)](create-github-enterprise-association.md#create-github-enterprise-association-console "create-github-enterprise-association.md#create-github-enterprise-association-console")
