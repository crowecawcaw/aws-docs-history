# Examples for baseline API usage

This section contains examples of input and output parameters for the AWS Control Tower baseline
APIs.

## `DisableBaseline`

For more information about this API operation, see [DisableBaseline](../APIReference/API_DisableBaseline.md "../APIReference/API_DisableBaseline.md").

`DisableBaseline` input:

```
{
    "enabledBaselineIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledbaseline/AB12CD34EF56GH789"
}
```

`DisableBaseline` output:

```
{
    "operationIdentifier": "58f12232-26be-4735-a3e9-dd30d90f021f"
}
```

`DisableBaseline` CLI example:

```
aws controltower disable-baseline \
    --enabled-baseline-identifier arn:aws:controltower:us-west-2:123456789012:enabledbaseline/AB12CD34EF56GH789 \
    --region us-west-2
```

## `EnableBaseline`

For more information about this API operation, see [EnableBaseline](../APIReference/API_EnableBaseline.md "../APIReference/API_EnableBaseline.md").

`EnableBaseline` input:

```
{
    "baselineIdentifier": "arn:aws:controltower:us-west-2::baseline:17BSJV3IGJ2QSGA2",
    "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-kgj0txdhpa/ou-r9mj-4j3mzjql",
    "baselineVersion": "3.0",
    "parameters": [
        {
            "key": "IdentityCenterEnabledBaselineArn",
            "value": "arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHCR4CJTSI4W07MZ"
        }
    ]
}
```

`EnableBaseline` output, returning a new resource:

```
{
    "operationIdentifier": "58f12232-26be-4735-a3e9-dd30d90f021f",
    "arn": "arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAGF7TNOHRD7ES5VV"
}
```

`EnableBaseline` CLI example:

This example shows enabling a baseline for an AWS Organizations organization that has the
landing zone opted-in to AWS IAM Identity Center access, managed by AWS Control Tower. To retrieve your
Identity Center `EnabledBaseline` identifier, you can call the
`ListEnabledBaselines` API, filtering on the Identity Center baseline:
`(arn:aws:controltower:`Region`::baseline/LN25R72TTG6IGPTQ)`

```
aws controltower list-enabled-baselines \
    --filter baselineIdentifiers=arn:aws:controltower:us-west-2::baseline/LN25R72TTG6IGPTQ \
    --region us-west-2
```

The response will show the `EnabledBaseline` detail, which shows its
identifier.

```
{
    "enabledBaselines": [
        {
            "arn": "arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHXS7P6C4I453EZC",
            "baselineIdentifier": "arn:aws:controltower:us-west-2::baseline/LN25R72TTG6IGPTQ",
            "targetIdentifier": "arn:aws:organizations::123456789012:account/o-aq21sw43de5/123456789012",
            "statusSummary": {
                "status": "SUCCEEDED"
            }
        }
    ]
}
```

###### Note

Make note of the ARN value from the response, and pass this value as a parameter
to enable the default baseline.

```
aws controltower enable-baseline \
    --baseline-identifier arn:aws:controltower:us-west-2::baseline/17BSJV3IGJ2QSGA2 \
    --baseline-version 3.0 \
    --target-identifier arn:aws:organizations::123456789012:ou/o-aq21sw43de5/ou-po90-lk87jh65 \
    --parameters '[{"key":"IdentityCenterEnabledBaselineArn","value":"arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHXS7P6C4I453EZC"}]' \
    --region us-west-2
```

For an organization with the landing zone opted-out from AWS Control Tower management of IAM Identity Center,
enable the baseline without the parameter.

```
aws controltower enable-baseline \
    --baseline-identifier arn:aws:controltower:us-west-2::baseline/17BSJV3IGJ2QSGA2 \
    --baseline-version 3.0 \
    --target-identifier arn:aws:organizations::123456789012:ou/o-aq21sw43de5/ou-po90-lk87jh65 \
    --region us-west-2
```

## `GetBaseline`

For more information about this API operation, see [GetBaseline](../APIReference/API_GetBaseline.md "../APIReference/API_GetBaseline.md").

`GetBaseline` input:

```
{
    "baselineIdentifier": "arn:aws:controltower:us-west-2::baseline/17BSJV3IGJ2QSGA2"
}
```

`GetBaseline` output:

```
{
    "arn": "arn:aws:controltower:us-west-2::baseline/17BSJV3IGJ2QSGA2",
    "name": "AWSControlTowerBaseline",
    "description": "Sets up resources and mandatory controls for member accounts within the target OU, required for AWS Control Tower governance.",
}
```

