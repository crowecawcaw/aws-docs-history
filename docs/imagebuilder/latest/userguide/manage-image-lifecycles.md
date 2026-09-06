# Manage lifecycle policies for Image Builder images

EC2 Image Builder lifecycle policies automate deprecation, disabling, and deletion
of outdated images and their associated resources. Each pipeline build creates a new image
version and distributes associated resources. Without lifecycle policies, earlier versions
remain in your account until you delete them manually.

Lifecycle policies define rules that control when and how Image Builder retires outdated images.
Associated resources include output images distributed to other AWS accounts,
organizations, and organizational units (OUs). These resources can span multiple
AWS Regions. You specify which lifecycle steps to include and when each step runs.

Enabled lifecycle policies run automatically once per day. Image Builder manages the
execution schedule. For execution details, see
[How lifecycle policy execution works](lifecycle-policy-execution.md "lifecycle-policy-execution.md").

###### Tip

For information about a deployable lifecycle policy example with ready-to-use
policy documents, see the [lifecycle sample](https://github.com/aws-samples/amazon-ec2-image-builder-samples/tree/HEAD/lifecycle "https://github.com/aws-samples/amazon-ec2-image-builder-samples/tree/HEAD/lifecycle") on GitHub. For more information, see
[Explore Image Builder sample projects on GitHub](sample-projects.md "sample-projects.md").

###### Benefits of automated lifecycle management

Automated lifecycle management:

- Automates retirement of images and their associated resources across
  accounts and Regions.
- Eliminates compliance risks from launching new instances with outdated
  images.
- Maintains fresh image inventories by removing obsolete versions.
- Reduces infrastructure costs by removing associated resources
  when you delete images.

###### Cost savings

There is no cost to use EC2 Image Builder to create custom AMI or container images. However,
standard pricing applies for other services that are used in the process. Removing outdated images and associated resources reduces
costs:

- Reduces the number of images you need to patch by removing outdated versions.
- Removes distributed AMIs and their associated snapshots when you delete AMI image
  resources, eliminating snapshot storage costs.
- Deletes underlying resources when you delete container image resources,
  eliminating Amazon ECR storage costs and data transfer charges.

###### Note

Before you configure policy actions, verify that no downstream dependencies
reference images the policy removes. Image Builder does not evaluate the impact on downstream
dependencies such as Auto Scaling groups or launch templates.

###### Contents

- [Lifecycle management prerequisites for Image Builder images](image-lifecycle-prerequisites.md "image-lifecycle-prerequisites.md")
- [List lifecycle management policies for Image Builder image resources](list-lifecycle-policies.md "list-lifecycle-policies.md")
- [View lifecycle policy details](view-lifecycle-policy.md "view-lifecycle-policy.md")
- [Create lifecycle policies](create-lifecycle-policies.md "create-lifecycle-policies.md")
- [How lifecycle policy execution works](lifecycle-policy-execution.md "lifecycle-policy-execution.md")
- [How lifecycle management rules work for Image Builder image resources](image-lifecycle-rules.md "image-lifecycle-rules.md")
