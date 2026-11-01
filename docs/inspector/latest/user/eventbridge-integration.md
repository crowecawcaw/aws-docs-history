

# Amazon EventBridge event schema for Amazon Inspector events
<a name="eventbridge-integration"></a>

 [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) delivers a stream of real-time data from applications and other AWS services to targets, such as AWS Lambda functions, Amazon Simple Notification Service topics, and data streams in Amazon Kinesis Data Streams. To support integration with other applications, services, and systems, Amazon Inspector automatically publishes findings to EventBridge as [events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html). You can use Amazon Inspector to publish events for findings, coverage, and scans. This section provides example schemas for EventBridge events. 

**Topics**
+ [Amazon EventBridge base schema for Amazon Inspector](#event-schema-basic)
+ [Amazon Inspector finding event schema example](#event-finding)
+ [Amazon Inspector initial scan complete event schema example](#event-initial-scan)
+ [Amazon Inspector on-demand machine image scan event schema examples](#event-on-demand-scan)
+ [Amazon Inspector coverage event schema example](#event-coverage-event)
+ [Amazon Inspector auto enable schema example](#event-auto-enable)

## Amazon EventBridge base schema for Amazon Inspector
<a name="event-schema-basic"></a>

The following is an example of the basic schema for an EventBridge event for Amazon Inspector. Event details differ based on the type of event.

```
{
    "version": "0",
    "id": "Event ID",
    "detail-type": "Inspector2 *event type*",
    "source": "aws.inspector2",
    "account": "AWS account ID (string)",
    "time": "event timestamp (string)",
    "region": "AWS Region (string)",
    "resources": [
        *IDs or ARNs of the resources involved in the event* 
    ],
    "detail": {
        *Details of an Amazon Inspector event type*
    }
}
```

## Amazon Inspector finding event schema example
<a name="event-finding"></a>

 The following includes examples of the schema for an EventBridge event for Amazon Inspector findings. Finding events are created when Amazon Inspector identifies a software vulnerability or network issue in one of your resources. For a guide to creating notifications in response to this type of event, see [Creating custom responses to Amazon Inspector findings with Amazon EventBridge](findings-managing-automating-responses.md).

 The following fields identify a finding event: 
+  `detail-type` is set to `Inspector2 Finding`. 
+  `detail` describes the finding. 
+  `detail.resources.tags` is where key-value data is stored. 

 Each object in `detail.resources` can also include the following fields. These fields are present for all resources, including AWS resources. 

 For AWS resources, these fields appear alongside the AWS-specific fields. You can rely on a single, provider-agnostic representation regardless of where the resource is hosted. 
+  `provider` is the cloud provider of the resource, for example `AWS` or `AZURE`. 
+  `providerAccountId` is the cloud provider account identifier for the resource, such as an Azure subscription ID. For AWS resources, this matches the `account` field. 
+  `providerOrgId` is the cloud provider organization or tenant identifier for the resource, such as an Azure tenant ID. Amazon Inspector populates this field for `AZURE` resources. 
+  `detail.resources.details` contains a provider-agnostic resource detail object that corresponds to the resource `type`: `vm` for a virtual machine, `image` for a container image, or `serverlessFunction` for a serverless function. These are the multi-cloud equivalents of the `awsEc2Instance`, `awsEcrContainerImage`, and `awsLambdaFunction` objects. For AWS resources, Amazon Inspector also includes the provider-agnostic object alongside the corresponding AWS-specific object. For example, an Amazon EC2 instance finding includes both `awsEc2Instance` and `vm`. 

 You can filter the tabs to see finding event schemas for different resources and finding types. 

------
#### [ Amazon EC2 package vulnerability finding ]

```
{
    "version": "0",
    "id": "4d621919-f1f4-4201-a0e2-37e4e330ff51",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "123456789012",
    "time": "2024-09-04T17:00:36Z",
    "region": "eu-central-1",
    "resources": [
        "i-12345678901234567"
    ],
    "detail": {
        "awsAccountId": "123456789012",
        "description": "In snapd versions prior to 2.62, snapd failed to properly check the destination of symbolic links when extracting a snap. The snap format is a squashfs file-system image and so can contain symbolic links and other file types. Various file entries within the snap squashfs image (such as icons and desktop files etc) are directly read by snapd when it is extracted. An attacker who could convince a user to install a malicious snap which contained symbolic links at these paths could then cause snapd to write out the contents of the symbolic link destination into a world-readable directory. This in-turn could allow an unprivileged user to gain access to privileged information.",
        "epss": {
            "score": 0.00043
        },
        "exploitAvailable": "NO",
        "findingArn": "arn:aws:inspector2:eu-central-1:123456789012:finding/{{FINDING_ID}}",
        "firstObservedAt": "Wed Sep 04 16:59:44.356 UTC 2024",
        "fixAvailable": "YES",
        "inspectorScore": 4.8,
        "inspectorScoreDetails": {
            "adjustedCvss": {
                "adjustments": [],
                "cvssSource": "UBUNTU_CVE",
                "score": 4.8,
                "scoreSource": "UBUNTU_CVE",
                "scoringVector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:L",
                "version": "3.1"
            }
        },
        "lastObservedAt": "Wed Sep 04 16:59:44.476 UTC 2024",
        "packageVulnerabilityDetails": {
            "cvss": [
                {
                    "baseScore": 4.8,
                    "scoringVector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:L",
                    "source": "UBUNTU_CVE",
                    "version": "3.1"
                },
                {
                    "baseScore": 7.3,
                    "scoringVector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H",
                    "source": "NVD",
                    "version": "3.1"
                }
            ],
            "referenceUrls": [
                "https://www.cve.org/CVERecord?id=CVE-2024-29069",
                "https://ubuntu.com/security/notices/USN-6940-1"
            ],
            "relatedVulnerabilities": [
                "USN-6940-1"
            ],
            "source": "UBUNTU_CVE",
            "sourceUrl": "https://people.canonical.com/~ubuntu-security/cve/2024/CVE-2024-29069.html",
            "vendorCreatedAt": "Thu Jul 25 20:15:00.000 UTC 2024",
            "vendorSeverity": "medium",
            "vulnerabilityId": "CVE-2024-29069",
            "vulnerablePackages": [
                {
                    "arch": "ALL",
                    "epoch": 0,
                    "fixedInVersion": "0:2.63+22.04ubuntu0.1",
                    "name": "snapd",
                    "packageManager": "OS",
                    "remediation": "apt-get update && apt-get upgrade",
                    "version": "2.63"
                }
            ]
        },
        "remediation": {
            "recommendation": {
                "text": "None Provided"
            }
        },
        "resources": [
            {
                "details": {
                    "awsEc2Instance": {
                        "iamInstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/AmazonSSMRoleForInstancesQuickSetup",
                        "imageId": "ami-02ff980600c693b38",
                        "ipV4Addresses": [
                            "192.0.2.10",
                            "203.0.113.20"
                        ],
                        "ipV6Addresses": [],
                        "launchedAt": "Wed Sep 04 16:57:40.000 UTC 2024",
                        "platform": "UBUNTU_22_04",
                        "subnetId": "subnet-12345678",
                        "type": "t2.small",
                        "vpcId": "vpc-12345678"
                    },
                    "vm": {
                        "type": "t2.small",
                        "vmImageReference": "ami-02ff980600c693b38",
                        "ipV4Addresses": [
                            "192.0.2.10",
                            "203.0.113.20"
                        ],
                        "ipV6Addresses": [],
                        "networkId": "vpc-12345678",
                        "subnetIds": [
                            "subnet-12345678"
                        ],
                        "launchedAt": "Wed Sep 04 16:57:40.000 UTC 2024",
                        "platform": "UBUNTU_22_04",
                        "executionRole": "arn:aws:iam::123456789012:instance-profile/AmazonSSMRoleForInstancesQuickSetup"
                    }
                },
                "id": "i-12345678901234567",
                "partition": "aws",
                "provider": "AWS",
                "providerAccountId": "123456789012",
                "region": "eu-central-1",
                "type": "AWS_EC2_INSTANCE"
            }
        ],
        "severity": "MEDIUM",
        "status": "CLOSED",
        "title": "CVE-2024-29069 - snapd",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Wed Sep 04 17:00:36.951 UTC 2024"
    }
}
```

------
#### [ Amazon EC2 network reachability finding ]

```
{
    "version": "0",
    "id": "9eb1603b-4263-19ec-8be2-33184694cb92",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "123456789012",
    "time": "2024-09-05T13:06:56Z",
    "region": "eu-central-1",
    "resources": ["i-12345678901234567"],
    "detail": {
        "awsAccountId": "123456789012",
        "description": "On the instance i-12345678901234567, the port range 22-22 is reachable from the InternetGateway igw-261bab4d from an attached ENI eni-094ad651219472857.",
        "findingArn": "arn:aws:inspector2:eu-central-1:123456789012:finding/{{FINDING_ID}}",
        "firstObservedAt": "Thu Sep 05 13:06:56.334 UTC 2024",
        "lastObservedAt": "Thu Sep 05 13:06:56.334 UTC 2024",
        "networkReachabilityDetails": {
            "networkPath": {
                "steps": [{
                    "componentId": "igw-261bab4d",
                    "componentType": "AWS::EC2::InternetGateway"
                }, {
                    "componentId": "acl-171b527d",
                    "componentType": "AWS::EC2::NetworkAcl"
                }, {
                    "componentId": "sg-0d34debf87410f2d9",
                    "componentType": "AWS::EC2::SecurityGroup"
                }, {
                    "componentId": "eni-094ad651219472857",
                    "componentType": "AWS::EC2::NetworkInterface"
                }, {
                    "componentId": "i-12345678901234567",
                    "componentType": "AWS::EC2::Instance"
                }]
            },
            "openPortRange": {
                "begin": 22,
                "end": 22
            },
            "protocol": "TCP"
        },
        "remediation": {
            "recommendation": {
                "text": "You can restrict access to your instance by modifying the Security Groups or ACLs in the network path."
            }
        },
        "resources": [{
            "details": {
                "awsEc2Instance": {
                    "iamInstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/AmazonSSMRoleForInstancesQuickSetup",
                    "imageId": "ami-02ff980600c693b38",
                    "ipV4Addresses": ["192.0.2.10", "203.0.113.20"],
                    "ipV6Addresses": [],
                    "launchedAt": "Wed Sep 04 17:41:24.000 UTC 2024",
                    "platform": "UBUNTU_22_04",
                    "subnetId": "subnet-12345678",
                    "type": "t2.small",
                    "vpcId": "vpc-12345678"
                },
                "vm": {
                    "type": "t2.small",
                    "vmImageReference": "ami-02ff980600c693b38",
                    "ipV4Addresses": ["192.0.2.10", "203.0.113.20"],
                    "ipV6Addresses": [],
                    "networkId": "vpc-12345678",
                    "subnetIds": ["subnet-12345678"],
                    "launchedAt": "Wed Sep 04 17:41:24.000 UTC 2024",
                    "platform": "UBUNTU_22_04",
                    "executionRole": "arn:aws:iam::123456789012:instance-profile/AmazonSSMRoleForInstancesQuickSetup"
                }
            },
            "id": "i-12345678901234567",
            "partition": "aws",
            "provider": "AWS",
            "providerAccountId": "123456789012",
            "region": "eu-central-1",
            "type": "AWS_EC2_INSTANCE"
        }],
        "severity": "MEDIUM",
        "status": "ACTIVE",
        "title": "Port 22 is reachable from an Internet Gateway - TCP",
        "type": "NETWORK_REACHABILITY",
        "updatedAt": "Thu Sep 05 13:06:56.334 UTC 2024"
    }
}
```

------
#### [ Amazon ECR package vulnerability finding ]

```
{
    "version": "0",
    "id": "5325facf-a1aa-7d97-6bce-25fde6f6d2fc",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "123456789012",
    "time": "2024-09-04T16:55:38Z",
    "region": "eu-central-1",
    "resources": [
        "arn:aws:ecr:eu-central-1:123456789012:repository/inspector2/sha256:84f507df33c6864d49c296fb734192696e4cb6f78166ac51ac8b9b118181085d"
    ],
    "detail.resources.tags.testkey": "allow",
    "detail": {
        "awsAccountId": "123456789012",
        "description": "Possible denial of service in X.509 name checks",
        "epss": {
            "score": 0.00045
        },
        "exploitAvailable": "NO",
        "findingArn": "arn:aws:inspector2:eu-central-1:123456789012:finding/{{FINDING_ID}}",
        "firstObservedAt": "Wed Sep 04 16:55:38.411 UTC 2024",
        "fixAvailable": "YES",
        "lastObservedAt": "Wed Sep 04 16:55:38.411 UTC 2024",
        "packageVulnerabilityDetails": {
            "cvss": [],
            "referenceUrls": [
                "https://www.cve.org/CVERecord?id=CVE-2024-6119",
                "https://ubuntu.com/security/notices/USN-6986-1"
            ],
            "relatedVulnerabilities": [
                "USN-6986-1"
            ],
            "source": "UBUNTU_CVE",
            "sourceUrl": "https://people.canonical.com/~ubuntu-security/cve/2024/CVE-2024-6119.html",
            "vendorCreatedAt": "Tue Sep 03 00:00:00.000 UTC 2024",
            "vendorSeverity": "medium",
            "vulnerabilityId": "CVE-2024-6119",
            "vulnerablePackages": [
                {
                    "arch": "ARM64",
                    "epoch": 0,
                    "fixedInVersion": "0:3.0.13-0ubuntu3.4",
                    "name": "libssl3t64",
                    "packageManager": "OS",
                    "release": "0ubuntu3.2",
                    "remediation": "apt-get update && apt-get upgrade",
                    "sourceLayerHash": "sha256:1567e7ea90b67fc95ccdeeec39bdc3045098dee7e0c604975b957a9f8c0e9616",
                    "version": "3.0.13"
                },
                {
                    "arch": "ARM64",
                    "epoch": 0,
                    "fixedInVersion": "0:3.0.13-0ubuntu3.4",
                    "name": "openssl",
                    "packageManager": "OS",
                    "release": "0ubuntu3.2",
                    "remediation": "apt-get update && apt-get upgrade",
                    "sourceLayerHash": "sha256:1567e7ea90b67fc95ccdeeec39bdc3045098dee7e0c604975b957a9f8c0e9616",
                    "version": "3.0.13"
                }
            ]
        },
        "remediation": {
            "recommendation": {
                "text": "None Provided"
            }
        },
        "resources": [
            {
                "details": {
                    "awsEcrContainerImage": {
                        "architecture": "arm64",
                        "imageHash": "sha256:84f507df33c6864d49c296fb734192696e4cb6f78166ac51ac8b9b118181085d",
                        "imageTags": [
                            "ubuntu_latest"
                        ],
                        "platform": "UBUNTU_24_04",
                        "pushedAt": "Wed Sep 04 16:55:28.000 UTC 2024",
                        "registry": "123456789012",
                        "repositoryName": "inspector2"
                    },
                    "image": {
                        "repositoryName": "inspector2",
                        "registry": "123456789012",
                        "imageTags": [
                            "ubuntu_latest"
                        ],
                        "imageDigest": "sha256:84f507df33c6864d49c296fb734192696e4cb6f78166ac51ac8b9b118181085d",
                        "pushedAt": "Wed Sep 04 16:55:28.000 UTC 2024",
                        "architecture": "arm64",
                        "platform": "UBUNTU_24_04"
                    }
                },
                "id": "arn:aws:ecr:eu-central-1:123456789012:repository/inspector2/sha256:84f507df33c6864d49c296fb734192696e4cb6f78166ac51ac8b9b118181085d",
                "partition": "aws",
                "provider": "AWS",
                "providerAccountId": "123456789012",
                "region": "eu-central-1",
                "type": "AWS_ECR_CONTAINER_IMAGE"
            }
        ],
        "severity": "MEDIUM",
        "status": "ACTIVE",
        "title": "CVE-2024-6119 - libssl3t64, openssl",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Wed Sep 04 16:55:38.411 UTC 2024"
    }
}
```

------
#### [  Lambda package vulnerability finding ]

```
{
    "version": "0",
    "id": "9eadd71a-e49c-9864-6ba9-2a5d3f83c88f",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "123456789012",
    "time": "2024-09-04T16:50:37Z",
    "region": "eu-central-1",
    "resources": [
        "arn:aws:lambda:eu-central-1:123456789012:function:VulnerableFunction:$LATEST"
    ],
    "detail": {
        "awsAccountId": "123456789012",
        "description": "Flask is a lightweight WSGI web application framework. When all of the following conditions are met, a response containing data intended for one client may be cached and subsequently sent by the proxy to other clients. If the proxy also caches `Set-Cookie` headers, it may send one client's `session` cookie to other clients. The severity depends on the application's use of the session and the proxy's behavior regarding cookies. The risk depends on all these conditions being met.\n\n1. The application must be hosted behind a caching proxy that does not strip cookies or ignore responses with cookies. 2. The application sets `session.permanent = True` 3. The application does not access or modify the session at any point during a request. 4. `SESSION_REFRESH_EACH_REQUEST` enabled (the default). 5. The application does not set a `Cache-Control` header to indicate that a page is private or should not be cached.\n\nThis happens because vulnerable versions of Flask only set the `Vary: Cookie` header when the session is ac",
        "epss": {
            "score": 0.00208
        },
        "exploitAvailable": "YES",
        "exploitabilityDetails": {
            "lastKnownExploitAt": "Sat Aug 31 00:04:50.000 UTC 2024"
        },
        "findingArn": "arn:aws:inspector2:eu-central-1:123456789012:finding/{{FINDING_ID}}",
        "firstObservedAt": "Wed Sep 04 16:50:37.627 UTC 2024",
        "fixAvailable": "YES",
        "inspectorScore": 7.5,
        "inspectorScoreDetails": {
            "adjustedCvss": {
                "cvssSource": "NVD",
                "score": 7.5,
                "scoreSource": "NVD",
                "scoringVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
                "version": "3.1"
            }
        },
        "lastObservedAt": "Wed Sep 04 16:50:37.627 UTC 2024",
        "packageVulnerabilityDetails": {
            "cvss": [
                {
                    "baseScore": 7.5,
                    "scoringVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
                    "source": "NVD",
                    "version": "3.1"
                }
            ],
            "referenceUrls": [
                "https://www.debian.org/security/2023/dsa-5442",
                "https://lists.debian.org/debian-lts-announce/2023/08/msg00024.html"
            ],
            "relatedVulnerabilities": [],
            "source": "NVD",
            "sourceUrl": "https://nvd.nist.gov/vuln/detail/CVE-2023-30861",
            "vendorCreatedAt": "Tue May 02 18:15:52.000 UTC 2023",
            "vendorSeverity": "HIGH",
            "vendorUpdatedAt": "Sun Aug 20 21:15:09.000 UTC 2023",
            "vulnerabilityId": "CVE-2023-30861",
            "vulnerablePackages": [
                {
                    "epoch": 0,
                    "filePath": "requirements.txt",
                    "fixedInVersion": "2.3.2",
                    "name": "flask",
                    "packageManager": "PIP",
                    "version": "2.0.0"
                }
            ]
        },
        "remediation": {
            "recommendation": {
                "text": "None Provided"
            }
        },
        "resources": [
            {
                "details": {
                    "awsLambdaFunction": {
                        "architectures": [
                            "X86_64"
                        ],
                        "codeSha256": "O7jkFEmfPB+CK3Y6Pby5zW9gjG+zusAaqRRMGS8B27c=",
                        "executionRoleArn": "arn:aws:iam::123456789012:role/service-role/VulnerableFunction-role-f9vs5mq8",
                        "functionName": "VulnerableFunction",
                        "lastModifiedAt": "Wed Sep 04 16:50:20.000 UTC 2024",
                        "packageType": "ZIP",
                        "runtime": "PYTHON_3_11",
                        "version": "$LATEST"
                    },
                    "serverlessFunction": {
                        "serverlessFunctionName": "VulnerableFunction",
                        "runtime": "PYTHON_3_11",
                        "version": "$LATEST",
                        "codeDigest": "O7jkFEmfPB+CK3Y6Pby5zW9gjG+zusAaqRRMGS8B27c=",
                        "lastModifiedAt": "Wed Sep 04 16:50:20.000 UTC 2024",
                        "executionRole": "arn:aws:iam::123456789012:role/service-role/VulnerableFunction-role-f9vs5mq8",
                        "packageType": "ZIP",
                        "architectures": [
                            "X86_64"
                        ]
                    }
                },
                "id": "arn:aws:lambda:eu-central-1:123456789012:function:VulnerableFunction:$LATEST",
                "partition": "aws",
                "provider": "AWS",
                "providerAccountId": "123456789012",
                "region": "eu-central-1",
                "type": "AWS_LAMBDA_FUNCTION"
            }
        ],
        "severity": "HIGH",
        "status": "ACTIVE",
        "title": "CVE-2023-30861 - flask",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Wed Sep 04 16:50:37.627 UTC 2024"
    }
}
```

------
#### [ Lambda code vulnerability finding ]

```
{
    "version": "0",
    "id": "e764f7be-f931-ff1b-204b-8cab2d91724b",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "123456789012",
    "time": "2024-09-04T16:51:01Z",
    "region": "eu-central-1",
    "resources": [
        "arn:aws:lambda:eu-central-1:123456789012:function:VulnerableFunction:$LATEST"
    ],
    "detail": {
        "awsAccountId": "123456789012",
        "codeVulnerabilityDetails": {
            "cwes": [
                "CWE-798"
            ],
            "detectorId": "python/hardcoded-credentials@v1.0",
            "detectorName": "Hardcoded credentials",
            "detectorTags": [
                "secrets",
                "security",
                "owasp-top10",
                "top25-cwes",
                "cwe-798",
                "Python"
            ],
            "filePath": {
                "endLine": 6,
                "fileName": "lambda_function.py",
                "filePath": "lambda_function.py",
                "startLine": 6
            },
            "ruleId": "python-detect-hardcoded-aws-credentials"
        },
        "description": "Access credentials, such as passwords and access keys, should not be hardcoded in source code. Hardcoding credentials may cause leaks even after removing them. This is because version control systems might retain older versions of the code. Credentials should be stored securely and obtained from the runtime environment.",
        "findingArn": "arn:aws:inspector2:eu-central-1:123456789012:finding/{{FINDING_ID}}",
        "firstObservedAt": "Wed Sep 04 16:51:01.869 UTC 2024",
        "lastObservedAt": "Wed Sep 04 16:51:01.869 UTC 2024",
        "remediation": {
            "recommendation": {
                "text": "Your code uses hardcoded AWS credentials which might allow unauthorized users access to your AWS account. These attacks can occur a long time after the credentials are removed from the code. We recommend that you set AWS credentials with environment variables or an AWS profile instead. You should consider deleting the affected account or rotating the secret key and then monitoring Amazon CloudWatch for unexpected activity.\n[https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)"
            }
        },
        "resources": [
            {
                "details": {
                    "awsLambdaFunction": {
                        "architectures": [
                            "X86_64"
                        ],
                        "codeSha256": "O7jkFEmfPB+CK3Y6Pby5zW9gjG+zusAaqRRMGS8B27c=",
                        "executionRoleArn": "arn:aws:iam::123456789012:role/service-role/VulnerableFunction-role-f9vs5mq8",
                        "functionName": "VulnerableFunction",
                        "lastModifiedAt": "Wed Sep 04 16:50:20.000 UTC 2024",
                        "packageType": "ZIP",
                        "runtime": "PYTHON_3_11",
                        "version": "$LATEST"
                    },
                    "serverlessFunction": {
                        "serverlessFunctionName": "VulnerableFunction",
                        "runtime": "PYTHON_3_11",
                        "version": "$LATEST",
                        "codeDigest": "O7jkFEmfPB+CK3Y6Pby5zW9gjG+zusAaqRRMGS8B27c=",
                        "lastModifiedAt": "Wed Sep 04 16:50:20.000 UTC 2024",
                        "executionRole": "arn:aws:iam::123456789012:role/service-role/VulnerableFunction-role-f9vs5mq8",
                        "packageType": "ZIP",
                        "architectures": [
                            "X86_64"
                        ]
                    }
                },
                "id": "arn:aws:lambda:eu-central-1:123456789012:function:VulnerableFunction:$LATEST",
                "partition": "aws",
                "provider": "AWS",
                "providerAccountId": "123456789012",
                "region": "eu-central-1",
                "type": "AWS_LAMBDA_FUNCTION"
            }
        ],
        "severity": "CRITICAL",
        "status": "ACTIVE",
        "title": "CWE-798 - Hardcoded credentials",
        "type": "CODE_VULNERABILITY",
        "updatedAt": "Wed Sep 04 16:51:01.869 UTC 2024"
    }
}
```

------
#### [ Azure virtual machine package vulnerability finding ]

```
{
    "version": "0",
    "id": "a1b2c3d4-1111-2222-3333-444455556666",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "123456789012",
    "time": "2024-09-04T17:00:36Z",
    "region": "us-east-1",
    "resources": [
        "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.compute/virtualmachines/example-vm"
    ],
    "detail": {
        "awsAccountId": "123456789012",
        "description": "A package vulnerability was detected on an Azure virtual machine monitored by Amazon Inspector.",
        "exploitAvailable": "NO",
        "findingArn": "arn:aws:inspector2:us-east-1:123456789012:finding/{{FINDING_ID}}",
        "firstObservedAt": "Wed Sep 04 16:59:44.356 UTC 2024",
        "fixAvailable": "YES",
        "lastObservedAt": "Wed Sep 04 16:59:44.476 UTC 2024",
        "packageVulnerabilityDetails": {
            "cvss": [
                {
                    "baseScore": 4.8,
                    "scoringVector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:L",
                    "source": "UBUNTU_CVE",
                    "version": "3.1"
                }
            ],
            "referenceUrls": [
                "https://www.cve.org/CVERecord?id=CVE-2024-29069"
            ],
            "relatedVulnerabilities": [],
            "source": "UBUNTU_CVE",
            "sourceUrl": "https://people.canonical.com/~ubuntu-security/cve/2024/CVE-2024-29069.html",
            "vendorSeverity": "medium",
            "vulnerabilityId": "CVE-2024-29069",
            "vulnerablePackages": [
                {
                    "arch": "ALL",
                    "epoch": 0,
                    "fixedInVersion": "0:2.63+22.04ubuntu0.1",
                    "name": "snapd",
                    "packageManager": "OS",
                    "remediation": "apt-get update && apt-get upgrade",
                    "version": "2.63"
                }
            ]
        },
        "remediation": {
            "recommendation": {
                "text": "None Provided"
            }
        },
        "resources": [
            {
                "details": {
                    "vm": {
                        "type": "Standard_D2s_v3",
                        "vmName": "example-vm",
                        "vmImageReference": "Canonical:0001-com-ubuntu-server-jammy:22_04-lts:latest",
                        "ipV4Addresses": [
                            "10.0.0.4"
                        ],
                        "ipV6Addresses": [],
                        "networkId": "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.network/virtualnetworks/example-vnet",
                        "subnetIds": [
                            "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.network/virtualnetworks/example-vnet/subnets/default"
                        ],
                        "securityGroupIds": [
                            "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.network/networksecuritygroups/example-nsg"
                        ],
                        "launchedAt": "Wed Sep 04 16:57:40.000 UTC 2024",
                        "platform": "UBUNTU_22_04",
                        "executionRole": "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.managedidentity/userassignedidentities/example-identity",
                        "keyName": "example-key"
                    }
                },
                "id": "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.compute/virtualmachines/example-vm",
                "provider": "AZURE",
                "providerAccountId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                "providerOrgId": "11111111-2222-3333-4444-555555555555",
                "region": "eastus",
                "type": "Microsoft.Compute/virtualMachines"
            }
        ],
        "severity": "MEDIUM",
        "status": "ACTIVE",
        "title": "CVE-2024-29069 - snapd",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Wed Sep 04 17:00:36.951 UTC 2024"
    }
}
```

------
#### [ Azure container image package vulnerability finding ]

```
{
    "version": "0",
    "id": "b2c3d4e5-2222-3333-4444-555566667777",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "123456789012",
    "time": "2024-09-04T16:55:38Z",
    "region": "us-east-1",
    "resources": [
        "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.containerregistry/registries/exampleregistry/repositories/inspector2/images/sha256:84f507df33c6864d49c296fb734192696e4cb6f78166ac51ac8b9b118181085d"
    ],
    "detail": {
        "awsAccountId": "123456789012",
        "description": "A package vulnerability was detected in an Azure Container Registry image monitored by Amazon Inspector.",
        "exploitAvailable": "NO",
        "findingArn": "arn:aws:inspector2:us-east-1:123456789012:finding/{{FINDING_ID}}",
        "firstObservedAt": "Wed Sep 04 16:55:38.411 UTC 2024",
        "fixAvailable": "YES",
        "lastObservedAt": "Wed Sep 04 16:55:38.411 UTC 2024",
        "packageVulnerabilityDetails": {
            "cvss": [],
            "referenceUrls": [
                "https://www.cve.org/CVERecord?id=CVE-2024-6119"
            ],
            "relatedVulnerabilities": [],
            "source": "UBUNTU_CVE",
            "sourceUrl": "https://people.canonical.com/~ubuntu-security/cve/2024/CVE-2024-6119.html",
            "vendorSeverity": "medium",
            "vulnerabilityId": "CVE-2024-6119",
            "vulnerablePackages": [
                {
                    "arch": "ARM64",
                    "epoch": 0,
                    "fixedInVersion": "0:3.0.13-0ubuntu3.4",
                    "name": "openssl",
                    "packageManager": "OS",
                    "remediation": "apt-get update && apt-get upgrade",
                    "version": "3.0.13"
                }
            ]
        },
        "remediation": {
            "recommendation": {
                "text": "None Provided"
            }
        },
        "resources": [
            {
                "details": {
                    "image": {
                        "repositoryName": "inspector2",
                        "registry": "exampleregistry.azurecr.io",
                        "imageTags": [
                            "ubuntu_latest"
                        ],
                        "imageDigest": "sha256:84f507df33c6864d49c296fb734192696e4cb6f78166ac51ac8b9b118181085d",
                        "pushedAt": "Wed Sep 04 16:55:28.000 UTC 2024",
                        "architecture": "arm64",
                        "author": "example-author",
                        "platform": "UBUNTU_24_04"
                    }
                },
                "id": "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.containerregistry/registries/exampleregistry/repositories/inspector2/images/sha256:84f507df33c6864d49c296fb734192696e4cb6f78166ac51ac8b9b118181085d",
                "provider": "AZURE",
                "providerAccountId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                "providerOrgId": "11111111-2222-3333-4444-555555555555",
                "region": "eastus",
                "type": "Microsoft.ContainerRegistry/registry/containerImage"
            }
        ],
        "severity": "MEDIUM",
        "status": "ACTIVE",
        "title": "CVE-2024-6119 - openssl",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Wed Sep 04 16:55:38.411 UTC 2024"
    }
}
```

------
#### [ Azure function app package vulnerability finding ]

```
{
    "version": "0",
    "id": "c3d4e5f6-3333-4444-5555-666677778888",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "123456789012",
    "time": "2024-09-04T16:50:37Z",
    "region": "us-east-1",
    "resources": [
        "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.web/sites/example-functionapp"
    ],
    "detail": {
        "awsAccountId": "123456789012",
        "description": "A package vulnerability was detected in an Azure function app monitored by Amazon Inspector.",
        "exploitAvailable": "YES",
        "findingArn": "arn:aws:inspector2:us-east-1:123456789012:finding/{{FINDING_ID}}",
        "firstObservedAt": "Wed Sep 04 16:50:37.627 UTC 2024",
        "fixAvailable": "YES",
        "lastObservedAt": "Wed Sep 04 16:50:37.627 UTC 2024",
        "packageVulnerabilityDetails": {
            "cvss": [
                {
                    "baseScore": 7.5,
                    "scoringVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
                    "source": "NVD",
                    "version": "3.1"
                }
            ],
            "referenceUrls": [],
            "relatedVulnerabilities": [],
            "source": "NVD",
            "sourceUrl": "https://nvd.nist.gov/vuln/detail/CVE-2023-30861",
            "vendorSeverity": "HIGH",
            "vulnerabilityId": "CVE-2023-30861",
            "vulnerablePackages": [
                {
                    "epoch": 0,
                    "filePath": "requirements.txt",
                    "fixedInVersion": "2.3.2",
                    "name": "flask",
                    "packageManager": "PIP",
                    "version": "2.0.0"
                }
            ]
        },
        "remediation": {
            "recommendation": {
                "text": "None Provided"
            }
        },
        "resources": [
            {
                "details": {
                    "serverlessFunction": {
                        "serverlessFunctionName": "example-functionapp",
                        "runtime": "PYTHON_3_11",
                        "version": "1",
                        "codeDigest": "O7jkFEmfPB+CK3Y6Pby5zW9gjG+zusAaqRRMGS8B27c=",
                        "lastModifiedAt": "Wed Sep 04 16:50:20.000 UTC 2024",
                        "executionRole": "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.managedidentity/userassignedidentities/example-identity",
                        "packageType": "ZIP",
                        "architectures": [
                            "X86_64"
                        ]
                    }
                },
                "id": "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.web/sites/example-functionapp",
                "provider": "AZURE",
                "providerAccountId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                "providerOrgId": "11111111-2222-3333-4444-555555555555",
                "region": "eastus",
                "type": "Microsoft.Web/sites"
            }
        ],
        "severity": "HIGH",
        "status": "ACTIVE",
        "title": "CVE-2023-30861 - flask",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Wed Sep 04 16:50:37.627 UTC 2024"
    }
}
```

------

**Note**  
The detail value returns the JSON details of a single finding as an object. It does not return the entire findings response syntax, which supports multiple findings within an array.

## Amazon Inspector initial scan complete event schema example
<a name="event-initial-scan"></a>

The following is an example of the EventBridge event schema for an Amazon Inspector event for completing an initial scan. This event is created when Amazon Inspector completes an initial scan of one of your resources.

The following fields identify an initial scan complete event:
+ The `detail-type` field is set to `Inspector2 Scan`.
+ The `detail` object contains a `finding-severity-counts` object that details the number of findings in the applicable severity categories, such as `CRITICAL`, `HIGH`, and `MEDIUM`.

Select from the options to see different initial scan event schemas by resource type.

------
#### [ Amazon EC2 instance initial scan ]

```
{
    "version": "0",
    "id": "28a46762-6ac8-6cc4-4f55-bc9ab99af928",
    "detail-type": "Inspector2 Scan",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2023-01-20T22:52:35Z",
    "region": "us-east-1",
    "resources": [
        "i-087d63509b8c97098"
    ],
    "detail": {
        "scan-status": "INITIAL_SCAN_COMPLETE",
        "finding-severity-counts": {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "TOTAL": 0
        },
        "instance-id": "i-087d63509b8c97098",
        "version": "1.0"
    }
}
```

------
#### [ Amazon ECR image initial scan ]

```
{
    "version": "0",
    "id": "fdaa751a-984c-a709-44f9-9a9da9cd3606",
    "detail-type": "Inspector2 Scan",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2023-01-20T23:15:18Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:ecr:us-east-1:111122223333:repository/inspector2"
    ],
    "detail": {
        "scan-status": "INITIAL_SCAN_COMPLETE",
        "repository-name": "arn:aws:ecr:us-east-1:111122223333:repository/inspector2",
        "finding-severity-counts": {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "TOTAL": 0
        },
        "image-digest": "sha256:965fbcae990b0467ed5657caceaec165018ef44a4d2d46c7cdea80a9dff0d1ea",
        "image-tags": [
            "ubuntu22"
        ],
        "version": "1.0"
    }
}
```

------
#### [ Lambda function initial scan ]

```
{
  "version": "0",
  "id": "4f290a7c-361b-c442-03c8-a629f6f20d6c",
  "detail-type": "Inspector2 Scan",
  "source": "aws.inspector2",
  "account": "111122223333",
  "time": "2023-02-23T18:06:03Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:lambda:us-west-2:111122223333:function:lambda-example:$LATEST"
  ],
  "detail": {
    "scan-status": "INITIAL_SCAN_COMPLETE",
    "finding-severity-counts": {
      "CRITICAL": 0,
      "HIGH": 0,
      "MEDIUM": 0,
      "TOTAL": 0
    },
    "version": "1.0"
  }
}
```

------
#### [ Machine image initial scan ]

```
{
  "version": "0",
  "id": "6b1f9d0e-2c47-4a52-9f10-7a1b8c3d5e2f",
  "detail-type": "Inspector2 Scan",
  "source": "aws.inspector2",
  "account": "111122223333",
  "time": "2026-08-13T13:42:52Z",
  "region": "us-east-1",
  "resources": [
    "ami-0abcdef1234567890"
  ],
  "detail": {
    "scan-status": "INITIAL_SCAN_COMPLETE",
    "finding-severity-counts": {
      "CRITICAL": 0,
      "HIGH": 2,
      "MEDIUM": 5,
      "TOTAL": 7
    },
    "machine-image-id": "ami-0abcdef1234567890",
    "version": "1.0"
  }
}
```

------

## Amazon Inspector on-demand machine image scan event schema examples
<a name="event-on-demand-scan"></a>

 The following are examples of the EventBridge event schemas for an on-demand machine image scan. Amazon Inspector publishes these events when you start a scan with the [StartOnDemandScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartOnDemandScan.html) API operation. EventBridge is the only delivery mechanism for on-demand scan findings. For more information, see [Running on-demand machine image scans with Amazon Inspector](machine-image-on-demand.md). 

Amazon Inspector publishes two kinds of events for an on-demand scan:
+  A **scan complete event**, published once when the scan reaches a terminal state. The `detail-type` field is set to `Inspector2 OnDemand Scan Complete`. A successful event contains a `findingSeverityCounts` object. A failed event contains a `scanStatusReason` field instead. 
+  A **findings event**, published once for each vulnerability that Amazon Inspector detects. The `detail-type` field is set to `OnDemand AMI Scan Findings`. These events don't include machine image metadata beyond the machine image ID. 

 Every event contains the `scanId` of the scan, so you can correlate findings events with the scan complete event for the same scan. 

Select from the options to see the different on-demand scan event schemas.

------
#### [ Scan complete – successful ]

```
{
    "version": "0",
    "id": "7bf7f4b1-9f6c-4d3e-8a2b-5c1d0e9f3a44",
    "detail-type": "Inspector2 OnDemand Scan Complete",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2026-06-12T01:30:00Z",
    "region": "us-east-1",
    "resources": [
        "ami-0abcdef1234567890"
    ],
    "detail": {
        "scanId": "9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d",
        "awsAccountId": "111122223333",
        "resourceId": "ami-0abcdef1234567890",
        "resourceType": "MACHINE_IMAGE",
        "scanStatus": "SUCCESSFUL",
        "startedAt": "2026-06-12T00:00:00.000Z",
        "completedAt": "2026-06-12T01:30:00.000Z",
        "findingSeverityCounts": {
            "CRITICAL": 0,
            "HIGH": 2,
            "MEDIUM": 5,
            "LOW": 1,
            "INFORMATIONAL": 0,
            "UNTRIAGED": 0,
            "TOTAL": 8
        },
        "version": "1.0"
    }
}
```

------
#### [ Scan complete – failed ]

```
{
    "version": "0",
    "id": "3c2e9a17-8b4d-4f61-9a0c-2d7e6f1b8c33",
    "detail-type": "Inspector2 OnDemand Scan Complete",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2026-06-12T01:30:00Z",
    "region": "us-east-1",
    "resources": [
        "ami-0abcdef1234567890"
    ],
    "detail": {
        "scanId": "9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d",
        "awsAccountId": "111122223333",
        "resourceId": "ami-0abcdef1234567890",
        "resourceType": "MACHINE_IMAGE",
        "scanStatus": "FAILED",
        "scanStatusReason": "UNSUPPORTED_OS",
        "startedAt": "2026-06-12T00:00:00.000Z",
        "completedAt": "2026-06-12T01:30:00.000Z",
        "version": "1.0"
    }
}
```

 For the list of `scanStatusReason` values that Amazon Inspector can return for a failed on-demand scan, see [Scan status values for on-demand machine image scans](machine-image-on-demand.md#machine-image-on-demand-status). 

------
#### [ Findings ]

```
{
    "source": "inspector2.ami.ondemand",
    "detail-type": "OnDemand AMI Scan Findings",
    "detail": {
        "findingArn": "arn:aws:inspector2:us-east-1:111122223333:finding/ondemand/9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d/cea7c73a3d57d9c142992e845644d317",
        "scanId": "9f1c4b8d2e6a4f0b7c3d5e1a8b2f6c4d",
        "awsAccountId": "111122223333",
        "type": "PACKAGE_VULNERABILITY",
        "title": "CVE-2022-3171 - com.google.protobuf:protobuf-java",
        "description": "A parsing issue with binary data in protobuf-java...",
        "severity": "HIGH",
        "status": "ACTIVE",
        "firstObservedAt": "2026-06-12T01:30:00.000Z",
        "lastObservedAt": "2026-06-12T01:30:00.000Z",
        "updatedAt": "2026-06-12T01:30:00.000Z",
        "resources": [
            {
                "type": "MACHINE_IMAGE",
                "id": "ami-0abcdef1234567890",
                "partition": "aws",
                "region": "us-east-1"
            }
        ],
        "inspectorScore": 7.5,
        "inspectorScoreDetails": {
            "adjustedCvss": {
                "scoreSource": "NVD",
                "cvssSource": "NVD",
                "version": "3.1",
                "score": 7.5,
                "scoringVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
                "adjustments": []
            }
        },
        "packageVulnerabilityDetails": {
            "vulnerabilityId": "CVE-2022-3171",
            "vulnerablePackages": [
                {
                    "name": "com.google.protobuf:protobuf-java",
                    "version": "2.5.0",
                    "epoch": 0,
                    "packageManager": "JAVA",
                    "filePath": "/usr/lib/jars/protobuf-java-2.5.0.jar",
                    "fixedInVersion": "3.16.3"
                }
            ],
            "source": "NVD",
            "sourceUrl": "https://nvd.nist.gov/vuln/detail/CVE-2022-3171",
            "vendorSeverity": "high"
        },
        "remediation": {
            "recommendation": {
                "text": "Update com.google.protobuf:protobuf-java to 3.16.3 or later"
            }
        },
        "fixAvailable": "YES",
        "exploitAvailable": "NO"
    }
}
```

------

**Note**  
 EventBridge delivers events at least once, so your rule can receive the same event more than once. Use the `findingArn` field to deduplicate findings events. 

## Amazon Inspector coverage event schema example
<a name="event-coverage-event"></a>

The following is an example of the EventBridge event schema for an Amazon Inspector event for coverage. This event is created when Amazon Inspector scan coverage for a resource is changed. The following fields identify a coverage event:
+ The `detail-type` field is set to `Inspector2 Coverage`.
+ The `detail` object contains a `scanStatus` object that indicates the new scanning status for the resource.

The `detail` object also includes the following fields. These fields are present for all resources, including AWS resources.
+ `provider` is the cloud provider of the resource, for example `AWS` or `AZURE`.
+ `providerAccountId` is the cloud provider account identifier for the resource, such as an Azure subscription ID. For AWS resources, this matches the `account` field.
+ `providerRegion` is the cloud provider region of the resource. For AWS resources, this matches the `region` field.
+ `providerOrgId` is the cloud provider organization or tenant identifier for the resource, such as an Azure tenant ID. Amazon Inspector populates this field for `AZURE` resources.

Select from the options to see different coverage event schemas by resource type.

------
#### [ Amazon EC2 instance coverage ]

```
{
    "version": "0",
    "id": "000adda5-0fbf-913e-bc0e-10f0376412aa",
    "detail-type": "Inspector2 Coverage",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2023-01-20T22:51:39Z",
    "region": "us-east-1",
    "resources": [
        "i-087d63509b8c97098"
    ],
    "detail": {
        "scanStatus": {
            "reason": "UNMANAGED_EC2_INSTANCE",
            "statusCodeValue": "INACTIVE"
        },
        "scanType": "PACKAGE",
        "provider": "AWS",
        "providerAccountId": "111122223333",
        "providerRegion": "us-east-1",
        "eventTimestamp": "2023-01-20T22:51:35.665501Z",
        "version": "1.0"
    }
}
```

------
#### [ Azure virtual machine coverage ]

```
{
    "version": "0",
    "id": "111b1dda-0fbf-913e-bc0e-10f0376412bb",
    "detail-type": "Inspector2 Coverage",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2023-01-20T22:51:39Z",
    "region": "us-east-1",
    "resources": [
        "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourcegroups/example-rg/providers/microsoft.compute/virtualmachines/example-vm"
    ],
    "detail": {
        "scanStatus": {
            "reason": "SUCCESSFUL",
            "statusCodeValue": "ACTIVE"
        },
        "scanType": "PACKAGE",
        "provider": "AZURE",
        "providerAccountId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "providerRegion": "eastus",
        "providerOrgId": "11111111-2222-3333-4444-555555555555",
        "eventTimestamp": "2023-01-20T22:51:35.665501Z",
        "version": "1.0"
    }
}
```

------

## Amazon Inspector auto enable schema example
<a name="event-auto-enable"></a>

 The auto-enable event is sent to the delegated admin when Amazon Inspector is unable to support the number of members in an organization. The following fields identify an auto-enable event: 
+  The `detail-type` field is set to `Inspector2 AutoEnable`. 
+  The `detail` object describes why the auto enable event failed. 

```
{ 
    "version": "0",
    "id": "85fc3613-e913-7fc4-a80c-a3753e4aa9ae", 
    "detail-type": "Inspector2 AutoEnable", 
    "source": "aws.inspector2", 
    "account": "123456789012", 
    "time": "2024-08-21T02:36:48Z", 
    "region": "us-east-1", 
    "detail": { 
        “version”: “1.0.0”, 
        “AutoEnableStatus”: “Failed”, 
        “Reason”: "The number of member accounts enabled with AWS Inspector has reached the maximum limit of 10,000" 
        } 
}
```