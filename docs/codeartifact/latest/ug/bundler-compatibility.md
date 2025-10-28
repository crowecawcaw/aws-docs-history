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

Additionally, CodeArtifact does not support the various spec APIs, such as `specs.4.8.gz`.
