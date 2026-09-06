

# AWS Schema Conversion Tool
<a name="chap-oracle-aurora-mysql.tools.awssct"></a>

The AWS Schema Conversion Tool (AWS SCT) is a Java utility that connects to source and target databases, scans the source database schema objects (tables, views, indexes, procedures, and so on), and converts them to target database objects.

This section provides a step-by-step process for using AWS SCT to migrate an Oracle database to an Aurora MySQL database cluster. Since AWS SCT can automatically migrate most of the database objects, it greatly reduces manual effort.

We recommend to start every migration with the process outlined in this section and then use the rest of the Playbook to further explore manual solutions for objects that couldn’t be migrated automatically. For more information, see the AWS Schema Conversion Tool [User Guide](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/Welcome.html).

**Note**  
This walkthrough uses the AWS Database Migration Service Sample Database. You can download it from [GitHub](https://github.com/aws-samples/aws-database-migration-samples).

## Download the software and drivers
<a name="chap-oracle-aurora-mysql.tools.awssct.download"></a>

Download and install AWS SCT. For more information, see [Installing, verifying, and updating](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html) in the AWS Schema Conversion Tool User Guide.

Download the [Oracle](http://www.oracle.com/technetwork/database/features/jdbc/jdbc-drivers-12c-download-1958347.html) and [MySQL](https://dev.mysql.com/downloads/connector/j/) drivers. For more information, see [Installing the required database drivers](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html#CHAP_Installing.JDBCDrivers).

## Configure AWS SCT
<a name="chap-oracle-aurora-mysql.tools.awssct.configure"></a>

Follow this procedure for configuring `AWSSCT` to streamline your database migration process.

1. Start AWS Schema Conversion Tool (AWS SCT).

1. Choose **Settings** and then choose **Global settings**.

1. On the left navigation bar, choose **Drivers**.

1. Enter the paths for the Oracle and MySQL drivers downloaded in the first step.

    ![Enter the paths for the Oracle and MySQL drivers](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-oracle-aurora-mysql-configure-aws-sct.png) 

1. Choose **Apply** and then **OK**.

## Create a new migration project
<a name="chap-oracle-aurora-mysql.tools.awssct.newproject"></a>

Create a new migration project to define the source and target databases, configure migration settings, and launch the replication process.

1. In AWS SCT, choose **File**, and then choose **New project wizard**. Alternatively, use the keyboard shortcut **Ctrl\+W**.

1. Enter a project name and select a location for the project files. For **Source engine**, choose **Oracle**, and then choose **Next**.

1. Enter connection details for the source Oracle database and choose **Test connection** to verify. Choose **Next**.

1. Select the schema or database to migrate and choose **Next**.

1. The progress bar displays the objects that AWS SCT analyzes. When AWS SCT completes the analysis, the application displays the database migration assessment report. Read the Executive summary and other sections. Note that the information on the screen is only partial. To read the full report, including details of the individual issues, choose **Save to PDF** at the top right and open the PDF document.

    ![Assessment report](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-oracle-aurora-mysql-aws-sct-assessment-report.png) 

1. Scroll down to the **Database objects with conversion actions for Amazon Aurora (MySQL compatible)** section.

    ![Assessment report conversion statistics](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-oracle-aurora-mysql-aws-sct-assessment-report-conversion-statistics.png) 

1. Scroll further down to the **Detailed recommendations for Amazon Aurora (MySQL compatible) migrations** section and review the migration recommendations.

1. Return to AWS SCT and choose **Next**. Enter the connection details for the target Aurora MySQL database and choose **Finish**.

1. When the connection is complete, AWS SCT displays the main window. In this interface, you can explore the individual issues and recommendations discovered by AWS SCT.

1. Choose the schema, open the context (right-click) menu, and then choose **Create report** to create a report tailored for the target database type. You can view this report in AWS SCT.

1. The progress bar updates while the report is generated.

1.  AWS SCT displays the executive summary page of the database migration assessment report.

1. Choose **Action items**. In this window, you can investigate each issue in detail and view the suggested course of action. For each issue, drill down to view all instances of that issue.

1. Choose the database name, open the context (right-click) menu, and choose **Convert schema**. Make sure that you uncheck the `sys` and `information_schema` system schemas. This step doesn’t make any changes to the target database.

1. On the right pane, AWS SCT displays the new virtual schema as if it exists in the target database. Drilling down into individual objects displays the actual syntax generated by AWS SCT to migrate the objects.

1. Choose the database on the right pane, open the context (right-click) menu, and choose either **Apply to database** to automatically run the conversion script against the target database, or choose **Save as SQL** to save to an SQL file.

1. We recommend saving to an SQL file because you can verify and QA the converted code. Also, you can make the adjustments needed for objects that couldn’t be automatically converted.

For more information, see the AWS Schema Conversion Tool [User Guide](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/Welcome.html).