`GetBaseline` CLI example:

```
aws controltower get-baseline \
    --baseline-identifier arn:aws:controltower:us-west-2::baseline/17BSJV3IGJ2QSGA2 \
    --region us-west-2
```

## `GetBaselineOperation`

For more information about this API operation, see [GetBaselineOperation](../APIReference/API_GetBaselineOperation.md "../APIReference/API_GetBaselineOperation.md").

`GetBaselineOperation` input:

```
{
    "operationIdentifier": "58f12232-26be-4735-a3e9-dd30d90f021f"
}
```

`GetBaselineOperation` output:

```
{
    "baselineOperation": {
        "operationIdentifier": "58f12232-26be-4735-a3e9-dd30d90f021f",
        "operationType": "DISABLE_BASELINE",
        "status": "FAILED",
        "startTime": "2023-01-12T19:05:00Z",
        "endTime": "2023-01-12T19:45:00Z",
        "statusMessage": "Can't perform DisableBaseline on a parent target with governed child OUs"
    }
}
```

`GetBaselineOperation` CLI example:

```
aws controltower get-baseline-operation \
    --operation-identifier 58f12232-26be-4735-a3e9-dd30d90f021f \
    --region us-west-2
```

## `GetEnabledBaseline`

For more information about this API operation, see [GetEnabledBaseline](../APIReference/API_GetEnabledBaseline.md "../APIReference/API_GetEnabledBaseline.md").

`GetEnabledBaseline` input:

```
{
    "enabledBaselineIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHCR4CJTSI4W07MZ"
}
```

`GetEnabledBaseline` output:

```
{
    "enabledBaselineDetails": {
        "arn": "arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHCR4CJTSI4W07MZ",
        "baselineIdentifier": "arn:aws:controltower:us-west-2::baseline:17BSJV3IGJ2QSGA2",
        "baselineVersion": "3.0",
        "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-kgj0txdhpa/ou-r9mj-4j3mzjql",
        "statusSummary": {
            "status": "SUCCEEDED",
            "lastOperationIdentifier": "58f12232-26be-4735-a3e9-dd30d90f021f"
        },
        "parameters": [
            {
                "key": "IdentityCenterEnabledBaselineArn",
                "value": "arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHCR4CJTSI4W07MZ"
            }
        ]
    }
}
```

`GetEnabledBaseline` CLI example:

```
aws controltower get-enabled-baseline \
    --enabled-baseline-identifier arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHXS7P6C4I453EZC \
    --region us-west-2
```

## `ListBaselines`

For more information about this API operation, see [ListBaselines](../APIReference/API_ListBaselines.md "../APIReference/API_ListBaselines.md").

`ListBaselines` input (using optional inputs):

```
{
    "nextToken": "AbCd1234",
    "maxResults": "4"
}
```

`ListBaselines` output:

```
{
    "baselines": [
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/4T4HA1KMO10S6311",
            "name": "AuditBaseline",
            "description": "Sets up resources to monitor security and compliance of accounts in your organization."
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/J8HX46AHS5MIKQPD",
            "name": "LogArchiveBaseline",
            "description": "Sets up a central repository for logs of API activities and resource configurations from accounts in your organization."
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/LN25R72TTG6IGPTQ",
            "name": "IdentityCenterBaseline",
            "description": "Sets up shared resources for AWS Identity Center, which prepares the AWSControlTowerBaseline to set up Identity Center access for accounts."
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2",
            "name": "AWSControlTowerBaseline",
            "description": "Sets up resources and mandatory controls for member accounts within the target OU, required for AWS Control Tower governance."
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/3WPD0NA6TJ9AOMU2",
            "name": "BackupCentralVaultBaseline",
            "description": "Sets up central AWS Backup vault in your organization."
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/H6C5JFCJJ3CPU3J5",
            "name": "BackupManagerBaseline",
            "description": "Sets up delegated admin and AWS Backup Audit Manager."
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/APO9ATVPBKFRRGLK",
            "name": "BackupBaseline",
            "description": "Sets up local Backup vault and attach Backup policy."
        }
    ]
}
```

`ListBaselines` CLI example:

```
aws controltower list-baselines \
    --region us-west-2
```

## `ListEnabledBaselines`

The `ListEnabledBaselines` API has an optional parameter that allows you to view the baselines as they apply to the accounts that are members of an OU. The examples that follow show some CLI commands you can use to view the baselines for an account. AWS Control Tower refers to these baselines, which are enabled on the OU, but apply to each account within the OU, as _child enabled baselines_, because they derive their governance configuration from the baselines that are applied on the OU.

