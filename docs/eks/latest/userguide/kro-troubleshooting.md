**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshoot issues with kro capabilities

This topic provides troubleshooting guidance for the EKS Capability for kro, including capability health checks, RBAC permissions, CEL expression errors, and resource composition issues.

###### Note

EKS Capabilities are fully managed and run outside your cluster.
You don’t have access to controller logs or the `kro-system` namespace.
Troubleshooting focuses on capability health, RBAC configuration, and resource status.

## Capability is ACTIVE but ResourceGraphDefinitions aren’t working

If your kro capability shows `ACTIVE` status but ResourceGraphDefinitions aren’t creating underlying resources, check the capability health, RBAC permissions, and resource status.

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
  --capability-name my-kro

# Look for issues in the health section
```

**Common causes**:

- **RBAC permissions missing**: kro lacks permissions to create underlying Kubernetes resources
- **Invalid CEL expressions**: Syntax errors in ResourceGraphDefinition
- **Resource dependencies**: Dependent resources not ready
- **Schema validation**: Instance doesn’t match RGD schema requirements

**Verify RBAC permissions**:

```
# Check if capability has cluster admin policy
kubectl get accessentry -A | grep kro
```

If the capability doesn’t have the required permissions, associate the `AmazonEKSClusterAdminPolicy` with the kro capability’s access entry, or create more restrictive RBAC policies for production use.
See [Configure kro permissions](kro-permissions.md "kro-permissions.md") for details.

**Check ResourceGraphDefinition status**:

```
# List all RGDs
kubectl get resourcegraphdefinition

# Describe specific RGD
kubectl describe resourcegraphdefinition my-rgd

# Check for validation errors
kubectl get resourcegraphdefinition my-rgd -o jsonpath='{.status.conditions}'
```

ResourceGraphDefinitions have three key status conditions:

- `ResourceGraphAccepted` - Whether the RGD passed validation (CEL syntax, type checking, field existence)
- `KindReady` - Whether the CRD for your custom API was generated and registered
- `ControllerReady` - Whether kro is actively watching for instances of your custom API

If `ResourceGraphAccepted` is `False`, check the condition message for validation errors like unknown fields, type mismatches, or circular dependencies.

## Instances created but underlying resources not appearing

If custom resource instances exist but the underlying Kubernetes resources (Deployments, Services, ConfigMaps) aren’t being created, verify kro has permissions and check for composition errors.

**Check instance status**:

```
# Describe the instance (replace with your custom resource kind and name)
kubectl describe `custom-kind`
         `my-instance`

# View instance events
kubectl get events --field-selector involvedObject.name=`my-instance`

# Check instance status conditions
kubectl get `custom-kind`
         `my-instance` -o jsonpath='{.status.conditions}'

# Check instance state
kubectl get `custom-kind`
         `my-instance` -o jsonpath='{.status.state}'
```

Instances have a `state` field showing high-level status:

- `ACTIVE` - Instance is successfully running
- `IN_PROGRESS` - Instance is being processed or reconciled
- `FAILED` - Instance failed to reconcile
- `DELETING` - Instance is being deleted
- `ERROR` - An error occurred during processing

Instances also have four status conditions:

- `InstanceManaged` - Finalizers and labels are properly set
- `GraphResolved` - Runtime graph created and resources resolved
- `ResourcesReady` - All resources created and ready
- `Ready` - Overall instance health (only becomes `True` when all sub-conditions are `True`)

Focus on the `Ready` condition to determine instance health.
If `Ready` is `False`, check the sub-conditions to identify which phase failed.

**Verify RBAC permissions**:

The kro capability needs permissions to create the underlying Kubernetes resources defined in your ResourceGraphDefinitions.

```
# Check if the capability has the AmazonEKSClusterAdminPolicy
kubectl get accessentry -A | grep kro
```

If permissions are missing, associate the `AmazonEKSClusterAdminPolicy` with the kro capability’s access entry, or create more restrictive RBAC policies for production use.
See [Configure kro permissions](kro-permissions.md "kro-permissions.md") for details.

## CEL expression errors

CEL expression errors are caught at ResourceGraphDefinition creation time, not when instances are created.
kro validates all CEL syntax, type-checks expressions against Kubernetes schemas, and verifies field existence when you create the RGD.

**Common CEL validation errors**:

- **Undefined field reference**: Referencing a field that doesn’t exist in the schema or resource
- **Type mismatch**: Expression returns wrong type (e.g., string where integer expected)
- **Invalid syntax**: Missing brackets, quotes, or operators in CEL expression
- **Unknown resource type**: Referencing a CRD that doesn’t exist in the cluster

**Check RGD validation status**:

```
# Check if RGD was accepted
kubectl get resourcegraphdefinition `my-rgd` -o jsonpath='{.status.conditions[?(@.type=="ResourceGraphAccepted")]}'

