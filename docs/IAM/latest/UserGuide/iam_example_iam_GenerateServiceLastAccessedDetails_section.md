# Use `GenerateServiceLastAccessedDetails` with a CLI

The following code examples show how to use `GenerateServiceLastAccessedDetails`.

CLI

**AWS CLI**

**Example 1: To generate a service access report for a custom policy**

The following `generate-service-last-accessed-details` example starts a background job to generate a report that lists the services accessed by IAM users and other entities with a custom policy named `intern-boundary`. You can display the report after it is created by running the `get-service-last-accessed-details` command.

```
`aws iam generate-service-last-accessed-details \
 --arn `arn:aws:iam::123456789012:policy/intern-boundary``

```

Output:

```
{
    "JobId": "2eb6c2b8-7b4c-3xmp-3c13-03b72c8cdfdc"
}
```

**Example 2: To generate a service access report for the AWS managed AdministratorAccess policy**

The following `generate-service-last-accessed-details` example starts a background job to generate a report that lists the services accessed by IAM users and other entities with the AWS managed `AdministratorAccess` policy. You can display the report after it is created by running the `get-service-last-accessed-details` command.

```
`aws iam generate-service-last-accessed-details \
 --arn `arn:aws:iam::aws:policy/AdministratorAccess``

```

Output:

```
{
    "JobId": "78b6c2ba-d09e-6xmp-7039-ecde30b26916"
}
```

For more information, see [Refining permissions in AWS using last accessed information](access_policies_access-advisor.md "access_policies_access-advisor.md") in the _AWS IAM User Guide_.

- For API details, see
  [GenerateServiceLastAccessedDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-service-last-accessed-details.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-service-last-accessed-details.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example is equivalent cmdlet of GenerateServiceLastAccessedDetails API. This provides with a job id which can be used in Get-IAMServiceLastAccessedDetail and Get-IAMServiceLastAccessedDetailWithEntity**

```
Request-IAMServiceLastAccessedDetail -Arn arn:aws:iam::123456789012:user/TestUser

```

- For API details, see
  [GenerateServiceLastAccessedDetails](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example is equivalent cmdlet of GenerateServiceLastAccessedDetails API. This provides with a job id which can be used in Get-IAMServiceLastAccessedDetail and Get-IAMServiceLastAccessedDetailWithEntity**

```
Request-IAMServiceLastAccessedDetail -Arn arn:aws:iam::123456789012:user/TestUser

```

- For API details, see
  [GenerateServiceLastAccessedDetails](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
