

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshooting EKS Capabilities
<a name="capabilities-troubleshooting"></a>

**Note**  
EKS Capabilities are fully managed and run outside your cluster. You do not have direct access to controller namespaces. Troubleshooting focuses on capability health, resource status, configuration, and controller logs. You can configure controller log delivery to gain visibility into controller behavior. See [Access EKS Capabilities controller logs](capabilities-controller-logs.md).

## General troubleshooting approach
<a name="_general_troubleshooting_approach"></a>

When troubleshooting EKS Capabilities, follow this general approach:

1.  **Check capability health**: Use `aws eks describe-capability` to view the capability status and health issues

1.  **Verify resource status**: Check the Kubernetes resources (CRDs) you created for status conditions and events

1.  **Review controller logs**: If log delivery is configured, query controller logs for errors and reconciliation details

1.  **Review IAM permissions**: Ensure the Capability Role has the necessary permissions

1.  **Check configuration**: Verify capability-specific configuration is correct

## Use controller logs for troubleshooting
<a name="_use_controller_logs_for_troubleshooting"></a>

If you have configured controller log delivery (see [Access EKS Capabilities controller logs](capabilities-controller-logs.md)), you can query logs to identify reconciliation errors, resource conflicts, and configuration issues.

### Query errors across all controllers
<a name="_query_errors_across_all_controllers"></a>

```
fields @timestamp, controller, message, error
| filter level = "error"
| sort @timestamp desc
| limit 50
```

### Filter logs for a specific ACK service controller
<a name="_filter_logs_for_a_specific_ack_service_controller"></a>

Use the `controllerGroup` field to isolate logs from a specific ACK service controller:

```
fields @timestamp, message, error
| filter controllerGroup = "s3.services.k8s.aws"
| filter level = "error"
| sort @timestamp desc
```

To filter further by resource kind (for example, only `SecurityGroup` logs from the EC2 controller):

```
fields @timestamp, message, error
| filter controllerGroup = "ec2.services.k8s.aws"
| filter controllerKind = "SecurityGroup"
| sort @timestamp desc
| limit 100
```

### Filter logs for a specific Argo CD application
<a name="_filter_logs_for_a_specific_argo_cd_application"></a>

Use the `application` field to isolate logs for a particular Argo CD application:

```
fields @timestamp, message, error
| filter application = "my-application"
| sort @timestamp desc
| limit 100
```

### Track reconciliation for a specific resource
<a name="_track_reconciliation_for_a_specific_resource"></a>

Use the `reconcileID` field to follow a single reconciliation cycle:

```
fields @timestamp, level, message, error
| filter reconcileID = "your-reconcile-id"
| sort @timestamp asc
```

### Common log patterns indicating issues
<a name="_common_log_patterns_indicating_issues"></a>
+  **Repeated reconciliation errors** — The controller is unable to reach the desired state for a resource. Check the `error` field for details such as IAM permission failures or invalid resource configurations.
+  **"Reconciler error" with AWS API errors** — The Capability Role may be missing permissions for the specific AWS service operation. Review the error message and update IAM policies accordingly.
+  **No log entries for a resource** — If you don’t see logs for a resource you expect the controller to reconcile, verify the capability is `ACTIVE` and that the resource exists in a namespace the capability can access.

## Check capability health
<a name="_check_capability_health"></a>

All EKS Capabilities provide health information through the EKS console and the `describe-capability` API.

 **Console**:

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home\#/clusters.

1. Select your cluster name.

1. Choose the **Observability** tab.

1. Choose **Monitor cluster**.

1. Choose the **Capabilities** tab to view health and status for all capabilities.

The Capabilities tab shows:
+ Capability name and type
+ Current status
+ Health issues, with description

 ** AWS CLI**:

```
aws eks describe-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-capability-name}}
```

