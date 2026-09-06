

# Web browser access
<a name="browser-access"></a>

Web UI access allows you to connect directly to development spaces running on your SageMaker HyperPod cluster through a secure web browser interface. This provides immediate access to Jupyter Lab and other web-based development environments without requiring local software installation.

## Prerequisites
<a name="browser-access-prereq"></a>

Before setting up web UI access, ensure you have completed the following:
+ *SageMaker Spaces add-on installation*: Follow the [SageMaker Spaces add-on installation ](https://docs.aws.amazon.com/sagemaker/latest/dg/operator-install.html) and enable web UI access during installation
+ *User access to EKS cluster*: Users need EKS Access Entry configured with appropriate permissions. See [Add users and set up service accounts for EKS Access Entry setup details](https://docs.aws.amazon.com/sagemaker/latest/dg/add-user.html)
+ *Development spaces*: Create and start development spaces on your HyperPod cluster
+ *kubectl access*: Ensure kubectl is configured to access your EKS cluster

## Generate Web UI Access URL
<a name="browser-access-url"></a>

**Using HyperPod CLI**

If you have the HyperPod CLI installed, you can use this simplified command:

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
<a name="browser-access-develop"></a>

1. *Generate the web UI URL* using one of the methods above

1. *Copy the URL* from the response

1. *Open the URL* in your web browser

1. *Access your development environment* through the web interface

## Supported Development Environments
<a name="browser-access-develop-env"></a>

The web UI provides access to:
+ *Jupyter Lab*
+ *Code Editor*

## Troubleshooting
<a name="browser-access-troubleshooting"></a>

**Cannot generate access URLs**

Check the following:
+ SageMaker Spaces add-on is running: kubectl get pods -n sagemaker-spaces-system
+ Development space is running and healthy
+ User has appropriate EKS Access Entry permissions