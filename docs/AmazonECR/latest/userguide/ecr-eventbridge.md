# Amazon ECR events and EventBridge

Amazon EventBridge enables you to automate your AWS services and to respond automatically to
system events such as application availability issues or resource changes. Events from
AWS services are delivered to EventBridge in near real time. You can write simple rules to
indicate which events are of interest to you and include automated actions to take when
an event matches a rule. The actions that can be automatically triggered include the
following:

- Adding events to log groups in CloudWatch Logs
- Invoking an AWS Lambda function
- Invoking Amazon EC2 Run Command
- Relaying the event to Amazon Kinesis Data Streams
- Activating an AWS Step Functions state machine
- Notifying an Amazon SNS topic or an Amazon SQS queue
  For more information, see [Getting Started
  with Amazon EventBridge](../../../eventbridge/latest/userguide/eventbridge-getting-set-up.md "../../../eventbridge/latest/userguide/eventbridge-getting-set-up.md") in the _Amazon EventBridge User Guide_.

## Sample events from Amazon ECR

The following are example events from Amazon ECR. Events are emitted on a best effort
basis.

**Event for a completed image push**

The following event is sent when each image push is completed. For more
information, see [Pushing a Docker image to an Amazon ECR private repository](docker-push-ecr-image.md "docker-push-ecr-image.md").

```
{
    "version": "0",
    "id": "13cde686-328b-6117-af20-0e5566167482",
    "detail-type": "ECR Image Action",
    "source": "aws.ecr",
    "account": "`123456789012`",
    "time": "2019-11-16T01:54:34Z",
    "region": "us-west-2",
    "resources": [],
    "detail": {
        "result": "SUCCESS",
        "repository-name": "`my-repository-name`",
        "image-digest": "`sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234`",
        "action-type": "PUSH",
        "image-tag": "latest"
    }
}
```

**Event for a pull through cache action**

The following event is sent when a pull through cache action is attempted. For
more information, see [Sync an upstream registry with an Amazon ECR private registry](pull-through-cache.md "pull-through-cache.md").

```
{
    "version": "0",
    "id": "85fc3613-e913-7fc4-a80c-a3753e4aa9ae",
    "detail-type": "ECR Pull Through Cache Action",
    "source": "aws.ecr",
    "account": "`123456789012`",
    "time": "2023-02-29T02:36:48Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecr:us-west-2:`123456789012`:repository/docker-hub/alpine"
    ],
    "detail": {
        "rule-version": "1",
        "sync-status": "SUCCESS",
        "ecr-repository-prefix": "docker-hub",
        "repository-name": "docker-hub/alpine",
        "upstream-registry-url": "public.ecr.aws",
        "image-tag": "3.17.2",
        "image-digest": "`sha256:4aa08ef415aecc80814cb42fa41b658480779d80c77ab15EXAMPLE`",
    }
}
```

**Event for a completed image scan (basic
scanning)**

When basic scanning is enabled for your registry, the following event is sent when
each image scan is completed. The `finding-severity-counts` parameter
will only return a value for a severity level if one exists. For example, if the
image contains no findings at `CRITICAL` level, then no critical count is
returned. For more information, see [Scan images for OS vulnerabilities in Amazon ECR](image-scanning-basic.md "image-scanning-basic.md").

###### Note

For details about events that Amazon Inspector emits when enhanced scanning is enabled,
see [EventBridge events sent for enhanced scanning in Amazon ECR](image-scanning-enhanced-events.md "image-scanning-enhanced-events.md").

```
{
    "version": "0",
    "id": "85fc3613-e913-7fc4-a80c-a3753e4aa9ae",
    "detail-type": "ECR Image Scan",
    "source": "aws.ecr",
    "account": "`123456789012`",
    "time": "2019-10-29T02:36:48Z",
    "region": "`us-east-1`",
    "resources": [
        "arn:aws:ecr:`us-east-1`:`123456789012`:repository/`my-repository-name`"
    ],
    "detail": {
        "scan-status": "COMPLETE",
        "repository-name": "`my-repository-name`",
        "finding-severity-counts": {
	       "CRITICAL": `10`,
	       "MEDIUM": `9`
	     },
        "image-digest": "`sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234`",
        "image-tags": []
    }
}
```

**Event for a change notification on a resource with enhanced
scanning enabled (enhanced scanning)**

When enhanced scanning is enabled for your registry, the following event is sent
by Amazon ECR when there is a change with a resource that has enhanced scanning enabled.
This includes new repositories being created, the scan frequency for a repository
being changed, or when images are created or deleted in repositories with enhanced
scanning enabled. For more information, see [Scan images for software vulnerabilities in Amazon ECR](image-scanning.md "image-scanning.md").

