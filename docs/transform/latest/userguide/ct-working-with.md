# Working with continuous modernization

## Source management

Use `atx ct source` commands to connect repositories. Supported providers:
GitHub, GitLab, Bitbucket, local.

### GitHub organizations

Token: personal access token (classic) with `repo` scope. Read-only for
analysis, full repo for remediation.

```
atx ct source add --name `name` --provider github --org `org` --token `pat`
```

### GitLab groups and users

Token: personal access token with `api` scope.

```
atx ct source add --name `name` --provider gitlab --org `group-or-user` --token `pat`
# Self-hosted:
atx ct source add --name `name` --provider gitlab --org `group-or-user` --token `pat` --url https://`gitlab.example.com`
```

### Bitbucket workspaces and projects

Bitbucket Cloud — scopes: `read:repository:bitbucket`,
`write:repository:bitbucket`, `read:pullrequest:bitbucket`,
`write:pullrequest:bitbucket`. Also needs `--email` and
`--username`.

```
atx ct source add --name `name` --provider bitbucket --org `workspace` --token `api-token` --email `email` --username `username`
```

Bitbucket Data Center:

```
atx ct source add --name `name` --provider bitbucket --org `project-key` --token `http-access-token` --url https://`bitbucket.example.com`
```

### Local repositories

```
atx ct source add --name `name` --provider local --path `parent-directory`
```

###### Important

`--path` must point to a parent directory containing git repos as
subdirectories, not to a single repo.

### Managing sources

```
atx ct source list
atx ct source remove --name `name`
```

## Repository discovery and management

```
atx ct discovery scan --source `name`
atx ct discovery status --source `name`
atx ct discovery scan --source `name` --path `new-directory`
```

After discovery:

```
atx ct repository list
atx ct repository list --source `name`
atx ct repository list --labels "`team:frontend,priority:high`"
atx ct repository update --source `name` --repo "`source`::`slug`" --labels "`team:frontend,priority:high`"
atx ct repository update --source `name` --labels "`migration:wave-1`"
```

## Running analysis

The `--type` flag specifies the kind of analysis to run:

- `tech-debt-quick` – Outdated dependencies and easy
  wins.
- `tech-debt-comprehensive` – Deeper AI-powered analysis covering
  dependency, security, pattern, performance, maintainability, architecture, code-quality, and
  infrastructure findings.
- `security` – Security vulnerabilities and
  exposures.
- `agentic-readiness` – Readiness of your repositories for AI agents
  (frameworks, APIs, documentation).
- `modernization-readiness` – Modernization opportunities across your
  infrastructure, application, data, security, and operations
  dimensions.

```
atx ct analysis run --type `type` --source `name` [--repo `source`::`slug`] [--wait]
atx ct analysis get --id `id` --json
atx ct analysis list --json
atx ct analysis list --status `pending|running|complete|cancelled|failed` --json
atx ct analysis list --type `type` --json
atx ct analysis cancel --id `id`
atx ct analysis delete --id `id` [--cascade-findings]
```

### Custom analysis

```
atx ct analysis run --type custom --transformation-name `name` --source `source` --repo `source`::`slug` --wait
```

Configuration with `-g` flag: key-value, JSON, or file path.

List TDs: `atx custom def list`

## Managing findings

```
atx ct findings list --json
atx ct findings list --repo `source`::`slug` --source `name` --severity `high|medium|low` --type `analysis-type` --status `open|dismissed|obsolete` --analysis-id `id` --fix-transform `transform-name` --json
```

### Finding statuses

- `open` — Active
- `dismissed` — Manually dismissed (requires reason)
- `obsolete` — System-set when re-analysis no longer produces the
  finding

```
atx ct findings update --id `id` --status dismissed --reason "`reason`"
atx ct findings update --id `id` --status open
atx ct findings batch-update --ids `id1`,`id2` --status dismissed --reason "`reason`"
atx ct findings get --id `id`
atx ct findings delete --id `id`
```

### Finding obsolescence

Re-analysis marks resolved findings as obsolete. Cannot be re-opened. Retained for
audit.

## Creating remediations

Three modes: findings-based, TD override, direct TD.

```
atx ct remediation create --ids `id1`,`id2` --name "`name`"
atx ct remediation create --ids `id1`,`id2` --transformation-name `TD`
atx ct remediation create --transformation-name `TD` --repo `source`::`slug`
```

Output by provider: GitHub PR, GitLab MR, Bitbucket PR, Local branch.

###### Note

Token must have write access for PR/MR creation.

Local execution with `--local` flag.

```
atx ct remediation create --transformation-name `TD` --repo `source`::`slug` -g "`additionalPlanContext=Upgrade to Node.js 22`"
atx ct remediation list
atx ct remediation status --id `id`
atx ct remediation retry --id `id`
atx ct remediation delete --id `id`
```

## AWS Transform web application (Optional)

The AWS Transform web application is an optional interface for monitoring continuous
modernization analyses, findings, and remediations across your portfolio of code
sources.

Before using the AWS Transform web application, you need to have a user identity enabled to
access AWS Transform in your organization. For information about enabling AWS Transform, see
[Setting up AWS Transform](transform-setup.md "transform-setup.md").

To use the AWS Transform web application:

1. Visit `https://aws.amazon.com/transform/` and sign in using
   AWS IAM Identity Center credentials.
2. If continuous modernization does not appear after you sign in, sign in with
   IAM credentials instead. To enable IAM credentials sign-in:

   1. In the AWS Management Console, open AWS Transform and choose
      **Settings**.
   2. In the **Access AWS Transform with IAM credentials**
      section, enable IAM credentials access.
   3. On the same settings page, copy the sign-in link shown under
      **Web application URL (with IAM)**.
   4. Paste the sign-in URL into the same browser window where the AWS
      Management Console is open. This ensures the web application uses the AWS credentials
      from that account.

3. Open the left navigation menu and choose **continuous
   modernization**. The Dashboard displays summary statistics including sources,
   repositories, total findings by severity, and analysis types.
4. Use the **Analyses**,
   **Findings**, and
   **Remediations** tabs to view detailed
   results.
5. Chat with AWS Transform directly from the web application to ask questions about
   your analyses, findings, or remediations.

The web application is designed for enterprise-scale operations where you need
centralized visibility into continuous modernization analyses and remediations across multiple
codebases.
