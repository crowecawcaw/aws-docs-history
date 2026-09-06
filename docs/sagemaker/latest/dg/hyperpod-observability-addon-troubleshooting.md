

# Troubleshooting the Amazon SageMaker HyperPod observability add-on
<a name="hyperpod-observability-addon-troubleshooting"></a>

Use the following guidance to resolve common issues with the Amazon SageMaker HyperPod (SageMaker HyperPod) observability add-on.

## Troubleshooting missing metrics in Amazon Managed Grafana
<a name="troubleshooting-missing-metrics"></a>

If metrics don't appear in your Amazon Managed Grafana dashboards, perform the following steps to identify and resolve the issue.

### Verify the Amazon Managed Service for Prometheus-Amazon Managed Grafana connection
<a name="verify-amp-grafana-connection"></a>

1. Sign in to the Amazon Managed Grafana console.

1. In the left pane, choose **All workspaces**.

1. In the **Workspaces** table, choose your workspace.

1. In the details page of the workspace, choose the **Data sources** tab.

1. Verify that the Amazon Managed Service for Prometheus data source exists.

1. Check the connection settings:
   + Confirm that the endpoint URL is correct.
   + Verify that IAM authentication is properly configured.
   + Choose **Test connection**. Verify that the status is **Data source is working**.

### Verify the Amazon EKS add-on status
<a name="verify-eks-addon-status"></a>

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home\#/clusters](https://console.aws.amazon.com/eks/home#/clusters).

1. Select your cluster.

1. Choose the **Add-ons** tab.

1. Verify that the SageMaker HyperPod observability add-on is listed and that its status is **ACTIVE**.

1. If the status isn't **ACTIVE**, see [Troubleshooting add-on installation failures](#troubleshooting-addon-installation-failures).

### Verify Pod Identity association
<a name="verify-pod-identity-association"></a>

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home\#/clusters](https://console.aws.amazon.com/eks/home#/clusters).

1. Select your cluster.

1. On the cluster details page, choose the **Access** tab.

1. In the **Pod Identity associations** table, choose the association that has the following property values:
   + **Namespace**: `hyperpod-observability`
   + **Service account**: `hyperpod-observability-operator-otel-collector`
   + **Add-on**: `amazon-sagemaker-hyperpod-observability`

1. Ensure that the IAM role that is attached to this association has the following permissions.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "PrometheusAccess",
               "Effect": "Allow",
               "Action": "aps:RemoteWrite",
               "Resource": "arn:aws:aps:{{us-east-1}}:{{111122223333}}:workspace/{{workspace-ID}}"
           },
           {
               "Sid": "CloudwatchLogsAccess",
               "Effect": "Allow",
               "Action": [
                   "logs:CreateLogGroup",
                   "logs:CreateLogStream",
                   "logs:DescribeLogGroups",
                   "logs:DescribeLogStreams",
                   "logs:PutLogEvents",
                   "logs:GetLogEvents",
                   "logs:FilterLogEvents",
                   "logs:GetLogRecord",
                   "logs:StartQuery",
                   "logs:StopQuery",
                   "logs:GetQueryResults"
               ],
               "Resource": [
                   "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:/aws/sagemaker/Clusters/*",
                   "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:/aws/sagemaker/Clusters/*:log-stream:*"
               ]
           }
       ]
   }
   ```

------

1. Ensure that the IAM role that is attached to this association has the following trust policy. Verify that the source ARN and source account are correct.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
               "Effect": "Allow",
               "Principal": {
                   "Service": "pods.eks.amazonaws.com"
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:TagSession"
               ],
               "Condition": {
                   "StringEquals": {
                       "aws:SourceArn": "arn:aws:eks:us-east-1:111122223333:cluster/{{cluster-name}}",
                       "aws:SourceAccount": "111122223333"
                   }
               }
           }
       ]
   }
   ```

------

### Check Amazon Managed Service for Prometheus throttling
<a name="check-amp-throttling"></a>

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the **Managed quotas** box, search for and select Amazon Managed Service for Prometheus.

