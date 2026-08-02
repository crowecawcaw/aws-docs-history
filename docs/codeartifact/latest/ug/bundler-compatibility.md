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

Bundler resolves Ruby gem dependencies using one of two protocols: the Compact Index API
or the Dependencies API. CodeArtifact supports both. Bundler 2.4.11 and later prefer the Compact
Index API and fall back to the Dependencies API if it is unavailable; earlier versions only
use the Dependencies API. RubyGems 3.5.19 and later use the Compact Index API directly when
running `gem install`.

CodeArtifact supports the following Compact Index endpoints:

- `GET /versions`: Returns every gem in the repository with its
  full version list. Bundler and RubyGems use this endpoint as the entry point for
  dependency resolution.
- `GET /names`: Returns every gem name in the repository, sorted
  alphabetically.
- `GET /info/`gem-name``: Returns the
  version, dependency, and required-Ruby-version information for a single gem.

The `/versions` and `/names` endpoints support repositories that
contain up to 5,000 gems. Requests against repositories that contain more than 5,000 gems
return an HTTP 400 error.

CodeArtifact also supports the Bundler Dependencies API at `/api/v1/dependencies`.
A single request can include multiple gem names; for details on how multi-gem requests
are weighted against your account's _Read requests per second_ quota,
see [Quotas in AWS CodeArtifact](service-limits.md "service-limits.md").

Because `/versions` and `/names` return data for every gem in
the repository, CodeArtifact also weights these requests by the number of gems returned. CI/CD
environments running concurrent `bundle install` or `gem install`
operations can be throttled even when the HTTP request rate appears low. If you experience
throttling during Ruby gem resolution, request a quota increase for _Read requests
per second from a single AWS account_.

If you previously pinned RubyGems to a version below 3.5.19 as a workaround for
CodeArtifact compatibility, you can now remove that pin and upgrade to the latest version.

CodeArtifact does not support the legacy RubyGems specification indexes, including
`specs.4.8.gz`, `latest_specs.4.8.gz`, and
`prerelease_specs.4.8.gz`. These were superseded by the Compact Index API.

#### Testing Compact Index support

To verify that Compact Index resolution is working correctly with your CodeArtifact repository:

1. If you previously pinned RubyGems to a version below 3.5.19, remove the pin:

```
gem update --system
```

2. Verify your RubyGems and Bundler versions:

```
gem --version    # Should be 3.5.19 or higher
bundle --version # Should be 2.4.11 or higher
```

3. Test `gem install` against your CodeArtifact repository:

```
gem install <gem-name> --source https://<domain>-<account-id>.d.codeartifact.<region>.amazonaws.com/ruby/<repo>/
```

4. Test `bundle install` with verbose output to confirm Compact Index is being used:

```
bundle install --verbose 2>&1 | grep -i "compact\|/versions\|/info"
```

You should see requests to `/versions` and `/info/<gem-name>`
rather than `/api/v1/dependencies`.
