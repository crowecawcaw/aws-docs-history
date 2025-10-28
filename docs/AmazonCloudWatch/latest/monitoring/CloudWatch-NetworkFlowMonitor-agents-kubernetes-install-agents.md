# Download Helm charts and install agents

You can download the Network Flow Monitor agent Helm charts from the AWS public repository by using the
following command. Make sure that you first authenticate with your GitHub account.

`git clone https://github.com/aws/network-flow-monitor-agent.git`

In the `./charts/amazon-network-flow-monitor-agent` directory, you can find the
Network Flow Monitor agent Helm charts and Makefile that contain the installation make targets that you use
for installing agents. You install agents for Network Flow Monitor by using the following Makefile target:
`helm/install/customer`

You can customize the installation if you like, for example, by doing the following:

```
# Overwrite the kubeconfig files to use
KUBECONFIG=<MY_KUBECONFIG_ABS_PATH> make helm/install/customer

# Overwrite the Kubernetes namespace to use
NAMESPACE=<MY_K8S_NAMESPACE> make helm/install/customer
```

To verify that the Kubernetes application pods for the Network Flow Monitor agents have been created and deployed successfully,
check to be sure that their state is `Running`. You can check state of the agents by running the following
command: `kubectl get pods -o wide -A | grep amazon-network-flow-monitor`
