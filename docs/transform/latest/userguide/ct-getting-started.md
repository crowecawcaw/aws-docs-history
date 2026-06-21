# Getting started

## Prerequisites

To use continuous modernization effectively, you should have a basic understanding of Git
version control, familiarity with your source code platform (GitHub, GitLab, or Bitbucket),
working knowledge of AWS IAM permissions, and experience with command-line tools.

Before you use continuous modernization, verify that you have the following:

- AWS Transform CLI installed:

```
curl -fsSL https://transform-cli.awsstatic.com/install.sh | bash
```

- Node.js 22 or later
- Valid AWS credentials (`AWS_PROFILE` or environment
  variables)
- The AWS managed policy `AWSTransformCustomFullAccess` attached
  to your IAM user or role

## Quick start

1. Start the continuous modernization server:

```
atx ct server &
```

2. Add a source:

```
atx ct source add --name `name` --provider `provider` --org `org-or-group` --token `token`
```

Where `name` is a descriptive identifier for your source,
`provider` is the platform (`github`,
`gitlab`, `bitbucket`, or `local`),
`org-or-group` is your organization or group name, and
`token` is your authentication token. 3. Discover repositories:

```
atx ct discovery scan --source `name`
```

4. Run an analysis:

```
atx ct analysis run --type `type` --source `name` --wait
```

5. Explore findings:

```
atx ct findings list --json
```

6. Remediate findings:

```
atx ct remediation create --ids `id1`,`id2` --name "`remediation-name`"
```
