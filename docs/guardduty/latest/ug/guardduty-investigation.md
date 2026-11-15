

# GuardDuty Investigation (Preview)
<a name="guardduty-investigation"></a>

GuardDuty Investigation provides AI-powered security analysis of your GuardDuty findings and accounts. When you create an investigation, GuardDuty examines finding context, related activity from the last 90 days, affected resources, threat intelligence and threat indicators using knowledge graphs. Each investigation provides a threat disposition assessment with confidence scoring, MITRE ATT&CK® technique classification, supporting evidence, and actionable recommendations.

Each investigation produces the following insights:
+ **Risk level** – An assessment of the overall risk: Info, Low, Medium, High, or Critical.
+ **Confidence** – The confidence level of the assessment: Unknown, Low, Medium, or High.
+ **Summary** – A description of the investigation findings and key observations.
+ **Investigation Details** – Additional information and context related to the investigation.
+ **Recommended Actions** – Detailed actions, including the CLI commands, you can take to address the identified issues.

**Note**  
GuardDuty Investigation is available in the following 10 commercial AWS Regions only: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and Asia Pacific (Tokyo).

## Analysis types
<a name="guardduty-investigation-analysis-types"></a>

GuardDuty Investigation supports the following three types of analysis:
+ **Finding analysis** – Analyzes specific GuardDuty findings, when you specify the finding ID (32-character hexadecimal).
+ **Account analysis** – Analyzes the threat posture of an AWS account, when you provide the 12-digit AWS account ID.
+ **Organization analysis** – Analyzes your organization's threat posture.

## Cross-Region inference
<a name="guardduty-investigation-cross-region-inference"></a>

GuardDuty Investigation leverages Cross-Region Inference Service (CRIS), which automatically selects the optimal AWS Region within your geography to process the investigation analysis and generate the investigation report. This maximizes available compute resources, model availability, and delivers the best customer experience.

Your data remains stored only in the Region where the investigation request originates. However, investigation data and summary results may be processed outside that Region. All data is transmitted encrypted across the Amazon secure network.

GuardDuty Investigation securely routes your inference requests to available compute resources within the geographic area where the request originated, as shown in the following table.


**Cross-Region inference routing**  

| Supported geography | GuardDuty Region | Inference Regions | 
| --- | --- | --- | 
| United States | US East (N. Virginia) | US East (N. Virginia), US East (Ohio), US West (Oregon) | 
| United States | US East (Ohio) | US East (N. Virginia), US East (Ohio), US West (Oregon) | 
| United States | US West (Oregon) | US East (N. Virginia), US East (Ohio), US West (Oregon) | 
| United States | Canada (Central) | Canada (Central), US East (N. Virginia), US East (Ohio), US West (Oregon) | 
| Europe | Europe (Frankfurt) | Europe (Frankfurt), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (Paris) | 
| Europe | Europe (Ireland) | Europe (Frankfurt), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (Paris) | 
| Europe | Europe (London) | Europe (Frankfurt), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris) | 
| Europe | Europe (Paris) | Europe (Frankfurt), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (Paris) | 
| Europe | Europe (Stockholm) | Europe (Frankfurt), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (Paris) | 
| Japan | Asia Pacific (Tokyo) | Asia Pacific (Tokyo), Asia Pacific (Osaka) | 

## Prerequisites
<a name="guardduty-investigation-prerequisites"></a>

Before you can use GuardDuty Investigation, make sure that the following prerequisites are met:
+ You must have an active GuardDuty detector in the AWS Region where you want to create investigations. For more information about enabling GuardDuty, see [Getting started with GuardDuty](guardduty_settingup.md).
+ You must enable the GuardDuty Investigation feature on your detector.

------
#### [ Console ]

  1. Open the GuardDuty console.

  1. In the navigation pane, choose **Settings**.

  1. Under **AI powered investigations - Preview**, choose **Enable**.

