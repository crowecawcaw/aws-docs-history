# Remote access methods for SageMaker Spaces

SageMaker AI Spaces supports two remote access mechanisms. Both connect a local IDE or
terminal to a development space on your HyperPod cluster. The mechanisms differ in
network model, client requirements, and administrator setup. Choose the one that best
fits your network, tooling, and security requirements.

**Remote access using SSH over SSM
(recommended)**

This method tunnels SSH through SSM, so no inbound ports are open on your
cluster. Because it requires no inbound network access, it provides a strong
network security posture, and we recommend it as the default. Your local
machine requires the Session Manager plugin and an SSH client. For the full
list of client requirements, see
[Local machine prerequisites](customization.md#remote-ide-requirement-machine "customization.md#remote-ide-requirement-machine"). For setup instructions,
see [Remote access using SSH over SSM](vscode-access.md "vscode-access.md").

**Direct SSH**

Direct SSH exposes an inbound SSH port on your workspace pods and connects with
standard SSH tooling. Choose this method when:

- You want to use standard SSH clients and run multiple tools over a
  single SSH connection, such as a remote IDE plus port forwarding for
  web apps.
- Your client machines cannot install the AWS CLI or Session
  Manager plugin, or cannot use AWS credentials, and you need to
  connect with plain SSH only.

###### Important

Direct SSH bypasses IAM authorization completely. Network
connectivity and SSH key authentication determine all access control.
Any client that can reach the pod IP on the configured
port and authenticate with a valid SSH key can connect.

Direct SSH opens an inbound TCP port, so it requires administrator setup on
the cluster (a security group inbound rule and ExternalDNS with a private
hosted zone) and applies cluster-wide. Before you enable it, review the
caveats in [Direct SSH](direct-ssh-access.md "direct-ssh-access.md").