1. Choose the **Active series per workspace** quota.

1. In the **Resource-level quotas** tab, select your Amazon Managed Service for Prometheus workspace.

1. Ensure that the utilization is less than your current quota.

1. If you've reached the quota limit, select your workspace by choosing the radio button to its left, and then choose **Request increase at resource level** .

### Verify KV caching and intelligent routing are enabled
<a name="verify-caching-routing"></a>

If the `KVCache Metrics` dashboard is missing, feature is either not enabled or the port isn't mentioned in the `modelMetrics`. For more information on how to enable this, see steps 1 and 3 in [Configure KV caching and intelligent routing](sagemaker-hyperpod-model-deployment-caching-routing.md#sagemaker-hyperpod-model-deployment-deploy-ftm-cache-route). 

If the `Intelligent Router Metrics` dashboard is missing, enable the feature to have them show up. For more information on how to enable this, see [Configure KV caching and intelligent routing](sagemaker-hyperpod-model-deployment-caching-routing.md#sagemaker-hyperpod-model-deployment-deploy-ftm-cache-route). 

## Troubleshooting add-on installation failures
<a name="troubleshooting-addon-installation-failures"></a>

If the observability add-on fails to install, use the following steps to diagnose and resolve the issue.

### Check health probe status
<a name="check-health-probe-status"></a>

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home\#/clusters](https://console.aws.amazon.com/eks/home#/clusters).

1. Select your cluster.

1. Choose the **Add-ons** tab.

1. Choose the failed add-on.

1. Review the **Health issues** section.

1. If the health issue is related to credentials or pod identity, see [Verify Pod Identity association](#verify-pod-identity-association). Also ensure that the pod identity agent add-on is running in the cluster.

1. Check for errors in the manager logs. For instructions, see [Review manager logs](#review-manager-logs).

1. Contact AWS Support with the issue details.

### Review manager logs
<a name="review-manager-logs"></a>

1. Get the add-on manager pod:

   ```
   kubectl logs -n hyperpod-observability -l control-plane=hyperpod-observability-controller-manager
   ```

1. For urgent issues, contact Support.

## Review all observability pods
<a name="review-all-observability-pods"></a>

All the pods that the SageMaker HyperPod observability add-on creates are in the `hyperpod-observability` namespace. To get the status of these pods, run the following command.

```
kubectl get pods -n hyperpod-observability
```

Look for the pods whose status is either `pending` or `crashloopbackoff`. Run the following command to get the logs of these pending or failing pods.

```
kubectl logs -n hyperpod-observability pod-name
```

If you don't find errors in the logs, run the following command to describe the pods and look for errors.

```
kubectl describe -n hyperpod-observability pod pod-name
```

To get more context, run the two following commands to describe the deployments and daemonsets for these pods.

```
kubectl describe -n hyperpod-observability deployment deployment-name
```

```
kubectl describe -n hyperpod-observability daemonset daemonset-name
```

## Troubleshooting pods that are stuck in the pending status
<a name="pods-stuck-in-pending"></a>

If you see that there are pods that are stuck in the `pending` status, make sure that the node is large enough to fit in all the pods. To verify that it is, perform the following steps.

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home\#/clusters](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose your cluster.

1. Choose the cluster's **Compute** tab.

1. Choose the node with the smallest instance type.

1. In the capacity allocation section, look for available pods.

1. If there are no available pods, then you need a larger instance type.

For urgent issues, contact AWS Support.

## Troubleshooting observability on Restricted Instance Groups
<a name="troubleshooting-rig-observability"></a>

Use the following guidance to resolve issues specific to clusters with Restricted Instance Groups.

### Observability pods not starting on restricted nodes
<a name="troubleshooting-rig-pods-not-starting"></a>

If observability pods are not starting on restricted nodes, check the pod status and events:

```
kubectl get pods -n hyperpod-observability -o wide
kubectl describe pod {{pod-name}} -n hyperpod-observability
```

Common causes include:
+ **Image pull failures:** The pod events may show image pull errors if the observability container images are not yet allowlisted on the restricted nodes. Ensure that you are running the latest version of the observability add-on. If the issue persists after upgrading, contact Support.
+ **Taint tolerations:** Verify that the pod spec includes the required toleration for restricted nodes. The add-on starting from version `v1.0.5-eksbuild.1` automatically adds this toleration when RIG support is enabled. If you are using older version, please upgrade to the latest version.

### Viewing logs for pods on restricted nodes
<a name="troubleshooting-rig-viewing-logs"></a>

The `kubectl logs` command does not work for pods running on restricted nodes. This is an expected limitation because the communication path required for log streaming is not available on restricted nodes.

To view logs from restricted nodes, use the **Cluster Logs** dashboard in Amazon Managed Grafana, which queries CloudWatch Logs directly. You can filter by instance ID, log stream, log level, and free-text search to find relevant log entries.

### DNS resolution failures in clusters with both standard and restricted nodes
<a name="troubleshooting-rig-dns-resolution"></a>

In hybrid clusters (clusters with both standard and restricted instance groups), pods on standard nodes may experience DNS resolution timeouts when trying to reach AWS service endpoints such as Amazon Managed Service for Prometheus or CloudWatch.

**Cause:** The `kube-dns` service has endpoints from both standard CoreDNS pods and RIG CoreDNS pods. Standard node pods cannot reach RIG CoreDNS endpoints due to network isolation. When `kube-proxy` load-balances a DNS request from a standard node pod to a RIG CoreDNS endpoint, the request times out.

**Resolution:** Set `internalTrafficPolicy: Local` on the `kube-dns` service so that pods only reach CoreDNS on their local node:

```
kubectl patch svc kube-dns -n kube-system -p '{"spec":{"internalTrafficPolicy":"Local"}}'
```

After applying this patch, restart the affected observability pods:

```
kubectl delete pods -n hyperpod-observability -l app.kubernetes.io/name=hyperpod-node-collector
```

### Metrics from restricted nodes not reaching Amazon Managed Service for Prometheus
<a name="troubleshooting-rig-metrics-not-reaching-amp"></a>

If metrics from restricted nodes are not appearing in your Amazon Managed Service for Prometheus workspace:

1. **Verify the execution role permissions.** Ensure that the execution role for the Restricted Instance Group has `aps:RemoteWrite` permission for your Prometheus workspace. For more information, see [Additional prerequisites for Restricted Instance Groups](hyperpod-observability-addon-setup.md#hyperpod-observability-addon-rig-prerequisites).

1. **Check the node collector pod status.** Run the following command and verify that node collector pods are running on restricted nodes:

   ```
   kubectl get pods -n hyperpod-observability | grep node-collector
   ```

1. **Check the central collector deployments.** In clusters with restricted nodes, the add-on deploys one central collector per network boundary. Verify that a central collector exists for each boundary:

   ```
   kubectl get deployments -n hyperpod-observability | grep central-collector
   ```

1. **Check pod events for errors.** Use `kubectl describe` on the collector pods to look for error events:

   ```
   kubectl describe pod {{collector-pod-name}} -n hyperpod-observability
   ```

If the issue persists after verifying the above, contact Support.

### Pod Identity verification does not apply to restricted instance group nodes
<a name="troubleshooting-rig-pod-identity"></a>

The [Verify Pod Identity association](#verify-pod-identity-association) troubleshooting steps apply only to standard nodes. On restricted nodes, the add-on uses the cluster instance group execution role for AWS authentication instead of Amazon EKS Pod Identity. If metrics are missing from restricted nodes, verify the execution role permissions instead of the Pod Identity association.

### Fluent Bit not running on restricted nodes
<a name="troubleshooting-rig-fluent-bit"></a>

This is expected behavior. Fluent Bit is intentionally not deployed on restricted nodes. Logs from restricted nodes are published to CloudWatch through the SageMaker HyperPod platform independently of the observability add-on. Use the **Cluster Logs** dashboard in Amazon Managed Grafana to view these logs.