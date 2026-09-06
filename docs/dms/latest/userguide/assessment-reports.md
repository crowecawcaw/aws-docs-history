

# Conversion assessment reports with DMS Schema Conversion
<a name="assessment-reports"></a>

An important part of DMS Schema Conversion is the report that it generates to help you convert your schema. This *conversion assessment report* analyzes the database objects in your source schema and identifies which objects DMS Schema Conversion can convert automatically and which objects require manual action. You can view the report in the AWS DMS console or save a copy as a PDF or comma-separated value (CSV) files.

The conversion assessment report includes the following:
+ An executive summary
+ Recommendations for converting database objects that require manual action

When you have database objects that DMS Schema Conversion cannot convert automatically, the report provides estimates showing how much effort is required to write the equivalent code for your target DB instance.

**Topics**
+ [Running an assessment for a conversion assessment report with DMS Schema Conversion](#assessment-reports-create)
+ [Saving your conversion assessment report for DMS Schema Conversion](#assessment-reports-save)
+ [Viewing your conversion assessment report for DMS Schema Conversion](#assessment-reports-view)
+ [Understanding conversion assessment report metrics](assessment-reports-understanding.md)
+ [Using the conversion assessment report for migration planning](assessment-reports-planning.md)

## Running an assessment for a conversion assessment report with DMS Schema Conversion
<a name="assessment-reports-create"></a>

After you create a migration project, use one of the following methods to run an assessment of the conversion complexity.

------
#### [ AWS Management Console ]

**To run an assessment and generate a conversion assessment report**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. Choose **Migration projects**. The **Migration projects** page opens.

1. Choose your migration project, and then choose **Schema conversion**.

1. Choose **Launch schema conversion**. The **Schema conversion** page opens.

1. In the source database pane, select the node that you want to assess. The **Assess** action is available on the **Databases** node, on individual database nodes, and on schema nodes such as **dbo**. It is not available on individual object nodes such as tables or procedures.

1. Select at least one parent node in the source database pane. The **Actions** menu becomes available only when a parent node is selected.

1. Open the **Actions** menu and choose **Assess**. A confirmation dialog box appears.

1. Choose **Assess** in the dialog box to confirm your choice.

------
#### [ AWS CLI ]

The following example uses [start-metadata-model-assessment](https://docs.aws.amazon.com/cli/latest/reference/dms/start-metadata-model-assessment.html) to queue an assessment of the conversion complexity for all objects in the {{ExampleSchema}} schema.

```
aws dms start-metadata-model-assessment \
        --migration-project-identifier "{{arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}}" \
        --selection-rules '{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "{{source-server}}", "schema-name": "{{ExampleSchema}}"}, "rule-action": "explicit"}]}'
```

**Note**  
The `--selection-rules` parameter takes a JSON string that specifies which database objects to include in the assessment. For the full selection rules JSON structure, see [Selection rules in DMS Schema Conversion](sc-selection-rules.md).

The response contains a `RequestIdentifier` that identifies the assessment request.

```
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

Because an assessment runs asynchronously, use [aws dms wait metadata-model-assessed](https://docs.aws.amazon.com/cli/latest/reference/dms/wait/metadata-model-assessed.html) to block until the assessment completes before proceeding.

```
aws dms wait metadata-model-assessed \
        --migration-project-identifier "{{arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}}"
```

The command polls every 30 seconds and returns when the assessment reaches a terminal state. It exits with return code 255 if the assessment does not complete after 360 checks (approximately 3 hours).

Starting an assessment does not generate an entirely new report from scratch each time. The conversion assessment report reflects the current state of your migration project, so it includes the action items and generative AI candidates for whatever you have assessed or converted so far. For more information, see [Understanding conversion assessment report metrics](assessment-reports-understanding.md).

------

## Saving your conversion assessment report for DMS Schema Conversion
<a name="assessment-reports-save"></a>

After you run an assessment or a conversion, you can save a copy of the conversion assessment report as a PDF or comma-separated value (CSV) files.

------
#### [ AWS Management Console ]

**To save a conversion assessment report as a PDF file**

1. Choose **Export**, then choose **PDF**. Review the dialog box, and choose **Export to PDF**. 

1. DMS Schema Conversion stores the PDF file in the Amazon S3 bucket that you configured under **S3 bucket access settings** in your migration project.

1. Open the assessment report file in your Amazon S3 bucket.

**To save a conversion assessment report as CSV files**

1. Choose **Export**, then choose **CSV**. Review the dialog box, and choose **Export to CSV**. 

1. DMS Schema Conversion stores a ZIP archive containing the CSV files in the Amazon S3 bucket that you configured under **S3 bucket access settings** in your migration project.

1. Download and extract the ZIP archive from your Amazon S3 bucket to access the CSV files.

The Amazon S3 bucket where DMS Schema Conversion stores exported reports is the bucket that you specified under **S3 bucket access settings** when you created your migration project.

Files are stored under a folder matching your migration project name. When exporting from the AWS Management Console, files are named using the source engine, target engine, and a UTC timestamp: `{{project-name}}/{{SOURCE_ENGINE}}_{{TARGET_ENGINE}}_{{YYYY-MM-DD}}T{{HH-MM-SS.sssZ}}` — for example, `ora-pg-demo/ORACLE_POSTGRESQL_2026-07-01T09-00-47.846Z.pdf`.

The CSV archive contains at least three files organized under a two-level directory path. The top-level directory is the **source server name** exactly as configured in the source data provider (hostname or IP address). The subdirectory and file names use the **target database hostname**:
+ `{{source-server}}/{{target-host}}/{{target-host}}.csv` — one row per action item occurrence.
+ `{{source-server}}/{{target-host}}/{{target-host}}_Action_Items_Summary.csv` — one row per action item type, with effort values.
+ `{{source-server}}/{{target-host}}/{{target-host}}_Summary.csv` — one row per object type, with complexity counts.
+ `{{source-server}}/{{target-host}}/{{target-host}}_Stub_Objects.csv` — one row per stub object generated for an unsupported built-in. This file is present only when **Convert unsupported built-in objects to stub objects** is enabled in your migration project settings.

------
#### [ AWS CLI ]

The following example uses [export-metadata-model-assessment](https://docs.aws.amazon.com/cli/latest/reference/dms/export-metadata-model-assessment.html) to export the conversion assessment report for a migration project as both a PDF file and a CSV archive to your Amazon S3 bucket.

```
aws dms export-metadata-model-assessment \
        --migration-project-identifier "{{arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}}" \
        --selection-rules '{"rules":[{"rule-type":"selection","rule-id":"1","rule-name":"1","rule-action":"explicit","object-locator":{"server-name":"{{source-server}}","schema-name":"{{ExampleSchema}}"}}]}' \
        --assessment-report-types pdf csv
```

**Note**  
The `--selection-rules` parameter takes a JSON string that specifies which database objects to include in the report. For the full selection rules JSON structure, see [Selection rules in DMS Schema Conversion](sc-selection-rules.md).

The response contains the Amazon S3 object key and download URL for each report file.

When you do not specify `--file-name`, files are stored under a folder matching your migration project name, using a timestamp as the file name: `{{project-name}}/{{YYYY-MM-DD-HH-MM-SS}}.pdf` and `{{project-name}}/{{YYYY-MM-DD-HH-MM-SS}}.zip` — for example, `sqlserver-pg-pma/2026-07-15-10-08-12.zip`. Specify `--file-name` to override the timestamp prefix within that folder.

```
{
    "PdfReport": {
        "S3ObjectKey": "{{project-name}}/{{YYYY-MM-DD-HH-MM-SS}}.pdf",
        "ObjectURL": "https://amzn-s3-demo-bucket.s3.amazonaws.com/{{project-name}}/{{YYYY-MM-DD-HH-MM-SS}}.pdf"
    },
    "CsvReport": {
        "S3ObjectKey": "{{project-name}}/{{YYYY-MM-DD-HH-MM-SS}}.zip",
        "ObjectURL": "https://amzn-s3-demo-bucket.s3.amazonaws.com/{{project-name}}/{{YYYY-MM-DD-HH-MM-SS}}.zip"
    }
}
```

------

**Note**  
The conversion assessment report is also available after you run a conversion operation, not only after running an explicit assessment. After a conversion, the report reflects the objects that still require manual action and marks the objects that DMS Schema Conversion converted using generative AI. For information about running a conversion, see [Converting your database schema: step-by-step guide](schema-conversion-convert.md).

## Viewing your conversion assessment report for DMS Schema Conversion
<a name="assessment-reports-view"></a>

To view your conversion assessment report, use one of the following methods.

**Important**  
The conversion assessment report covers only the database objects that were included in the scope of the most recent assessment or conversion operation. Objects that were not selected when you ran **Assess** or **Convert** do not appear in the report, even if they exist in your source database.  
Each new assessment or conversion operation overwrites the previous report. The **Summary** and **Action items** tabs always reflect only the most recent operation. If you need to keep the results of the current report, export it as a PDF or CSV file before running a new assessment or conversion. For export instructions, see [Saving assessment reports](#assessment-reports-save).

------
#### [ AWS Management Console ]

After you run an assessment or a conversion, DMS Schema Conversion adds information in the following tabs:
+ **Summary**
+ **Action items**

The **Summary** tab displays the summary information from the conversion assessment report. It shows the number of database objects that DMS Schema Conversion can automatically convert for database storage objects and database code objects.

DMS Schema Conversion converts many database objects automatically and identifies those that require manual action to complete the conversion to the target database engine. The **Summary** tab provides an estimate of the required effort to create database objects in your target DB instance that are equivalent to those in your source.

To see the conversion summary for database storage objects such as tables, sequences, constraints, data types, and so on, choose **Database storage objects**.

To see the conversion summary for database code objects such as procedures, functions, views, triggers, and so on, choose **Database code objects**.

To change the scope of the assessment report, select the required node in the source database tree. DMS Schema Conversion updates the assessment report summary to match the selected scope.

The **Action items** tab contains a list of action items for database objects that DMS Schema Conversion cannot automatically convert to a format compatible with the target database engine. For each action item, DMS Schema Conversion provides the description of the issue and the recommended action. DMS Schema Conversion groups similar action items and displays the number of occurrences.

To view the code for the related database object, select an action item in the list.

DMS Schema Conversion with generative AI streamlines the database migration process by offering recommendations to help you convert previously unconverted code objects that typically require complex manual conversion. Currently, this feature is available for Oracle, SQL Server, SAP ASE (Sybase ASE), IBM Db2 for LUW, and IBM Db2 for z/OS as source databases, converting to PostgreSQL or Aurora PostgreSQL.

The assessment report shows which database code objects are candidates for conversion using generative AI. You can export this report to a PDF for a short list of five objects per action item. You can export the report to a CSV file to see the full list of candidates.

When you enable **Convert schema using generative AI** and perform a conversion, the updated assessment report marks each database object with a corresponding action item — both objects that were successfully converted using generative AI and objects that generative AI could not convert, making it easy to identify and track the results of AI-assisted conversion.

To quickly locate objects that are converted by generative AI:

1. Navigate to the **Action Items** tab.

1. In the top-right corner, locate the drop-down menu.

1. Select **Generated by AI** from the options.

This filtering method allows you to efficiently view all database objects that were successfully converted using this feature. For more information about converting database objects with generative AI, see [Scope of Generative AI conversion](schema-conversion-convert.databaseobjects.md#schema-conversion-convert.databaseobjects.genai).

------
#### [ PDF report ]

The PDF report contains the following four chapters, in this order:
+ **Executive summary** — An overview of the migration complexity. Shows the number of database objects that DMS Schema Conversion can convert automatically and the number that require manual action, broken down by object type (tables, views, procedures, triggers, and so on) and by complexity category (automatically converted, simple actions, medium-complexity actions, and complex actions). For more information about these categories, see [Complexity categories](assessment-reports-understanding.md#assessment-reports-understanding-complexity).
+ **Database objects with conversion actions** — A breakdown of which specific database objects require manual action, organized by object type. Each entry identifies the object by name and lists its action item code.
+ **Candidates for conversion with generative AI** — The database objects that DMS Schema Conversion identifies as candidates for automated conversion using generative AI. The PDF lists up to five candidate objects per action item type. To see the complete list of candidates, export the report as CSV.
+ **Detailed recommendations for migrations** — A per-object analysis of every database object that requires manual action. For each object, this chapter shows the action item code (see [Action item codes](assessment-reports-understanding.md#assessment-reports-understanding-codes)), a description of the specific incompatibility with the target database engine, and the recommended manual conversion action. Unlike the **Action items** tab in the AWS Management Console, which groups action items by type across all objects, this chapter lists each affected object individually.

To export the report as a PDF, see [Saving assessment reports](#assessment-reports-save).

------
#### [ CSV report ]

When you export your assessment report to CSV, DMS Schema Conversion creates an archive containing at least three CSV files. The archive uses a two-level directory structure: the top-level directory is the **source server name** exactly as configured in your source data provider (hostname or IP address), and the subdirectory and file names use the **target database hostname**.{{}}

The main CSV file (no suffix) contains one row per action item occurrence. It contains the following columns:
+ **Category** — The type of database object that the action item applies to, such as `procedure` or `view-constraint`.
+ **Occurrence** — The fully qualified path to the specific database object instance that the action item affects, such as `Schemas.{{schema_name}}.Procedures.{{procedure_name}}`.
+ **Action item** — The numeric action item code that identifies the type of conversion issue. For more information, see [Action item codes](assessment-reports-understanding.md#assessment-reports-understanding-codes).
+ **Subject** — The specific database object name or code element that the action item refers to, such as an unresolved identifier. This field is empty when the action item does not reference a specific object name.
+ **Group** — A generic description of the issue type shared by every occurrence of that action item code. DMS Schema Conversion uses this value to group related occurrences together.
+ **Description** — A detailed description of the specific incompatibility for this occurrence.
+ **Documentation references** — Links to relevant documentation for resolving the incompatibility.
+ **Recommended action** — The suggested manual conversion step to resolve the incompatibility.
+ **Filtered** — Indicates whether the action item was filtered out of the report view.
+ **Estimated complexity** — The complexity category assigned to this occurrence: automatically converted, simple actions, medium-complexity actions, or complex actions.
+ **Line** — The line number in the source object's code where the incompatibility occurs.
+ **Position** — The character position on the line where the incompatibility occurs.
+ **Source** — The source database engine.
+ **Target** — The target database engine.
+ **Server IP address and port** — The host and port of the source database server.
+ **Database name** — The name of the source database.
+ **Schema name** — The name of the source schema containing the affected object.
+ **AI/ML Recommendation** — The generative AI recommendation for converting this object, when generative AI conversion was enabled and produced a result for this occurrence.{{}}

Contains one row per action item type with the following columns:
+ **Schema** — The name of the source schema containing the affected objects.
+ **Action item** — The numeric action item code that identifies the type of conversion issue. For more information, see [Action item codes](assessment-reports-understanding.md#assessment-reports-understanding-codes).
+ **Number of occurrences** — The total number of database objects affected by this action item type.
+ **Learning curve efforts** — The one-time effort required to design a conversion approach for this action item type. You incur this cost once per action item type regardless of the number of occurrences. Values use a weighted scale ranging from low (least effort) to high (most effort).
+ **Efforts to convert an occurrence** — The effort required to resolve each individual occurrence of this action item type, following the designed conversion approach. Values use the same weighted scale as learning curve efforts.
+ **Action item description** — A description of the incompatibility that this action item type represents.
+ **Recommended action** — The suggested manual conversion step to resolve this action item type.{{}}

Contains one row per database object type with the following columns:
+ **Category** — The database object type that the row summarizes, such as `TABLE`, `VIEW`, `PROCEDURE`, `TRIGGER`, `INDEX`, `CONSTRAINT`, `SEQUENCE`, or `FUNCTION`. The file also includes aggregate metric rows with a `Category` value of `Storage_objects_count`, `Code_objects_count`, or `SQL_syntax_elements_number`. For more information about these aggregate values, see [Conversion statistics and SQL metrics](assessment-reports-understanding.md#assessment-reports-understanding-statistics).
+ **Number of objects** — The total number of database objects of this type in the assessed scope.
+ **Objects automatically converted** — The number of objects that DMS Schema Conversion can convert without any manual action.
+ **Objects with simple actions** — The number of objects that require a small amount of manual effort to convert.
+ **Objects with medium-complexity actions** — The number of objects that require a moderate amount of manual effort to convert.
+ **Objects with complex actions** — The number of objects that require significant manual effort to convert.
+ **Total lines of code** — The total number of lines of source code across all objects of this type.

To export the report as CSV, see [Saving assessment reports](#assessment-reports-save).{{}}

This file is present only when **Convert unsupported built-in objects to stub objects** is enabled in your migration project settings. It contains one row per stub object generated for an unsupported built-in, with the following columns:
+ **Category** — The type of the stub object, such as `scalar-function`.
+ **Stub object name** — The fully qualified name of the generated stub, including schema and signature.
+ **Number of occurrences** — The number of times this stub object is referenced in the converted code.

------