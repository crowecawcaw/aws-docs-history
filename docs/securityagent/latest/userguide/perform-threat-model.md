

# Create a threat model
<a name="perform-threat-model"></a>

Create threat models in the AWS Security Agent web application to analyze your application’s architecture and identify security threats. A threat model produces two main outputs: a **system overview** that describes how your system is built and behaves, and a set of **threats** that describe how the system could be attacked, each with a severity level, STRIDE classification, and actionable recommendations.

A threat model accepts two kinds of inputs, and you can provide either or both:
+  **Scope docs** – Technical design documents, API specifications, or architecture documentation that define what the threat model focuses on. When provided, the agent scopes its analysis to the context described in these documents. You can upload files (DOC, DOCX, JPEG, MD, PDF, PNG, TXT), provide S3 URIs, or connect Confluence pages through an integration.
+  **Sources** – Source code from connected repositories (GitHub, GitHub Enterprise Server, GitLab, GitLab Self-Managed, or Bitbucket) or from S3 locations. AWS Security Agent reads source code to understand your existing system. When combined with scope docs, the source code provides context about the current implementation.

In this procedure, you create a threat model by configuring its inputs and permissions, then start a run.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ Access to the AWS Security Agent web application
+ At least one of the following:
  + A connected repository (GitHub, GitHub Enterprise Server, GitLab, GitLab Self-Managed, or Bitbucket) to use as a source (see [Enable threat modeling](enable-threat-model.md))
  + An S3 bucket containing source code
  + Design documents to upload as scope docs, or a Confluence integration

**Tip**  
If you already have repositories or S3 buckets connected to your Agent Space (for example, through code review or penetration testing setup), you can create a threat model immediately — no additional setup is required.

## How AWS Security Agent runs a threat model
<a name="_how_aws_security_agent_runs_a_threat_model"></a>

The inputs you provide determine how AWS Security Agent runs the threat model. There are three scenarios.


| Inputs you provide | How AWS Security Agent runs the threat model | 
| --- | --- | 
|  **Sources only** (source code) | AWS Security Agent analyzes the source code to understand your application’s structure, classifies components, extracts data flows, builds a threat model, and identifies threats based on how the system is actually implemented. | 
|  **Scope docs only** (design documents) | AWS Security Agent runs a threat model focused on the design described in your documents. It identifies threats based on the architecture, data flows, and components described in the scope docs — useful for threat modeling a design before any code exists. | 
|  **Both sources and scope docs**  | AWS Security Agent scopes the threat model to the context described in the scope docs (for example, a design document for a new feature). It uses the source code to understand your existing system, then threat models the design described in the scope docs — whether that design is already implemented or not. | 

## Access the threat models page
<a name="_access_the_threat_models_page"></a>

Navigate to the threat modeling section in the web application.

1. Log in to the AWS Security Agent web application.

1. In the left sidebar, choose **Threat models**.

1. You see a list of existing threat models with their title, latest run status, and threat counts by severity.

## Create a threat model
<a name="_create_a_threat_model"></a>

Set up a new threat model by configuring its inputs and permissions.

1. On the **Threat models** page, choose **Create threat model**.

### Configure threat model details
<a name="_configure_threat_model_details"></a>

Provide a title for your threat model.

1. In the **Title** field, enter a descriptive name for your threat model.
**Tip**  
Use a name that identifies the application or service being modeled. For example, "billing-service" or "checkout-api".

### Add scope documents
<a name="_add_scope_documents"></a>

Provide the technical design documents that define what the threat model focuses on, such as architecture documentation, API specifications, or design proposals. When scope docs are provided, the agent scopes its analysis to the context described in these documents. Scope docs are optional if you provide sources.

1. In the **Scope documents** section, add documents using one or more of the following methods:
   +  **Upload files** – Upload design documents directly (DOC, DOCX, JPEG, MD, PDF, PNG, or TXT).
   +  **S3 URIs** – Enter S3 URIs pointing to documents stored in connected S3 buckets.
   +  **Confluence pages** – If you have a Confluence integration connected to your Agent Space, select pages from your Confluence workspace.

**Tip**  
For best results, include architecture diagrams, API specifications, and technical documentation that describe your system’s components, data flows, and trust boundaries.

### Add sources
<a name="_add_sources"></a>

Select the source code AWS Security Agent uses to understand your existing system. When combined with scope docs, the source code provides context about the current implementation — the agent uses it to understand what already exists. Sources are optional if you provide scope docs.

1. In the **Sources** section, add source code using one or more of the following methods:

