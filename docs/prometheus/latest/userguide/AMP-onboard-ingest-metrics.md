# Ingest Prometheus metrics to the

workspace

One way to ingest metrics is to use a standalone Prometheus _agent_
(a Prometheus instance running in agent mode) to scrape metrics from your cluster and
forward them to Amazon Managed Service for Prometheus for storage and monitoring. This section explains how to set
up the ingestion of metrics into your Amazon Managed Service for Prometheus workspace from Amazon EKS by setting up a new
instance of Prometheus agent using Helm.

To generate metrics in Amazon EKS, such as Kubernetes or node-level metrics, you can use
the Amazon EKS community add-ons. For more information, see [Available community add-ons](../../../eks/latest/userguide/community-addons.md#_available_community_add_ons "../../../eks/latest/userguide/community-addons.md#_available_community_add_ons") in the _Amazon EKS User Guide_.

For information about other ways to ingest data into Amazon Managed Service for Prometheus, including how to
secure metrics and create high-availability metrics, see [Ingest metrics to your Amazon Managed Service for Prometheus
workspace](AMP-ingest-methods.md "AMP-ingest-methods.md").

###### Note

Metrics ingested into a workspace are stored for 150 days by default, and are then
automatically deleted. You can adjust the retention period by configuring your
workspace up to a maximum of 1095 days (three years). For more information, see
[Configure
your workspace](AMP-workspace-configuration.md "AMP-workspace-configuration.md").

The instructions in this section get you up and running with Amazon Managed Service for Prometheus quickly. It
assumes that you have already [created a
workspace](AMP-onboard-create-workspace.md "AMP-onboard-create-workspace.md"). In this section, you set up a new Prometheus server in an Amazon EKS
cluster, and the new server uses a default configuration to act as an agent to send
metrics to Amazon Managed Service for Prometheus. This method has the following prerequisites:

- You must have an Amazon EKS cluster from which the new Prometheus server will
  collect metrics.
- Your Amazon EKS cluster must have an [Amazon EBS CSI driver](../../../eks/latest/userguide/ebs-csi.md "../../../eks/latest/userguide/ebs-csi.md") installed
  (required by Helm).
- You must use Helm CLI 3.0 or later.
- You must use a Linux or MacOS computer to perform the steps in the following
  sections.

## Step 1: Add new Helm chart

repositories

To add new Helm chart repositories, enter the following commands. For more
information about these commands, see [Helm Repo](https://helm.sh/docs/helm/helm_repo/ "https://helm.sh/docs/helm/helm_repo/").

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add kube-state-metrics https://kubernetes.github.io/kube-state-metrics
helm repo update
```

## Step 2: Create a Prometheus

namespace

Enter the following command to create a Prometheus namespace for the Prometheus
server and other monitoring components. Replace
`prometheus-agent-namespace` with the name that you
want for this namespace.

```
kubectl create namespace `prometheus-agent-namespace`
```

## Step 3: Set up IAM roles for

service accounts

For this method of ingestion, you need to use IAM roles for service accounts in
the Amazon EKS cluster where the Prometheus agent is running.

With IAM roles for service accounts, you can associate an IAM role with a
Kubernetes service account. This service account can then provide AWS permissions
to the containers in any pod that uses that service account. For more information,
see [IAM roles for
service accounts](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md").

If you have not already set up these roles, follow the instructions at [Set up service roles for the ingestion of metrics
from Amazon EKS clusters](set-up-irsa.md#set-up-irsa-ingest "set-up-irsa.md#set-up-irsa-ingest") to set up the
roles. The instructions in that section require the use of `eksctl`. For
more information, see [Getting started with
Amazon Elastic Kubernetes Service – `eksctl`](../../../eks/latest/userguide/getting-started-eksctl.md "../../../eks/latest/userguide/getting-started-eksctl.md").

###### Note

When you are not on EKS or AWS and using just access key and secret key to
access Amazon Managed Service for Prometheus, you cannot use the `EKS-IAM-ROLE` based
SigV4.

## Step 4: Set up the

new server and start ingesting metrics

To install the new Prometheus agent and send metrics to your Amazon Managed Service for Prometheus workspace,
follow these steps.

###### To install a new Prometheus agent and send metrics to your Amazon Managed Service for Prometheus

workspace

1. Use a text editor to create a file named
   `my_prometheus_values_yaml` with the following
   content.
   - Replace `IAM_PROXY_PROMETHEUS_ROLE_ARN`
     with the ARN of the **amp-iamproxy-ingest-role**
     that you created in [Set up service roles for the ingestion of metrics
     from Amazon EKS clusters](set-up-irsa.md#set-up-irsa-ingest "set-up-irsa.md#set-up-irsa-ingest").
   - Replace `WORKSPACE_ID` with the ID of
     your Amazon Managed Service for Prometheus workspace.
   - Replace `REGION` with the Region of your
     Amazon Managed Service for Prometheus workspace.

```
## The following is a set of default values for prometheus server helm chart which enable remoteWrite to AMP
## For the rest of prometheus helm chart values see: https://github.com/prometheus-community/helm-charts/blob/main/charts/prometheus/values.yaml
##
serviceAccounts:
  server:
    name: amp-iamproxy-ingest-service-account
    annotations:
      eks.amazonaws.com/role-arn: ${IAM_PROXY_PROMETHEUS_ROLE_ARN}
server:
  remoteWrite:
    - url: https://aps-workspaces.${REGION}.amazonaws.com/workspaces/${WORKSPACE_ID}/api/v1/remote_write
      sigv4:
        region: ${REGION}
      queue_config:
        max_samples_per_send: 1000
        max_shards: 200
        capacity: 2500
```

2. Enter the following command to create the Prometheus server.
   - Replace `prometheus-chart-name` with your
     Prometheus release name.
   - Replace `prometheus-agent-namespace` with
     the name of your Prometheus namespace.

```
helm install `prometheus-chart-name` prometheus-community/prometheus -n `prometheus-agent-namespace` \
-f my_prometheus_values_yaml
```
