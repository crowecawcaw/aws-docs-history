# Store objects and custom

error pages in different locations

If you want to store your objects and your custom error pages in different locations,
your distribution must include a cache behavior for which the following is true:

- The value of **Path Pattern** matches the path to your custom
  error messages. For example, suppose you saved custom error pages for 4xx errors
  in an Amazon S3 bucket in a directory named `/4xx-errors`. Your
  distribution must include a cache behavior for which the path pattern routes
  requests for your custom error pages to that location, for example,
  `/4xx-errors/*`.
- The value of **Origin** specifies the value of
  **Origin ID** for the origin that contains your custom
  error pages.
  For more information, see [Cache behavior
  settings](DownloadDistValuesCacheBehavior.md "DownloadDistValuesCacheBehavior.md").