------
#### [ API/CLI ]

  Call the [UpdateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API and enable the `AI_ANALYST` feature on your detector.

  ```
  aws guardduty update-detector \
      --detector-id {{2cb3d4e5f6a7b8c9d0e1f2a3b4c5d6e7}} \
      --features '[{"Name": "AI_ANALYST", "Status": "ENABLED"}]'
  ```

------
+ Your IAM identity must have the required permissions to perform investigation actions. The following IAM actions are required:
  + `guardduty:CreateInvestigation` – Required to create a new investigation.
  + `guardduty:GetInvestigation` – Required to retrieve investigation results.
  + `guardduty:ListInvestigations` – Required to list investigations for a detector.
  + `guardduty:ListInvestigationRecords` – Required to list the records of an investigation.

The following example IAM policy grants permission to use all GuardDuty Investigation actions:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "guardduty:CreateInvestigation",
                "guardduty:GetInvestigation",
                "guardduty:ListInvestigations",
                "guardduty:ListInvestigationRecords"
            ],
            "Resource": "arn:aws:guardduty:{{us-east-1}}:{{123456789012}}:detector/{{2cb3d4e5f6a7b8c9d0e1f2a3b4c5d6e7}}"
        }
    ]
}
```

In the preceding policy, replace {{us-east-1}} with your AWS Region, {{123456789012}} with your AWS account ID, and {{2cb3d4e5f6a7b8c9d0e1f2a3b4c5d6e7}} with your detector ID.

### Access model for administrator and member accounts
<a name="guardduty-investigation-access-model"></a>

The following access rules apply to GuardDuty Investigation depending on whether you use an administrator account or a member account:
+ **Administrator accounts** – Can create, get, and list investigations for themselves and their member accounts.
+ **Member accounts** – Can only get and list investigations for their own account. Member accounts cannot create investigations and cannot access investigations belonging to other accounts or the administrator account.

## Creating an investigation
<a name="guardduty-investigation-create"></a>

You can create an investigation to analyze GuardDuty findings and accounts in your AWS environment. The investigation runs asynchronously in the background. After you create an investigation, use the investigation ID to check its status and retrieve results.

**Important**  
During preview, you can initiate up to 10 investigations per account per day, with a total limit of 100 investigations per account. Failed investigations do not count toward these quotas. If you are using the API/CLI, the trigger prompt can be up to 2,048 characters.

Choose your preferred access method to create an investigation.

------
#### [ Console ]

1. Open the GuardDuty console and navigate to **Investigations** in the left navigation.

1. Choose **Initiate investigation**.

1. Select an investigation scope:
   + **A specific finding** – Enter the finding ID you want to analyze.
   + **My account** (standalone only) – No additional input required. GuardDuty will analyze your account.
   + **A specific account** (administrator only) – Enter the 12-digit AWS account ID.
   + **All accounts in organization** (administrator only) – No additional input required.

1. Choose **Initiate investigation** to start the analysis.

------
#### [ API/CLI ]

Run the CreateInvestigation API operation to start a new investigation. You must provide the detector ID and a trigger prompt that describes what to investigate.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty create-investigation \
    --detector-id {{2cb3d4e5f6a7b8c9d0e1f2a3b4c5d6e7}} \
    --trigger-prompt "{{Investigate finding 1ab2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 in account 123456789012}}"
```

In the preceding command, replace the {{detector-id}} with your own detector ID and {{trigger-prompt}} with a description of what you want to investigate.

You can optionally include a `--client-token` parameter for idempotency. If you retry the request with the same client token, GuardDuty returns the existing investigation instead of creating a duplicate.

Example output:

```
{
    "InvestigationId": "a1b2c3d4-5678-90ab-cdef-ef1234567890"
}
```

**Trigger prompt requirements**

