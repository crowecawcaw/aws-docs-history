# Examples of automation rules

This section provides examples of automation rules for common Security Hub CSPM use cases. These
examples correspond to rule templates that are available on the Security Hub CSPM console.

## Elevate severity to

Critical when specific resource such as an S3 bucket is at risk

In this example, the rule criteria are matched when the `ResourceId` in
a finding is a specific Amazon Simple Storage Service (Amazon S3) bucket. The rule action is to change the
severity of matched findings to `CRITICAL`. You can modify this template
to apply to other resources.

**Example API request**:

```
{
    "IsTerminal": `true`,
    "RuleName": "`Elevate severity of findings that relate to important resources`",
    "RuleOrder": `1`,
    "RuleStatus": "`ENABLED`",
    "Description": "`Elevate finding severity to `CRITICAL` when specific resource such as an S3 bucket is at risk`",
    "Criteria": {
        "ProductName": [{
            "Value": "`Security Hub CSPM`",
            "Comparison": "`EQUALS`"
        }],
        "ComplianceStatus": [{
            "Value": "`FAILED`",
            "Comparison": "`EQUALS`"
        }],
        "RecordState": [{
            "Value": "`ACTIVE`",
            "Comparison": "`EQUALS`"
        }],
        "WorkflowStatus": [{
            "Value": "`NEW`",
            "Comparison": "`EQUALS`"
        }],
        "ResourceId": [{
            "Value": "arn:aws:`s3:::amzn-s3-demo-bucket/developers/design_info.doc`",
            "Comparison": "`EQUALS`"
        }]
    },
    "Actions": [{
        "Type": "FINDING_FIELDS_UPDATE",
        "FindingFieldsUpdate": {
            "Severity": {
                "Label": "`CRITICAL`"
            },
            "Note": {
                "Text": "`This is a critical resource. Please review ASAP.`",
                "UpdatedBy": "`sechub-automation`"
            }
        }
    }]
}
```

**Example CLI command:**

```
`$`
`aws securityhub create-automation-rule \
--is-terminal \
--rule-name "`Elevate severity of findings that relate to important resources`" \
--rule-order `1` \
--rule-status "`ENABLED`" \