For more information about this API operation, see [ListEnabledBaselines](../APIReference/API_ListEnabledBaselines.md "../APIReference/API_ListEnabledBaselines.md").

`ListEnabledBaselines` input to show child enabled baselines:

```
aws controltower list-enabled-baselines --include-children
```

`ListEnabledBaselines` output to view child enabled baselines:

```
{
    "enabledBaselines": [
        {
            "arn": "arn:aws:controltower:us-east-1:666355521292:enabledbaseline/XO2UQ1PC6BB5085S5",
            "baselineIdentifier": "arn:aws:controltower:us-east-1::baseline/APO9ATVPBKFRRGLK",
            "baselineVersion": "1.0",
            "statusSummary": {
                "lastOperationIdentifier": "07d6d2b8-e357-4f96-ba00-98ea88143445",
                "status": "SUCCEEDED"
            },
            "targetIdentifier": "arn:aws:organizations::666355521292:ou/o-vaex10vaey/ou-k86y-ld9k8vpu"
        },
        {
            "arn": "arn:aws:controltower:us-east-1:666355521292:enabledbaseline/XAFPKQQXOJB50ZWQH",
            "baselineIdentifier": "arn:aws:controltower:us-east-1::baseline/APO9ATVPBKFRRGLK",
            "baselineVersion": "1.0",
            "parentIdentifier": "arn:aws:controltower:us-east-1:666355521292:enabledbaseline/XOIZ4G08CWB50ZWON",
            "statusSummary": {
                "lastOperationIdentifier": "3508793e-48c8-4895-965b-3dc6abd52b6b",
                "status": "SUCCEEDED"
            },
            "targetIdentifier": "arn:aws:organizations::666355521292:account/o-vaex10vaey/183295447314"
        }
]
```

###### Note

In the previous example, the `parentIdentifier` field shows the enabled baseline of the parent OU for this child enabled baseline.

View all baselines applied on a specific target (OU or account):

```
aws controltower list-enabled-baselines \
    --filter '{
        "targetIdentifiers": ["`TARGET_ARN`"]
    }
```

View all OUs that have a specific baseline:

```
aws controltower list-enabled-baselines \
    --filter '{
        "baselineIdentifiers": ["`BASELINE_ARN`"]
    }'
```

View all OUs and accounts that have a specific baseline:

```
aws controltower list-enabled-baselines \
    --filter '{
        "baselineIdentifiers": ["`BASELINE_ARN`"]
    }'  \
    --include-children
```

View all accounts in an OU that have Baseline B enabled:

```
### First fetch the enabled baseline record for Baseline B on the OU
 aws controltower list-enabled-baselines \
    --filter '{
        "targetIdentifiers": ["`OU_TARGET_ARN`"],
        "baselineIdentifiers": ["BASELINE_ARN_FOR_BASELINE_B"]
    }'

### Call ListEnabled baseline to fetch all accounts that have their parent as the enabled baseline record on the OU
aws controltower list-enabled-baselines \
    --filter '{
        "parentIdentifiers": ["`ENABLED_BASELINE_ARN_FOR_OU`"]
    }' \
    --include-children
```

###### More about child enabled baselines

- You can use `GetEnabledBaseline` API to view detailed information about a specific child enabled baseline
- You can use the `GetBaselineOperation` API to view an operation performed on the child enabled baseline
- You cannot call any write APIs, such as `EnableBaseline`, `UpdateEnabledBaseline`, `ResetEnabledBaseline` or `DisableBaseline`, on a child enabled baseline directly.
- Child enabled baseline resources can be modified by means of the AWS Control Tower service only, through operations that are performed on the parent OU, or by means of Account Factory.

Examples for using filters:

`ListEnabledBaselines` input (no filters):

```
{
    "nextToken": "bde7-XX0c6fXXXXXX",
    "maxResults": 5
}
```

`ListEnabledBaselines` input (`baselineIdentifiers` filter
only):

```
{
    "filter": {
        "baselineIdentifiers": ['arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2', 'arn:aws:controltower:us-east-1::baseline/12GZU8CKZKVMS2AW']
    },
    "nextToken": "bde7-XX0c6fXXXXXX",
    "maxResults": 5
}
```

`ListEnabledBaselines` input (`targetIdentifiers` filter
only):

