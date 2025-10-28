# What you need to know when invalidating files

When you specify a file to invalidate, refer to the following information:

**Case
sensitivity**

Invalidation paths are case sensitive. For example,
`/images/image.jpg` and `/images/Image.jpg`
specify two different files.

**Changing the URI by using a Lambda function**

If your CloudFront distribution triggers a Lambda function on viewer request
events, and if the function changes the URI of the requested file, we
recommend that you invalidate both URIs to remove the file from CloudFront
edge caches:

- The URI in the viewer request
- The URI after the function changed it

###### Example

Suppose your Lambda function changes the URI for a file
from:

`https://d111111abcdef8.cloudfront.net/index.html`

To a URI that includes a language directory:

`https://d111111abcdef8.cloudfront.net/en/index.html`

To invalidate the file, you must specify the following
paths:

- `/index.html`
- `/en/index.html`

For more information, see [Invalidation paths](#invalidation-specifying-objects-paths "#invalidation-specifying-objects-paths").

**Default root object**

To invalidate the default root object (file), specify the path the
same way that you specify the path for any other file. For more
information, see [How default root object works](DefaultRootObject.md#DefaultRootObjectHow "DefaultRootObject.md#DefaultRootObjectHow").

**Forwarding cookies**

If you configured CloudFront to forward cookies to your origin, CloudFront edge
caches might contain several versions of the file. When you invalidate a
file, CloudFront invalidates every cached version of the file regardless of
its associated cookies. You can’t selectively invalidate some versions
and not others based on the associated cookies. For more information,
see [Cache content based on cookies](Cookies.md "Cookies.md").

**Forwarding headers**

If you configured CloudFront to forward a list of headers to your origin and
to cache based on the values of the headers, CloudFront edge caches might
contain several versions of the file. When you invalidate a file, CloudFront
invalidates every cached version of the file regardless of the header
values. You can’t selectively invalidate some versions and not others
based on header values. (If you configure CloudFront to forward all headers to
your origin, CloudFront doesn't cache your files.) For more information, see
[Cache content based on request headers](header-caching.md "header-caching.md").

**Forwarding query strings**

If you configured CloudFront to forward query strings to your origin, you
must include the query strings when invalidating files, as shown in the
following examples:

- `/images/image.jpg?parameter1=a`
- `/images/image.jpg?parameter1=b`

If client requests include five different query strings for the same
file, you can either invalidate the file five times, once for each query
string, or you can use the \* wildcard in the invalidation path, as shown
in the following example:

`/images/image.jpg*`

For more information about using wildcards in the invalidation path,
see [Invalidation paths](#invalidation-specifying-objects-paths "#invalidation-specifying-objects-paths").

For more information about query strings, see [Cache content based on query string
parameters](QueryStringParameters.md "QueryStringParameters.md").

To determine which query strings are in use, you can enable CloudFront
logging. For more information, see [Standard logging (access logs)](AccessLogs.md "AccessLogs.md").

**Maximum allowed**

For more information about the maximum number of invalidations
allowed, see [Concurrent invalidation request maximum](InvalidationLimits.md "InvalidationLimits.md").

**Microsoft Smooth Streaming files**

You can't invalidate media files in the Microsoft Smooth Streaming
format when you have enabled Smooth Streaming for the corresponding
cache behavior.

**Non-ASCII or unsafe characters in the
path**

If the path includes non-ASCII characters or unsafe characters as
defined in [RFC
1738](https://tools.ietf.org/html/rfc1738 "https://tools.ietf.org/html/rfc1738"), URL-encode those characters. Don't URL-encode any
other characters in the path, or CloudFront won't invalidate the old version
of the updated file.

###### Important

Don't use the `~` character in your path. CloudFront doesn't
support this character for invalidations, whether it's URL-encoded
or not.

**Invalidation paths**

The path is relative to the distribution. For example, to invalidate
the file at `https://d111111abcdef8.cloudfront.net/images/image2.jpg`,
you would specify `/images/image2.jpg`.

###### Note

In the [CloudFront
console](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home"), you can omit the leading slash in the path,
like this: `images/image2.jpg`. When you use the CloudFront API
directly, invalidation paths must begin with a leading slash.

You can also invalidate multiple files simultaneously by using the
`*` wildcard. The `*`, which replaces 0 or
more characters, must be the last character in the invalidation path.

###### Important

To use wildcards (\*) in the invalidation, you must put the wildcard at the end of the path. Asterisks (\*) inserted anywhere else are treated as a literal character match instead of a wildcard invalidation.

If you use the AWS Command Line Interface (AWS CLI) to invalidate files and you specify a
path that includes the `*` wildcard, you must use quotes
(`"`) around the path like `"/*"`.

The maximum length of a path is 4,000 characters.

###### Example: Invalidation paths

- To invalidate all files in a directory:

`/``directory-path``/*`

- To invalidate a directory, all of its subdirectories, and
  all files in the directory and subdirectories:

`/``directory-path``*`

- To invalidate all files that have the same name but
  different file name extensions, such as logo.jpg, logo.png,
  and logo.gif:

`/``directory-path``/``file-name``.*`

- To invalidate all of the files in a directory for which
  the file name starts with the same characters (such as all
  of the files for a video in HLS format), regardless of the
  file name extension:

`/``directory-path``/``initial-characters-in-file-name``*`

- When you configure CloudFront to cache based on query string
  parameters and you want to invalidate every version of a
  file:

`/``directory-path``/``file-name``.``file-name-extension``*`

- To invalidate all files in a distribution:

`/*`

For information about invalidating files if you use a Lambda function
to change the URI, see [Changing the URI Using a Lambda Function](#invalidation-lambda-at-edge "#invalidation-lambda-at-edge").

If the invalidation path is a directory and if you have not
standardized on a method for specifying directories—with or
without a trailing slash (/)—we recommend that you invalidate the
directory both with and without a trailing slash, for example,
`/images` and `/images/`.

**Signed
URLs**

If you are using signed URLs, invalidate a file by including only the
portion of the URL before the question mark (?).
