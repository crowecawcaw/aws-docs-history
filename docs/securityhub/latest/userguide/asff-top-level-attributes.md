# Optional top-level ASFF attributes

The following top-level attributes in the AWS Security Finding Format (ASFF) are optional for findings in Security Hub CSPM.
For more information about these attributes, see [AwsSecurityFinding](../../1.0/APIReference/API_AwsSecurityFinding.md "../../1.0/APIReference/API_AwsSecurityFinding.md") in the _AWS Security Hub API
Reference_.

## Action

The [`Action`](../../1.0/APIReference/API_Action.md "../../1.0/APIReference/API_Action.md") object provides details about an action that
affects or was taken on a resource.

**Example**

```
"Action": {
    "ActionType": "PORT_PROBE",
    "PortProbeAction": {
        "PortProbeDetails": [
            {
                "LocalPortDetails": {
                    "Port": 80,
                    "PortName": "HTTP"
                  },
                "LocalIpDetails": {
                     "IpAddressV4": "192.0.2.0"
                 },
                "RemoteIpDetails": {
                    "Country": {
                        "CountryName": "Example Country"
                    },
                    "City": {
                        "CityName": "Example City"
                    },
                   "GeoLocation": {
                       "Lon": 0,
                       "Lat": 0
                   },
                   "Organization": {
                       "AsnOrg": "ExampleASO",
                       "Org": "ExampleOrg",
                       "Isp": "ExampleISP",
                       "Asn": 64496
                   }
                }
            }
        ],
        "Blocked": false
    }
}
```

## AwsAccountName

The AWS account name that the finding applies to.

**Example**

```
"AwsAccountName": "jane-doe-testaccount"
```

## CompanyName

The name of the company for the product that generated the finding. For
control-based findings, the company is AWS.

Security Hub CSPM populates this attribute automatically for each finding. You cannot update
it using [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") or [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md"). The exception to this is
when you use a custom integration. See [Integrating Security Hub CSPM with custom products](securityhub-custom-providers.md "securityhub-custom-providers.md").

When you use the Security Hub CSPM console to filter findings by company name, you use this
attribute. When you use the Security Hub CSPM API to filter findings by company name, you use
the `aws/securityhub/CompanyName` attribute under
`ProductFields`. Security Hub CSPM does not synchronize those two
attributes.

**Example**

```
"CompanyName": "AWS"
```

## Compliance

The [`Compliance`](../../1.0/APIReference/API_Compliance.md "../../1.0/APIReference/API_Compliance.md") object typically provides details about a control
finding, such as applicable standards and the status of the control check.

**Example**

```
"Compliance": {
    "AssociatedStandards": [
        {"StandardsId": "standards/aws-foundational-security-best-practices/v/1.0.0"},
        {"StandardsId": "standards/service-managed-aws-control-tower/v/1.0.0"},
        {"StandardsId": "standards/nist-800-53/v/5.0.0"}
    ],
    "RelatedRequirements": [
        "NIST.800-53.r5 AC-4",
        "NIST.800-53.r5 AC-4(21)",
        "NIST.800-53.r5 SC-7",
        "NIST.800-53.r5 SC-7(11)",
        "NIST.800-53.r5 SC-7(16)",
        "NIST.800-53.r5 SC-7(21)",
        "NIST.800-53.r5 SC-7(4)",
        "NIST.800-53.r5 SC-7(5)"
    ],
    "SecurityControlId": "EC2.18",
    "SecurityControlParameters":[
        {
            "Name": "authorizedTcpPorts",
            "Value": ["80", "443"]
        },
        {
            "Name": "authorizedUdpPorts",
            "Value": ["427"]
        }
    ],
    "Status": "NOT_AVAILABLE",
    "StatusReasons": [
        {
            "ReasonCode": "CONFIG_RETURNS_NOT_APPLICABLE",
            "Description": "This finding has a compliance status of NOT AVAILABLE because AWS Config sent Security Hub CSPM a finding with a compliance state of Not Applicable. The potential reasons for a Not Applicable finding from Config are that (1) a resource has been moved out of scope of the Config rule; (2) the Config rule has been deleted; (3) the resource has been deleted; or (4) the logic of the Config rule itself includes scenarios where Not Applicable is returned. The specific reason why Not Applicable is returned is not available in the Config rule evaluation."
        }
    ]
}
```

