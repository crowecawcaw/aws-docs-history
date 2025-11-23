# Sign images in Amazon ECR

Amazon ECR integrates with AWS Signer to provide two ways for you to sign your container
images: _managed signing_ (automatic, recommended) and _manual signing_
(client-side). You can store both your container images and the signatures in your private
repositories.

## Choose a signing method

Amazon ECR supports two methods for signing container images:

**Managed signing** (recommended)

Managed signing automatically generates cryptographic signatures when images are pushed
to Amazon ECR. This method simplifies setup. Managed signing is the recommended
approach for most users. For more information, see [Managed signing](managed-signing.md "managed-signing.md").

**Manual signing**

Manual signing uses the Notation CLI and AWS Signer plugin to sign images before
pushing them to Amazon ECR. This method provides more control over the signing process and is
useful when you need to sign images outside of the push workflow or require fine-grained
control over signing operations. For more information, see [Manual signing](image-signing-manual.md "image-signing-manual.md").

## Considerations

The following should be considered when using Amazon ECR image signing:

- Signatures stored in your repository count against the service quota for
  the maximum number of images per repository. Each signature counts as 1 artifact against the images per repository quota. For more information, see [Amazon ECR service quotas](service-quotas.md "service-quotas.md").
- When reference artifacts are present in a repository, Amazon ECR lifecycle
  policies will automatically clean up those artifacts within 24 hours of the
  deletion of the subject image.
