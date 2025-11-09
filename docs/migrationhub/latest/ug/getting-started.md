AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Getting started with AWS Migration Hub

In this section, you can find information about how to get started with AWS Migration Hub.
Included are steps to introduce you to the initial console pages that Migration Hub presents to a new
user.

###### Note

If you are a developer or are interested in sending migration status from a migration
tool, script, or custom code, see [AWS Migration Hub API](api-reference.md "api-reference.md") and [AWS Migration Hub Home Region API
Reference](../../../migrationhub-home-region/latest/APIReference/Welcome.md "../../../migrationhub-home-region/latest/APIReference/Welcome.md").

All Migration Hub and AWS Application Discovery Service API commands must be called from within the home Region only,
and they require you to call `GetHomeRegion` at least once before you call any
other API, to obtain the account's Migration Hub home Region. Calls originating from outside your
home Region are rejected.

## Prerequisites

To perform the steps in this getting-started section, you must first ensure the following:

- You have signed up for AWS. For more information, see [Setting up AWS Migration Hub](setting-up.md "setting-up.md").
- You have selected your Migration Hub home Region. For information, see [Managing your AWS Migration Hub home Region](home-region.md "home-region.md").

Here's what to expect:

- Migration Hub monitors the status of your migrations in all AWS Regions, provided that
  your migration tools are available in each Region.
- The migration status of every AWS Region undergoing migration is shown in your home
  Region console.
- The migration tools that integrate with Migration Hub store all data about your migration
  status in Migration Hub. The data is stored in your selected home Region.
- The migration tools do not send a status unless you have authorized their
  connection.
- For a list of AWS Regions where you can use Migration Hub, see the [Amazon Web Services General Reference](../../../general/latest/gr/rande.md#migrationhub_region "../../../general/latest/gr/rande.md#migrationhub_region").
- For more information about working with your home Region, see the section about [Managing your AWS Migration Hub home Region](home-region.md "home-region.md").

## Access to AWS Migration Hub

AWS Migration Hub tracks the status of application migrations on the AWS Migration Hub console in your
home Region. The Getting Started section and other sections of this guide use the console to
illustrate migration functionality. Open the AWS Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").

Additionally, you can use the AWS Migration Hub API to track the status of your migrations from
other tools, or to send custom migration status to AWS Migration Hub. For more information about the
Migration Hub API, see [AWS Migration Hub API](api-reference.md "api-reference.md"). You'll also
need to call the `GetHomeRegion` API from the Migration Hub [home region API](../../../migrationhub-home-region/latest/APIReference/Welcome.md "../../../migrationhub-home-region/latest/APIReference/Welcome.md")
when working with Migration Hub programmatically.

The AWS SDKs assist you to develop applications that interact with Migration Hub. The AWS
SDKs for Java, .NET, and PHP wrap the underlying Migration Hub API to simplify your programming
tasks. For information about downloading the SDK libraries, see [Sample Code Libraries](http://aws.amazon.com/code "http://aws.amazon.com/code").

###### Topics

- [Discover on-premises resources using AWS Migration Hub
  discovery tools](gs-new-user-discovery.md "gs-new-user-discovery.md")
- [Migrate to AWS by using AWS Migration Hub migration
  tools and tracking](gs-new-user-migration.md "gs-new-user-migration.md")
- [Track the status of your migrations in AWS Migration Hub](migrate-wt-track.md "migrate-wt-track.md")
