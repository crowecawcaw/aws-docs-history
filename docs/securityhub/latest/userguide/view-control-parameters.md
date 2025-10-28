# Reviewing current control parameter values

It can be helpful to know the current value of a control parameter before you modify it.

You can review the current values for individual control parameters in your account. If you use central configuration, the
delegated AWS Security Hub CSPM administrator can also review parameter values that are specified in a configuration policy.

Choose your preferred method, and follow the steps to review current control parameter values.

Security Hub CSPM console

###### To review current control parameter values (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Controls**. Choose a control.
3. Choose the **Parameters** tab. This tab shows the current parameter values for the control.

Security Hub CSPM API
**To review current control parameter values (API)**

Invoke the [BatchGetSecurityControls](../../1.0/APIReference/API_BatchGetSecurityControls.md "../../1.0/APIReference/API_BatchGetSecurityControls.md") API, and provide one or more security control IDs or
ARNs. The `Parameters` object in the response shows the current parameter values for the specified controls.

For example, the following AWS CLI command shows the current parameter values for `APIGatway.1`, `CloudWatch.15`,
and `IAM.7`. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securityhub batch-get-security-controls \
--region `us-east-1` \
--security-control-ids '[`"APIGateway.1", "CloudWatch.15", "IAM.7"`]'`

```

Choose your preferred method to view the current parameter values in a central configuration policy.

Security Hub CSPM console

###### To review current control parameter values in a configuration policy (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region. 2. In the navigation pane, choose **Settings** and **Configuration**. 3. On the **Policies** tab, select the configuration policy, and then choose **View details**. The
policy details then appear, including current parameter values.

Security Hub CSPM API

###### To review current control parameter values in a configuration policy (API)

1. Invoke the [GetConfigurationPolicy](../../1.0/APIReference/API_GetConfigurationPolicy.md "../../1.0/APIReference/API_GetConfigurationPolicy.md") API from the delegated administrator account in the home
   Region.
2. Provide the ARN or ID of
   the configuration policy whose details you want to see. The response includes current parameter values.

For example, the following AWS CLI command retrieves the current control parameter values in the specified configuration policy.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve
readability.

```
`$` `aws securityhub get-configuration-policy \
--region `us-east-1` \
--identifier `"arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"``

```

Control findings also include the current values of control parameters. In the [AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md"), these
values appear in the `Parameters` field of the `Compliance` object.
To review findings on the Security Hub CSPM console, choose **Findings** in the navigation pane. To review findings
programmatically, use the [GetFindings](../../1.0/APIReference/API_GetFindings.md "../../1.0/APIReference/API_GetFindings.md")
operation of the Security Hub CSPM API.
