

# Install skills with the AWS CLI

With the AWS Command Line Interface (AWS CLI), you can install a skill from AWS Agent Registry into the AI coding agents on your computer. You run one command, and you don’t download, verify, or extract the skill package yourself. For instructions on downloading and verifying a skill package yourself, see [Download a skill package](registry-skill-package-download.md).

To work with skills, use the following commands in the `aws agent-registry` command group:
+  `list-skills` – Lists the skills in a registry. For each skill, it also shows the AI coding agents on your computer that the skill is currently installed for.
+  `install-skill` – Downloads a skill and verifies it against the SHA-256 checksum that the registry publishes. It then installs the skill for your AI coding agents.
+  `uninstall-skill` – Removes a skill that `install-skill` installed.
+  `sign-out` – Signs you out of a registry that uses JSON Web Token (JWT) authorization.

The examples on this page use example values, such as the registry ID `a1b2c3d4e5f6g7h8` and the record ID `r1s2t3u4v5w6`. Replace them with your own registry ID, record ID, client ID, and Region.

By default, when you run `install-skill`, you install the skill for every supported agent that the CLI detects on your computer. The CLI detects an agent when the agent’s configuration folder exists, for example `~/.kiro` for Kiro. To install for one agent only, use `--agent`. To install into a folder of your choice instead, use `--target-directory`.

The following table lists the supported agents, the value to pass to `--agent`, and the skills folder that the CLI installs into.


| Agent |  `--agent` value | Skills folder | 
| --- | --- | --- | 
| Claude Code |  `claude-code`  |  `~/.claude/skills`  | 
| Cline |  `cline`  |  `~/.cline/skills`  | 
| Cursor |  `cursor`  |  `~/.cursor/skills`  | 
| Kiro |  `kiro`  |  `~/.kiro/skills`  | 
| Codex, Gemini CLI, OpenCode, and Windsurf |  `universal`, or `codex`, `gemini-cli`, `opencode`, or `windsurf`  |  `~/.agents/skills`  | 

Codex, Gemini CLI, OpenCode, and Windsurf share the `~/.agents/skills` folder. The CLI installs a skill into that folder once, and `list-skills` reports it as `universal`.

## Prerequisites
<a name="registry-skill-install-cli-prerequisites"></a>

