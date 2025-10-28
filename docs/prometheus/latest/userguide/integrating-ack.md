# Manage Amazon Managed Service for Prometheus with AWS Controllers for Kubernetes

Amazon Managed Service for Prometheus is integrated with [AWS Controllers for Kubernetes
(ACK)](https://aws-controllers-k8s.github.io/community/docs/community/overview/ "https://aws-controllers-k8s.github.io/community/docs/community/overview/"), with support for managing your workspace,
Alert Manager, and Ruler resources in Amazon EKS. You can use AWS Controllers for Kubernetes custom resource
definitions (CRDs) and native Kubernetes objects without having to define any resources
outside of your cluster.

This section describes how to set up AWS Controllers for Kubernetes and Amazon Managed Service for Prometheus in an existing Amazon EKS
cluster.

You can also read the blog posts [introducing AWS Controllers for Kubernetes](https://aws.amazon.com/blogs/containers/aws-controllers-for-kubernetes-ack/ "https://aws.amazon.com/blogs/containers/aws-controllers-for-kubernetes-ack/")
and [introducing the ACK controller for Amazon Managed Service for Prometheus](https://aws.amazon.com/blogs/mt/introducing-the-ack-controller-for-amazon-managed-service-for-prometheus/ "https://aws.amazon.com/blogs/mt/introducing-the-ack-controller-for-amazon-managed-service-for-prometheus/").

## Prerequisites

Before starting to integrate AWS Controllers for Kubernetes and Amazon Managed Service for Prometheus with your Amazon EKS cluster, you must have
the following prerequisites.

- You must have an [existing AWS account and
  permissions](AMP-setting-up.md "AMP-setting-up.md") to create Amazon Managed Service for Prometheus and IAM roles programmatically.
- You must have an existing [Amazon EKS
  cluster](../../../eks/latest/userguide/getting-started-console.md "../../../eks/latest/userguide/getting-started-console.md") with OpenID Connect (OIDC)
  enabled.

If you do not have OIDC enabled, you can use the following command to
enable it. Remember to replace the
`YOUR_CLUSTER_NAME` and
`AWS_REGION` with the correct values for your
account.

```
eksctl utils associate-iam-oidc-provider \
    --cluster ${`YOUR_CLUSTER_NAME`} --region ${`AWS_REGION`} \
    --approve
```

For more information about using OIDC with Amazon EKS, see [OIDC
identity provider authentication](../../../eks/latest/userguide/authenticate-oidc-identity-provider.md "../../../eks/latest/userguide/authenticate-oidc-identity-provider.md") and [Creating
an IAM OIDC provider](../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md "../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md") in the _Amazon EKS User Guide_.

- You must have the [Amazon EBS CSI driver installed](../../../eks/latest/userguide/ebs-csi.md "../../../eks/latest/userguide/ebs-csi.md")
  in your Amazon EKS cluster.
- You must have the [AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  installed. The AWS CLI is used to call AWS functionality from the
  command line.
- [Helm](../../../eks/latest/userguide/helm.md "../../../eks/latest/userguide/helm.md"), the package manager for
  Kubernetes, must be installed.
- [Control plane metrics with
  Prometheus](../../../eks/latest/userguide/prometheus.md "../../../eks/latest/userguide/prometheus.md") must be set up in your Amazon EKS cluster.
- You must have an [Amazon Simple Notification Service
  (Amazon SNS)](../../../sns.md "../../../sns.md") topic where you want to send alerts from your new workspace.
  Make sure that you have [given Amazon Managed Service for Prometheus
  permission to send messages to the topic](AMP-alertmanager-receiver-AMPpermission.md "AMP-alertmanager-receiver-AMPpermission.md").

When your Amazon EKS cluster is configured appropriately, you should be able to see
metrics formatted for Prometheus by calling `kubectl get --raw 
 /metrics`. Now you are ready to install an AWS Controllers for Kubernetes service controller
and use it to deploy Amazon Managed Service for Prometheus resources.

## Deploying a workspace with AWS Controllers for Kubernetes

To deploy a new Amazon Managed Service for Prometheus workspace, you will install an AWS Controllers for Kubernetes controller, and
then use that to create the workspace.

###### To deploy a new Amazon Managed Service for Prometheus workspace with AWS Controllers for Kubernetes

1. Use the following commands to use Helm to install the Amazon Managed Service for Prometheus
   service controller. For more information see [Install an ACK Controller](https://aws-controllers-k8s.github.io/community/docs/user-docs/install/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/install/") in the AWS Controllers for Kubernetes documentation on GitHub.
   Use the correct `region` for your system, such as
   `us-east-1`.

```
export SERVICE=prometheusservice
export RELEASE_VERSION=`curl -sL https://api.github.com/repos/aws-controllers-k8s/$SERVICE-controller/releases/latest | jq -r '.tag_name | ltrimstr("v")'`
export ACK_SYSTEM_NAMESPACE=ack-system
export AWS_REGION=`region`

aws ecr-public get-login-password --region us-east-1 | helm registry login --username AWS --password-stdin public.ecr.aws
helm install --create-namespace -n $ACK_SYSTEM_NAMESPACE ack-$SERVICE-controller \
  oci://public.ecr.aws/aws-controllers-k8s/$SERVICE-chart --version=$RELEASE_VERSION --set=aws.region=$AWS_REGION
```

After a few moments, you should see a response similar to the following
indicating success.

```
You are now able to create Amazon Managed Service for Prometheus (AMP) resources!
The controller is running in "cluster" mode.
The controller is configured to manage AWS resources in region: "us-east-1"
```

You can optionally verify that the AWS Controllers for Kubernetes controller has been
successfully installed with the following command.

```
helm list --namespace $ACK_SYSTEM_NAMESPACE -o yaml
```

This will return information about the controller
`ack-prometheusservice-controller`, including the `status:
 deployed`. 2. Create a file called `workspace.yaml` with the following text.
This will be used as configuration for the workspace you are creating.

```
apiVersion: prometheusservice.services.k8s.aws/v1alpha1
kind: Workspace
metadata:
  name: my-amp-workspace
spec:
  alias: my-amp-workspace
  tags:
    ClusterName: EKS-demo
```

3. Run the following command to create your workspace (this command depends on
   the system variables that you set up in step 1).

```
kubectl apply -f workspace.yaml -n $ACK_SYSTEM_NAMESPACE
```

Within a few moments, you should be able to see a new workspace, called
`my-amp-workspace` in your account.

Running the following command to view the details and status of your
workspace including the _workspace ID_. Alternately, you
can view the new workspace in the [Amazon Managed Service for Prometheus console](https://console.aws.amazon.com/prometheus "https://console.aws.amazon.com/prometheus").

```
kubectl describe workspace my-amp-workspace -n $ACK_SYSTEM_NAMESPACE
```

###### Note

You can also [use an existing workspace](https://aws-controllers-k8s.github.io/community/docs/user-docs/adopted-resource/ "https://aws-controllers-k8s.github.io/community/docs/user-docs/adopted-resource/") rather than create a new one. 4. Create two new yaml files as configuration for the Rulegroups and
AlertManager that you will create next using the following configuration.

Save this configuration as `rulegroup.yaml`. Replace
`WORKSPACE-ID` with the workspace ID from the previous
step.

```
apiVersion: prometheusservice.services.k8s.aws/v1alpha1
kind: RuleGroupsNamespace
metadata:
  name: default-rule
spec:
  workspaceID: `WORKSPACE-ID`
  name: default-rule
  configuration: |
    groups:
    - name: example
      rules:
      - alert: HostHighCpuLoad
        expr: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[2m])) * 100) > 60
        for: 5m
        labels:
          severity: warning
          event_type: scale_up
        annotations:
          summary: Host high CPU load (instance {{ $labels.instance }})
          description: "CPU load is > 60%\n  VALUE = {{ $value }}\n  LABELS = {{ $labels }}"
      - alert: HostLowCpuLoad
        expr: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[2m])) * 100) < 30
        for: 5m
        labels:
          severity: warning
          event_type: scale_down
        annotations:
          summary: Host low CPU load (instance {{ $labels.instance }})
          description: "CPU load is < 30%\n  VALUE = {{ $value }}\n  LABELS = {{ $labels }}"
