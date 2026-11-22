

# Resource tags details

You can use the **resource** columns in AWS Cost and Usage Reports to find information about the specific resources covered by a line item. These columns include user-defined cost allocation tags. Examples include the following:

## resourceTags/user:creator
<a name="resource-details-creator"></a>

Use a **user:Creator** tag to track which user created a resource.

## resourceTags/user:name
<a name="resource-details-name"></a>

Use a **user:Name** tag to track which resources are associated with a specific user.

## resourceTags/user:owner
<a name="resource-details-owner"></a>

Use a **user:Owner** tag to track which user owns a resource.

## resourceTags/user:purpose
<a name="resource-details-purpose"></a>

Use a **user:Purpose** tag to track why a resource was created.

## resourceTags/aws:s3:PrefixLevel1 through resourceTags/aws:s3:PrefixLevel15
<a name="resource-details-s3-prefixlevel"></a>

AWS-generated cost allocation tags that split cost allocation data adds to Amazon S3 prefix line items. resourceTags/aws:s3:PrefixLevel1 holds the first segment of the prefix path, resourceTags/aws:s3:PrefixLevel2 the second, and so on through resourceTags/aws:s3:PrefixLevel15 for the deepest matched level. Levels deeper than the matched prefix are empty. On the unattributed line item, resourceTags/aws:s3:PrefixLevel1 is `(unattributed)`.

## resourceTags/aws:s3:BucketName
<a name="resource-details-s3-bucketname"></a>

An AWS-generated cost allocation tag that holds the name of the bucket on Amazon S3 prefix line items.