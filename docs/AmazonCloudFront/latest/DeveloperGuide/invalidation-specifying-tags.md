

# What you need to know when invalidating tags
<a name="invalidation-specifying-tags"></a>

When you specify a tag to invalidate, refer to the following information:

 **Opt-in required**   
Tag invalidation only works on distributions that have `CacheTagConfig` configured. Distributions without this configuration ignore cache tag headers from the origin. For more information, see [Invalidating content by cache tags](invalidation-by-tags.md).

 **Tag invalidation prefix**   
Tag invalidation items must begin with the `#` character. For example, to invalidate all cached objects tagged with `product:electronics`, specify ` #product:electronics` in the `Paths.Items` list.

 **Case sensitivity**   
Tag values are case-insensitive. For example, `#Product:Electronics` and ` #product:electronics` refer to the same tag.

 **Tag format**   
Each tag value must contain only ASCII visible characters (33–126), excluding commas. The maximum length of a tag is 256 characters.

 **No wildcard support**   
Unlike path invalidations, tag invalidation items do not support the `*` wildcard. Each `#`-prefixed item matches the exact tag value.

 **Maximum tags per cached object**   
CloudFront processes up to 50 tags per cached object. If an origin response contains more than 50 tags in the configured header, the additional tags beyond the limit are not stored and cannot be used for invalidation.

 **Forwarding cookies, headers, and query strings**   
When you invalidate by tag, CloudFront invalidates every cached variant of every object that carries the specified tag, regardless of associated cookies, headers, or query string parameters. You can't selectively invalidate some variants and not others.

 **Mixed path and tag invalidations**   
You can include both path items (for example, `/images/*`) and tag items (for example, `#brand:acme`) in the same invalidation batch in a `CreateInvalidation` request. Each item counts as one invalidation path toward your limits.

 **Maximum allowed**   
Tag invalidation items count toward the same concurrent invalidation limits as path items. Each tag item counts as one invalidation path. For more information, see [Quotas on invalidations](cloudfront-limits.md#limits-invalidations).

 **Changing the header name**   
If you change the `HeaderName` in `CacheTagConfig`, invalidations issued against tags extracted under the old header name will no longer be evaluated. Before changing the header name:  

1. Start returning both the old and new cache tag headers from your origin.

1. Issue a path invalidation (for example, `/*`) or invalidate existing tags.

1. Update `CacheTagConfig` with the new `HeaderName` .

1. Stop returning the old header from your origin.

 **Distribution tenants**   
Tag invalidation is also supported for distribution tenants via the ` CreateInvalidationForDistributionTenant` API.