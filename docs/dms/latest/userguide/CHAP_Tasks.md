# Enabling and working with premigration

assessments for a task

A premigration assessment evaluates specified components of a database migration task
to help identify any problems that might prevent a migration task from running as
expected. This assessment gives you a chance to identify and fix issues before you run a new or
modified task. This allows you to avoid delays related to task failures caused by missing requirements
or known limitations.

AWS DMS provides access to two different options for premigration assessments:

- **Data type assessment**: A legacy report that provides
  a limited scope of assessments.
- **Premigration assessment run**: Contains various types
  of individual assessments, including data type assessment results.

###### Note

If you choose a premigration assessment run,
you don't need to choose a data type assessment separately.

These options are described in the following
topics:

- [Specifying, starting, and viewing
  premigration assessment runs](CHAP_Tasks.md "CHAP_Tasks.md"): A premigration (recommended)
  assessment run specifies one or more individual assessments to run based on a
  new or existing migration task configuration. Each individual assessment
  evaluates a specific element of a supported source and/or target database
  from the perspective of criteria such as the migration type, supported objects, index
  configuration, and other task settings, such as table mappings that identify the
  schemas and tables to migrate.

For example, an individual assessment might evaluate what source data types or
primary key formats can or can't be migrated, possibly based on the AWS DMS
engine version. You can start and view the results of the latest assessment run
and view the results of all prior assessment runs for a task either using the
AWS DMS Management Console or using the AWS CLI and SDKs to access the AWS DMS API.
You can also view the results of prior assessment runs for a task in an Amazon S3
bucket that you have selected for AWS DMS to store these results.

###### Note

The number and types of available individual assessments can increase over
time. For more information about periodic updates, see [Specifying individual
assessments](CHAP_Tasks.md#CHAP_Tasks.PremigrationAssessmentRuns.Individual "CHAP_Tasks.md#CHAP_Tasks.PremigrationAssessmentRuns.Individual").

- [Starting and viewing data type
  assessments (Legacy)](CHAP_Tasks.md "CHAP_Tasks.md"): A data type (legacy)
  assessment returns the results of a single type of premigration assessment in a
  single JSON structure: the data types that might not be migrated correctly in a
  supported relational source database instance. This report returns the results
  for all problematic data types found in every schema and table in the
  source database that is selected for migration.
