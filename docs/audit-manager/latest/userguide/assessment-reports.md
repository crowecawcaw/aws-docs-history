# Assessment reports

An _assessment report_ summarizes the selected evidence
that was collected for an assessment. It also contains links to PDF files with details about
each piece of evidence. The specific contents, organization, and naming convention of an
assessment report depend on the parameters that you choose when you [generate the
report](generate-assessment-report.md "generate-assessment-report.md").

Assessment reports help you to select and compile the evidence that's relevant for your
audit. However, they don't assess the compliance of the evidence itself. Instead, Audit Manager simply
provides the selected evidence details as an output that you can share with your auditor.

###### Contents

- [Understanding the assessment report folder structure](assessment-reports.md#assessment-report-folder-structure "assessment-reports.md#assessment-report-folder-structure")
- [Navigating an assessment report](assessment-reports.md#assessment-report-how-to-navigate "assessment-reports.md#assessment-report-how-to-navigate")
- [Reviewing the sections of an assessment report](assessment-reports.md#assessment-report-sections "assessment-reports.md#assessment-report-sections")
  - [Cover page](assessment-reports.md#assessment-report-cover-page "assessment-reports.md#assessment-report-cover-page")
  - [Overview page](assessment-reports.md#assessment-report-overview "assessment-reports.md#assessment-report-overview")
    - [Report summary](assessment-reports.md#assessment-report-overview-summary "assessment-reports.md#assessment-report-overview-summary")
    - [Assessment summary](assessment-reports.md#assessment-report-overview-assessment-summary "assessment-reports.md#assessment-report-overview-assessment-summary")

  - [Table of contents page](assessment-reports.md#assessment-report-toc "assessment-reports.md#assessment-report-toc")
  - [Control page](assessment-reports.md#assessment-report-control "assessment-reports.md#assessment-report-control")
    - [Control summary](assessment-reports.md#assessment-report-control-summary "assessment-reports.md#assessment-report-control-summary")
    - [Collected evidence](assessment-reports.md#assessment-report-selection "assessment-reports.md#assessment-report-selection")

  - [Evidence summary page](assessment-reports.md#assessment-report-evidence-summary "assessment-reports.md#assessment-report-evidence-summary")
  - [Evidence detail page](assessment-reports.md#assessment-report-evidence-detail "assessment-reports.md#assessment-report-evidence-detail")

- [Validating an assessment report](assessment-reports.md#assessment-report-integrity "assessment-reports.md#assessment-report-integrity")
- [Additional resources](assessment-reports.md#troubleshooting-assessment-reports "assessment-reports.md#troubleshooting-assessment-reports")

## Understanding the assessment report folder structure

When you download an assessment report, Audit Manager produces a zip folder. This contains your
assessment report and related evidence files in nested subfolders.

The zip folder is structured as follows:

- **Assessment folder** (example:
  `myAssessmentName-a1b2c3d4`) – The root folder.
  - **Assessment report folder** (example:
    `reportName-a1b2c3d4e5f6g7`) – A subfolder where you can find the
    AssessmentReportSummary.pdf, digest.txt, and README.txt files.
    - **Evidence by control folder** (example:
      `controlName-a1b2c3d4e5f6g`) – A subfolder that groups
      evidence files by the related control.
      - **Evidence by data source folder** (example:
        `CloudTrail`, `Security Hub CSPM`) – A subfolder that groups
        evidence files by the data source type.
        - **Evidence by date folder** (example:
          `2022-07-01` ) – A subfolder that groups evidence
          files by the evidence collection date.
          - **Evidence files** – The files
            that contain details about individual pieces of evidence.

## Navigating an assessment report

Start by opening the zip folder and navigating one level down to the assessment report
folder. Here, you can find the assessment report PDF and the README.txt file.

You can review the README.txt file to understand the structure and the contents of the zip
folder. It also provides reference information about the naming conventions for each file.
This information can help you navigate directly to a subfolder or evidence file if you’re
looking for a specific item.

Otherwise, to browse evidence and locate the information that you need, open the
assessment report PDF. This gives you a high-level overview of the report, and a summary of
the assessment that the report was created from.

Next, use the table of contents (TOC) to explore the report. You can choose any
hyperlinked control in the TOC to jump directly to a summary of that control.

When you're ready to review evidence details for a control, you can do so by choosing the
hyperlinked evidence name. For automated evidence, the hyperlink opens a new PDF file with
details about that evidence. For manual evidence, the hyperlink takes you to the S3 bucket
that contains the evidence.

###### Tip

The breadcrumb navigation at the top of each page shows your current location in the
assessment report as you browse controls and evidence. Select the hyperlinked TOC to
navigate back to the TOC at any time.

## Reviewing the sections of an assessment report

Use the following information to learn more about each section of an assessment
report.

###### Note

When you see a hyphen (-) next to any of the attributes in the following sections, this
indicates that the value of that attribute is null, or a value doesn't exist.

- [Cover page](#assessment-report-cover-page "#assessment-report-cover-page")
- [Overview page](#assessment-report-overview "#assessment-report-overview")
- [Table of contents page](#assessment-report-toc "#assessment-report-toc")
- [Control page](#assessment-report-control "#assessment-report-control")
- [Evidence summary page](#assessment-report-evidence-summary "#assessment-report-evidence-summary")
- [Evidence detail page](#assessment-report-evidence-detail "#assessment-report-evidence-detail")

### Cover page

The cover page includes the name of the assessment report. It also displays the date and
time that the report was generated, along with the account ID of the user who generated the
report.

The cover page is formatted as follows. Audit Manager replaces the
`placeholders` with the information that's relevant to your
report.

```
`Assessment report name`
Report generated on `MM/DD/YYYY` at `HH:MM:SS AM/PM UCT` by `AccountID`
```

### Overview page

The overview page has two parts: a summary of the report itself, and a summary of the
assessment that's being reported on.

#### Report summary

This section summarizes the assessment report.

| Name                            | Description                                                                                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Report name**                 | The name of the report.                                                                                                                                                   |
| **Description**                 | The description that's entered by the audit owner when they generate the<br>report.                                                                                       |
| **Date generated**              | The date when the report was generated. The time is represented in<br>Coordinated Universal Time (UTC).                                                                   |
| **Total controls included**     | The number of controls that are included in the report and have collected<br>evidence. This is a subset of the total number of controls in the<br>assessment.             |
| **AWS accounts included**       | The number of AWS accounts that are included in the report and have<br>collected evidence. This is a subset of the total number of AWS accounts in<br>the assessment.     |
| **Assessment report selection** | The number of evidence items that are selected for inclusion in the report.<br>This includes the total number of compliance check issues that are found in the<br>report. |

#### Assessment summary

This section summarizes the assessment that the report relates to.

| Name                      | Description                                                                       |
| ------------------------- | --------------------------------------------------------------------------------- |
| **Assessment name**       | The name of the assessment that the report was generated from.                    |
| **Status**                | The status of the assessment at the time when the report was<br>generated.        |
| **Assessnent Region**     | The AWS Region that the assessment was created in.                                |
| **AWS accounts in scope** | The list of AWS accounts that are in the scope of the assessment.                 |
| **Framework name**        | The name of the framework that the assessment was created from.                   |
| **Audit owners**          | The user or role of the assessment's audit owners.                                |
| **Last updated**          | The date when the assessment was last updated. The time is represented in<br>UTC. |

### Table of contents page

The TOC displays the full contents of the assessment report. The contents are grouped
and organized based on the control sets that are included in the assessment. Controls are
listed underneath their respective control set.

Choose any item in the table of contents to navigate directly to that section of the
report. You can either choose a control set or go directly to a control.

### Control page

The control page has two parts: a summary of the control itself, and a summary of the
evidence that was collected for the control.

#### Control summary

This section includes the following information.

| Name                            | Description                                                                                                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Control name**                | The name of the control.                                                                                                                                                                                 |
| **Description**                 | The description of the control.                                                                                                                                                                          |
| **Control set**                 | The name of the control set that the control belongs to.                                                                                                                                                 |
| **Testing information**         | The recommended testing procedures for this control.                                                                                                                                                     |
| **Action plan**                 | The recommended actions to perform if the control isn't fulfilled.                                                                                                                                       |
| **Assessment report selection** | The number of evidence items related to this control that were included in<br>the assessment report. This includes the number of compliance check issues that<br>were found for this control's evidence. |

#### Collected evidence

This section shows the evidence that was collected for the control. The evidence is
grouped by folders, which are organized and named by the evidence collection date. Next to
each evidence folder name is the total number of compliance check issues for that
folder.

Underneath each evidence folder name is a list of hyperlinked evidence names.

- Automated evidence names start with an evidence collection timestamp, followed by
  the service code, event name (up to 20 characters), account ID, and a unique
  12-character unique ID.

For example:
`21-30-24_IAM_CreateUser_111122223333_a1b2c3d4e5f6`

For automated evidence, the hyperlinked name opens a new PDF file with a summary
and further details.

- Manual evidence names start with an evidence upload timestamp, followed by the
  `manual` label, account ID, and a 12-character unique ID. They also
  include the first 10 characters of the file name, and the file extension (up to 10
  characters).

For example:
`00-00-00_manual_111122223333_a1b2c3d4e5f6_myimage.png`

For manual evidence, the hyperlinked name takes you to the S3 bucket that contains
that evidence.

Next to each evidence name is the result of the compliance check for that item.

- For automated evidence that's collected from AWS Security Hub CSPM or AWS Config, a
  **Compliant**, **Non-compliant**, or
  **Inconclusive** result is reported.
- For automated evidence that's collected from AWS CloudTrail and API calls, and for all
  manual evidence, an **Inconclusive** result is shown.

### Evidence summary page

The evidence summary page includes the following information.

| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ID**                      | The unique identifier for the evidence.                                                                                                                                                                                                                                                                                                                                                                                              |
| **Date collected**          | The date when the evidence was created or uploaded.                                                                                                                                                                                                                                                                                                                                                                                  |
| **Description**             | A description of the evidence, including the account ID and the data source<br>type.                                                                                                                                                                                                                                                                                                                                                 |
| **Assessment name**         | The name of the assessment that the report was generated from.                                                                                                                                                                                                                                                                                                                                                                       |
| **Framework name**          | The name of the framework that the assessment was created from.                                                                                                                                                                                                                                                                                                                                                                      |
| **Control name**            | The name of the control that the evidence supports.                                                                                                                                                                                                                                                                                                                                                                                  |
| **Control set name**        | The name of the control set that the related control belongs to.                                                                                                                                                                                                                                                                                                                                                                     |
| **Control description**     | The description of the control that the evidence supports.                                                                                                                                                                                                                                                                                                                                                                           |
| **Testing information**     | The recommended testing procedures for the control.                                                                                                                                                                                                                                                                                                                                                                                  |
| **Action plan**             | The recommended actions to perform if the control is not fulfilled.                                                                                                                                                                                                                                                                                                                                                                  |
| **AWS Region**              | The name of the Region that's associated with the evidence.                                                                                                                                                                                                                                                                                                                                                                          |
| **IAM ID**                  | The ARN of the user or role that's associated with the evidence.                                                                                                                                                                                                                                                                                                                                                                     |
| **AWS account**             | The AWS account ID that's associated with the evidence.                                                                                                                                                                                                                                                                                                                                                                              |
| **AWS service**             | The name of the AWS service that's associated with the evidence.                                                                                                                                                                                                                                                                                                                                                                     |
| **Event name**              | The name of the evidence event.                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Event time**              | The time when the evidence event occurred.                                                                                                                                                                                                                                                                                                                                                                                           |
| **Data source**             | Where the evidence was collected or uploaded from. The data source type can be<br>either AWS Config, Security Hub CSPM, AWS API calls, CloudTrail, or Manual.                                                                                                                                                                                                                                                                        |
| **Evidence by type**        | The category of the evidence<br>• _Compliance check_ evidence is collected<br>from AWS Config or Security Hub CSPM.<br>• _User activity_ evidence is collected<br>from CloudTrail logs.<br>• _Configuration data_ evidence is<br>collected from snapshots of other AWS services.<br>• _Manual_ evidence is evidence that you<br>upload manually.                                                                                     |
| **Compliance check status** | The evaluation status for evidence that falls under the _compliance check<br>• category.<br>• For automated evidence that's collected from AWS Security Hub CSPM or AWS Config, a<br>**Compliant**, **Non-compliant**, or<br>\*\*Inconclusive_<br>• result is reported.<br>• For automated evidence that's collected from AWS CloudTrail and API calls, and<br>for all manual evidence, an \*_Inconclusive_<br>• result is<br>shown. |

### Evidence detail page

The evidence detail page shows the name of the evidence and an evidence detail table.
This table provides a detailed breakdown of each element of the evidence so that you can
understand the data and validate that it's correct. Depending on the data source of the
evidence, the contents of the evidence detail page vary.

###### Tip

The breadcrumb navigation at the top of each page shows your current location as you
browse evidence details. Select **Evidence summary** to navigate back to
the evidence summary at any time.

## Validating an assessment report

When you generate an assessment report, Audit Manager produces a report file checksum called
`digest.txt`. You can use this file to validate the integrity of the report and
ensure that no evidence was modified after the report was created. It contains a JSON object
with signatures and hashes that are invalidated if any part of the report archive is altered.

To validate the integrity of an assessment report, use the [ValidateAssessmentReportIntegrity](../APIReference/API_ValidateAssessmentReportIntegrity.md "../APIReference/API_ValidateAssessmentReportIntegrity.md") API that's provided by Audit Manager.

## Additional resources

To find answers to common questions and issues, see [Troubleshooting assessment report issues](assessment-report-issues.md "assessment-report-issues.md") in the
_Troubleshooting_ section of this guide.
