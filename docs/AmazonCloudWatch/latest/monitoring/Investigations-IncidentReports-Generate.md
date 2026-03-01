# Generate a report from an investigation

You can generate incident reports from in-progress or completed investigations.
Incident reports generated early in an investigation may not include key facts such as
root causes and recommended actions. When the investigation is active you can edit the
facts available to supplement the investigation with additional information. After the
investigation is ended, you can't edit or add facts to the investigation.

**Prerequisites**

Before generating an incident confirm the following requirements are met:

- Ensure the investigation group uses the required KMS key and has appropriate
  IAM policies attached to its role for decrypting data from AWS services. If
  your AWS resources are encrypted with customer-managed KMS keys, you must add
  IAM policy statements to the investigation group role to grant CloudWatch
  Investigations the permissions needed to decrypt and access this data.
- Investigation group role has been granted the following permissions:
  - `aiops:GetInvestigation`
  - `aiops:ListInvestigationEvents`
  - `aiops:GetInvestigationEvent`
  - `aiops:PutFact`
  - `aiops:UpdateReport`
  - `aiops:CreateReport`
  - `aiops:GetReport`
  - `aiops:ListFacts`
  - `aiops:GetFact`
  - `aiops:GetFactVersions`

###### Note

You can add these permissions as an inline policy to the investigation
group role, or attach an additional permissions policy to investigation
group role. For more information see, [Permissions for incident report generation](Investigations-Security.md#Investigations-Security-IAM-IRG "Investigations-Security.md#Investigations-Security-IAM-IRG").

The new managed policy `AIOpsAssistantIncidentReportPolicy`
provides the required permissions and is automatically added to
investigation groups created after October 10, 2025. For more information,
see [AIOpsAssistantIncidentReportPolicy](managed-policies-cloudwatch.md#managed-policies-QInvestigations-AIOpsAssistantIncidentReportPolicy "managed-policies-cloudwatch.md#managed-policies-QInvestigations-AIOpsAssistantIncidentReportPolicy").

###### To generate an incident report

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **AI Operations**,
   **Investigations**.
3. Choose the name of an investigation.
4. On the investigation page, under **Feed** accept any
   additional relevant hypotheses and add any additional notes to the
   investigation.

###### Note

Report generation requires an investigation with at least one accepted
hypothesis. 5. On the top of the investigation page, choose **Incident
report**. Wait while the relevant facts of the investigation are
collected and synced. 6. On the **Incident Report** page review the facts being used
to generate the report. The facts are available in the right pane. Navigate
through the fact category tab using the left and right arrows, or expand the
pane to see all of the categories.

    1. Choose **Edit** on a fact panel to manually add or
     edit the data in that category.
    2. Choose **View details** on a fact panel to see the
     supporting evidence and fact history gathered by the AI assistant. You
     can also choose **Edit** within the fact detail
     window.
    3. Choose **Add facts** if you want to provide
     additional context to the investigation, such as external events or
     extenuating circumstances.

7. Choose **Generate report**.

CloudWatch investigations will analyze the investigation data and generate a structured report.
This process might take some time. 8. Review the generated report in the preview pane. The report will
include:

    * Automatically extracted timeline events
    * Root cause analysis based on accepted hypotheses
    * Impact assessment derived from investigation telemetry
    * Recommended corrective actions and lessons learned following AWS
     best practices

9. To retain a copy of the report in a different location, you can choose to copy
   the text of the report and paste it into your desired location.
10. Choose **Report assessment** to review a list of data gaps in
    the report. You can use this information to gather additional data for the
    report and then update the facts accordingly and regenerate the report.
