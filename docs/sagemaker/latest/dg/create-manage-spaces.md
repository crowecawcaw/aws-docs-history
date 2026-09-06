

# Create and manage spaces
<a name="create-manage-spaces"></a>

Data scientists can list to view all the spaces they have access to, create a space using one of the templates, update space to update the image, file system, and other attributes of space configuration, and delete a space. As a prerequisite, customers must install HyperPod CLI or use kubectl to create and manage spaces. For more details on HyperPod CLI, please see [this](https://github.com/aws/sagemaker-hyperpod-cli/blob/main/README.md#space). To use kubectl commands, please refer to [this guide](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) to install kubectl.

## Create space
<a name="create-manage-spaces-create"></a>

**HyperPod CLI**

Create a Jupyter space

```
hyp create hyp-space \ 
    --name myspace \ 
    --display-name "My Space" \ 
    --memory 8Gi \ 
    --template-ref name=sagemaker-jupyter-template,namespace=jupyter-k8s-system
```

Create a Code Editor space

```
hyp create hyp-space \ 
    --name myspace \ 
    --display-name "My Space" \ 
    --memory 8Gi \ 
    --template-ref name=sagemaker-code-editor-template,namespace=jupyter-k8s-system
```

**kubectl**

```
kubectl apply -f - <<EOF
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  name: my-space
spec:
  displayName: my-space
  desiredStatus: Running
EOF
```

or you can simply apply the yaml file

```
kubectl apply -f my-workspace.yaml
```

## List spaces
<a name="create-manage-spaces-list"></a>

**HyperPod CLI**

```
hyp list hyp-space
```

**kubectl**

```
kubectl get workspaces -n <workspace-namespace> 
```

## Describe a space
<a name="create-manage-spaces-describe"></a>

**HyperPod CLI**

```
hyp describe hyp-space --name myspace
```

**kubectl**

```
# Basic Status reporting
kubectl get workspace my-workspace -n <workspace-namespace>

# Enhanced Workspace Information Retrieval 
kubectl get workspace my-workspace -n <workspace-namespace> -o wide

# Complete Workspace Information Retrieval
kubectl get workspace my-workspace -n <workspace-namespace> -o json
kubectl get workspace my-workspace -n <workspace-namespace> -o yaml
```

## Update a space
<a name="create-manage-spaces-update"></a>

**HyperPod CLI**

```
hyp update hyp-space \
    --name myspace \
    --display-name "Updated My Space"
```

**kubectl**

Update the original workspace YAML file as needed, then re-apply it. Be sure that the metadata name is not modified. You can also use these kubectl command to modify fields without reapplying the entire workspace yaml: 

```
# Open a Terminal IDE and modify the Workspace
kubectl edit workspace -n <workspace-namespace>

# Patch a Workspace
kubectl patch workspace <workspace-name> --type='merge' -p \
    '{"spec":{"<field name>":"<desired value>"}}' -n <workspace-namespace>
```

## Start/Stop a space
<a name="create-manage-spaces-stop"></a>

**HyperPod CLI**

```
hyp start hyp-space --name myspace
hyp stop hyp-space --name myspace
```

**kubectl**

You can update the desired status field in the Workspace to start/stop a space.

```
# Start a Workspace
kubectl patch workspace <workspace-name> --type='merge' -p \
    '{"spec":{"desiredStatus":"Running"}}' -n <workspace-namespace>
    
# Stop a Workspace
kubectl patch workspace <workspace-name> --type='merge' -p \
    '{"spec":{"desiredStatus":"Stopped"}}' -n <workspace-namespace>
```

## Get Logs
<a name="create-manage-spaces-log"></a>

**HyperPod CLI**

```
hyp get-logs hyp-space --name myspace
```

**kubectl**

```
# Check Pod Logs
kubectl logs -l workspace.jupyter.org/workspace-name=<workspace-metadata-name>

# Check Pod Events
kubectl describe pod -l workspace.jupyter.org/workspace-name=<workspace-metadata-name>

# Check Operator Logs
kubectl logs -n jupyter-k8s-system deployment/jupyter-k8s-controller-manager
```

## Delete a space
<a name="create-manage-spaces-delete"></a>

**HyperPod CLI**

```
hyp delete hyp-space --name myspace
```

**kubectl**

```
# Delete a Workspace
kubectl delete workspace <workspace-name> -n <namespace>
```