## Confidence

The likelihood that a finding accurately identifies the behavior or issue that it
was intended to identify.

`Confidence` should only be updated using [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md").

Finding providers who want to provide a value for `Confidence` should
use the `Confidence` attribute under `FindingProviderFields`.
See [Updating findings with
FindingProviderFields](finding-update-batchimportfindings.md#batchimportfindings-findingproviderfields "finding-update-batchimportfindings.md#batchimportfindings-findingproviderfields").

`Confidence` is scored on a 0–100 basis using a ratio scale. 0
means 0 percent confidence, and 100 means 100 percent confidence. For example, a
data exfiltration detection based on a statistical deviation of network traffic has
low confidence because an actual exfiltration hasn't been verified.

**Example**

```
"Confidence": 42
```

## Criticality

The level of importance that is assigned to the resources that are associated with
a finding.

`Criticality` should only be updated by calling the [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md") API operation. Don't update this
object with [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md").

Finding providers who want to provide a value for `Criticality` should
use the `Criticality` attribute under `FindingProviderFields`.
See [Updating findings with
FindingProviderFields](finding-update-batchimportfindings.md#batchimportfindings-findingproviderfields "finding-update-batchimportfindings.md#batchimportfindings-findingproviderfields").

`Criticality` is scored on a 0–100 basis, using a ratio scale
that supports only full integers. A score of 0 means that the underlying resources
have no criticality, and a score of 100 is reserved for the most critical
resources.

For each resource, consider the following when assigning
`Criticality`:

- Does the affected resource contain sensitive data (for example, an S3
  bucket with PII)?
- Does the affected resource enable an adversary to deepen their access or
  extend their capabilities to carry out additional malicious activity (for
  example, a compromised sysadmin account)?
- Is the resource a business-critical asset (for example, a key business
  system that if compromised could have significant revenue impact)?

You can use the following guidelines:

- A resource powering mission-critical systems or containing highly
  sensitive data can be scored in the 75–100 range.
- A resource powering important (but not critical systems) or containing
  moderately important data can be scored in the 25–74 range.
- A resource powering unimportant systems or containing nonsensitive data
  should be scored in the 0–24 range.

**Example**

```
"Criticality": 99
```

## Detection

The `Detection` object provides details about an attack sequence finding from Amazon GuardDuty Extended Threat Detection.
GuardDuty generates an attack sequence finding when multiple
events align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you
must have GuardDuty enabled in your account. For more information, see [Amazon GuardDuty Extended Threat Detection](../../../guardduty/latest/ug/guardduty-extended-threat-detection.md "../../../guardduty/latest/ug/guardduty-extended-threat-detection.md")
in the _Amazon GuardDuty User Guide_.

**Example**

```
"Detection": {
    "Sequence": {
    	"Uid": "1111111111111-184ec3b9-cf8d-452d-9aad-f5bdb7afb010",
    	"Actors": [{
    		"Id": "USER:AROA987654321EXAMPLE:i-b188560f:1234567891",
    		"Session": {
    			"Uid": "1234567891",
    			"MfAStatus": "DISABLED",
    			"CreatedTime": "1716916944000",
    			"Issuer": "arn:aws:s3:::amzn-s3-demo-destination-bucket"
    		},
    		"User": {
    			"CredentialUid": "ASIAIOSFODNN7EXAMPLE",
    			"Name": "ec2_instance_role_production",
    			"Type": "AssumedRole",
    			"Uid": "AROA987654321EXAMPLE:i-b188560f",
    			"Account": {
    				"Uid": "AccountId",
    				"Name": "AccountName"
    			}
    		}
    	}],
    	"Endpoints": [{
    		"Id": "EndpointId",
    		"Ip": "203.0.113.1",
    		"Domain": "example.com",
    		"Port": 4040,
    		"Location": {
    			"City": "New York",
    			"Country": "US",
    			"Lat": 40.7123,
    			"Lon": -74.0068
    		},
    		"AutonomousSystem": {
    			"Name": "AnyCompany",
    			"Number": 64496
    		},
    		"Connection": {
    			"Direction": "INBOUND"
    		}
    	}],
    	"Signals": [{
    		"Id": "arn:aws:guardduty:us-east-1:123456789012:detector/d0bfe135ab8b4dd8c3eaae7df9900073/finding/535a382b1bcc44d6b219517a29058fb7",
    		"Title": "Someone ran a penetration test tool on your account.",
    		"ActorIds": ["USER:AROA987654321EXAMPLE:i-b188560f:1234567891"],
    		"Count": 19,
    		"FirstSeenAt": 1716916943000,
    		"SignalIndicators": [
    			{
    				"Key": "ATTACK_TACTIC",
    				"Title": "Attack Tactic",
    				"Values": [
    					"Impact"
    				]
    			},
    			{
    				"Key": "HIGH_RISK_API",
    				"Title": "High Risk Api",
    				"Values": [
    					"s3:DeleteObject"
    				]
    			},
    			{
    				"Key": "ATTACK_TECHNIQUE",
    				"Title": "Attack Technique",
    				"Values": [
    					"Data Destruction"
    				]
    			},
    		],
    		"LastSeenAt": 1716916944000,
    		"Name": "Test:IAMUser/KaliLinux",
    		"ResourceIds": [
    			"arn:aws:s3:::amzn-s3-demo-destination-bucket"
    		],
    		"Type": "FINDING"
    	}],
    	"SequenceIndicators": [
    		{
    			"Key": "ATTACK_TACTIC",
    			"Title": "Attack Tactic",
    			"Values": [
    				"Discovery",
    				"Exfiltration",
    				"Impact"
    			]
    		},
    		{
    			"Key": "HIGH_RISK_API",
    			"Title": "High Risk Api",
    			"Values": [
    				"s3:DeleteObject",
    				"s3:GetObject",
    				"s3:ListBuckets"
    				"s3:ListObjects"
    			]
    		},
    		{
    			"Key": "ATTACK_TECHNIQUE",
    			"Title": "Attack Technique",
    			"Values": [
    				"Cloud Service Discovery",
    				"Data Destruction"
    			]
    		}
    	]
    }
}
```

## FindingProviderFields

`FindingProviderFields` includes the following attributes:

- `Confidence`
- `Criticality`
- `RelatedFindings`
- `Severity`
- `Types`

The preceding fields are nested under the `FindingProviderFields` object, but have analogues of the same name
as top-level ASFF fields. When a new finding is sent to Security Hub CSPM by a finding provider, Security Hub CSPM populates the
`FindingProviderFields` object automatically if it is empty based on the corresponding top-level fields.

Finding providers can update `FindingProviderFields` by using the[`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") operation of the Security Hub CSPM API. Finding providers cannot update
this object with [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md").

For details on how Security Hub CSPM handles updates from `BatchImportFindings` to
`FindingProviderFields` and to the corresponding top-level
attributes, see [Updating findings with
FindingProviderFields](finding-update-batchimportfindings.md#batchimportfindings-findingproviderfields "finding-update-batchimportfindings.md#batchimportfindings-findingproviderfields").

Customers can update the top-level fields by using the `BatchUpdateFindings` operation. Customers can't
update `FindingProviderFields`.

**Example**

```
"FindingProviderFields": {
    "Confidence": 42,
    "Criticality": 99,
    "RelatedFindings":[
      {
        "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/guardduty",
        "Id": "123e4567-e89b-12d3-a456-426655440000"
      }
    ],
    "Severity": {
        "Label": "MEDIUM",
        "Original": "MEDIUM"
    },
    "Types": [ "Software and Configuration Checks/Vulnerabilities/CVE" ]
}
```

## FirstObservedAt

Indicates when the potential security issue or event captured by a finding was
first observed.

This timestamp specifies when the event or vulnerability was first observed.
Consequently, it can differ from the `CreatedAt` timestamp, which reflects
when this finding record was created.

For control findings that Security Hub CSPM generates and updates, this timestamp can also
indicate when the compliance status of a resource most recently changed. For other types
of findings, this timestamp should be immutable between updates of the finding record,
but can be updated if a more accurate timestamp is determined.

**Example**

```
"FirstObservedAt": "2017-03-22T13:22:13.933Z"
```

## LastObservedAt

Indicates when the potential security issue or event captured by a finding was most
recently observed by the security findings product.

This timestamp specifies when the event or vulnerability was last or most recently
observed. Consequently, it can differ from the `UpdatedAt` timestamp, which
reflects when this finding record was last or most recently updated.

You can provide this timestamp, but it isn't required upon first observation. If you
populate this field upon first observation, the timestamp should be the same as the
`FirstObservedAt` timestamp. You should update this field to reflect the
last or most recently observed timestamp each time a finding is observed.

**Example**

```
"LastObservedAt": "2017-03-23T13:22:13.933Z"
```

## Malware

The [`Malware`](../../1.0/APIReference/API_Malware.md "../../1.0/APIReference/API_Malware.md")
object provides a list of malware related to a finding.

**Example**

```
"Malware": [
    {
        "Name": "Stringler",
        "Type": "COIN_MINER",
        "Path": "/usr/sbin/stringler",
        "State": "OBSERVED"
    }
]
```

## Network (Retired)

The [`Network`](../../1.0/APIReference/API_Network.md "../../1.0/APIReference/API_Network.md")
object provides network-related information about a finding.

This object is retired. To provide this data, you can either map the data to a
resource in `Resources`, or use the `Action` object.

**Example**

```
"Network": {
    "Direction": "IN",
    "OpenPortRange": {
        "Begin": 443,
        "End": 443
    },
    "Protocol": "TCP",
    "SourceIpV4": "1.2.3.4",
    "SourceIpV6": "FE80:CD00:0000:0CDE:1257:0000:211E:729C",
    "SourcePort": "42",
    "SourceDomain": "example1.com",
    "SourceMac": "00:0d:83:b1:c0:8e",
    "DestinationIpV4": "2.3.4.5",
    "DestinationIpV6": "FE80:CD00:0000:0CDE:1257:0000:211E:729C",
    "DestinationPort": "80",
    "DestinationDomain": "example2.com"
}
```

## NetworkPath

The [`NetworkPath`](../../1.0/APIReference/API_NetworkPathComponent.md "../../1.0/APIReference/API_NetworkPathComponent.md") object provides information about a
network path that is related to a finding. Each entry in `NetworkPath`
represents a component of the path.

**Example**

```
"NetworkPath" : [
    {
        "ComponentId": "abc-01a234bc56d8901ee",
        "ComponentType": "AWS::EC2::InternetGateway",
        "Egress": {
            "Destination": {
                "Address": [ "192.0.2.0/24" ],
                "PortRanges": [
                    {
                        "Begin": 443,
                        "End": 443
                    }
                ]
            },
            "Protocol": "TCP",
            "Source": {
                "Address": ["203.0.113.0/24"]
            }
        },
        "Ingress": {
            "Destination": {
                "Address": [ "198.51.100.0/24" ],
                "PortRanges": [
                    {
                        "Begin": 443,
                        "End": 443
                    }
                 ]
            },
            "Protocol": "TCP",
            "Source": {
                "Address": [ "203.0.113.0/24" ]
            }
        }
     }
]

```

## Note

The [`Note`](../../1.0/APIReference/API_Note.md "../../1.0/APIReference/API_Note.md") object specifies a user-defined note that you can
add to a finding.

A finding provider can provide an initial note for a finding, but cannot add notes
after that. You can only update a note using [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md").

**Example**

```
"Note": {
    "Text": "Don't forget to check under the mat.",
    "UpdatedBy": "jsmith",
    "UpdatedAt": "2018-08-31T00:15:09Z"
}
```

## PatchSummary

The [`PatchSummary`](../../1.0/APIReference/API_PatchSummary.md "../../1.0/APIReference/API_PatchSummary.md") object provides a summary of the patch
compliance status for an instance against a selected compliance standard.

**Example**

```
"PatchSummary" : {
    "FailedCount" : 0,
    "Id" : "pb-123456789098",
    "InstalledCount" : 100,
    "InstalledOtherCount" : 1023,
    "InstalledPendingReboot" : 0,
    "InstalledRejectedCount" : 0,
    "MissingCount" : 100,
    "Operation" : "Install",
    "OperationEndTime" : "2018-09-27T23:39:31Z",
    "OperationStartTime" : "2018-09-27T23:37:31Z",
    "RebootOption" : "RebootIfNeeded"
}
```

## Process

The [`Process`](../../1.0/APIReference/API_ProcessDetails.md "../../1.0/APIReference/API_ProcessDetails.md") object provides process-related details about a
finding.

Example:

```
"Process": {
    "LaunchedAt": "2018-09-27T22:37:31Z",
    "Name": "syslogd",
    "ParentPid": 56789,
    "Path": "/usr/sbin/syslogd",
    "Pid": 12345,
    "TerminatedAt": "2018-09-27T23:37:31Z"
}
```

## ProcessedAt

Indicates when Security Hub CSPM received a finding and began to process it.

This differs from `CreatedAt` and `UpdatedAt`, which are
required timestamps that relate to the finding provider's interaction with the security
issue and finding. The `ProcessedAt` timestamp indicates when Security Hub CSPM starts to
process a finding. A finding appears in a user's account after processing is
complete.

```
"ProcessedAt": "2023-03-23T13:22:13.933Z"
```

## ProductFields

A data type where security findings products can include additional
solution-specific details that are not part of the defined AWS Security Finding Format.

For findings generated by Security Hub CSPM controls, `ProductFields` includes
information about the control. See [Generating and updating control findings](controls-findings-create-update.md "controls-findings-create-update.md").

This field should not contain redundant data and must not contain data that
conflicts with AWS Security Finding Format fields.

The "`aws/`" prefix represents a reserved namespace for AWS products
and services only and must not be submitted with findings from third-party
integrations.

Although not required, products should format field names as
`company-id/product-id/field-name`, where the
`company-id` and `product-id` match those supplied
in the `ProductArn` of the finding.

The fields referencing `Archival` are used when Security Hub CSPM archives an existing finding. For example,
Security Hub CSPM archives existing findings when you disable a control or standard and when you turn [consolidated control findings](controls-findings-create-update.md#consolidated-control-findings "controls-findings-create-update.md#consolidated-control-findings")
on or off.

This field may also include information about the standard that includes the control that
produced the finding.

**Example**

```
"ProductFields": {
    "API", "DeleteTrail",
    "ArchivalReasons:0/Description": "The finding is in an `ARCHIVED` state because consolidated control findings has been turned on or off. This causes findings in the previous state to be archived when new findings are being generated.",
    "ArchivalReasons:0/ReasonCode": "CONSOLIDATED_CONTROL_FINDINGS_UPDATE",
    "aws/inspector/AssessmentTargetName": "My prod env",
    "aws/inspector/AssessmentTemplateName": "My daily CVE assessment",
    "aws/inspector/RulesPackageName": "Common Vulnerabilities and Exposures",
    "generico/secure-pro/Action.Type", "AWS_API_CALL",
    "generico/secure-pro/Count": "6",
    "Service_Name": "cloudtrail.amazonaws.com"
}
```

## ProductName

Provides the name of the product that generated the finding. For control-based
findings, the product name is Security Hub CSPM.

Security Hub CSPM populates this attribute automatically for each finding. You cannot update
it using [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") or [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md"). The exception to this is when you
use a custom integration. See [Integrating Security Hub CSPM with custom products](securityhub-custom-providers.md "securityhub-custom-providers.md").

When you use the Security Hub CSPM console to filter findings by product name, you use this
attribute.

When you use the Security Hub CSPM API to filter findings by product name, you use the
`aws/securityhub/ProductName` attribute under
`ProductFields`.

Security Hub CSPM does not synchronize those two attributes.

## RecordState

Provides the record state of a finding.

By default, when initially generated by a service, findings are considered
`ACTIVE`.

The `ARCHIVED` state indicates that a finding should be hidden from
view. Archived findings are not deleted immediately. You can search, review, and report
on them. Security Hub CSPM automatically archives control-based findings if the associated resource
is deleted, the resource does not exist, or the control is disabled.

`RecordState` is intended for finding providers, and can be updated
only by using the [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") operation. You cannot update it by
using the [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md") operation.

To track the status of your investigation into a finding, use [Workflow](#asff-workflow "#asff-workflow") instead of
`RecordState`.

If the record state changes from `ARCHIVED` to `ACTIVE`, and
the workflow status of the finding is `NOTIFIED` or `RESOLVED`,
Security Hub CSPM automatically changes the workflow status to `NEW`.

**Example**

```
"RecordState": "ACTIVE"
```

## Region

Specifies the AWS Region from which the finding was generated.

Security Hub CSPM populates this attribute automatically for each finding. You cannot update
it using [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") or [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md").

**Example**

```
"Region": "us-west-2"
```

## RelatedFindings

Provides a list of findings that are related to the current finding.

`RelatedFindings` should only be updated with the [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md") API operation. You should not
update this object with [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md").

For [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") requests, finding providers should
use the `RelatedFindings` object under [FindingProviderFields](#asff-findingproviderfields "#asff-findingproviderfields").

To view descriptions of `RelatedFindings` attributes, see [`RelatedFinding`](../../1.0/APIReference/API_RelatedFinding.md "../../1.0/APIReference/API_RelatedFinding.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"RelatedFindings": [
    { "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/guardduty",
      "Id": "123e4567-e89b-12d3-a456-426655440000" },
    { "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/guardduty",
      "Id": "AcmeNerfHerder-111111111111-x189dx7824" }
]
```

## RiskAssessment

**Example**

```
"RiskAssessment": {
    "Posture": {
        "FindingTotal": 4,
        "Indicators": [
            {
                "Type": "Reachability",
                "Findings": [
                    {
                        "Id": "arn:aws:inspector2:us-east-2:123456789012:finding/1234567890abcdef0",
                        "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/inspector",
                        "Title": "Finding title"
                    },
                    {
                        "Id": "arn:aws:inspector2:us-east-2:123456789012:finding/abcdef01234567890",
                        "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/inspector",
                        "Title": "Finding title"
                    }
                ]
            },
            {
                "Type": "Vulnerability",
                "Findings": [
                    {
                        "Id": "arn:aws:inspector2:us-east-2:123456789012:finding/021345abcdef6789",
                        "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/inspector",
                        "Title": "Finding title"
                    },
                    {
                        "Id": "arn:aws:inspector2:us-east-2:123456789012:finding/021345ghijkl6789",
                        "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/inspector",
                        "Title": "Finding title"
                    }
                ]
            }
        ]
    }
}
```

## Remediation

The [`Remediation`](../../1.0/APIReference/API_Remediation.md "../../1.0/APIReference/API_Remediation.md") object provides information about recommended
remediation steps to address the finding.

**Example**

```
"Remediation": {
    "Recommendation": {
        "Text": "For instructions on how to fix this issue, see the AWS Security Hub CSPM documentation for EC2.2.",
        "Url": "https://docs.aws.amazon.com/console/securityhub/EC2.2/remediation"
    }
}
```

## Sample

Specifies whether the finding is a sample finding.

```
"Sample": true
```

## SourceUrl

The `SourceUrl` object provides a URL that links to a page about the
current finding in the finding product.

```
"SourceUrl": "http://sourceurl.com"
```

## ThreatIntelIndicators

The [`ThreatIntelIndicator`](../../1.0/APIReference/API_ThreatIntelIndicator.md "../../1.0/APIReference/API_ThreatIntelIndicator.md") object provides threat
intelligence details that are related to a finding.

**Example**

```
"ThreatIntelIndicators": [
  {
    "Category": "BACKDOOR",
    "LastObservedAt": "2018-09-27T23:37:31Z",
    "Source": "Threat Intel Weekly",
    "SourceUrl": "http://threatintelweekly.org/backdoors/8888",
    "Type": "IPV4_ADDRESS",
    "Value": "8.8.8.8",
  }
]
```

## Threats

The [Threats](../../1.0/APIReference/API_Threat.md "../../1.0/APIReference/API_Threat.md") object provides details about the threat
detected by a finding.

**Example**

```
"Threats": [{
    "FilePaths": [{
        "FileName": "b.txt",
        "FilePath": "/tmp/b.txt",
        "Hash": "sha256",
        "ResourceId": "arn:aws:ec2:us-west-2:123456789012:volume/vol-032f3bdd89aee112f"
    }],
    "ItemCount": 3,
    "Name": "Iot.linux.mirai.vwisi",
    "Severity": "HIGH"
}]
```

## UserDefinedFields

Provides a list of name-value string pairs that are associated with the finding.
These are custom, user-defined fields that are added to a finding. These fields can
be generated automatically through your specific configuration.

Finding providers should not use this field for data that the product generates.
Instead, finding providers can use the `ProductFields` field for data
that does not map to any standard AWS Security Finding Format field.

These fields can only be updated using [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md").

**Example**

```
"UserDefinedFields": {
    "reviewedByCio": "true",
    "comeBackToLater": "Check this again on Monday"
}
```

## VerificationState

Provides the veracity of a finding. Findings products can provide a value of
`UNKNOWN` for this field. A findings product should provide a value
for this field if there is a meaningful analog in the findings product's system.
This field is typically populated by a user determination or action after
investigating a finding.

A finding provider can provide an initial value for this attribute, but cannot
update it after that. You can only update this attribute by using [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md").

```
"VerificationState": "Confirmed"
```

## Vulnerabilities

The [Vulnerabilities](../../1.0/APIReference/API_Vulnerability.md "../../1.0/APIReference/API_Vulnerability.md") object provides a list of
vulnerabilities that are associated with a finding.

**Example**

```
"Vulnerabilities" : [
    {
        "CodeVulnerabilities": [{
            "Cwes": [
                "CWE-798",
                "CWE-799"
            ],
            "FilePath": {
                "EndLine": 421,
                "FileName": "package-lock.json",
                "FilePath": "package-lock.json",
                "StartLine": 420
            },
                "SourceArn":"arn:aws:lambda:us-east-1:123456789012:layer:AWS-AppConfig-Extension:114"
        }],
        "Cvss": [
            {
                "BaseScore": 4.7,
                "BaseVector": "AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N",
                "Version": "V3"
            },
            {
                "BaseScore": 4.7,
                "BaseVector": "AV:L/AC:M/Au:N/C:C/I:N/A:N",
                "Version": "V2"
            }
        ],
        "EpssScore": 0.015,
        "ExploitAvailable": "YES",
        "FixAvailable": "YES",
        "Id": "CVE-2020-12345",
        "LastKnownExploitAt": "2020-01-16T00:01:35Z",
        "ReferenceUrls":[
           "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-12418",
            "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17563"
        ],
        "RelatedVulnerabilities": ["CVE-2020-12345"],
        "Vendor": {
            "Name": "Alas",
            "Url":"https://alas.aws.amazon.com/ALAS-2020-1337.html",
            "VendorCreatedAt":"2020-01-16T00:01:43Z",
            "VendorSeverity":"Medium",
            "VendorUpdatedAt":"2020-01-16T00:01:43Z"
        },
        "VulnerablePackages": [
            {
                "Architecture": "x86_64",
                "Epoch": "1",
                "FilePath": "/tmp",
                "FixedInVersion": "0.14.0",
                "Name": "openssl",
                "PackageManager": "OS",
                "Release": "16.amzn2.0.3",
                "Remediation": "Update aws-crt to 0.14.0",
                "SourceLayerArn": "arn:aws:lambda:us-west-2:123456789012:layer:id",
                "SourceLayerHash": "sha256:c1962c35b63a6ff6ce7df6e042ee82371a605ca9515569edec46ff14f926f001",
                "Version": "1.0.2k"
            }
        ]
    }
]
```

## Workflow

The [`Workflow`](../../1.0/APIReference/API_Workflow.md "../../1.0/APIReference/API_Workflow.md") object provides information about the status of
the investigation into a finding.

This field is intended for customers to use with remediation, orchestration, and
ticketing tools. It is not intended for finding providers.

You can only update the `Workflow` field with [`BatchUpdateFindings`](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md"). Customers can also update it from
the console. See [Setting the workflow status of findings in
Security Hub CSPM](findings-workflow-status.md "findings-workflow-status.md").

**Example**

```
"Workflow": {
    "Status": "NEW"
}
```

## WorkflowState (Retired)

This object is retired and has been replaced by the `Status` field of
the `Workflow` object.

This field provides the workflow state of a finding. Findings products can provide
the value of `NEW` for this field. A findings product can provide a value
for this field if there is a meaningful analog in the findings product's
system.

**Example**

```
"WorkflowState": "NEW"
```
