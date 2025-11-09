# Migration assessment

The assessment job type in AWS Transform is designed to provide cost estimates and savings for
migrating your workloads to AWS.

This job type uses an advanced AI-powered language model specifically trained for AWS
infrastructure analysis. The specialized LLM evaluates Amazon EC2 instance recommendations,
performs BYOL (Bring Your Own License) analysis, and determines optimal dedicated host
mappings by incorporating real-time Amazon EC2 pricing data and host configuration
specifications.

The assessment job type currently supports compute-based workloads. While it includes
servers deployed to run specialized workloads, it cannot assess the specialized workloads
themselves.

When planning to migrate to AWS you can use this assessment to:

- Get cost estimates, including Amazon EC2 and Amazon EBS and storage cost estimates, for your
  migration
- Identify potential savings opportunities
- Receive Amazon EC2 instance recommendations
- Analyze licensing options (BYOL)
- Determine optimal dedicated host mappings

## Creating and starting a

job

The first step of a migration project is to create an AWS Transform job.

###### To create and start a new migration assessment job

1. On your workspace landing page, choose **Create a job with
   AWS Transform**.
2. Choose the migration assessment option.
3. Review the job details that AWS Transform proposes. You can specify a different
   name for the job if you'd like.
4. Choose **Create and start a job**.

## Migration assessment workflow

1. In the left navigation pane, choose **Share on-premises server
   data**.
2. Upload data files that can be used by AWS Transform for the assessment. Make sure the file includes all the servers that
   you want to assess for migration to AWS. You can include 30,000 servers per
   assessment job. The maximum supported file size is 10 MB. These types of files are supported:
   - The [AWS Transform discovery tool](discovery-tool.md "discovery-tool.md") enables you to automatically
     discover server inventory in your organization in preparation for migration.
     When you configure OS access the discovery tool can help you obtain database assessment and assist in application dependency mapping and wave planning.
   - RVTools: You can upload either a
     ZIP of .csv files or an excel file that RVTools produces when you
     choose **Export all to Excel** from the RVTools **File** menu.
   - [Migration Portfolio Assessment](https://mpa.accelerate.amazonaws.com/ "https://mpa.accelerate.amazonaws.com/") (MPA) import file
   - [Export for vCenter](https://github.com/awslabs/export-for-vcenter "https://github.com/awslabs/export-for-vcenter")
   - [Migration Evaluator Quick Insights](https://aws.amazon.com/migration-evaluator/ "https://aws.amazon.com/migration-evaluator/"). You can download the **Migration Evaluator Quick Insights** file from the [Migration Evaluator Console](https://console.tsologic.com/ "https://console.tsologic.com/").
   - A Microsoft Excel file created from the AWS Transform Assessment Data
     template. You can download the AWS Transform Assessment data template from AWS Transform.

3. To include a storage assessment, upload a NetApp Data Infrastructure Insights (DII) file or an
   Excel file created from the AWS Transform Assessment data template. See [Preparing DII files](transform-app-assessments.md#transform-assessment-workflow-dii "transform-app-assessments.md#transform-assessment-workflow-dii") to learn more about DII files.
   You can download the AWS Transform Assessment Data template from AWS Transform.
4. Specify the AWS Region where you want to host your migrated workloads. All
   commercial AWS Regions are supported.
5. Choose **Generate business case**. The right pane
   automatically switches to the **Worklog** tab where you can
   track the progress of the job.
6. Download and review the business case.
7. (Optional) Use the chat pane to ask AWS Transform questions about your business
   case.

### Preparing DII files

To provide AWS Transform with the necessary data for a storage assessment you have to run NetApp queries and save the results in CSV files. Zip the CSV files and upload the zip to AWS Transform.

For NAS volumes, run these queries:

- Disk
- Internal Volumes
- Storage
- Share

For SAN volumes, run these queries:

- Virtual Machines
- Volume

Follow these steps to run the queries and save the resulting files:

1. From the home page of your NetApp DII tenant choose **Explore** and then choose **New Metric Query**.
2. Select the query type.
3. Select a period of 30 days.
4. Open the settings from the gear icon and choose **Select all the columns**.
5. Save as a CSV file by selecting the **Export to csv** icon.

## Tracking the progress of a

migration assessment job

The **Worklog** tab provides a detailed log of the actions that
AWS Transform takes, along with human input requests and your responses to those requests.
AWS Transform adds entries to the worklog to show the progress of the assessments, including
processing uploaded files, analyzing files, generating the assessment report, and any
errors that occur.
