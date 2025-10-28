# Reviewing Detective Investigations reports

Investigations reports lets you review the generated **Reports** for
investigations that you have run previously in Detective.

To review investigations reports

1. Sign in to the AWS Management Console. Then open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Investigations**.
   Take note of the following attributes from an investigations report.

- ID – The generated identifier of the
  investigations report. You can choose this **ID** to read a
  summary of the investigation report, which has the details of the
  investigation.
- Status – Each investigation is
  associated with a **Status** based on the completion status
  of the investigation. Status values can be **In
  progress**,
  **Succeeded**, or
  **Failed**.
- Severity – Each investigation is
  assigned a **Severity**. Detective automatically assigns a severity
  to the finding.

A severity represents the disposition as analyzed by the investigation of a single
resource at a given scope time. A severity reported by an investigation doesn't
imply or otherwise indicate the criticality or importance that an affected
resource might have for your organization.

Investigation severity values can be **Critical**,
**High**, **Medium**,
**Low**, or **Informational** from most to
least severe.

Investigations that are assigned a Critical or High severity value should be prioritized for further inspection, as they are more likely to represent high-impact security issues identified by Detective.

- Entity – The **Entity**
  column contains details on the specific entities detected in the
  investigation. Some entities are AWS accounts, such as user and role.
- Status – The
  **Creation** date column contains details on the date and
  time the investigation report was first created.
