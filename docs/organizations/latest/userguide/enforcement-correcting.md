# Correcting non-compliant tags in

resources with AWS Organizations

After finding non-compliant tags, make corrections using any of the following methods.
You must be signed in to the account that has the resource with non-compliant
tags:

- Use the console or tagging API operations of the AWS service that created
  the non-compliant resources.
- Use the AWS Resource Groups [TagResources](../../../resourcegroupstagging/latest/APIReference/API_TagResources.md "../../../resourcegroupstagging/latest/APIReference/API_TagResources.md") and [UntagResources](../../../resourcegroupstagging/latest/APIReference/API_UntagResources.md "../../../resourcegroupstagging/latest/APIReference/API_UntagResources.md") operations to add tags that are compliant with the
  effective policy or to remove non-compliant tags.
