# Viewing Details and Compliance Information for your Conformance Packs for AWS Config

###### Important

For accurate reporting on the compliance status, you must record the `AWS::Config::ResourceCompliance` resource type.
For more information, see [Recording AWS Resources](select-resources.md "select-resources.md").

You can use the AWS Config console or the AWS CLI to view your conformance packs.
The AWS Config console has a unified dashboard. The AWS CLI allows you to run commands for specific information.

Viewing Conformance Packs (Console)
To view your conformance packs in the AWS Management Console, see [Conformance Pack Dashboard Pack](conformance-pack-dashboard.md "conformance-pack-dashboard.md").

Viewing the Details for your Conformance Packs (AWS CLI)

1. Enter the following command.

```
aws configservice describe-conformance-packs
```

OR

```
aws configservice describe-conformance-packs --conformance-pack-name="`MyConformancePack1`"
```

2. You should see output similar to the following.

```
{
    "conformancePackName": "`MyConformancePack1`",
    "conformancePackId": "`conformance-pack-ID`",
    "conformancePackArn": "arn:aws:config:us-west-2:`AccountID`:conformance-pack/`MyConformancePack1`/`conformance-pack-ID`",
    "conformancePackInputParameters": [],
    "lastUpdateRequestedTime": "Thu Jul 18 16:07:05 PDT 2019"
}
```

Viewing the Status for your Conformance Packs (AWS CLI)

1. Enter the following command.

```
aws configservice describe-conformance-pack-status --conformance-pack-name="`MyConformancePack1`"
```

2. You should see output similar to the following .

```
{
    "stackArn": "arn:aws:cloudformation:us-west-2:`AccountID`:stack/awsconfigconforms-`MyConformancePack1`-`conformance-pack-ID`/d4301fe0-a9b1-11e9-994d-025f28dd83ba",
    "conformancePackName": "`MyConformancePack1`",
    "conformancePackId": "`conformance-pack-ID`",
    "lastUpdateCompletedTime": "Thu Jul 18 16:15:17 PDT 2019",
    "conformancePackState": "CREATE_COMPLETE",
    "conformancePackArn": "arn:aws:config:us-west-2:`AccountID`:conformance-pack/`MyConformancePack1`/`conformance-pack-ID`",
    "lastUpdateRequestedTime": "Thu Jul 18 16:14:35 PDT 2019"
}

```

Viewing the Compliance Status for your Conformance Packs (AWS CLI)

1. Enter the following command.

```
aws configservice describe-conformance-pack-compliance --conformance-pack-name="`MyConformancePack1`"
```

2. You should see output similar to the following.

```
{
    "conformancePackName": "`MyConformancePack1`",
    "conformancePackRuleComplianceList": [
        {
            "configRuleName": "awsconfigconforms-`RuleName1`-`conformance-pack-ID`",
            "complianceType": "NON_COMPLIANT"
        },
        {
            "configRuleName": "awsconfigconforms-`RuleName2`-`conformance-pack-ID`",
            "complianceType": "COMPLIANT"
        }
    ]
}
```

Viewing the Compliance Details for your Conformance Packs (AWS CLI)

1. Enter the following command.

```
aws configservice get-conformance-pack-compliance-details --conformance-pack-name="`MyConformancePack1`"
```

2. You should see output similar to the following.

```
{
    "conformancePackRuleEvaluationResults": [
        {
            "evaluationResultIdentifier": {
                "orderingTimestamp": "Tue Jul 16 23:07:35 PDT 2019",
                "evaluationResultQualifier": {
                    "resourceId": "`resourceID`",
                    "configRuleName": "awsconfigconforms-`RuleName1`-`conformance-pack-ID`",
                    "resourceType": "AWS::::Account"
                }
            },
            "configRuleInvokedTime": "Tue Jul 16 23:07:50 PDT 2019",
            "resultRecordedTime": "Tue Jul 16 23:07:51 PDT 2019",
            "complianceType": "NON_COMPLIANT"
        },
        {
            "evaluationResultIdentifier": {
                "orderingTimestamp": "Thu Jun 27 15:16:36 PDT 2019",
                "evaluationResultQualifier": {
                    "resourceId": "`resourceID`",
                    "configRuleName": "awsconfigconforms-`RuleName2`-`conformance-pack-ID`",
                    "resourceType": "AWS::EC2::SecurityGroup"
                }
            },
           "configRuleInvokedTime": "Thu Jul 11 23:08:06 PDT 2019",
            "resultRecordedTime": "Thu Jul 11 23:08:06 PDT 2019",
            "complianceType": "COMPLIANT"
        }
    ],
    "conformancePackName": "`MyConformancePack1`"
}
}
```
