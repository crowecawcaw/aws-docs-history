# Setting up the CloudWatch agent to collect

cluster metrics

###### Important

If you are installing Container Insights on on Amazon EKS cluster, we recommend that
you use the Amazon CloudWatch Observability EKS add-on for the installation, instead of using
the instructions in this section. For more information and instructions, see [Quick start with the Amazon CloudWatch
Observability EKS add-on](Container-Insights-setup-EKS-addon.md "Container-Insights-setup-EKS-addon.md").

To set up Container Insights to collect metrics, you can follow the steps in [Quick Start setup for
Container Insights on Amazon EKS and Kubernetes](Container-Insights-setup-EKS-quickstart.md "Container-Insights-setup-EKS-quickstart.md") or you can follow the steps
in this section. In the following steps, you set up the CloudWatch agent to be able to collect
metrics from your clusters.

If you are installing in an Amazon EKS cluster and you use the instructions in this
section on or after November 6, 2023, you install Container Insights with enhanced
observability for Amazon EKS in the cluster.

## Step 1: Create a namespace for CloudWatch

Use the following step to create a Kubernetes namespace called
`amazon-cloudwatch` for CloudWatch. You can skip this step if you have already
created this namespace.

###### To create a namespace for CloudWatch

- Enter the following command.

```
kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/latest/k8s-deployment-manifest-templates/deployment-mode/daemonset/container-insights-monitoring/cloudwatch-namespace.yaml
```

## Step 2: Create a service account in the

cluster

Use one of the following methods to create a service account for the CloudWatch agent,
if you do not already have one.

- Use `kubectl`
- Use a `kubeconfig` file

### Use `kubectl` for authentication

###### To use `kubectl` to create a service account for the CloudWatch

agent

- Enter the following command.

```
kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/latest/k8s-deployment-manifest-templates/deployment-mode/daemonset/container-insights-monitoring/cwagent/cwagent-serviceaccount.yaml
```

If you didn't follow the previous steps, but you already have a service account
for the CloudWatch agent that you want to use, you must ensure that it has the following
rules. Additionally, in the rest of the steps in the Container Insights
installation, you must use the name of that service account instead of
`cloudwatch-agent`.

```
rules:
  - apiGroups: [""]
    resources: ["pods", "nodes", "endpoints"]
    verbs: ["list", "watch"]
  - apiGroups: [ "" ]
    resources: [ "services" ]
    verbs: [ "list", "watch" ]
  - apiGroups: ["apps"]
    resources: ["replicasets", "daemonsets", "deployments", "statefulsets"]
    verbs: ["list", "watch"]
  - apiGroups: ["batch"]
    resources: ["jobs"]
    verbs: ["list", "watch"]
  - apiGroups: [""]
    resources: ["nodes/proxy"]
    verbs: ["get"]
  - apiGroups: [""]
    resources: ["nodes/stats", "configmaps", "events"]
    verbs: ["create", "get"]
  - apiGroups: [""]
    resources: ["configmaps"]
    resourceNames: ["cwagent-clusterleader"]
    verbs: ["get","update"]
  - nonResourceURLs: ["/metrics"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [ "discovery.k8s.io" ]
    resources: [ "endpointslices" ]
    verbs: [ "list", "watch", "get" ]

```

### Use `kubeconfig` for

authentication

Alternatively, you can use a `kubeconfig` file for authentication.
This method allows you to bypass the need for a service account b directly
specifying the `kubeconfig` path in your CloudWatch agent configuration. It
also allows you to remove your dependency on the Kubernetes control plane API for
authentication, streamlining your setup and potentially increasing security by
managing authentication through your kubeconfig file.

To use this method, update your CloudWatch agent configuration file to specify the
path to your `kubeconfig` file, as in the following example.

```
{
  "logs": {
    "metrics_collected": {
      "kubernetes": {
        "cluster_name": "`YOUR_CLUSTER_NAME`",
        "enhanced_container_insights": false,
        "accelerated_compute_metrics": false,
        "tag_service": false,
        "kube_config_path": "/path/to/your/kubeconfig"
        "host_ip": "`HOSTIP`"
      }
    }
  }
}
```

To create a `kubeconfig` file, create a Certificate Signing Request
(CSR) for the `admin/{create_your_own_user}` user with the
`system:masters` Kubernetes role. Then sign with Kubernetes cluster’s
Certificate Authority (CA) and create the `kubeconfig` file.

## Step 3: Create a ConfigMap for the CloudWatch

agent

Use the following steps to create a ConfigMap for the CloudWatch agent.

###### To create a ConfigMap for the CloudWatch agent

1. Download the ConfigMap YAML to your `kubectl` client host by
   running the following command:

```
curl -O https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/latest/k8s-deployment-manifest-templates/deployment-mode/daemonset/container-insights-monitoring/cwagent/cwagent-configmap-enhanced.yaml
```

