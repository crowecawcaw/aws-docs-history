# Determine which files to

invalidate

If you want to invalidate multiple files such as all of the files in a directory
or all files that begin with the same characters, you can include the `*`
wildcard at the end of the invalidation path. For more information about using the
`*` wildcard, see [Invalidation paths](invalidation-specifying-objects.md#invalidation-specifying-objects-paths "invalidation-specifying-objects.md#invalidation-specifying-objects-paths").

To invalidate files, you can specify either the path for individual files or a
path that ends with the `*` wildcard, which might apply to one file or to
many, as shown in the following examples:

- `/images/image1.jpg`
- `/images/image*`
- `/images/*`
  If you want to invalidate selected files but your users don’t necessarily access
  every file on your origin, you can determine which files viewers have requested from
  CloudFront and invalidate only those files. To determine which files viewers have
  requested, enable CloudFront access logging. For more information about access logs, see
  [Access logs (standard logs)](AccessLogs.md "AccessLogs.md").
