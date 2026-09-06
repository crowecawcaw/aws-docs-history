

# Attaching Ray cluster to Space
<a name="sagemaker-hyperpod-ray-attach-space"></a>

Attaching a Ray cluster to a space points your IDE or notebook session at that cluster, so `ray.init()` connects to it. Inside the space, the cluster is reachable on port 8265 for interactive development, the same port a local Ray cluster uses. You get the experience of running Ray on a laptop, with cloud-scale compute behind it.

You manage the connection from the **Ray cluster** tab inside the space.

## Prerequisites
<a name="sagemaker-hyperpod-ray-attach-space-prereqs"></a>
+ (Optional) Amazon SageMaker Studio configured for your cluster. For more information, see [Setting up Studio for Ray](sagemaker-hyperpod-ray-studio-setup.md).
+ The SageMaker Spaces add-on is **Active**. For more information, see [Setting up the Spaces add-on](sagemaker-hyperpod-ray-spaces-addon-setup.md).
+ A JupyterLab or Code Editor space, created from the **IDE and Notebooks** tab in Amazon SageMaker Studio.
+ A running Ray cluster in the same namespace as the space pods.

## Connect a space to a Ray cluster with Amazon SageMaker Studio
<a name="sagemaker-hyperpod-ray-attach-space-connect"></a>

**To attach a space to a Ray cluster**

1. Open the JupyterLab or Code Editor space you created under the **IDE and Notebooks** tab in Studio, then choose the **Ray cluster** tab.

1. Choose **Connect**.

1. Choose an existing cluster from the picker, or create a new one, then save.

Use **Change** to point the space at a different cluster, and **Disconnect** to detach it.

**Important**  
Saving a connection change restarts the space pods. Save unsaved work first.

## Connect a space to a Ray cluster with kubectl
<a name="sagemaker-hyperpod-ray-attach-space-kubectl"></a>

You can also patch the space's `Workspace` resource with `kubectl` instead of using Studio. The Ray integration template lives in the `jupyter-k8s-system` namespace, and you pass the Ray cluster name as a parameter.

Replace the following values in both commands:


| Placeholder | Replace with | 
| --- | --- | 
| my-workspace | The name of the space's Workspace resource. | 
| my-namespace | The namespace that holds both the space and the Ray cluster. | 
| my-cluster | The name of the RayCluster to attach. | 

Leave `ray-integration` and `jupyter-k8s-system` as they are. They identify the integration template the add-on installs.

```
kubectl patch workspace {{my-workspace}} -n {{my-namespace}} --type=merge -p '{
  "spec": {
    "integrationTemplateRefs": [
      {
        "name": "ray-integration",
        "namespace": "jupyter-k8s-system",
        "parameters": [
          { "name": "rayClusterName", "value": "{{my-cluster}}" }
        ]
      }
    ]
  }
}'
```

To detach the space from its cluster, clear the integration references.

```
kubectl patch workspace {{my-workspace}} -n {{my-namespace}} --type=merge -p '{"spec":{"integrationTemplateRefs":[]}}'
```

## Verify
<a name="sagemaker-hyperpod-ray-attach-space-verify"></a>

After you connect the space, `ray.init()` and `ray job submit` reach the attached cluster by default. Open a terminal or notebook in the space and run `ray.init()`. Confirm that it connects to the cluster.

## Version compatibility
<a name="sagemaker-hyperpod-ray-attach-space-compat"></a>

The space's SageMaker AI Distribution image carries its own Ray version, and it must match the cluster's `spec.rayVersion`. When the versions differ, Studio shows a warning and offers to create a compatible cluster instead.

The Python version must match as well, including the patch version. A space running Python 3.11.9 and a cluster running Python 3.11.4 are not compatible.

A version mismatch surfaces as errors during development. For a simpler experience you can choose the same SageMaker AI Distribution image for both the Ray cluster and the Space Image to ensure compatibility.