The trigger prompt must describe what to investigate. GuardDuty determines the analysis type based on the content of your prompt:
+ **Finding analysis** – Include exactly one finding ID (32-character hexadecimal string) in the prompt. The finding must exist and belong to the caller's account or a member account. You cannot include multiple finding IDs in a single prompt.
+ **Account analysis** – Include exactly one 12-digit AWS account ID in the prompt. The caller must be the administrator of that account. You cannot include multiple account IDs in a single prompt.
+ **Organization analysis** – Describe an organization-wide security concern in your prompt. The investigation analyzes signals across the organization.

GuardDuty uses AI to interpret your free-form prompt and determine the appropriate analysis scope. If you include a finding ID, it performs finding analysis. If you include an account ID, it performs account analysis. If your prompt describes an organization-wide concern, it performs organization analysis. If the prompt does not match a specific analysis type, the investigation defaults to analyzing the caller's own account.

The following are example trigger prompts for each analysis type:
+ **Finding analysis** – `"Investigate finding 1ab2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 in account 123456789012"`
+ **Account analysis** – `"Analyze findings in account with id 123456789012"`
+ **Organization analysis** – `"Analyze findings in my organization"`

**Creating an investigation for a member account**

If you are an administrator account, you can create an investigation for a member account by including the member account ID in the trigger prompt. Use the administrator account's detector ID in the command. The investigation results will contain findings from the specified member account.

```
aws guardduty create-investigation \
    --detector-id {{2cb3d4e5f6a7b8c9d0e1f2a3b4c5d6e7}} \
    --trigger-prompt "Analyze findings in account with id 111122223333"
```

In the preceding command, replace the {{detector-id}} with your administrator account's detector ID. The 12-digit account ID in the trigger prompt identifies the member account to investigate.

------

## Viewing investigation results
<a name="guardduty-investigation-get"></a>

After you create an investigation, you can retrieve the results including the summary, investigation details, confidence level, and recommendation. An investigation can have one of the following statuses:
+ **RUNNING** – The investigation is still in progress.
+ **COMPLETED** – The investigation finished successfully and results are available.
+ **FAILED** – The investigation encountered an error. Check the error field for details.

Choose your preferred access method to view investigation results.

*AI-generated analysis and recommendations may contain errors or incomplete assessments. Human review is recommended.*

------
#### [ Console ]

1. Open the GuardDuty console and navigate to **Investigations** in the left navigation.

1. In the investigations table, find the completed investigation you want to review.

1. Choose the investigation title link to open the details page.

**Note**  
Investigation titles are only clickable when the status is **Completed**.

------
#### [ API/CLI ]

Run the GetInvestigation API operation to retrieve the full details of a completed investigation.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty get-investigation \
    --detector-id {{2cb3d4e5f6a7b8c9d0e1f2a3b4c5d6e7}} \
    --investigation-id {{a1b2c3d4-5678-90ab-cdef-ef1234567890}}
