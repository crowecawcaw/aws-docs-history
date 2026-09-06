

# Correcting non-compliant tags in resources
<a name="enforcement-correcting"></a>

After finding non-compliant tags, make corrections using any of the following methods. You must be signed in to the account that has the resource with non-compliant tags:
+ Use the console or tagging API operations of the AWS service that created the non-compliant resources.
+ Use the AWS Resource Groups [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) and [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html) operations to add tags that are compliant with the effective policy or to remove non-compliant tags. 