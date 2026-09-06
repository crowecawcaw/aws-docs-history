

# Generating a dashboard connection URL
<a name="sagemaker-hyperpod-ray-dashboard-connection-url"></a>

A dashboard connection URL is an authenticated link to a Ray cluster's dashboard. You create a `RayDashboardConnection` resource for the cluster, and the endpoint operator returns the URL on the resource status.

## Prerequisites
<a name="sagemaker-hyperpod-ray-dashboard-connection-url-prereqs"></a>
+ The SageMaker HyperPod Ray Endpoint Operator is installed. For more information, see [Installing the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator.md).

You can generate the URL with the HyperPod CLI, which is simpler than creating the resource directly, or create the `RayDashboardConnection` resource with `kubectl`.

To generate the URL with the HyperPod CLI, run:

```
hyp create ray-dashboard-connection \
  --cluster-name {{my-cluster}} \
  --namespace {{my-namespace}}
```

The command returns a short-lived presigned URL. Open it in a browser.

**To create the connection resource with kubectl**

1. Create the connection resource and read the URL from its status.

   ```
   kubectl create -o jsonpath='{.status.connectionUrl}' -f - <<EOF
   apiVersion: connection.access.sagemaker.amazonaws.com/v1alpha1
   kind: RayDashboardConnection
   metadata:
     namespace: {{my-namespace}}
   spec:
     clusterName: {{my-cluster}}
   EOF
   ```

1. Open the returned URL in a browser.

The URL carries a short-lived token. The browser exchanges it for a session cookie that is valid for up to six hours, after which you generate a new URL.

**Note**  
Choosing **Ray Dashboard** for a cluster in Studio generates this URL for you.