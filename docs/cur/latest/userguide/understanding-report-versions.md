# Understanding your report versions

AWS updates your Cost and Usage Report at least once a day until your charges are finalized.
When you create a report, you can choose to create new report versions or overwrite the
existing report version with every update.

Your report files include a .csv file or a collection of .csv files and the manifest file.
Your report can also include any additional files that support your data’s integration with
Amazon Athena, Amazon Redshift, or Quick Suite.

The following sections describe the file organization and naming conventions based on the
report versioning that you choose.

## Cost and Usage Reports delivery timeline

During the report period, AWS delivers a new report and a new manifest file each time
AWS updates the report. AWS builds on previous reports until the end of the billing
period. After the end of the report billing period, AWS generates a new report with none
of the information from the previous report.

## Creating new Cost and Usage Report versions

When you choose to keep your previous Cost and Usage Reports, your AWS CUR uses the following Amazon S3
organization and naming conventions.

```
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<assemblyId>/<`example-report-name`>-<file-number>.csv.<zip|gz>
```

- `report-prefix` = The prefix that you assign to the report.
- `report-name` = The name that you assign to the report.
- `yyyymmdd-yyyymmdd` = The range of dates that the report covers. Reports
  are finalized at the end of the date range.
- `assemblyId` = An ID that AWS creates each time that the report is
  updated.
- `file-number` = If the update includes a large file, AWS might split it
  into multiple files. The `file-number` tracks the different files in an
  update.
- `csv` = The format of the report files.
- `zip` or `gz` = The type of compression applied to the report
  files.

For example, your report could be delivered as a collection of the following
files.

```
<`example-report-prefix`>/<`example-report-name`>/20160101-20160131/<123456789>/<`example-report-name`>-<1>.csv.<zip>
<`example-report-prefix`>/<`example-report-name`>/20160101-20160131/<123456789>/<`example-report-name`>-<2>.csv.<zip>
<`example-report-prefix`>/<`example-report-name`>/20160101-20160131/<123456789>/<`example-report-name`>-<3>.csv.<zip>
<example-report-prefix>/<example-report-name>/20160101-20160131/<123456789>/<example-report-name>-Manifest.json
<example-report-prefix>/<example-report-name>/20160101-20160131/<example-report-name>-Manifest.json

```

AWS delivers all reports in a report date range to the same
`report-prefix/report-name/yyyymmdd-yyyymmdd` folder. AWS gives each report a
unique ID and delivers it to the `assemblyId` subfolder in the date range folder.
If the report is too large for a single file, the report is split into multiple files and
delivered to the same `assemblyId` folder.

For more information on manifesting files when you keep a previous report, see [Cost and Usage Reports manifest files](#manifest-cur-files "#manifest-cur-files")

## Overwriting previous Cost and Usage Reports

When you choose to overwrite your previous Cost and Usage Reports, your AWS CUR uses the following
Amazon S3 organization and naming conventions.

```
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>-<file-number>.csv.<zip|gz>
```

- `report-prefix` = The prefix that you assign to the report.
- `report-name` = The name that you assign to the report.
- `yyyymmdd-yyyymmdd` = The range of dates that the report covers. AWS
  finalizes reports at the end of the date range.
-
- `file-number` = If the update includes a large file, AWS might split it
  into multiple files. The `file-number` tracks the different files in an
  update.
- `csv` = The format of the report files.
- `zip` or `gz` = The type of compression applied to the report
  files.

For example, your report could be delivered as a collection of the following
files.

```
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>-<1>.csv.<zip>
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>-<2>.csv.<zip><`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>-<3>.csv.<zip>
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>-Manifest.json
```

### Athena specifications

If you chose Athena support when you created your AWS CUR, the file naming conventions
are the same as when you choose to overwrite your AWS CUR except for the format and
compression. Athena AWS CUR files use `.parquet` instead. For example, your report
could be delivered as a collection of the following files.

```
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>.parquet
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<cost_and_usage_data_status>
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>-Manifest.json
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>-create-table.sql
<`example-report-prefix`>/<`example-report-name`>/yyyymmdd-yyyymmdd/crawler-cfn.yml
```

### CloudFormation specifications

In addition to the AWS CUR files, AWS also delivers an CloudFormation template that you can use
to set up an CloudFormation stack that enables you to query Amazon S3 data using Athena. If you don't
want to use the CloudFormation template, you can use the provided SQL to create your own Athena
tables. For more information, see [Querying Cost and Usage Reports using Amazon Athena](cur-query-athena.md "cur-query-athena.md").

## Cost and Usage Reports manifest files

When AWS updates AWS CUR, AWS also creates and delivers manifest files that you can
use for Amazon Athena, Amazon Redshift, or Quick Suite.

Manifest files use the naming conventions, and lists the following:

- All of the detail columns that are included in the report to date
- A list of report files if the report was split into multiple files
- The time period covered by the report, and other information.

```
<example-report-prefix>/<example-report-name>/yyyymmdd-yyyymmdd/<example-report-name>-Manifest.json
<example-report-prefix>/<example-report-name>/yyyymmdd-yyyymmdd/<assemblyId>/<example-report-name>-Manifest.json
<example-report-prefix>/<example-report-name>/<example-report-name>/year=2018/month=12/<example-report-name>-Manifest.json
```

### Creating new Cost and Usage Report versions

When you keep the previous Cost and Usage Reports, the manifest file is delivered to both the
date range folder and the `assemblyId` folder. Each time AWS creates a new
AWS CUR for a date range, it overwrites the manifest file stored in the date range folder
with an updated manifest file. AWS delivers the same updated manifest file to the
`assemblyId` folder along with the files for that update. Manifest files in
the `assemblyId` folder aren't overwritten.

### Overwriting the previous Cost and Usage Reports

When you overwrite the previous AWS CUR, the manifest file is delivered to the
`month=mm` folder. The manifest file is overwritten along with the report
files.

### Amazon Redshift specifications

If you chose the option for Amazon Redshift support in your AWS CUR, AWS also creates and
delivers a file with the SQL commands that you need to upload your report into Amazon Redshift. You
can open the SQL file with a regular text editor. The SQL file uses the following naming
convention.

```

<example-report-prefix>/<example-report-name>/yyyymmdd-yyyymmdd/<assemblyId>/<example-report-name>-RedshiftCommands.sql
```

If you use the commands in the `RedshiftCommands` file, you don't need to
open the `RedshiftManifest` file.

###### Important

The `manifest` file determines which report files the `copy`
command in the `RedshiftCommands` file uploads. Deleting or removing the
`manifest` file breaks the copy command in the
`RedshiftCommands` file.

### Amazon Athena specifications

If you chose the option for Amazon Athena support in your AWS CUR, AWS also creates and
delivers multiple files to help set up all of the resources that you need. AWS delivers
a CloudFormation template, a SQL file with the SQL to create your Athena table manually, and a file
with the SQL to check your AWS CUR refresh status. These files use the following naming
conventions.

```
<`example-report-prefix`>/<`example-report-name`>/<`example-report-name`>/yyyymmdd-yyyymmdd/crawler-cfn.yml
<`example-report-prefix`>/<`example-report-name`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<`example-report-name`>-create-table.sql
<`example-report-prefix`>/<`example-report-name`>/<`example-report-name`>/yyyymmdd-yyyymmdd/<cost_and_usage_data_status>
```
