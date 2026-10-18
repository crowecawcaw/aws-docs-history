

# Exporting a penetration test report
<a name="export-penetration-report"></a>

Exporting a penetration test report generates a downloadable PDF record of your test results. Use the report to preserve test evidence and share findings with stakeholders. For example, you can share it with an auditor or attach it to an internal risk assessment record.

The report does not establish compliance or certification. Your auditor determines whether the report and your supporting records satisfy your organization’s audit requirements.

## Understanding compliance-ready reports
<a name="compliance-ready-report"></a>

Use a compliance-ready report when you need to give an auditor structured evidence of your penetration testing. The report records when and how you tested, what you tested, what you found, and how your organization responded. You can use it as supporting evidence for audits under these frameworks:
+ The American Institute of Certified Public Accountants (AICPA) Trust Services Criteria for System and Organization Controls (SOC) 2
+ International Organization for Standardization and International Electrotechnical Commission (ISO/IEC) 27001:2022
+ The Health Insurance Portability and Accountability Act (HIPAA) Security Rule

These frameworks do not require a specific penetration test report. They define control outcomes rather than a required report format. Use the report as one source of evidence within your organization’s broader control program.

For framework requirements, see the [AICPA Trust Services Criteria](https://us.aicpa.org/content/dam/aicpa/interestareas/frc/assuranceadvisoryservices/downloadabledocuments/trust-services-criteria.pdf), [ISO/IEC 27001](https://www.iso.org/standard/27001), and [45 CFR 164.308](https://www.ecfr.gov/current/title-45/section-164.308).

### Mapping report evidence to control areas
<a name="_mapping_report_evidence_to_control_areas"></a>

The following table explains how auditors can use report evidence. It does not replace the framework requirements or your auditor’s judgment.


| Framework and control areas | What an auditor evaluates | Relevant report evidence | 
| --- | --- | --- | 
| AICPA Trust Services Criteria for SOC 2: CC4.1, CC7.1, and CC7.4–CC7.5 | Whether your organization evaluates controls, identifies vulnerabilities, and tracks corrective action. For a Type II examination, the auditor also evaluates whether evidence falls within the examination period. | The test window, scope, methodology, findings, severity ratings, proof-of-concept, and reproduction steps. Reviewer annotations can document your response when you include them. Pair the report with remediation and revalidation records. | 
| ISO/IEC 27001:2022: A.8.8, A.8.25, and A.8.29 | Whether your organization uses planned and documented processes to identify and manage technical vulnerabilities and perform security testing during development and acceptance. | The test scope, four-phase methodology, tester-independence statement, vulnerability coverage, findings, and reproduction evidence. Pair the report with your risk-treatment and remediation records. | 
| Health Insurance Portability and Accountability Act (HIPAA) Security Rule: 45 CFR 164.308(a)(1)(ii)(A), 164.308(a)(1)(ii)(B), and 164.308(a)(8) | Whether your organization performs an accurate and thorough risk analysis, manages identified risks, and periodically evaluates its safeguards. | The assessment boundary, test window, findings, severity ratings, and evidence. Pair the report with records of mitigation decisions and follow-up evaluation. | 

Neither SOC 2, ISO/IEC 27001:2022, nor the HIPAA Security Rule explicitly requires a penetration test. A penetration test report can provide evidence for the control areas in the table when its scope and timing match the audited system and period.

### Reviewing the compliance-ready report contents
<a name="_reviewing_the_compliance_ready_report_contents"></a>

The following list describes the content added when you turn on **Generate a compliance-ready report**:
+  **About this report** — Explains that the report provides supporting evidence for security-testing and vulnerability-management controls. It also states the report’s compliance limits.
+  **Methodology** — Describes the four-phase testing methodology: preflight, static analysis, penetration testing, and finalizing.
+  **Tester independence** — Identifies AWS Security Agent as an automated third-party testing service that operates independently from the tested system’s builders and operators.
+  **Test window** — Shows when the engagement occurred so you can align the evidence with an audit or examination period.
+  **Vulnerability coverage** — Lists the vulnerability classes in scope and groups them by category. For a web application test scope, coverage aligns with the Open Worldwide Application Security Project (OWASP) Top 10 for web applications.
+  **Confidentiality** — Marks the report as confidential. You can share it with your auditors and assessors under confidentiality.

The **Tasks Executed** section records the tests performed during the engagement. The vulnerability coverage appendix describes classes in scope; it does not state that AWS Security Agent tested every class against every endpoint.

AWS Security Agent is not a professional penetration testing service, a Payment Card Industry Qualified Security Assessor (QSA), or an Approved Scanning Vendor (ASV). The report is not a Payment Card Industry Data Security Standard (PCI DSS) 11.4 penetration test deliverable. It is also not a Federal Risk and Authorization Management Program (FedRAMP) penetration test deliverable.

### Preparing evidence for an auditor
<a name="_preparing_evidence_for_an_auditor"></a>

Before you share a report, confirm that the evidence matches the audit request:
+ Make sure that the target URLs, connected resources, and exclusions match the audited system boundary.
+ Make sure that the test window falls within the period your auditor requested.
+ Include the severities, confidence levels, statuses, and finding types your auditor expects.
+ Document who authorized the test and why the tester was appropriate.
+ Include records that show how you handled each applicable finding.
+ Include revalidation results or other follow-up evidence when your auditor requests them.
+ Follow your organization’s confidentiality requirements when sharing and storing the report.

The report provides point-in-time test evidence. Your vulnerability-management process supplies the management response, remediation ownership, exceptions, and ongoing control evidence that an auditor may also request.

### Including annotation notes
<a name="include-annotation-notes"></a>

Turn on **Include annotation notes** to add each reviewer’s annotation to its finding. Use annotations to capture context such as risk justification, triage decisions, accepted-risk rationale, or remediation status.

The report separates annotation notes added by the tested organization from the agent’s assessment. For information about adding an annotation, see [Edit findings](review-penetration-findings.md#edit-findings).

## Preparing to export a report
<a name="export-penetration-report-prerequisites"></a>

Confirm that you have access to the AWS Security Agent web application and permission to view the penetration test run. A completed run provides the final test window and findings. You can also export an in-progress run when you need an interim record.

For information about running a test, see [Create a penetration test](perform-penetration-test.md). For information about interpreting findings, see [Review findings from a penetration test](review-penetration-findings.md).

## To open the Generate report dialog
<a name="step-1-open-the-generate-report-dialog"></a>

Open the dialog when you need to export a completed or in-progress penetration test run:

1. Log in to the AWS Security Agent web application.

1. Navigate to **Penetration tests**.

1. Choose the penetration test run that you want to export.

1. In the toolbar, choose **Generate report**.

## Choosing findings to include
<a name="step-2-choose-which-findings-to-include"></a>

Filter findings to focus on the issues relevant to your review and reduce generation time for large reports. The following table lists the available filters and the findings they include.


| Filter | Findings included | 
| --- | --- | 
| Risk levels | Findings with the selected severity levels: Critical, High, Medium, Low, or Informational. | 
| Confidence levels | Findings with the selected agent-confidence levels: High, Medium, or Low. | 
| Finding status | Findings with the selected workflow statuses. | 
| Finding types | Security findings, requirement violations, or both. | 

A report with many findings might take several minutes to generate. If the report is large, narrow the risk level or finding type filters first. For information about severity levels, see [Understanding severity and CVSS scores](severity-and-cvss.md).

## To generate and download the report
<a name="step-4-generate-and-download-the-report"></a>

Generate the report when you need to share findings or preserve evidence for remediation and audit review. This procedure downloads the findings that match your filters. After you confirm the filters, complete the following steps:

1. Review your filter selections.

1. (Optional) Turn on **Generate a compliance-ready report**.

1. (Optional) Turn on **Include annotation notes**.

1. Choose **Generate and download**.

For details about these options, see [Understanding compliance-ready reports](#compliance-ready-report) and [Including annotation notes](#include-annotation-notes).

Your report downloads as a PDF file. A large report might take several minutes to generate.

## After you download the report
<a name="export-penetration-report-next-steps"></a>

After downloading the report, you can take these actions:
+ Share the report with stakeholders or your auditor according to your organization’s confidentiality requirements.
+ Track a finding in Jira. See [Export findings to an issue tracker](export-findings-to-issue-tracker.md).
+ Revalidate a finding after you deploy a fix. See [Revalidate findings](revalidate-findings.md).