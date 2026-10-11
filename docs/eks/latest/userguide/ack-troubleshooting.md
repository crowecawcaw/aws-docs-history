

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshoot issues with ACK capabilities
<a name="ack-troubleshooting"></a>

**Note**  
EKS Capabilities are fully managed and run outside your cluster. You do not have direct access to controller namespaces. You can configure controller log delivery for visibility into controller behavior. See [Access EKS Capabilities controller logs](capabilities-controller-logs.md). Troubleshooting focuses on capability health, resource status, and IAM configuration.

## Capability is ACTIVE but resources are not being created
<a name="_capability_is_active_but_resources_are_not_being_created"></a>

If your ACK capability shows `ACTIVE` status but resources are not being created in AWS, check the capability health, resource status, and IAM permissions.

 **Check capability health**:

You can view capability health and status issues in the EKS console or using the AWS CLI.

 **Console**:

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home\#/clusters.

1. Select your cluster name.

1. In the left navigation pane, choose **Cluster monitoring**.

1. Choose the **Capabilities** tab to view health and status for all capabilities.

 ** AWS CLI**:

```
# View capability status and health
aws eks describe-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-ack}}

# Look for issues in the health section
```

 **Common causes**:
+  **IAM permissions missing**: The Capability Role lacks permissions for the AWS service
+  **Wrong namespace**: Resources created in namespace without proper IAMRoleSelector
+  **Invalid resource spec**: Check resource status conditions for validation errors
+  **API throttling**: AWS API rate limits being hit
+  **Admission webhooks**: Admission webhooks blocking the controller from patching resource status

 **Check resource status**:

```
# Describe the resource to see conditions and events
kubectl describe bucket {{my-bucket}} -n default

# Look for status conditions
kubectl get bucket {{my-bucket}} -n default -o jsonpath='{.status.conditions}'

# View resource events
kubectl get events --field-selector involvedObject.name={{my-bucket}} -n default
```

 **Verify IAM permissions**:

```
# View the Capability Role's policies
aws iam list-attached-role-policies --role-name {{my-ack-capability-role}}
aws iam list-role-policies --role-name {{my-ack-capability-role}}

# Get specific policy details
aws iam get-role-policy --role-name {{my-ack-capability-role}} --policy-name {{policy-name}}
```

## Resources created in AWS but not showing in Kubernetes
<a name="resources_created_in_shared_aws_but_not_showing_in_kubernetes"></a>

ACK only tracks resources it creates through Kubernetes manifests. To manage existing AWS resources with ACK, use the adoption feature.

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

For more on resource adoption, see [ACK concepts](ack-concepts.md).

## Cross-account resources not being created
<a name="_cross_account_resources_not_being_created"></a>

If resources are not being created in a target AWS account when using IAM Role Selectors, verify the trust relationship and IAMRoleSelector configuration.

 **Verify trust relationship**:

```
# Check the trust policy in the target account role
aws iam get-role --role-name {{cross-account-ack-role}} --query 'Role.AssumeRolePolicyDocument'
```

The trust policy must allow the source account’s Capability Role to assume it.

 **Confirm IAMRoleSelector configuration**:

```
# List IAMRoleSelectors (cluster-scoped)
kubectl get iamroleselector

# Describe specific selector
kubectl describe iamroleselector {{my-selector}}
```

 **Verify namespace alignment**:

IAMRoleSelectors are cluster-scoped resources but target specific namespaces. Ensure your ACK resources are in a namespace that matches the IAMRoleSelector’s namespace selector:

```
# Check resource namespace
kubectl get bucket {{my-cross-account-bucket}} -n {{production}}

# List all IAMRoleSelectors (cluster-scoped)
kubectl get iamroleselector

# Check which namespace the selector targets
kubectl get iamroleselector {{my-selector}} -o jsonpath='{.spec.namespaceSelector}'
```

 **Check IAMRoleSelected condition**:

Verify that the IAMRoleSelector was successfully matched to your resource by checking the `ACK.IAMRoleSelected` condition:

```
# Check if IAMRoleSelector was matched
kubectl get bucket {{my-cross-account-bucket}} -n {{production}} -o jsonpath='{.status.conditions[?(@.type=="ACK.IAMRoleSelected")]}'
```

If the condition is `False` or missing, the IAMRoleSelector’s namespace selector does not match the resource’s namespace. Verify the selector’s `namespaceSelector` matches your resource’s namespace labels.

 **Check Capability Role permissions**:

The Capability Role needs `sts:AssumeRole` and `sts:TagSession` permissions for the target account role:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["sts:AssumeRole", "sts:TagSession"],
      "Resource": {{"arn:aws:iam::444455556666:role/cross-account-ack-role"}}
    }
  ]
}
```

For detailed cross-account configuration, see [Configure ACK permissions](ack-permissions.md).

## Resource stuck in Terminating after a service was turned off
<a name="ack-stuck-deletion-disabled-service"></a>

If you delete a Kubernetes resource whose ACK service is listed in the capability’s `disabledServices`, the resource stays in the `Terminating` state and its AWS resource is never deleted. ACK adds a finalizer to every resource that it manages, named for the resource’s group and kind, such as `finalizers.s3.services.k8s.aws/Bucket`. The finalizer is removed only after a running controller deletes or releases the AWS resource. Because the controller for a turned-off service doesn’t run, nothing removes the finalizer, and the `services.k8s.aws/deletion-policy` annotation isn’t applied.

To confirm, check for a deletion timestamp and a remaining ACK finalizer:

```
kubectl get bucket {{my-bucket}} -n {{my-namespace}} \
  -o jsonpath='{.metadata.deletionTimestamp}{"\n"}{.metadata.finalizers}{"\n"}'
```

Then confirm that the service is turned off for the capability:

```
aws eks describe-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-ack}} \
  --query 'capability.configuration.ack.disabledServices'
```

To resolve this, re-enable the service so that its controller runs and completes the deletion. Remove the service from `disabledServices`, passing the complete list of services that you want to remain turned off. If this service was the only one turned off, specify an empty list. The following example re-enables `s3` while leaving `ec2` and `iam` turned off:

```
aws eks update-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-ack}} \
  --configuration '{"ack": {"disabledServices": ["ec2", "iam"]}}'
```

After the capability returns to `ACTIVE`, the controller processes the pending deletion and removes the finalizer.

**Warning**  
Removing the finalizer by hand deletes the Kubernetes resource but leaves the AWS resource in place, with no record of it in your cluster. Only do this if you intend to keep the AWS resource and manage it outside of ACK, or if you have already deleted it another way.  

```
kubectl patch bucket {{my-bucket}} -n {{my-namespace}} \
  --type merge -p '{"metadata":{"finalizers":[]}}'
```
This clears every finalizer on the resource. Confirm which finalizers are present before you run it, and be aware that clearing them also skips any cleanup that another controller’s finalizer would have performed.

To avoid this, re-enable a service before you delete its resources, or delete the resources before you turn the service off. For more information, see [ACK capability configuration options](create-ack-capability.md#ack-configuration-options).

## Next steps
<a name="_next_steps"></a>
+  [ACK considerations for EKS](ack-considerations.md) - ACK considerations and best practices
+  [Configure ACK permissions](ack-permissions.md) - Configure IAM permissions and multi-account patterns
+  [ACK concepts](ack-concepts.md) - Understand ACK concepts and resource lifecycle
+  [Troubleshooting EKS Capabilities](capabilities-troubleshooting.md) - General capability troubleshooting guidance