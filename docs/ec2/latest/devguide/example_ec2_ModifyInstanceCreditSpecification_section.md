

# Use `ModifyInstanceCreditSpecification` with a CLI
<a name="example_ec2_ModifyInstanceCreditSpecification_section"></a>

The following code examples show how to use `ModifyInstanceCreditSpecification`.

------
#### [ CLI ]

**AWS CLI**  
**To modify the credit option for CPU usage of an instance**  
This example modifies the credit option for CPU usage of the specified instance in the specified region to "unlimited". Valid credit options are "standard" and "unlimited".  
Command:  

```
aws ec2 modify-instance-credit-specification --instance-credit-specification {{"InstanceId=i-1234567890abcdef0,CpuCredits=unlimited"}}
```
Output:  

```
{
  "SuccessfulInstanceCreditSpecifications": [
    {
      "InstanceId": "i-1234567890abcdef0"
    }
  ],
  "UnsuccessfulInstanceCreditSpecifications": []
}
```
+  For API details, see [ModifyInstanceCreditSpecification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-credit-specification.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This enables T2 unlimited credits for instance i-01234567890abcdef.**  

```
$Credit = New-Object -TypeName Amazon.EC2.Model.InstanceCreditSpecificationRequest
$Credit.InstanceId = "i-01234567890abcdef"
$Credit.CpuCredits = "unlimited"
Edit-EC2InstanceCreditSpecification -InstanceCreditSpecification $Credit
```
+  For API details, see [ModifyInstanceCreditSpecification](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This enables T2 unlimited credits for instance i-01234567890abcdef.**  

```
$Credit = New-Object -TypeName Amazon.EC2.Model.InstanceCreditSpecificationRequest
$Credit.InstanceId = "i-01234567890abcdef"
$Credit.CpuCredits = "unlimited"
Edit-EC2InstanceCreditSpecification -InstanceCreditSpecification $Credit
```
+  For API details, see [ModifyInstanceCreditSpecification](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.