#### Integrated repositories
<a name="_integrated_repositories"></a>

Select from repositories connected to your Agent Space (GitHub, GitHub Enterprise Server, GitLab, GitLab Self-Managed, or Bitbucket).

1. Select the checkbox next to each repository you want to include as a source.

1. Use the search field to find specific repositories by name.

**Note**  
Only repositories connected to your Agent Space appear here. To add more repositories, ask your administrator to update the Agent Space configuration.

**Tip**  
When you select a repository, you can specify a branch. By default, the service uses the primary branch. To use a different branch, enter the branch name in the field next to the repository.

#### S3 sources
<a name="_s3_sources"></a>

Add S3 URIs pointing to source code stored in connected S3 buckets.

1. Enter the S3 URI for each source code location you want to include.

### Configure AWS resources
<a name="_configure_aws_resources"></a>

Select the IAM service role and optional CloudWatch log group for this threat model.

1. In the **Service role** dropdown, select the IAM role from your configured service roles.
**Note**  
The service role must have permissions to access your source code in S3 and write to CloudWatch logs. Service roles are configured during Agent Space setup in the AWS Management Console.

1. (Optional) In the **Log group** dropdown, select a CloudWatch log group to store threat model execution logs.

### Create the threat model
<a name="_create_the_threat_model"></a>

1. Review your configuration.

1. Choose **Create threat model**.

You are redirected to the threat model detail page where you can start a run.

## Run a threat model
<a name="_run_a_threat_model"></a>

After creating a threat model, start a run to begin the analysis.

1. On the threat model detail page, choose **Start run**.

1. AWS Security Agent begins analyzing your sources and scope docs.

You can also start a run from the **Threat models** list page by choosing **Start run** next to the threat model you want to run.

## Monitor a threat model run
<a name="_monitor_a_threat_model_run"></a>

Track the progress of your threat model as it executes.

### Run status
<a name="_run_status"></a>

The run page header displays a status indicator:
+  **In progress** – The threat model agent is running.
+  **Stopping** – A cancel was requested; the agent is finishing its current task before halting.
+  **Completed** – The run finished successfully.
+  **Failed** – The run encountered an error. An error message is displayed with details. Start a new run after resolving the issue.
+  **Stopped** – The run was canceled by the user. Any threats generated before the stop are preserved.

### Run page tabs
<a name="_run_page_tabs"></a>

On the run detail page, navigate between tabs:
+  **Overview** – View the run summary (job ID, start time, status, duration) with a severity level pie chart showing the breakdown of threats by severity (Critical, High, Medium, Low). Below the summary, view a STRIDE threat categories bar chart showing how many threats fall into each STRIDE category. After the run completes, view the system overview produced by the agent.
+  **Configuration** – View the sources, documents, and permissions (service role, CloudWatch log group) that were used for this run.
+  **Preflight** – View the status of preflight checks that run before threat analysis begins, including logging infrastructure setup, S3 source access validation (when applicable), and testing environment setup. A progress bar shows how many checks have completed.
+  **Logs** – View a filterable list of tasks the agent performed during the run. Select any task to view its detailed log output in a side panel.
+  **Threats** – View the threats identified during the run (see [Review threats from a threat model](review-threat-model-findings.md)).

### Run history
<a name="_run_history"></a>

Each threat model maintains a history of all runs. On the threat model detail page:
+ The runs table lists all runs with their start time, status, duration, threats count, and ID.
+ Choose any run’s start time link to view its full details.

**Tip**  
Re-run the same threat model after you update your source code or revise your scope docs to see how the system overview and threats change over time.

## Edit a threat model
<a name="_edit_a_threat_model"></a>

To modify your threat model configuration:

1. On the threat model detail page, choose **Edit**.

1. Update the title, sources, scope docs, or AWS resources as needed.

1. Choose **Save changes**.

**Note**  
Editing a threat model does not affect previously completed runs. Those preserve the configuration snapshot used at the time they ran.

## Delete a threat model
<a name="_delete_a_threat_model"></a>

To delete a threat model and all its associated runs and threats:

1. On the threat model detail page, open the actions menu and choose **Delete**.

1. Confirm the deletion.

**Important**  
If a run is currently in progress, you must stop it before deleting the threat model.

## Next steps
<a name="_next_steps"></a>

After running a threat model:
+ Review the system overview and threats (see [Review threats from a threat model](review-threat-model-findings.md))
+ Re-run the threat model after making changes to verify threats are addressed
+ Adjust your sources and scope docs as your application evolves