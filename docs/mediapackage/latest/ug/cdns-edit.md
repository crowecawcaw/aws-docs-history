# Editing a Distribution

Edit an Amazon CloudFront distribution from the CloudFront console.

The only edit that
AWS Elemental MediaPackage can make to an origin is to create an origin when you add an endpoint
to a channel in MediaPackage. You can't edit a distribution from the MediaPackage
console.

To access the distribution in CloudFront, choose the distribution's ID on the channel's
details page. For more information about editing a distribution in CloudFront, see [Viewing and Updating
Distribution](../../../AmazonCloudFront/latest/DeveloperGuide/HowToUpdateDistribution.md "../../../AmazonCloudFront/latest/DeveloperGuide/HowToUpdateDistribution.md") in the _Amazon CloudFront Developer Guide_.

###### Important

When you're editing a distribution, do not change the default on the
**Tagging** page. CloudFront uses the AWS Elemental MediaPackage channel ID in
this tag to link the distribution and the channel together. If the tag is modified,
then you will no longer be able to view or manage the distribution from
MediaPackage.
