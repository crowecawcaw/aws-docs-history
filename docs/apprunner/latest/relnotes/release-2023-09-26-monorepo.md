

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds support for monorepo source-code based services on September 26, 2023
<a name="release-2023-09-26-monorepo"></a>

AWS App Runner now supports the deployment and maintenance for monorepo source-code based services.

**Release date:** September 26, 2023

## Changes
<a name="release-2023-09-26-monorepo.changes"></a>

AWS App Runner now offers you the option to designate a repository source directory for your services. When you create an App Runner service you can enter the application’s source directory along with the repository and branch. This source directory defines where your application’s build and start commands will execute. App Runner can now create and support multiple App Runner services from a single repository with different source directories, allowing you to utilize a monorepo based architecture.

If your source code management system doesn’t follow a monorepo architecture, you can continue to use the existing default root source directory for your deployment strategy. However, if you need more flexibility to designate your source code repository to a source directory other than the top-level repository directory, you can also benefit from this feature.

For more information, see [App Runner service based on source code](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html) in the *AWS App Runner Developer Guide*.