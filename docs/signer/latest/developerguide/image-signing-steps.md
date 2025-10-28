# Sign an image

The procedures on this page show you how create a signing profile, install a helper program, and sign a
container image.

## Step 1: Create a AWS Signer Notation signing profile

Create an AWS Signer Notation signing profile. If using the AWS Command Line Interface, API, AWS CloudFormation, or AWS SDKs set the platform ID to `Notation-OCI-SHA384-ECDSA`. In the console, for **signing platform** choose **Notation for container registries**. For more information on creating a signing profile, see [Create a Signer signing profile](signing-profiles.md "signing-profiles.md").

## Step 2: Install a helper program

Notation requires you to include a helper program in the client's host path in order to interact with the credential store. You
can use either the [Amazon Elastic Container Registry Docker credential helper](https://github.com/awslabs/amazon-ecr-credential-helper "https://github.com/awslabs/amazon-ecr-credential-helper") or the [Docker credential helper](https://github.com/docker/docker-credential-helpers "https://github.com/docker/docker-credential-helpers") to manage your credentials. We recommend using the Amazon ECR Docker credential helper, as it includes a credentials store and handles authentication for you. The Amazon ECR Docker Credential Helper not only stores and uses credentials when signing and verifying images in Amazon ECR, but also eliminates the need to use the Notation CLI notation login command or write custom logic to refresh authentication tokens and provide transparent access to your Amazon ECR repositories.

Download the [Amazon Elastic Container Registry Docker credential helper](https://github.com/awslabs/amazon-ecr-credential-helper "https://github.com/awslabs/amazon-ecr-credential-helper"). Configure `config.json` for use with Amazon ECR.

The following procedure explains how to install and configure the Docker credential helper.

###### To use the Docker credential helper

1. First set up a credentials store. Notation relies on a credentials store for secure storage and retrieval of credentials from Amazon ECR. Most operating systems come with a default credentials store, such as osxkeychain for macOS, or wincred for Windows. If you have the Docker CLI installed on the same host where Notation is installed, Notation uses the credentials store configuration that you set up for the Docker CLI.

Alternatively, you can install a third-party credentials store such as [pass](https://www.passwordstore.org "https://www.passwordstore.org"). You can pass these credentials to Notation as environment variables. For more information about environment variables, see [Configure environment variables to authenticate to an OCI-compliant registry](https://notaryproject.dev/docs/user-guides/how-to/registry-authentication/#configure-environment-variables-to-authenticate-to-an-oci-compliant-registry "https://notaryproject.dev/docs/user-guides/how-to/registry-authentication/#configure-environment-variables-to-authenticate-to-an-oci-compliant-registry") in the Notary Project user guide. 2. Download the [Docker
credential helper](https://github.com/docker/docker-credential-helpers "https://github.com/docker/docker-credential-helpers"). Set the `credsStore` option in `config.json` to the suffix of the program that you want to use. 3. Manually configure Notation client authentication. Because the Notation CLI doesn't support standard AWS authentication methods, you must manually configure Notation client authentication so that Amazon ECR knows who's requesting to sign (push signature) or verify (pull signature) an image. You can accomplish this with the Notation CLI `notation login` command, which authenticates to an Amazon ECR registry and provides an authorization token that's valid for 12 hours. Or, if you’re using the AWS Command Line Interface, you can use the `get-login-password` command which retrieves the token, decodes it, and converts into a `notation login` command for you.

The following command allows Notation to get credentials for authenticating with Amazon ECR:

```
aws ecr get-login-password --region `us-west-1` | notation login --username AWS --password-stdin `111122223333`.dkr.ecr.`us-west-1`.amazonaws.com
```

## Step 3: Sign the image using the Notation CLI

Use the Notation CLI to sign the image, specifying the image using the
repository name and the SHA256 digest. This creates the signature and pushes it
to the same Amazon ECR private repository that the image being signed is
in.

###### Note

You can specify the AWS Region and credentials profile that the
Notation plugin uses for interactions with AWS Signer either by
setting values for the `AWS_DEFAULT_REGION` and
`AWS_PROFILE` environment variables or by providing the
arguments **--plugin-config
aws-region=${`Region`}** and
**--plugin-config
aws-profile=${`profile-name`}**

In the following example, we're signing an image in the `curl`
repository with SHA digest
`sha256:ca78e5f730f9a789ef8c63bb55275ac12dfb9e8099e6EXAMPLE`.

```
`notation sign `111122223333`.dkr.ecr.`Region`.amazonaws.com/`curl@sha256:ca78e5f730f9a789ef8c63bb55275ac12dfb9e8099e6EXAMPLE` --plugin "com.amazonaws.signer.notation.plugin" --id "arn:aws:signer:`Region`:`111122223333`:/signing-profiles/`ecrSigningProfileName`"`
```

## Step 4: Verify image

After you have signed your container image, you can verify the signature
locally or during an Amazon EKS deployment and further manage the signature with
Amazon ECR.

- [Locally verify an image after signing](image-verification.md "image-verification.md")
- [Verify an image during in Amazon EKS or Kubernetes clusters](kubernetes-verification.md "kubernetes-verification.md")
- [Manage your signature in your Amazon ECR repository](../../../AmazonECR/latest/userguide/image-signing.md "../../../AmazonECR/latest/userguide/image-signing.md") in the _Amazon Elastic Container Registry User Guide_.
