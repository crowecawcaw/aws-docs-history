# Use `GetConsoleOutput` with a CLI

The following code examples show how to use `GetConsoleOutput`.

CLI

**AWS CLI**

**Example 1: To get the console output**

The following `get-console-output` example gets the console output for the specified Linux instance.

```
`aws ec2 get-console-output \
 --instance-id `i-1234567890abcdef0``

```

Output:

```
{
    "InstanceId": "i-1234567890abcdef0",
    "Timestamp": "2013-07-25T21:23:53.000Z",
    "Output": "..."
}
```

For more information, see [Instance console output](../../../AWSEC2/latest/UserGuide/instance-console.md#instance-console-console-output "../../../AWSEC2/latest/UserGuide/instance-console.md#instance-console-console-output") in the _Amazon EC2 User Guide_.

**Example 2: To get the latest console output**

The following `get-console-output` example gets the latest console output for the specified Linux instance.

```
`aws ec2 get-console-output \
 --instance-id `i-1234567890abcdef0` \
 --latest \
 --output `text``

```

Output:

```
i-1234567890abcdef0 [    0.000000] Command line: root=LABEL=/ console=tty1 console=ttyS0 selinux=0 nvme_core.io_timeout=4294967295
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
...
Cloud-init v. 0.7.6 finished at Wed, 09 May 2018 19:01:13 +0000. Datasource DataSourceEc2.  Up 21.50 seconds
Amazon Linux AMI release 2018.03
Kernel 4.14.26-46.32.amzn1.x
```

For more information, see [Instance console output](../../../AWSEC2/latest/UserGuide/instance-console.md#instance-console-console-output "../../../AWSEC2/latest/UserGuide/instance-console.md#instance-console-console-output") in the _Amazon EC2 User Guide_.

- For API details, see
  [GetConsoleOutput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-console-output.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-console-output.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example gets the console output for the specified Linux instance. The console output is encoded.**

```
Get-EC2ConsoleOutput -InstanceId i-0e19abcd47c123456

```

**Output:**

```
InstanceId          Output
----------          ------
i-0e194d3c47c123637 WyAgICAwLjAwMDAwMF0gQ29tbW...bGU9dHR5UzAgc2Vs
```

**Example 2: This example stores the encoded console output in a variable and then decodes it.**

```
$Output_encoded = (Get-EC2ConsoleOutput -InstanceId i-0e19abcd47c123456).Output
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($Output_encoded))

```

- For API details, see
  [GetConsoleOutput](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example gets the console output for the specified Linux instance. The console output is encoded.**

```
Get-EC2ConsoleOutput -InstanceId i-0e19abcd47c123456

```

**Output:**

```
InstanceId          Output
----------          ------
i-0e194d3c47c123637 WyAgICAwLjAwMDAwMF0gQ29tbW...bGU9dHR5UzAgc2Vs
```

**Example 2: This example stores the encoded console output in a variable and then decodes it.**

```
$Output_encoded = (Get-EC2ConsoleOutput -InstanceId i-0e19abcd47c123456).Output
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($Output_encoded))

```

- For API details, see
  [GetConsoleOutput](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
