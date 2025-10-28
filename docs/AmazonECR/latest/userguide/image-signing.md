# Signing an image stored in an Amazon ECR private

repository

Amazon ECR integrates with AWS Signer to provide a way for you to sign your container
images. You can store both your container images and the signatures in your private
repositories.

## Considerations

The following should be considered when using Amazon ECR image signing.

- Signatures stored in your repository count against the service quota for
  the maximum number of images per repository. For more information, see [Amazon ECR service quotas](service-quotas.md "service-quotas.md").
- When reference artifacts are present in a repository, Amazon ECR lifecycle
  policies will automatically clean up those artifacts within 24 hours of the
  deletion of the subject image.

## Prerequisites

Before you begin, The following prerequisites must be met.

- Install and configure the latest version of the AWS CLI. For more
  information, see [Installing or
  updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
  _AWS Command Line Interface User Guide_.
- Install the Notation CLI and the AWS Signer plugin for Notation. For
  more information, see [Prerequisites for signing container images](../../../signer/latest/developerguide/image-signing-prerequisites.md "../../../signer/latest/developerguide/image-signing-prerequisites.md") in the
  _AWS Signer Developer Guide_.
- Have a container image stored in an Amazon ECR private repository to sign. For
  more information, see [Pushing an image to an Amazon ECR private repository](image-push.md "image-push.md").

## Configure authentication for the

Notary client

Before you can create a signature using the Notation CLI, you must configure the
client so it can authenticate to Amazon ECR. If you have Docker installed on the same
host where you install the Notation client, then Notation will reuse the same
authentication method you use for the Docker client. The Docker `login`
and `logout` commands will allow the Notation `sign` and
`verify` commands to use those same credentials, and you don’t have
to separately authenticate Notation. For more information on configuring your
Notation client for authentication, see [Authenticate with OCI-compliant registries](https://notaryproject.dev/docs/user-guides/how-to/registry-authentication/ "https://notaryproject.dev/docs/user-guides/how-to/registry-authentication/") in the Notary Project
documentation.

If you are not using Docker or another tool that uses Docker credentials, then we
recommend using the Amazon ECR Docker Credential Helper as your credential store. For
more information on how to install and configure the Amazon ECR Credential Helper, see
[Amazon ECR
Docker Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper "https://github.com/awslabs/amazon-ecr-credential-helper").

## Signing an image

The following steps can be used to create the resources necessary to sign a container
image and store the signature in an Amazon ECR private repository. Notation signs images using
the digest.

###### To sign an image

1. Create an AWS Signer signing profile using the
   `Notation-OCI-SHA384-ECDSA` signing platform. You can optionally
   specify a signature validity period using the
   `--signature-validity-period` parameter. This value may be specified
   using `DAYS`, `MONTHS`, or `YEARS`. If no validity
   period is specified, the default value of 135 months is used.

```
`aws signer put-signing-profile --profile-name `ecr_signing_profile` --platform-id Notation-OCI-SHA384-ECDSA`
```

###### Note

The signing profile name only supports alphanumeric characters and the
underscore (`_`). 2. Authenticate the Notation client to your default registry. The following example
uses the AWS CLI to authenticate the Notation CLI to an Amazon ECR private
registry.

```
`aws ecr get-login-password --region `region` | notation login --username AWS --password-stdin `111122223333`.dkr.ecr.`region`.amazonaws.com`
```

3. Use the Notation CLI to sign the image, specifying the image using the repository name and the SHA digest. This creates the signature and pushes it
   to the same Amazon ECR private repository that the image being signed is in.

In the following example, we are signing an image in the `curl` repository with SHA digest `sha256:ca78e5f730f9a789ef8c63bb55275ac12dfb9e8099e6EXAMPLE`.

```
`notation sign `111122223333`.dkr.ecr.`region`.amazonaws.com/`curl@sha256:ca78e5f730f9a789ef8c63bb55275ac12dfb9e8099e6EXAMPLE` --plugin "com.amazonaws.signer.notation.plugin" --id "arn:aws:signer:`region`:`111122223333`:/signing-profiles/`ecrSigningProfileName`"`
```

## Next steps

After you sign your container image, you can verify the signature locally. For
instructions about verifying an image, see [Verify an image
locally after signing](../../../signer/latest/developerguide/image-verification.md "../../../signer/latest/developerguide/image-verification.md") in the _AWS Signer Developer
Guide_.
