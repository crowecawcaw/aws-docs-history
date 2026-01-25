**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# ACK concepts

ACK manages AWS resources through Kubernetes APIs by continuously reconciling the desired state in your manifests with the actual state in AWS.
When you create or update a Kubernetes custom resource, ACK makes the necessary AWS API calls to create or modify the corresponding AWS resource, then monitors it for drift and updates the Kubernetes status to reflect the current state.
This approach lets you manage infrastructure using familiar Kubernetes tools and workflows while maintaining consistency between your cluster and AWS.

This topic explains the fundamental concepts behind how ACK manages AWS resources through Kubernetes APIs.

## Getting started with ACK

After creating the ACK capability (see [Create an ACK capability](create-ack-capability.md "create-ack-capability.md")), you can start managing AWS resources using Kubernetes manifests in your cluster.

As an example, create this S3 bucket manifest in `bucket.yaml`, choosing your own unique bucket name.

```
apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: my-test-bucket
  namespace: default
spec:
  name: `my-unique-bucket-name-12345`

```

Apply the manifest:

```
kubectl apply -f bucket.yaml
```

Check the status:

```
kubectl get bucket my-test-bucket
kubectl describe bucket my-test-bucket
```

Verify the bucket was created in AWS:

```
aws s3 ls | grep `my-unique-bucket-name-12345`

```

Delete the Kubernetes resource:

```
kubectl delete bucket my-test-bucket
```

Verify the bucket was deleted from AWS:

```
aws s3 ls | grep `my-unique-bucket-name-12345`

```

The bucket should no longer appear in the list, demonstrating that ACK manages the full lifecycle of AWS resources.

