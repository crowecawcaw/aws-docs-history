# EventBridge events sent for enhanced

scanning in Amazon ECR

When enhanced scanning is turned on, Amazon ECR sends an event to EventBridge when the scan
frequency for a repository is changed. Amazon Inspector sends events to EventBridge when an initial
scan is completed and when an image scan finding is created, updated, or
closed.

**Event for a repository scan frequency
change**

When enhanced scanning is turned on for your registry, the following event is sent
by Amazon ECR when there is a change with a resource that has enhanced scanning turned
on. This includes new repositories being created, the scan frequency for a
repository being changed, or when images are created or deleted in repositories with
enhanced scanning turned on. For more information, see [Scan images for software vulnerabilities in Amazon ECR](image-scanning.md "image-scanning.md").

```
{
	"version": "0",
	"id": "0c18352a-a4d4-6853-ef53-0abEXAMPLE",
	"detail-type": "ECR Scan Resource Change",
	"source": "aws.ecr",
	"account": "`123456789012`",
	"time": "2021-10-14T20:53:46Z",
	"region": "`us-east-1`",
	"resources": [],
	"detail": {
		"action-type": "SCAN_FREQUENCY_CHANGE",
		"repositories": [{
				"repository-name": "repository-1",
				"repository-arn": "arn:aws:ecr:`us-east-1`:`123456789012`:repository/repository-1",
				"scan-frequency": "SCAN_ON_PUSH",
				"previous-scan-frequency": "MANUAL"
			},
			{
				"repository-name": "repository-2",
				"repository-arn": "arn:aws:ecr:`us-east-1`:`123456789012`:repository/repository-2",
				"scan-frequency": "CONTINUOUS_SCAN",
				"previous-scan-frequency": "SCAN_ON_PUSH"
			},
			{
				"repository-name": "repository-3",
				"repository-arn": "arn:aws:ecr:`us-east-1`:`123456789012`:repository/repository-3",
				"scan-frequency": "CONTINUOUS_SCAN",
				"previous-scan-frequency": "SCAN_ON_PUSH"
			}
		],
		"resource-type": "REPOSITORY",
		"scan-type": "ENHANCED"
	}
}
```

**Event for an initial image scan (enhanced
scanning)**

When enhanced scanning is turned on for your registry, the following event is sent
by Amazon Inspector when the initial image scan is completed. The `finding-severity-counts`
parameter will only return a value for a severity level if one exists. For example,
if the image contains no findings at `CRITICAL` level, then no critical
count is returned. For more information, see [Scan images for OS and programming language
package vulnerabilities in Amazon ECR](image-scanning-enhanced.md "image-scanning-enhanced.md").

Event pattern:

```
{
  "source": ["aws.inspector2"],
  "detail-type": ["Inspector2 Scan"]
}
```

Example output:

```
{
    "version": "0",
    "id": "739c0d3c-4f02-85c7-5a88-94a9EXAMPLE",
    "detail-type": "Inspector2 Scan",
    "source": "aws.inspector2",
    "account": "`123456789012`",
    "time": "2021-12-03T18:03:16Z",
    "region": "us-east-2",
    "resources": [
        "arn:aws:ecr:us-east-2:`123456789012`:repository/amazon/amazon-ecs-sample"
    ],
    "detail": {
        "scan-status": "INITIAL_SCAN_COMPLETE",
        "repository-name": "arn:aws:ecr:us-east-2:123456789012:repository/amazon/amazon-ecs-sample",
        "finding-severity-counts": {
            "CRITICAL": 7,
            "HIGH": 61,
            "MEDIUM": 62,
            "TOTAL": 158
        },
        "image-digest": "sha256:36c7b282abd0186e01419f2e58743e1bf635808231049bbc9d77e5EXAMPLE",
        "image-tags": [
            "latest"
        ]
    }
}
```

**Event for an image scan finding update (enhanced
scanning)**

When enhanced scanning is turned on for your registry, the following event is sent
by Amazon Inspector when the image scan finding is created, updated, or closed. For more
information, see [Scan images for OS and programming language
package vulnerabilities in Amazon ECR](image-scanning-enhanced.md "image-scanning-enhanced.md").

Event pattern:

```
{
  "source": ["aws.inspector2"],
  "detail-type": ["Inspector2 Finding"]
}
```

