**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshooting EKS Capabilities

This topic provides general troubleshooting guidance for EKS Capabilities, including capability health checks, common issues, and links to capability-specific troubleshooting.

###### Note

EKS Capabilities are fully managed and run outside your cluster.
You don’t have access to controller logs or controller namespaces.
Troubleshooting focuses on capability health, resource status, and configuration.

## General troubleshooting approach

When troubleshooting EKS Capabilities, follow this general approach:

1. **Check capability health**: Use `aws eks describe-capability` to view the capability status and health issues
2. **Verify resource status**: Check the Kubernetes resources (CRDs) you created for status conditions and events
3. **Review IAM permissions**: Ensure the Capability Role has the necessary permissions
4. **Check configuration**: Verify capability-specific configuration is correct

## Check capability health

All EKS Capabilities provide health information through the EKS console and the `describe-capability` API.

**Console**:

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Select your cluster name.
3. Choose the **Observability** tab.
4. Choose **Monitor cluster**.
5. Choose the **Capabilities** tab to view health and status for all capabilities.

The Capabilities tab shows:

- Capability name and type
- Current status
- Health issues, with description

**AWS CLI**:

```
aws eks describe-capability \
  --region region-code \
  --cluster-name my-cluster \
  --capability-name my-capability-name
```

The response includes:

- **status**: Current capability state (`CREATING`, `ACTIVE`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`)
- **health**: Health information including any issues detected by the capability

## Common capability statuses

**CREATING**: Capability is being set up.

**ACTIVE**: Capability is running and ready to use. If resources aren’t working as expected, check resource status and IAM permissions.

**UPDATING**: Configuration changes are being applied. Wait for the status to return to `ACTIVE`.

**CREATE_FAILED** or **UPDATE_FAILED**: Setup or update encountered an error. Check the health section for details. Common causes:

- IAM role trust policy incorrect or missing
- IAM role doesn’t exist or isn’t accessible
- Cluster access issues
- Invalid configuration parameters

## Verify Kubernetes resource status

EKS Capabilities create and manage Kubernetes Custom Resource Definitions (CRDs) in your cluster.
When troubleshooting, check the status of the resources you created:

```
# List resources of a specific type
kubectl get `resource-kind` -A

# Describe a specific resource to see conditions and events
kubectl describe `resource-kind`
         `resource-name` -n `namespace`

# View resource status conditions
kubectl get `resource-kind`
         `resource-name` -n `namespace` -o jsonpath='{.status.conditions}'

# View events related to the resource
kubectl get events --field-selector involvedObject.name=`resource-name` -n `namespace`

```

Resource status conditions provide information about:

- Whether the resource is ready
- Any errors encountered
- Current reconciliation state

## Review IAM permissions and cluster access

Many capability issues stem from IAM permission problems or missing cluster access configuration. Verify both the Capability Role permissions and cluster access entries.

### Check IAM role permissions

Verify the Capability Role has the necessary permissions:

```
# List attached managed policies
aws iam list-attached-role-policies --role-name `my-capability-role`

# List inline policies
aws iam list-role-policies --role-name `my-capability-role`

# Get specific policy details
aws iam get-role-policy --role-name `my-capability-role` --policy-name `policy-name`

# View the role's trust policy
aws iam get-role --role-name `my-capability-role` --query 'Role.AssumeRolePolicyDocument'
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

All capabilities require proper EKS Access Entries and Access Policies on the cluster where they operate.

**Verify Access Entry exists**:

```
aws eks list-access-entries \
  --cluster-name `my-cluster` \
  --region `region-code`

```

Look for the Capability Role ARN in the list. If missing, the capability cannot access the cluster.

**Check Access Policies attached to the entry**:

```
aws eks list-associated-access-policies \
  --cluster-name `my-cluster` \
  --principal-arn `arn:aws:iam::111122223333:role/my-capability-role` \
  --region `region-code`

```

All capabilities require appropriate Access Policies:

- **ACK**: Needs permissions to create and manage Kubernetes resources
- **kro**: Needs permissions to create and manage Kubernetes resources
- **Argo CD**: Needs permissions to create and manage Applications, and requires Access Entries on remote target clusters for multi-cluster deployments

**For Argo CD multi-cluster deployments**:

If deploying to remote clusters, verify the Capability Role has an Access Entry on each target cluster:

```
# Check Access Entry on target cluster
aws eks describe-access-entry \
  --cluster-name `target-cluster` \
  --principal-arn `arn:aws:iam::111122223333:role/argocd-capability-role` \
  --region `region-code`

```

If the Access Entry is missing on a target cluster, Argo CD cannot deploy applications to it.
See [Register target clusters](argocd-register-clusters.md "argocd-register-clusters.md") for configuration details.

## Capability-specific troubleshooting

For detailed troubleshooting guidance specific to each capability type:

- [Troubleshoot issues with ACK capabilities](ack-troubleshooting.md "ack-troubleshooting.md") - Troubleshoot ACK resource creation, IAM permissions, and cross-account access
- [Troubleshoot issues with Argo CD capabilities](argocd-troubleshooting.md "argocd-troubleshooting.md") - Troubleshoot application sync, repository authentication, and multi-cluster deployments
- [Troubleshoot issues with kro capabilities](kro-troubleshooting.md "kro-troubleshooting.md") - Troubleshoot ResourceGraphDefinitions, CEL expressions, and RBAC permissions

## Common issues across all capabilities

### Capability stuck in CREATING state

If a capability remains in `CREATING` state for longer than expected:

1. Check the capability health for specific issues in the console (**Observability** > **Monitor cluster** > **Capabilities** tab) or using the AWS CLI:

```
aws eks describe-capability \
  --region region-code \
  --cluster-name my-cluster \
  --capability-name my-capability-name \
  --query 'capability.health'
```

2. Verify the IAM role exists and has the correct trust policy
3. Ensure your cluster is accessible and healthy
4. Check for any cluster-level issues that might prevent capability setup

### Resources not being created or updated

If the capability is `ACTIVE` but resources aren’t being created or updated:

1. Check the resource status for error conditions
2. Verify IAM permissions for the specific AWS services (ACK) or repositories (Argo CD)
3. Check RBAC permissions for creating underlying resources (kro)
4. Review resource specifications for validation errors

### Capability health shows issues

If `describe-capability` shows health issues:

1. Read the issue descriptions carefully—they often indicate the specific problem
2. Address the root cause (IAM permissions, configuration errors, etc.)
3. The capability will automatically recover once the issue is resolved

## Next steps

- [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md") - Manage capability resources
- [Troubleshoot issues with ACK capabilities](ack-troubleshooting.md "ack-troubleshooting.md") - ACK-specific troubleshooting
- [Troubleshoot issues with Argo CD capabilities](argocd-troubleshooting.md "argocd-troubleshooting.md") - Argo CD-specific troubleshooting
- [Troubleshoot issues with kro capabilities](kro-troubleshooting.md "kro-troubleshooting.md") - kro-specific troubleshooting
- [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md") - Security best practices for capabilities
