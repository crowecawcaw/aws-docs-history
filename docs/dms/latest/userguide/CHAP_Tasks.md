# Starting and viewing data type

assessments (Legacy)

###### Note

This section describes legacy content. We recommend that you use premigration assessment
runs, described prior in [Specifying, starting, and viewing
premigration assessment runs](CHAP_Tasks.md "CHAP_Tasks.md").

Data type assessments are not available in the console. You can only run data type assessments
using the API or CLI, and you can only view the results of a data type assessment in the task's S3 bucket.

The Pre-migration Assessment will automatically run under these conditions:

- During Start Task: If you haven't manually run the assessment during task creation.
- During Resume Task: If no completed assessment exists within the past 7 days.
  A data type assessment identifies data types in a source database that might not
  get migrated correctly because the target doesn't support them. During this assessment, AWS DMS reads the source database
  schemas for a migration task and creates a list of the column data types. It then
  compares this list to a predefined list of data types supported by AWS DMS. If your
  migration task has unsupported data types, AWS DMS
  creates a report that you can look at to see if your migration task has any
  unsupported data types. AWS DMS doesn't create a report if your migration task doesn't have any
  unsupported data types.

AWS DMS supports creating data type assessment reports for the following relational
databases:

- Oracle
- SQL Server
- PostgreSQL
- MySQL
- MariaDB
- Amazon Aurora
  You can start and view a data type assessment report using the CLI and SDKs to
  access the AWS DMS API:

- The CLI uses the [`start-replication-task-assessment`](../../../cli/latest/reference/dms/start-replication-task-assessment.md "../../../cli/latest/reference/dms/start-replication-task-assessment.md") command to start
  a data type assessment and uses the [`describe-replication-task-assessment-results`](../../../cli/latest/reference/dms/describe-replication-task-assessment-results.md "../../../cli/latest/reference/dms/describe-replication-task-assessment-results.md")
  command to view the latest data type assessment report in JSON
  format.
- The AWS DMS API uses the [`StartReplicationTaskAssessment`](../APIReference/API_StartReplicationTaskAssessment.md "../APIReference/API_StartReplicationTaskAssessment.md")
  operation to start a data type assessment and uses the [`DescribeReplicationTaskAssessmentResults`](../APIReference/API_DescribeReplicationTaskAssessmentResults.md "../APIReference/API_DescribeReplicationTaskAssessmentResults.md")
  operation to view the latest data type assessment report in JSON
  format.
  The data type assessment report is a single JSON file that includes a summary that
  lists the unsupported data types and the column count for each one. It includes a
  list of data structures for each unsupported data type including the schemas,
  tables, and columns that have the unsupported data type. You can use the report to
  modify the source data types and improve the migration success.

There are two levels of unsupported data types. Data types that appear on the
report as not supported can't be migrated. Data types that appear on the report
as partially supported might be converted to another data type, but not migrate as
you expect.

The following example shows a sample data type assessment report that you might
view.

```
{
    "summary":{
        "task-name":"test15",
        "not-supported":{
            "data-type": [
                "sql-variant"
            ],
            "column-count":3
        },
        "partially-supported":{
            "data-type":[
                "float8",
                "jsonb"
            ],
            "column-count":2
        }
    },
    "types":[
        {
            "data-type":"float8",
            "support-level":"partially-supported",
            "schemas":[
                {
                    "schema-name":"schema1",
                    "tables":[
                        {
                            "table-name":"table1",
                            "columns":[
                                "column1",
                                "column2"
                            ]
                        },
                        {
                            "table-name":"table2",
                            "columns":[
                                "column3",
                                "column4"
                            ]
                        }
                    ]
                },
                {
                    "schema-name":"schema2",
                    "tables":[
                        {
                            "table-name":"table3",
                            "columns":[
                                "column5",
                                "column6"
                            ]
                        },
                        {
                            "table-name":"table4",
                            "columns":[
                                "column7",
                                "column8"
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "datatype":"int8",
            "support-level":"partially-supported",
            "schemas":[
                {
                    "schema-name":"schema1",
                    "tables":[
                        {
                            "table-name":"table1",
                            "columns":[
                                "column9",
                                "column10"
                            ]
                        },
                        {
                            "table-name":"table2",
                            "columns":[
                                "column11",
                                "column12"
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

```

AWS DMS stores the latest and all previous data type assessments in an Amazon S3
bucket created by AWS DMS in your account. The Amazon S3 bucket name has the following
format, where `customerId` is your customer ID and
`customerDNS` is an internal identifier.

```
dms-`customerId`-`customerDNS`
```

###### Note

By default, you can create up to 100 Amazon S3 buckets in each of your AWS
accounts. Because AWS DMS creates a bucket in your account, make sure that it
doesn't exceed your bucket limit. Otherwise, the data type assessment
fails.

All data type assessment reports for a given migration task are stored in a bucket
folder named with the task identifier. Each report's file name is the date of
the data type assessment in the format yyyy-mm-dd-hh-mm. You can view and compare
previous data type assessment reports from the Amazon S3 Management Console.

AWS DMS also creates an AWS Identity and Access Management (IAM) role to allow access to the S3 bucket
created for these reports. The role name is `dms-access-for-tasks`. The
role uses the `AmazonDMSRedshiftS3Role` policy. If a **ResourceNotFoundFault**
error occurs when you run `StartReplicationTaskAssessment`, see
[ResourceNotFoundFault](CHAP_Tasks.AssessmentReport.md#CHAP_Tasks.AssessmentReport.Troubleshooting.ResourceNotFoundFault "CHAP_Tasks.AssessmentReport.md#CHAP_Tasks.AssessmentReport.Troubleshooting.ResourceNotFoundFault") in the Troubleshooting section
for information about creating the `dms-access-for-tasks`
role manually.
