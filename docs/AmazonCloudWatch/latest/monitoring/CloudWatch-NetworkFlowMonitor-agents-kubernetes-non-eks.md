# Install agents for self-managed Kubernetes instances

Follow the steps in this section to install Network Flow Monitor agents for workloads on self-managed Kubernetes clusters. After you 
 complete the steps, Network Flow Monitor agent pods will be running on all of your self-managed Kubernetes cluster nodes.

If you use Amazon Elastic Kubernetes Service (Amazon EKS), the installation steps to follow are in the following section: 
 [Install the EKS AWS Network Flow Monitor Agent add-on](CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks.md "CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks.md").
 

###### Contents

* [Before you begin](#CloudWatch-NetworkFlowMonitor-agents-kubernetes-before-you-begin "#CloudWatch-NetworkFlowMonitor-agents-kubernetes-before-you-begin")
* [Download Helm charts and install agents](#CloudWatch-NetworkFlowMonitor-agents-kubernetes-install-agents "#CloudWatch-NetworkFlowMonitor-agents-kubernetes-install-agents")
* [Configure permissions for agents to deliver metrics](#CloudWatch-NetworkFlowMonitor-agents-kubernetes-permissions "#CloudWatch-NetworkFlowMonitor-agents-kubernetes-permissions")

## Before you begin


Before you start the installation process, follow the steps in this section to make sure that your environment 
 is set up to successfully install agents on the right Kubernetes clusters.




**Ensure that your version of Kubernetes is supported**
Network Flow Monitor agent installation requires Kubernetes Version 1.25, or a more recent version.


**Ensure that you have installed required tools**
The scripts that you use for this installation process require that you install the following 
 tools. If you don’t have the tools installed already, see the provided links for more information.



* The AWS Command Line Interface (CLI). For more information, see [Installing or updating to the latest version of the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html")
 in the AWS Command Line Interface Reference Guide.
* The Helm package manager. For more information, see [Installing Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/") on the Helm website.
* The `kubectl` command line tool. For more information, see [Install kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl "https://kubernetes.io/docs/tasks/tools/#kubectl") on the Kubernetes website.
* The `make` Linux command dependency. For more information, see the following blog post: [Intro to make Linux Command: Installation and Usage](https://ioflood.com/blog/install-make-command-linux/ "https://ioflood.com/blog/install-make-command-linux/"). For example, do one of the following:




	+ For Debian based distributions, such as Ubuntu, use the following command: `sudo apt-get install make`
	+ For RPM-based distributions, such as CentOS, use the following command: `sudo yum install make`

**Ensure that you have valid, correctly configured KubeConfig environment variables**
Network Flow Monitor agent installation uses the Helm package manager tool, which uses the kubeconfig variable, 
 `$HELM_KUBECONTEXT`, to determine the target Kubernetes clusters to work with. Also, be
 aware that when Helm runs installation scripts, by default, it references the standard `~/.kube/config` file. 
 You can change the configuration environment variables, to use a different config file (by updating
 `$KUBECONFIG`) or to define the target cluster you want to work with (by updating `$HELM_KUBECONTEXT`).
 


**Create a Network Flow Monitor Kubernetes namespace**
The Network Flow Monitor agent's Kubernetes application installs its resources into a specific namespace. The namespace
 must exist for the installation to succeed. To ensure that the required namespace is in place, you can 
 do one of the following: 



* Create the default namespace, `amazon-network-flow-monitor`, before you begin.
* Create a different namespace, and then define it in the `$NAMESPACE` 
 environment variable when you run the installation to make targets.



## Download Helm charts and install agents


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


## Configure permissions for agents to deliver metrics


After you install agents for Network Flow Monitor, you must enable the agents to send network 
 metrics to the Network Flow Monitor ingestion APIs. Agents in Network Flow Monitor must have permission to access the Network Flow Monitor ingestion APIs 
 so that they can deliver network flow metrics that they've collected for each instance. You grant this access 
 by implementing IAM roles for service accounts (IRSA).
 


To enable agents to deliver network metrics to Network Flow Monitor, follow the steps in this section.



1. **Implement IAM roles for service accounts**


IAM roles for service accounts provides the ability to manage credentials for your applications, 
 similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances. Implementing IRSA is 
 the recommended way to provide all permissions required by Network Flow Monitor agents to successfully access
 Network Flow Monitor ingestion APIs. For more information, see [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html "https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html") 
 in the Amazon EKS User Guide.


When you set up IRSA for Network Flow Monitor agents, use the following information:




	* **ServiceAccount:** When you define your IAM role trust policy, 
	 for `ServiceAccount`, specify `aws-network-flow-monitor-agent-service-account`.
	* **Namespace:** For the `namespace`, specify `amazon-network-flow-monitor`.
	* **Temporary credentials deployment:** When you configure 
	 permissions after you have deployed Network Flow Monitor agent pods, updating the `ServiceAccount` with
	 your IAM role, Kubernetes does not deploy the IAM role credentials. To ensure that the Network Flow Monitor
	 agents acquire the IAM role credentials that you've specified, you must rolling out a restart of `DaemonSet`.
	 For example, use a command like the following:
	
	
	`kubectl rollout restart daemonset -n amazon-network-flow-monitor aws-network-flow-monitor-agent`
2. **Confirm that the Network Flow Monitor agent is successfully accessing the Network Flow Monitor ingestion APIs**


You can check to make sure that your configuration for agents is working correctly by 
 using the HTTP 200 logs for Network Flow Monitor agent pods. First, search for
 a Network Flow Monitor agent pod, and then search through the log files to find successful HTTP 200 requests.
 For example, you can do the following:




	1. Locate a Network Flow Monitor agent Pod name. For example, you can use the following command:
	
	
	
	```
	RANDOM_AGENT_POD_NAME=$(kubectl get pods -o wide -A | grep amazon-network-flow-monitor | grep Running | head -n 1 | tr -s ' ' | cut -d " " -f 2)
				
	```
	2. Grep all the HTTP logs for the pod name that you've located. If you've changed the NAMESPACE, make sure 
	 that you use the new one.
	
	
	
	```
	NAMESPACE=amazon-network-flow-monitor
	kubectl logs $`RANDOM_AGENT_POD_NAME` -\-namespace ${NAMESPACE} | grep HTTP
	
	```
If access has been granted successfully, you should see log entries similar to the following:



```
...
{"level":"INFO","message":"HTTP request complete","status":200,"target":"amzn_nefmon::reports::publisher_endpoint","timestamp":1737027525679}
{"level":"INFO","message":"HTTP request complete","status":200,"target":"amzn_nefmon::reports::publisher_endpoint","timestamp":1737027552827}

```

Note that the Network Flow Monitor agent publishes network flow reports every 30 seconds, by calling the Network Flow Monitor ingestion APIs.