The response includes:
+  **status**: Current capability state (`CREATING`, `ACTIVE`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`)
+  **health**: Health information including any issues detected by the capability

## Common capability statuses
<a name="_common_capability_statuses"></a>

 **CREATING**: Capability is being set up.

 **ACTIVE**: Capability is running and ready to use. If resources are not working as expected, check resource status and IAM permissions.

 **UPDATING**: Configuration changes are being applied. Wait for the status to return to `ACTIVE`.

 **CREATE\_FAILED** or **UPDATE\_FAILED**: Setup or update encountered an error. Check the health section for details. Common causes:
+ IAM role trust policy incorrect or missing
+ IAM role does not exist or is not accessible
+ Cluster access issues
+ Invalid configuration parameters

## Verify Kubernetes resource status
<a name="_verify_kubernetes_resource_status"></a>

EKS Capabilities create and manage Kubernetes Custom Resource Definitions (CRDs) in your cluster. When troubleshooting, check the status of the resources you created:

```
# List resources of a specific type
kubectl get {{resource-kind}} -A

# Describe a specific resource to see conditions and events
kubectl describe {{resource-kind resource-name}} -n {{namespace}}

# View resource status conditions
kubectl get {{resource-kind resource-name}} -n {{namespace}} -o jsonpath='{.status.conditions}'

# View events related to the resource
kubectl get events --field-selector involvedObject.name={{resource-name}} -n {{namespace}}
```

Resource status conditions provide information about:
+ Whether the resource is ready
+ Any errors encountered
+ Current reconciliation state

## Review IAM permissions and cluster access
<a name="_review_iam_permissions_and_cluster_access"></a>

Many capability issues stem from IAM permission problems or missing cluster access configuration. Verify both the Capability Role permissions and cluster access entries.

### Check IAM role permissions
<a name="_check_iam_role_permissions"></a>

Verify the Capability Role has the necessary permissions:

```
# List attached managed policies
aws iam list-attached-role-policies --role-name {{my-capability-role}}

# List inline policies
aws iam list-role-policies --role-name {{my-capability-role}}

# Get specific policy details
aws iam get-role-policy --role-name {{my-capability-role}} --policy-name {{policy-name}}

# View the role's trust policy
aws iam get-role --role-name {{my-capability-role}} --query 'Role.AssumeRolePolicyDocument'
```

The trust policy must allow the `capabilities.eks.amazonaws.com` service principal:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "capabilities.eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Check EKS Access Entries and Access Policies
<a name="_check_eks_access_entries_and_access_policies"></a>

All capabilities require proper EKS Access Entries and Access Policies on the cluster where they operate.

 **Verify Access Entry exists**:

```
aws eks list-access-entries \
  --cluster-name {{my-cluster}} \
  --region {{region-code}}
```

Look for the Capability Role ARN in the list. If missing, the capability cannot access the cluster.

 **Check Access Policies attached to the entry**:

```
aws eks list-associated-access-policies \
  --cluster-name {{my-cluster}} \
  --principal-arn {{arn:aws:iam::111122223333:role/my-capability-role}} \
  --region {{region-code}}
```

All capabilities require appropriate Access Policies:
+  **ACK**: Needs permissions to create and manage Kubernetes resources
+  **kro**: Needs permissions to create and manage Kubernetes resources
+  **Argo CD**: Needs permissions to create and manage Applications, and requires Access Entries on remote target clusters for multi-cluster deployments

 **For Argo CD multi-cluster deployments**:

If deploying to remote clusters, verify the Capability Role has an Access Entry on each target cluster:

```
# Check Access Entry on target cluster
aws eks describe-access-entry \
  --cluster-name {{target-cluster}} \
  --principal-arn {{arn:aws:iam::111122223333:role/argocd-capability-role}} \
  --region {{region-code}}
```

If the Access Entry is missing on a target cluster, Argo CD cannot deploy applications to it. See [Register target clusters](argocd-register-clusters.md) for configuration details.

## Capability-specific troubleshooting
<a name="_capability_specific_troubleshooting"></a>

For detailed troubleshooting guidance specific to each capability type:
+  [Troubleshoot issues with ACK capabilities](ack-troubleshooting.md) - Troubleshoot ACK resource creation, IAM permissions, and cross-account access
+  [Troubleshoot issues with Argo CD capabilities](argocd-troubleshooting.md) - Troubleshoot application sync, repository authentication, and multi-cluster deployments
+  [Troubleshoot issues with kro capabilities](kro-troubleshooting.md) - Troubleshoot ResourceGraphDefinitions, CEL expressions, and RBAC permissions

## Common issues across all capabilities
<a name="_common_issues_across_all_capabilities"></a>

### Capability stuck in CREATING state
<a name="_capability_stuck_in_creating_state"></a>

If a capability remains in `CREATING` state for longer than expected:

1. Check the capability health for specific issues in the console (**Observability** > **Monitor cluster** > **Capabilities** tab) or using the AWS CLI:

   ```
   aws eks describe-capability \
     --region {{region-code}} \
     --cluster-name {{my-cluster}} \
     --capability-name {{my-capability-name}} \
     --query 'capability.health'
   ```

1. Verify the IAM role exists and has the correct trust policy

1. Ensure your cluster is accessible and healthy

1. Check for any cluster-level issues that might prevent capability setup

### Resources not being created or updated
<a name="_resources_not_being_created_or_updated"></a>

If the capability is `ACTIVE` but resources are not being created or updated:

1. Check the resource status for error conditions

1. Verify IAM permissions for the specific AWS services (ACK) or repositories (Argo CD)

1. Check RBAC permissions for creating underlying resources (kro)

1. Review resource specifications for validation errors

### Capability health shows issues
<a name="_capability_health_shows_issues"></a>

If `describe-capability` shows health issues:

1. Read the issue descriptions carefully—they often indicate the specific problem

1. Address the root cause (IAM permissions, configuration errors, etc.)

1. The capability will automatically recover once the issue is resolved

## Next steps
<a name="_next_steps"></a>
+  [Working with capability resources](working-with-capabilities.md) - Manage capability resources
+  [Troubleshoot issues with ACK capabilities](ack-troubleshooting.md) - ACK-specific troubleshooting
+  [Troubleshoot issues with Argo CD capabilities](argocd-troubleshooting.md) - Argo CD-specific troubleshooting
+  [Troubleshoot issues with kro capabilities](kro-troubleshooting.md) - kro-specific troubleshooting
+  [Security considerations for EKS Capabilities](capabilities-security.md) - Security best practices for capabilities