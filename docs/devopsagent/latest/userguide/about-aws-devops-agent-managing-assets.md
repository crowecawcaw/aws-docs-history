# Managing assets

AWS DevOps Agent stores the configuration and reference material for an Agent Space as **assets**, the customer-managed resources that shape what the agent knows and how it behaves. Skills, AGENTS.md files, and attachments are all assets, and you can create, read, update, and delete them programmatically through the Asset API.

To configure what AWS DevOps Agent knows and how it behaves, manage assets in your Agent Space. This topic covers the asset model, IAM permissions, and the metadata each asset type expects. Use the AWS CLI, the AWS SDK for Python (Boto3), or AWS CloudFormation to manage assets end-to-end. For the conceptual overview of skills themselves, see [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills.md "about-aws-devops-agent-devops-agent-skills.md"). For agent-generated knowledge that you do not create yourself, see [Learned Skills](about-aws-devops-agent-learned-skills.md "about-aws-devops-agent-learned-skills.md").

## When to use the Asset API

The Operator Web App is the fastest way to author a single skill or upload an AGENTS.md file interactively. The Asset API exposes the same operations programmatically so that scripts and automation can manage assets without going through the Web App. Common reasons to call the Asset API directly include:

- Authoring or updating an asset from a script, terminal, or notebook instead of the Web App.
- Bulk-loading a starter set of skills or AGENTS.md files into a new Agent Space.
- Reading an asset's contents to back it up or compare versions.

Every operation in the Asset API is exposed through the AWS CLI as `aws devops-agent <operation>` and through the AWS SDKs as the `devops-agent` client.

## Asset API operations

The Asset API exposes the following operations. Each row lists the IAM action you must grant to call the operation and the resource the action applies to. Every action lives in the `aidevops:` namespace and, except for `ListAssetTypes`, applies to an Agent Space resource of the form `arn:aws:aidevops:<region>:<account-id>:agentspace/<agentSpaceId>`. For broader background on `aidevops:` permissions, see [DevOps Agent IAM permissions](aws-devops-agent-security-devops-agent-iam-permissions.md "aws-devops-agent-security-devops-agent-iam-permissions.md").

| Operation           | Description                                                                                                                         | IAM action                   | Resource    |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------- |
| `ListAssetTypes`    | List the asset types supported by AWS DevOps Agent.                                                                                 | `aidevops:ListAssetTypes`    | `*`         |
| `CreateAsset`       | Create a new asset in an Agent Space (skill, AGENTS.md, attachment, custom agent, memory store, memory, test profile, or feedback). | `aidevops:CreateAsset`       | Agent Space |
| `GetAsset`          | Retrieve an asset's metadata and version information.                                                                               | `aidevops:GetAsset`          | Agent Space |
| `UpdateAsset`       | Update the metadata or content of an existing asset.                                                                                | `aidevops:UpdateAsset`       | Agent Space |
| `DeleteAsset`       | Delete an asset and all of its files from an Agent Space.                                                                           | `aidevops:DeleteAsset`       | Agent Space |
| `ListAssets`        | List assets in an Agent Space, with optional filtering by asset type.                                                               | `aidevops:ListAssets`        | Agent Space |
| `ListAssetVersions` | List the historical versions of an asset.                                                                                           | `aidevops:ListAssetVersions` | Agent Space |
| `GetAssetContent`   | Download an asset's full content as a zip bundle.                                                                                   | `aidevops:GetAssetContent`   | Agent Space |
| `CreateAssetFile`   | Add a new file to an existing asset.                                                                                                | `aidevops:CreateAssetFile`   | Agent Space |
| `GetAssetFile`      | Retrieve a single file from an asset by its path.                                                                                   | `aidevops:GetAssetFile`      | Agent Space |
| `UpdateAssetFile`   | Replace the content or metadata of an existing file in an asset.                                                                    | `aidevops:UpdateAssetFile`   | Agent Space |
| `DeleteAssetFile`   | Remove a single file from an asset.                                                                                                 | `aidevops:DeleteAssetFile`   | Agent Space |
| `ListAssetFiles`    | List the files within an asset.                                                                                                     | `aidevops:ListAssetFiles`    | Agent Space |

### Example IAM policies

The following policy grants full management access to assets in a single Agent Space:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aidevops:CreateAsset",
        "aidevops:GetAsset",
        "aidevops:UpdateAsset",
        "aidevops:DeleteAsset",
        "aidevops:ListAssets",
        "aidevops:ListAssetVersions",
        "aidevops:GetAssetContent",
        "aidevops:CreateAssetFile",
        "aidevops:GetAssetFile",
        "aidevops:UpdateAssetFile",
        "aidevops:DeleteAssetFile",
        "aidevops:ListAssetFiles"
      ],
      "Resource": "arn:aws:aidevops:us-east-1:111122223333:agentspace/8f6187a7-0388-4926-8217-3a0fe32f757c"
    },
    {
      "Effect": "Allow",
      "Action": "aidevops:ListAssetTypes",
      "Resource": "*"
    }
  ]
}
```

The following policy grants read-only access to assets in a single Agent Space:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aidevops:GetAsset",
        "aidevops:ListAssets",
        "aidevops:ListAssetVersions",
        "aidevops:GetAssetContent",
        "aidevops:GetAssetFile",
        "aidevops:ListAssetFiles"
      ],
      "Resource": "arn:aws:aidevops:us-east-1:111122223333:agentspace/8f6187a7-0388-4926-8217-3a0fe32f757c"
    },
    {
      "Effect": "Allow",
      "Action": "aidevops:ListAssetTypes",
      "Resource": "*"
    }
  ]
}
```

