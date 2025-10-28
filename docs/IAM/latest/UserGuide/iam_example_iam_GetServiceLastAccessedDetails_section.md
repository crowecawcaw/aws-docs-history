# Use `GetServiceLastAccessedDetails` with a CLI

The following code examples show how to use `GetServiceLastAccessedDetails`.

CLI

**AWS CLI**

**To retrieve a service access report**

The following `get-service-last-accessed-details` example retrieves a previously generated report that lists the services accessed by IAM entities. To generate a report, use the `generate-service-last-accessed-details` command.

```
`aws iam get-service-last-accessed-details \
 --job-id `2eb6c2b8-7b4c-3xmp-3c13-03b72c8cdfdc``

```

Output:

```
{
    "JobStatus": "COMPLETED",
    "JobCreationDate": "2019-10-01T03:50:35.929Z",
    "ServicesLastAccessed": [
        ...
        {
            "ServiceName": "AWS Lambda",
            "LastAuthenticated": "2019-09-30T23:02:00Z",
            "ServiceNamespace": "lambda",
            "LastAuthenticatedEntity": "arn:aws:iam::123456789012:user/admin",
            "TotalAuthenticatedEntities": 6
        },
    ]
}
```

For more information, see [Refining permissions in AWS using last accessed information](access_policies_access-advisor.md "access_policies_access-advisor.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetServiceLastAccessedDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-last-accessed-details.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-last-accessed-details.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example provides details of the service last accessed by the IAM entity(user, group, role or policy) associated in Request call.**

```
Request-IAMServiceLastAccessedDetail -Arn arn:aws:iam::123456789012:user/TestUser

```

**Output:**

```
f0b7a819-eab0-929b-dc26-ca598911cb9f
```

```
Get-IAMServiceLastAccessedDetail -JobId f0b7a819-eab0-929b-dc26-ca598911cb9f

```

- For API details, see
  [GetServiceLastAccessedDetails](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example provides details of the service last accessed by the IAM entity(user, group, role or policy) associated in Request call.**

```
Request-IAMServiceLastAccessedDetail -Arn arn:aws:iam::123456789012:user/TestUser

```

**Output:**

```
f0b7a819-eab0-929b-dc26-ca598911cb9f
```

```
Get-IAMServiceLastAccessedDetail -JobId f0b7a819-eab0-929b-dc26-ca598911cb9f

```

- For API details, see
  [GetServiceLastAccessedDetails](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
