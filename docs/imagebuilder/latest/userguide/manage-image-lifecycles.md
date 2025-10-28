# Manage lifecycle policies for Image Builder images

When you create custom images, it's important that you have a plan to retire those images
before they become obsolete. Image Builder pipelines can apply updates and security patches
automatically. However, each build creates a new version of the image and all of the
associated resources that it distributes. Earlier versions remain in your account until you
manually delete them, or create a script to perform the task.

With Image Builder lifecycle management policies, you can automate the process of deprecating,
disabling, and deleting outdated images and their associated resources. Associated
resources can include output images that you've distributed to other AWS accounts,
organizations, and organizational units (OUs) across AWS Regions. You define the rules
for how and when to take each step in the lifecycle process, and which steps to include
in your policy.

###### Benefits of automated lifecycle management

Overall benefits of automated lifecycle management include the following:

- Simplifies lifecycle management for your custom images with an automated way to
  retire images and associated resources.
- Helps to prevent compliance risks that come from using outdated images to launch
  new instances.
- Keeps image inventories fresh by removing outdated images.
- Can reduce storage and data transfer costs by optionally removing associated
  resources for images that are deleted.

###### Realize cost savings

There is no cost to use EC2 Image Builder to create custom AMI or container images. However,
standard pricing applies for other services that are used in the process. When you remove unused or outdated images and their associated
resources from your AWS account, you can realize time and cost savings in the
following ways:

- Reduce the time it takes to patch existing images when you're not also patching
  unused or outdated images.
- For AMI image resources that you delete, you can choose to also remove distributed
  AMIs and their associated snapshots. This approach can save on the cost of storing
  snapshots.
- For container image resources that you delete, you can choose to delete underlying
  resources. This approach can save on Amazon ECR storage costs and data transfer rates for
  your Docker images that are stored in ECR repositories.

###### Note

Image Builder can't evaluate the potential impact for all possible downstream dependencies,
such as Auto Scaling groups or launch templates. You must consider downstream
dependencies for your images when you configure policy actions.

###### Contents

- [Lifecycle management prerequisites for
  Image Builder images](image-lifecycle-prerequisites.md "image-lifecycle-prerequisites.md")
- [List lifecycle management policies for Image Builder
  image resources](list-lifecycle-policies.md "list-lifecycle-policies.md")
- [View lifecycle policy details](view-lifecycle-policy.md "view-lifecycle-policy.md")
- [Create lifecycle policies](create-lifecycle-policies.md "create-lifecycle-policies.md")
- [How lifecycle management rules work for Image Builder image resources](image-lifecycle-rules.md "image-lifecycle-rules.md")
