# Use `GetAccountSummary` with an AWS SDK or CLI

The following code examples show how to use `GetAccountSummary`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Manage your account](iam_example_iam_Scenario_AccountManagement_section.md "iam_example_iam_Scenario_AccountManagement_section.md")

CLI

**AWS CLI**

**To get information about IAM entity usage and IAM quotas in the current account**

The following `get-account-summary` command returns information about the current IAM entity usage and current IAM entity quotas in the account.

```
`aws iam get-account-summary`

```

Output:

```
{
    "SummaryMap": {
        "UsersQuota": 5000,
        "GroupsQuota": 100,
        "InstanceProfiles": 6,
        "SigningCertificatesPerUserQuota": 2,
        "AccountAccessKeysPresent": 0,
        "RolesQuota": 250,
        "RolePolicySizeQuota": 10240,
        "AccountSigningCertificatesPresent": 0,
        "Users": 27,
        "ServerCertificatesQuota": 20,
        "ServerCertificates": 0,
        "AssumeRolePolicySizeQuota": 2048,
        "Groups": 7,
        "MFADevicesInUse": 1,
        "Roles": 3,
        "AccountMFAEnabled": 1,
        "MFADevices": 3,
        "GroupsPerUserQuota": 10,
        "GroupPolicySizeQuota": 5120,
        "InstanceProfilesQuota": 100,
        "AccessKeysPerUserQuota": 2,
        "Providers": 0,
        "UserPolicySizeQuota": 2048
    }
}
```

For more information about entity limitations, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetAccountSummary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-account-summary.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-account-summary.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns information about the current IAM entity usage and current IAM entity quotas in the AWS account.**

```
Get-IAMAccountSummary

```

**Output:**

```

Key                                        Value
Users                                      7
GroupPolicySizeQuota                       5120
PolicyVersionsInUseQuota                   10000
ServerCertificatesQuota                    20
AccountSigningCertificatesPresent          0
AccountAccessKeysPresent                   0
Groups                                     3
UsersQuota                                 5000
RolePolicySizeQuota                        10240
UserPolicySizeQuota                        2048
GroupsPerUserQuota                         10
AssumeRolePolicySizeQuota                  2048
AttachedPoliciesPerGroupQuota              2
Roles                                      9
VersionsPerPolicyQuota                     5
GroupsQuota                                100
PolicySizeQuota                            5120
Policies                                   5
RolesQuota                                 250
ServerCertificates                         0
AttachedPoliciesPerRoleQuota               2
MFADevicesInUse                            2
PoliciesQuota                              1000
AccountMFAEnabled                          1
Providers                                  2
InstanceProfilesQuota                      100
MFADevices                                 4
AccessKeysPerUserQuota                     2
AttachedPoliciesPerUserQuota               2
SigningCertificatesPerUserQuota            2
PolicyVersionsInUse                        4
InstanceProfiles                           1
...
```

- For API details, see
  [GetAccountSummary](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns information about the current IAM entity usage and current IAM entity quotas in the AWS account.**

```
Get-IAMAccountSummary

```

**Output:**

```

Key                                        Value
Users                                      7
GroupPolicySizeQuota                       5120
PolicyVersionsInUseQuota                   10000
ServerCertificatesQuota                    20
AccountSigningCertificatesPresent          0
AccountAccessKeysPresent                   0
Groups                                     3
UsersQuota                                 5000
RolePolicySizeQuota                        10240
UserPolicySizeQuota                        2048
GroupsPerUserQuota                         10
AssumeRolePolicySizeQuota                  2048
AttachedPoliciesPerGroupQuota              2
Roles                                      9
VersionsPerPolicyQuota                     5
GroupsQuota                                100
PolicySizeQuota                            5120
Policies                                   5
RolesQuota                                 250
ServerCertificates                         0
AttachedPoliciesPerRoleQuota               2
MFADevicesInUse                            2
PoliciesQuota                              1000
AccountMFAEnabled                          1
Providers                                  2
InstanceProfilesQuota                      100
MFADevices                                 4
AccessKeysPerUserQuota                     2
AttachedPoliciesPerUserQuota               2
SigningCertificatesPerUserQuota            2
PolicyVersionsInUse                        4
InstanceProfiles                           1
...
```

- For API details, see
  [GetAccountSummary](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples").

```
def get_summary():
    """
    Gets a summary of account usage.

    :return: The summary of account usage.
    """
    try:
        summary = iam.AccountSummary()
        logger.debug(summary.summary_map)
    except ClientError:
        logger.exception("Couldn't get a summary for your account.")
        raise
    else:
        return summary.summary_map




```

- For API details, see
  [GetAccountSummary](../../../goto/boto3/iam-2010-05-08/GetAccountSummary.md "../../../goto/boto3/iam-2010-05-08/GetAccountSummary.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
