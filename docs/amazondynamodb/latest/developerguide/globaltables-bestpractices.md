# Best practices for global tables

The following sections describe best practices for deploying and using global
tables.

## Version

There are two versions of DynamoDB global tables available: version 2019.11.21 (Current)
and [version 2017.11.29
(Legacy)](globaltables.md "globaltables.md"). You should use version 2019.11.21 (Current) whenever possible.

## Deletion

protection

You should enable deletion protection on global table replicas you want protected
against accidental deletion. You must enable deletion protection on each replica.

## Using AWS CloudFormation

AWS CloudFormation does not currently support the coordination of multi-Region resources like
global tables across stacks. If you define each replica of a global table in a separate
Regional stack, you will encounter errors due to detected drift across stacks when
performing replica updates. To avoid this issue, you should choose one Region as the
reference Region for deploying your global tables and define all of your global table's
replicas in that Region's stack.

###### Important

You cannot convert a resource of type `AWS::DynamoDB::Table` into a
resource of type `AWS::DynamoDB::GlobalTable` by changing its type in
your template. Attempting to convert a single-Region table to a global table by
changing its CloudFormation resource type may result in the deletion of your DynamoDB
table.

You can use the `AWS::DynamoDB::GlobalTable` resource to create a table in
a single Region. This table will be deployed like any other single-Region table. If you
later update the stack to add other Regions to a resource, replicas will be added to the
table and it will safely be converted to a global table.

If you have an existing `AWS::DynamoDB::Table` resource you want to convert
to a `AWS::DynamoDB::GlobalTable` resource, the recommended steps to convert
the resource type are:

1. Set the `AWS::DynamoDB::Table` deletion policy to retain.
2. Remove the table from the stack definition.
3. Add replicas to the single-Region table in the AWS console, converting it to
   a global table.
4. Import the new global table as a new `AWS::DynamoDB::GlobalTable`
   resource to the stack.

## Backups and Point-in-Time

Recovery

Enabling automated backups and Point-in-Time Recovery (PITR) for one replica in a
global table may be sufficient to meet your disaster recovery objectives. Replica
backups created with AWS-Backup can be automatically replicated across Regions for
greater resilience. Consider your disaster recovery plan goals in the context of
multi-Region high availability when choosing your backup and PITR enablement
strategy.

## Designing for multi-Region high

availability

For prescriptive guidance on deploying global tables, see [Best Practices for DynamoDB global table
design](bp-global-table-design.md "bp-global-table-design.md").