## Asset types

Every asset has an `assetType` string that identifies what kind of resource it is. You can create eight asset types through the Asset API: `skill`, `agents_md`, `attachment`, `custom_agent`, `memory_store`, `memory`, `test_profile`, and `feedback`. The sections that follow describe each type. You can also call `ListAssetTypes` to retrieve the type identifiers at runtime.

Each asset carries a free-form `metadata` JSON object that describes the resource. The keys inside `metadata` use snake\_case (for example, `agent_types`, `skill_type`). The keys outside `metadata`, at the top level of the request body, use camelCase (for example, `agentSpaceId`, `assetType`, `clientToken`). The required and optional `metadata` keys depend on the asset type, as described in the sections that follow.

When you call `UpdateAsset` or `UpdateAssetFile`, the service applies PATCH semantics to `metadata`: keys that you include are replaced, and keys that you omit retain their stored values. You cannot change an asset's `assetType` after it has been created.

### skill

A `skill` asset packages instructions and reference material that the agent loads when relevant. A simple skill is a single `SKILL.md` file; a complex skill is a zip bundle that contains a `SKILL.md` file plus optional `references/` or `assets/` directories.

**Required `metadata` properties:**

- **name** (string) – A unique identifier for the skill. Lowercase letters, numbers, and hyphens only, 1–64 characters. Must not start or end with a hyphen. Required for simple skills only. For zip uploads the service reads `name` from the `SKILL.md` frontmatter and any value supplied here is ignored.
- **description** (string) – A 1–1024 character explanation of when the agent should use the skill. Required for simple skills only. For zip uploads the service reads `description` from the `SKILL.md` frontmatter and any value supplied here is ignored.
- **agent\_types** (array of strings) – One or more agent types this skill applies to. Use `["GENERIC"]` to make the skill available to all agent types. Other values include `CHAT`, `INCIDENT_TRIAGE`, `INCIDENT_RCA`, `INCIDENT_MITIGATION`, `PREVENTION`, `RELEASE_READINESS_REVIEW`, and `RELEASE_TESTING`. The `GENERIC` value cannot be combined with other values.

**Optional `metadata` properties:**

