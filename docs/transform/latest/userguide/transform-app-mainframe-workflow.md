# Transformation of mainframe

applications

AWS Transform accelerates the transformation of your mainframe modernization applications from
COBOL to Java. The following document guides you through the process of leveraging
generative AI and the automated transformation capabilities of AWS Transform for analyzing
codebases, planning transformation, and executing the refactored code in an accelerated
manner. All of this while preserving your mission-critical business logic.

###### Topics

- [Prerequisite: Prepare code in S3](#transform-app-mainframe-workflow-prereq "#transform-app-mainframe-workflow-prereq")
- [Step 1: Sign-in and
  onboarding](#transform-app-mainframe-workflow-signin "#transform-app-mainframe-workflow-signin")
- [Step 2: Create and
  start a job](#transform-app-mainframe-workflow-start-job "#transform-app-mainframe-workflow-start-job")
- [Step 3: Set up a
  connector](#transform-app-mainframe-workflow-setup-connector "#transform-app-mainframe-workflow-setup-connector")
- [Step 4: Tracking
  transformation progress](#transform-app-mainframe-workflow-track-progress "#transform-app-mainframe-workflow-track-progress")
- [Step 5: Analyze
  code](#transform-app-mainframe-workflow-code-analysis "#transform-app-mainframe-workflow-code-analysis")
- [Step 6:
  Generate technical documentation](#transform-app-mainframe-workflow-generate-documentation "#transform-app-mainframe-workflow-generate-documentation")
- [Step 7: Extract
  business logic](#transform-app-mainframe-workflow-extract-business-logic "#transform-app-mainframe-workflow-extract-business-logic")
- [Step 8:
  Decomposition](#transform-app-mainframe-workflow-decomposition "#transform-app-mainframe-workflow-decomposition")
- [Step 9: Migration
  wave planning](#transform-app-mainframe-workflow-wave-planning "#transform-app-mainframe-workflow-wave-planning")
- [Step 10: Refactor
  code](#transform-app-mainframe-workflow-refactor-code "#transform-app-mainframe-workflow-refactor-code")
- [Step 11: Re-run the job](#transform-app-mainframe-workflow-rerun-job "#transform-app-mainframe-workflow-rerun-job")
- [Step 12: Deployment
  capabilities in AWS Transform](#transform-app-mainframe-features-deployment "#transform-app-mainframe-features-deployment")

## Prerequisite: Prepare code in S3

AWS Transform is capable of handling complex mainframe codebases. To use this codebase,
make sure you have all the assets in your S3 location.

- **Source code:** You must upload your
  mainframe source code files to S3. This includes COBOL programs, JCL
  scripts, copybooks, and any other relevant source files.
- **Data files**: If you have any VSAM files or
  other data files that your mainframe applications use, these need to be
  uploaded to S3.
- **Configuration files**: Any configuration
  files specific to your mainframe environment should be included.
- **Documentation**: If you have any existing
  documentation about your mainframe applications or systems, it's helpful to
  upload them to S3.

###### Note

    + For technical documentation generation, you can leverage an optional
     configuration file to generate PDF documents which aligns with your
     required formats and standards, including headers, footers, logos, and
     customized information.
    + AWS Transform leverages automation with Generative AI for documentation generation
     and business rule extraction. Including a glossary CSV file with
     information about important abbreviations and terminologies in the root
     directory of your zip file will help improve the generated documentation
     quality.

- **Test data**: If available, upload any test
  data sets that can be used to validate the modernized application.

## Step 1: Sign-in and

onboarding

To sign into the AWS Transform web experience, follow all the instructions in [Getting started with AWS Transform](getting-started.md "getting-started.md") section of the documentation.

When setting up your workspace for mainframe transformation, you can optionally
set up an Amazon S3 bucket to be used with the S3 connector. After creating the bucket
and uploading the desired input files into the bucket, save that S3 bucket ARN for
use later. Or you can set up the S3 bucket when setting up the connector as well.
For more information, see [Step 3: Set up a
connector](#transform-app-mainframe-workflow-setup-connector "#transform-app-mainframe-workflow-setup-connector").

###### Important

AWS Transform will refuse operations from you if you don’t have the proper
permissions. For example, a contributor cannot cancel a job transformation of
mainframe applications or delete a job. Only an administrator can perform these
functions.

## Step 2: Create and

start a job

Follow these steps to start a new job in your workspace.

1. On your workspace landing page, choose **Ask AWS Transform to create a
   job**.
2. Next, choose **Mainframe Modernization** as
   the type of job.
3. In the chat window, AWS Transform will ask you to confirm the job details, such
   as, the job type, job name, and what steps you want this job to
   perform.

###### Note

You can ask AWS Transform to perform any combination of the capabilities
mentioned in [High-level
walkthrough](transform-app-mainframe.md#transform-app-mainframe-highlevel-walkthrough "transform-app-mainframe.md#transform-app-mainframe-highlevel-walkthrough"). But you
always need to finish the **Analyze code**
step. 4. Once confirmed, choose **Create job**.

AWS Transform then kicks off the modernization for your job.

## Step 3: Set up a

connector

In this step, you set up a connector with your Amazon S3 bucket, which allows AWS Transform to
access resources, and perform consecutive transformation functions.

1. Under job plan, expand **Kick off modernization**, and
   choose **Connect to AWS account**.

###### Note

You directly skip to **Specify resource
location** page if you have already created a connector and
added S3 bucket when creating your workspace. 2. Enter the AWS account ID you would like to use to perform the mainframe
modernization capabilities. 3. Choose **Next**. 4. Enter the Amazon S3 bucket ARN from earlier where your resources are stored for
transformation of your mainframe applications. 5. Choose **Create connector**. 6. Once you add the Amazon S3 bucket ARN, you will get a verification link. You must share
this link with your AWS administrator, and ask them to approve the request in the
AWS Management Console. After the request is approved, you will see connection details with Amazon S3
as the connector type.

###### Note

If you need to create a different connector, you can choose to restart the set
up connector process. 7. When your connector is set to active, on the **Specify
asset location** page, enter the Amazon S3 bucket path for the input
resources you would like to transform for your mainframe applications. 8. (Optional) You can also choose to enable AWS Transform chat to learn from the
progress you make on this job. This will allow AWS Transform to assist you with
better guidance and result generation in each step. This data will only be
stored within your workspace and will not be used for any other purposes
beyond this job. If you disable this experience, AWS Transform chat will guide you
based in the publicly available information in AWS Documentation. 9. Then, choose **Continue** to move to the next step.

###### Important

Your data will be stored and persisted in the AWS Transform's artifact store in your
workspace and will only be used for running the job.

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
            "https://*.transform.eu-central-1.on.aws",
            "https://*.transform.us-east-1.on.aws"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 0
    }
]
```

## Step 4: Tracking

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

## Step 5: Analyze

code

After you share the Amazon S3 bucket path with AWS Transform, it will analyze the code
for each file with details such as file name, file type, lines of code, and their
paths.

###### Note

You can download the Analyze code results using the **Download** link in the left navigation pane. This will download a
zip file that contains the classification file for manual classification
workflow, assets, dependencies JSON file, and list of missing files.

Under **Analyze code** in the left navigation
pane, choose **View code analysis results**.

You can
view your code analysis results in multiple ways:

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

## Step 6:

Generate technical documentation

In this step, you can generate technical documentation for your mainframe
applications undergoing modernization. By analyzing your code, AWS Transform can
automatically create detailed documentation of your application programs, including
descriptions of the program logic, flows, integrations, and dependencies present in
your legacy systems. This documentation capability helps bridge the knowledge gap,
enabling you to make informed decisions as you transition your applications to
modern cloud architectures.

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

### Add user information into the documentation with user’s glossary file, a

pdf configuration file and user logo files

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
3. Select the external link element next to the PDF.

The PDF will open in a new browser tab for you to access and read.

###### Note

AWS Transform also gives you the ability to download either an XML of PDF version of the generated technical documentation.

###### Important

If you're having issues with documentation inline viewer, make sure that
the S3 bucket is set up correctly. For more information on S3 bucket's CORS
policy, see [S3 bucket
CORS permissions](#transform-app-mainframe-workflow-setup-connector-s3 "#transform-app-mainframe-workflow-setup-connector-s3").

## Step 7: Extract

business logic

In this step, you can extract essential business logic from your mainframe
applications that are undergoing modernization. AWS Transform automatically analyzes your code to
identify and document critical business elements, including detailed process flows,
and business logic that is embedded in your applications. This capability serves
multiple stakeholders in your modernization journey. Business analysts can leverage
extracted logic to create precise business requirements and identify gaps or
inconsistencies in current implementations. Developers gain the ability to quickly
comprehend complex legacy system functionality without extensive mainframe
expertise.

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

### Add user information into the documentation with user’s glossary

file

```
ARTIFACT_ID.zip
└── app/
    ├── File1.CBL
    ├── File2.JCL
    ├── subFolder/
    │   └ File3.CBL
└── glossary.csv
└ ...
```

**glossary.csv file**: You can choose to provide
and upload an optional glossary in the zip file in the source S3 bucket. Save the glossary as a CSV file named _glossary.csv_. The glossary helps creating documentation with relevant
descriptions using the customer's vocabulary. A sample
`glossary.csv` file looks like:

```
LOL,Laugh out loud
ASAP,As soon as possible
WIP,Work in progress
SWOT,"Strengths, Weaknesses, Opportunities and Threats"
```

### View the extracted business documentation inline

You can view the business logic in the Extract business rule step. To do
this,

1. Navigate to **Review business logic extraction results**.
2. Select the document you want to view from the table, and then click the **View result** button.

The business documentation page opens in a new browser tab.

## Step 8:

Decomposition

In this step, you decompose your code into domains that account for dependencies
between programs and components. This helps the related files and programs to be
grouped appropriately within the same domain. It also helps maintain the integrity
of the application logic during the decomposition process.

1. Expand **Decompose code** from the left
   navigation pane.
2. Choose **Decompose into domains**.

###### Note

Two domains (unassigned and disconnected) are automatically created
initially by the application. Unassigned domain is strictly under
decomposition control and cannot be edited. 3. Create a new domain by choosing **Create domain** from
the AWS Transform prompt (for first domain only), or from under
**Actions** menu. 4. In **Create domain**, provide domain name,
optional description, and mark some files as seeds. Seeds are elements that
are labeled with business features or functions for AWS Transform to group related
components into domains. For more information about seeds, see [Seeds](#transform-app-mainframe-workflow-decomposition-seeds "#transform-app-mainframe-workflow-decomposition-seeds").

CICS configured files (CSD) and scheduler configured files (SCL) can be
used for automatic seed detection.

###### Note

You can also set one domain only as a common component. The files in
this domain are common to multiple domains. 5. Choose **Create**.

###### Note

You can create multiple domains with different files as seeds. 6. After confirming all domains and seeds, choose
**Decompose**. 7. AWS Transform will check the source code files and then decompose into domains
with programs and data sets with similar use cases and high programming
dependencies.

AWS Transform gives you a tabular and graph view of decomposed domains as
dependencies. Graph view has two options:

    * **Domain view** – Can view how
     different domains are related to each other in visual format.
    * **Dependency view** – Can view
     all files in each domain as a complex dependency graph. If a node
     that was added to a domain didn't receive information from a seed in
     the same domain, then this node will either be predicted into
     unassigned (node didn't receive any information), disconnected (in a
     sub graph that didn't receive seed information) or into another
     domain (node received information from at least that domain).

Repeat these steps to add more domains or to reconfigure your already
created domains with a different set of seeds if you don’t like current
domain structure. 8. When completed, choose **Continue**.

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

## Step 9: Migration

wave planning

Based on the domains you created in the previous step, AWS Transform generates a migration
wave plan with recommended modernization order.

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

## Step 10: Refactor

code

In this step, AWS Transform refactors the code in all or selected domain files into Java
code. The goal of this step is to preserve the critical business logic of your
application while refactoring it to a modernized cloud-optimized Java
application.

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

### Reforge code

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

## Step 11: Re-run the job

With re-run capabilities you can restart an in-progress job, re-run a previously completed job, or modify job objectives. When you initiate a re-run through
either the **re-run** button or the chat interface, you can choose to restart the entire
job plan or select specific steps to re-run. AWS Transform automatically retains the
results of completed steps from the previous run, except those for dependent steps,
which also run again. For example:

- If you choose to re-run **Analyze code**, all of the other steps
  are also re-run.
- If you only re-run **Generate technical documentation** or
  **Extract business logic**, other steps are
  not re-run.
- If you re-run **Decomposition**, then **Migration wave planning** and **Refactor
  code** are also rerun.

###### Note

When a rerun has been initiated for any step, AWS Transform compares
the source code used during the analysis step in the original
job with the source code currently available in the resource location
specified when the job was created. If AWS Transform finds that the source code has
been updated then it requires the **Analyze
code** step, which necessitates a re-run of all of the subsequent
steps.

You can download certain assets to preserve progress. For example, you can
download the classification file from the **Analyze
code** step to retain manual classifications. In the **Decomposition** step, you can download dependency updates,
and domain and seed files, to retain previously created domains. This allows for a
more iterative approach, enabling you to refine your work as needed throughout the
transformation process. Be careful about using artifacts from previous jobs if the
source code has been updated as this can introduce inconsistencies to the
job.

When all the steps are successfully completed the left navigation pane displays each
job task completed in green.

## Step 12: Deployment

capabilities in AWS Transform

AWS Transform helps you set up cloud environments for modernized mainframe applications by
providing ready-to-use Infrastructure as Code (IaC) templates. Through the AWS Transform
chat interface, you can access pre-built templates that create essential components
like compute resources, databases, storage, and security controls. The templates are
available in popular formats including AWS CloudFormation (CFN), AWS Cloud Development Kit (AWS CDK), and Terraform, giving
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
