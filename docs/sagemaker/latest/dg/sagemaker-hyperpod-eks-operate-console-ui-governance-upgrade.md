

# Upgrade the task governance add-on
<a name="sagemaker-hyperpod-eks-operate-console-ui-governance-upgrade"></a>

Use this section to upgrade the HyperPod task governance Amazon EKS add-on between versions. Each subsection provides version-specific procedures for upgrading your add-on while preserving your existing configuration.

**Topics**
+ [Upgrade from v1.3.x to v1.5](#hp-eks-task-governance-upgrade-v13-to-v15)

## Upgrade from v1.3.x to v1.5
<a name="hp-eks-task-governance-upgrade-v13-to-v15"></a>

The recommended way to upgrade from v1.3.x to v1.5 is the upgrade option in the SageMaker AI HyperPod console, which migrates the Kueue CRDs automatically. Use the manual procedure in this section only if you cannot use the console.

A direct `aws eks update-addon` from v1.3.x to v1.5 fails because v1.3.x stores some Kueue custom resource definitions (CRDs) under the `v1alpha1` API version, which v1.5 removes:

```
CustomResourceDefinition.apiextensions.k8s.io "cohorts.kueue.x-k8s.io" is invalid:
status.storedVersions[0]: Invalid value: "v1alpha1": missing from spec.versions
```

This procedure backs up your Kueue objects and clears the old stored version. It then upgrades the add-on and restores your objects under the new schema.

**Data impact and timing**  
This procedure deletes and re-creates your Kueue custom resource objects (ClusterQueues, LocalQueues, ResourceFlavors, Topologies, and related objects). It backs them up first and restores them, so no configuration is lost. It does not delete any namespace, does not delete any CRD, and does not change any SageMaker AI ComputeQuota or ClusterSchedulerConfig record.  
Run this when no new workloads need to be submitted. Running pods are generally not interrupted, but we recommend not relying on active workloads during the migration. New workloads cannot be scheduled until the procedure completes. Run against one cluster at a time.

### Prerequisites
<a name="hp-eks-task-governance-upgrade-v13-to-v15-prerequisites"></a>

Before you begin, make sure you have the following:
+ `kubectl` configured for the target Amazon EKS cluster with cluster-administrator access
+ The AWS CLI configured for the cluster's account and Region
+ `jq` installed
+ The add-on is currently at v1.3.x with status `ACTIVE` or `DEGRADED`

Throughout, replace {{region}} with your Region and {{cluster-name}} with your Amazon EKS cluster name.

To upgrade the add-on from v1.3.x to v1.5, complete the following steps:

1. **Confirm the current add-on version and set a working directory.**

   ```
   aws eks describe-addon --region {{region}} --cluster-name {{cluster-name}} \
     --addon-name amazon-sagemaker-hyperpod-taskgovernance \
     --query 'addon.addonVersion' --output text
   ```

   Confirm the output begins with `v1.3.`. Then set `BACKUP_DIR` to an absolute path in a writable directory and create it. Later steps read from and write to this variable, so run every step in the same shell session.

   ```
   export BACKUP_DIR={{/absolute/path/to/backup-dir}}
   mkdir -p "$BACKUP_DIR"
   ```

1. **Back up every Kueue custom resource to local files.**

   ```
   for crd in admissionchecks clusterqueues cohorts localqueues multikueueclusters \
              multikueueconfigs provisioningrequestconfigs resourceflavors topologies \
              workloadpriorityclasses workloads; do
     kubectl get "${crd}.kueue.x-k8s.io" --all-namespaces -o json \
       > "$BACKUP_DIR/${crd}.json" 2>/dev/null
     echo "${crd}: $(jq '.items | length' "$BACKUP_DIR/${crd}.json" 2>/dev/null || echo 0)"
   done
   ```
**Verify the backup before continuing**  
Confirm that the backup directory contains a JSON file for each custom resource in the preceding command, and that the object counts in the command output match what your cluster had. Do not proceed if any file is missing or empty.

1. **Delete the backed-up objects and clear the old stored version from each CRD.**

   This removes the `v1alpha1` (or `v1beta1`) entry from `status.storedVersions` so the v1.5 CRDs can install. The objects are safe in your backup and are restored in a later step.

   ```
   for crd in admissionchecks clusterqueues cohorts localqueues multikueueclusters \
              multikueueconfigs provisioningrequestconfigs resourceflavors topologies \
              workloadpriorityclasses workloads; do
     kubectl get crd "${crd}.kueue.x-k8s.io" >/dev/null 2>&1 || continue
     kubectl delete "${crd}.kueue.x-k8s.io" --all --all-namespaces \
       --ignore-not-found=true --wait=false --request-timeout=30s
     kubectl patch crd "${crd}.kueue.x-k8s.io" --subresource=status --type=merge \
       --request-timeout=30s -p '{"status":{"storedVersions":["v1beta2"]}}'
   done
   ```
**About --all-namespaces and --wait=false**  
`--all-namespaces` here selects custom resources across all namespaces to delete; it does not delete any namespace. `--wait=false` avoids blocking on finalizers. The add-on update in the next step resolves them.

1. **Update the add-on to v1.5.**

   ```
   aws eks update-addon --region {{region}} --cluster-name {{cluster-name}} \
     --addon-name amazon-sagemaker-hyperpod-taskgovernance \
     --addon-version v1.5.0-eksbuild.1 --resolve-conflicts OVERWRITE
   ```

   Wait until the status is `ACTIVE`:

   ```
   aws eks describe-addon --region {{region}} --cluster-name {{cluster-name}} \
     --addon-name amazon-sagemaker-hyperpod-taskgovernance \
     --query 'addon.status' --output text
   ```

1. **Wait for the new install to settle before restoring.**

   Do not restore immediately after the add-on reports `ACTIVE`. Wait for the controller, its webhook, and the post-install jobs to be ready, or the restore in the next step can hang.

   ```
   kubectl rollout status deploy/kueue-controller-manager -n kueue-system --timeout=300s
   ```

   ```
   until [ -n "$(kubectl get endpoints -n kueue-system kueue-webhook-service \
                 -o jsonpath='{.subsets[*].addresses[*].ip}' 2>/dev/null)" ]; do
     echo "waiting for kueue webhook endpoint..."; sleep 5
   done
   ```

   ```
   kubectl wait --for=condition=complete job -l app.kubernetes.io/name=kueue \
     -n kueue-system --timeout=180s || true
   ```

1. **Restore your objects under the new schema.**

   This transforms each backed-up object to the v1.5 (`v1beta2`) schema and re-applies it.

   ```
   transform() {
     jq '
       .apiVersion = "kueue.x-k8s.io/v1beta2"
       | del(.status)
       | del(.metadata.resourceVersion, .metadata.uid, .metadata.creationTimestamp,
             .metadata.generation, .metadata.managedFields, .metadata.selfLink)
       | del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")
       | if .kind == "Cohort" and (.spec.parent != null)
           then .spec.parentName = (.spec.parentName // .spec.parent) | del(.spec.parent) else . end
       | if .kind == "ClusterQueue" and (.spec.cohort != null)
           then .spec.cohortName = (.spec.cohortName // .spec.cohort) | del(.spec.cohort) else . end
       | if .kind == "ClusterQueue" then del(.spec.admissionChecks) else . end
       | if .kind == "AdmissionCheck" then del(.spec.retryDelayMinutes) else . end
     '
   }
   
   for crd in resourceflavors topologies workloadpriorityclasses admissionchecks cohorts \
              provisioningrequestconfigs multikueueclusters multikueueconfigs \
              clusterqueues localqueues workloads; do
     f="$BACKUP_DIR/${crd}.json"
     [ -s "$f" ] || continue
     count=$(jq '.items | length' "$f")
     for (( i=0; i<count; i++ )); do
       obj=$(jq -c ".items[$i]" "$f" | transform)
       name=$(printf '%s' "$obj" | jq -r '.kind + "/" + .metadata.name')
       if printf '%s' "$obj" | kubectl apply --request-timeout=30s -f - >/dev/null 2>&1; then
         echo "applied $name"
       else
         echo "check $name (may already be recreated by the add-on)"
       fi
     done
   done
   ```

1. **Verify the result.**

   ```
   aws eks describe-addon --region {{region}} --cluster-name {{cluster-name}} \
     --addon-name amazon-sagemaker-hyperpod-taskgovernance \
     --query 'addon.{version:addonVersion,status:status}'
   ```

   An example output is as follows.

   ```
   {
       "version": "v1.5.0-eksbuild.1",
       "status": "ACTIVE"
   }
   ```

   Confirm your objects are present and no CRD still lists `v1alpha1`:

   ```
   kubectl get clusterqueues
   kubectl get localqueues --all-namespaces
   kubectl get crd clusterqueues.kueue.x-k8s.io -o jsonpath='{.status.storedVersions}'
   ```

   The `storedVersions` output must contain only `v1beta2` (or `v1beta1` and `v1beta2`), never `v1alpha1`. Compare the restored objects against the files in `$BACKUP_DIR` to confirm that your configuration values are unchanged.