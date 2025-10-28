AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Troubleshooting AWS Migration Hub

This page provides troubleshooting guidance for AWS Migration Hub, as well as links to topics on
how to troubleshoot issues with AWS Application Discovery Service, Agentless Collector, and Migration
Evaluator.

###### Topics

- [My migrations do not appear in
  Migration Hub](#migs-do-not-appear-in-hub "#migs-do-not-appear-in-hub")
- [Updates about my migrations don't appear
  inside an application](#migs-do-not-appear-in-app "#migs-do-not-appear-in-app")
- [My API call failed](#api-call-failed-status "#api-call-failed-status")
- [Errors enabling data collection](#data-collection-errors "#data-collection-errors")
- [Troubleshooting AWS Application Discovery Service issues](#app-discovery-issues "#app-discovery-issues")
- [Troubleshooting Agentless Collector
  issues](#agentless-collector-issues "#agentless-collector-issues")
- [Troubleshooting Migration Evaluator
  issues](#migration-evaluator-issues "#migration-evaluator-issues")

## My migrations do not appear in

Migration Hub

If you are not seeing your applications' migration status updates on the
**Updates** page in Migration Hub, it could be due to one of the
following reasons:

- You have not selected a home Region or you are not currently viewing the home
  Region console.
- Migration tools are not authorized to communicate with Migration Hub.
- You do not have the necessary policies and roles set up in IAM.
- Migration status mapping is incorrect or needs to be done manually.

### Authentication issues

To make sure authentication is occurring correctly:

- Check whether the migration tools you are using have been authorized to
  communicate with Migration Hub. For more information, see [steps to authorize a migration
  tool](gs-new-user-migration.md#migrate-wt-migrate-using-tools "gs-new-user-migration.md#migrate-wt-migrate-using-tools").
- Check the [Tools
  page](http://console.aws.amazon.com/migrationhub/migrate/tools "http://console.aws.amazon.com/migrationhub/migrate/tools") to see the status of connected tools. Learn more about
  setting up necessary policies and roles in [Managed policies and roles](new-customer-setup.md#required-managed-policies "new-customer-setup.md#required-managed-policies").

### Migration status matching when using AWS discovery

tools

- Check whether a migration update must be manually mapped or was
  incorrectly mapped to a discovered server, see [Tracking migration updates in AWS Migration Hub](updates-tracking-wt.md "updates-tracking-wt.md").

## Updates about my migrations don't appear

inside an application

If you are not seeing your migration updates associated with an application, it could
be due to one of the following reasons:

- Servers not being grouped as an application.
- Migration update status not being refreshed.
- Migration updates are not mapped or are incorrectly mapped to a server.

### Servers application grouping issues

- Check whether all your servers have been grouped into an application. See
  [steps to group servers
  into applications](gs-new-user-migration.md#migrate-wt-group-as-applications "gs-new-user-migration.md#migrate-wt-group-as-applications").

### Update status issues

- The application details page requires you to refresh the page to see the
  latest status. See [steps to track status of
  migrations](migrate-wt-track.md "migrate-wt-track.md").

### Update and server mapping issues

- Check whether the update is present on **Updates**
  page.
- If not on the **Updates** page, then check whether the
  migration tool was authorized by looking on the **Migration
  Tools** page - in the navigation pane, under
  **Migrate**, choose **Tools**.
- On the **Updates** page, verify that the update is mapped
  to the correct server (it will show "Edit" in "Mapped servers"
  column).
- If mapped to a server on the **Updates** page, then
  verify whether the server is grouped into an application on the
  **Servers** page with an application name present in
  the "Applications" column.

## My API call failed

- Check whether you called `GetHomeRegion` before your call, if
  required.
- You can use the AWS Migration Hub home Region APIs within your home Region only. API
  calls originating from outside your home Region are rejected, except for the
  ability to register your agents and collectors.

## Errors enabling data collection

Although you can register discovery agents and collectors outside of your AWS Migration Hub
home Region, you cannot start data collection outside the home Region. The Application Discovery Service
`StartDataCollection` API call prevents you from enabling data collection
outside the home Region.

## Troubleshooting AWS Application Discovery Service issues

See [Troubleshooting AWS Application Discovery Service](../../../application-discovery/latest/userguide/troubleshooting.md "../../../application-discovery/latest/userguide/troubleshooting.md").

## Troubleshooting Agentless Collector

issues

See [Troubleshooting Agentless Collector](../../../application-discovery/latest/userguide/agentless-collector-troubleshooting.md "../../../application-discovery/latest/userguide/agentless-collector-troubleshooting.md").

## Troubleshooting Migration Evaluator

issues

See the [Collector Installation Guide](https://d1.awsstatic.com/migration-evaluator-resources/ME_TSOLogic_Agentless-Collector-Install-Guide_English.pdf "https://d1.awsstatic.com/migration-evaluator-resources/ME_TSOLogic_Agentless-Collector-Install-Guide_English.pdf") on the [Migration Evaluator
Resources](https://aws.amazon.com/migration-evaluator/resources/ "https://aws.amazon.com/migration-evaluator/resources/") page.