Before you use the skill commands, make sure that you have the following:
+ A version of the AWS CLI that includes the `aws agent-registry list-skills` command. To install or update the AWS CLI, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the * AWS Command Line Interface User Guide*.
+ One or more supported AI coding agents on your computer, or a folder to install skills into with `--target-directory`.
+ For a registry that uses AWS Identity and Access Management (IAM) authorization, AWS credentials with the permissions that follow this list.
+ For a registry that uses JWT authorization, a user account in its identity provider, and the client ID that the registry owner set up for the AWS CLI. For more information, see [Set up the identity provider for the AWS CLI](#registry-skill-install-cli-jwt).

For a registry that uses IAM authorization, your AWS credentials need the following permissions on the registry and its skill records:

 `agent-registry:ListDiscoverableRegistryRecords`   
To list skills with `list-skills`, and to install a skill by its record name with `install-skill --record-name`.

 `agent-registry:GetDiscoverableRegistryRecord`   
To install a skill with `install-skill`, and to show `skillName` in the output of `list-skills`.

 `kms:Decrypt` on the registry’s AWS KMS key  
When the registry is encrypted with a customer managed key.

For more information, see [Registry data plane actions](registry-iam-permissions.md#registry-iam-data-plane) and [Permissions for registries encrypted with a customer managed key](registry-iam-permissions.md#registry-iam-skills-kms).

 `uninstall-skill` and `sign-out` need no AWS credentials or permissions. `uninstall-skill` works only on your computer, and `sign-out` contacts only the registry’s identity provider.

## Registries that use IAM or JWT authorization
<a name="registry-skill-install-cli-auth"></a>

A registry authorizes consumers with IAM or with JWT. For more information, see [Supported Inbound Authorization types](registry-supported-auth-types.md).

For a registry that uses IAM authorization, the commands sign requests with your AWS credentials, like other AWS CLI commands. You don’t need any extra options. For more information about setting up your credentials, see [Authentication and access credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html) in the * AWS Command Line Interface User Guide*.

For a registry that uses JWT authorization, add `--authorizer JWT` to `list-skills` and `install-skill`. The CLI then signs you in to the registry’s identity provider and sends a token from it. For more information about how sign-in works, and for an end-to-end example, see [Use a registry that uses JWT authorization](#registry-skill-install-cli-jwt-registries).

The CLI refuses `--no-verify-ssl` for a request that carries a bearer token from `--authorizer JWT`, `AWS_BEARER_TOKEN_AGENT_REGISTRY`, or an IAM Identity Center sign-in. Remove `--no-verify-ssl`, or trust a TLS-inspecting proxy’s certificate authority with `--ca-bundle`.

## Use a registry that uses JWT authorization
<a name="registry-skill-install-cli-jwt-registries"></a>

A registry that uses JWT authorization signs you in with its identity provider instead of your AWS credentials. The following sections show how you sign in and install skills from such a registry, and how the registry owner sets up the identity provider for the AWS CLI.

### Sign in and install skills
<a name="registry-skill-install-cli-jwt-walkthrough"></a>

When you add `--authorizer JWT` to `list-skills` or `install-skill`, the CLI sends a token from the registry’s identity provider. It gets the token as follows:
+ The first time, the CLI opens the identity provider’s sign-in page in your browser. It waits up to 10 minutes for you to sign in.
+ The CLI caches the sign-in in `~/.aws/agent-registry/cache`. Later commands for the same registry reuse the sign-in, and refresh it when possible, without opening the browser.
+ Pass the client ID with `--client-id` the first time that you sign in. Later sign-ins to the same registry reuse it. If you omit it the first time, the CLI prompts for it in a terminal.
+ To print the sign-in link instead of opening a browser, add `--no-browser`. The sign-in still returns to the loopback address `127.0.0.1` on the computer that runs the CLI. To sign in with a browser on another computer, connect from it with `ssh -L 8484:127.0.0.1:8484` to the computer that runs the CLI.
+ If the `AWS_BEARER_TOKEN_AGENT_REGISTRY` environment variable is set, the CLI sends that token as it is. It doesn’t sign you in or use the cache.

The following procedure shows the full flow, from sign-in to sign-out. It uses a registry with the ID `a1b2c3d4e5f6g7h8` in the US East (N. Virginia) Region. The registry trusts an identity provider at `https://example.us.auth0.com/`.

**To install a skill from a registry that uses JWT authorization**

1. Get the client ID of the app client that the registry owner set up for the AWS CLI. This example uses the client ID `0oa1b2c3d4e5f6g7h8i9`. If you own the registry, set up the app client first. For instructions, see [Set up the identity provider for the AWS CLI](#registry-skill-install-cli-jwt).

1. To sign in and list the skills in the registry, run `list-skills` with `--authorizer JWT` and your client ID. The command opens the identity provider’s sign-in page in your browser. After you sign in, it lists the skills.

   ```bash
   aws agent-registry list-skills \
       --registry-id a1b2c3d4e5f6g7h8 \
       --authorizer JWT \
       --client-id 0oa1b2c3d4e5f6g7h8i9 \
       --region us-east-1
   ```

   Output:

   ```text
   Registry a1b2c3d4e5f6g7h8 trusts: https://example.us.auth0.com/
   Detected identity provider: generic OIDC provider
   Attempting to open your default browser. If the browser does not open, open the following URL.
   
   https://example.us.auth0.com/authorize?response_type=code&client_id=0oa1b2c3d4e5f6g7h8i9&...
   
   Waiting for sign-in to complete (up to 10 minutes)...
   Signed in.
   
   {
       "skills": [
           {
               "name": "pdf-extract",
               "skillName": "pdf-extract",
               "recordId": "r1s2t3u4v5w6",
               "description": "Extracts text and tables from PDF files.",
               "recordVersion": "1.2.0",
               "installedFor": []
           }
       ]
   }
   ```

1. To install a skill, run `install-skill` with `--authorizer JWT` and the skill’s `recordId`. You don’t need `--client-id` this time. The command reuses your sign-in from the previous step, so it doesn’t open the browser.

   ```bash
   aws agent-registry install-skill \
       --registry-id a1b2c3d4e5f6g7h8 \
       --record-id r1s2t3u4v5w6 \
       --authorizer JWT \
       --region us-east-1
   ```

   Output:

   ```text
   Downloading pdf-extract from https://artifact-111122223333-us-east-1.s3.us-east-1.amazonaws.com...
   Verified SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
   Claude Code: Installed pdf-extract to /home/user/.claude/skills/pdf-extract
   Kiro: Installed pdf-extract to /home/user/.kiro/skills/pdf-extract
   ```

   If you run `install-skill` before you sign in, it signs you in first, in the same way as `list-skills` in the previous step.

1. Run other `list-skills` and `install-skill` commands for the same registry with `--authorizer JWT`. They reuse the cached sign-in. When the token expires, the CLI refreshes it when possible, without opening the browser. For more information about these commands, see [List skills](#registry-skill-install-cli-list) and [Install a skill](#registry-skill-install-cli-install).

1. To remove the skill, run `uninstall-skill`. This command doesn’t need `--authorizer JWT` or a sign-in, because it works only on your computer.

   ```bash
   aws agent-registry uninstall-skill \
       --name pdf-extract \
       --yes
   ```

   Output:

   ```text
   Claude Code: Uninstalled pdf-extract from /home/user/.claude/skills (installed from registry a1b2c3d4e5f6g7h8, record r1s2t3u4v5w6)
   Kiro: Uninstalled pdf-extract from /home/user/.kiro/skills (installed from registry a1b2c3d4e5f6g7h8, record r1s2t3u4v5w6)
   ```

1. When you no longer need the registry, sign out of it. The command revokes the refresh token at the identity provider, and then deletes the sign-in from your computer.

   ```bash
   aws agent-registry sign-out \
       --registry-id a1b2c3d4e5f6g7h8 \
       --region us-east-1
   ```

   Output:

   ```text
   Registry a1b2c3d4e5f6g7h8 at https://agent-registry.us-east-1.api.aws: revoked the refresh token; removed the sign-in.
   ```

   To sign out of every registry that has a cached sign-in on your computer, use `--all` instead of `--registry-id`. For more information, see [Sign out of a registry](#registry-skill-install-cli-sign-out).

### Set up the identity provider for the AWS CLI
<a name="registry-skill-install-cli-jwt"></a>

If you own a registry that uses JWT authorization, set up an app client for the AWS CLI in the registry’s identity provider. The CLI runs on your users' computers and can’t keep a secret, so the app client must have the following settings:
+ A public client, with no client secret. The CLI signs in with the authorization code grant and Proof Key for Code Exchange (PKCE).
+ The callback URL `http://127.0.0.1:8484/oauth/callback`. The CLI listens at the loopback address `127.0.0.1` on your users' computers. The callback URL must use exactly this address. After your users sign in, the identity provider returns to this address. If your users set the `AWS_AGENT_REGISTRY_CALLBACK_PORT` environment variable, the callback URL uses that port instead.
+ The authorization code grant and the refresh token grant. With the refresh token, the CLI can renew a sign-in without opening the browser again.
+ The `openid` scope, and any scopes that the registry advertises.

An Amazon Cognito user pool also needs a domain.

The registry’s JWT authorizer must accept the token that the CLI sends. Configure its authorization rules as follows. For more information about these rules, see [Set up a JWT manually with your own identity provider](registry-supported-auth-types.md#registry-jwt-manual).


| Identity provider | App client | Authorization rule | 
| --- | --- | --- | 
| Amazon Cognito | A user pool app client of type **Mobile app**. |  **Allowed clients** (`allowedClients`) set to the app client ID. | 
| Auth0 | An application of type **Native**. |  **Allowed audiences** (`allowedAudience`) set to the application’s client ID. If the tenant has a default audience, use that API’s identifier instead. | 
| Okta | An OpenID Connect (OIDC) app integration of type **Native Application**. On the `default` authorization server, add an access policy and a rule for the app. |  **Allowed audiences** (`allowedAudience`) set to `api://default`. | 

## List skills
<a name="registry-skill-install-cli-list"></a>

The `list-skills` command lists the skill records in a registry. For each skill, it also shows the AI coding agents on your computer that the skill is currently installed for. It reads every page of records, and downloads nothing. To check one agent only, use `--agent`.

Each skill in the output has the following fields:

 `name`   
The name of the record. To install the skill by this name, pass it to `install-skill` with `--record-name`.

 `skillName`   
The `name` in the frontmatter of the skill’s `SKILL.md`. `install-skill` names the skill’s folder after it, so it can differ from `name`. The command omits `skillName` when it can’t read the record’s `SKILL.md`.

 `recordId`   
The record ID. Pass it to `install-skill` with `--record-id`.

 `description`   
The description of the record.

 `recordVersion`   
The version of the record.

 `installedFor`   
The agents on your computer that the skill is currently installed for. An agent counts only if its skills folder has a copy that `install-skill` installed from this registry and record. Each agent has an `id`, which is the value to pass to `--agent`, and a display `name`.

**Example 1 – List the skills in a registry**  
The following `list-skills` example lists the skills in the specified registry.  

```bash
aws agent-registry list-skills \
    --registry-id a1b2c3d4e5f6g7h8 \
    --region us-east-1
```
Output:  

```json
{
    "skills": [
        {
            "name": "pdf-extract",
            "skillName": "pdf-extract",
            "recordId": "r1s2t3u4v5w6",
            "description": "Extracts text and tables from PDF files.",
            "recordVersion": "1.2.0",
            "installedFor": [
                {
                    "id": "claude-code",
                    "name": "Claude Code"
                },
                {
                    "id": "kiro",
                    "name": "Kiro"
                }
            ]
        },
        {
            "name": "csv-tools",
            "skillName": "csv-tools",
            "recordId": "k7l8m9n0p1q2",
            "description": "Cleans, joins and summarizes CSV files.",
            "recordVersion": "0.3.1",
            "installedFor": []
        }
    ]
}
```

**Example 2 – List the skills in a registry as a table**  
The following `list-skills` example shows the name, record ID, and version of each skill as a table.  

```bash
aws agent-registry list-skills \
    --registry-id a1b2c3d4e5f6g7h8 \
    --query 'skills[].{name:name,recordId:recordId,version:recordVersion}' \
    --output table \
    --region us-east-1
```
Output:  

```text
--------------------------------------------
|                list-skills               |
+-------------+----------------+-----------+
|    name     |   recordId     |  version  |
+-------------+----------------+-----------+
|  pdf-extract|  r1s2t3u4v5w6  |  1.2.0    |
|  csv-tools  |  k7l8m9n0p1q2  |  0.3.1    |
+-------------+----------------+-----------+
```

For an example that lists the skills in a registry that uses JWT authorization, see [Sign in and install skills](#registry-skill-install-cli-jwt-walkthrough).

## Install a skill
<a name="registry-skill-install-cli-install"></a>

Use `install-skill` to install a skill from a registry for your AI coding agents. Identify the skill by its record ID (`--record-id`) or its record name (`--record-name`). Specify exactly one of these options.

 `--record-name` must match the record’s `name` in the output of `list-skills` exactly, including case. It doesn’t match `skillName`, the name in the skill’s `SKILL.md`. To find the record, the command lists the registry’s skill records with `ListDiscoverableRegistryRecords`. For a registry that uses IAM authorization, this requires the `agent-registry:ListDiscoverableRegistryRecords` permission. `--record-name` also works with `--authorizer JWT`.

Record names aren’t unique. A registry can have several skill records with the same name, such as two versions of a skill. If more than one record has the name, the command installs nothing and lists each record ID with its version. Choose one, and pass it with `--record-id`. Example 7 in this section shows the output.

When you run `install-skill`, it gets the record’s latest approved revision with `BatchGetDiscoverableRegistryRecord`. What it installs depends on the record’s content source. For the content sources, see [Ways to provide skill content](registry-skill-packages.md#registry-skill-packages-content-sources).


| Record content | What `install-skill` does | 
| --- | --- | 
| An uploaded package, or a full package that the registry synchronizes | Downloads the package from the record’s `artifact.downloadUrl`. Before it writes anything, the command verifies the SHA-256 checksum. If the checksum doesn’t match, the command refuses to install the skill. It then extracts the package into each skills folder. | 
| Inline SKILL.md, or SKILL.md that the registry synchronizes without a package | Installs a folder that contains only `SKILL.md`, written from the record’s text. The command downloads nothing, and says that it installs only `SKILL.md`. | 
| Only a URL for SKILL.md, in the `source` of the record’s `skillMd` descriptor, with no SKILL.md text and no package | The command refuses the record. The CLI doesn’t download a `SKILL.md` from a URL that the publisher chooses. To make the skill installable, the publisher can add the SKILL.md text to the record (inline SKILL.md), or provide a package. | 
| No package and no SKILL.md text | The command refuses the record. | 

The command refuses to extract an archive that has absolute paths, `..` path segments, or links. It also refuses an archive that is larger than its size limits. If the package wraps its files in a single top-level folder, the command installs the files without that folder.

The command names the skill’s folder after the `name` in the frontmatter of the skill’s `SKILL.md`. It doesn’t use the record’s name. When the two names differ, the command says so.

Before it writes anything, the command checks the name against the [Agent Skills specification](https://agentskills.io/specification) on the Agent Skills website. The specification allows a `name` of 1–64 characters. The name can contain only lowercase letters (a–z), digits, and hyphens. It can’t start or end with a hyphen, or contain two hyphens in a row. The following table shows how the command handles each kind of name.


| Name | Examples | What `install-skill` does | 
| --- | --- | --- | 
| Follows the Agent Skills specification. |  `pdf-extract`, `csv-tools`  | Uses the name as it is. | 
| Doesn’t follow the specification, but has at most 64 characters and begins with a letter or digit. The characters are letters in any case, digits, dots, underscores, and hyphens. Older skills often have names like these. |  `pdf_processing_skill`, `PDF.Tools`  | Uses the name, and prints a warning. Some agents might not load the skill. | 
| Any other name. For example, a name that is longer than 64 characters, that starts with a dot or a hyphen, or that has any other character, such as a space or a slash. |  `my skill`, `../x`, `-pdf`  | Refuses the record, and writes nothing. | 

The command records where each skill came from. It writes this in a `.agent-registry-skill.json` file at the root of the skill’s folder. The command updates or replaces an existing folder only when this file names the same registry, endpoint, and record.

A skills folder might already have a folder with the skill’s name that the command can’t replace. This happens in the following cases:
+ The folder holds a skill that `install-skill` installed from another registry, endpoint, or record.
+ The folder has no readable `.agent-registry-skill.json` file. For example, you created the folder yourself, or another tool installed it.

In these cases, the command installs nothing into that skills folder, and leaves the existing folder as it is. `--force` doesn’t change this. The command prints a message, prefixed with the agent’s name, that says how to fix the conflict. It still installs the skill into the other skills folders. It then exits with status 1. For an example, see Example 6 later in this section.

**Example 1 – Install a skill for every detected agent**  
The following `install-skill` example installs the specified skill for every detected agent.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-id r1s2t3u4v5w6 \
    --region us-east-1
```
Output:  

```text
Downloading pdf-extract from https://artifact-111122223333-us-east-1.s3.us-east-1.amazonaws.com...
Verified SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Claude Code: Installed pdf-extract to /home/user/.claude/skills/pdf-extract
Kiro: Installed pdf-extract to /home/user/.kiro/skills/pdf-extract
```

**Example 2 – Install a skill for one agent**  
The following `install-skill` example installs the specified skill for Claude Code only.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-id r1s2t3u4v5w6 \
    --agent claude-code \
    --region us-east-1
```
Output:  

```text
Downloading pdf-extract from https://artifact-111122223333-us-east-1.s3.us-east-1.amazonaws.com...
Verified SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Claude Code: Installed pdf-extract to /home/user/.claude/skills/pdf-extract
```

**Example 3 – Install a skill into a folder of your choice**  
The following `install-skill` example installs the specified skill into a subfolder of `/home/user/my-project/skills`. It doesn’t install into the skills folders of the detected agents.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-id r1s2t3u4v5w6 \
    --target-directory /home/user/my-project/skills \
    --region us-east-1
```
Output:  

```text
Downloading pdf-extract from https://artifact-111122223333-us-east-1.s3.us-east-1.amazonaws.com...
Verified SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Installed pdf-extract to /home/user/my-project/skills/pdf-extract
```

**Example 4 – Install a skill whose record has only SKILL.md text**  
The following `install-skill` example installs a skill whose record has no package but holds the text of its `SKILL.md`. The command writes that text as the skill’s `SKILL.md` and downloads nothing.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-id r1s2t3u4v5w6 \
    --region us-east-1
```
Output:  

```text
Installing the SKILL.md text published on record r1s2t3u4v5w6; the record has no package, so only SKILL.md is installed.
Claude Code: Installed pdf-extract to /home/user/.claude/skills/pdf-extract
Kiro: Installed pdf-extract to /home/user/.kiro/skills/pdf-extract
```

**Example 5 – Install a skill whose record has a different name**  
The following `install-skill` example installs a skill from a record named `pdf_processing_skill`. The skill’s `SKILL.md` names the skill `pdf-processing-skill`, so the command installs it in a folder with that name.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-id r1s2t3u4v5w6 \
    --region us-east-1
```
Output:  

```text
Downloading pdf_processing_skill from https://artifact-111122223333-us-east-1.s3.us-east-1.amazonaws.com...
Verified SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Record 'pdf_processing_skill' installs as skill 'pdf-processing-skill'.
Claude Code: Installed pdf-processing-skill to /home/user/.claude/skills/pdf-processing-skill
Kiro: Installed pdf-processing-skill to /home/user/.kiro/skills/pdf-processing-skill
```

**Example 6 – Install a skill when a folder with its name holds a skill from another record**  
In the following `install-skill` example, the Claude Code skills folder already has a `pdf-extract` folder. `install-skill` installed that folder from registry `b2c3d4e5f6g7h8i9`, record `x9y8z7w6v5u4`. The command leaves that folder as it is, installs the skill for Kiro, and exits with status 1.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-id r1s2t3u4v5w6 \
    --region us-east-1
```
Output:  

```text
Downloading pdf-extract from https://artifact-111122223333-us-east-1.s3.us-east-1.amazonaws.com...
Verified SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Claude Code: Refusing to replace /home/user/.claude/skills/pdf-extract: it was installed from registry b2c3d4e5f6g7h8i9, record x9y8z7w6v5u4, not registry a1b2c3d4e5f6g7h8, record r1s2t3u4v5w6. Uninstall it first with aws agent-registry uninstall-skill --name pdf-extract --agent claude-code, or install into another folder with --agent or --target-directory.
Kiro: Installed pdf-extract to /home/user/.kiro/skills/pdf-extract
```
If the existing folder has no readable `.agent-registry-skill.json` file, the message for that folder is the following instead.  

```text
Claude Code: Refusing to replace /home/user/.claude/skills/pdf-extract: it has no readable .agent-registry-skill.json, so this command can't tell where it came from. Move or delete the folder yourself, or install into another folder with --agent or --target-directory.
```

**Example 7 – Install a skill by its record name**  
The following `install-skill` example installs the skill whose record is named `pdf-extract`. The command prints the record ID that the name matches, and then installs that record.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-name pdf-extract \
    --region us-east-1
```
Output:  

```text
Record 'pdf-extract' is r1s2t3u4v5w6.
Downloading pdf-extract from https://artifact-111122223333-us-east-1.s3.us-east-1.amazonaws.com...
Verified SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Claude Code: Installed pdf-extract to /home/user/.claude/skills/pdf-extract
Kiro: Installed pdf-extract to /home/user/.kiro/skills/pdf-extract
```
If the registry has more than one skill record named `pdf-extract`, the command installs nothing, and the output is the following instead.  

```text
Registry a1b2c3d4e5f6g7h8 has more than one skill record named 'pdf-extract': r1s2t3u4v5w6 (1.2.0), z9y8x7w6v5u4 (1.3.0). Pass --record-id to choose one.
```
If no skill record has the name, the output is the following.  

```text
Registry a1b2c3d4e5f6g7h8 has no skill record named 'pdf-extract'; --record-name matches the record's name (name in list-skills), not its SKILL.md name (skillName). Run aws agent-registry list-skills --registry-id a1b2c3d4e5f6g7h8 to see the names.
```

For an example that installs a skill from a registry that uses JWT authorization, see [Sign in and install skills](#registry-skill-install-cli-jwt-walkthrough).

## Update a skill
<a name="registry-skill-install-cli-update"></a>

To update a skill, run `install-skill` again with the same registry and record. The command finds the skills that it installed from the record by their `.agent-registry-skill.json` files, whatever their folders are named:
+ If an installed copy matches the content that the record now publishes, the command leaves the copy as it is.
+ If the record publishes a new version, the command replaces the installed copy with it.

  You can’t choose a version. `install-skill` always installs the record’s latest approved revision, and it has no option to install an earlier one.
+ If the skill’s `SKILL.md` has a new `name`, the command installs the skill under that name and reports the earlier copy without removing it.

When every copy is up to date, the command downloads nothing. To reinstall a skill that is already up to date, add `--force`.

A record might offer only its `SKILL.md` text after you install the skill from its package. This happens when the registry returns the record’s `SKILL.md` text without a download URL for the package. In that case, the command keeps the installed package. To replace the package with the `SKILL.md` text alone, add `--force`. `--force` never replaces a skill from another registry, endpoint, or record, or a skill that `install-skill` didn’t install.

**Example 1 – Reinstall a skill that is already up to date**  
The following `install-skill` example uses `--force` to reinstall a skill whose installed copies already match the package that the record publishes.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-id r1s2t3u4v5w6 \
    --force \
    --region us-east-1
```
Output:  

```text
Downloading pdf-extract from https://artifact-111122223333-us-east-1.s3.us-east-1.amazonaws.com...
Verified SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Claude Code: Reinstalled pdf-extract at /home/user/.claude/skills/pdf-extract.
Kiro: Reinstalled pdf-extract at /home/user/.kiro/skills/pdf-extract.
```

**Example 2 – Keep an installed package when the record offers only SKILL.md text**  
The following `install-skill` example runs for a skill that you installed earlier from the record’s package. The record now returns only its `SKILL.md` text, so the command keeps the installed package.  

```bash
aws agent-registry install-skill \
    --registry-id a1b2c3d4e5f6g7h8 \
    --record-id r1s2t3u4v5w6 \
    --region us-east-1
```
Output:  

```text
Claude Code: pdf-extract at /home/user/.claude/skills/pdf-extract holds the record's package; the record now publishes no downloadable package, so it was left as it is. Pass --force to replace it with the SKILL.md text only.
Kiro: pdf-extract at /home/user/.kiro/skills/pdf-extract holds the record's package; the record now publishes no downloadable package, so it was left as it is. Pass --force to replace it with the SKILL.md text only.
```

## Uninstall a skill
<a name="registry-skill-install-cli-uninstall"></a>

Use `uninstall-skill` to remove a skill from the skills folder of every detected agent. To remove it for one agent only, use `--agent`. To remove it from a folder of your choice, use `--target-directory`. Pass the name of the skill’s folder with `--name`. Use the name that `install-skill` printed. It’s the skill’s `SKILL.md` name (`skillName` in `list-skills`), not the record name that `--record-name` uses.

The command removes only skills that `install-skill` installed, from any registry. Each skill’s folder must contain a `SKILL.md` and a readable `.agent-registry-skill.json` file. The command skips any other folder.

Before it removes anything, the command lists each folder to remove and asks you to confirm. To skip the prompt, add `--yes`. If standard input isn’t a terminal, the command requires `--yes`.

**Example 1 – Uninstall a skill from every detected agent**  
The following `uninstall-skill` example removes the `pdf-extract` skill from every detected agent that it is installed for, without a prompt.  

```bash
aws agent-registry uninstall-skill \
    --name pdf-extract \
    --yes
```
Output:  

```text
Claude Code: Uninstalled pdf-extract from /home/user/.claude/skills (installed from registry a1b2c3d4e5f6g7h8, record r1s2t3u4v5w6)
Kiro: Uninstalled pdf-extract from /home/user/.kiro/skills (installed from registry a1b2c3d4e5f6g7h8, record r1s2t3u4v5w6)
```

**Example 2 – Uninstall a skill from one agent**  
The following `uninstall-skill` example removes the `pdf-extract` skill from Kiro only, after it asks for confirmation.  

```bash
aws agent-registry uninstall-skill \
    --name pdf-extract \
    --agent kiro
```
Output:  

```text
Remove /home/user/.kiro/skills/pdf-extract (from registry a1b2c3d4e5f6g7h8, record r1s2t3u4v5w6)? [y/N]: y
Kiro: Uninstalled pdf-extract from /home/user/.kiro/skills (installed from registry a1b2c3d4e5f6g7h8, record r1s2t3u4v5w6)
```

**Example 3 – Uninstall a skill from a folder of your choice**  
The following `uninstall-skill` example removes the `pdf-extract` skill from a folder that you installed it into with `install-skill --target-directory`.  

```bash
aws agent-registry uninstall-skill \
    --name pdf-extract \
    --target-directory /home/user/my-project/skills \
    --yes
```
Output:  

```text
Uninstalled pdf-extract from /home/user/my-project/skills (installed from registry a1b2c3d4e5f6g7h8, record r1s2t3u4v5w6)
```

## Sign out of a registry
<a name="registry-skill-install-cli-sign-out"></a>

Use `sign-out` to sign out of a registry that uses JWT authorization. For each cached sign-in, it revokes the refresh token at the identity provider, and then deletes the sign-in from `~/.aws/agent-registry/cache`. Specify a registry with `--registry-id`, or sign out of every registry with `--all`.

If the sign-in has no refresh token, or the identity provider has no revocation endpoint, the command deletes the sign-in and succeeds. It reports why it didn’t revoke the token.

If a revocation request fails, the command still removes the sign-in. Later commands sign you in again. The command keeps the refresh token in a separate store only to revoke it later. It then exits with status 1. The next `sign-out` for the registry retries the revocation. The CLI never uses a kept refresh token to sign in or to refresh a sign-in.

 `sign-out` doesn’t affect a token that you set in the `AWS_BEARER_TOKEN_AGENT_REGISTRY` environment variable.

**Example 1 – Sign out of a registry**  
The following `sign-out` example signs out of the specified registry.  

```bash
aws agent-registry sign-out \
    --registry-id a1b2c3d4e5f6g7h8
```
Output:  

```text
Registry a1b2c3d4e5f6g7h8 at https://agent-registry.us-east-1.api.aws: revoked the refresh token; removed the sign-in.
```

**Example 2 – Sign out of every registry**  
The following `sign-out` example signs out of every registry that has a cached sign-in on your computer.  

```bash
aws agent-registry sign-out \
    --all
```
Output:  

```text
Registry a1b2c3d4e5f6g7h8 at https://agent-registry.us-east-1.api.aws: revoked the refresh token; removed the sign-in.
Registry b9c8d7e6f5g4h3i2 at https://agent-registry.us-east-1.api.aws: revoked the refresh token; removed the sign-in.
```

## Resolve AWS CLI skill installation and sign-in errors
<a name="registry-skill-install-cli-troubleshooting"></a>

The following table describes common errors from the skill commands. These include missing agents and sign-in or authorization errors. The table lists the causes of each error and how to fix it.


| Error | Cause | What to do | 
| --- | --- | --- | 
|  `No supported AI coding agents found` from `install-skill`  | The CLI didn’t find the configuration folder of any supported agent on your computer. | Install into a folder of your choice with `--target-directory`, or set up a supported agent and use `--agent`. | 
|  `AccessDeniedException`  | The error message says that the authentication type doesn’t match. The registry uses JWT authorization, but the command signed the request with your AWS credentials. | Add `--authorizer JWT`. | 
|  `UnauthorizedException`  | The sign-in succeeded, but the registry’s JWT authorizer didn’t accept the token that the CLI sent. Common causes are the following:+  You signed in with a client ID other than the one that the registry owner set up for the AWS CLI. <br />+  The authorization rules of the registry don’t match the app client. For example, **Allowed clients** (`allowedClients`) or **Allowed audiences** (`allowedAudience`) has a different value.  | To fix this error, do the following:1.  Check that you used the client ID of the app client that the registry owner set up for the AWS CLI. <br />2.  If you used a different client ID, run `sign-out` for the registry. Then run the command again with the correct `--client-id`. <br />3.  If the error continues, ask the registry owner to check the authorization rules of the registry. For instructions on configuring these rules, see [Set up the identity provider for the AWS CLI](#registry-skill-install-cli-jwt).  | 
| The browser shows an error from the identity provider | The identity provider rejected the sign-in request from the CLI. Common causes are the following:+  The callback URL of the app client isn’t exactly `http://127.0.0.1:8484/oauth/callback`. <br />+  The app client doesn’t have the authorization code grant turned on. <br />+  For Okta, the authorization server has no access policy or rule for the app.  | Ask the registry owner to do the following:1.  Check that the callback URL of the app client is exactly `http://127.0.0.1:8484/oauth/callback`. <br />2.  Check that the authorization code grant is turned on for the app client. <br />3.  For Okta, check the access policy and its rule on the `default` authorization server.  | 

**Important**  
The checksum proves that you received the package that the registry stored. It doesn’t prove that the package is safe. AWS Agent Registry checks the structure of a package but doesn’t scan it for malware or check what its scripts do. Before an agent runs a skill that you install, validate it in the same way as any other content from an external source. For more information about validating records, see [Validate record metadata before you act on it](registry-data-protection.md#registry-consumer-validation).