# View detailed validation errors
kubectl describe resourcegraphdefinition `my-rgd`

```

If `ResourceGraphAccepted` is `False`, the condition message contains the validation error.

**Example valid CEL expressions**:

```
# Reference schema field
${schema.spec.appName}

# Conditional expression
${schema.spec.replicas > 1}

# String template (expressions must return strings)
name: "${schema.spec.appName}-service"

# Standalone expression (can be any type)
replicas: ${schema.spec.replicaCount}

# Resource reference
${deployment.status.availableReplicas}

# Optional field access (returns null if field doesn't exist)
${configmap.data.?DATABASE_URL}
```

## Resource dependencies not resolving

kro automatically infers dependencies from CEL expressions and creates resources in the correct order.
If resources aren’t being created as expected, check the dependency order and resource readiness.

**View computed creation order**:

```
# See the order kro will create resources
kubectl get resourcegraphdefinition `my-rgd` -o jsonpath='{.status.topologicalOrder}'
```

This shows the computed order based on CEL expression references between resources.

**Check resource readiness**:

```
# View instance status to see which resources are ready
kubectl get `custom-kind`
         `my-instance` -o jsonpath='{.status}'

# Check specific resource status
kubectl get deployment `my-deployment` -o jsonpath='{.status.conditions}'
```

**Verify readyWhen conditions (if used)**:

The `readyWhen` field is optional.
If not specified, resources are considered ready immediately after creation.
If you’ve defined `readyWhen` conditions, verify they correctly check for resource readiness:

```
resources:
  - id: deployment
    readyWhen:
      - ${deployment.status.availableReplicas == deployment.spec.replicas}
```

**Check resource events**:

```
# View events for the underlying resources
kubectl get events -n `namespace` --sort-by='.lastTimestamp'
```

## Schema validation failures

If instances fail to create due to schema validation errors, verify the instance matches the RGD schema requirements.

**Check validation errors**:

```
# Attempt to create instance and view error
kubectl apply -f instance.yaml

# View existing instance validation status
kubectl describe `custom-kind`
         `my-instance` | grep -A 5 "Validation"
```

**Common validation issues**:

- **Required fields missing**: Instance doesn’t provide all required schema fields
- **Type mismatch**: Providing string where integer is expected
- **Invalid enum value**: Using value not in allowed list
- **Pattern mismatch**: String doesn’t match regex pattern

**Review RGD schema**:

```
# View the schema definition
kubectl get resourcegraphdefinition `my-rgd` -o jsonpath='{.spec.schema}'
```

Ensure your instance provides all required fields with correct types.

## Next steps

- [kro considerations for EKS](kro-considerations.md "kro-considerations.md") - kro considerations and best practices
- [Configure kro permissions](kro-permissions.md "kro-permissions.md") - Configure RBAC for platform and application teams
- [kro concepts](kro-concepts.md "kro-concepts.md") - Understand kro concepts and resource lifecycle
- [Troubleshooting EKS Capabilities](capabilities-troubleshooting.md "capabilities-troubleshooting.md") - General capability troubleshooting guidance
