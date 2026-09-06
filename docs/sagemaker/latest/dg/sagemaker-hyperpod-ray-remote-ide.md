

# Accessing your development environment
<a name="sagemaker-hyperpod-ray-remote-ide"></a>

A space runs JupyterLab or Code Editor on your cluster. You reach it in a browser, or from a local IDE over a remote connection. Either way your code runs in the space and on the Ray cluster attached to it, so `ray.init()` reaches the cluster.

## Supported development environments
<a name="sagemaker-hyperpod-ray-remote-ide-environments"></a>
+ JupyterLab
+ Code Editor

## Web browser access
<a name="sagemaker-hyperpod-ray-remote-ide-browser"></a>

The SageMaker Spaces add-on issues a URL that opens the space in your browser, with nothing to install locally. Turn on web UI access when you install the add-on. For the URL commands and troubleshooting, see [Web browser access](browser-access.md).

## Remote IDE access
<a name="sagemaker-hyperpod-ray-remote-ide-connect"></a>

Connect a local IDE such as VS Code, Cursor, or Kiro to the space, so your editor runs on your laptop while code runs in the space. There are two mechanisms:
+ **SSH over SSM**, the recommended default. Tunnels SSH through SSM and opens no inbound ports on your cluster. Your laptop needs the Session Manager plugin and an SSH client.
+ **Direct SSH**. Exposes an inbound SSH port on the workspace pods. Choose it when your clients cannot install the AWS CLI or Session Manager plugin. It bypasses IAM authorization, needs administrator setup, and applies cluster-wide.

For setup, see [Remote access methods for SageMaker Spaces](access-mechanism.md).

Once connected, open a terminal or notebook in the space and run `ray.init()` to reach the attached cluster.