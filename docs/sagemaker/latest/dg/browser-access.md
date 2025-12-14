# Web browser access

Web UI access allows you to connect directly to development spaces running on your
SageMaker HyperPod cluster through a secure web browser interface. This provides
immediate access to Jupyter Lab and other web-based development environments without
requiring local software installation.

## Prerequisites

Before setting up web UI access, ensure you have completed the following:

- _SageMaker Spaces add-on installation_:
  Follow the [SageMaker Spaces add-on installation](operator-install.md "operator-install.md") and
  enable web UI access during installation
- _User access to EKS cluster_: Users need
  EKS Access Entry configured with appropriate permissions. See [Add users and
  set up service accounts for EKS Access Entry setup details](add-user.md "add-user.md")
- _Development spaces_: Create and start
  development spaces on your HyperPod cluster
- _kubectl access_: Ensure kubectl is
  configured to access your EKS cluster

## Generate Web UI Access URL

**Using HyperPod CLI**

If you have the HyperPod CLI installed, you can use this simplified
command:

```
hyp create hyp-space-access --name <space-name> --connection-type web-ui
```

**Using kubectl**

You can also use the `kubectl` command line to create a connection request.

```
kubectl create -f - -o yaml <<EOF
apiVersion: connection.workspace.jupyter.org/v1alpha1
kind: WorkspaceConnection
metadata:
  namespace: <space-namespace>
spec:
  workspaceName: <space-name>
  workspaceConnectionType: web-ui
EOF
```

The URL is present in the `status.workspaceConnectionUrl` of the output of this command.

## Accessing Your Development Space

1. _Generate the web UI URL_ using one of
   the methods above
2. _Copy the URL_ from the response
3. _Open the URL_ in your web browser
4. _Access your development environment_
   through the web interface

## Supported Development Environments

The web UI provides access to:

- _Jupyter Lab_
- _Code Editor_

## Troubleshooting

**Cannot generate access URLs**

Check the following:

- SageMaker Spaces add-on is running: kubectl get pods -n
  sagemaker-spaces-system
- Development space is running and healthy
- User has appropriate EKS Access Entry permissions