```

Save the following configuration as `alertmanager.yaml`. Replace
`WORKSPACE-ID` with the workspace ID from the
previous step. Replace `TOPIC-ARN` with the ARN for the
Amazon SNS topic to send notifications to, and `REGION` with
the AWS Region you are using. Remember that Amazon Managed Service for Prometheus [must have permissions](AMP-alertmanager-receiver-AMPpermission.md "AMP-alertmanager-receiver-AMPpermission.md")
to the Amazon SNS topic.

```
apiVersion: prometheusservice.services.k8s.aws/v1alpha1
kind: AlertManagerDefinition
metadata:
  name: alert-manager
spec:
  workspaceID: `WORKSPACE-ID`
  configuration: |
    alertmanager_config: |
      route:
         receiver: default_receiver
      receivers:
        - name: default_receiver
          sns_configs:
          - topic_arn: `TOPIC-ARN`
            sigv4:
              region: `REGION`
            message: |
              alert_type: {{ .CommonLabels.alertname }}
              event_type: {{ .CommonLabels.event_type }}
```

###### Note

To learn more about the formats of these configuration files, see
[RuleGroupsNamespaceData](../APIReference/yaml-RuleGroupsNamespaceData.md "../APIReference/yaml-RuleGroupsNamespaceData.md") and
[AlertManagerDefinitionData](../APIReference/yaml-AlertManagerDefinitionData.md "../APIReference/yaml-AlertManagerDefinitionData.md"). 5. Run the following commands to create your rule group and alert manager
configuration (this command depends on the system variables that you set up
in step 1).

```
kubectl apply -f rulegroup.yaml -n $ACK_SYSTEM_NAMESPACE
kubectl apply -f alertmanager.yaml -n $ACK_SYSTEM_NAMESPACE
```

The changes will be available within a few moments.

###### Note

To update a resource, rather than create it, you simply update the yaml
file, and run the `kubectl apply` command again.

To delete a resource, run the following command.
Replace `ResourceType` with the type of resource
you want to delete `Workspace`, `AlertManagerDefinition`,
or `RuleGroupNamespace`. Replace
`ResourceName` with the name of the resource to
delete.

```
kubectl delete `ResourceType` `ResourceName` -n $ACK_SYSTEM_NAMESPACE
```

That completes deploying the new workspace. The next section describes configuring
your cluster to send metrics to that workspace.

## Configuring your Amazon EKS cluster to write to

the Amazon Managed Service for Prometheus workspace

This section describes how to use Helm to configure the Prometheus running in your
Amazon EKS cluster to remote write metrics to the Amazon Managed Service for Prometheus workspace that you created in
the previous section.

For this procedure, you will need the name of the IAM role you have created to use
for ingesting metrics. If you have not done this already, see [Set up service roles for the ingestion of metrics
from Amazon EKS clusters](set-up-irsa.md#set-up-irsa-ingest "set-up-irsa.md#set-up-irsa-ingest") for more
information and instructions. If you follow those instructions, the IAM role will
be called `amp-iamproxy-ingest-role`.

###### To configure your Amazon EKS cluster for remote write

1. Use the following command to get the `prometheusEndpoint` for your
   workspace. Replace `WORKSPACE-ID` with the workspace ID
   from the previous section.

```
aws amp describe-workspace --workspace-id `WORKSPACE-ID`
```

The prometheusEndpoint will be in the return results, and be formatted like
this:

```
https://aps-workspaces.us-west-2.amazonaws.com/workspaces/ws-a1b2c3d4-a123-b456-c789-ac1234567890/
```

Save this URL for use in the next few steps. 2. Create a new file with the following text and call it
`prometheus-config.yaml`. Replace `account`
with your account ID, `workspaceURL/` with the
URL you just found, and `region` with the appropriate
AWS Region for your system.

```
serviceAccounts:
        server:
            name: "amp-iamproxy-ingest-service-account"
            annotations:
                eks.amazonaws.com/role-arn: "arn:aws:iam::`account`:role/amp-iamproxy-ingest-role"