```
{
	"version": "0",
	"id": "0c18352a-a4d4-6853-ef53-0ab8638973bf",
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

**Event for an image deletion**

The following event is sent when an image is deleted. For more information, see
[Deleting an image in Amazon ECR](delete_image.md "delete_image.md").

```
{
    "version": "0",
    "id": "dd3b46cb-2c74-f49e-393b-28286b67279d",
    "detail-type": "ECR Image Action",
    "source": "aws.ecr",
    "account": "`123456789012`",
    "time": "2019-11-16T02:01:05Z",
    "region": "us-west-2",
    "resources": [],
    "detail": {
        "result": "SUCCESS",
        "repository-name": "`my-repository-name`",
        "image-digest": "`sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234`",
        "action-type": "DELETE",
        "image-tag": "latest"
    }
}
```

**Event for an image archival action**

The following event is sent when an image is archived. The
`target-storage-class` field will be set to `ARCHIVE`.
The event includes the manifest and artifact media types to identify the type of
content being archived.

```
{
    "version": "0",
    "id": "4f5ec4d5-4de4-7aad-a046-EXAMPLE",
    "detail-type": "ECR Image Action",
    "source": "aws.ecr",
    "account": "`123456789012`",
    "time": "2019-08-06T00:58:09Z",
    "region": "`us-east-1`",
    "resources": [],
    "detail": {
        "action-type": "UPDATE_STORAGE_CLASS",
        "target-storage-class": "ARCHIVE",
        "image-digest": "`sha256:f98d67af8e53a536502bfc600de3266556b06ed635a32d60aa7a5fe6d7e609d7`",
        "repository-name": "`ubuntu`",
        "result": "SUCCESS",
        "manifest-media-type": "application/vnd.oci.image.manifest.v1+json",
        "artifact-media-type": "application/vnd.oci.image.config.v1+json"
    }
}
```

**Event for an image restore action**

The following event is sent when an archived image is restored. The
`target-storage-class` field will be set to `STANDARD`.
The event includes a `last-activated-at` field showing when the image
was last restored.

```
{
    "version": "0",
    "id": "7b8fc5e6-5ef5-8bbe-b157-EXAMPLE",
    "detail-type": "ECR Image Action",
    "source": "aws.ecr",
    "account": "`123456789012`",
    "time": "2019-08-06T01:15:22Z",
    "region": "`us-east-1`",
    "resources": [],
    "detail": {
        "action-type": "UPDATE_STORAGE_CLASS",
        "target-storage-class": "STANDARD",
        "image-digest": "`sha256:f98d67af8e53a536502bfc600de3266556b06ed635a32d60aa7a5fe6d7e609d7`",
        "repository-name": "`ubuntu`",
        "result": "SUCCESS",
        "manifest-media-type": "application/vnd.oci.image.manifest.v1+json",
        "artifact-media-type": "application/vnd.oci.image.config.v1+json",
        "last-activated-at": "2025-10-10T19:13:02.74Z"
    }
}
```

**Event for a referrer restore action**

The following event is sent when an archived referrer (reference artifact such as
an SBOM, signature, or attestation) is restored. Note that the
`detail-type` is `ECR Referrer Action` to distinguish it
from regular image actions. The `manifest-media-type` and
`artifact-media-type` fields identify the specific type of referrer
being restored. In this example, an SBOM artifact is being restored.

```
{
    "version": "0",
    "id": "8c9gd6f7-6fg6-9ccf-c268-EXAMPLE",
    "detail-type": "ECR Referrer Action",
    "source": "aws.ecr",
    "account": "`123456789012`",
    "time": "2019-08-06T01:20:45Z",
    "region": "`us-east-1`",
    "resources": [],
    "detail": {
        "action-type": "UPDATE_STORAGE_CLASS",
        "target-storage-class": "STANDARD",
        "image-digest": "`sha256:f98d67af8e53a536502bfc600de3266556b06ed635a32d60aa7a5fe6d7e609d7`",
        "repository-name": "`sbom`",
        "result": "SUCCESS",
        "manifest-media-type": "application/vnd.cncf.oras.artifact.manifest.v1+json",
        "artifact-media-type": "text/sbom+json",
        "last-activated-at": "2025-10-10T19:13:02.74Z"
    }
}
```

**Event for a completed image replication**

The following event is sent when each image replication is completed. For more
information, see [Private image replication in Amazon ECR](replication.md "replication.md").

```
{
  "version": "0",
  "id": "c8b133b1-6029-ee73-e2a1-4f466b8ba999",
  "detail-type": "ECR Replication Action",
  "source": "aws.ecr",
  "account": "`123456789012`",
  "time": "2024-05-08T20:44:54Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ecr:`us-east-1`:`123456789012`:repository/docker-hub/alpine"
  ],
  "detail": {
    "result": "SUCCESS",
    "repository-name": "`docker-hub/alpine`",
    "image-digest": "`sha256:7f5b2640fe6fb4f46592dfd3410c4a79dac4f89e4782432e0378abcd1234`",
    "source-account": "`123456789012`",
    "action-type": "REPLICATE",
    "source-region": "`us-west-2`",
    "image-tag": "3.17.2"
  }
}
```

**Event for a failed image replication**

The following event is sent when an image replication fails. The
`result` field will contain `FAILED` and additional error
information may be included in the event details.

```
{
  "version": "0",
  "id": "d9c244c2-7130-ff84-f3b2-5g577c9cb000",
  "detail-type": "ECR Replication Action",
  "source": "aws.ecr",
  "account": "`123456789012`",
  "time": "2024-05-08T20:45:12Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ecr:`us-east-1`:`123456789012`:repository/my-app"
  ],
  "detail": {
    "result": "FAILED",
    "repository-name": "`my-app`",
    "image-digest": "`sha256:8g6c3751gf7gc5g47603ege4511d5a80ead5g90f5893543f1489bde2345`",
    "source-account": "`123456789012`",
    "action-type": "REPLICATE",
    "source-region": "`us-west-2`",
    "image-tag": "latest"
  }
}
```
