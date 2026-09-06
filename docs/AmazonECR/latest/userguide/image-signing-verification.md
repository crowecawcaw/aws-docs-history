

# Signature verification
<a name="image-signing-verification"></a>

After you sign your container images, you can verify the signatures to ensure that images have not been tampered with and come from a trusted source. Amazon ECR supports several methods for verifying signatures:

## Managed verification with Amazon EKS
<a name="image-signing-verification-managed"></a>

Amazon EKS provides native integration for automatic signature verification. When you configure signature verification in your Amazon EKS clusters, the service automatically verifies image signatures before allowing containers to run. For more information about configuring signature verification, see [Validate container image signatures during deployment](https://docs.aws.amazon.com/eks/latest/userguide/image-verification.html) in the *Amazon EKS User Guide*.

## Lambda admission controller for Amazon ECS
<a name="image-signing-verification-lambda"></a>

Amazon ECS provides service lifecycle hooks that allow you to run custom logic during service deployments. These hooks can trigger AWS Lambda functions at specific points in the deployment process, enabling you to validate container image signatures before allowing services to start. For more information, see [Verify container image signatures for Amazon ECS](https://docs.aws.amazon.com/signer/latest/developerguide/ecs-verification.html) in the *AWS Signer Developer Guide*.

## Manual verification with Notation CLI
<a name="image-signing-verification-manual"></a>

You can verify signatures manually using the Notation CLI. This method requires you to install and configure the Notation CLI on your local machine or in your verification environment. For detailed instructions about verifying an image using Notation CLI, see [Verify an image locally after signing](https://docs.aws.amazon.com/signer/latest/developerguide/image-verification.html) in the *AWS Signer Developer Guide*.

## Configure authentication for the Notation client
<a name="image-signing-authentication"></a>

If you use manual signing or verify signatures manually using the Notation CLI, you must configure the Notation client so it can authenticate to Amazon ECR. If you have Docker installed on the same host where you install the Notation client, then Notation will reuse the same authentication method you use for the Docker client. The Docker `login` and `logout` commands will allow the Notation `sign` and `verify` commands to use those same credentials, and you don't have to separately authenticate Notation. For more information on configuring your Notation client for authentication, see [Authenticate with OCI-compliant registries](https://notaryproject.dev/docs/user-guides/how-to/registry-authentication/) in the Notary Project documentation.

If you are not using Docker or another tool that uses Docker credentials, then we recommend using the Amazon ECR Docker Credential Helper as your credential store. For more information on how to install and configure the Amazon ECR Credential Helper, see [Amazon ECR Docker Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper).