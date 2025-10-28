# Release: App Runner adds support for monorepo source-code based services on September 26, 2023

AWS App Runner now supports the deployment and maintenance for monorepo source-code based services.

**Release date:** September 26, 2023

## Changes

AWS App Runner now offers you the option to designate a repository source directory for your services. When you create an App Runner service you can enter the
application’s source directory along with the repository and branch. This source directory defines where your application’s build and start commands will
execute. App Runner can now create and support multiple App Runner services from a single repository with different source directories, allowing you to utilize a
monorepo based architecture.

If your source code management system doesn’t follow a monorepo architecture, you can continue to use the existing default root source directory for
your deployment strategy. However, if you need more flexibility to designate your source code repository to a source directory other than the top-level
repository directory, you can also benefit from this feature.

For more information, see [App Runner service based on source code](../dg/service-source-code.md "../dg/service-source-code.md") in the
_AWS App Runner Developer Guide_.
