# Manual signing

Manual signing uses the Notation CLI and AWS Signer plugin to sign images before pushing
them to Amazon ECR. This method provides more control over the signing process and is useful when
you need to sign images outside of the push workflow or require fine-grained control over
signing operations.

For detailed instructions about signing container images using the Notation CLI and AWS Signer, see [Sign container images in Signer](../../../signer/latest/developerguide/container-workflow.md "../../../signer/latest/developerguide/container-workflow.md") and the related topics in the _AWS Signer Developer Guide_.

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
