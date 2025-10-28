# Use `GenerateCredentialReport` with an AWS SDK or CLI

The following code examples show how to use `GenerateCredentialReport`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Manage your account](iam_example_iam_Scenario_AccountManagement_section.md "iam_example_iam_Scenario_AccountManagement_section.md")

CLI

**AWS CLI**

**To generate a credential report**

The following example attempts to generate a credential report for the AWS account.

```
`aws iam generate-credential-report`

```

Output:

```
{
    "State":  "STARTED",
    "Description": "No report exists. Starting a new report generation task"
}
```

For more information, see [Getting credential reports for your AWS account](id_credentials_getting-report.md "id_credentials_getting-report.md") in the _AWS IAM User Guide_.

- For API details, see
  [GenerateCredentialReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-credential-report.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-credential-report.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example requests generation of a new report, which can be done every four hours. If the last report is still recent the State field reads `COMPLETE`. Use `Get-IAMCredentialReport` to view the completed report.**

```
Request-IAMCredentialReport

```

**Output:**

```
Description                                                    State
-----------                                                    -----
No report exists. Starting a new report generation task        STARTED
```

- For API details, see
  [GenerateCredentialReport](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example requests generation of a new report, which can be done every four hours. If the last report is still recent the State field reads `COMPLETE`. Use `Get-IAMCredentialReport` to view the completed report.**

```
Request-IAMCredentialReport

```

**Output:**

```
Description                                                    State
-----------                                                    -----
No report exists. Starting a new report generation task        STARTED
```

- For API details, see
  [GenerateCredentialReport](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples").

```
def generate_credential_report():
    """
    Starts generation of a credentials report about the current account. After
    calling this function to generate the report, call get_credential_report
    to get the latest report. A new report can be generated a minimum of four hours
    after the last one was generated.
    """
    try:
        response = iam.meta.client.generate_credential_report()
        logger.info(
            "Generating credentials report for your account. " "Current state is %s.",
            response["State"],
        )
    except ClientError:
        logger.exception("Couldn't generate a credentials report for your account.")
        raise
    else:
        return response




```

- For API details, see
  [GenerateCredentialReport](../../../goto/boto3/iam-2010-05-08/GenerateCredentialReport.md "../../../goto/boto3/iam-2010-05-08/GenerateCredentialReport.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