```

Example output for a completed investigation:

```
{
    "Investigation": {
        "InvestigationId": "a1b2c3d4-5678-90ab-cdef-ef1234567890",
        "Status": "COMPLETED",
        "TriggerPrompt": "Investigate finding 1ab2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 in account 123456789012",
        "TriggeredBy": "123456789012",
        "RiskLevel": "Critical",
        "Risk": "Detection logic is valid but no live resources are compromised.",
        "Confidence": "High",
        "Summary": "{\"keyObservations\":{\"title\":\"...\",\"narrative\":\"...\",\"observations\":[...]},\"countermeasures\":[...],\"threatAssessment\":{...}}",
        "Cloud": {
            "Provider": "AWS",
            "Region": "us-east-1",
            "Account": "123456789012"
        },
        "Metadata": {
            "Product": {
                "Name": "Amazon GuardDuty AI Analyst",
                "Feature": "Investigation"
            },
            "Version": "1.0.0"
        },
        "StartTime": 1705319400.0,
        "EndTime": 1705319700.0
    }
}
```

The `Summary` field contains a JSON string with the full investigation results, including key observations, countermeasures with CLI commands, and a MITRE ATT&CK® threat assessment.

------

### Interpreting investigation results
<a name="guardduty-investigation-interpret-results"></a>

The following table describes the risk levels that an investigation can return:


**Investigation risk levels**  

| Risk level | Description | 
| --- | --- | 
| Info | Informational finding with no identified risk to the environment. | 
| Low | Minor risk that is unlikely to require immediate action. | 
| Medium | Moderate risk that you must review and might require remediation. | 
| High | Significant risk that requires prompt investigation and remediation. | 
| Critical | Severe risk that requires immediate action to prevent further compromise. | 

The following table describes the confidence levels:


**Investigation confidence levels**  

| Confidence level | Description | 
| --- | --- | 
| Unknown | Insufficient data to determine confidence in the assessment. | 
| Low | Limited evidence supports the assessment. | 
| Medium | Moderate evidence supports the assessment. | 
| High | Strong evidence supports the assessment. | 

## Listing investigations
<a name="guardduty-investigation-list"></a>

You can list all investigations for a detector, with optional sorting and pagination. This helps you review and track the status of multiple investigations.

Choose your preferred access method to list investigations.

------
#### [ Console ]

1. Open the GuardDuty console and navigate to **Investigations** in the left navigation.

1. The investigations table displays all investigations for the current detector with their status, risk level, and timestamps.

------
#### [ API/CLI ]

Run the ListInvestigations API operation to list investigation summaries for a detector.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty list-investigations \
    --detector-id {{2cb3d4e5f6a7b8c9d0e1f2a3b4c5d6e7}} \
    --max-results 10
```

You can sort the results by specifying a `--sort-criteria` parameter. The following example lists investigations sorted by start time in descending order:

```
aws guardduty list-investigations \
    --detector-id {{2cb3d4e5f6a7b8c9d0e1f2a3b4c5d6e7}} \
    --sort-criteria '{"attributeName": "START_TIME", "orderBy": "DESC"}' \
    --max-results 10
```

The available sort attributes are `START_TIME`, `END_TIME`, `STATUS`, `RISK_LEVEL`, and `CONFIDENCE`. You can sort in `ASC` (ascending) or `DESC` (descending) order.

Example output:

```
{
    "Investigations": [
        {
            "InvestigationId": "a1b2c3d4-5678-90ab-cdef-ef1234567890",
            "Status": "COMPLETED",
            "TriggerPrompt": "Investigate finding 1ab2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 in account 123456789012",
            "RiskLevel": "Critical",
            "Confidence": "High",
            "StartTime": 1705319400.0,
            "EndTime": 1705319700.0,
            "AccountId": "123456789012"
        },
        {
            "InvestigationId": "b2c3d4e5-6789-01bc-def0-ef2345678901",
            "Status": "COMPLETED",
            "TriggerPrompt": "Analyze findings in account with id 123456789012",
            "RiskLevel": "High",
            "Confidence": "High",
            "StartTime": 1705315800.0,
            "EndTime": 1705316100.0,
            "AccountId": "123456789012"
        },
        {
            "InvestigationId": "c3d4e5f6-7890-12cd-ef01-ef3456789012",
            "Status": "COMPLETED",
            "TriggerPrompt": "Analyze findings in my organization",
            "RiskLevel": "Medium",
            "Confidence": "Medium",
            "StartTime": 1705312200.0,
            "EndTime": 1705312500.0,
            "AccountId": "123456789012"
        }
    ]
}
```

If the response includes a `NextToken` value, pass it in a subsequent request to retrieve the next page of results. You can retrieve up to 50 results per page.

------

## Listing investigation records
<a name="guardduty-investigation-records"></a>

