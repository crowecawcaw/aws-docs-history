

# Use `GetServiceLastAccessedDetailsWithEntities` with a CLI
<a name="iam_example_iam_GetServiceLastAccessedDetailsWithEntities_section"></a>

The following code examples show how to use `GetServiceLastAccessedDetailsWithEntities`.

------
#### [ CLI ]

**AWS CLI**  
**To retrieve a service access report with details for a service**  
The following `get-service-last-accessed-details-with-entities` example retrieves a report that contains details about IAM users and other entities that accessed the specified service. To generate a report, use the `generate-service-last-accessed-details` command. To get a list of services accessed with namespaces, use `get-service-last-accessed-details`.  

```
aws iam get-service-last-accessed-details-with-entities \
    --job-id {{78b6c2ba-d09e-6xmp-7039-ecde30b26916}} \
    --service-namespace {{lambda}}
```
Output:  

```
{
    "JobStatus": "COMPLETED",
    "JobCreationDate": "2019-10-01T03:55:41.756Z",
    "JobCompletionDate": "2019-10-01T03:55:42.533Z",
    "EntityDetailsList": [
        {
            "EntityInfo": {
                "Arn": "arn:aws:iam::123456789012:user/admin",
                "Name": "admin",
                "Type": "USER",
                "Id": "AIDAIO2XMPLENQEXAMPLE",
                "Path": "/"
            },
            "LastAuthenticated": "2019-09-30T23:02:00Z"
        },
        {
            "EntityInfo": {
                "Arn": "arn:aws:iam::123456789012:user/developer",
                "Name": "developer",
                "Type": "USER",
                "Id": "AIDAIBEYXMPL2YEXAMPLE",
                "Path": "/"
            },
            "LastAuthenticated": "2019-09-16T19:34:00Z"
        }
    ]
}
```
For more information, see [Refining permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) in the *AWS IAM User Guide*.  
+  For API details, see [GetServiceLastAccessedDetailsWithEntities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-last-accessed-details-with-entities.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example provides the last accessed timestamp for the service in the request by that respective IAM entity.**  

```
$results = Get-IAMServiceLastAccessedDetailWithEntity -JobId f0b7a819-eab0-929b-dc26-ca598911cb9f -ServiceNamespace ec2
$results
```
**Output:**  

```
EntityDetailsList : {Amazon.IdentityManagement.Model.EntityDetails}
Error             : 
IsTruncated       : False
JobCompletionDate : 12/29/19 11:19:31 AM
JobCreationDate   : 12/29/19 11:19:31 AM
JobStatus         : COMPLETED
Marker            :
```

```
$results.EntityDetailsList
```
**Output:**  

```
EntityInfo                                 LastAuthenticated
----------                                 -----------------
Amazon.IdentityManagement.Model.EntityInfo 11/16/19 3:47:00 PM
```

```
$results.EntityInfo
```
**Output:**  

```
Arn  : arn:aws:iam::123456789012:user/TestUser
Id   : AIDA4NBK5CXF5TZHU1234
Name : TestUser
Path : /
Type : USER
```
+  For API details, see [GetServiceLastAccessedDetailsWithEntities](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example provides the last accessed timestamp for the service in the request by that respective IAM entity.**  

```
$results = Get-IAMServiceLastAccessedDetailWithEntity -JobId f0b7a819-eab0-929b-dc26-ca598911cb9f -ServiceNamespace ec2
$results
```
**Output:**  

```
EntityDetailsList : {Amazon.IdentityManagement.Model.EntityDetails}
Error             : 
IsTruncated       : False
JobCompletionDate : 12/29/19 11:19:31 AM
JobCreationDate   : 12/29/19 11:19:31 AM
JobStatus         : COMPLETED
Marker            :
```

```
$results.EntityDetailsList
```
**Output:**  

```
EntityInfo                                 LastAuthenticated
----------                                 -----------------
Amazon.IdentityManagement.Model.EntityInfo 11/16/19 3:47:00 PM
```

```
$results.EntityInfo
```
**Output:**  

```
Arn  : arn:aws:iam::123456789012:user/TestUser
Id   : AIDA4NBK5CXF5TZHU1234
Name : TestUser
Path : /
Type : USER
```
+  For API details, see [GetServiceLastAccessedDetailsWithEntities](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.