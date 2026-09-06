

# Set up ingestion from a new Prometheus server using Helm
<a name="AMP-onboard-ingest-metrics-new-Prometheus"></a>

The instructions in this section get you up and running with Amazon Managed Service for Prometheus quickly. You set up a new Prometheus server in an Amazon EKS cluster, and the new server uses a default configuration to send metrics to Amazon Managed Service for Prometheus. This method has the following prerequisites:
+ You must have an Amazon EKS cluster from which the new Prometheus server will collect metrics.
+ Your Amazon EKS cluster must have an [Amazon EBS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) installed (required by Helm).
+ You must use Helm CLI 3.0 or later.
+ You must use a Linux or macOS computer to perform the steps in the following sections.

## Step 1: Add new Helm chart repositories
<a name="AMP-onboard-new-Prometheus-HelmRepo"></a>

To add new Helm chart repositories, enter the following commands. For more information about these commands, see [Helm Repo](https://helm.sh/docs/helm/helm_repo/).

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add kube-state-metrics https://kubernetes.github.io/kube-state-metrics
helm repo update
```

## Step 2: Create a Prometheus namespace
<a name="AMP-onboard-new-Prometheus-namespace"></a>

Enter the following command to create a Prometheus namespace for the Prometheus server and other monitoring components. Replace {{prometheus-namespace}} with the name that you want for this namespace.

```
kubectl create namespace {{prometheus-namespace}}
```

## Step 3: Set up IAM roles for service accounts
<a name="AMP-onboard-new-Prometheus-IRSA"></a>

For the method of onboarding that we are documenting, you need to use IAM roles for service accounts in the Amazon EKS cluster where the Prometheus server is running. 

With IAM roles for service accounts, you can associate an IAM role with a Kubernetes service account. This service account can then provide AWS permissions to the containers in any pod that uses that service account. For more information, see [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

If you have not already set up these roles, follow the instructions at [Set up service roles for the ingestion of metrics from Amazon EKS clusters](set-up-irsa.md#set-up-irsa-ingest) to set up the roles. The instructions in that section require the use of `eksctl`. For more information, see [Getting started with Amazon Elastic Kubernetes Service – `eksctl`](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html). 

**Note**  
When you are not on EKS or AWS and using just access key and secret key to access Amazon Managed Service for Prometheus, you cannot use the `EKS-IAM-ROLE` based SigV4.

## Step 4: Set up the new server and start ingesting metrics
<a name="AMP-onboard-ingest-metrics-new-Prometheus-Helm"></a>

To install the new Prometheus server that sends metrics to your Amazon Managed Service for Prometheus workspace, follow these steps.

**To install a new Prometheus server to send metrics to your Amazon Managed Service for Prometheus workspace**

1. Use a text editor to create a file named `my_prometheus_values_yaml` with the following content.
   + Replace {{IAM\_PROXY\_PROMETHEUS\_ROLE\_ARN}} with the ARN of the **amp-iamproxy-ingest-role** that you created in [Set up service roles for the ingestion of metrics from Amazon EKS clusters](set-up-irsa.md#set-up-irsa-ingest).
   + Replace {{WORKSPACE\_ID}} with the ID of your Amazon Managed Service for Prometheus workspace.
   + Replace {{REGION}} with the Region of your Amazon Managed Service for Prometheus workspace.

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

1. Enter the following command to create the Prometheus server.
   + Replace {{prometheus-chart-name}} with your Prometheus release name.
   + Replace {{prometheus-namespace}} with the name of your Prometheus namespace.

   ```
   helm install {{prometheus-chart-name}} prometheus-community/prometheus -n {{prometheus-namespace}} \
   -f my_prometheus_values_yaml
   ```
**Note**  
You can customize the `helm install` command in many ways. For more information, see [Helm install](https://helm.sh/docs/helm/helm_install/) in the *Helm documentation*.