Example output:

```
{
    "version": "0",
    "id": "42dbea55-45ad-b2b4-87a8-afaEXAMPLE",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "`123456789012`",
    "time": "2021-12-03T18:02:30Z",
    "region": "us-east-2",
    "resources": [
        "arn:aws:ecr:us-east-2:`123456789012`:repository/amazon/amazon-ecs-sample/sha256:36c7b282abd0186e01419f2e58743e1bf635808231049bbc9d77eEXAMPLE"
    ],
    "detail": {
        "awsAccountId": "`123456789012`",
        "description": "In libssh2 v1.9.0 and earlier versions, the SSH_MSG_DISCONNECT logic in packet.c has an integer overflow in a bounds check, enabling an attacker to specify an arbitrary (out-of-bounds) offset for a subsequent memory read. A crafted SSH server may be able to disclose sensitive information or cause a denial of service condition on the client system when a user connects to the server.",
        "findingArn": "arn:aws:inspector2:us-east-2:`123456789012`:finding/be674aaddd0f75ac632055EXAMPLE",
        "firstObservedAt": "Dec 3, 2021, 6:02:30 PM",
        "inspectorScore": 6.5,
        "inspectorScoreDetails": {
            "adjustedCvss": {
                "adjustments": [],
                "cvssSource": "REDHAT_CVE",
                "score": 6.5,
                "scoreSource": "REDHAT_CVE",
                "scoringVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N",
                "version": "3.0"
            }
        },
        "lastObservedAt": "Dec 3, 2021, 6:02:30 PM",
        "packageVulnerabilityDetails": {
            "cvss": [
                {
                    "baseScore": 6.5,
                    "scoringVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N",
                    "source": "REDHAT_CVE",
                    "version": "3.0"
                },
                {
                    "baseScore": 5.8,
                    "scoringVector": "AV:N/AC:M/Au:N/C:P/I:N/A:P",
                    "source": "NVD",
                    "version": "2.0"
                },
                {
                    "baseScore": 8.1,
                    "scoringVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:H",
                    "source": "NVD",
                    "version": "3.1"
                }
            ],
            "referenceUrls": [
                "https://access.redhat.com/errata/RHSA-2020:3915"
            ],
            "source": "REDHAT_CVE",
            "sourceUrl": "https://access.redhat.com/security/cve/CVE-2019-17498",
            "vendorCreatedAt": "Oct 16, 2019, 12:00:00 AM",
            "vendorSeverity": "Moderate",
            "vulnerabilityId": "CVE-2019-17498",
            "vulnerablePackages": [
                {
                    "arch": "X86_64",
                    "epoch": 0,
                    "name": "libssh2",
                    "packageManager": "OS",
                    "release": "12.amzn2.2",
                    "sourceLayerHash": "sha256:72d97abdfae3b3c933ff41e39779cc72853d7bd9dc1e4800c5294dEXAMPLE",
                    "version": "1.4.3"
                }
            ]
        },
        "remediation": {
            "recommendation": {
                "text": "Update all packages in the vulnerable packages section to their latest versions."
            }
        },
        "resources": [
            {
                "details": {
                    "awsEcrContainerImage": {
                        "architecture": "amd64",
                        "imageHash": "sha256:36c7b282abd0186e01419f2e58743e1bf635808231049bbc9d77e5EXAMPLE",
                        "imageTags": [
                            "latest"
                        ],
                        "platform": "AMAZON_LINUX_2",
                        "pushedAt": "Dec 3, 2021, 6:02:13 PM",
                        "lastInUseAt": "Dec 3, 2021, 6:02:13 PM",
                        "inUseCount": 1,
                        "registry": "123456789012",
                        "repositoryName": "amazon/amazon-ecs-sample"
                    }
                },
                "id": "arn:aws:ecr:us-east-2:`123456789012`:repository/amazon/amazon-ecs-sample/sha256:36c7b282abd0186e01419f2e58743e1bf635808231049bbc9d77EXAMPLE",
                "partition": "N/A",
                "region": "N/A",
                "type": "AWS_ECR_CONTAINER_IMAGE"
            }
        ],
        "severity": "MEDIUM",
        "status": "ACTIVE",
        "title": "CVE-2019-17498 - libssh2",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Dec 3, 2021, 6:02:30 PM"
    }
}
```
