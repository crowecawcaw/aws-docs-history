

# Manual signing
<a name="image-signing-manual"></a>

Manual signing uses the Notation CLI and AWS Signer plugin to sign images before pushing them to Amazon ECR. This method provides more control over the signing process and is useful when you need to sign images outside of the push workflow or require fine-grained control over signing operations.

For detailed instructions about signing container images using the Notation CLI and AWS Signer, see [Sign container images in Signer](https://docs.aws.amazon.com/signer/latest/developerguide/container-workflow.html) and the related topics in the *AWS Signer Developer Guide*.

## Prerequisites
<a name="image-signing-prerequisites"></a>

Before you begin, The following prerequisites must be met.
+ Install and configure the latest version of the AWS CLI. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.
+ Install the Notation CLI and the AWS Signer plugin for Notation. For more information, see [Prerequisites for signing container images](https://docs.aws.amazon.com/signer/latest/developerguide/image-signing-prerequisites.html) in the *AWS Signer Developer Guide*.
+ Have a container image stored in an Amazon ECR private repository to sign. For more information, see [Pushing an image to an Amazon ECR private repository](image-push.md).