- **skill\_type** (string) – Defaults to `USER`. The Asset API only allows customer-created skills, so the only accepted value is `USER`. The service rejects requests that set `skill_type` to `LEARNED`, which is reserved for skills generated by the agent itself.
- **status** (string) – Activation state of the skill. Accepted values are `ACTIVE` and `INACTIVE` (uppercase only). Defaults to `ACTIVE`. Inactive skills remain in the Agent Space but are not loaded by the agent during investigations or chat. Use `UpdateAsset` with `metadata.status` to deactivate or reactivate a skill without deleting it. Skills are the only asset type that supports activation; the `status` field is ignored on every other asset type. See [Activating and deactivating skills](#activating-and-deactivating-skills "#activating-and-deactivating-skills") for a worked example.
- **enable\_tools** (array of strings) – A list of tool identifiers that the agent can call when it loads this skill.

**Example `metadata`:**

```
{
  "name": "rds-performance-investigation",
  "description": "Investigation procedures for RDS performance issues including connection exhaustion, slow queries, replication lag, and storage capacity. Use this skill when investigating database latency, connection errors, or read/write performance degradation.",
  "agent_types": ["GENERIC"]
}
```

**Limits:** Zip uploads must not exceed 6 MB. An Agent Space can contain up to 200 user-created skills.

### agents\_md

An `agents_md` asset is a markdown file containing standing agent instructions for a specific agent type. The agent loads the matching AGENTS.md at the start of every task. For more information about agent instructions, see [Agent instructions](about-aws-devops-agent-agent-instructions.md "about-aws-devops-agent-agent-instructions.md").

**Required `metadata` properties:**

- **agent\_type** (string) – The agent type the AGENTS.md file applies to. Valid values are `GENERIC`, `CHAT`, `INCIDENT_TRIAGE`, `INCIDENT_RCA`, `INCIDENT_MITIGATION`, `PREVENTION`, `RELEASE_READINESS_REVIEW`, and `RELEASE_TESTING`.

**Example `metadata`:**

```
{
  "agent_type": "INCIDENT_TRIAGE"
}
```

**Limits:** Each Agent Space can contain at most one AGENTS.md per `agent_type`. The file content must be markdown (`text/markdown`) and must not exceed 25 KB.

### attachment

An `attachment` asset stores a binary or text file that the agent can reference during investigations, for example, an architecture diagram, a runbook PDF, or a sample log file.

**Required `metadata` properties:**

- **filename** (string) – The original file name, including the base name and any extension (for example, `topology.png`).
- **extension** (string) – The file extension without the leading dot (for example, `png`, `pdf`, `csv`).
- **size** (number) – The size of the file in bytes.

**Example `metadata`:**

```
{
  "filename": "topology.png",
  "extension": "png",
  "size": 184320
}
```

**Limits:** The total size of all attachments in an Agent Space cannot exceed 10 GB.

### custom\_agent

A `custom_agent` asset defines a specialized agent configuration with a curated set of tools, skills, and attached memory stores. Use a custom agent to scope the agent to a specific workflow or set of capabilities.

**Required `metadata` properties:**

- **name** (string) – A unique identifier for the custom agent. Lowercase letters, numbers, and hyphens only, 1–64 characters. Must not start or end with a hyphen.

**Optional `metadata` properties:**

- **tools** (array of strings) – The tool identifiers the custom agent is allowed to use. Defaults to an empty list when omitted.
- **skills** (array of strings) – The skill identifiers the custom agent loads. Defaults to an empty list when omitted.
- **memory\_stores** (array of strings) – The identifiers of the memory stores the custom agent can read and write. Defaults to an empty list when omitted. A custom agent accesses only the stores listed here.

**Example `metadata`:**

```
{
  "name": "rds-firefighter",
  "tools": ["cloudwatch:GetMetricData", "rds:DescribeDBInstances"],
  "skills": ["rds-performance-investigation"],
  "memory_stores": ["incident-runbooks"]
}
```

### memory\_store

A `memory_store` asset is a container that groups related memory files. The agent reads the store's name and description to decide whether to open it and list the memories inside. Memories and memory stores support agent memory. For more information about memories, see [DevOps Agent Memories](about-aws-devops-agent-devops-agent-memories.md "about-aws-devops-agent-devops-agent-memories.md").

Create memories in two steps. First, create the `memory_store`. Then, create each `memory` inside it, as described in [memory](#memory "#memory").

**Required `metadata` properties:**

- **name** (string) – A unique identifier for the memory store. Lowercase letters, numbers, and hyphens only, 1–128 characters. Must not start or end with a hyphen.
- **description** (string) – A 1–1024 character description of what the store holds. The agent uses it to decide whether to open the store.
- **agent\_types** (array of strings) – One or more agent types that can see the store. Use `["GENERIC"]` to make the store visible to all agent types. A `CreateAsset` request without a non-empty `agent_types` fails.

**Example `metadata`:**

```
{
  "name": "incident-runbooks",
  "description": "Operational memories about past incidents and their resolutions.",
  "agent_types": ["GENERIC"]
}
```

### memory

A `memory` asset is an individual memory file that belongs to a memory store. The agent reads the memory's name and description to decide whether to read the full file. Create the parent `memory_store` first, and then set `memory_store_id` on the memory to the store's asset ID.

**Required `metadata` properties:**

- **name** (string) – An identifier for the memory, written as a `/`-separated path of lowercase kebab-case segments, 1–255 characters (for example, `databases/rds-failover`).
- **description** (string) – A 1–1024 character description of what the memory contains.
- **memory\_store\_id** (string) – The asset ID of the memory store this memory belongs to.

**Example `metadata`:**

```
{
  "name": "databases/rds-failover",
  "description": "Steps that resolved the RDS failover incident in June.",
  "memory_store_id": "a1b2c3d4-5678-90ab-cdef-example11111"
}
```

### test\_profile

A `test_profile` asset stores a reusable configuration for a release-testing run, including the kind of testing to perform and the target endpoint.

**Required `metadata` properties:**

- **test\_agent\_type** (string) – The type of testing this profile performs. Valid values are `releaseUiTesting` and `releaseApiTesting`.
- **target\_url** (string) – The URL the test run targets.

**Optional `metadata` properties:**

- **name** (string) – A human-readable identifier for the test profile. Lowercase letters, numbers, and hyphens only, 1–128 characters. Must not start or end with a hyphen.
- **description** (string) – A 1–1024 character description of what the test profile covers.
- **test\_personas** (array of strings) – The personas to exercise during the test run. Valid values are `guest` and `authenticated`.
- **api\_spec** (string) – An API specification for the test run. Relevant for `releaseApiTesting`.
- **credentials\_secret\_arn** (string) – The ARN of an AWS Secrets Manager secret holding credentials for the test run.

**Example `metadata`:**

```
{
  "name": "checkout-api-tests",
  "description": "Release API tests for the checkout service.",
  "test_agent_type": "releaseApiTesting",
  "target_url": "https://api.example.com",
  "test_personas": ["guest", "authenticated"],
  "api_spec": "openapi: 3.0.0",
  "credentials_secret_arn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:checkout-creds"
}
```

### feedback

A `feedback` asset records customer-provided feedback on a single agent execution. Use feedback assets to capture verdicts and notes that downstream evaluation pipelines can aggregate.

**Required `metadata` properties:**

- **agent\_types** (array of strings) – The agent types that produced the execution. Must contain at least one value (for example, `INCIDENT_TRIAGE`).

**Optional `metadata` properties:**

- **execution\_id** (string) – The execution this feedback is associated with. Set this on `CreateAsset`; it cannot be changed by `UpdateAsset`.

**Example `metadata`:**

```
{
  "execution_id": "b2c3d4e5-6789-01ab-cdef-example22222",
  "agent_types": ["INCIDENT_TRIAGE"]
}
```

## Asset content: file or zip

Every `CreateAsset` request includes a `content` object that holds the bytes the asset stores. The shape of `content` depends on whether you are uploading a single file or a zip bundle:

- **Single text file** – `content.file.body.text` carries up to 1.5 MB of UTF-8 text. Use this for simple skills and AGENTS.md files.

`json { "content": { "file": { "path": "SKILL.md", "body": { "text": "# Skill\n\nInstructions go here." } } } }`

- **Single binary file** – `content.file.body.bytes` carries up to 6 MB of base64-encoded binary content. Use this for attachments such as images or PDFs. Because the blob is nested inside the `content` union, base64-encode the file ahead of time and submit the request with `--cli-input-json` (see [Create a skill from a binary file](#create-a-skill-from-a-binary-file "#create-a-skill-from-a-binary-file") for a worked example).

`json { "content": { "file": { "path": "topology.png", "body": { "bytes": "<base64-encoded bytes>" } } } }`

- **Zip bundle** – `content.zip.zipFile` carries a base64-encoded zip archive of up to 6 MB. Use this for skills that include a `SKILL.md` plus additional files in a `references/` or `assets/` directory.

`json { "content": { "zip": { "zipFile": "<base64-encoded zip bytes>" } } }`

To add, replace, or delete individual files inside an existing asset without re-uploading the whole bundle, use `CreateAssetFile`, `UpdateAssetFile`, and `DeleteAssetFile`.

## Managing a skill end-to-end

The walkthrough that follows creates a skill three different ways (from a single text file, from a binary file, and from a zip bundle), and then exercises the read, update, and delete operations. Replace `8f6187a7-0388-4926-8217-3a0fe32f757c` with your Agent Space ID.

### Create a skill from a single text file

This is the simplest path: a single `SKILL.md` file uploaded inline. Because the upload contains exactly one text file, you must supply `name` and `description` in `metadata`.

**AWS CLI:**

```
aws devops-agent create-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-type skill \
  --metadata '{
    "name": "rds-performance-investigation",
    "description": "Investigation procedures for RDS performance issues. Use when investigating database latency, connection errors, or query timeouts.",
    "agent_types": ["GENERIC"]
  }' \
  --content '{
    "file": {
      "path": "SKILL.md",
      "body": {
        "text": "# RDS Performance Investigation\n\nUse this skill when customers report database latency, connection errors, query timeouts, or read/write performance degradation."
      }
    }
  }'
```

**Python (Boto3):**

```
import boto3

client = boto3.client("devops-agent")

response = client.create_asset(
    agentSpaceId="8f6187a7-0388-4926-8217-3a0fe32f757c",
    assetType="skill",
    metadata={
        "name": "rds-performance-investigation",
        "description": (
            "Investigation procedures for RDS performance issues. "
            "Use when investigating database latency, connection errors, "
            "or query timeouts."
        ),
        "agent_types": ["GENERIC"],
    },
    content={
        "file": {
            "path": "SKILL.md",
            "body": {
                "text": (
                    "# RDS Performance Investigation\n\n"
                    "Use this skill when customers report database latency, "
                    "connection errors, query timeouts, or read/write "
                    "performance degradation."
                )
            },
        }
    },
)

asset_id = response["asset"]["assetId"]
```

### Create a skill from a binary file

Use a binary upload when the skill content is not UTF-8 text. The example below uploads a pre-rendered PDF as the skill body. Because the request body contains a base64-encoded blob nested inside the `content` union, supply the request from a JSON file with `--cli-input-json` and base64-encode the blob ahead of time.

The `-w 0` flag below tells GNU `base64` to emit the encoded blob on a single line; without it the default 76-character line wrap inserts newlines that produce invalid JSON when the blob is interpolated into the heredoc. On macOS, use `base64 -i ops-runbook.pdf` (the BSD `base64` does not wrap by default).

**Build the request body:**

```
base64 -w 0 ops-runbook.pdf > ops-runbook.b64
cat > create-skill.json <<EOF
{
  "agentSpaceId": "8f6187a7-0388-4926-8217-3a0fe32f757c",
  "assetType": "skill",
  "metadata": {
    "name": "ops-runbook",
    "description": "Operations runbook covering on-call escalation paths.",
    "agent_types": ["GENERIC"]
  },
  "content": {
    "file": {
      "path": "SKILL.pdf",
      "body": { "bytes": "$(cat ops-runbook.b64)" }
    }
  }
}
EOF
```

**AWS CLI:**

```
aws devops-agent create-asset --cli-input-json file://create-skill.json
```

**Python (Boto3):**

```
with open("ops-runbook.pdf", "rb") as f:
    body_bytes = f.read()

response = client.create_asset(
    agentSpaceId="8f6187a7-0388-4926-8217-3a0fe32f757c",
    assetType="skill",
    metadata={
        "name": "ops-runbook",
        "description": "Operations runbook covering on-call escalation paths.",
        "agent_types": ["GENERIC"],
    },
    content={
        "file": {
            "path": "SKILL.pdf",
            "body": {"bytes": body_bytes},
        }
    },
)
```

### Create a skill from a zip bundle

Use a zip upload when the skill includes more than one file, for example, a `SKILL.md` plus reference material and assets. For zip uploads the service reads `name` and `description` from the `SKILL.md` frontmatter, so do not include them in `metadata`.

The zip layout looks like:

```
rds-performance-investigation.zip
├── SKILL.md
├── references/
│   └── rds-metrics-reference.md
└── assets/
    └── rds-investigation-flowchart.png
```

`SKILL.md` must include frontmatter so the service can extract the name and description:

```
---
name: rds-performance-investigation
description: Investigation procedures for RDS performance issues including
  connection exhaustion, slow queries, replication lag, and storage capacity.
  Use this skill when investigating database latency, connection errors, or
  read/write performance degradation.
---

# RDS Performance Investigation
...
```

**Build the request body:**

```
base64 -w 0 rds-performance-investigation.zip > skill.zip.b64
cat > create-skill.json <<EOF
{
  "agentSpaceId": "8f6187a7-0388-4926-8217-3a0fe32f757c",
  "assetType": "skill",
  "metadata": { "agent_types": ["GENERIC"] },
  "content": {
    "zip": { "zipFile": "$(cat skill.zip.b64)" }
  }
}
EOF
```

**AWS CLI:**

```
aws devops-agent create-asset --cli-input-json file://create-skill.json
```

**Python (Boto3):**

```
with open("rds-performance-investigation.zip", "rb") as f:
    zip_bytes = f.read()

response = client.create_asset(
    agentSpaceId="8f6187a7-0388-4926-8217-3a0fe32f757c",
    assetType="skill",
    metadata={"agent_types": ["GENERIC"]},
    content={"zip": {"zipFile": zip_bytes}},
)
```

### Import a skill from a repository

You can create a skill by importing it directly from a GitHub repository directory. AWS DevOps Agent fetches the skill content, extracts the name and description from the SKILL.md frontmatter, and creates the skill in your Agent Space. This lets you manage skills in version control and import or sync them programmatically.

**Prerequisites:**

- Your Agent Space must have a GitHub account associated. See [Connecting GitHub](connecting-to-cicd-pipelines-connecting-github.md "connecting-to-cicd-pipelines-connecting-github.md").
- The repository directory must contain a valid SKILL.md file with frontmatter.

**AWS CLI:**

```
aws devops-agent create-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-type skill \
  --metadata '{ "agent_types": ["GENERIC"] }' \
  --content '{"sourceUrl": {"url": "https://github.com/my-org/my-repo/tree/main/skills/rds-investigation"}}'
```

**Python (Boto3):**

```
response = client.create_asset(
    agentSpaceId="8f6187a7-0388-4926-8217-3a0fe32f757c",
    assetType="skill",
    metadata={"agent_types": ["GENERIC"]},
    content={
        "sourceUrl": {
            "url": "https://github.com/my-org/my-repo/tree/main/skills/rds-investigation"
        }
    },
)

asset_id = response["asset"]["assetId"]
```

The service fetches the directory contents, reads the SKILL.md frontmatter for `name` and `description`, and imports all files. Do not include `name` or `description` in `metadata`—they are extracted from the frontmatter automatically.

**Syncing an imported skill:**

To pull the latest changes from the repository, call `UpdateAsset` with `content.sourceUrl`:

```
aws devops-agent update-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-id <assetId> \
  --content '{"sourceUrl": {"url": "https://github.com/my-org/my-repo/tree/main/skills/rds-investigation"}}'
```

```
response = client.update_asset(
    agentSpaceId="8f6187a7-0388-4926-8217-3a0fe32f757c",
    assetId="<assetId>",
    content={
        "sourceUrl": {
            "url": "https://github.com/my-org/my-repo/tree/main/skills/rds-investigation"
        }
    },
)
```

Syncing replaces the skill content entirely with the current state of the repository directory. Editable fields (status, agent types) are preserved.

**Viewing the import source:**

`GetAsset` returns the source information in `metadata.source` for repository-imported skills:

```
{
  "metadata": {
    "name": "rds-performance-investigation",
    "description": "Investigation procedures for RDS performance issues...",
    "source": {
      "url": "https://github.com/my-org/my-repo/tree/main/skills/rds-investigation",
      "lastSyncedAt": 1718467200
    },
    "agent_types": ["GENERIC"],
    "skill_type": "USER",
    "status": "ACTIVE"
  }
}
```

**Constraints:**

- Only GitHub URLs are accepted. You can point to a directory containing a SKILL.md (for example, `https://github.com/org/repo/tree/main/skills/my-skill`), which imports the entire directory including reference files. If the SKILL.md is at the root of the repository, you can also link directly to the file (for example, `https://github.com/org/repo/blob/main/SKILL.md`), which imports only the SKILL.md.
- The directory must contain a SKILL.md with valid frontmatter.
- Total directory size must not exceed 6 MB and at most 100 files.
- `content.sourceUrl` is mutually exclusive with `content.file` and `content.zip`—you cannot combine them in the same request.
- A metadata-only update (without `content`) preserves the existing import source and does not re-fetch from the repository.

### Get, list, update, and delete

Use `GetAsset` to retrieve a single asset by ID:

```
aws devops-agent get-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-id <assetId>
```

Use `ListAssets` to page through every asset in an Agent Space:

```
aws devops-agent list-assets \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --max-results 50

aws devops-agent list-assets \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --max-results 50 \
  --next-token <token>
```

Use `UpdateAsset` to change one or more `metadata` fields without re-uploading content. Keys that you omit keep their existing values:

```
aws devops-agent update-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-id <assetId> \
  --metadata '{ "agent_types": ["INCIDENT_TRIAGE", "INCIDENT_RCA"] }'
```

Use `ListAssetVersions` to inspect the version history of an asset. Each successful `UpdateAsset` or `UpdateAssetFile` call advances the asset's version number:

```
aws devops-agent list-asset-versions \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-id <assetId>
```

Use `DeleteAsset` to remove the asset and all of its files:

```
aws devops-agent delete-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-id <assetId>
```

### Add a single file to an existing skill

If you already created a skill from a zip bundle and want to add one new reference file, you do not need to re-upload the whole bundle. Use `CreateAssetFile`:

```
aws devops-agent create-asset-file \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-id <assetId> \
  --path references/troubleshooting.md \
  --content '{ "text": "# Troubleshooting\n\nAdditional notes." }'
```

To replace the file in place, use `update-asset-file` with the same arguments. To remove it, use `delete-asset-file`.

### Activating and deactivating skills

Skills carry an activation state in `metadata.status`. New skills are `ACTIVE` by default and are loaded by the agent during investigations and chat. You can deactivate a skill to take it out of rotation without deleting it, for example while you investigate why it is producing unexpected results, and reactivate it later.

**Set the initial state on create** by including `metadata.status` in the `CreateAsset` request:

```
aws devops-agent create-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-type skill \
  --metadata '{
    "name": "rds-performance-investigation",
    "description": "Investigation procedures for RDS performance issues.",
    "agent_types": ["GENERIC"],
    "status": "INACTIVE"
  }' \
  --content '{
    "file": {
      "path": "SKILL.md",
      "body": { "text": "# RDS Performance Investigation" }
    }
  }'
```

**Deactivate an existing skill** with `UpdateAsset`. Because `metadata` is applied as a partial update, sending only `status` leaves every other field intact:

```
aws devops-agent update-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-id <assetId> \
  --metadata '{ "status": "INACTIVE" }'
```

**Reactivate** the same way, with `"status": "ACTIVE"`:

```
aws devops-agent update-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-id <assetId> \
  --metadata '{ "status": "ACTIVE" }'
```

`GetAsset` and `ListAssets` always include the current `status` in `metadata` for skill assets, so you can read the live activation state at any time.

The `status` field is case-sensitive. Only `ACTIVE` and `INACTIVE` (uppercase) are accepted. Any other value fails with a `ValidationException`. Activation applies only to skills; setting `metadata.status` on any other asset type has no effect and the field is dropped from the response.

## Managing assets with AWS CloudFormation

Use the Asset API for interactive or script-driven changes. To manage assets declaratively, model them as `AWS::DevOpsAgent::Asset` resources in AWS CloudFormation. With this approach, you can version-control your assets alongside your other infrastructure, deploy them through a pipeline, and reproduce them across Agent Spaces. CloudFormation creates each asset as a child of a parent Agent Space, so an asset you define in a template maps to exactly the same resource a `CreateAsset` call produces.

You manage every asset type through the same `AWS::DevOpsAgent::Asset` resource. The supported types are `skill`, `agents_md`, `attachment`, `custom_agent`, `memory_store`, `memory`, `test_profile`, and `feedback`. Only the `AssetType`, `Metadata`, and content differ from one type to the next. The following examples create a skill and a custom agent; the other types follow the same shape, using the metadata described in [Asset types](#asset-types "#asset-types").

### The AWS::DevOpsAgent::Asset resource

The resource properties map directly to the `CreateAsset` request fields described earlier in this topic:

| CloudFormation property   | Type    | Maps to                         | Notes                                                                                                                                                    |
| ------------------------- | ------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AgentSpaceId`            | String  | `agentSpaceId`                  | Required. Create-only—changing it replaces the asset.                                                                                                    |
| `AssetType`               | String  | `assetType`                     | Required. Create-only. The asset type identifier—for example `skill` or `custom_agent`. Any type in [Asset types](#asset-types "#asset-types") is valid. |
| `Metadata`                | JSON    | `metadata`                      | The same metadata document as the API (for a skill: `name`, `description`, `agent_types`, and optionally `status`). Updated in place.                    |
| `Files`                   | List    | `content.file`                  | Inline files, each with `Path` and either `ContentText` or `ContentBytes`, plus optional per-file `Metadata`. Mutually exclusive with `Zip`.             |
| `Zip`                     | String  | `content.zip.zipFile`           | Base64-encoded zip bundle. Mutually exclusive with `Files`.                                                                                              |
| `AssetId`                 | String  | `asset.assetId`                 | Read-only. Retrieve with `Fn::GetAtt`.                                                                                                                   |
| `Arn`                     | String  | `asset.arn`                     | Read-only. The asset ARN, nested under the parent Agent Space.                                                                                           |
| `Version`                 | Integer | `asset.version`                 | Read-only. Bumps on every successful update.                                                                                                             |
| `CreatedAt` / `UpdatedAt` | String  | `asset.createdAt` / `updatedAt` | Read-only timestamps.                                                                                                                                    |

Two behaviors are worth calling out before you write a template:

- **`AgentSpaceId` and `AssetType` are create-only.** Changing either one replaces the asset. CloudFormation creates a new asset with a new `AssetId` and `Arn`, then deletes the old one. Content and metadata changes update the existing asset in place.
- **CloudFormation manages the asset as a whole** —its metadata and its complete file set. To change a skill, edit the template and update the stack. Operations that act on parts of an asset are not part of the resource and remain API-only. This includes per-file edits (`CreateAssetFile`, `UpdateAssetFile`, `DeleteAssetFile`) and version history (`ListAssetVersions`). It also includes content download (`GetAssetContent`) and repository import and sync (the `sourceUrl` content type). For those, use the AWS CLI or an SDK as shown earlier in this topic.

### Create a skill

The following template creates the single-file `rds-performance-investigation` skill used in the AWS CLI walkthrough. It takes the parent Agent Space ID as a parameter and exports the new asset's ID and ARN.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: A DevOps Agent skill managed as an AWS::DevOpsAgent::Asset resource.

Parameters:
  AgentSpaceId:
    Type: String
    Description: The ID of the Agent Space that owns the skill.

Resources:
  RdsPerformanceSkill:
    Type: AWS::DevOpsAgent::Asset
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      AssetType: skill
      Metadata:
        name: rds-performance-investigation
        description: Investigation procedures for RDS performance issues.
        agent_types:
          - GENERIC
      Files:
        - Path: SKILL.md
          ContentText: |
            # RDS Performance Investigation

            Use this skill when customers report database latency, connection
            errors, query timeouts, or read/write performance degradation.

Outputs:
  SkillAssetId:
    Value: !GetAtt RdsPerformanceSkill.AssetId
  SkillArn:
    Value: !GetAtt RdsPerformanceSkill.Arn
```

Deploy it with the AWS CLI, passing your Agent Space ID:

```
aws cloudformation deploy \
  --template-file skill.yaml \
  --stack-name DevOpsAgentSkillStack \
  --parameter-overrides AgentSpaceId=8f6187a7-0388-4926-8217-3a0fe32f757c \
  --region <REGION>
```

A skill that ships more than one file—for example a `SKILL.md` plus a reference document—adds more entries to `Files`:

```
      Files:
        - Path: SKILL.md
          ContentText: |
            # RDS Performance Investigation
            Investigation entry point.
        - Path: references/rds-metrics-reference.md
          ContentText: |
            # RDS metrics reference
            Key CloudWatch metrics to check.
```

To create the skill deactivated, or to deactivate it later, set `status` in `Metadata` (see [Activating and deactivating skills](#activating-and-deactivating-skills "#activating-and-deactivating-skills")) and update the stack:

```
      Metadata:
        name: rds-performance-investigation
        description: Investigation procedures for RDS performance issues.
        agent_types:
          - GENERIC
        status: INACTIVE
```

### Create a custom agent

A custom agent is the same resource with a different `AssetType`, `Metadata`, and content. The following template creates an `incident-runbooks` memory store, then a `custom_agent` asset that curates a set of tools, skills, and attached memory stores. The `skills` and `memory_stores` lists reference assets by their `name` metadata—here, the `rds-performance-investigation` skill you created earlier and the `incident-runbooks` store defined alongside the agent. Because those references are by name, use `DependsOn` so the store is created before the agent that attaches it.

```
  IncidentRunbooksStore:
    Type: AWS::DevOpsAgent::Asset
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      AssetType: memory_store
      Metadata:
        name: incident-runbooks
        description: Standing runbooks and known issues for incident response.
        agent_types:
          - GENERIC
      Files:
        - Path: README.md
          ContentText: |
            Operational memories for incident response.

  RdsFirefighter:
    Type: AWS::DevOpsAgent::Asset
    DependsOn: IncidentRunbooksStore
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      AssetType: custom_agent
      Metadata:
        name: rds-firefighter
        tools:
          - cloudwatch:GetMetricData
          - rds:DescribeDBInstances
        skills:
          - rds-performance-investigation
        memory_stores:
          - incident-runbooks
      Files:
        - Path: AGENT.md
          ContentText: |
            # RDS Firefighter
            Custom agent for RDS incidents.
```

The other asset types work the same way—set `AssetType` and supply the `Metadata` keys that type requires (see [Asset types](#asset-types "#asset-types")). For example, an `agents_md` asset sets `AssetType: agents_md` with `Metadata` containing `agent_type: INCIDENT_TRIAGE` and an `AGENTS.md` file.

### Schedule the custom agent with a trigger

To run the custom agent automatically, add an `AWS::DevOpsAgent::Trigger` resource. A trigger is a child of the Agent Space. Its action references the custom agent to run by asset ID, in the form `custom:<assetId>`. Use `Fn::GetAtt` to pass the custom agent's `AssetId` so CloudFormation wires the two resources together and orders their creation.

The following trigger runs the `rds-firefighter` custom agent once a day:

```
  DailyRdsCheck:
    Type: AWS::DevOpsAgent::Trigger
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      Type: TIME_BASED
      Condition:
        Schedule:
          Expression: rate(1 day)
      Action:
        actionType: create:task
        task:
          agent: !Sub
            - custom:${AssetId}
            - AssetId: !GetAtt RdsFirefighter.AssetId
      Status: Active
```

The `AgentSpaceId`, `Type`, `Condition`, and `Action` properties are create-only. Changing any of them replaces the trigger. The `Status` property accepts `Active` or `Inactive` and can be updated in place. Set it to `Inactive` to pause the trigger without deleting it. For more information about schedule expression syntax, see [Executing custom agents](custom-agents-executing-custom-agents.md "custom-agents-executing-custom-agents.md").

`AWS::DevOpsAgent::Asset` and `AWS::DevOpsAgent::Trigger` are available in the AWS Regions where AWS DevOps Agent is offered. For more information about supported AWS Regions, see [Supported Regions](about-aws-devops-agent-supported-regions.md "about-aws-devops-agent-supported-regions.md"). To deploy the parent Agent Space, IAM roles, and operator app as infrastructure as code, see [Getting started with AWS DevOps Agent using AWS CloudFormation](getting-started-with-aws-devops-agent-getting-started-with-aws-devops-agent-using-aws-cloudformation.md "getting-started-with-aws-devops-agent-getting-started-with-aws-devops-agent-using-aws-cloudformation.md").

## Examples for the other asset types

The skill walkthrough above applies to every other asset type. The only difference is the `metadata` block and, for attachments, the choice of binary content. The minimal `CreateAsset` calls below illustrate each type.

Memory stores and memories use the same `CreateAsset` operation—create the store first, then a memory in it. For the metadata each accepts, see [memory\_store](#memory_store "#memory_store") and [memory](#memory "#memory") ; for a memory-store example with the AWS CLI, see the [AWS DevOps Agent CLI onboarding guide](getting-started-with-aws-devops-agent-cli-onboarding-guide.md "getting-started-with-aws-devops-agent-cli-onboarding-guide.md"). The following creates a memory in an existing store, using the store's `assetId` as `memory_store_id`:

```
aws devops-agent create-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-type memory \
  --metadata '{
    "name": "alarms/checkout-latency",
    "description": "The checkout latency alarm is expected to spike during nightly batch jobs.",
    "memory_store_id": "<MEMORY_STORE_ASSET_ID>"
  }' \
  --content '{
    "file": {
      "path": "checkout-latency.md",
      "body": { "text": "# Checkout latency\n\nExpected to spike during nightly batch jobs." }
    }
  }'
```

**Create an AGENTS.md:**

```
aws devops-agent create-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-type agents_md \
  --metadata '{ "agent_type": "INCIDENT_TRIAGE" }' \
  --content '{
    "file": {
      "path": "AGENTS.md",
      "body": { "text": "# Triage Instructions\n\nFollow these steps for new incidents." }
    }
  }'
```

**Create an attachment** (binary content; build the request from a JSON file as shown in [Create a skill from a binary file](#create-a-skill-from-a-binary-file "#create-a-skill-from-a-binary-file")):

```
base64 -w 0 topology.png > topology.png.b64
cat > create-attachment.json <<EOF
{
  "agentSpaceId": "8f6187a7-0388-4926-8217-3a0fe32f757c",
  "assetType": "attachment",
  "metadata": {
    "filename": "topology.png",
    "extension": "png",
    "size": 184320
  },
  "content": {
    "file": {
      "path": "topology.png",
      "body": { "bytes": "$(cat topology.png.b64)" }
    }
  }
}
EOF
aws devops-agent create-asset --cli-input-json file://create-attachment.json
```

**Create a custom agent:**

```
aws devops-agent create-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-type custom_agent \
  --metadata '{
    "name": "rds-firefighter",
    "tools": ["cloudwatch:GetMetricData", "rds:DescribeDBInstances"],
    "skills": ["rds-performance-investigation"]
  }' \
  --content '{
    "file": {
      "path": "AGENT.md",
      "body": { "text": "# RDS Firefighter\n\nCustom agent for RDS incidents." }
    }
  }'
```

**Create a test profile:**

```
aws devops-agent create-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-type test_profile \
  --metadata '{
    "name": "checkout-api-tests",
    "test_agent_type": "releaseApiTesting",
    "target_url": "https://api.example.com",
    "test_personas": ["guest", "authenticated"]
  }' \
  --content '{
    "file": {
      "path": "PROFILE.md",
      "body": { "text": "# Checkout API test profile" }
    }
  }'
```

**Create a feedback asset:**

```
aws devops-agent create-asset \
  --agent-space-id 8f6187a7-0388-4926-8217-3a0fe32f757c \
  --asset-type feedback \
  --metadata '{
    "execution_id": "b2c3d4e5-6789-01ab-cdef-example22222",
    "agent_types": ["INCIDENT_TRIAGE"]
  }' \
  --content '{
    "file": {
      "path": "FEEDBACK.md",
      "body": { "text": "{\"verdict\":\"correct\"}" }
    }
  }'
```

**List supported asset types:**

```
aws devops-agent list-asset-types
```
