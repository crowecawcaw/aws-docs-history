# Set up ingestion

from an existing Prometheus server in Kubernetes on EC2

Amazon Managed Service for Prometheus supports ingesting metrics from Prometheus servers in clusters running
Amazon EKS and in self-managed Kubernetes clusters running on Amazon EC2. The detailed
instructions in this section are for a Prometheus server in an Amazon EKS cluster. The
steps for a self-managed Kubernetes cluster on Amazon EC2 are the same, except that you
will need to set up the OIDC provider and IAM roles for service accounts yourself
in the Kubernetes cluster.

The instructions in this section use Helm as the Kubernetes package
manager.

###### Topics

- [Step 1: Set up IAM
  roles for service accounts](#AMP-onboard-existing-Prometheus-IRSA "#AMP-onboard-existing-Prometheus-IRSA")
- [Step 2:
  Upgrade your existing Prometheus server using Helm](#AMP-onboard-ingest-metrics-existing-remotewrite "#AMP-onboard-ingest-metrics-existing-remotewrite")

## Step 1: Set up IAM

roles for service accounts

For the method of onboarding that we are documenting, you need to use IAM
roles for service accounts in the Amazon EKS cluster where the Prometheus server is
running. These roles are also called _service roles_.

With service roles, you can associate an IAM role with a Kubernetes service
account. This service account can then provide AWS permissions to the
containers in any pod that uses that service account. For more information, see
[IAM roles
for service accounts](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md").

If you have not already set up these roles, follow the instructions at [Set up service roles for the ingestion of metrics
from Amazon EKS clusters](set-up-irsa.md#set-up-irsa-ingest "set-up-irsa.md#set-up-irsa-ingest") to set up
the roles.

## Step 2:

Upgrade your existing Prometheus server using Helm

The instructions in this section include setting up remote write and sigv4 to
authenticate and authorize the Prometheus server to remote write to your
Amazon Managed Service for Prometheus workspace.

### Using Prometheus version

2.26.0 or later

Follow these steps if you are using a Helm chart with Prometheus Server
image of version 2.26.0 or later.

###### To set up remote write from a Prometheus server using Helm

chart

1. Create a new remote write section in your Helm configuration
   file:
   - Replace `${IAM_PROXY_PROMETHEUS_ROLE_ARN}` with
     the ARN of the **amp-iamproxy-ingest-role**
     that you created in [Step 1: Set up IAM
     roles for service accounts](#AMP-onboard-existing-Prometheus-IRSA "#AMP-onboard-existing-Prometheus-IRSA").
     The role ARN should have the format of
     `arn:aws:iam::`your account
     ID`:role/amp-iamproxy-ingest-role`.
   - Replace `${WORKSPACE_ID}` with your Amazon Managed Service for Prometheus
     workspace ID.
   - Replace `${REGION}` with the Region of the
     Amazon Managed Service for Prometheus workspace (such as `us-west-2`).

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

2. Update your existing Prometheus Server configuration using
   Helm:
   - Replace `prometheus-chart-name` with your
     Prometheus release name.
   - Replace `prometheus-namespace` with the
     Kubernetes namespace where your Prometheus Server is
     installed.
   - Replace `my_prometheus_values_yaml` with the
     path to your Helm configuration file.
   - Replace `current_helm_chart_version` with the
     current version of your Prometheus Server Helm chart. You
     can find the current chart version by using the [helm
     list](https://helm.sh/docs/helm/helm_list/ "https://helm.sh/docs/helm/helm_list/") command.

```
helm upgrade `prometheus-chart-name` prometheus-community/prometheus \
       -n `prometheus-namespace` \
       -f `my_prometheus_values_yaml` \
       --version `current_helm_chart_version`
```

### Using earlier versions of

Prometheus

Follow these steps if you are using a version of Prometheus earlier than
2.26.0. These steps use a sidecar approach, because earlier versions of
Prometheus don't natively support AWS Signature Version 4 signing process
(AWS SigV4).

These instructions assume that you are using Helm to deploy
Prometheus.

###### To set up remote write from a Prometheus server

1. On your Prometheus server, create a new remote write
   configuration. First, create a new update file. We will call the
   file `amp_ingest_override_values.yaml`.

Add the following values to the YAML file.

```
serviceAccounts:
        server:
            name: "amp-iamproxy-ingest-service-account"
            annotations:
                eks.amazonaws.com/role-arn: "${SERVICE_ACCOUNT_IAM_INGEST_ROLE_ARN}"
    server:
        sidecarContainers:
            - name: aws-sigv4-proxy-sidecar
              image: public.ecr.aws/aws-observability/aws-sigv4-proxy:1.0
              args:
              - --name
              - aps
              - --region
              - ${REGION}
              - --host
              - aps-workspaces.${REGION}.amazonaws.com
              - --port
              - :8005
              ports:
              - name: aws-sigv4-proxy
                containerPort: 8005
        statefulSet:
            enabled: "true"
        remoteWrite:
            - url: http://localhost:8005/workspaces/${WORKSPACE_ID}/api/v1/remote_write
```

Replace `${REGION}` with the Region of the Amazon Managed Service for Prometheus
workspace.

Replace `${SERVICE_ACCOUNT_IAM_INGEST_ROLE_ARN}` with
the ARN of the **amp-iamproxy-ingest-role** that
you created in [Step 1: Set up IAM
roles for service accounts](#AMP-onboard-existing-Prometheus-IRSA "#AMP-onboard-existing-Prometheus-IRSA"). The role
ARN should have the format of `arn:aws:iam::`your
account
ID`:role/amp-iamproxy-ingest-role`.

Replace `${WORKSPACE_ID}` with your workspace
ID. 2. Upgrade your Prometheus Helm chart. First, find your Helm chart
name by entering the following command. In the output from this
command, look for a chart with a name that includes
`prometheus`.

```
helm ls --all-namespaces
```

Then enter the following command.

```
helm upgrade --install `prometheus-helm-chart-name` prometheus-community/prometheus -n `prometheus-namespace` -f ./amp_ingest_override_values.yaml
```

Replace `prometheus-helm-chart-name` with
the name of the Prometheus helm chart returned in the previous
command. Replace `prometheus-namespace`
with the name of your namespace.

#### Downloading Helm

charts

If you don't already have Helm charts downloaded locally, you can use
the following command to download them.

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm pull prometheus-community/prometheus --untar
```
