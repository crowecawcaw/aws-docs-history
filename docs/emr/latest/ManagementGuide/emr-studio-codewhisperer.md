# Amazon CodeWhisperer integration with EMR Studio

Workspaces

## Overview

You can use [Amazon CodeWhisperer](../../../codewhisperer/latest/userguide/what-is-cwspr.md "../../../codewhisperer/latest/userguide/what-is-cwspr.md") with
Amazon EMR Studio to get real-time recommendations as you write code in JupyterLab. CodeWhisperer
can complete your comments, finish single lines of code, make line-by-line recommendations,
and generate fully-formed functions.

###### Note

When you use Amazon EMR Studio, AWS might store data about your usage and content for
service improvement purposes. For more information and instructions to opt out of data
sharing, see [Sharing your data with
AWS](../../../codewhisperer/latest/userguide/sharing-data.md "../../../codewhisperer/latest/userguide/sharing-data.md") in the _Amazon CodeWhisperer User Guide_.

## Considerations for using CodeWhisperer

with Workspaces

- CodeWhisperer integration is available in the same AWS Regions where EMR Studio is
  available, as documented in the [EMR Studio
  considerations](emr-studio-considerations.md "emr-studio-considerations.md").
- Amazon EMR Studio automatically uses the CodeWhisperer endpoint in US East (N. Virginia)
  (us-east-1) for recommendations, regardless of the Region that your studio is in.
- CodeWhisperer supports only Python language for coding ETL scripts for Spark jobs in
  EMR Studio.
- A client-side telemetry option quantifies your usage of CodeWhisperer. This
  functionality isn't supported with EMR Studio.

## Permissions required for

CodeWhisperer

To use CodeWhisperer, you must attach the following policy to your IAM user role for
Amazon EMR Studio:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeWhispererPermissions",
 "Effect": "Allow",
 "Action": [
 "codewhisperer:GenerateRecommendations"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Use CodeWhisperer with

Workspaces

To display the CodeWhisperer reference log in JupyterLab, open the
**CodeWhisperer** panel at the bottom of the JupyterLab window and choose
**Open Code Reference Log**.

The following list contains shortcuts that you can use to interact with CodeWhisperer
suggestions:

- Pause recommendations – Use **Pause
  Auto-Suggestions** from the CodeWhisperer settings.
- Accept a recommendation – Press
  **Tab** on your keyboard.
- Reject a recommendation – Press
  **Escape** on your keyboard.
- Navigate recommendations – Use the
  **Up** and **Down** arrows on your keyboard.
- Manual invoke – Press **Alt**
  and **C** on your keyboard. If you're using a Mac, press
  **Cmd** and **C**.

You can also use CodeWhisperer to change settings like log level and get suggestions for
code references. For more information, see [Setting up CodeWhisperer with
JupyterLab](../../../codewhisperer/latest/userguide/jupyterlab-setup.md "../../../codewhisperer/latest/userguide/jupyterlab-setup.md") and [Features](../../../codewhisperer/latest/userguide/features.md "../../../codewhisperer/latest/userguide/features.md") in the
_Amazon CodeWhisperer User Guide_.
