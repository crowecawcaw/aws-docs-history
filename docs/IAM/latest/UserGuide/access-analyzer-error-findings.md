# IAM Access Analyzer error findings

When IAM Access Analyzer analyzes resources, it typically generates findings that show who has
access to your resources. However, in some cases, the analyzer might encounter issues that
prevent it from completing the analysis. In these situations, IAM Access Analyzer generates error
findings instead.

Error findings indicate that IAM Access Analyzer couldn't complete the analysis for a specific
resource or for a specific principal-resource pair. These findings help you identify resources
that might need attention to ensure proper analysis.

## External access error

findings

External access analyzers, which identify resources shared outside your account or
organization, can generate two types of error findings:

- INTERNAL_ERROR – Indicates that IAM Access Analyzer encountered an internal issue
  while analyzing the resource. This could be due to service limitations or temporary
  issues.

```
{
	"findingDetails": [
		{
			"externalAccessDetails": {}
		}
	],
	"resource": "arn:aws:iam::941407043048:role/TestAccessAnalyzer",
	"status": "ACTIVE",
	"error": "INTERNAL_ERROR",
	"createdAt": "2022-07-14T01:31:43.085000+00:00",
	"resourceType": "AWS::IAM::Role",
	"findingType": "ExternalAccess",
	"resourceOwnerAccount": "941407043048",
	"analyzedAt": "2025-03-19T06:51:46.109000+00:00",
	"id": "4b035c7d-b7d2-40e4-a6c3-9887d1a995df",
	"updatedAt": "2022-07-14T01:31:43.085000+00:00"
}
```

- ACCESS_DENIED – Indicates that IAM Access Analyzer doesn't have the required
  permissions to analyze the resource. This typically happens when the service-linked role
  (SLR) for IAM Access Analyzer is denied access to the resource.

```
{
	"findingDetails": [
		{
			"externalAccessDetails": {}
		}
	],
	"resource": "arn:aws:kms:us-west-2:941407043048:key/01cae123-b7f2-4488-9a05-0070a072ea2c",
	"status": "ACTIVE",
	"error": "ACCESS_DENIED",
	"createdAt": "2022-07-14T01:31:43.104000+00:00",
	"resourceType": "AWS::KMS::Key",
	"findingType": "ExternalAccess",
	"resourceOwnerAccount": "941407043048",
	"analyzedAt": "2025-03-19T06:51:46.090000+00:00",
	"id": "7ef6f04a-9d2c-4038-9cc0-2a5f00a4d8f8",
	"updatedAt": "2022-07-14T01:31:43.104000+00:00"
}
```

## Internal access error

findings

Internal access analyzers, which identify access within your account or organization, can
generate four types of error findings:

- PRINCIPAL_LIMIT_EXCEEDED – Generated when more than 3,000 principals have
  access to a critical resource. This error helps you identify resources with overly broad
  access that might need to be restricted.

If you make changes to the resource or principals in your environment that bring the
number of principals below the limit, the analyzer will generate normal findings during
the next scan, and the error finding will be marked as resolved.

```
{
	"id": "efec28fe-b304-412f-af0f-704d0d70c79c",
	"status": "ACTIVE",
	"error": "PRINCIPAL_LIMIT_EXCEEDED",
	"resource": "arn:aws:s3:::critical-data",
	"resourceType": "AWS::S3::Bucket",
	"resourceOwnerAccount": "111122223333",
	"createdAt": "2023-11-30T00:56:56.437000+00:00",
	"analyzedAt": "2024-03-06T04:11:54.406000+00:00",
	"updatedAt": "2023-11-30T00:56:56.437000+00:00",
	"findingType": "InternalAccess",
	"findingDetails": [
		{
			"internalAccessDetails": {}
		}
	]
}
```

- Resource-level errors (INTERNAL_ERROR or ACCESS_DENIED) – Similar to external
  access errors, these indicate that the analyzer couldn't analyze a specific resource due
  to internal issues or permission problems. When a resource-level error occurs, the
  analyzer generates a single error finding for the resource instead of normal
  findings.

