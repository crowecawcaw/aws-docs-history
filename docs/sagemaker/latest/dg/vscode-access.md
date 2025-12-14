# Remote access to SageMaker Spaces

Remote access allows you to connect your local Visual Studio Code directly to
development spaces running on your SageMaker HyperPod cluster. Remote connections use
SSM to establish secure, encrypted tunnels between your local
machine and the development spaces.

## Prerequisites

Before setting up remote access, ensure you have completed the following:

- _SageMaker Spaces add-on installation_:
  Follow [SageMaker Spaces add-on installation](operator-install.md "operator-install.md") and
  enable remote access during installation (either Quick install or Custom
  install with remote access configuration enabled).
- _User access to EKS cluster_: Users need
  EKS Access Entry configured with appropriate permissions. See [Add users and set up service accounts for EKS Access Entry setup details](add-user.md "add-user.md")
- _Development spaces_: Create and start
  development spaces on your HyperPod cluster
- _kubectl access_: Ensure kubectl is
  configured to access your EKS cluster

## Generate VS Code remote connection

### Using HyperPod CLI

If you have the HyperPod CLI installed, you can use this simplified command:

```
hyp create hyp-space-access --name <space-name> --connection-type vscode-remote
```

### Using kubectl

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

1. Generate the VS Code connection URL using one of the methods above
2. Copy the VS Code URL from the response
3. Click the URL or paste it into your browser
4. VS Code will prompt to open the remote connection
5. Confirm the connection to establish the remote development
   environment

## Supported Development Environments

The web UI provides access to:

- _Jupyter Lab_
- _Code Editor_

## Troubleshooting

**Cannot generate connection URLs**

_Check the following:_

- SageMaker Spaces add-on is running: kubectl get pods -n
  sagemaker-spaces-system
- Development space is running and healthy
- Remote access was enabled during add-on installation
- User has appropriate EKS Access Entry permissions
