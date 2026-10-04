

# Viewing proactive response metrics
<a name="viewing-proactive-response-metrics"></a>

The **Dashboard** page in the AWS Security Incident Response console includes a **Proactive response** section that shows finding-lifecycle metrics for your membership over a selected time period. These metrics help you understand how AWS Security Incident Response monitors, triages, investigates, and escalates the findings ingested from Amazon GuardDuty and Security Hub CSPM.

**Important**  
Proactive response metrics reflect activity that occurred on or after September 30, 2026, when this feature was released. The **Ingest** and **Triage** metrics include findings from before that date, but the investigation, escalation, false positive, and true positive metrics are not backfilled and reflect only activity on or after the release date. As a result, for timeframes that extend before the release date, these metrics might not account for all of the findings that AWS Security Incident Response processed during the selected period.

**To view proactive response metrics**

1. Open the AWS Security Incident Response console.

1. In the navigation pane, choose **Dashboard**.

1. In the **Proactive response** section, for **Timeframe**, choose the time period to display metrics for: **Last 7 days**, **Last 30 days**, or **Last 90 days**.

The **Proactive response** section presents the metrics as follows.

**Note**  
You can also retrieve these metrics programmatically by calling the `GetFindingMetrics` operation. For more information, see [GetFindingMetrics](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetFindingMetrics.html) in the *AWS Security Incident Response API Reference*.

## Overview
<a name="proactive-response-metrics-overview"></a>

The **Overview** section summarizes the value that proactive response provided during the selected timeframe:
+ **Noise reduction** — The percentage of ingested findings that AWS Security Incident Response resolved through automated triage without requiring escalation to a Security Incident case.
+ **Time saved (hours)** — An estimate of the analyst time saved by automated triage of ingested findings during the timeframe, calculated as one hour for each ingested finding.

## Finding evaluations
<a name="proactive-response-metrics-finding-evaluations"></a>

The **Finding evaluations** section shows the number of findings at each stage of the finding lifecycle during the selected timeframe:
+ **Ingest** — The number of threat detection findings collected from Amazon GuardDuty and supported third-party tools connected through Security Hub CSPM. AWS Security Incident Response focuses on activity that could signal an active threat rather than posture or compliance findings.
+ **Triage** — The number of findings automatically evaluated against AWS logs, metadata, threat intelligence, and the context you provide about your environment to determine whether the activity is expected. Findings confirmed as benign or expected are archived.
+ **Investigation** — The number of findings that automated triage could not confirm as expected activity and that were handed to Security Incident Response Engineering for hands-on investigation.
+ **Escalation** — The number of investigations raised as Security Incident cases because they revealed a genuine security risk or the activity could not be confirmed as expected.

## Finding lifecycle flow
<a name="proactive-response-metrics-lifecycle-flow"></a>

The lifecycle flow diagram visualizes how findings move through proactive response during the selected timeframe. It shows findings flowing from their detection sources, Amazon GuardDuty and Security Hub CSPM, through triage, investigation, and escalation. The diagram also shows the findings that were closed as false positives at the triage and investigation stages, and the findings whose investigation or escalation was still in progress at the end of the timeframe.