--description "`Elevate finding severity to `CRITICAL` when specific resource such as an S3 bucket is at risk`"` \
--criteria '{
"ProductName": [{
"Value": "`Security Hub CSPM`",
"Comparison": `"`EQUALS`"
}],
"ComplianceStatus": [{
"Value": "`FAILED`",
"Comparison": "`EQUALS`"
}],
"RecordState": [{
"Value": "`ACTIVE`",
"Comparison": "`EQUALS`"
}],
"WorkflowStatus": [{
"Value": "`NEW`",
"Comparison": "`EQUALS`"
}],
"ResourceId": [{
"Value": "`arn:aws:s3:::amzn-s3-demo-bucket/developers/design_info.doc"`,
"Comparison": "`EQUALS`"
}]
}' \
--actions '[{
"Type": "FINDING_FIELDS_UPDATE",
"FindingFieldsUpdate": {
"Severity": {
"Label": "`CRITICAL`"
},
"Note": {
"Text": "`This is a critical resource. Please review ASAP.`",
"UpdatedBy": "`sechub-automation`"
}
}
}]' \
--region `us-east-1``
```

## Elevate severity of

findings that relate to resources in production accounts

In this example, the rule criteria are matched when a `HIGH` severity
finding is generated in specific production accounts. The rule action is to change
the severity of matched findings to `CRITICAL`.

**Example API request**:

```
{
    "IsTerminal": `false`,
    "RuleName": "`Elevate severity for production accounts`",
    "RuleOrder": `1`,
    "RuleStatus": "`ENABLED`",
    "Description": "`Elevate finding severity from `HIGH` to `CRITICAL` for findings that relate to resources in specific production accounts`",
    "Criteria": {
        "ProductName": [{
            "Value": "`Security Hub CSPM`",
            "Comparison": "`EQUALS`"
        }],
        "ComplianceStatus": [{
            "Value": "`FAILED`",
            "Comparison": "`EQUALS`"
        }],
        "RecordState": [{
            "Value": "`ACTIVE`",
            "Comparison": "`EQUALS`"
        }],
        "WorkflowStatus": [{
            "Value": "`NEW`",
            "Comparison": "`EQUALS`"
        }],
        "SeverityLabel": [{
            "Value": "`HIGH`",
            "Comparison": "`EQUALS`"
        }],
        "AwsAccountId": [
        {
            "Value": "`111122223333`",
            "Comparison": "`EQUALS`"
        },
        {
            "Value": "`123456789012`",
            "Comparison": "`EQUALS`"
        }]
    },
    "Actions": [{
        "Type": "FINDING_FIELDS_UPDATE",
        "FindingFieldsUpdate": {
            "Severity": {
                "Label": "`CRITICAL`"
            },
            "Note": {
                "Text": "`A resource in production accounts is at risk. Please review ASAP.`",
                "UpdatedBy": "`sechub-automation`"
            }
        }
    }]
}
```

**Example CLI command**:

```

aws securityhub create-automation-rule \
--no-is-terminal \
--rule-name `"`Elevate severity of findings that relate to resources in production accounts`"` \
--rule-order ``1`` \
--rule-status `"`ENABLED`"` \
--description `"`Elevate finding severity from `HIGH` to `CRITICAL` for findings that relate to resources in specific production accounts`"` \
--criteria '{
"ProductName": [{
"Value": `"`Security Hub CSPM`"`,
"Comparison": `"`EQUALS`"`
}],
"ComplianceStatus": [{
"Value": `"`FAILED`"`,
"Comparison": `"`EQUALS`"`
}],
"RecordState": [{
"Value": `"`ACTIVE`"`,
"Comparison": `"`EQUALS`"`
}],
"SeverityLabel": [{
"Value": `"`HIGH`"`,
"Comparison": `"`EQUALS`"`
}],
"AwsAccountId": [
{
"Value": `"`111122223333`"`,
"Comparison": `"`EQUALS`"`
},
{
"Value": `"`123456789012`"`,
"Comparison": `"`EQUALS`"`
}]
}' \
--actions '[{
"Type": `"FINDING_FIELDS_UPDATE"`,
"FindingFieldsUpdate": {
"Severity": {
"Label": `"`CRITICAL`"`
},
"Note": {
"Text": `"`A resource in production accounts is at risk. Please review ASAP.`"`,
"UpdatedBy": `"`sechub-automation`"`
}
}
}]' \
--region ``us-east-1``
```

## Suppress informational

findings

In this example, the rule criteria are matched for `INFORMATIONAL`
severity findings sent to Security Hub CSPM from Amazon GuardDuty. The rule action is to change the
workflow status of matched findings to `SUPPRESSED`.

**Example API request**:

```
{
    "IsTerminal": `false`,
    "RuleName": "`Suppress informational findings`",
    "RuleOrder": `1`,
    "RuleStatus": "`ENABLED`",
    "Description": "`Suppress GuardDuty findings with `INFORMATIONAL` severity`",
    "Criteria": {
        "ProductName": [{
            "Value": "`GuardDuty`",
            "Comparison": "`EQUALS`"
        }],
        "RecordState": [{
            "Value": "`ACTIVE`",
            "Comparison": "`EQUALS`"
        }],
        "WorkflowStatus": [{
            "Value": "`NEW`",
            "Comparison": "`EQUALS`"
        }],
        "SeverityLabel": [{
            "Value": "`INFORMATIONAL`",
            "Comparison": "`EQUALS`"
        }]
    },
    "Actions": [{
        "Type": "FINDING_FIELDS_UPDATE",
        "FindingFieldsUpdate": {
            "Workflow": {
                "Status": "`SUPPRESSED`"
            },
            "Note": {
                "Text": "`Automatically suppress GuardDuty findings with `INFORMATIONAL` severity`",
                "UpdatedBy": "`sechub-automation`"
            }
        }
    }]
}
```

**Example CLI command**:

```

aws securityhub create-automation-rule \
--no-is-terminal \
--rule-name `"`Suppress informational findings`"` \
--rule-order ``1`` \
--rule-status `"`ENABLED`"` \
--description `"`Suppress GuardDuty findings with `INFORMATIONAL` severity`"` \
--criteria '{
"ProductName": [{
"Value": `"`GuardDuty`"`,
"Comparison": `"`EQUALS`"`
}],
"ComplianceStatus": [{
"Value": `"`FAILED`"`,
"Comparison": `"`EQUALS`"`
}],
"RecordState": [{
"Value": `"`ACTIVE`"`,
"Comparison": `"`EQUALS`"`
}],
"WorkflowStatus": [{
"Value": `"`NEW`"`,
"Comparison": `"`EQUALS`"`
}],
"SeverityLabel": [{
"Value": `"`INFORMATIONAL`"`,
"Comparison": `"`EQUALS`"`
}]
}' \
--actions '[{
"Type": `"FINDING_FIELDS_UPDATE"`,
"FindingFieldsUpdate": {
"Workflow": {
"Status": `"`SUPPRESSED`"`
},
"Note": {
"Text": `"`Automatically suppress GuardDuty findings with `INFORMATIONAL` severity`"`,
"UpdatedBy": `"`sechub-automation`"`
}
}
}]' \
--region ``us-east-1``

```