2. Edit the downloaded YAML file, as follows:
   - **cluster_name** – In the
     `kubernetes` section, replace `{{cluster_name}}` with
     the name of your cluster. Remove the `{{}}` characters.
     Alternatively, if you're using an Amazon EKS cluster, you can delete the
     `"cluster_name"` field and value. If you do, the CloudWatch agent
     detects the cluster name from the Amazon EC2 tags.

3. (Optional) Make further changes to the ConfigMap based on your monitoring
   requirements, as follows:
   - **metrics_collection_interval** – In
     the `kubernetes` section, you can specify how often the agent
     collects metrics. The default is 60 seconds. The default cadvisor collection
     interval in kubelet is 15 seconds, so don't set this value to less than 15
     seconds.
   - **endpoint_override** – In the
     `logs` section, you can specify the CloudWatch Logs endpoint if you want to
     override the default endpoint. You might want to do this if you're publishing
     from a cluster in a VPC and you want the data to go to a VPC endpoint.
   - **force_flush_interval** – In the
     `logs` section, you can specify the interval for batching log
     events before they are published to CloudWatch Logs. The default is 5 seconds.
   - **region** – By default, the agent
     published metrics to the Region where the worker node is located. To override
     this, you can add a `region` field in the `agent`
     section: for example, `"region":"us-west-2"`.
   - **statsd** section – If you want the
     CloudWatch Logs agent to also run as a StatsD listener in each worker node of your
     cluster, you can add a `statsd` section to the `metrics`
     section, as in the following example. For information about other StatsD
     options for this section, see [Retrieve custom metrics with
     StatsD](CloudWatch-Agent-custom-metrics-statsd.md "CloudWatch-Agent-custom-metrics-statsd.md").

   ```
   "metrics": {
     "metrics_collected": {
       "statsd": {
         "service_address":":8125"
       }
     }
   }
   ```

   A full example of the JSON section is as follows. If you're using a
   `kubeconfig` file for authentication, add the
   `kube_config_path` parameter to specify the path to your
   kubeconfig file.

   ```
   {
       "agent": {
           "region": "us-east-1"
       },
       "logs": {
           "metrics_collected": {
               "kubernetes": {
                   "cluster_name": "MyCluster",
                   "metrics_collection_interval": 60,
                   "kube_config_path": "`/path/to/your/kubeconfig`" //if using kubeconfig for authentication
               }
           },
           "force_flush_interval": 5,
           "endpoint_override": "logs.us-east-1.amazonaws.com"
       },
       "metrics": {
           "metrics_collected": {
               "statsd": {
                   "service_address": ":8125"
               }
           }
       }
   }
   ```

4. Create the ConfigMap in the cluster by running the following command.

```
kubectl apply -f cwagent-configmap-enhanced.yaml
```

## Step 4: Deploy the CloudWatch agent as a

DaemonSet

To finish the installation of the CloudWatch agent and begin collecting container
metrics, use the following steps.

###### To deploy the CloudWatch agent as a DaemonSet

1. - If you do not want to use StatsD on the cluster, enter the following
     command.

   ```
   kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/latest/k8s-deployment-manifest-templates/deployment-mode/daemonset/container-insights-monitoring/cwagent/cwagent-daemonset.yaml
   ```

   - If you do want to use StatsD, follow these steps:
     1. Download the DaemonSet YAML to your `kubectl` client host
        by running the following command.

     ```
     curl -O  https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/latest/k8s-deployment-manifest-templates/deployment-mode/daemonset/container-insights-monitoring/cwagent/cwagent-daemonset.yaml
     ```

     2. Uncomment the `port` section in the
        `cwagent-daemonset.yaml` file as in the following:

     ```
     ports:
       - containerPort: 8125
         hostPort: 8125
         protocol: UDP

     ```

     3. Deploy the CloudWatch agent in your cluster by running the following
        command.

     ```
     kubectl apply -f cwagent-daemonset.yaml
     ```

     4. Deploy the CloudWatch agent on Windows nodes in your cluster by running the
        following command. The StatsD listener is not supported on the CloudWatch agent
        on Windows.

     ```
     kubectl apply -f cwagent-daemonset-windows.yaml
     ```

2. Validate that the agent is deployed by running the following command.

```
kubectl get pods -n amazon-cloudwatch
```

When complete, the CloudWatch agent creates a log group named
`/aws/containerinsights/`Cluster_Name`/performance`
and sends the performance log events to this log group. If you also set up the agent
as a StatsD listener, the agent also listens for StatsD metrics on port 8125 with the
IP address of the node where the application pod is scheduled.

### Troubleshooting

If the agent doesn't deploy correctly, try the following:

- Run the following command to get the list of pods.

```
kubectl get pods -n amazon-cloudwatch
```

- Run the following command and check the events at the bottom of the
  output.

```
kubectl describe pod `pod-name` -n amazon-cloudwatch
```

- Run the following command to check the logs.

```
kubectl logs `pod-name`  -n amazon-cloudwatch
```
