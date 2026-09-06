

# Review threats from a threat model
<a name="review-threat-model-findings"></a>

After a threat model run completes, review the system overview and threats to understand how your application could be attacked and what to do about it. The system overview is a comprehensive document describing your application’s architecture, trust boundaries, data flows, and security posture. Each threat includes a statement, severity level, STRIDE classification, affected assets, and a recommendation for addressing it.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ A completed threat model run
+ Access to the AWS Security Agent web application

## Step 1: Access the threat model run
<a name="_step_1_access_the_threat_model_run"></a>

Navigate to your completed threat model run.

1. Log in to the AWS Security Agent web application.

1. In the left sidebar, choose **Threat models**.

1. Select the threat model you want to examine.

1. In the runs table, select the completed run by choosing its start time link.

## Step 2: Review the system overview
<a name="_step_2_review_the_system_overview"></a>

The system overview is a comprehensive description of how AWS Security Agent understands your system. It is a structured document that can include:
+  **Purpose** – What the system does and who it serves.
+  **Capabilities** – Key functionality the system provides.
+  **Design intent** – The design change or feature being threat modeled (when scope docs are provided).
+  **Architecture** – How the system is built, including deployment patterns and communication protocols.
+  **Components** – A table of system components with their purpose and key interactions.
+  **Trust boundaries** – Where security contexts change, including what protections exist at each crossing.
+  **Data flows** – Detailed descriptions of how data moves through the system, including protocols, credentials, and protections at each step.
+  **Security posture** – Current authentication, encryption, and access control mechanisms.
+  **Sensitive assets** – Data and credentials that require protection, with their classification and exposure points.
+  **Key assumptions** – Security-relevant assumptions the agent made about the system.

To review the system overview:

1. Select the **Overview** tab.

1. Review the **Run summary** section, which shows the job ID, start time, status, and duration.

1. Review the **Severity level** chart, which shows a breakdown of threats by severity (Critical, High, Medium, Low) with counts and percentages.

1. Review the **Threat categories** chart, which shows how many threats fall into each STRIDE category (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).

1. In the **System overview** section, read the agent’s full analysis.

**Tip**  
If the system overview doesn’t accurately reflect your system, refine your inputs — add relevant repositories as sources or upload more complete scope docs — and run the threat model again.

## Step 3: Review threats
<a name="_step_3_review_threats"></a>

Navigate to the **Threats** tab to view all threats identified during the run.

1. Select the **Threats** tab.

1. Threats display as a list with each card showing the threat title, severity badge, status, and last updated timestamp. You can filter threats by severity, status, or search by title.

1. Select a threat from the list to view its full details in the right panel.

### Threat severity
<a name="_threat_severity"></a>

Each threat is assigned a severity level:
+  **Critical** – Requires immediate action; exploitation could lead to full system compromise.
+  **High** – Requires prompt attention; exploitation could result in significant security impact.
+  **Medium** – Should be addressed in a reasonable timeframe; contributes to overall security risk.
+  **Low** – Can be addressed as part of regular maintenance; minimal immediate risk.

### Threat details
<a name="_threat_details"></a>

Select a threat to view its details in the right panel. The details are organized into the following sections:

 **Metadata row:** 
+  **Severity** – The risk level assigned by the agent (Critical, High, Medium, or Low).
+  **STRIDE categories** – The threat classification: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, or Elevation of Privilege.
+  **Created at** – When the threat was identified.
+  **Last updated** – When the threat was last modified.

 **Description section:** 
+  **Statement** – A natural-language description of the threat: what the threat source can do, what the impact is, and what conditions enable it.
+  **Source** – The actor or origin of the threat (for example, "authenticated user" or "external attacker").
+  **Action** – What the threat source can do (for example, "inject SQL queries into the search parameter").
+  **Impact** – The direct consequence of the threat action (for example, "unauthorized access to customer records").

 **References section:** 
+  **Affected assets** – Specific assets affected by the threat (for example, "customer payment records" or "DynamoDB table").
+  **Prerequisites** – Conditions that must be true for the threat to be exploitable.
+  **Impacted goals** – Security goals affected: Confidentiality, Integrity, Availability, Authorization, Authentication, or Non-repudiation.
+  **Evidence** – Source code file paths that support the threat, linking back to specific files in your repository.
+  **Anchor** – A code reference linking the threat to a specific node in your source code.

 **Recommendation section:** 
+  **Recommendation** – Actionable guidance for addressing the threat.

## Step 4: Create a threat manually
<a name="_step_4_create_a_threat_manually"></a>

You can add threats that the agent did not identify — for example, threats discovered during manual review or from external sources.

1. On the **Threats** tab of a completed run, choose **Create threat**.

1. Fill in the threat details:
   +  **Statement** – A natural-language description of the threat.
   +  **Severity** – Select Critical, High, Medium, or Low.
   +  **Source** – The actor or origin of the threat.
   +  **Prerequisites** – Conditions required for the threat to be exploitable.
   +  **Action** – What the threat source can do.
   +  **Impact** – The direct consequence of the threat action.
   +  **Affected assets** – Specific assets affected (comma-separated).
   +  **Impacted security goals** – Select from Confidentiality, Integrity, Availability, Authorization, Authentication, or Non-repudiation.
   +  **STRIDE categories** – Select applicable categories.
   +  **Recommendation** – Guidance for addressing the threat.

1. Choose **Create**.

The manually created threat appears in the threats list alongside agent-generated threats.

## Step 5: Edit and triage threats
<a name="_step_5_edit_and_triage_threats"></a>

As you review threats, you can edit their details and update their status to track progress.

1. Select a threat from the list.

1. Choose the edit icon in the threat detail panel to open the edit form.

1. You can modify the following fields:
   +  **Status** – Track the threat lifecycle:
     +  **Open** – The threat is acknowledged and needs attention (default).
     +  **Resolved** – You have fixed the issue.
     +  **Dismissed** – You reviewed the threat and determined it is not applicable.
   +  **Severity** – Adjust the severity level if the agent’s assessment doesn’t match your context.
   +  **Statement** – Refine the threat description.
   +  **Source, Prerequisites, Action, Impact** – Update the threat details based on your domain knowledge.
   +  **Affected assets** – Add or remove affected assets (comma-separated).
   +  **Impacted security goals** – Select the security goals affected (Confidentiality, Integrity, Availability, Authorization, Authentication, Non-repudiation).

1. Choose **Save** to apply your changes.

## Step 6: Download a report
<a name="_step_6_download_a_report"></a>

After a run completes, you can download a PDF report summarizing the system overview and all identified threats.

1. On the completed run page, choose **Generate report**.

1. The PDF downloads to your computer.

## Step 7: Review preflight checks and logs
<a name="_step_7_review_preflight_checks_and_logs"></a>

If you need to investigate how the agent reached its conclusions or debug a partial failure:

1. Select the **Preflight** tab to view the status of preflight checks that run before threat analysis begins. Each check shows its status (complete, in progress, or pending), and a progress bar indicates how many checks have completed. You can expand a completed check to view its detailed log output.

1. Select the **Logs** tab to view a filterable list of tasks the agent performed during the run. Select any task from the list to view its detailed log output in the side panel.

## Next steps
<a name="_next_steps"></a>

After reviewing your threat model results:
+ Address high-severity threats first based on the agent’s recommendations
+ Update threat statuses as you implement fixes
+ Run a new threat model to verify your changes address the identified threats
+ Adjust your sources and scope docs as your application evolves (see [Create a threat model](perform-threat-model.md))