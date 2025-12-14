# Transformation of mainframe

applications

AWS Transform accelerates the transformation of your mainframe modernization applications. This topic describes the available capabilities.

###### Topics

- [Prerequisite: Prepare project inputs in S3](#transform-app-mainframe-workflow-prereq "#transform-app-mainframe-workflow-prereq")
- [Sign-in and
  create a job](#transform-app-mainframe-workflow-signin "#transform-app-mainframe-workflow-signin")
- [Tracking
  transformation progress](#transform-app-mainframe-workflow-track-progress "#transform-app-mainframe-workflow-track-progress")
- [Set up a
  connector](#transform-app-mainframe-workflow-setup-connector "#transform-app-mainframe-workflow-setup-connector")
- [Analyze
  code](#transform-app-mainframe-workflow-code-analysis "#transform-app-mainframe-workflow-code-analysis")
- [Data analysis](#transform-app-mainframe-workflow-data-analysis "#transform-app-mainframe-workflow-data-analysis")
- [Activity metrics analysis](#transform-app-mainframe-workflow-activity-metrics "#transform-app-mainframe-workflow-activity-metrics")
- [Generate technical documentation](#transform-app-mainframe-workflow-generate-documentation "#transform-app-mainframe-workflow-generate-documentation")
- [Extract
  business logic](#transform-app-mainframe-workflow-extract-business-logic "#transform-app-mainframe-workflow-extract-business-logic")
- [Decomposition](#transform-app-mainframe-workflow-decomposition "#transform-app-mainframe-workflow-decomposition")
- [Migration
  wave planning](#transform-app-mainframe-workflow-wave-planning "#transform-app-mainframe-workflow-wave-planning")
- [Refactor
  code](#transform-app-mainframe-workflow-refactor-code "#transform-app-mainframe-workflow-refactor-code")
- [Reforge code](#transform-app-mainframe-workflow-refactor-code-reforge "#transform-app-mainframe-workflow-refactor-code-reforge")
- [Plan your modernized applications testing](#transform-app-mainframe-workflow-test-planning "#transform-app-mainframe-workflow-test-planning")
- [Generate
  test data collection scripts](#transform-app-mainframe-workflow-test-data-collection "#transform-app-mainframe-workflow-test-data-collection")
- [Test automation
  script generation](#transform-app-mainframe-workflow-test-automation "#transform-app-mainframe-workflow-test-automation")
- [Deployment
  capabilities in AWS Transform](#transform-app-mainframe-features-deployment "#transform-app-mainframe-features-deployment")

## Prerequisite: Prepare project inputs in S3

AWS Transform is capable of handling complex mainframe codebases. To use codebase,
make sure you have all the assets in your S3 location.

**Key project inputs:**

- **Source code:** You must upload your mainframe source code files to S3. This includes COBOL programs, JCL scripts, copybooks, and any other relevant source files.
- **Data files**: If you have any VSAM files or other data files that your mainframe applications use, these need to be uploaded to S3.
- **Configuration files**: Include configuration files specific to your mainframe environment.

**Other project inputs**

- System Management Facility (SMF) records: If applicable, upload SMF records to a new folder in the S3 bucket where the source code is stored, these records should be in a .zip file format.
- Formatting: For technical documentation generation, you can leverage an optional configuration file to generate PDF documents which aligns with your required formats and standards, including headers, footers, logos, and customized information.
- Glossary: AWS Transform AWS Transform leverages automation with Generative AI for documentation generation and business rule extraction. Including a glossary CSV file with information about important abbreviations and terminologies in the root directory of your zip file will help improve the generated documentation quality.
- Test data: If available, upload test data sets that can be used to validate the modernized application. This data should be stored in a new folder in the S3 bucket where the source code is stored.

**Download modernization tools**

For a test environment modernizing mainframe applications, beyond the automation necessary to run test cases at scale, AWS Transform makes tools available to achieve specific testing tasks. These tools include Data Migrator, designed to facilitate the migration of database schemas and data from legacy systems, Compare tool, to automate the verification that a
modernized application produces the same results as reference data, and Terminals, to provide capabilities to connect to legacy
mainframe and midrange screen interfaces to capture scenario scripts and videos, in the context of capturing online test cases. These tools are downloaded in your S3 bucket.

**Optional configuration of S3 vector
bucket.**

In Regions where S3 vector buckets are available, AWS Transform will store searchable vector
encodings of job output in this S3 vector bucket in your account to provide an AI powered search and chat experience. Data is not used outside of this job, and is not used to train models. T
o enable this, you must create and provide S3 vector bucket. AWS Transform automatically creates
and attaches a role with required permissions to write to this bucket.

## Sign-in and

create a job

To sign into the AWS Transform web experience, follow all the instructions in the
[Getting started with AWS Transform](getting-started.md "getting-started.md") section of the
documentation.

**To create and
start a job:** Follow the steps in [Start your project.](transform-environment.md#start-workflow "transform-environment.md#start-workflow")

When setting up your workspace for mainframe transformation, you can optionally
set up an Amazon S3 bucket to be used with the S3 connector. After creating the bucket
and uploading the desired input files into the bucket, save that S3 bucket ARN for
use later. Or you can set up the S3 bucket when setting up the connector as well.
For more information, see [Set up a
connector](#transform-app-mainframe-workflow-setup-connector "#transform-app-mainframe-workflow-setup-connector").

**Create workspace:** Name and
describe your workspace where jobs, collaborators, and associated
artifacts will be stored.

**Create job:** Create a job by selecting from
preconfigured job plans, or customize the job plan based on your objective by
selecting from the list of supported capabilities.

When you set up your workspace for
mainframe transformation, you must set up an Amazon S3 bucket to be used
with the S3 connector. After creating the bucket and uploading the
desired input files into the bucket, save that S3 bucket ARN for use
later. Alternatively, you can set up the S3 bucket when setting up the
connector as well.

###### Important

AWS Transform will refuse operations from you if you don’t have the proper
permissions. For example, a contributor cannot cancel a job transformation of
mainframe applications or delete a job. Only an administrator can perform these
functions.

When you create your job you can select from the capabilities below, but the Kickoff step is always required as it is where the location of the source code for the project is located.
In the first job set up in a workspace you are required to set up a connector to your Amazon S3 bucket.

## Tracking

transformation progress

You can track the progress of the transformation throughout the process in two
ways:

- **Worklog** – This provides a detailed
  log of the actions AWS Transform takes, along with human input requests, and your
  responses to those requests.
- **Dashboard** – This provides
  high-level summary of the mainframe application transformation. It shows
  metrics on number of jobs transformed, transformation applied, and estimated
  time to complete the transformation of mainframe applications. You can also
  see details of each step including, lines of code by file types, generated
  documentation by each file type, the decomposed code, migration plan, and
  the refactored code.

## Set up a

connector

Set up a connector with your Amazon S3 bucket so that AWS Transform can access your resources and perform transformation functions.

This is some of the information that AWS Transform might ask you to provide:

- AWS account ID for performing mainframe modernization capabilities
- Amazon S3 bucket ARN where your transformation resources are stored
- Amazon S3 bucket path for the input resources you want to transform
- Whether to enable AWS Transform chat to learn from your job progress
  (optional)

Once you have set up your S3 connector and S3 project inputs, and shared an S3 vector bucket for indexed output, you can create a job based on the objective of the mainframe modernization project.
Here is the full list of capabilities you can select from with dependencies noted For example, code analysis is required for most steps.

###### Important

Your data is stored and persisted in the AWS Transform's artifact store in your
workspace and is used only for running the job.

### S3 bucket

CORS permissions

When setting up your S3 bucket to view artifacts in AWS Transform, you need to add
this policy to the S3 bucket's CORS permission. If this policy is not set up
correctly, you may not be able to use the inline viewing or file comparison
functionalities of AWS Transform.

```
[
    {
        "AllowedHeaders": [],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
              "https://.transform.eu-central-1.on.aws",
              "https://.transform.ap-south-1.on.aws",
              "https://.transform.ap-northeast-1.on.aws",
              "https://.transform.ap-northeast-2.on.aws",
              "https://.transform.ap-southeast-2.on.aws",
              "https://.transform.ca-central-1.on.aws",
              "https://.transform.eu-west-2.on.aws",
              "https://.transform.us-east-1.on.aws"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 0
    }
]

```

## Analyze

code

After you share the Amazon S3 bucket path with AWS Transform, it will analyze the code
for each file with details such as file name, file type, lines of code, and their
paths.

###### Note

You can download the Analyze code results through the artifacts tab at the job or workspace level.
At the job level go to the ‘Artifacts’ option in the left navigation menu, and open the ‘results’ folder,
or at the workspace level find the name of the job, and open the ‘results’ folder.
This will download a zip file that contains the classification file for manual classification workflow, assets list,
dependencies JSON file, and list of missing files.

In the job plan select Analyze code in the left navigation pane to view your results. You can view your code analysis results in several ways:

- **List view** – All files in the Amazon S3
  bucket you want to transform for mainframe
- **File type view** – All files in the
  Amazon S3 bucket displayed per file type. For a list of supported file
  types, see [Supported
  files](transform-app-mainframe.md#transform-app-mainframe-supported-files "transform-app-mainframe.md#transform-app-mainframe-supported-files").
- **Folder view** – All files in the
  Amazon S3 bucket displayed in folder structure.
  Within the file results, AWS Transform provides the following information
  depending on what file view you choose:

- Name
- File type
- Total lines of code
- File path
- Comment lines
- Empty lines
- Effective lines of code
- Number of files
- Cyclomatic Complexity - Cyclomatic complexity represents the number of
  linearly independent paths through a program’s source code. AWS Transform will show
  a cyclomatic complexity for each of the files. With this metric, you can
  evaluate code maintainability and identify areas that need refactoring.

**Missing files**– Missing files from the
mainframe modernization code analysis. These files ideally, should be added as a
part of the source input in Amazon S3 bucket, and the analysis step should be re-run for
better and cohesive results.

**Identically named** – AWS Transform gives you a list of files
that share the same name, and possibly the same characteristics (e.g., number of
lines of code). It will not have the ability to compare the difference between the
contents of any two files at one time.

**Duplicated IDs** – With Cobol program, the **Program ID** field serves as the unique identifier of the
file. This ID must be unique because it’s used to call the program throughout your
project. However, some projects might have COBOL files with different names but the
same Program ID. Getting the list of those files during the assessment can help
understand the dependencies among all programs.

###### Note

This is specific to COBOL code and files.

When you have programs with duplicated IDs, it’s suggested to change the Program IDs of these
files to have a unique identifier for each of these in the COBOL code. You can then
re-run your job to get more accurate and comprehensive code analysis results.

By resolving duplicate Program IDs, you can:

- Improve code clarity and maintainability
- Reduce potential conflicts in program calls
- Enhance the accuracy of dependency mapping
- Simplify future modernization efforts

**Codebase issues** – Potential issues detected within the codebase
that you should resolved before continuing with the modernization project. These issues could
include missing references with associated statements or unsupported links in the code.

**Update classification** – With manual
reclassification, you can reclassify files using the bulk update feature by
uploading the JSON file with the new classification.

###### Important

This is only available for `UNKNOWN` and `TXT` files.

After reclassification, AWS Transform will:

1. Updates the classification results
2. Re-runs dependency analysis with the new file types
3. Refreshes all affected analysis results

###### Note

You can reclassify files only after the initial analysis loop
completes.

### Inline

viewer and file comparison

The Inline viewer is a feature in the AWS Transform for mainframe capabilities that
provides two key visualization capabilities:

- **File view**: View content of selected
  legacy files from jobs
- **File comparison**: Compare content of two
  legacy files side-by-side

**Input file viewing**

###### To view your files in the **Analyze code**

step

- Under **View code analysis results**,
  select a file using the check box in the list.

Choose the **View** action button
(enabled when 1 item is selected).

File content will be rendered on screen in the **File View** component.

**File comparison**

###### To compare files in the **Analyze code**

step

1. Under **View code analysis results**,
   select two files using the check boxes in the list.
2. Choose the **Compare** action button
   (enabled only when 2 items are selected).
3. Files will be displayed side-by-side in the **File
   comparison** component.

###### Note

You can't select more than two files to compare files.

###### Important

If you're having issues with inline viewer or file comparison make sure
that the S3 bucket is set up correctly. For more information on S3 bucket's
CORS policy, see [S3 bucket
CORS permissions](#transform-app-mainframe-workflow-setup-connector-s3 "#transform-app-mainframe-workflow-setup-connector-s3").

## Data analysis

AWS Transform provides data analysis to help understand the impact of data relationships and elements to the mainframe modernization project. The two outputs provided are:

- Data lineage: Traces the lifecycle of data by mapping relationships between data sources, jobs, and programs
- Data dictionary: Serves as a repository documenting the structural metadata of legacy data elements

On completion of the analysis, there will be two tabs present for each output, and then multiple views available described below for both data lineage and dictionary.

###### Note

When you request data anlysis. AWS Transform performs code analysis, which is required in order to perform
data analysis.

### Data lineage

AWS Transform provides multiple views based on the data relationships that need to be
understood across the code base being modernized. The four table views available
in data lineage include:

- **Data sets**: This view provides a
  comprehensive impact analysis, including operation tracking to help
  distinguish between read, write, update, and delete
- **Db2 tables**: Provide the impact
  analysis related to Db2 tables and the operations
- **Program-to-data**: Identify which COBOL
  programs reference each dataset
- **JCL-to-data relationships**: Identify
  which JCL scripts reference each dataset

Summary provides an overview of data sources, and their relationships to programs and JCLs, as well as summary information about how the data sources are leveraged and total operations found in the codebase.

### Data dictionary

Understanding the data elements within the data sources present in the codebase is the next step to realize how the various data sources are dependent. Data dictionary is a data catalog providing field level metadata with business language descriptions for accurate transformation mapping.

- **COBOL data structure**: Provides field
  information across COBOL copybooks present in the codebase, including
  field properties and business definition
- **Db2 tables**: Provides column and table
  properties across the Db2 tables present in the codebase, including
  primary and foreign key, schema information, and data types

Relationship between data lineage and dictionary is available by selecting the
data source, and then utilizing the data lineage or data dictionary button in
order to dive deeper on the relationship between the data source and the data
elements. The navigation between data lineage and dictionary, provides
integrated data visibility with data lineage providing the "what" - structure
and meaning, alongside the "where" - usage and relationship.

## Activity metrics analysis

Activity metrics analysis allows you to analyze System Management Facility (SMF) records type 30 and type 110. The analysis provides insights into batch jobs and CICS transactions that used within your mainframe application, and can help with retiring unused code or decisions around target architecture for modernized application. If you choose to include activity metrics analysis in your job, then we recommend completing the code analysis step first to provide richer SMF outputs, though this is not required.

###### Note

When you negotiate the job plan for mainframe modernization,
we recommend completing the code analysis and decomposition steps first to provide richer outputs.

### Onboard SMF records for analysis

You must provide the SMF record location within your S3 bucket as the initial
step for SMF analysis. We recommend providing a minimum of 13 months of records
to capture annual occurrences that shorter time frames might miss. While 13
months is recommended, any time frame with detectable SMF records will produce
analysis results.

Your SMF extract must meet these format requirements:

- Include all types 30 and 110
- Use raw binary file in EBCDIC format
- Include RDW bytes

Provide a link to the SMF records within your S3 bucket, ensuring the records are in a folder separate from your source code. Records must be in .zip file format. If you provide a link to a folder where SMF records are not detected, you will receive an error message and no analysis will be completed.

### Analysis output

The analysis output contains three components: tabular view, .csv output (available in your S3 bucket), and visualization within the dashboard. The header displays the time range of your provided records so you can identify any missing key dates. For example, if your records span May 1 - October 31st but exclude the busy day after Thanksgiving, you can easily understand that key records are missing. Timestamps in the web application reflect your system's time zone and the SMF records.

#### Tabular view

The tabular view contains up to three main components for batch jobs and CICS transactions:

- **Summary** - Provides key jobs and transactions
- **Batch job/CICS transactions analysis** - Provides aggregated analysis across jobs and transactions
- **Code analysis comparison** (batch only) - Available when code analysis step is executed prior to SMF analysis

The discovery summary provides three groups of jobs and transactions that help you quickly identify items for deeper analysis.

Batch job and CICS transaction analysis provides aggregated analysis across jobs and transactions. Analysis results have some columns hidden by default - use the gear icon to display additional fields.

The transaction key generates unique data aggregation for CICS transactions, combining four fields into a single key value:

- Transaction ID
- Program name
- SysPlex ID
- SysID

You can search by the complete key or any component of the key in the analysis output.

Code analysis comparison highlights jobs found in either SMF records or the analyze code step but not present in both. This shows jobs that haven't run during your SMF record timeframe or weren't present in the analyze code step. This output is only available when you execute the code analysis step before SMF analysis in your job.

#### Best practices

To get comprehensive outputs, for **Batch jobs (type 30)**, ensure your JCL file name matches the job name to get meaningful outputs in the code analysis comparison.

##

Generate technical documentation

You can generate technical documentation for your mainframe
applications undergoing modernization. By analyzing your code, AWS Transform can
automatically create detailed documentation of your application programs, including
descriptions of the program logic, flows, integrations, and dependencies present in
your legacy systems. This documentation capability helps bridge the knowledge gap,
enabling you to make informed decisions as you transition your applications to
modern cloud architectures.

###### Note

When you request generation of technical documentation, AWS Transform performs code analysis, including code dependency analysis, which are required in order to generate the documentation.

###### To generate technical documentation

1. In the left navigation pane, under **Generate
   technical documentation**, choose **Select files and
   configure settings**.
2. Select the files in the Amazon S3 bucket that you want to generate
   documentation for, and configure the settings in the **Collaboration** tab.

###### Note

Selected files should have the same encoding type (that is, all in the
same CCSID - UTF8 or ASCII). Otherwise, generated technical
documentation might have empty fields or sections. 3. Choose the documentation detail level:

    * **Summary** – Provides a
     high-level overview of each file in the scope. Also, gives a
     one-line summary of each file.
    * **Detailed functional specification**
     – Provides comprehensive details for each file in the
     mainframe application transformation scope. Some details include
     logic and flow, dependencies, input and output processing, and
     various transaction details.

###### Note

Documentation can be generated only for COBOL and JCL
files. 4. Choose **Continue**. 5. Once AWS Transform generates documentation, review the documentation results by
following the Amazon S3 bucket path in the console, where the results are
generated and stored. 6. Once the documentation is generated, you can also use AWS Transform chat to ask
questions about the generated documentation and decide the next
steps.

### Add user information into the documentation

```
ARTIFACT_ID.zip
└── app/
    ├── File1.CBL
    ├── File2.JCL
    ├── subFolder/
    │   └ File3.CBL
└── glossary.csv
└── pdf_config.json
├── header-logo.png
├── footer-logo.png
└ ...
```

Optional files can be added in the zip file to help improve the generated
documentation quality and provide customized PDF cover page. Some of these can
be:

- **glossary.csv file**: You can choose to
  provide and upload an optional glossary in the zip file in the S3
  bucket. The glossary is in CSV format. This glossary helps create
  documentation with relevant descriptions in line with the customer vocabulary.
  A sample `glossary.csv` file looks like:

```
LOL,Laugh out loud
ASAP,As soon as possible
WIP,Work in progress
SWOT,"Strengths, Weaknesses, Opportunities and Threats"
```

- **pdf_config.json**: You can leverage
  this optional configuration file to generate PDF documents which align
  with their company’s formats and standards, including headers, footers,
  logos, and customized information. A sample
  `pdf_config.json` looks like:

```
{
    "header": {
    "text": "Acme Corporation Documentation",
    "logo": "header-logo.png"
  },
  "customSection": {
    "variables": [
      {
        "key": "business Unit",
        "value": "XYZ"
      },
      {
        "key": "application Name",
        "value": "ABC"
      },
      {
        "key": "xxxxxxxxxx",
        "value": "yyyyyyyyyyyy"
      },
      {
        "key": "urls",
        "value": [
          {
            "text": "Product Intranet Site",
            "url": "https://example.com/intranet"
          },
          {
            "text": "Compliance Policies",
            "url": "https://example.com/policies"
          }
        ]
      }
    ]
  },
  "footer": {
    "text": "This document is intended for internal use only. Do not distribute without permission.",
    "logo": "footer-logo.png",
    "pageNumber": true
  }
}
```

    + **Header:**




    	- For the cover page PDF file, the default text will be the
    	 project name.
    	- For each program PDF file, the default text will be the
    	 program name.
    	- There is no default logo. If a header logo is not configured,
    	 no logo will be displayed.
    	- The font size and logo size shall be dynamically changed based
    	 on the number of words or logo file size.
    + **Custom section:**




    	- If the custom section is not configured, it will be omitted
    	 from the PDF.
    	- The link has to be click able.
    + **Footer:**




    	- There is no default text or logo for the footer.
    	- The page number will be displayed in the footer by default,
    	 unless explicitly configured otherwise.
    	- The font size and logo size shall be dynamically changed based
    	 on the number of words or logo file size.

### Generate documentation inline viewer

You can view the PDF files in the generate technical documentation step.

###### To view the PDF files

1. Navigate to the **Review documentation
   results** tab.
2. Locate the PDF in the table listing generated PDFs.
3. Either select the rile and then select **View** or select the link element overlaid on the file name.

The PDF opens in AWS Transform, with the option to expand the screen in the top right.

###### Note

AWS Transform also gives you the ability to download either an XML of PDF version of the generated technical documentation.

###### Important

If you're having issues with documentation inline viewer, make sure that
the S3 bucket is set up correctly. For more information on S3 bucket's CORS
policy, see [S3 bucket
CORS permissions](#transform-app-mainframe-workflow-setup-connector-s3 "#transform-app-mainframe-workflow-setup-connector-s3").

## Extract

business logic

You can extract essential business logic from your mainframe
applications that are undergoing modernization. AWS Transform automatically analyzes your code to
identify and document critical business elements, including detailed process flows,
and business logic that is embedded in your applications. This capability serves
multiple stakeholders in your modernization journey. Business analysts can leverage
extracted logic to create precise business requirements and identify gaps or
inconsistencies in current implementations. Developers gain the ability to quickly
comprehend complex legacy system functionality without extensive mainframe
expertise.

###### Note

When you request business logic extraction. AWS Transform performs code analysis, including code
dependency and entry point analysis, which are required in order to perform
business logic extraction.

###### To extract business logic

1. In the left navigation pane, under **Extract business
   logic**, choose **Configure settings**.
2. In the **Collaboration tab** select how you want to extract business logic:
   - **Application level**: Generates business documents for all business functions, transactions, batch jobs, and files. This selects all of the files in the application.
   - **File level**: Generates business documents only for files you select from the file table.

###### Note

    * For either option you can select **Include detailed functional
     specification** so that AWS Transform includes control flow
     and comprehensive business rules for the selected files.
    * Selected files should have the same encoding type (that is, all in the same CCSID - UTF8 or
     ASCII). Otherwise, generated documentation might have empty
     fields or sections.
    * Documentation can be generated only for COBOL and JCL files.
    * For application level, programs used by CICS transactions and
     batch jobs are grouped together, while all other programs are
     categorized as *Unassigned*.

3. Choose **Continue**.
4. Once AWS Transform extracts business logic it stores the results in an Amazon S3 bucket
   in JSON format so that you can view them online.

###### Note

The number of generated business rule files might be larger than your initial
selection. Some selected files may trigger business rule extraction to include
additional dependent files, which will also appear in the results table.

### View the extracted business documentation inline

You can view the business logic in the Extract business rule step. To do
this,

1. Navigate to **Review business logic extraction results**.
2. Select the document you want to view from the table, and then click the **View result** button.

The business documentation page opens in a new browser tab.

##

Decomposition

You can decompose your code into domains that account for dependencies
between programs and components. This helps the related files and programs to be
grouped appropriately within the same domain. It also helps maintain the integrity
of the application logic during the decomposition process.

###### Note

When you request decomposition, AWS Transform performs code analysis, including code dependency analysis, which are required in order to perform decomposition.
We also recommend that you perform business logic extraction before decomposition for better results.

To get started with decomposing your application:

1. Select **Decompose code** from the left
   navigation pane.

###### Note

One domain, Unassigned, is automatically created for all files not associated with a domain. On initial navigation, all files should be associated to Unassigned, unless domains were proposed from application level business logic extraction. 2. Create a new domain through the Actions menu, and then choose Create domain. 3. In Create domain, provide domain name, optional description, and mark some files as seeds.

    * CICS configured files (CSD) and scheduler configured files (SCL) can be used for automatic seed detection.
    * You can also set one domain only as a common component. The files in this domain are common to multiple domains.

4. Choose Create.

###### Note

You can create multiple domains with different files as seeds. 5. After confirming all domains and seeds, choose Decompose. 6. AWS Transform will check the source code files and then decompose into domains with programs and data sets with similar use cases and high programming dependencies.

AWS Transform gives you a tabular and graph view of decomposed domains as dependencies. Graph view has three options:

    * **Domain view** – Can view how different domains are related to each other in visual format.
    * **Dependency view** – Can view all files in each domain as a complex dependency graph. If a node that was added to a domain didn't receive information from a seed in the same domain, then this node will either be predicted into unassigned (node didn't receive any information), disconnected (in a sub graph that didn't receive seed information) or into another domain (node received information from at least that domain).
    * **Subgraph view** - User can create subgraphs to visualize a subset of nodes to more clearly understand the relational impact and boundaries of that collection of nodes.




    	+ To create a subgraph select a group of nodes and select the Extract subgraph option from the tool bar
    	+ Merging subgraphs is available, when merging a new third subgraph is created in addition to the two subgraphs you are merging.

###### Note

Repeat these steps to add more domains or to reconfigure your already created domains with a different set of seeds if you don't like current domain structure. 7. When completed, choose **Continue**.

### Seeds

Seeds are the foundational inputs for the decompose code phase. Each component
or file (e.g., JCL, COBOL, Db2 tables, CSD, and scheduler files) can be assigned
as a seed to only one domain, ensuring clear boundaries and alignment during the
decomposition process.

The identification of the seeds depends on the structure of the application or
portfolio. In the case of a typical mainframe legacy application, seeds can
often be determined by adhering to established naming conventions, batch-level
grouping in the scheduler, and transaction-level grouping defined in the CICS
system. Additionally, database tables can also serve as seeds, providing another
layer of structure for decomposition.

### Import and/or update dependencies files

During decomposition, you can upload a JSON file for the dependencies that
replaces the existing files generated by the dependencies analysis AWS Transform
performs.

**Export dependencies** function allows you to
download the dependencies json file generated in the decomposition step. After
downloading, you can modify the file per your requirement. Then, you can
**import dependencies** using the AWS Transform’s
upload functionality which allows you to upload the new JSON file of the
dependencies that replaces the file generated by the dependencies analysis.
After that, the graph in the decomposition step will be updated.

###### To export, modify, and import dependencies

1. On the **View decomposition results**
   page, choose **Actions**.
2. In the dropdown list, choose **Update dependencies
   file** option under **Other
   actions**.
3. In the **Update dependencies file**
   modal,
   1. Download the dependency file AWS Transform created from the existing
      analysis results.
   2. In the downloaded file, modify the dependencies based on what
      you want to achieve.
   3. After modifying, save and upload this file using the **Upload dependency file** button.

   ###### Note

   The only accepted file format is JSON file.

4. Next, choose **Import**.

AWS Transform will import the dependency file and create a new dependencies graph
based on your input.

### Import and/or Update Domains

For customers that have domains, seed, and/or file relationships mapped prior to the decomposition step, you can upload this domain definition through the Import domains file function available through the Actions menu. Some examples of when this function may be utilized:

- Bring forward decomposition from another job
- Subject matter experts providing this mapping

Once the domains file has been imported, the user can either run decomposition against the domain definition, or if satisfied can Save and then Submit the domain definition.

### Parent/child/neighbor files

In a dependencies graph, programs relate to each other through different types
of connections. Understanding these relationships helps you analyze program
dependencies during transformation of your mainframe applications. It also helps
with understanding the boundaries of a domain. For example, if you select a
domain, and then select parent one level, it will show you the connected
nodes.

**Parent relationships** – A parent file
calls or controls other programs. Parents sit above their dependent programs in
the hierarchy. You can select parent at one level or at all levels.

**Children relationships** – A child file
is called or controlled by the parent program. Children sit below their parent
in the file hierarchy.

**Neighbor relationships** – Neighbors are
files at the same hierarchical level. They share the same parent program and
might interact with each other directly.

## Migration

wave planning

Based on the domains you created in the previous step, AWS Transform generates a migration
wave plan with recommended modernization order.

###### Note

Decomposition is a required step that must be completed in your job plan prior to running migration wave planning. If migration wave planning is not selected, but added to the job plan due to the inclusion of decomposition, this step will auto complete.

1. To view the planning results, choose **Plan Migration
   Wave**, and then choose **Review Planning
   Results**.
2. Review the domain wave plan (either in a table view or a chart
   view).
3. You can either choose to go with the recommended migration wave plan
   generated by AWS Transform or add your preference manually by importing a JSON
   file.

###### Note

You can choose to migrate multiple domains in a single wave. 4. (Optional) If you decide to manually adjust migration wave plan, AWS Transform
generates a new migration wave plan per your preference. You can also adjust
the domains in each wave as required by choosing **Add preference** and then, **Add and regenerate**. 5. After verifying, choose **Continue**.

If you're satisfied with this migration plan, you can move next step for
refactoring the code. If you need to adjust the preference, you can follow these
steps again.

## Refactor

code

In this step, AWS Transform refactors the code in all or selected domain files into Java
code. The goal of this step is to preserve the critical business logic of your
application while refactoring it to a modernized cloud-optimized Java
application.

###### Note

When you request refactoring, AWS Transform performs code analysis, including code dependency analysis, which are required in order to perform refactoring.
We also recommend that you perform decomposition and wave migration planning before refactoring, for better results.

1. Navigate to **Refactor code** in the left
   navigation pane, and choose **Domains to migrate**.
2. Select the domains you want to refactor.
3. Choose **Continue**. You can track the status of
   refactoring domains (and files in it) using the worklog. AWS Transform will do the
   transformation of the mainframe code, and generate results without any
   manual input.
4. After refactoring completes, it will change the status to
   `Completed` in the worklog. You can view the results of
   refactored code by going to the Amazon S3 bucket where the results are
   stored. Each domain will provide a status for **Transform** (with each file), and **Generate** and will be marked as `Done`.

###### Note

Along with the refactored code, your S3 bucket will also have the AWS Blu
Age Runtime to be compiled.

You might also see certain domains that have a `Done with issues`
status. Expand those to see files showing a `Warning` status or an
`Error` status. You can view the issues for the `Warning`
and `Error` files, and choose to fix them for better refactoring results.
Additional guidance for fixing these errors and warnings can be found in the console
by viewing each of these files.

### File transformation status

After your refactoring completes, AWS Transform will give you transformation
status for all your files. These may include:

**Ignored** – AWS Transform will also give you the
`Ignored files` after the code refactor. These are the files that
are ignored during refactoring and haven’t been included in the
transformation.

**Missing** – `Missing files`
are not included during the refactoring and transformation. These should be
added again as a part of the source input in Amazon S3 bucket for better and
cohesive results. AWS Transform will give you the number and information of missing
files in the console.

**Pass through** – `Pass
 through` files are not modified during the refactoring step, and do
not go through any transformation. This status is useful for the Refactoring
action which may not have changed the file depending on the configured
refactoring.

**Fatal** – An unexpected error occurred
during the transformation of this file.

**Error** – An error occurred during the
transformation of this file and these files need to go through refactoring
again.

**Warning** – The transformation generated
all expected outputs for this file, but some elements might be missing or need
additional input. Fixing these and running the refactoring steps again would
give you better transformation results.

**Success** – The transformation generated
all expected outputs for this file and it has detected nothing
suspicious.

### Custom transformation configuration

Refactor transformation allows you to change and/or modify configuration to
improve the results of transformation.

###### To customize your transformation configuration

1. In **Refactor code** section, go to
   **Configure transformation** under
   Select domains.
2. In **Configure refactor** modal, specify
   the **Refactor engine version** (e.g.
   `4.6.0`) which will be used to compile and run the
   generated application. For more information on available engine
   versions, see [AWS Blu Age release notes](../../../m2/latest/userguide/ba-release-notes.md "../../../m2/latest/userguide/ba-release-notes.md").
3. Add your project name, root package, and target database. The target
   database is target RDMS for the project.
4. Under **Legacy encoding**, define the
   default encoding for your files (e.g., `CP1047`). And mark the check boxes
   next to **Export Blusam masks** and
   **Specify generate file format**. You
   can also choose to specify conversion table encoding file format.
5. Review all you changes. Then, choose **Save and
   close**.

This will allow you to reconfigure your code with the new specified
properties.

## Reforge code

**Reforge** uses Large Language Models (LLMs) to
improve the quality of refactored code. The initial COBOL-to-Java transformation
preserves functional equivalence while retaining COBOL-influenced data
structures and variable names from the legacy system. Reforge restructures this
code to follow modern Java practices and idioms, replacing COBOL-style
constructs with native Java collections and naming conventions. This makes the
code more readable and maintainable for Java developers.

###### Note

Quotas for reforge are:

- 3,000,000 lines of code per job
- 50,000,000 lines of code per user per month

Reforge your code after refactoring by following these steps:

1. Choose **Reforge java code** in the left navigation pane and then select
   **Configure code reforge**.
2. Provide the S3 location to your zipped buildable source project and choose
   **Continue**. Use this zip structure:

```
input.zip
        └── PROJECT-pom
        ├── PROJECT-entities
        ├── PROJECT-service
        ├── PROJECT-tools
        ├── PROJECT-web (optional)
        └── pom.xml

```

AWS Transform analyzes your zip package to locate files within the PROJECT-service directory
so that it can provide a selectable list of classes that you can reforge. These classes have the suffix `ProcessImpl.java`. 3. Complete the **Select classes to reforge** page and choose
**Continue**. Track the reforge status on the
**Worklog** tab. 4. View the results of your completed reforge on the **View results** page,
which displays the reforge status per class. It also specifies where to find
the Reforge result in your S3 bucket.

Once AWS Transform
gets this input from you it gives you a downloadable file with the **Reforge results**.

This is the zip structure resulting from a successful reforge:

```
reforge.zip
└── maven_project
├── reforge.log
└──tokenizer_map.json
```

- **maven_project** contains the reforged source
  code.
  - Files that have been refactored but whose compilation was not
    successfully finalized are located at `/src/main/resources/reforge/originalClassName.java.incomplete` and are named
    `originalClassName.java.incomplete`. Compare these to the original versions of the files to choose reforged functions you want to save.
  - Source files provided to AWS Transform that were refactored
    successfully are backed up to `src/main/resources/reforge/originalClassName.java.original` and are named
    `originalClassName.java.original`. The
    refactored versions of the files replace the source files provided
    to AWS Transform.

###### Note

The `originalClassName.java` files are replaced
with the reforged files only if the reforging process is successful. Otherwise, they retain the original content.

- **reforge.log** contains logs that you can use
  to diagnose job failures or provide to AWS support in case of an issue.
- **tokenizer_map.json** contains a mapping of token IDs to your data,
  such as file paths and class/method names, that are tokenized in the logs for privacy protection. You can provide this file to AWS support in case of an issue.

## Plan your modernized applications testing

You can create and manage test plans for your mainframe modernized applications based on extracted code attributes, job complexity, and scheduler paths. AWS Transform helps prioritize which jobs to test and identifies the specific artifacts needed for each test case. The test planning process is divided into three main phases: configuration, scoping, and review.

###### To create a test plan

1. **Configure test plan settings**
   1. In the left navigation pane, under **Plan your testing**, choose **Configure settings**.
   2. (Optional) Provide S3 paths for your Business Logic Extraction (BLE). These artifacts enhance test plan quality. Without BLE artifacts
      some fields in the test plan may remain incomplete.

2. **Define test plan scope**
   1. Select entry points, such as batch jobs, to include in your test plan.
   2. Filter and sort jobs based on multiple attributes:
      - Business functions (extracted from BRE BLE)
      - Domains (from decomposition phase)
      - File paths and locations
      - Custom search criteria

   3. Select individual jobs or entire groups for testing.
   4. Review job relationships and dependencies.

3. **Review and adjust the test plan**

The generated test plan provides comprehensive information including:

    * Preferred execution order based on dependencies
    * Job group assignments from scheduler
    * Complexity scores, which are aggregate scores for test cases
    * Business domain associations
    * Cyclomatic complexity metrics
    * Dataset and table dependencies
    * Lines of code metrics
    * Business function mappings

### Test plan customization options

Your test plan can be customized to address specific needs. For example, you can:

- Create new test cases by selecting multiple entry points
- Merge existing test cases to combine related functionality
- Split test cases for more granular testing
- Remove unnecessary test cases
- Add or remove entry points for existing test cases
- Modify test case descriptions and attributes
- Adjust execution order

### Detailed test case information

Each test case provides details that describe its content and the related dataset or datafiles:

- Comprehensive description of test scope
- Complete list of entry points included
- Aggregate metrics showing complexity and size
- Business rules and automated test case guidance
- Dataset and table dependencies with direction (input/output)
- Interactive dependency graph visualization
- Execution prerequisites and requirements

### Data management features

These details help you understand the data related to the test case. You can:

- Filter data sets by input/output direction
- Identify required artifacts for test execution
- Track data dependencies between test cases
- Monitor data set usage across test plans

###### Note

AWS Transform automatically analyzes scheduler dependencies and assigns complexity scores to help prioritize testing efforts. Higher complexity scores indicate jobs that may require more thorough testing or isolation during the testing process.

### Business rules and test case guidance

The AWS Transform test plan provides recommendations for your test case plan based on Business Rule Extraction:

- Automatic processing of business rules using LLM
- Generation of synthetic test cases
- Testing guidance for specific business scenarios
- Traceability between rules and test cases

The final test plan is stored in the specified S3 location and includes all of the necessary information to execute your testing strategy effectively. You can export the test plan for integration with other testing tools or documentation systems.

###### Note

While synthetic test case guidance is provided, the actual test artifacts must be created separately based on the guidance. The test plan serves as a comprehensive blueprint for your testing strategy but does not generate the test data or execution scripts.

### Test case creation rules - Summary

#### General rules

- A test case contains 1 to many JCLs in schedule execution order
- Test cases are created from valid supported schedulers (CA7 and Control-M)
- The test executes JCLs, not the scheduler itself or scheduled tasks
- A scheduled task is unique and executes only one JCL
- One JCL can be executed by multiple scheduled tasks
- One JCL can exist without being in a schedule

#### Default test case creation rules

- If a single JCL is in a test case:
  - JCL is not involved with a schedule
  - JCL is executed by a scheduled task that diverges into multiple branches
  - A branch in the schedule contains only this JCL

- If multiple JCL in a test case: represents a linear execution path sequence within a schedule branch
- If JCL is on a divergent scheduled task: JCL becomes its own separate test case
- If JCL is on a convergent scheduled task: JCL can start a new test case but won't be included in previous branches
- Missing JCLs are skipped and execution continues (with planned future enhancement to cut test case at missing JCL point)

#### User operations rules

- **Create Test Case**: user selects from available JCLs
  - Succeeds if JCLs exist in schedule execution branch sequence
  - Follows schedule execution order

- **Add a JCL to Test Case**: user selects from available JCLs
  - Succeeds if JCL can exist in the test case's schedule execution branch/path

- **Remove JCL from Test Case**: user can remove any JCL from a test case
  - Allowed even if it causes execution path gaps

- **Merge Test Cases**: user selects two test cases to combine
  - Succeeds if JCLs can exist together in same schedule execution branch
  - Maintains schedule execution order

- **Split Test Case**: user selects one JCL in a test case for split
  - Creates new test case from split point forward
  - Original test case modified to exclude JCLs past split point

- **Delete Test Case**: user can delete any created test case

###### Note

You cannot create, add, or merge test cases from different scheduler branches/path. A future enhancement is planned to allow operations beyond divergent/convergent tasks in the scheduler.

## Generate

test data collection scripts

You can generate JCL scripts to collect test data from your mainframe systems
based on the test plan created in the previous step. AWS Transform automatically creates
data collection scripts for datasets, database tables, and sequential files
needed for comprehensive testing. The data collection process is divided into
four main phases: input configuration, test case selection, script
configuration, and script generation.

###### To generate test data collection scripts

1. **Provide test plan input**
   1. In the left navigation pane, under **Test data collection**, choose **Provide test plan input**.
   2. Specify the S3 path to your test plan JSON file from [Plan your modernized applications testing](#transform-app-mainframe-workflow-test-planning "#transform-app-mainframe-workflow-test-planning").
   3. The input field is pre-populated if the test plan was generated in a previous job step.
   4. You can also select test plan from other jobs by specifying the appropriate S3 location.

2. **Select test cases for data collection**
   1. Review the complete list of test cases from your test plan.
   2. Filter and sort test cases based on multiple attributes:
      - Business functions and domains
      - Database table dependencies
      - Data set requirements
      - Complexity metrics
      - Custom search criteria

   3. Select individual test cases or use bulk selection options.
   4. Review test case details including entry points, metrics, and business rules by clicking on one Test Case to see details.

3. **Configure data collection scripts**
   1. Download sample templates and configuration files for reference.
      - AWS Transform provides sample templates for Db2 database unloads, VSAM file REPRO and sequential dataset processing to be used as guidance on the kinds of template expected by the process.
      - Standards may vary from site to site so the expectation is that customers will modify or replace these templates that conform to their own standards.
      - These modified templates need to be uploaded to a S3 bucket where the test data collection can process them.

   2. Provide variable configuration file (JSON format) containing:
      - User prefixes and environment-specific constants
      - Database configuration parameters
      - Destination endpoint settings and data transfer parameters
      - Other required parameters defined by user and to be used in JCL templates

   3. Upload JCL templates for different data collection methods:
      - **Db2 template**: For database table unloading (customize for BMC, IBM DSN, or other unload utilities)
      - **VSAM template**: For VSAM file processing (typically uses REPRO utility)
      - **Sequential datasets template**: For processing sequential datasets, partitioned datasets, GDGs etc.

4. **Review and manage generated scripts**

The generated scripts provide comprehensive data collection capabilities including:

    * Separate scripts for "before" and "after" test execution data collection
    * Organized script structure by test case and data type
    * Scripts are automatically stored into S3 bucket for easy access and transfer
    * Generated JCL scripts are ready for mainframe execution
    * Variable substitution is based on user configuration defined in the templates

### Script generation features

Generated scripts are automatically customized based on your templates and configuration:

- **Template-based generation**: Uses your provided JCL templates with variable substitution
- **Environment**: Incorporates your specific mainframe configuration
- **Data type handling**: Creates appropriate scripts for sequential datasets, VSAM files, and database tables
- **Collection for test cases**: Generates both "before" and "after" data collection scripts
- **Sequential dataset processing**: AWS provided sample provides for a file transfer function, but this can be customized to compression utilities available at your site or utilities such as Connect Direct or managed file transfer etc.

### Data collection strategy

The generated scripts support comprehensive data collection strategies:

- **Sequential dataset collection**: REPRO and copy utilities for VSAM and flat files
- **Database table unloading**: Customizable Db2 unload processes
- **Sequential dataset processing**: Customizable post processing of sequential datasets such as compression, managed file transfer services etc.
- **Dependency management**: Coordinated collection based on test case definition

###### Note

AWS Transform generates scripts based on your templates and configuration. Review all generated JCL before executing on your mainframe environment to ensure compatibility with your specific system configuration and security requirements.

### Template customization and best practices

ATX Test Data Collection provides flexible template customization capabilities:

- **Multi-utility support**: Adapt templates for different mainframe utilities (BMC, IBM, DSN)
- **Variable-driven configuration**: Use constants for environment-specific parameters
- **Reusable templates**: Create standardized templates for consistent script generation
- **Data handling**: Incorporate organization-specific data handling requirements
- **Security integration**: Include appropriate security and access controls
- **Performance optimization**: Configure for efficient data collection and transfer

### Generated output structure

The generated scripts are organized in your S3 bucket with the following structure:

- **Test case organization**: Scripts grouped by associated test cases
- **Collection timing**: Separate folders for "before" and "after" data collection
- **Data type classification**: Scripts organized by sequential datasets, database tables, and transfers
- **Metadata files**: Summary information and execution guidance
- **Ready-to-transfer format**: JCL formatted for direct mainframe deployment

The final script collection is stored in the specified S3 location and includes all necessary JCL to execute your data collection strategy effectively. You can download the scripts for transfer to your mainframe environment or integrate with automated deployment processes.

###### Note

While comprehensive JCL scripts are generated, actual execution must be performed on your mainframe environment. The scripts serve as ready-to-use data collection tools but require appropriate mainframe access and execution permissions.

## Test automation

script generation

You can generate test automation scripts to execute test cases on your modernized application based on the test plan created in the previous step.
AWS Transform automatically creates comprehensive test scripts that utilize the data collected from the test data collection process. The test automation script generation process
consists of three main phases: input configuration, test case selection, and script generation results.

###### To generate test scripts

1. **Provide test plan input**
   1. In the left navigation pane, under **Test automation script generation**, choose **Provide test plan input**.
   2. Specify the S3 path to your test plan JSON file from [Plan your modernized applications testing](#transform-app-mainframe-workflow-test-planning "#transform-app-mainframe-workflow-test-planning").
   3. The input field is pre-populated if the test plan was generated in a previous job step.
   4. You can also select test plan from other jobs by specifying the appropriate S3 location.
   5. The system uses this test plan as the foundation for generating automation scripts.

2. **Select test cases for script generation**
   1. Review the complete list of test cases from your test plan.
   2. Filter and sort test cases based on multiple attributes:
      - Business functions and domains
      - Database table dependencies
      - Data set requirements
      - Complexity metrics
      - Custom search criteria

   3. Select individual test cases or use bulk selection options with
      the **Check All** and **Uncheck
      All** buttons.
   4. Review test case details including entry points, metrics, and business rules by clicking on individual test cases.

   The selected test cases will have automation scripts generated for execution on the modernized application.

3. **Review and manage generated test automation scripts:**
   - The system displays a success message confirming script generation completion.
   - Generated test scripts are automatically stored in your specified S3 bucket location.
   - Access the complete list of generated test scripts with their respective S3 locations.
   - Each test case has its corresponding automation script stored in individual S3 locations.
   - Scripts are ready for deployment and execution on your modernized application environment.

### Test automation script features

The generated automation scripts provide comprehensive testing capabilities:

- **Modernized application testing**: Scripts are specifically designed to execute test cases on your transformed application
- **Data integration**: Utilizes the test data collected from the previous test data collection step, these data need to be copied to folders for each test cases
- **Automated execution**: Scripts can be used to set up data sinks, run test cases, and compare results, some parameters will have to be set according to your deployment environment
- **Organized structure**: Scripts are systematically organized by test case in your S3 bucket
- **Ready-to-deploy format**: Scripts are formatted for direct deployment to your testing environment

### Generated output structure

The generated test automation scripts are organized in your S3 bucket with the following structure:

- **Test case organization**: Each test case has its dedicated script stored in individual S3 folder
- **Execution-ready format**: Scripts are formatted for immediate deployment and execution after setting up some variable depending from your environment
- **Centralized access**: All scripts are accessible from a single S3 bucket location for easy management

### Test execution strategy

The generated scripts support comprehensive test execution workflows:

- **Environment setup**: Scripts include capabilities for setting up initial data to execute the test
- **Data preparation**: Integration with collected test data from test case data collection step
- **Test case execution**: Automated execution of individual test cases on the modernized application
- **Result comparison**: Built-in capabilities for comparing test results and validating application behavior

###### Note

AWS Transform generates test automation scripts based on your test plan and selected test cases. The scripts are designed for execution on your modernized application environment and utilize the test data collected in the previous step. Review all generated scripts before deployment to ensure compatibility with your specific application configuration and testing requirements.

### Best practices for test automation

- **Environment validation**: Ensure your modernized application environment is properly configured before script execution
- **Data verification**: Validate that the required test data from the collection phase is available and accessible
- **Script customization**: Review and customize generated scripts as needed for your specific testing requirements
- **Execution monitoring**: Implement appropriate monitoring and logging during test script execution
- **Result analysis**: Establish processes for analyzing test results and identifying application issues

The final collection of test automation scripts provides a complete testing framework for validating your modernized application functionality. The scripts can be integrated into your continuous testing processes or executed as part of your application validation workflow.

## Deployment

capabilities in AWS Transform

AWS Transform helps you set up cloud environments for modernized mainframe applications by
providing ready-to-use Infrastructure as Code (IaC) templates. Through the AWS Transform
chat interface, you can access pre-built templates that create essential components
like compute resources, databases, storage, and security controls. The templates are
available in popular formats including CloudFormation (CFN), AWS Cloud Development Kit (AWS CDK), and Terraform, giving
you flexibility to deploy your infrastructure.

These templates serve as building blocks that reduce the time and expertise needed
to configure environments for your modernized mainframe applications. You can
customize these templates to fit your needs, giving you a foundation to build your
deployment environment.

To retrieve the IaC templates, ask in the AWS Transform chat for the
Infrastructure-as-Code templates clarifying your preferred modernization pattern
(such as AWS Blu Age Refactor), your preferred topology (standalone vs high
availability), and your preferred format (CloudFormation vs Cloud Development Kit vs
Terraform).
