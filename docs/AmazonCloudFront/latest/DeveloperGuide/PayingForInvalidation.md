

# Pay for file invalidation
<a name="PayingForInvalidation"></a>

The first 1,000 invalidation paths that you submit per month are free; you pay for each invalidation path over 1,000 in a month. An invalidation path can be for a single file (such as `/images/logo.jpg`) or for multiple files (such as ` /images/*`). A path that includes the `*` wildcard counts as one path even if it causes CloudFront to invalidate thousands of files.

The maximum of 1,000 free invalidation paths per month applies to the total number of invalidation paths across all of the distributions that you create with one AWS account. For example, if you use the AWS account `john@example.com` to create three distributions, and you submit 600 invalidation paths for *each distribution* in a given month (for a total of 1,800 invalidation paths), AWS will charge you for the difference between the total invalidation paths and the 1000 free limit. In this example, AWS would charge you for 800 invalidation paths in that month.

The charge to submit an invalidation path is the same regardless of the number of files you’re invalidating: a single file (`/images/logo.jpg`) or all of the files that are associated with a distribution (`/*`). Because you're charged per path in your invalidation request, even if you bundle multiple paths into a single request, each path is still counted individually for billing purposes. 

For more information about invalidation pricing, see [Amazon CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/). For more information about invalidation paths, see [Invalidation paths](invalidation-specifying-objects.md#invalidation-specifying-objects-paths).

Tag invalidation paths count toward the same 1,000 free invalidation paths per month allowance. For example, if you submit 500 path invalidations and 600 tag invalidations in a month (for a total of 1,100 invalidation paths), you are charged for 100 invalidation paths. A single tag invalidation item (for example, ` #product:electronics`) counts as one path regardless of how many cached objects it invalidates — the same as a wildcard path invalidation (for example, ` /*`) counts as one path.

For more information about tag invalidation, see [Invalidating content by cache tags](invalidation-by-tags.md).