For more information on getting started with ACK, see [Getting Started with ACK](https://aws-controllers-k8s.github.io/community/docs/user-docs/getting-started/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/getting-started/").

## Resource lifecycle and reconciliation

ACK uses a continuous reconciliation loop to ensure your AWS resources match the desired state defined in your Kubernetes manifests.

**How reconciliation works**:

1. You create or update a Kubernetes custom resource (for example, an S3 Bucket)
2. ACK detects the change and compares the desired state with the actual state in AWS
3. If they differ, ACK makes AWS API calls to reconcile the difference
4. ACK updates the resource status in Kubernetes to reflect the current state
5. The loop repeats continuously, typically every few hours

Reconciliation is triggered when you create a new Kubernetes resource, update an existing resource’s `spec`, or when ACK detects drift in AWS from manual changes made outside ACK.
Additionally, ACK performs periodic reconciliation with a resync period of 10 hours.
Changes to Kubernetes resources trigger immediate reconciliation, while passive drift detection of upstream AWS resource changes occurs during the periodic resync.

When working through the getting started example above, ACK performs these steps:

1. Checks if bucket exists in AWS
2. If not, calls `s3:CreateBucket`
3. Updates Kubernetes status with bucket ARN and state
4. Continues monitoring for drift

To learn more about how ACK works, see [ACK Reconciliation](https://aws-controllers-k8s.github.io/community/docs/user-docs/reconciliation/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/reconciliation/").

## Status conditions

ACK resources use status conditions to communicate their state.
Understanding these conditions helps you troubleshoot issues and understand resource health.

- **Ready**: Indicates the resource is ready to be consumed (standardized Kubernetes condition).
- **ACK.ResourceSynced**: Indicates the resource spec matches the AWS resource state.
- **ACK.Terminal**: Indicates an unrecoverable error has occurred.
- **ACK.Adopted**: Indicates the resource was adopted from an existing AWS resource rather than created new.
- **ACK.Recoverable**: Indicates a recoverable error that may resolve without updating the spec.
- **ACK.Advisory**: Provides advisory information about the resource.
- **ACK.LateInitialized**: Indicates whether late initialization of fields is complete.
- **ACK.ReferencesResolved**: Indicates whether all `AWSResourceReference` fields have been resolved.
- **ACK.IAMRoleSelected**: Indicates whether an IAMRoleSelector has been selected to manage this resource.

Check resource status:

```
# Check if resource is ready
kubectl get bucket my-bucket -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}'

# Check for terminal errors
kubectl get bucket my-bucket -o jsonpath='{.status.conditions[?(@.type=="ACK.Terminal")]}'
```

Example status:

```
status:
  conditions:
  - type: Ready
    status: "True"
    lastTransitionTime: "2024-01-15T10:30:00Z"
  - type: ACK.ResourceSynced
    status: "True"
    lastTransitionTime: "2024-01-15T10:30:00Z"
  - type: ACK.Terminal
    status: "True"
  ackResourceMetadata:
    arn: arn:aws:s3:::my-unique-bucket-name
    ownerAccountID: "111122223333"
    region: us-west-2
```

To learn more about ACK status and conditions, see [ACK Conditions](https://aws-controllers-k8s.github.io/community/docs/user-docs/conditions/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/conditions/").

## Deletion policies

ACK’s deletion policy controls what happens to AWS resources when you delete the Kubernetes resource.

**Delete (default)**

The AWS resource is deleted when you delete the Kubernetes resource:
This is the default behavior.

```
# No annotation needed - this is the default
apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: temp-bucket
spec:
  name: temporary-bucket
```

Deleting this resource deletes the S3 bucket in AWS.

**Retain**

The AWS resource is kept when you delete the Kubernetes resource:

```
apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: important-bucket
  annotations:
    services.k8s.aws/deletion-policy: "retain"
spec:
  name: production-data-bucket
```

Deleting this resource removes it from Kubernetes but leaves the S3 bucket in AWS.

The `retain` policy is useful for production databases that should outlive the Kubernetes resource, shared resources used by multiple applications, resources with important data that shouldn’t be accidentally deleted, or temporary ACK management where you adopt a resource, configure it, then release it back to manual management.

To learn more about ACK deletion policy, see [ACK Deletion Policy](https://aws-controllers-k8s.github.io/community/docs/user-docs/deletion-policy/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/deletion-policy/").

## Resource adoption

Adoption allows you to bring existing AWS resources under ACK management without recreating them.

When to use adoption:

- Migrating existing infrastructure to ACK management
- Recovering orphaned AWS resources in case of accidental resource deletion in Kubernetes
- Importing resources created by other tools (CloudFormation, Terraform)

How adoption works:

```
apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: existing-bucket
  annotations:
    services.k8s.aws/adoption-policy: "adopt-or-create"
spec:
  name: my-existing-bucket-name
```

When you create this resource:

1. ACK checks if a bucket with that name exists in AWS
2. If found, ACK adopts it (no API calls to create)
3. ACK reads the current configuration from AWS
4. ACK updates the Kubernetes status to reflect the actual state
5. Future updates reconcile the resource normally

Once adopted, resources are managed like any other ACK resource, and deleting the Kubernetes resource will delete the AWS resource unless you use the `retain` deletion policy.

When adopting resources, the AWS resource must already exist and ACK needs read permissions to discover it.
The `adopt-or-create` policy adopts the resource if it exists, or creates it if it doesn’t.
This is useful when you want a declarative workflow that works whether the resource exists or not.

To learn more about ACK resource adoption, see [ACK Resource Adoption](https://aws-controllers-k8s.github.io/community/docs/user-docs/adopted-resource/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/adopted-resource/").

## Cross-account and cross-region resources

ACK can manage resources in different AWS accounts and regions from a single cluster.

**Cross-region resource annotations**

You can specify the region of an AWS resource using an annotation:

```
apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: eu-bucket
  annotations:
    services.k8s.aws/region: eu-west-1
spec:
  name: my-eu-bucket
```

You can also specify the region of all AWS resources created in a given namespace:

**Namespace annotations**

Set a default region for all resources in a namespace:

```
apiVersion: v1
kind: Namespace
metadata:
  name: production
  annotations:
    services.k8s.aws/default-region: us-west-2
```

Resources created in this namespace use this region unless overridden with a resource-level annotation.

**Cross-account**

Use IAM Role Selectors to map specific IAM roles to namespaces:

```
apiVersion: services.k8s.aws/v1alpha1
kind: IAMRoleSelector
metadata:
  name: target-account-config
spec:
  arn: arn:aws:iam::444455556666:role/ACKTargetAccountRole
  namespaceSelector:
    names:
      - production
```

Resources created in the mapped namespace automatically use the specified role.

To learn more about IAM Role Selectors, see [ACK Cross-Account Resource Management](https://aws-controllers-k8s.github.io/docs/guides/cross-account "https://aws-controllers-k8s.github.io/docs/guides/cross-account").
For cross-account configuration details, see [Configure ACK permissions](ack-permissions.md "ack-permissions.md").

## Error handling and retry behavior

ACK automatically handles transient errors and retries failed operations.

Retry strategy:

- Transient errors (rate limiting, temporary service issues, insufficient permissions) trigger automatic retries
- Exponential backoff prevents overwhelming AWS APIs
- Maximum retry attempts vary by error type
- Permanent errors (invalid parameters, resource name conflicts) don’t retry

Check resource status for error details using `kubectl describe`:

```
kubectl describe bucket my-bucket
```

Look for status conditions with error messages, events showing recent reconciliation attempts, and the `message` field in status conditions explaining failures.
Common errors include insufficient IAM permissions, resource name conflicts in AWS, invalid configuration values in the `spec`, and exceeded AWS service quotas.

For troubleshooting common errors, see [Troubleshoot issues with ACK capabilities](ack-troubleshooting.md "ack-troubleshooting.md").

## Resource composition with kro

For composing and connecting multiple ACK resources together, use the EKS Capability for kro (Kube Resource Orchestrator).
kro provides a declarative way to define groups of resources, passing configuration between resources to manage complex infrastructure patterns simply.

For detailed examples of creating custom resource compositions with ACK resources, see [kro concepts](kro-concepts.md "kro-concepts.md")

## Next steps

- [ACK considerations for EKS](ack-considerations.md "ack-considerations.md") - EKS-specific patterns and integration strategies
