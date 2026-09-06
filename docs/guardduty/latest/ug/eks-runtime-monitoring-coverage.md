

# Runtime coverage and troubleshooting for Amazon EKS clusters
<a name="eks-runtime-monitoring-coverage"></a>

After you enable Runtime Monitoring and install the GuardDuty security agent (add-on) for EKS either manually or through automated agent configuration, you can start assessing the coverage for your EKS clusters. 

**Topics**
+ [Reviewing coverage statistics](#reviewing-coverage-statistics-eks-runtime-monitoring)
+ [Coverage status change with EventBridge notifications](#eks-runtime-monitoring-coverage-status-change)
+ [Troubleshooting Amazon EKS runtime coverage issues](#eks-runtime-monitoring-coverage-issues-troubleshoot)

## Reviewing coverage statistics
<a name="reviewing-coverage-statistics-eks-runtime-monitoring"></a>

The coverage statistics for the EKS clusters associated with your own accounts or your member accounts is the percentage of the healthy EKS clusters over all EKS clusters in the selected AWS Region. The following equation represents this as:

*(Healthy clusters/All clusters)\*100*

Choose one of the access methods to review the coverage statistics for your accounts.

------
#### [ Console ]
+ Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).
+ In the navigation pane, choose **Runtime Monitoring**.
+ Choose the **EKS clusters runtime coverage** tab.
+ Under the **EKS clusters runtime coverage** tab, you can view the coverage statistics aggregated by the coverage status that is available in the **Clusters list** table. 
  + You can filter the **Clusters list** table by the following columns:
    + **Cluster name**
    + **Account ID**
    + **Agent management type**
    + **Coverage status**
    + **Add-on version**
+ If any of your EKS clusters have the **Coverage status** as **Unhealthy**, the **Issue** column may include additional information about the reason for the **Unhealthy** status.

------
#### [ API/CLI ]
+ Run the [ListCoverage](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCoverage.html) API with your own valid detector ID, Region, and service endpoint. You can filter and sort the cluster list using this API.
  + You can change the example `filter-criteria` with one of the following options for `CriterionKey`:
    + `ACCOUNT_ID`
    + `CLUSTER_NAME`
    + `RESOURCE_TYPE`
    + `COVERAGE_STATUS`
    + `ADDON_VERSION`
    + `MANAGEMENT_TYPE`
  + You can change the example `AttributeName` in `sort-criteria` with the following options:
    + `ACCOUNT_ID`
    + `CLUSTER_NAME`
    + `COVERAGE_STATUS`
    + `ISSUE`
    + `ADDON_VERSION`
    + `UPDATED_AT`
  + You can change the {{max-results}} (up to 50).
  + To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty --region {{us-east-1}} list-coverage --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --sort-criteria '{"AttributeName": "{{CLUSTER_NAME}}", "OrderBy": "{{DESC}}"}' --filter-criteria '{"FilterCriterion":[{"CriterionKey":"{{ACCOUNT_ID}}", "FilterCondition":{"EqualsValue":"111122223333"}}] }'  --max-results {{5}}
  ```
+ Run the [GetCoverageStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCoverageStatistics.html) API to retrieve coverage aggregated statistics based on the `statisticsType`.
  + You can change the example `statisticsType` to one of the following options:
    + `COUNT_BY_COVERAGE_STATUS` – Represents coverage statistics for EKS clusters aggregated by coverage status.
    + `COUNT_BY_RESOURCE_TYPE` – Coverage statistics aggregated based on the type of AWS resource in the list.
    + You can change the example `filter-criteria` in the command. You can use the following options for `CriterionKey`:
      + `ACCOUNT_ID`
      + `CLUSTER_NAME`
      + `RESOURCE_TYPE`
      + `COVERAGE_STATUS`
      + `ADDON_VERSION`
      + `MANAGEMENT_TYPE`
  + To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty --region {{us-east-1}} get-coverage-statistics --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --statistics-type {{COUNT_BY_COVERAGE_STATUS}} --filter-criteria '{"FilterCriterion":[{"CriterionKey":"{{ACCOUNT_ID}}", "FilterCondition":{"EqualsValue":"123456789012"}}] }'
  ```

------

If the coverage status of your EKS cluster is **Unhealthy**, see [Troubleshooting Amazon EKS runtime coverage issues](#eks-runtime-monitoring-coverage-issues-troubleshoot).

## Coverage status change with EventBridge notifications
<a name="eks-runtime-monitoring-coverage-status-change"></a>

The coverage status of an EKS cluster in your account may show up as **Unhealthy**. To detect when the coverage status becomes **Unhealthy**, we recommend you monitor the coverage status periodically and troubleshoot, if the status is **Unhealthy**. Alternatively, you can create an Amazon EventBridge rule to notify you when the coverage status changes from either `Unhealthy` to `Healthy` or otherwise. By default, GuardDuty publishes this in the [EventBridge bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html) for your account.

### Sample notification schema
<a name="coverage-status-eventbridge-schema"></a>

In an EventBridge rule, you can use the pre-defined sample events and event patterns to receive coverage status notification. For more information about creating an EventBridge rule, see [Create rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html#eb-gs-create-rule) in the *Amazon EventBridge User Guide*. 

Additionally, you can create a custom event pattern by using the following example notification schema. Make sure to replace the values for your account. To get notified when the coverage status of your Amazon EKS cluster changes from `Healthy` to `Unhealthy`, the `detail-type` should be {{GuardDuty Runtime Protection Unhealthy}}. To get notified when the coverage status changes from `Unhealthy` to `Healthy`, replace the value of `detail-type` with {{GuardDuty Runtime Protection Healthy}}.

```
{
  "version": "0",
  "id": "event ID",
  "detail-type": "GuardDuty Runtime Protection {{Unhealthy}}",
  "source": "aws.guardduty",
  "account": "AWS account ID",
  "time": "event timestamp (string)",
  "region": "AWS Region",
  "resources": [
       ],
  "detail": {
    "schemaVersion": "1.0",
    "resourceAccountId": "string",
    "currentStatus": "string",
    "previousStatus": "string",
    "resourceDetails": {
        "resourceType": "EKS",
        "eksClusterDetails": { 
            "clusterName": "string",
            "availableNodes": "string",
             "desiredNodes": "string",
             "addonVersion": "string"
         }
    },
    "issue": "string",
    "lastUpdatedAt": "timestamp"
  }
}
```

## Troubleshooting Amazon EKS runtime coverage issues
<a name="eks-runtime-monitoring-coverage-issues-troubleshoot"></a>

If the coverage status for your EKS cluster is `Unhealthy`, you can view the corresponding error either under the **Issue** column in the GuardDuty console, or by using the [CoverageResource](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageResource.html) data type.

When working with inclusion or exclusion tags for monitoring your EKS clusters selectively, it may take some time for the tags to sync. This may impact the coverage status of the associated EKS cluster. You can try removing and adding the corresponding tag (inclusion or exclusion) again. For more information, see [Tagging your Amazon EKS resources](https://docs.aws.amazon.com/eks/latest/userguide/eks-using-tags.html) in the **Amazon EKS User Guide**.

The structure of a coverage issue is `Issue type:Extra information`. Typically, the issues will have an optional *Extra information* that may include specific client-side exception or description about the issue. Based on *Extra information*, the following tables provide the recommended steps to troubleshoot the coverage issues for your EKS clusters.



- **Addon Creation Failed**
  - **Extra information:** Addon `aws-guardduty-agent` is not compatible with current cluster version of cluster {{ClusterName}}. Addon specified is not supported.
  - **Recommended troubleshooting steps:** Make sure that you're using one of those Kubernetes versions that support deploying the `aws-guardduty-agent` EKS add-on. For more information, see [Kubernetes versions supported by GuardDuty security agent](prereq-runtime-monitoring-eks-support.md#gdu-agent-supported-k8-version). For information about updating your Kubernetes version, see [Updating an Amazon EKS cluster Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html).

- **Addon Creation Failed Addon Update Failed Addon Status Unhealthy**
  - **Extra information:** EKS Addon issue - `AddonIssueCode`: `AddonIssueMessage`
  - **Recommended troubleshooting steps:** For information about recommended steps for a specific add-on issue code, see [Troubleshooting steps for Addon creation/update error with Addon issue code](#gdu-eks-runtime-coverage-addon-issues).<br />For a list of addon issue codes that you might experience in this issue, see [AddonIssue](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonIssue.html#API_AddonIssue_Contents).<br />

- ** VPC Endpoint Creation Failed **
  - **Extra information:** VPC endpoint creation not supported for shared VPC {{vpcId}} / **Recommended troubleshooting steps:** Runtime Monitoring now supports the use of a shared VPC within an organization. Make sure your accounts meet all the prerequisites. For more information, see [Prerequisites for using shared VPC](runtime-monitoring-shared-vpc.md#shared-vpc-prerequisite-runtime-monitoring).
  - **Extra information:** **Only when using shared VPC with automated agent configuration**<br />Owner account ID {{111122223333}} for shared VPC {{vpcId}} doesn't have either Runtime Monitoring, automated agent configuration, or both, enabled. / **Recommended troubleshooting steps:** The shared VPC owner account must enable Runtime Monitoring and automated agent configuration for at least one resource type (Amazon EKS or Amazon ECS (AWS Fargate)). For more information, see [Prerequisites specific to GuardDuty Runtime Monitoring](runtime-monitoring-shared-vpc.md#shared-vpc-runtime-monitoring-prereq-gd-setup).
  - **Extra information:** Enabling private DNS requires both `enableDnsSupport` and `enableDnsHostnames` VPC attributes set to `true` for {{vpcId}} (Service: Ec2, Status Code:400, Request ID: {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}). / **Recommended troubleshooting steps:** Ensure that the following VPC attributes are set to `true` – `enableDnsSupport` and `enableDnsHostnames`. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).<br />If you're using Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/) to create the Amazon VPC, make sure to select both **Enable DNS hostnames** and **Enable DNS resolution**. For more information, see [VPC configuration options](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-options).

- **Shared VPC Endpoint Deletion Failed**
  - **Extra information:** Shared VPC endpoint deletion not allowed for account ID {{111122223333}}, shared VPC {{vpcId}}, owner account ID {{555555555555}}.
  - **Recommended troubleshooting steps:** +  Disabling the Runtime Monitoring status of the shared VPC participant account doesn't impact the shared VPC endpoint policy and the security group that exists in the owner account.  <br />To delete the shared VPC endpoint and security group, you must disable Runtime Monitoring or automated agent configuration status in the shared VPC owner account. <br />+  The shared VPC participant account can't delete the shared VPC endpoint and security group hosted in the shared VPC owner account. 

- **Local EKS clusters**
  - **Extra information:** EKS addons are not supported on local outpost clusters.
  - **Recommended troubleshooting steps:** Not actionable.<br />For more information, see [Amazon EKS on AWS outposts](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts.html).

- **EKS Runtime Monitoring enablement permission not granted**
  - **Extra information:** (may or may not show extra information)
  - **Recommended troubleshooting steps:** 1.  If the extra information is available for this issue, fix the root cause and follow the next step. <br />2.  Toggle EKS Runtime Monitoring to turn it off and then turn it on again. Ensure that the GuardDuty agent also gets deployed, whether automatically through GuardDuty or manually. 

- **EKS Runtime Monitoring enablement resource provisioning in progress**
  - **Extra information:** (may or may not show extra information)
  - **Recommended troubleshooting steps:** Not actionable. <br />After you enable EKS Runtime Monitoring, the coverage status might remain `Unhealthy` until the resource provisioning step completes. The coverage status gets monitored and updated periodically.

- **Others (any other issue)**
  - **Extra information:** Error due to authorization failure
  - **Recommended troubleshooting steps:** Toggle EKS Runtime Monitoring to turn it off and then turn it on again. Ensure that the GuardDuty agent also gets deployed, either automatically through GuardDuty or manually.




**Troubleshooting steps for Addon creation/update error with Addon issue code**  

<table>
<thead>
  <tr><th>Addon creation or update error</th><th>Troubleshooting steps</th></tr>
</thead>
<tbody>
  <tr><td>EKS Addon Issue - <code>InsufficientNumberOfReplicas</code>: The add-on is unhealthy because it doesn't have the desired number of replicas.</td><td> <ul><li> Using the issue message, you can identify and fix the root cause. You can start by describing your cluster. For example, use <a href="https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/">https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/</a> to identify the root cause for pod failure. <br />After you fix the root cause, retry the step (add-on creation or update). </li><li> If the issue persists, validate that the VPC endpoint for your Amazon EKS cluster is correctly configured. For more information, see <a href="validate-vpc-endpoint-config-runtime-monitoring.md">Validating VPC endpoint configuration</a>. </li></ul> </td></tr>
  <tr><td>EKS Addon Issue - <code>InsufficientNumberOfReplicas</code>: The add-on is unhealthy because one or more pods is not scheduled <code>0/x</code> nodes are available: <code>x Insufficient cpu. preemption: not eligible due to preemptionPolicy=Never</code>.</td><td rowspan="3">To resolve this issue, you can do one of the following:<ul><li> Update pod priority of the GuardDuty agent: <a href="guardduty-configure-security-agent-eks-addon.md#gdu-eks-addon-configure-parameters-values">Configurable parameters and values</a> by setting the <code>PriorityClass</code> to any one of the options that support the <code>preemptionPolicy</code> value as <code>PreemptLowerPriority</code>. For information about pod priority, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption">Pod Priority and Preemption</a> in the <i>Kubernetes Documentation</i>. </li><li> Scale up the instance: For managing your resources and making optimal instance selection, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html">Manage compute resources by using nodes</a> and <a href="https://docs.aws.amazon.com/eks/latest/userguide/choosing-instance-type.html">Choose an optimal Amazon EC2 node instance type</a> in the <i><i>Amazon EKS User Guide</i></i>. </li></ul> The message shows <code>0/x</code> because GuardDuty reports only the first found error. The actual number of running pods in the GuardDuty daemonset might be greater than 0. </td></tr>
  <tr><td>EKS Addon Issue - <code>InsufficientNumberOfReplicas</code>: The add-on is unhealthy because one or more pods is not scheduled <code>0/x</code> nodes are available: <code>x Too many pods. preemption: not eligible due to preemptionPolicy=Never</code>.</td></tr>
  <tr><td>EKS Addon Issue - <code>InsufficientNumberOfReplicas</code>: The add-on is unhealthy because one or more pods is not scheduled <code>0/x</code> nodes are available: <code>1 Insufficient memory. preemption: not eligible due to preemptionPolicy=Never</code>.</td></tr>
  <tr><td>EKS Addon Issue - <code>InsufficientNumberOfReplicas</code>: The add-on is unhealthy because one or more pods have waiting containers <code>CrashLoopBackOff: Completed</code></td><td>You can view the logs associated with the pod and identify the issue. For information on how to do this, see <a href="https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/">Debug Running Pods</a> in the <i>Kubernetes Documentation</i>.<br />Use the following checklist to troubleshoot this add-on issue:<ul><li> Validate that Runtime Monitoring is enabled. </li><li> Validate that the <a href="prereq-runtime-monitoring-eks-support.md">Prerequisites for Amazon EKS cluster support</a>, such as verified OS distributions and supported Kubernetes versions, are met. </li><li> When you manage the security agent manually, confirm that you created a VPC endpoint for all the VPCs. When you enable GuardDuty automated configuration, you should still validate that the VPC endpoint gets created. For example, when using a shared VPC in automated configuration. <br />To validate this, see <a href="validate-vpc-endpoint-config-runtime-monitoring.md">Validating VPC endpoint configuration</a>. </li><li> Confirm that the GuardDuty security agent is able to resolve the GuardDuty VPC endpoint private DNS. To know the endpoints, see <b>Private DNS names for endpoints</b> in <a href="runtime-monitoring-managing-agents.md">Managing GuardDuty security agents</a>. <br />To do this, you can use either <code>nslookup</code> tool on Windows or Mac, or <code>dig</code> tool on Linux. When using <i>nslookup</i>, you can use the following command after replacing the Region {{us-west-2}} with your Region: <pre>nslookup guardduty-data.us-west-2.amazonaws.com</pre> </li><li> Validate that your GuardDuty VPC endpoint policy or the service control policy is not impacting <code>guardduty:SendSecurityTelemetry</code> action.  </li></ul></td></tr>
  <tr><td>EKS Addon Issue - <code>InsufficientNumberOfReplicas</code>: The add-on is unhealthy because one or more pods have waiting containers <code>CrashLoopBackOff: Error</code></td><td>You can view the logs associated with the pod and identify the issue. For information on how to do this, see <a href="https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/">Debug Running Pods</a> in the <i>Kubernetes Documentation</i>.<br />After you have identified the issue, use the following checklist to troubleshoot this:<ul><li> Validate that Runtime Monitoring is enabled. </li><li> Validate that the <a href="prereq-runtime-monitoring-eks-support.md">Prerequisites for Amazon EKS cluster support</a>, such as verified OS distributions and supported Kubernetes versions, are met. </li><li> The GuardDuty security agent is able to resolve the GuardDuty VPC endpoint private DNS. To know the endpoints, see <b>Private DNS names for endpoints</b> in <a href="runtime-monitoring-managing-agents.md">Managing GuardDuty security agents</a>. </li></ul></td></tr>
  <tr><td>EKS Addon Issue - <code>AdmissionRequestDenied</code>: admission webhook <code>"validate.kyverno.svc-fail"</code> denied the request: policy <code>DaemonSet/amazon-guardduty/aws-guardduty-agent</code> for resource violation: restrict-image-registries: <code>autogen-validate-registries</code>: ...</td><td><ol><li> Amazon EKS cluster or the security administrator must review the security policy that is blocking the Addon update. </li><li> You must either disable the controller (<code>webhook</code>) or have the controller accept the requests from Amazon EKS. </li></ol> </td></tr>
  <tr><td>EKS Addon Issue - <code>ConfigurationConflict</code>: Conflicts found when trying to apply. Will not continue due to resolve conflicts mode. <code>Conflicts: DaemonSet.apps aws-guardduty-agent - .spec.template.spec.containers[name="aws-guardduty-agent"].image</code></td><td>When creating or updating the Addon, provide the <code>OVERWRITE</code> resolve conflict flag. This will potentially overwrite any changes that have been made directly to the related resources in Kubernetes by using the Kubernetes API.<br />You can first <a href="https://docs.aws.amazon.com/eks/latest/userguide/removing-an-add-on.html">Remove an Amazon EKS add-on from a cluster</a> and then reinstall.</td></tr>
  <tr><td>EKS Addon Issue - <code>AccessDenied: priorityclasses.scheduling.k8s.io "aws-guardduty-agent.priorityclass" is forbidden: User "eks:addon-manager" cannot patch resource "priorityclasses" in API group "scheduling.k8s.io" at the cluster scope</code></td><td rowspan="2">You must add the missing permission to the <code>eks:addon-cluster-admin ClusterRoleBinding</code> manually. Add the following <code>yaml</code> to <code>eks:addon-cluster-admin</code>:<pre>---<br />kind: ClusterRoleBinding<br />apiVersion: rbac.authorization.k8s.io/v1<br />metadata:<br />  name: eks:addon-cluster-admin<br />subjects:<br />- kind: User<br />  name: eks:addon-manager<br />  apiGroup: rbac.authorization.k8s.io<br />roleRef:<br />  kind: ClusterRole<br />  name: cluster-admin<br />  apiGroup: rbac.authorization.k8s.io<br />---</pre><br />You can now apply this <code>yaml</code> to your Amazon EKS cluster by using the following command:<pre>kubectl apply -f eks-addon-cluster-admin.yaml</pre></td></tr>
  <tr><td>AddonUpdationFailed: EKSAddonIssue - <code>AccessDenied: namespaces\"amazon-guardduty\"isforbidden:User\"eks:addon-manager\"cannotpatchresource\"namespaces\"inAPIgroup\"\"inthenamespace\"amazon-guardduty\"</code></td></tr>
  <tr><td>EKS Addon Issue - <code>AccessDenied: admission webhook "validation.gatekeeper.sh" denied the request: [all-namespace-must-have-label-owner] All namespaces must have an `owner` label</code></td><td>You must either disable the controller or have the controller accept the requests from the Amazon EKS cluster.<br />Prior to creating or updating the add-on, you can also create a GuardDuty namespace and label it as <code>owner</code>.</td></tr>
  <tr><td>EKS Addon Issue - <code>AccessDenied: admission webhook "validation.gatekeeper.sh" denied the request: [allowed-container-registries] container &lt;aws-guardduty-agent&gt; has an invalid image registry</code></td><td>Add the image registry for GuardDuty to the <code>allowed-container-registries</code> in your admission controller. For more information, see <i>ECR repository for EKS v1.8.1-eks-build.2</i> in <a href="runtime-monitoring-ecr-repository-gdu-agent.md">Amazon ECR repository hosting GuardDuty agent</a>.</td></tr>
</tbody>
</table>