An investigation record is one step in the reasoning that GuardDuty followed during an investigation. GetInvestigation returns the results of an investigation, such as the status, risk level, confidence, and summary. For more information, see [Viewing investigation results](#guardduty-investigation-get). The records show how GuardDuty reached those results. They show the data that it retrieved, the observations that it made about your environment, and the analysis that it performed. Use the records to audit or explain the conclusion of an investigation.

ListInvestigationRecords returns records in the order that GuardDuty created them, oldest first. The response includes the investigation `Status` (`RUNNING`, `COMPLETED`, or `FAILED`). Records are available only when the investigation status is `COMPLETED`. If the investigation status is `RUNNING` or `FAILED`, the response contains an empty list of records.

The following table describes the record types.


**Investigation record types**  

| Record type | Description | 
| --- | --- | 
| UPDATE | A progress milestone, such as the request that started the investigation or a response from GuardDuty. | 
| FETCH | Data that GuardDuty retrieved for the investigation, such as a finding, a detector configuration, or a list of your member accounts. The record includes what GuardDuty requested and what it received. | 
| OBSERVATION | A fact that GuardDuty noted about your environment. Examples include the affected resource, the activity on that resource, and your detection coverage. | 
| ANALYSIS | An assessment that GuardDuty derived from the data. Examples include a threat assessment, a comparison against normal behavior, and a process lineage. | 
| METADATA | Operational details about the investigation itself, such as how long the investigation took. | 

Each record includes a `Title` and can include a plain-text `Narrative` that explains the step. A narrative can span several paragraphs. A record can also include a `SupportingData` structure that contains the structured details for the step. `UPDATE` records never include `SupportingData`, and records of other types don't always include it.

Choose your preferred access method to list investigation records.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Investigations**.

1. On the **Investigations** page, choose an investigation to open its details page.

1. On the details page, review the records on the investigation timeline. Each record shows its title and narrative.

------
#### [ API/CLI ]

Run the ListInvestigationRecords API operation to list the records for an investigation.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following AWS CLI command lists up to 20 records for an investigation:

```
aws guardduty list-investigation-records \
    --detector-id {{12abc34d567e8fa901bc2d34EXAMPLE}} \
    --investigation-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --max-results 20
```

In the preceding command, replace {{detector-id}} and {{investigation-id}} with your own values.

To return only specific record types, use the `--record-types` parameter. The following example returns only `OBSERVATION` and `ANALYSIS` records:

```
aws guardduty list-investigation-records \
    --detector-id {{12abc34d567e8fa901bc2d34EXAMPLE}} \
    --investigation-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --record-types OBSERVATION ANALYSIS
```

In the preceding command, replace {{detector-id}} and {{investigation-id}} with your own values.

The following example output shows two of the records that the command returns:

```
{
    "InvestigationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Status": "COMPLETED",
    "Records": [
        {
            "RecordId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Type": "OBSERVATION",
            "Title": "Detection coverage for this finding",
            "Narrative": "CloudTrail management events, which this finding type relies on, are enabled. Runtime Monitoring is disabled.",
            "CreatedAt": "2024-01-15T11:52:00.123456+00:00",
            "SupportingData": {
                "Observation": {
                    "ObservationType": "DETECTION_COVERAGE",
                    "DetectionCoverage": {
                        "ProtectionPlans": [
                            {
                                "Name": "CLOUD_TRAIL",
                                "Status": "ENABLED"
                            },
                            {
                                "Name": "RUNTIME_MONITORING",
                                "Status": "DISABLED"
                            }
                        ],
                        "FoundationalDataSources": [
                            "CLOUD_TRAIL",
                            "DNS_LOGS",
                            "FLOW_LOGS"
                        ]
                    }
                }
            }
        },
        {
            "RecordId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "Type": "ANALYSIS",
            "Title": "Threat assessment",
            "Narrative": "The instance credentials were used from an external address shortly after the instance was launched.",
            "CreatedAt": "2024-01-15T11:53:00.654321+00:00"
        }
    ],
    "NextToken": "AAEXAMPLEnextTokenValue"
}
```

If the response includes a `NextToken` value, pass it in a subsequent request to retrieve the next page of results. Each page can contain up to 50 records.

------