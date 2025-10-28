# Cache builds to improve performance

You can save time when your project builds by using a cache. A cache can store reusable
pieces of your build environment and use them across multiple builds. Your build project can
use one of two types of caching: Amazon S3 or local. If you use a local cache, you must choose
one or more of three cache modes: source cache, Docker layer cache, and custom cache.

###### Note

Docker layer cache mode is available for the Linux environment only. If you choose
this mode, you must run your build in privileged mode. CodeBuild projects granted privileged
mode grants its container access to all devices. For more information, see [Runtime privilege and Linux capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities "https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities") on the Docker Docs website.

###### Topics

- [Amazon S3 caching](caching-s3.md "caching-s3.md")
- [Local caching](caching-local.md "caching-local.md")
- [Specify a local cache](specify-caching-local.md "specify-caching-local.md")
