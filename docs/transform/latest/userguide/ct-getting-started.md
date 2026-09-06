

# Getting started
<a name="ct-getting-started"></a>

## Prerequisites
<a name="ct-prerequisites"></a>

To use continuous modernization effectively, you should have a basic understanding of Git version control, familiarity with your source code platform (GitHub, GitLab, or Bitbucket), working knowledge of AWS IAM permissions, and experience with command-line tools.

Before you use continuous modernization, verify that you have the following:
+ AWS Transform CLI installed:

  ```
  curl -fsSL https://transform-cli.awsstatic.com/install.sh | bash
  ```
+ Node.js 22 or later
+ Valid AWS credentials (`AWS_PROFILE` or environment variables)
+ The AWS managed policy `AWSTransformCustomFullAccess` attached to your IAM user or role

**Note**  
Running analyses and remediations on remote infrastructure or with the security agent requires additional managed policies. See the compute options and security agent setup in [How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works).

## Quick start
<a name="ct-quick-start"></a>

**Note**  
You no longer need to start a local server. The `atx ct server` command is deprecated.

1. Add a source:

   ```
   atx ct source add --name {{name}} --provider {{provider}} --org {{org-or-group}} --token {{token}}
   ```

   Where {{name}} is a descriptive identifier for your source, {{provider}} is the platform (`github`, `gitlab`, `bitbucket`, or `local`), {{org-or-group}} is your organization or group name, and {{token}} is your authentication token.

1. Discover repositories:

   ```
   atx ct discovery scan --source {{name}}
   ```

1. Run an analysis:

   ```
   atx ct analysis run --type {{type}} --source {{name}} --wait
   ```

1. Explore findings:

   ```
   atx ct findings list --json
   ```

1. Remediate findings:

   ```
   atx ct remediation create --ids {{id1}},{{id2}} --name "{{remediation-name}}"
   ```