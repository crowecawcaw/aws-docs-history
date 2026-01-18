**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshoot issues with ACK capabilities

This topic provides troubleshooting guidance for the EKS Capability for ACK, including capability health checks, resource status verification, and IAM permission issues.

###### Note

EKS Capabilities are fully managed and run outside your cluster.
You don’t have access to controller logs or controller namespaces.
Troubleshooting focuses on capability health, resource status, and IAM configuration.

## Capability is ACTIVE but resources aren’t being created

If your ACK capability shows `ACTIVE` status but resources aren’t being created in AWS, check the capability health, resource status, and IAM permissions.

**Check capability health**:

You can view capability health and status issues in the EKS console or using the AWS CLI.

**Console**:

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home#/clusters.
2. Select your cluster name.
3. Choose the **Observability** tab.
4. Choose **Monitor cluster**.
5. Choose the **Capabilities** tab to view health and status for all capabilities.

**AWS CLI**:

```
 # View capability status and health
aws eks describe-capability \
  --region region-code \
  --cluster-name my-cluster \
  --capability-name my-ack

# Look for issues in the health section
```

**Common causes**:

- **IAM permissions missing**: The Capability Role lacks permissions for the AWS service
- **Wrong namespace**: Resources created in namespace without proper IAMRoleSelector
- **Invalid resource spec**: Check resource status conditions for validation errors
- **API throttling**: AWS API rate limits being hit
- **Admission webhooks**: Admission webhooks blocking the controller from patching resource status

**Check resource status**:

```
 # Describe the resource to see conditions and events
kubectl describe bucket my-bucket -n default

# Look for status conditions
kubectl get bucket my-bucket -n default -o jsonpath='{.status.conditions}'

# View resource events
kubectl get events --field-selector involvedObject.name=my-bucket -n default
```

**Verify IAM permissions**:

```
 # View the Capability Role's policies
aws iam list-attached-role-policies --role-name <replaceable>my-ack-capability-role</replaceable>
aws iam list-role-policies --role-name <replaceable>my-ack-capability-role</replaceable>

# Get specific policy details
aws iam get-role-policy --role-name <replaceable>my-ack-capability-role</replaceable> --policy-name <replaceable>policy-name</replaceable>
```

## Resources created in AWS but not showing in Kubernetes

ACK only tracks resources it creates through Kubernetes manifests.
To manage existing AWS resources with ACK, use the adoption feature.

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

For more on resource adoption, see [ACK concepts](ack-concepts.md "ack-concepts.md").

## Cross-account resources not being created

If resources aren’t being created in a target AWS account when using IAM Role Selectors, verify the trust relationship and IAMRoleSelector configuration.

**Verify trust relationship**:

```
 # Check the trust policy in the target account role
aws iam get-role --role-name <replaceable>cross-account-ack-role</replaceable> --query 'Role.AssumeRolePolicyDocument'
```

The trust policy must allow the source account’s Capability Role to assume it.

**Confirm IAMRoleSelector configuration**:

```
 # List IAMRoleSelectors (cluster-scoped)
kubectl get iamroleselector

# Describe specific selector
kubectl describe iamroleselector my-selector
```

**Verify namespace alignment**:

IAMRoleSelectors are cluster-scoped resources but target specific namespaces.
Ensure your ACK resources are in a namespace that matches the IAMRoleSelector’s namespace selector:

```
 # Check resource namespace
kubectl get bucket <replaceable>my-cross-account-bucket</replaceable> -n <replaceable>production</replaceable>

# List all IAMRoleSelectors (cluster-scoped)
kubectl get iamroleselector

# Check which namespace the selector targets
kubectl get iamroleselector <replaceable>my-selector</replaceable> -o jsonpath='{.spec.namespaceSelector}'
```

**Check IAMRoleSelected condition**:

Verify that the IAMRoleSelector was successfully matched to your resource by checking the `ACK.IAMRoleSelected` condition:

```
 # Check if IAMRoleSelector was matched
kubectl get bucket <replaceable>my-cross-account-bucket</replaceable> -n <replaceable>production</replaceable> -o jsonpath='{.status.conditions[?(@.type=="ACK.IAMRoleSelected")]}'
```

If the condition is `False` or missing, the IAMRoleSelector’s namespace selector doesn’t match the resource’s namespace.
Verify the selector’s `namespaceSelector` matches your resource’s namespace labels.

**Check Capability Role permissions**:

The Capability Role needs `sts:AssumeRole` permission for the target account role:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::[.replaceable]`444455556666`:role/[.replaceable]`cross-account-ack-role`"
    }
  ]
}
```

For detailed cross-account configuration, see [Configure ACK permissions](ack-permissions.md "ack-permissions.md").

## Next steps

- [ACK considerations for EKS](ack-considerations.md "ack-considerations.md") - ACK considerations and best practices
- [Configure ACK permissions](ack-permissions.md "ack-permissions.md") - Configure IAM permissions and multi-account patterns
- [ACK concepts](ack-concepts.md "ack-concepts.md") - Understand ACK concepts and resource lifecycle
- [Troubleshooting EKS Capabilities](capabilities-troubleshooting.md "capabilities-troubleshooting.md") - General capability troubleshooting guidance
