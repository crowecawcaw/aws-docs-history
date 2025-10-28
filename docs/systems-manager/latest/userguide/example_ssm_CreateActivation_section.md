# Use `CreateActivation` with a CLI

The following code examples show how to use `CreateActivation`.

CLI

**AWS CLI**

**To create a managed instance activation**

The following `create-activation` example creates a managed instance activation.

```
`aws ssm create-activation \
 --default-instance-name `"HybridWebServers"` \
 --iam-role `"HybridWebServersRole"` \
 --registration-limit `5``

```

Output:

```
{
    "ActivationId": "5743558d-563b-4457-8682-d16c3EXAMPLE",
    "ActivationCode": "dRmgnYaFv567vEXAMPLE"
}
```

For more information, see [Step 4: Create a Managed-Instance Activation for a Hybrid Environment](sysman-managed-instance-activation.md "sysman-managed-instance-activation.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [CreateActivation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-activation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-activation.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a managed instance.**

```
New-SSMActivation -DefaultInstanceName "MyWebServers" -IamRole "SSMAutomationRole" -RegistrationLimit 10

```

**Output:**

```
ActivationCode       ActivationId
--------------       ------------
KWChhOxBTiwDcKE9BlKC 08e51e79-1e36-446c-8e63-9458569c1363
```

- For API details, see
  [CreateActivation](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a managed instance.**

```
New-SSMActivation -DefaultInstanceName "MyWebServers" -IamRole "SSMAutomationRole" -RegistrationLimit 10

```

**Output:**

```
ActivationCode       ActivationId
--------------       ------------
KWChhOxBTiwDcKE9BlKC 08e51e79-1e36-446c-8e63-9458569c1363
```

- For API details, see
  [CreateActivation](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
