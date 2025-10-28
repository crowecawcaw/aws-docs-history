# Migrating IIS applications to Elastic Beanstalk

AWS Elastic Beanstalk provides a streamlined migration path for your Windows applications running on
Internet Information Services (IIS). The migration capability described in this chapter
significantly reduces the time and complexity that’s typically associated with cloud migrations,
helping you to maintain application functionality and configuration integrity during the
transition to AWS.

###### The **eb migrate** operation

Use the **eb migrate** command in the Elastic Beanstalk Command Line Interface (EB
CLI), to automatically discover, package, and deploy your IIS applications to the AWS Cloud.
The process maintains application functionality and preserves your configurations, including
bindings, application pools, and authentication settings.

The following steps summarize the process that the `eb migrate` operation
performs to transition your application to the AWS Cloud:

1. Discover IIS sites and their configurations.
2. Package application content and configuration.
3. Create Elastic Beanstalk environment and application.
4. Deploy the application with preserved settings.

###### Workflow and location execution options

The **eb migrate** command provides options for flexible migration workflows and execution
locations. By default, run the command on the target server that contains the application you want to migrate
to Elastic Beanstalk. If you can't run commands directly on the application server, use the `remote` option to run
the command from a bastion host that connects to the target server containing your application and configurations.
To complete the migration in two steps, you can also generate the migration package without deploying it
using the `archive-only` option and then deploy it later at your convenience using the `archive` option.

For reference information about the **eb migrate** command, see [eb migrate](eb3-migrate.md "eb3-migrate.md").

###### Topics

The following topics provide detailed information about migrating IIS applications to
Elastic Beanstalk:

- [Prerequisites](dotnet-migrating-applications-prerequisites.md "dotnet-migrating-applications-prerequisites.md") - Understand the required
  software, access, and permissions to migrate your Windows applications to AWS Elastic Beanstalk
  environments.
- [Migration glossary](dotnet-migrating-applications-glossary.md "dotnet-migrating-applications-glossary.md") - Understand how IIS components
  map to Elastic Beanstalk resources
- [Understanding IIS to Elastic Beanstalk migration mapping](dotnet-migrating-applications-mapping.md "dotnet-migrating-applications-mapping.md") - Understand how IIS components
  map to Elastic Beanstalk resources
- [Performing basic IIS
  migrations](dotnet-migrating-applications-basic-migration.md "dotnet-migrating-applications-basic-migration.md") - Learn how to perform
  basic migrations
- [Advanced migration scenarios](dotnet-migrating-applications-advanced-scenarios.md "dotnet-migrating-applications-advanced-scenarios.md") - Handle complex
  migration scenarios
- [Security configurations and IAM
  roles](dotnet-migrating-applications-security.md "dotnet-migrating-applications-security.md") - Configure security settings
  during migration
- [Network configuration and port settings](dotnet-migrating-applications-network.md "dotnet-migrating-applications-network.md") - Manage network and port
  configurations
- [Troubleshooting and diagnostics](dotnet-migrating-applications-troubleshooting.md "dotnet-migrating-applications-troubleshooting.md") - Troubleshoot common
  migration issues
- [Comparing migration options: EB CLI vs. AWS Application Migration Service](dotnet-migrating-applications-comparison.md "dotnet-migrating-applications-comparison.md") - Compare two primary
  migration options.