```
{
    "filter": {
        "targetIdentifiers": ['arn:aws:organizations::123456789012:ou/o-s9511vn103/ou-xqj7-fex1u317', 'arn:aws:organizations::123456789012:ou/o-s9511vn103/ou-xqj7-11q6n2cf']
    },
    "nextToken": "bde7-XX0c6fXXXXXX",
    "maxResults": 2
}
```

`ListEnabledBaselines` input (`baselineIdentifiers` and
`targetIdentifiers` filters):

```
{
    "filter": {
        "baselineIdentifiers": ['arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2']
        "targetIdentifiers": ['arn:aws:organizations::123456789012:ou/o-s9511vn103/ou-xqj7-fex1u317']
    },
    "nextToken": "bde7-XX0c6fXXXXXX",
    "maxResults": 5
}
```

`ListEnabledBaselines` output:

```
{
    "enabledBaselines": [
        {
            "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAHCR4CJTSI4W07MZ",
            "baselineIdentifier": "arn:aws:controltower:us-east-1::baseline:17BSJV3IGJ2QSGA2",
            "baselineVersion": "3.0",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-kgj0txdhpa/ou-r9mj-4j3mzjql",
            "statusSummary": {
                "status": "SUCCEEDED",
                "lastOperationIdentifier": "58f12232-26be-4735-a3e9-dd30d90f021f"
            }
        },
        {
            "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAJ9NKW88AA4W9CLL",
            "baselineIdentifier": "arn:aws:controltower:us-east-1::baseline:17BSJV3IGJ2QSGA2",
            "baselineVersion": "4.0",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-s9511vn103/ou-xqj7-fex1u317",
            "statusSummary": {
            "status": "FAILED",
                "lastOperationIdentifier": "81e02df1-2b4d-48f0-838f-3833b93dcdc0"
            }
        }
    ],
    "nextToken": "e2bXXXXX6cab"
}
```

CLI example with one type of filter (`baselineIdentifiers` filter):

```
aws controltower list-enabled-baselines \
    --filter baselineIdentifiers=arn:aws:controltower:us-west-2::baseline/17BSJV3IGJ2QSGA2,arn:aws:controltower:us-west-2::baseline/LN25R72TTG6IGPTQ \
    --region us-west-2
```

CLI example using multiple filters (`baselineIdentifiers` and
`targetIdentifiers` filters):

```
aws controltower list-enabled-baselines \
    --filter targetIdentifiers=arn:aws:organizations::123456789012:ou/o-aq21sw43de5/ou-po90-lk87jh65,baselineIdentifiers=arn:aws:controltower:us-west-2::baseline/17BSJV3IGJ2QSGA2 \
    --region us-west-2
```

## `ResetEnabledBaseline`

For more information about this API operation, see [ResetEnabledBaseline](../APIReference/API_ResetEnabledBaseline.md "../APIReference/API_ResetEnabledBaseline.md").

`ResetEnabledbaseline` input:

```
{
    "enabledBaselineIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAJ9NKW88AA4W9CLL"
}
```

`ResetEnabledBaseline` output:

```
{
    "operationIdentifier": "81e02df1-2b4d-48f0-838f-3833b93dcdc0"
}
```

`ResetEnabledBaseline` CLI example:

```
aws controltower reset-enabled-baseline \
    --enabled-baseline-identifier arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHXS7P6C4I453EZC \
    --region us-west-2
```

## `UpdateEnabledBaseline`

For more information about this API operation, see [UpdateEnabledBaseline](../APIReference/API_UpdateEnabledBaseline.md "../APIReference/API_UpdateEnabledBaseline.md").

`UpdateEnabledBaseline` input:

```
{
    "enabledBaselineIdentifier": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAJ9NKW88AA4W9CLL",
    "baselineVersion": "4.0",
    "parameters": [
        {
            "key": "IdentityCenterEnabledBaselineArn",
            "value": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAHCR4CJTSI4W07MZ"
        }
    ]
}
```

`UpdateEnabledBaseline` output:

```
{
    "operationIdentifier": "81e02df1-2b4d-48f0-838f-3833b93dcdc0"
}
```

`UpdateEnabledBaseline` CLI example:

```
aws controltower update-enabled-baseline \
    --enabled-baseline-identifier arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHXS7P6C4I453EZC \
    --baseline-version 4.0
    --parameters '[{"key":"IdentityCenterEnabledBaselineArn","value":"arn:aws:controltower:us-west-2:123456789012:enabledbaseline/XAHXS7P6C4I453EZC"}]' \
    --region us-west-2
```