server:
    remoteWrite:
        - url: `workspaceURL/`api/v1/remote_write
          sigv4:
            region: `region`
          queue_config:
            max_samples_per_send: 1000
            max_shards: 200
            capacity: 2500
```

3. Find the Prometheus chart and namespace names as well as the chart version
   with the following Helm command.

```
helm ls --all-namespaces
```

Based on the steps so far, the Prometheus chart and namespace should both
be named `prometheus`, and the chart version may be
`15.2.0` 4. Run the following command, using the
`PrometheusChartName`,
`PrometheusNamespace`, and
`PrometheusChartVersion` found in the previous
step.

```
helm upgrade `PrometheusChartName` prometheus-community/prometheus -n `PrometheusNamespace` -f prometheus-config.yaml --version `PrometheusChartVersion`
```

After a few minutes, you'll see a message that the upgrade was successful. 5. Optionally, validate that metrics are succesfully being sent by querying
the Amazon Managed Service for Prometheus endpoint via `awscurl`. Replace
`Region` with the AWS Region that you are using,
and `workspaceURL/` with the URL you found in step 1.

```
awscurl --service="aps" --region="`Region`" "`workspaceURL/`api/v1/query?query=node_cpu_seconds_total"
```

You have now created an Amazon Managed Service for Prometheus workspace and connected to it from your Amazon EKS
cluster, using YAML files as configuration. These files, called custom resource
definitions (CRDs), live within your Amazon EKS cluster. You can use the AWS Controllers for Kubernetes
controller to manage all of your Amazon Managed Service for Prometheus resources directly from the cluster.
