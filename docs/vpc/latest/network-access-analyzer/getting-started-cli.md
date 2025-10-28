# Getting started with Network Access Analyzer using the AWS CLI

The following procedure describes how to get started with Network Access Analyzer using the AWS CLI.

###### Tasks

- [Step 1: Create a Network Access Scope](#create-access-scope-cli "#create-access-scope-cli")
- [Step 2: Analyze a Network Access Scope](#analyze-access-scope-cli "#analyze-access-scope-cli")
- [Step 3: Get the results of a Network Access Scope analysis](#view-results-cli "#view-results-cli")

## Step 1: Create a Network Access Scope

Use the following [create-network-insights-access-scope](../../../cli/latest/reference/ec2/create-network-insights-access-scope.md "../../../cli/latest/reference/ec2/create-network-insights-access-scope.md") command to create a Network Access Scope.

```
aws ec2 create-network-insights-access-scope
# optional/example input
--match-paths "Source={ResourceStatement={Resources=vpc-abcd12e3}}" "Destination={ResourceStatement={ResourceTypes=["AWS::EC2::InternetGateway"]}}"
# optional/example input
--exclude-paths "Source={ResourceStatement={ResourceTypes=["AWS::EC2::InternetGateway"]}}"
```

The following is example output.

```
{
    "NetworkInsightsAccessScope": {
        "NetworkInsightsAccessScopeId": "nis-0b1889d01c2801311",
        "NetworkInsightsAccessScopeArn": "arn:aws:ec2:us-east-1:470889052923:network-insights-access-scope/nis-0b1889d01c2801311",
        "CreatedDate": "2024-10-01T13:35:01.017000+00:00",
        "UpdatedDate": "2024-10-01T13:35:01.017000+00:00"
    },
    "NetworkInsightsAccessScopeContent": {
        "NetworkInsightsAccessScopeId": "nis-0b1889d01c2801311",
        "MatchPaths": [
            {
                "Source": {
                    "ResourceStatement": {
                        "Resources": [
                            "vpc-abcd12e3"
                        ]
                    }
                }
            },
            {
                "Destination": {
                    "ResourceStatement": {
                        "ResourceTypes": [
                            "AWS::EC2::InternetGateway"
                        ]
                    }
                }
            }
        ],
        "ExcludePaths": [
            {
                "Source": {
                    "ResourceStatement": {
                        "ResourceTypes": [
                            "AWS::EC2::InternetGateway"
                        ]
                    }
                }
            }
        ]
    }
}
```

You can also create a scope using the CLI JSON input option, as shown in the following
example.

```
aws ec2 create-network-insights-access-scope --cli-input-json file://path-to-access-scope-file.json
```

The following is an example input file.

```
{
     "MatchPaths": [
          {
               "Source": {
                    "ResourceStatement": {
                         "Resources": [
                              "vpc-abcd12e3"
                         ]
                    }
               }
          }
     ],
     "ExcludePaths": [
          {
               "Source": {
                    "ResourceStatement": {
                         "ResourceTypes": [
                              "AWS::EC2::InternetGateway"
                         ]
                    }
               }
          }
     ]
}
```

See [Generating an AWS CLI skeleton and input file](../../../cli/latest/userguide/cli-usage-skeleton.md "../../../cli/latest/userguide/cli-usage-skeleton.md") for more details about using
the CLI with JSON input.

Use the following [describe-network-insights-access-scopes](../../../cli/latest/reference/ec2/describe-network-insights-access-scopes.md "../../../cli/latest/reference/ec2/describe-network-insights-access-scopes.md") command to describe a Network Access Scope.

```
aws ec2 describe-network-insights-access-scopes
```

Use the following [get-network-insights-access-scope-content](../../../cli/latest/reference/ec2/get-network-insights-access-scope-content.md "../../../cli/latest/reference/ec2/get-network-insights-access-scope-content.md") command to get a Network Access Scope.

```
aws ec2 get-network-insights-access-scope-content --network-insights-access-scope-id nis-0e123eecc45c67d8
```

Use the following [delete-network-insights-access-scope](../../../cli/latest/reference/ec2/delete-network-insights-access-scope.md "../../../cli/latest/reference/ec2/delete-network-insights-access-scope.md") command to delete a Network Access Scope.

```
aws ec2 delete-network-insights-access-scope --network-insights-access-scope-id nis-0e123eecc45c67d8
```

## Step 2: Analyze a Network Access Scope

Use the following [start-network-insights-access-scope-analysis](../../../cli/latest/reference/ec2/start-network-insights-access-scope-analysis.md "../../../cli/latest/reference/ec2/start-network-insights-access-scope-analysis.md") command to analyze a Network Access
Scope. The analysis can take a few minutes to complete.

```
aws ec2 start-network-insights-access-scope-analysis --network-insights-access-scope-id nis-0e123eecc45c67d8
```

The following is example output.

```
{
    "NetworkInsightsAccessScopeAnalysis": {
        "NetworkInsightsAccessScopeAnalysisId": "nisa-0e123eecc45c67d89",
        "NetworkInsightsAccessScopeAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-access-scope-analysis/nisa-0e123eecc45c67d89",
        "NetworkInsightsAccessScopeId": "nis-0e123eecc45c67d8",
        "Status": "running",
        "StartDate": "2021-11-08T19:29:30.179000+00:00"
    }
}
```

## Step 3: Get the results of a Network Access Scope analysis

After the analysis completes, you can view the results
using the [describe-network-insights-access-scope-analyses](../../../cli/latest/reference/ec2/describe-network-insights-access-scope-analyses.md "../../../cli/latest/reference/ec2/describe-network-insights-access-scope-analyses.md") command.

```
aws ec2 describe-network-insights-access-scope-analyses
```

###### Example 1: Success

The following is example output for a successful analysis.

```
{
    "NetworkInsightsAccessScopeAnalyses": [
        {
            "NetworkInsightsAccessScopeAnalysisId": "nisa-09aeb24f525f2d9f7",
            "NetworkInsightsAccessScopeAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-access-scope-analysis/nisa-09aeb24f525f2d9f7",
            "NetworkInsightsAccessScopeId": "nis-0af1fcfd38e5cad4e",
            "Status": "succeeded",
            "StartDate": "2021-11-08T19:29:30.179000+00:00",
            "FindingsFound": "true",
            "Tags": []
        }
    ]
}
```

###### Example 2: No findings

The following is example output when no network paths are found in the
analysis.

```
aws ec2 get-network-insights-access-scope-analysis-findings --network-insights-access-scope-analysis-id nisa-07bcaad8bd8160e63
{
    "NetworkInsightsAccessScopeAnalysisId": "nisa-09aeb24f525f2d9f7",
    "AnalysisFindings": []
}
```

###### Example 3: Findings reported

The following is example output where findings were reported in the
analysis.

```
aws ec2 describe-network-insights-access-scope-analyses --network-insights-access-scope-analysis-id nisa-0c0d3ec68a9bb2f22
{
    "NetworkInsightsAccessScopeAnalyses": [
        {
            "NetworkInsightsAccessScopeAnalysisId": "nisa-09aeb24f525f2d9f7",
            "NetworkInsightsAccessScopeAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-access-scope-analysis/nisa-0c0d3ec68a9bb2f22",
            "NetworkInsightsAccessScopeId": "nis-096f763940bb6bcf2",
            "Status": "succeeded",
            "StartDate": "2021-10-06T20:23:53.604000+00:00",
            "FindingsFound": "true",
            "Tags": []
        }
    ]
}
```

```
aws ec2 get-network-insights-access-scope-analysis-findings --network-insights-access-scope-analysis-id nisa-0c0d3ec68a9bb2f22 --max-results 1
{
    "NetworkInsightsAccessScopeAnalysisId": "nisa-09aeb24f525f2d9f7",
    "AnalysisFindings": [
        {
            "NetworkInsightsAccessScopeAnalysisId": "nisa-09aeb24f525f2d9f7",
            "NetworkInsightsAccessScopeId": "nis-096f763940bb6bcf2",
            "FindingComponents": [
                {
                    "SequenceNumber": 1,
                    "Component": {
                        "Id": "igw-1a23b4cd",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:internet-gateway/igw-1a23b4cd"
                    },
                    "OutboundHeader": {
                        "DestinationAddresses": [
                            "172.31.22.225/32"
                        ]
                    },
                    "InboundHeader": {
                        "DestinationAddresses": [
                            "52.2.112.57/32"
                        ],
                        "DestinationPortRanges": [
                            {
                                "From": 80,
                                "To": 80
                            }
                        ],
                        "Protocol": "6",
                        "SourceAddresses": [
                            "0.0.0.0/5",
                            "11.0.0.0/8",
                            "12.0.0.0/6",
                            "128.0.0.0/3",
                            "16.0.0.0/4",
                            "160.0.0.0/5",
                            "168.0.0.0/6",
                            "172.0.0.0/12",
                            "172.128.0.0/9",
                            "172.32.0.0/11",
                            "172.64.0.0/10",
                            "173.0.0.0/8",
                            "174.0.0.0/7",
                            "176.0.0.0/4",
                            "192.0.0.0/9",
                            "192.128.0.0/11",
                            "192.160.0.0/13",
                            "192.169.0.0/16",
                            "192.170.0.0/15",
                            "192.172.0.0/14",
                            "192.176.0.0/12",
                            "192.192.0.0/10",
                            "193.0.0.0/8",
                            "194.0.0.0/7",
                            "196.0.0.0/6",
                            "200.0.0.0/5",
                            "208.0.0.0/4",
                            "224.0.0.0/3",
                            "32.0.0.0/3",
                            "64.0.0.0/2",
                            "8.0.0.0/7"
                        ],
                        "SourcePortRanges": [
                            {
                                "From": 0,
                                "To": 65535
                            }
                        ]
                    }
                },
                {
                    "SequenceNumber": 2,
                    "AclRule": {
                        "Cidr": "0.0.0.0/0",
                        "Egress": false,
                        "Protocol": "all",
                        "RuleAction": "allow",
                        "RuleNumber": 100
                    },
                    "Component": {
                        "Id": "acl-579af131",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-579af131"
                    }
                },
                {
                    "SequenceNumber": 3,
                    "Component": {
                        "Id": "sg-0cab31773e042794f",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:security-group/sg-0cab31773e042794f"
                    },
                    "SecurityGroupRule": {
                        "Cidr": "0.0.0.0/0",
                        "Direction": "ingress",
                        "PortRange": {
                            "From": 80,
                            "To": 80
                        },
                        "Protocol": "tcp"
                    }
                },
                {
                    "SequenceNumber": 4,
                    "Component": {
                        "Id": "eni-0680af09e502660e7",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:network-interface/eni-0680af09e502660e7"
                    },
                    "Subnet": {
                        "Id": "subnet-8061f9db",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-8061f9db"
                    },
                    "Vpc": {
                        "Id": "vpc-abcd12e3",
                        "Arn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-abcd12e3"
                    }
                }
            ]
        }
    ],
    "NextToken": "AYADeDdyvQENR4bFEGARVczOdwQAhwACABFFbmNyeXB0aW9uQ29udGV4dAATVG9rZW5FbmNyeXB0aW9uVXRpbAAVYXdzLWNyeXB0by1wdWJsaWMta2V5AERBb3RYci9LdXdNYXhheHdYOG5WbjZGTlk0Mk1ia3hYVFdOU0EwV2ovYjVmQVRqMWpSM3I3dFhPRXFKK0QrTWVJenc9PQABAA9QYXJoZWxpb25MYW1iZGEAGi05NjU1NwAAAIAAAAAM4NzUsusuKSY0yHVOADB9dYDlEuVXCHlFz4qXPHql2SEAe0TED2c1LstAFqJlHl8Chtk3Cq8uWXWU2yXNuTMCAAAAAAwAABAAAAAAAAAAAAAAAAAA559thKnp1ZJuDMynsbizu/////8AAAABAAAAAAAAAAAAAAABAAAAs+v6C/JyLKmZzcGXs3NAp676D8RwoAdF/sSfYUnAA7JwYLPlYSfBZ5fHHPjJ8Y6AVkJEzpGGza1CuzHFG9dqvkyuLoYxkpqGgbv0e0T2Q0rLfJID+vNWEqSb03/6JXltR5ipYGD7yAnOb6vCBmheU9dDdbPE1SnidTc6XLpR8ihzdqSaJZnslAxYXNcsjrSEWmERdBhOIBaUUhRjvxaEABVsShfamuzZIBvQrvDHFeiV8BKQj5rF1y1hfJ+lzU9BgN/NrgBnMGUCMQDSA4E1zrjcR+iFS4RNJincDtRKZz3T2AmoI23+Xh44OHSrTR2XgBdewZZzvKX1tdkCMHDGRfeLrJMXLvVo/sHL6ZqGR1FYWs3UWhMpkMGDdXZcQL+is60dXqAY1LOJLaDpaQ=="
}
```

###### Note

The list of source addresses in the previous example
includes everything in the 0.0.0.0/0 address range except for the RFC1918 range.
