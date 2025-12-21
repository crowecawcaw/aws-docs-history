# CodeRepository object

in ASFF

The `CodeRepository` object provides information about an external code
repository that you connected to AWS resources and configured Amazon Inspector to scan for
vulnerabilities.

The following example shows the AWS Security Finding Format (ASFF) syntax for the `CodeRepository`
object. To view descriptions of `CodeRepository` attributes, see [CodeRepositoryDetails](../../1.0/APIReference/API_CodeRepositoryDetails.md "../../1.0/APIReference/API_CodeRepositoryDetails.md") in the _AWS Security Hub API Reference_. For
background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

**Example**

```
"CodeRepository": {
    "ProviderType": "GITLAB_SELF_MANAGED",
    "ProjectName": "projectName",
    "CodeSecurityIntegrationArn": "arn:aws:inspector2:us-east-1:123456789012:codesecurity-integration/00000000-0000-0000-0000-000000000000"
}
```
