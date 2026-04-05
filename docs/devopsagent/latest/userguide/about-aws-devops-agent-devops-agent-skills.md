# DevOps Agent Skills

AWS DevOps Agent Skills are modular instruction sets that extend the agent's capabilities with specialized domain knowledge and investigation methodologies tailored to your infrastructure and operational workflows.

## What are Skills

Skills are self-contained directories containing Markdown instructions that provide specialized capabilities to AWS DevOps Agent. AWS DevOps Agent supports a subset of the [Agent Skills specification](https://agentskills.io/ "https://agentskills.io/") —an open standard for packaging agent instructions and resources—supporting only non-executable documents: Markdown instructions, PDFs, images, and data files.

Every skill requires a SKILL.md file containing instructions you want to provide for your AWS DevOps Agent. In addition to the required SKILL.md file, skills can include:

- **Investigation workflows** for specific scenarios or infrastructure types.
- **Reference materials** including architecture patterns and operational procedures.
- **Agent type targeting** – Skills can be targeted to specific agent types (Generic, On-demand, Incident Triage, Incident RCA, Incident Mitigation, Evaluation) to reduce context consumption and improve agent focus.

## Why use Skills

Skills transform AWS DevOps Agent from a general-purpose assistant into a specialist for your infrastructure and operational workflows. Unlike one-time instructions provided in a chat message, Skills are reusable capabilities that load automatically when relevant to tasks performed by AWS DevOps Agent.

**Key benefits:**

- **Specialize your agent** – Tailor AWS DevOps Agent with investigation procedures, best practices, and organizational knowledge specific to your infrastructure and operational patterns.
- **Reduce repetition** – Create investigation workflows once and AWS DevOps Agent uses them automatically across all relevant investigations, eliminating the need to provide the same guidance repeatedly.
- **Compose capabilities** – Combine multiple Skills to build end-to-end investigation workflows. AWS DevOps Agent reads multiple skills during execution, such as a skill to retrieve deployments from your custom CI/CD pipeline and a skill to search your code repositories.
- **Amplify custom tools** – Create skills that guide AWS DevOps Agent in using your custom MCP server tools effectively. Skills can document when to invoke specific tools, what parameters to use for different scenarios, and how to interpret results to accomplish workflows specific to your infrastructure.

## How Skills work

When AWS DevOps Agent encounters a relevant task, it loads the appropriate skills and follows the instructions to guide its investigation. For example, a "Database Performance Investigation" skill might include step-by-step procedures for analyzing RDS throttling issues, enabling the agent to systematically check alarm status, analyze connection metrics, and identify slow queries.

## Skill structure

A skill is organized as a directory containing:

```
my-skill/
├── SKILL.md              # Main skill instructions
├── references/           # Optional: additional reference documentation
└── assets/               # Optional: images, diagrams, data files
```

### SKILL.md

The `SKILL.md` is the only mandatory file. It contains the core instructions written in Markdown format. This file should:

- Describe when and how to use the skill.
- Provide step-by-step investigation procedures.
- Include decision trees for different scenarios.
- Document expected outputs and success criteria.

### Frontmatter

Frontmatter is the metadata block at the top of a `SKILL.md` file, enclosed between `---` delimiters. It contains the `name` and `description` fields that AWS DevOps Agent uses to determine when to activate the Skill during an investigation or task.

```
---
name: rds-performance-investigation
description: Investigation procedures for RDS performance issues including
  connection exhaustion, slow queries, replication lag, and storage capacity.
  Use this skill when investigating database latency, connection errors, or
  read/write performance degradation.
---
```

**name** – A unique identifier for the Skill. Use lowercase letters, numbers, and hyphens only (maximum 64 characters). Must not start or end with a hyphen.

**description** – A detailed explanation of when and why AWS DevOps Agent should use this Skill. AWS DevOps Agent evaluates this field to decide whether the Skill is relevant to the current task. A vague or missing description can cause the agent to skip the Skill entirely, even if the instructions are well-written.

**Important** – Write the description from the agent's perspective. Include the specific scenarios, services, error types, or symptoms that should trigger the Skill. For example, "Use this skill when investigating database latency, connection errors, or query timeouts for Amazon RDS instances" is more effective than "RDS skill".

When you create a Skill in the UI, the system generates frontmatter automatically from the name and description you provide. Skills uploaded as zip files must include frontmatter in the `SKILL.md` file.

## Example: Complete skill

The following example shows a complete, well-formed skill for investigating RDS performance issues. It demonstrates the directory structure, SKILL.md frontmatter, actionable investigation procedures, and a supplementary references file.

**Directory structure:**

```
rds-performance-investigation/
├── SKILL.md
├── references/
│   └── rds-metrics-reference.md
└── assets/
    └── rds-investigation-flowchart.png
```

**SKILL.md:**

```
---
name: rds-performance-investigation
description: Investigation procedures for RDS performance issues including
  connection exhaustion, slow queries, replication lag, and storage capacity.
  Use this skill when investigating database latency, connection errors, or
  read/write performance degradation.
---

# RDS Performance Investigation

Use this skill when customers report database latency, connection errors,
query timeouts, or read/write performance degradation.


## Step 1: Check alarm status

Query CloudWatch for active alarms on the affected RDS instance. Look for:
- `DatabaseConnections` exceeding 80% of max_connections
- `ReadLatency` or `WriteLatency` above 20ms
- `FreeStorageSpace` below 20% of total storage
- `ReplicaLag` above 30 seconds (read replicas only)


## Step 2: Analyze connection metrics

Retrieve `DatabaseConnections` over the past hour. If connections are near
the max_connections limit, check for connection pool misconfiguration or
long-running idle connections.


## Step 3: Identify slow queries

Use Performance Insights (`pi:GetResourceMetrics`) to retrieve the top SQL
statements by average active sessions. Focus on queries with high `db.load`
contribution or frequent I/O waits.


## Step 4: Summarize findings

Provide a summary with:
1. Current performance status (healthy / degraded / critical)
2. Root cause hypothesis with supporting metrics
3. Recommended remediation steps ranked by priority
```

**references/rds-metrics-reference.md:**

```
# RDS CloudWatch Metrics Reference


| Metric | Normal Range | Investigation Threshold |
|---|---|---|
| DatabaseConnections | < 70% max_connections | > 80% max_connections |
| ReadLatency | < 5ms | > 20ms |
| WriteLatency | < 5ms | > 20ms |
| FreeStorageSpace | > 30% total storage | < 20% total storage |
| ReplicaLag | < 5 seconds | > 30 seconds |
| CPUUtilization | < 70% | > 85% |
```

## Creating Skills

Before creating skills, you must have an Agent Space. For more information, see [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md "getting-started-with-aws-devops-agent-creating-an-agent-space.md").

You can create skills in two ways depending on your workflow preferences and skill complexity:

### Creating a skill in the UI

Skills created in the AWS DevOps Agent Operator Web App contain a name, description, and instructions in a single SKILL.md file.

**To create a skill in the UI:**

- Navigate to the Skills page in your Agent Space Operator Web App.
- Click "Add skill".
- Select "Create skill" from the modal.
- Fill out the skill form:
  - **Name** – Lowercase letters, numbers, and hyphens only (maximum 64 characters). Must not start or end with a hyphen. Example: `rds-throttling-investigation`
  - **Description** – Brief explanation of when to use this skill (minimum 100 characters recommended, maximum 1,024 characters). This helps the agent determine when to activate the skill.
  - **Status** – Set to Active (default) or Inactive. Inactive skills are not used by the agent.
  - **Agent Type** – Select one or more agent types that can use this skill. **Generic** is selected by default and makes the skill available to all agent types. To target specific agents, deselect Generic and choose from: On-demand, Incident Triage, Incident RCA, Incident Mitigation, or Evaluation.
  - **Instructions** – Step-by-step procedures in Markdown format. Be specific and actionable.

- Click "Create" to save the skill.

The system automatically generates a SKILL.md file with the proper frontmatter structure.

**To edit a skill created in the UI:**

- Navigate to the skill in the Skills list and click the skill to open it.
- Click **Edit**.
- Modify the name, description, or instructions.
- Click **Save** to update the skill.

### Uploading a skill

Skills uploaded as zip files contain a SKILL.md file plus additional resources such as reference materials or assets.

**Skill structure:**

```
my-skill.zip
├── SKILL.md              # Required: main skill instructions
├── references/           # Optional: reference documentation
│   ├── architecture.md
│   └── troubleshooting.md
└── assets/               # Optional: images, diagrams, data files
    ├── topology.png
    └── metrics.csv
```

**SKILL.md frontmatter requirements:**

Skills uploaded as zip files must include frontmatter in SKILL.md with `name` and `description` fields. AWS DevOps Agent uses these fields to determine when to activate the Skill. For details on writing effective frontmatter, see the Frontmatter section earlier in this topic.

```
---
name: rds-performance-analysis
description: Comprehensive RDS performance investigation procedures
  for connection exhaustion, slow queries, and storage capacity issues.
  Use when investigating database latency or read/write degradation.
---


# RDS Performance Analysis


[Your skill instructions here...]
```

**To create a skill via zip upload:**

- Create a directory with your skill files following the structure above.
- Ensure SKILL.md includes proper frontmatter (name and description).
- Compress the directory into a .zip file.
- Navigate to the Skills page in your Agent Space Operator Web App.
- Click "Add skill".
- Select "Upload skill" from the modal.
- Drag and drop your .zip file or click to browse (ZIP files only, maximum 6 MB).
- Select one or more agent types that can use this skill (Generic is selected by default and applies to all agent types; deselect to target On-demand, Incident Triage, Incident RCA, Incident Mitigation, or Evaluation specifically).
- Review the zip file requirements and validation results.
- Click "Upload" to add the skill to your Agent Space.

**Important restrictions for skills uploaded as zip files:**

- **Scripts are currently not supported** – Skills containing scripts in the `scripts/` directory will be rejected during upload. Script execution will be enabled in a future release once agents have access to a secure coding environment.
- **Size limit** – Total zip file size must not exceed 6 MB (including all files).
- **SKILL.md required** – The zip file must contain a SKILL.md file with valid frontmatter.

**Best practices for naming skills:**

Use clear, descriptive names like "rds-throttling-investigation" rather than generic names. A good skill name reflects the specific scenario or service it addresses, making it easier to identify the right skill at a glance.

## Managing Skills

AWS DevOps Agent provides comprehensive skill management capabilities through the Operator Web App:

**Listing skills** – View all Skills in your Agent Space. The Skills page displays skill name, Active or Inactive status, creation date, last updated date, and available actions.

**Viewing skills** – Click on any skill to see its detail view. Skills created in the UI display editable content where you can modify the name, description, or instructions directly in the UI and click "Save" to update. Skills uploaded as zip files display a file tree showing SKILL.md and any additional directories like references/ and assets/. Click files in the tree to view their contents in read-only mode.

**Selecting agents for a skill** – Configure which agent types can use each skill when creating or editing it. In the Agent Type dropdown, select one or more agent types using the checkboxes: **Generic** (default — applies to all agent types), **On-demand** (conversational queries), **Incident Triage** (initial incident assessment), **Incident RCA** (root cause analysis), **Incident Mitigation** (automated incident response), or **Evaluation** (proactive recommendations). Generic is selected by default and makes the skill available to all agent types. Skills targeted to specific agents reduce context consumption and improve agent focus.

**Activating and deactivating skills** – Temporarily disable skills without deleting them using the Active/Inactive toggle. Open the skill detail view and toggle the switch to "Inactive" to prevent the agent from loading it for new investigations while preserving all content and configurations. In-progress investigations continue using the skill. Toggle back to "Active" to make the skill immediately available again.

**Updating skills** – Modify existing skills based on how they were created. For skills created in the UI, click "Edit" in the skill detail view, modify the name, description, or instructions, and click "Save" to update. For skills uploaded as zip files, modify the files locally, create a new zip file, and upload a new version.

**Deleting skills** – Permanently remove skills from your Agent Space. Open the skill list view, click the more options menu (⋮) and select "Delete," review the warning about permanent deletion, type the skill name to confirm, and click "Delete Skill." Deletion cannot be undone. In-progress investigations may be affected if they attempt to load the deleted skill. For skills uploaded as zip files, download the zip file before deleting as a backup. Consider deactivating the skill instead of deleting it if you may need it again.

## Migrating from Runbooks

Existing Runbooks are automatically migrated to Skills with no customer action required. When your Agent Space transitions to the Skills model, all Runbooks are converted to Skills and appear in your Skills UI. After migration, you can:

- **Review migrated Skills** – Check that the automatic migration correctly converted your Runbooks.
- **Update as needed** – Edit Skills directly in the UI to refine instructions, update descriptions, or configure agent type targeting.
- **Expand with references** – For Skills that would benefit from additional reference materials or architecture diagrams, re-create them as zip upload skills with a references/ or assets/ directory.
- **Create new Skills** – Add new Skills for investigation workflows not previously covered by Runbooks.

Contact AWS Support if you encounter any issues with automatically migrated Skills or need assistance with post-migration updates.
