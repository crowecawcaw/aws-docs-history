

# Use `ListVirtualMfaDevices` with a CLI
<a name="iam_example_iam_ListVirtualMfaDevices_section"></a>

The following code examples show how to use `ListVirtualMfaDevices`.

------
#### [ CLI ]

**AWS CLI**  
**To list virtual MFA devices**  
The following `list-virtual-mfa-devices` command lists the virtual MFA devices that have been configured for the current account.  

```
aws iam list-virtual-mfa-devices
```
Output:  

```
{
    "VirtualMFADevices": [
        {
            "SerialNumber": "arn:aws:iam::123456789012:mfa/ExampleMFADevice"
        },
        {
            "SerialNumber": "arn:aws:iam::123456789012:mfa/Fred"
        }
    ]
}
```
For more information, see [Enabling a virtual multi-factor authentication (MFA) device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html) in the *AWS IAM User Guide*.  
+  For API details, see [ListVirtualMfaDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-virtual-mfa-devices.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example retrieves a collection of the virtual MFA devices that are assigned to users in the AWS account. The `User` property of each is an object with details of the IAM user to which the device is assigned.**  

```
Get-IAMVirtualMFADevice -AssignmentStatus Assigned
```
**Output:**  

```
Base32StringSeed : 
EnableDate       : 4/13/2015 12:03:42 PM
QRCodePNG        : 
SerialNumber     : arn:aws:iam::123456789012:mfa/David
User             : Amazon.IdentityManagement.Model.User

Base32StringSeed : 
EnableDate       : 4/13/2015 12:06:41 PM
QRCodePNG        : 
SerialNumber     : arn:aws:iam::123456789012:mfa/root-account-mfa-device
User             : Amazon.IdentityManagement.Model.User
```
+  For API details, see [ListVirtualMfaDevices](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example retrieves a collection of the virtual MFA devices that are assigned to users in the AWS account. The `User` property of each is an object with details of the IAM user to which the device is assigned.**  

```
Get-IAMVirtualMFADevice -AssignmentStatus Assigned
```
**Output:**  

```
Base32StringSeed : 
EnableDate       : 4/13/2015 12:03:42 PM
QRCodePNG        : 
SerialNumber     : arn:aws:iam::123456789012:mfa/David
User             : Amazon.IdentityManagement.Model.User

Base32StringSeed : 
EnableDate       : 4/13/2015 12:06:41 PM
QRCodePNG        : 
SerialNumber     : arn:aws:iam::123456789012:mfa/root-account-mfa-device
User             : Amazon.IdentityManagement.Model.User
```
+  For API details, see [ListVirtualMfaDevices](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.