

# Use `UpdateAssumeRolePolicy` with a CLI
<a name="iam_example_iam_UpdateAssumeRolePolicy_section"></a>

The following code examples show how to use `UpdateAssumeRolePolicy`.

------
#### [ CLI ]

**AWS CLI**  
**To update the trust policy for an IAM role**  
The following `update-assume-role-policy` command updates the trust policy for the role named `Test-Role`.  

```
aws iam update-assume-role-policy \
    --role-name {{Test-Role}} \
    --policy-document {{file://Test-Role-Trust-Policy.json}}
```
This command produces no output.  
The trust policy is defined as a JSON document in the *Test-Role-Trust-Policy.json* file. (The file name and extension do not have significance.) The trust policy must specify a principal.  
To update the permissions policy for a role, use the `put-role-policy` command.  
For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *AWS IAM User Guide*.  
+  For API details, see [UpdateAssumeRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-assume-role-policy.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example updates the IAM role named `ClientRole` with a new trust policy, the contents of which come from the file `ClientRolePolicy.json`. Note that you must use the `-Raw` switch parameter to successfully process the contents of the JSON file.**  

```
Update-IAMAssumeRolePolicy -RoleName ClientRole -PolicyDocument (Get-Content -raw ClientRolePolicy.json)
```
+  For API details, see [UpdateAssumeRolePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example updates the IAM role named `ClientRole` with a new trust policy, the contents of which come from the file `ClientRolePolicy.json`. Note that you must use the `-Raw` switch parameter to successfully process the contents of the JSON file.**  

```
Update-IAMAssumeRolePolicy -RoleName ClientRole -PolicyDocument (Get-Content -raw ClientRolePolicy.json)
```
+  For API details, see [UpdateAssumeRolePolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.