

# Remote access using SSH over SSM
<a name="vscode-access"></a>

Remote access allows you to connect your local Visual Studio Code directly to development spaces running on your SageMaker HyperPod cluster. Remote connections use SSM to establish secure, encrypted tunnels between your local machine and the development spaces.

## Prerequisites
<a name="vscode-access-prereq"></a>

Before setting up remote access, ensure you have completed the following:
+ *SageMaker Spaces add-on installation*: Follow [SageMaker Spaces add-on installation](https://docs.aws.amazon.com/sagemaker/latest/dg/operator-install.html) and enable remote access during installation (either Quick install or Custom install with remote access configuration enabled).
+ *User access to EKS cluster*: Users need EKS Access Entry configured with appropriate permissions. See [Add users and set up service accounts for EKS Access Entry setup details](https://docs.aws.amazon.com/sagemaker/latest/dg/add-user.html)
+ *Development spaces*: Create and start development spaces on your HyperPod cluster
+ *kubectl access*: Ensure kubectl is configured to access your EKS cluster

## Generate VS Code remote connection
<a name="vscode-access-remote"></a>

### Using HyperPod CLI
<a name="vscode-access-remote-cli"></a>

If you have the HyperPod CLI installed, you can use this simplified command:

```
hyp create hyp-space-access --name <space-name> --connection-type vscode-remote
```

### Using kubectl
<a name="vscode-access-remote-kubectl"></a>

You can also use the `kubectl` command line to create a connection request.

```
kubectl create -f - -o yaml <<EOF
apiVersion: connection.workspace.jupyter.org/v1alpha1
kind: WorkspaceConnection
metadata:
  namespace: <space-namespace>
spec:
  workspaceName: <space-name>
  workspaceConnectionType: vscode-remote
EOF
```

The URL is present in the `status.workspaceConnectionUrl` of the output of this command.

## Connecting with VS Code
<a name="vscode-access-remote-vscode"></a>

1. Generate the VS Code connection URL using one of the methods above

1. Copy the VS Code URL from the response

1. Click the URL or paste it into your browser

1. VS Code will prompt to open the remote connection

1. Confirm the connection to establish the remote development environment

## Supported Development Environments
<a name="vscode-access-remote-dev-env"></a>

The web UI provides access to:
+ *Jupyter Lab*
+ *Code Editor*

## Troubleshooting
<a name="troubleshooting"></a>

**Cannot generate connection URLs**

*Check the following:*
+ SageMaker Spaces add-on is running: kubectl get pods -n sagemaker-spaces-system
+ Development space is running and healthy
+ Remote access was enabled during add-on installation
+ User has appropriate EKS Access Entry permissions