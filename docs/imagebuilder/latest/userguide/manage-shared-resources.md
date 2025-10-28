# Share Image Builder resources with AWS RAM

EC2 Image Builder integrates with AWS Resource Access Manager (AWS RAM) so that you can share the following types
of Image Builder resources with any AWS account or through AWS Organizations.

- Components
- Images
- Recipes
  To share resources through AWS RAM, you must create a resource share. A resource share
  specifies the resources to share and the consumers with whom to share them. Consumers can
  be individual AWS accounts, organizational units, or an entire organization in AWS Organizations.
  The following list includes the types of accounts and organizations that you can share with.

- Specific AWS accounts inside or outside of its organization in
  AWS Organizations.
- An organizational unit (OU) inside of its organization in AWS Organizations.
- Its entire organization in AWS Organizations.
- AWS Organizations or OUs outside of its organization.
  In this model, the AWS account that owns the resource (owner) shares it with other
  AWS accounts or through AWS Organizations (consumers) within the same Region. When a shared
  resource is updated, consumers get those updates automatically.

###### Note

Shared components, images, and image recipes count toward the corresponding resource
limits of the owner only. The resource limits of the consumers are not affected by the
resources that are shared with them.

###### Topics

- [Resource owners](#share-ib-resources-owners "#share-ib-resources-owners")
- [Resource consumers](#share-ib-resources-comsumers "#share-ib-resources-comsumers")
- [Create an AWS RAM resource share for your Image Builder resources](manage-shared-resources-share.md "manage-shared-resources-share.md")
- [Unshare an Image Builder resource from AWS RAM](manage-shared-resources-unshare.md "manage-shared-resources-unshare.md")

## Resource owners

Image Builder resources can only be shared in the AWS Region where they are created. When you
share these resources, they will not replicate across Regions.

To get a list of the Image Builder resources that you own and can share, specify the ownership filter
in the console or when you run the command in the AWS CLI.

- [List Image Builder components](component-details.md#list-components "component-details.md#list-components")
- [List images](image-details-list.md#list-images "image-details-list.md#list-images")
- [List and view image recipe details](image-recipe-details.md "image-recipe-details.md")
- [List and view container recipe details](container-recipe-details.md "container-recipe-details.md")

For more information about AWS RAM, see the [_AWS RAM User Guide_](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

### Prerequisites for sharing

Image Builder resources

To share an Image Builder resource, such as a component, image, or recipe:

- Your AWS account must own the Image Builder resource that you want to share. You
  cannot share resources that have been shared with you.
- The AWS Key Management Service (AWS KMS) key associated with encrypted resources must be
  explicitly shared with the target accounts, organizations, or OUs.
- In order to share your Image Builder resources with AWS Organizations and OUs using AWS RAM, you
  must enable sharing. For more information, see
  [Enable
  Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS RAM User Guide_.
- If you distribute an image encrypted with AWS KMS across accounts in different
  Regions, you must create a KMS key and alias in each target Region.
  Additionally, the people who will be launching instances in those Regions
  will need access to the KMS key specified via the Key Policy.

The following resources that Image Builder creates from your pipeline build are not considered
Image Builder resources – rather, they are external resources that Image Builder distributes in
your account, and to the AWS Regions, accounts, and organizations or organizational
units (OUs) that you specify in your distribution configuration.

- Amazon Machine Images (AMIs)
- Container images that reside in Amazon ECR

For more information about distribution settings for your AMI, see [Create and update AMI distribution configurations](cr-upd-ami-distribution-settings.md "cr-upd-ami-distribution-settings.md").
For more information about distribution settings for your container image in Amazon ECR,
see [Create and update distribution settings
for container images](cr-upd-container-distribution-settings.md "cr-upd-container-distribution-settings.md").

For more information about sharing your AMI with AWS Organizations and OUs,
see [Share an
AMI with organizations or OUs](../../../AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.md "../../../AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.md").

## Resource consumers

Consumers can use a shared resource, but cannot modify it in any way. When they create
Image Builder recipes, they can specify a shared image as the base image, and they can add shared
components. They can also specify a shared recipe when they create an Image Builder image pipeline,
or when they use the **create-image** command in the AWS CLI.

If you belong to an organization in AWS Organizations, and sharing within your organization is
enabled, consumers in your organization are automatically granted access to the shared
resource. Otherwise, consumers receive an invitation to join the resource share and are granted
access to the shared resource after accepting the invitation.
