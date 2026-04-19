# Bundler compatibility

This guide contains information about CodeArtifact's compatibility with Bundler.

## Bundler compatibility

AWS CodeArtifact recommends Bundler 2.4.11 or higher. If you encounter issues with installation,
update the Bundler CLI to the latest version.

### Bundler version support

In Bundler versions lower than 2.4.11, there is a limit of 500 dependencies that can be defined in the
Gemfile before Bundler decides to query the full index, `specs.4.8.gz`. Since CodeArtifact does not support the
full index, specifying more than 500 dependencies will not work with CodeArtifact when using Bundler versions
lower than 2.4.11.

To define more than 500 dependencies in your Gemfile with CodeArtifact, update Bundler to version 2.4.11 or
higher.

### Bundler operations support

CodeArtifact's support for RubyGems does not include the Bundler Compact Index APIs (the `/versions` API is not supported).
CodeArtifact only supports the Dependencies API.

Because the Compact Index is not supported, Bundler resolves gems using the
Dependencies API (`/api/v1/dependencies`), which sends multiple gem names
in a single request. Each gem name in the request counts as a separate request toward
your account's _Read requests per second_ quota. For example, if
Bundler sends a dependency request containing 20 gem names, it counts as 20 requests
toward the quota. This can cause throttling in CI/CD environments with high concurrency,
even when the HTTP request count appears to be well below the configured limit. If you
experience throttling during Ruby gem resolution, request a quota increase for
_Read requests per second from a single AWS account_. For more
information, see [Quotas in AWS CodeArtifact](service-limits.md "service-limits.md").

Additionally, CodeArtifact does not support the various spec APIs, such as `specs.4.8.gz`.
