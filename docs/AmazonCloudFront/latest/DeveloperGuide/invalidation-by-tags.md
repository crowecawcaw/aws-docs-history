

# Invalidating content by cache tags
<a name="invalidation-by-tags"></a>

Amazon CloudFront supports tag invalidations, which lets you invalidate cached objects based on semantic tags rather than URL paths. This gives you flexible control over cache invalidation without requiring your URL structure to match your invalidation strategy.

## How tag invalidation works
<a name="invalidation-by-tags-how-it-works"></a>

1. **Configure your distribution**: Add a ` CacheTagConfig` to your distribution specifying the HTTP header name that your origin uses to return cache tags.

1. **Tag objects at your origin**: When returning an object you want to cache with tags, configure your origin to include the specified header in HTTP responses with comma-separated tag values.

   ```
   HTTP/1.1 200 OK
   Content-Type: text/html
   x-amz-meta-cache-tag: product:electronics, category:tv, brand:example
   Cache-Control: max-age=3600
   ```
**Note**  
For S3 origins, you can attach cache tags to your S3 objects as metadata. You can add a metadata entry with a key of your choice (example: ` cache-tag`) and a comma-separated list of tags as the value (example: `product:electronics, category:tv, brand:example`).  
S3 surfaces object metadata as response headers prefixed with ` x-amz-meta-<Key>`, so a metadata key of `cache-tag` would be returned as a `x-amz-meta-cache-tag` header. You can set the ` HeaderName` in your `CacheTagConfig` to ` x-amz-meta-cache-tag` to enable sending invalidations to these tags.
**Note**  
Alternatively, you can attach an origin response Lambda@Edge function to your cache behavior to add cache tag headers. If using Lambda@Edge, the header name does not need to follow the `x-amz-meta-<Key>` format.

1. **Invalidate by tag**: Use the ` CreateInvalidation` API with the `#` prefix to invalidate all objects cached with the specified tag.

   ```
   aws cloudfront create-invalidation \
     --distribution-id {{distribution_ID}} \
     --paths "#product:electronics"
   ```

   This invalidates ALL cached objects that contain the tag ` product:electronics`, regardless of their URL path.

## Tag format requirements
<a name="invalidation-by-tags-format"></a>

 **Origin response header value:** 
+ Tags are comma-separated in the header value.
+ Leading and trailing spaces around each tag are trimmed.
+ Both `tag1,tag2,tag3` and `tag1, tag2, tag3` are valid and equivalent.

 **Individual tag values:** 
+ ASCII visible characters (33–126)
+ No control characters, spaces, or commas
+ Case-insensitive
+ Maximum 256 characters per tag
+ Maximum 50 tags per object (additional tags are ignored)

## Configuring a distribution for tag invalidations
<a name="invalidation-by-tags-configuring"></a>

To enable tag invalidations, add a `CacheTagConfig` to your distribution configuration:

```
aws cloudfront create-distribution \
  --distribution-config '{
    "CallerReference": "my-distribution",
    "CacheTagConfig": {
      "HeaderName": "x-amz-meta-cache-tag"
    },
    "DefaultCacheBehavior": {
      "TargetOriginId": "myOrigin",
      "ViewerProtocolPolicy": "redirect-to-https",
      "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6"
    },
    "Origins": { ... },
    "Enabled": true,
    "Comment": "Distribution with tag support"
  }'
```

## Creating tag invalidations
<a name="invalidation-by-tags-creating"></a>

Use the `#` prefix in the `--paths` parameter to specify tags:

```
# Invalidate all objects tagged with "user1"
aws cloudfront create-invalidation \
  --distribution-id {{distribution_ID}} \
  --paths "#user1"

# Invalidate objects matching any of multiple tags (OR logic)
aws cloudfront create-invalidation \
  --distribution-id {{distribution_ID}} \
  --paths "#user1" "#product-category:electronics"

# Mix path and tag invalidations in one batch
aws cloudfront create-invalidation \
  --distribution-id {{distribution_ID}} \
  --paths "/index.html" "#user1" "/images/*" "#product-category:electronics"
```

## Checking invalidation status
<a name="invalidation-by-tags-checking-status"></a>

Use `GetInvalidation` to check the status. The response includes both path and tag items:

```
aws cloudfront get-invalidation \
  --distribution-id {{distribution_ID}} \
  --id {{invalidation_ID}}
```

## Important considerations
<a name="invalidation-by-tags-considerations"></a>
+ **Opt-in required**: Tag invalidation only works on distributions that have `CacheTagConfig` configured. Distributions without this configuration ignore cache tag headers from the origin.
+ **Tag processing limits**: CloudFront processes up to 50 tags per cached object. If an origin response contains more than 50 tags, the additional tags beyond the limit are not stored.
+ **Changing the header name**: Tag invalidations are looked up against the current `CacheTagConfig` configuration. If you change the `HeaderName` in the `CacheTagConfig`, invalidations issued to objects cached with tags under the old header name will no longer be evaluated. If you need to change the header name, start returning both the new and the old cache tags headers with your objects, then issue a path invalidation (for example, `/*`) or invalidate existing tags before changing the header name to avoid serving stale content. Once that's done you can stop sending the old cache tags header with your objects.
+ **Removing CacheTagConfig**: When you remove ` CacheTagConfig` from a distribution, CloudFront stops extracting tags from origin responses. Existing cached objects with tags are served normally until they expire or are invalidated by path.
+ **Backward compatibility**: Existing path and wildcard invalidations continue to work unchanged. Tag invalidations are additive — you can use both methods on the same distribution.
+ **Distribution tenants**: Tag invalidation is also supported for distribution tenants via the ` CreateInvalidationForDistributionTenant` API.

## Use case examples
<a name="invalidation-by-tags-examples"></a>

### Example 1: E-commerce product catalog
<a name="invalidation-by-tags-example-ecommerce"></a>

An e-commerce site tags cached product pages with product, category, and brand:

```
x-amz-meta-cache-tag: category:electronics, brand:acme, product:12345
```

When ACME updates their branding, invalidate all ACME products at once:

```
aws cloudfront create-invalidation \
  --distribution-id {{distribution_ID}} \
  --paths "#brand:acme"
```

### Example 2: User-generated content platform
<a name="invalidation-by-tags-example-ugc"></a>

A platform tags cached content with the owner's user ID:

```
x-amz-meta-cache-tag: user:12345, content-type:image
```

When a user closes their account, invalidate all their content after you've removed it from the origin:

```
aws cloudfront create-invalidation \
  --distribution-id {{distribution_ID}} \
  --paths "#user:12345"
```

### Example 3: Content versioning
<a name="invalidation-by-tags-example-versioning"></a>

A CMS tags content with version identifiers:

```
x-amz-meta-cache-tag: version:v2, template:homepage
```

When deploying a new version, invalidate all v2 content:

```
aws cloudfront create-invalidation \
  --distribution-id {{distribution_ID}} \
  --paths "#version:v2"
```