```
{
	"id": "efec28fe-b304-412f-af0f-704d0d70c79c",
	"status": "ACTIVE",
	"error": "INTERNAL_ERROR", // can be INTERNAL_ERROR or ACCESS_DENIED
	"resource": "arn:aws:s3:::critical-data",
	"resourceType": "AWS::S3::Bucket",
	"resourceOwnerAccount": "111122223333",
	"createdAt": "2023-11-30T00:56:56.437000+00:00",
	"analyzedAt": "2024-03-06T04:11:54.406000+00:00",
	"updatedAt": "2023-11-30T00:56:56.437000+00:00",
	"findingType": "InternalAccess",
	"findingDetails": [
		{
			"internalAccessDetails": {}
		}
	]
}
```

- Principal-level errors (INTERNAL_ERROR or ACCESS_DENIED) – Indicates that the
  analyzer couldn't analyze access for a specific principal to a specific resource. Unlike
  resource-level errors, a resource can have both normal findings for some principals and
  error findings for other principals.

```
{
	"id": "efec28fe-b304-412f-af0f-704d0d70c79c",
	"status": "ACTIVE",
	"error": "INTERNAL_ERROR", // can be INTERNAL_ERROR or ACCESS_DENIED
	"resource": "arn:aws:s3:::critical-data",
	"resourceType": "AWS::S3::Bucket",
	"resourceOwnerAccount": "111122223333",
	"createdAt": "2023-11-30T00:56:56.437000+00:00",
	"analyzedAt": "2024-03-06T04:11:54.406000+00:00",
	"updatedAt": "2023-11-30T00:56:56.437000+00:00",
	"findingType": "InternalAccess",
	"findingDetails": [
		{
			"internalAccessDetails": {
				"principal": {
					"AWS": "arn:aws:iam::111122223333:role/MyRole_1"
				},
				"principalOwnerAccount": "111122223333",
				"principalType": "IAM_ROLE",
				"accessType": "INTRA_ACCOUNT"
			}
		}
	]
}
```

- PRINCIPAL_ERRORS_LIMIT_EXCEEDED – Generated when there are too many principal-level
  error findings for a single resource. This is a resource-level error finding that may
  appear alongside normal findings for the same resource.

```
{
	"id": "efec28fe-b304-412f-af0f-704d0d70c79c",
	"status": "ACTIVE",
	"error": "PRINCIPAL_ERRORS_LIMIT_EXCEEDED",
	"resource": "arn:aws:s3:::critical-data",
	"resourceType": "AWS::S3::Bucket",
	"resourceOwnerAccount": "111122223333",
	"createdAt": "2023-11-30T00:56:56.437000+00:00",
	"analyzedAt": "2024-03-06T04:11:54.406000+00:00",
	"updatedAt": "2023-11-30T00:56:56.437000+00:00",
	"findingType": "InternalAccess",
	"resourceControlPolicyRestriction": "NOT_APPLICABLE",
	"serviceControlPolicyRestriction": "NOT_APPLICABLE",
	"findingDetails": [
		{
			"internalAccessDetails": {}
		}
	]
}
```

## Resolving error findings

If you resolve the issue that prevented IAM Access Analyzer from analyzing the resource, the
error finding will be removed completely instead of changing to a resolved finding.

To resolve error findings, consider the following approaches based on the error
type:

- For ACCESS_DENIED errors, verify that the IAM Access Analyzer service-linked role has the
  necessary permissions to access the resource.
- For PRINCIPAL_LIMIT_EXCEEDED errors, review the resource's access policies and
  consider restricting access to fewer principals.
- For INTERNAL_ERROR findings, you may need to wait for a subsequent analysis cycle or
  contact AWS support if the issue persists.
- For PRINCIPAL_ERRORS_LIMIT_EXCEEDED, review and potentially simplify the access patterns for
  the affected resource.

After making changes to address the underlying issues, IAM Access Analyzer will attempt to
analyze the resources again during its next scan cycle.
