# Performing a large data migration with AWS DataSync

Large-scale data migrations can involve transferring significant volumes of data that
encompass millions of files or objects in various formats. AWS DataSync simplifies these
complex transfers by managing scheduling, monitoring, encryption, and data
verification.

## What is a large data migration?

A large data migration typically involves transferring terabytes or more of data
spread across various sources to a new destination storage environment (in this case,
AWS). These migrations require careful planning and coordination within your
organization to move data successfully while minimizing business disruption.

DataSync can simplify these migrations, which are usually complex in nature. Some
benefits of using DataSync for your migration include:

- Automated management of data-transfer processes and the infrastructure
  required for high performance and secure data transfers.
- End-to-end security, including encryption and data integrity validation, to
  help ensure that your data arrives securely, intact, and ready to use.
- A purpose-built network protocol and a parallel, multi-threaded architecture
  to speed up migrations.

## Key stages of a large data

migration

You can usually break down a large migration into the following stages:

- **(Stage 1) Planning your data migration** - At
  this stage, you're trying to understand why you're migrating and what sort of
  data you're working with. Planning activities include:
  - Understanding why you want to migrate
  - Assembling a team to help you with all aspects of the
    migration.
  - Identifying data locations, formats, and usage patterns
  - Assessing available hardware resources and network requirements
    (if
    you're migrating from an on-premises data
    center)
  - Running proof of concept (POC) tests with DataSync to estimate migration
    timelines, plan cutover windows, and get a sense of how you need to
    configure DataSync

- **(Stage 2) Implementing your large data
  migration** - At this point, you're validating your plan and
  starting the migration. Implementation activities include:
  - Validating the migration plan
  - Executing phased cutovers that include monitoring and verifying your
    data transfers as expected
  - Optimizing and adjusting as needed in between each cutover
  - Cleaning up unused resources once you're done

## Additional resources

AWS Prescriptive Guidance has the following resources that can help you plan and
implement a large migration. Use this guide to understand how DataSync can work in the
context of common migration processes and activities.

- [Large migrations to the AWS cloud](https://aws.amazon.com/prescriptive-guidance/large-migrations/?large-migration-strategies.sort-by=item.additionalFields.sortText&large-migration-strategies.sort-order=desc&large-migration-playbooks.sort-by=item.additionalFields.sortText&large-migration-playbooks.sort-order=desc&large-migration-patterns.sort-by=item.additionalFields.sortText&large-migration-patterns.sort-order=desc "https://aws.amazon.com/prescriptive-guidance/large-migrations/?large-migration-strategies.sort-by=item.additionalFields.sortText&large-migration-strategies.sort-order=desc&large-migration-playbooks.sort-by=item.additionalFields.sortText&large-migration-playbooks.sort-order=desc&large-migration-patterns.sort-by=item.additionalFields.sortText&large-migration-patterns.sort-order=desc")
- [Strategy and best practices for AWS large migrations](../../../prescriptive-guidance/latest/strategy-large-scale-migrations/welcome.md "../../../prescriptive-guidance/latest/strategy-large-scale-migrations/welcome.md")
- [Migrate shared file systems in an AWS large migration](../../../prescriptive-guidance/latest/patterns/migrate-shared-file-systems-in-an-aws-large-migration.md "../../../prescriptive-guidance/latest/patterns/migrate-shared-file-systems-in-an-aws-large-migration.md") – This
  resource includes an **SFS-Discovery-Workbook**
  that you can download and use to plan a migration at the file share
  level.
