

# Use `DeleteVirtualMfaDevice` with a CLI
<a name="iam_example_iam_DeleteVirtualMfaDevice_section"></a>

The following code examples show how to use `DeleteVirtualMfaDevice`.

------
#### [ CLI ]

**AWS CLI**  
**To remove a virtual MFA device**  
The following `delete-virtual-mfa-device` command removes the specified MFA device from the current account.  

```
aws iam delete-virtual-mfa-device \
    --serial-number {{arn:aws:iam::123456789012:mfa/MFATest}}
```
This command produces no output.  
For more information, see [Deactivating MFA devices](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_disable.html) in the *AWS IAM User Guide*.  
+  For API details, see [DeleteVirtualMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-virtual-mfa-device.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the IAM virtual MFA device whose ARN is `arn:aws:iam::123456789012:mfa/bob`.**  

```
Remove-IAMVirtualMFADevice -SerialNumber arn:aws:iam::123456789012:mfa/bob
```
**Example 2: This example checks to see whether the IAM user Theresa has an MFA device assigned. If one is found, the device is disabled for the IAM user. If the device is virtual, then it is also deleted.**  

```
$mfa = Get-IAMMFADevice -UserName Theresa
if ($mfa) { 
    Disable-IAMMFADevice -SerialNumber $mfa.SerialNumber -UserName $name 
    if ($mfa.SerialNumber -like "arn:*") { Remove-IAMVirtualMFADevice -SerialNumber $mfa.SerialNumber }
}
```
+  For API details, see [DeleteVirtualMfaDevice](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the IAM virtual MFA device whose ARN is `arn:aws:iam::123456789012:mfa/bob`.**  

```
Remove-IAMVirtualMFADevice -SerialNumber arn:aws:iam::123456789012:mfa/bob
```
**Example 2: This example checks to see whether the IAM user Theresa has an MFA device assigned. If one is found, the device is disabled for the IAM user. If the device is virtual, then it is also deleted.**  

```
$mfa = Get-IAMMFADevice -UserName Theresa
if ($mfa) { 
    Disable-IAMMFADevice -SerialNumber $mfa.SerialNumber -UserName $name 
    if ($mfa.SerialNumber -like "arn:*") { Remove-IAMVirtualMFADevice -SerialNumber $mfa.SerialNumber }
}
```
+  For API details, see [DeleteVirtualMfaDevice](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.