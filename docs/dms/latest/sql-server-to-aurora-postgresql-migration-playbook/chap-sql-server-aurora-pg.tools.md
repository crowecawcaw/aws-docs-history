# AWS Schema Conversion Tool overview

You can use the AWS Schema Conversion Tool (AWS SCT) to streamline the migration of your Microsoft SQL Server 2019 database to Amazon Aurora PostgreSQL. This powerful Java utility automates the conversion of most database objects, significantly reducing manual effort in the migration process. By following the step-by-step instructions provided, you can connect to your source and target databases, analyze the schema objects, and generate a comprehensive migration assessment report. The tool offers valuable insights into potential conversion challenges and provides detailed recommendations for addressing them.

The AWS Schema Conversion Tool (AWS SCT) is a Java utility that connects to source and target databases, scans the source database schema objects (tables, views, indexes, procedures, and so on), and converts them to target database objects.

This section provides a step-by-step process for using AWS SCT to migrate an SQL Server database to an Aurora PostgreSQL database cluster. Since AWS SCT can automatically migrate most of the database objects, it greatly reduces manual effort.

We recommend to start every migration with the process outlined in this section and then use the rest of the Playbook to further explore manual solutions for objects that couldn’t be migrated automatically. For more information, see [Schema Conversion Tool user guide](../../../SchemaConversionTool/latest/userguide/Welcome.md "../../../SchemaConversionTool/latest/userguide/Welcome.md").

###### Note

This walkthrough uses the AWS DMS Sample Database. You can download it from [GitHub](https://github.com/aws-samples/aws-database-migration-samples "https://github.com/aws-samples/aws-database-migration-samples").

## Download the Software and Drivers

Download and install AWS SCT from the [Schema Conversion Tool user guide](../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md "../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md").

Download the [Microsoft SQL Server](https://docs.microsoft.com/en-us/sql/connect/jdbc/release-notes-for-the-jdbc-driver?view=sql-server-ver15#72 "https://docs.microsoft.com/en-us/sql/connect/jdbc/release-notes-for-the-jdbc-driver?view=sql-server-ver15#72") and [PostgreSQL](https://jdbc.postgresql.org/download "https://jdbc.postgresql.org/download") drivers.

Find other supported drivers in the [Schema Conversion Tool user guide](../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md#CHAP_Installing.JDBCDrivers "../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md#CHAP_Installing.JDBCDrivers").

## Configure AWS SCT

1. Start AWS Schema Conversion Tool (AWS SCT).
2. Choose **Settings** and then choose **Global settings**.
3. On the left navigation bar, choose **Drivers**.
4. Enter the paths for the SQL Server and PostgreSQL drivers downloaded in the first step.

![Enter the paths for the Microsoft and PostgreSQL drivers](images/pb-sql-server-aurora-pg-configure-aws-sct.png) 5. Choose **Apply** and then **OK**.

## Create a New Migration Project

1. Choose **File**, and then choose **New project wizard**. Alternatively, use the keyboard shortcut **Ctrl+W**.
2. Enter a project name and select a location for the project files. For **Source engine**, choose **Microsoft SQL Server**, and then choose **Next**.
3. Enter connection details for the source SQL Server database and choose **Test connection** to verify. Choose **Next**.
4. Select the schema or database to migrate and choose **Next**.

The progress bar displays the objects that AWS SCT analyzes. When AWS SCT completes the analysis, the application displays the database migration assessment report. Read the Executive summary and other sections. Note that the information on the screen is only partial. To read the full report, including details of the individual issues, choose **Save to PDF** at the top right and open the PDF document.

![Assessment report](images/pb-sql-server-aurora-pg-aws-sct-assessment-report.png)

Scroll down to the **Database objects with conversion actions for Amazon Aurora (PostgreSQL compatible)** section.

![Assessment report conversion statistics](images/pb-sql-server-aurora-pg-aws-sct-assessment-report-conversion-statistics.png)

Scroll further down to the **Detailed recommendations for Amazon Aurora (PostgreSQL compatible) migrations** section.

![Assessment report detailed recommendations](images/pb-sql-server-aurora-pg-aws-sct-assessment-report-detailed-recommendations.png)

Return to AWS SCT and choose **Next**. Enter the connection details for the target Aurora PostgreSQL database and choose **Finish**.

When the connection is complete, AWS SCT displays the main window. In this interface, you can explore the individual issues and recommendations discovered by AWS SCT.

Choose the schema, open the context (right-click) menu, and then choose **Create report** to create a report tailored for the target database type. You can view this report in AWS SCT.

The progress bar updates while the report is generated.

AWS SCT displays the executive summary page of the database migration assessment report.

Choose **Action items**. In this window, you can investigate each issue in detail and view the suggested course of action. For each issue, drill down to view all instances of that issue.

Choose the database name, open the context (right-click) menu, and choose **Convert schema**. Make sure that you uncheck the `sys` and `information_schema` system schemas. Aurora PostgreSQL already has an `information_schema` schema.

This step doesn’t make any changes to the target database.

On the right pane, AWS SCT displays the new virtual schema as if it exists in the target database. Drilling down into individual objects displays the actual syntax generated by AWS SCT to migrate the objects.

Choose the database on the right pane, open the context (right-click) menu, and choose either **Apply to database** to automatically run the conversion script against the target database, or choose **Save as SQL** to save to an SQL file.

![Apply to database](images/pb-sql-server-aurora-pg-aws-sct-apply-to-database.png)

We recommend saving to an SQL file because you can verify and QA the converted code. Also, you can make the adjustments needed for objects that couldn’t be automatically converted.

For more information, see the [Schema Conversion Tool user guide](../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md "../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md").
