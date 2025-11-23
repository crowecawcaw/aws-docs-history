# Archiving an image in Amazon ECR

## What is the ECR archival storage class?

Amazon ECR archival storage class is a new storage class that provides low-cost, long-term storage for
container images. Amazon ECR offers two storage classes:

- **ECR standard storage class** – The default storage
  class for active images that are regularly accessed.
- **ECR archival storage class** – A low-cost storage
  class for images that are rarely accessed but need to be retained for
  compliance or long-term reference. The archival storage class provides cost savings for large amount of images compared to the
  Standard storage class for long-term image retention. For detailed pricing
  information, see [Amazon ECR pricing](https://aws.amazon.com/ecr/pricing/ "https://aws.amazon.com/ecr/pricing/").

To archive images, you have two options. First, you can configure lifecycle rules to automatically archive images based on:

- Time since the image was pushed
- Time since the image was last pulled
- Number of images in the repository

You can also configure settings to permanently delete images after they've been
archived for a specified period. Refer to [Automate the cleanup of images by using lifecycle
policies in Amazon ECR](LifecyclePolicies.md "LifecyclePolicies.md") for more information.

You can also archive images using the Amazon ECR
console or AWS CLI. Refer to [Archiving an image](archive-image.md "archive-image.md") for more information.

When you need to use an archived image again, you can restore it back to the ECR
Standard storage class. You can expect ECR to restore the image within 20 minutes. Restored
images behave like newly pushed images and are immediately available for use when
the restore is complete. Restored images are subject to scanning,
replication, and repository lifecycle policies. Refer to [Restoring an image](restore-image.md "restore-image.md")
for more information.
