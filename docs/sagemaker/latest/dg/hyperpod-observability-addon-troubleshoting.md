# Troubleshooting

the Amazon SageMaker HyperPod observability add-on

Use the following guidance to resolve common issues with the Amazon SageMaker HyperPod
(SageMaker HyperPod) observability add-on.

## Troubleshooting missing

metrics in Amazon Managed Grafana

If metrics don't appear in your Amazon Managed Grafana dashboards, perform the
following steps to identify and resolve the issue.

### Verify the

Amazon Managed Service for Prometheus-Amazon Managed Grafana connection

1. Sign in to the Amazon Managed Grafana console.
2. In the left pane, choose **All
   workspaces**.
3. In the **Workspaces** table, choose your
   workspace.
4. In the details page of the workspace, choose the
   **Data sources** tab.
5. Verify that the Amazon Managed Service for Prometheus data source exists.
6. Check the connection settings:
   - Confirm that the endpoint URL is correct.
   - Verify that IAM authentication is properly
     configured.
   - Choose **Test connection**. Verify
     that the status is **Data source is
     working**.

### Verify the Amazon EKS add-on

status

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Select your cluster.
3. Choose the **Add-ons** tab.
4. Verify that the SageMaker HyperPod observability add-on is listed
   and that its status is **ACTIVE**.
5. If the status isn't **ACTIVE**, see [Troubleshooting add-on installation failures](#troubleshooting-addon-installation-failures "#troubleshooting-addon-installation-failures").

### Verify Pod Identity

association

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Select your cluster.
3. On the cluster details page, choose the
   **Access** tab.
4. In the **Pod Identity associations** table,
   choose the association that has the following property
   values:
   - **Namespace**:
     `hyperpod-observability`
   - **Service account**:
     `hyperpod-observability-operator-otel-collector`
   - **Add-on**:
     `amazon-sagemaker-hyperpod-observability`

5. Ensure that the IAM role that is attached to this
   association has the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PrometheusAccess",
 "Effect": "Allow",
 "Action": "aps:RemoteWrite",
 "Resource": "arn:aws:aps:`us-east-1`:`111122223333`:workspace/`workspace-ID`"
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
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/sagemaker/Clusters/*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/sagemaker/Clusters/*:log-stream:*"
 ]
 }
 ]
}`

```

6. Ensure that the IAM role that is attached to this
   association has the following trust policy. Verify that the
   source ARN and source account are correct.

JSON

```
`{
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
 "aws:SourceArn": "arn:aws:eks:us-east-1:111122223333:cluster/`cluster-name`",
 "aws:SourceAccount": "111122223333"
 }
 }
 }
 ]
}`

```

### Check Amazon Managed Service for Prometheus

throttling

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the **Managed quotas** box, search for and
   select Amazon Managed Service for Prometheus.
3. Choose the **Active series per workspace**
   quota.
4. In the **Resource-level quotas** tab, select
   your Amazon Managed Service for Prometheus workspace.
5. Ensure that the utilization is less than your current
   quota.
6. If you've reached the quota limit, select your workspace by
   choosing the radio button to its left, and then choose
   **Request increase at resource level**
   .

## Troubleshooting add-on installation failures

If the observability add-on fails to install, use the following steps to
diagnose and resolve the issue.

### Check health probe

status

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Select your cluster.
3. Choose the **Add-ons** tab.
4. Choose the failed add-on.
5. Review the **Health issues** section.
6. If the health issue is related to credentials or pod identity,
   see [Verify Pod Identity
   association](#verify-pod-identity-association "#verify-pod-identity-association"). Also
   ensure that the pod identity agent add-on is running in the
   cluster.
7. Check for errors in the manager logs. For instructions, see
   [Review manager logs](#review-manager-logs "#review-manager-logs").
8. Contact AWS Support with the issue details.

### Review manager logs

1. Get the add-on manager pod:

```
kubectl logs -n hyperpod-observability -l control-plane=hyperpod-observability-controller-manager
```

2. For urgent issues, contact Support.

## Review all observability

pods

All the pods that the SageMaker HyperPod observability add-on creates are in the
`hyperpod-observability` namespace. To get the status of
these pods, run the following command.

```
kubectl get pods -n hyperpod-observability
```

Look for the pods whose status is either `pending` or
`crashloopbackoff`. Run the following command to get the logs
of these pending or failing pods.

```
kubectl logs -n hyperpod-observability pod-name
```

If you don't find errors in the logs, run the following command to
describe the pods and look for errors.

```
kubectl describe -n hyperpod-observability pod pod-name
```

To get more context, run the two following commands to describe the
deployments and daemonsets for these pods.

```
kubectl describe -n hyperpod-observability deployment deployment-name
```

```
kubectl describe -n hyperpod-observability daemonset daemonset-name
```

## Troubleshooting pods that are stuck

in the pending status

If you see that there are pods that are stuck in the `pending`
status, make sure that the node is large enough to fit in all the pods. To
verify that it is, perform the following steps.

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose your cluster.
3. Choose the cluster's **Compute** tab.
4. Choose the node with the smallest instance type.
5. In the capacity allocation section, look for available
   pods.
6. If there are no available pods, then you need a larger instance
   type.

For urgent issues, contact AWS Support.
