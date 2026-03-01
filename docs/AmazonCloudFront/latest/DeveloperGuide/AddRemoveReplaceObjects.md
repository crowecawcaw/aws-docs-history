# Add, remove, or replace content that CloudFront distributes

This section explains how to make sure CloudFront can access the content that you want to be served to
your viewers, how to specify the objects in your website or in your application, and how to remove or replace
content.

###### Topics

- [Add and access content that CloudFront distributes](#AddingObjects "#AddingObjects")
- [Use file versioning to update or remove content with a CloudFront distribution](UpdatingExistingObjects.md "UpdatingExistingObjects.md")
- [Customize the URL format for files in CloudFront](LinkFormat.md "LinkFormat.md")
- [Specify a default root object](DefaultRootObject.md "DefaultRootObject.md")
- [Invalidate files to remove content](Invalidation.md "Invalidation.md")
- [Serve compressed files](ServingCompressedFiles.md "ServingCompressedFiles.md")

## Add and access content that CloudFront distributes

When you want CloudFront to distribute content (objects), you add files to one
of the origins that you specified for the distribution, and you expose a CloudFront link to the
files. A CloudFront edge location doesn't fetch the new files from an origin until the edge
location receives viewer requests for them. For more information, see
[How CloudFront delivers content](HowCloudFrontWorks.md "HowCloudFrontWorks.md").

When you add a file that you want CloudFront to distribute, make sure that you add it to one
of the Amazon S3 buckets specified in your distribution or, for a custom origin, to a directory
in the specified domain. In addition, confirm that the path pattern in the applicable cache
behavior sends requests to the correct origin.

For example, suppose the path pattern for a
cache behavior is `*.html`. If you don't have any other cache behaviors configured to forward
requests to that origin, CloudFront will only forward `*.html` files. In this scenario,
for example, CloudFront will never distribute .jpg files that you upload to the origin, because
you haven't created a cache behavior that includes .jpg files.

CloudFront servers don't determine the MIME type for the objects that they serve. When you upload
a file to your origin, we recommend that you set the `Content-Type` header field for it.
