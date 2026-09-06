

# AWS Schema Conversion Tool
<a name="chap-oracle-aurora-pg.tools.awssct"></a>

The AWS Schema Conversion Tool (AWS SCT) is a Java utility that connects to source and target databases, scans the source database schema objects (tables, views, indexes, procedures, and so on), and converts them to target database objects.

This section provides a step-by-step process for using AWS SCT to migrate an Oracle database to an Aurora PostgreSQL database cluster. Since AWS SCT can automatically migrate most of the database objects, it greatly reduces manual effort.

We recommend to start every migration with the process outlined in this section and then use the rest of the Playbook to further explore manual solutions for objects that could not be migrated automatically. For more information, see [AWS SCT user guide](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/Welcome.html).

**Note**  
This walkthrough uses the AWS DMS Sample Database. You can download it from [GitHub](https://github.com/aws-samples/aws-database-migration-samples).

## Download the software and drivers
<a name="chap-oracle-aurora-pg.tools.awssct.download"></a>

Download and install AWS SCT from the [AWS SCT user guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html).

Download the [Oracle Database](http://www.oracle.com/technetwork/database/features/jdbc/jdbc-drivers-12c-download-1958347.html) and [PostgreSQL](https://jdbc.postgresql.org/download) drivers.

Find other supported drivers in the [AWS SCT user guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html#CHAP_Installing.JDBCDrivers).

## Configure AWS SCT
<a name="chap-oracle-aurora-pg.tools.awssct.configure"></a>

Follow this procedure for configuring `AWSSCT` to streamline your database migration process.

1. Start AWS Schema Conversion Tool (AWS SCT).

1. Choose **Settings** and then choose **Global settings**.

1. On the left navigation bar, choose **Drivers**.

1. Enter the paths for the Oracle and PostgreSQL drivers downloaded in the first step.

    ![Enter the paths for the Oracle and PostgreSQL drivers](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-configure-aws-sct.png) 

1. Choose **Apply** and then **OK**.

## Create a new migration project
<a name="chap-oracle-aurora-pg.tools.awssct.newproject"></a>

Create a new migration project to define the source and target databases, configure migration settings, and launch the replication process.

1. Choose **File**, and then choose **New project wizard**. Alternatively, use the keyboard shortcut **Ctrl\+W**.

1. Enter a project name and select a location for the project files. Choose **Next**.

1. Enter connection details for the source Oracle database and choose **Test connection** to verify. Choose **Next**.

1. Select the schema or database to migrate and choose **Next**.

The progress bar displays the objects that AWS SCT analyzes. What AWS SCT completes the analysis, the application displays the database migration assessment report. Read the Executive summary and other sections. Note that the information on the screen is only partial. To read the full report, including details of the individual issues, choose **Save to PDF** at the top right and open the PDF document.

![Database Migration assessment report](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-aws-sct-assessment-report.png)


Scroll down to the **Database objects with conversion actions for Amazon Aurora (PostgreSQL compatible)** section.

![Conversion statistics](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-aws-sct-assessment-report-conversion-statistics.png)


Scroll further down to the **Detailed recommendations for Amazon Aurora (PostgreSQL compatible) migrations** section.

![Detailed recommendations](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-aws-sct-assessment-report-detailed-recommendations.png)


Return to AWS SCT and choose **Next**. Enter the connection details for the target Aurora PostgreSQL database and choose **Finish**.

When the connection is complete, AWS SCT displays the main window. In this interface, you can explore the individual issues and recommendations discovered by AWS SCT.

For example, expand **sample database**, **dms sample**, **Procedures**, **generate\_tickets**. This issue has a red marker indicating it could not be automatically converted and requires a manual code change (issue 811 above). Select the object to highlight the incompatible code section.

![Conversion issue in the generate tickets procedure](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-aws-sct-generate-tickets.png)


Right-click the schema and then choose **Create report** to create a report tailored for the target database type. You can view this report in AWS SCT.

The progress bar updates while the report is generated.

 AWS SCT displays the executive summary page of the database migration assessment report.

![Assessment report executive summary](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-aws-sct-executive-summary.png)


Choose **Action items**. In this window, you can investigate each issue in detail and view the suggested course of action. For each issue, drill down to view all instances of that issue.

![Assessment report action items tab](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-aws-sct-action-items.png)


Right-click the database name and choose **Convert schema**. Make sure that you uncheck the `sys` and `information_schema` system schemas. Aurora PostgreSQL already has an `information_schema` schema.

![Convert database schema](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-aws-sct-convert-schema.png)


This step doesn’t make any changes to the target database.

On the right pane, AWS SCT displays the new virtual schema as if it exists in the target database. Drilling down into individual objects displays the actual syntax generated by AWS SCT to migrate the objects.

Right-click the database on the right pane and choose either **Apply to database** to automatically run the conversion script against the target database, or choose **Save as SQL** to save to an SQL file.

![Apply converted code to database](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-oracle-aurora-pg-aws-sct-apply-to-database.png)


We recommend saving to an SQL file because you can verify and QA the converted code. Also, you can make the adjustments needed for objects that could not be automatically converted.

For more information, see the [Schema Conversion Tool User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html).