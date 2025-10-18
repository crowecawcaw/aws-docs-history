# Install agents on EC2 instances with SSM

Network Flow Monitor agents provide performance metrics about network flows. Follow the steps in this section to 
 install and work with Network Flow Monitor agents on EC2 instances, by using AWS Systems Manager. If you use Kubernetes, skip to
 the next sections for information about installing agents with Amazon EKS clusters or self-managed Kubernetes clusters.

Network Flow Monitor provides a Distributor package for you in Systems Manager to use to install or uninstall agents. In
 addition, Network Flow Monitor provides a document to activate or deactivate agents, by using the Document Type command. Use 
 standard Systems Manager procedures to use the package and the document, or follow the steps provided here for
 detailed guidance.

For more information in general about using Systems Manager, see the following documentation:


* [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html")
* [AWS Systems Manager Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html")
Complete the steps in the following sections to configure permissions, install, and work with Network Flow Monitor agents.

**Contents**


* [Install or uninstall agents](#CloudWatch-NetworkFlowMonitor-agents-ec2-install "#CloudWatch-NetworkFlowMonitor-agents-ec2-install")
* [Activate or deactivate agents](#CloudWatch-NetworkFlowMonitor-agents-ec2-manage "#CloudWatch-NetworkFlowMonitor-agents-ec2-manage")

## Install or uninstall agents by using Systems Manager


Network Flow Monitor provides a distributor package in AWS Systems Manager for you to install Network Flow Monitor agents:
 **AmazonCloudWatchNetworkFlowMonitorAgent**. To access and run the package to install
 agents, follow the steps provided here. 


###### To install agents in EC2 instances

1. In the AWS Management Console, in AWS Systems Manager, under **Node Tools**, choose **Distributor**.
2. Under **Owned by Amazon**, locate the Network Flow Monitor package,
 **AmazonCloudWatchNetworkFlowMonitorAgent**, and select it.
3. In the **Run command** flow, choose **Install one time** or **Install on schedule**.
4. In the **Target selection** section, choose how you want to select your EC2 instances to install agents on. You can select instances based on tags,
 choose instances manually, or base the choice on resource groups.
5. In the **Commmand parameters** section, under **Action**, choose **Install**.
6. Scroll down, if necessary, and then choose **Run** to start the installation.

If the installation is successful and the instances have permissions to access Network Flow Monitor endpoints, the agent will start collecting 
 metrics and send reports to the Network Flow Monitor backend. 


Agents that are active (sending metrics data) incur billing costs. For more information about Network Flow Monitor and Amazon CloudWatch pricing, see Network Monitoring on the 
 [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") page. If you don't need
 metrics data temporarily, you can deactivate an agent. For more information, see 
 [Activate or deactivate agents](#CloudWatch-NetworkFlowMonitor-agents-ec2-manage "#CloudWatch-NetworkFlowMonitor-agents-ec2-manage").
 If you no longer need Network Flow Monitor agents, you can uninstall them from the EC2 instances.


###### To uninstall agents from EC2 instances

1. In the AWS Management Console, in AWS Systems Manager, under **Node Tools**, choose **Distributor**.
2. Under **Owned by Amazon**, locate the Network Flow Monitor package,
 **AmazonCloudWatchNetworkFlowMonitorAgent**, and select it.
3. In the **Commmand parameters** section, under **Action**, choose **Uninstall**.
4. Select the EC2 instances to uninstall agents from.
5. Scroll down, if necessary, and then choose **Run** to start the installation.

## Activate or deactivate agents by using Systems Manager


After you install a Network Flow Monitor agent with SSM, you must activate it to receive network flow metrics from the instance
 where it's installed. Agents that are active (sending metrics data) incur billing costs. For more information about 
 Network Flow Monitor and Amazon CloudWatch pricing, see Network Monitoring on the [Amazon CloudWatch 
 pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") page. If you don't need metrics data temporarily, you can deactivate an agent to prevent
 ongoing billing for the agent.


Network Flow Monitor provides a document in AWS Systems Manager that you can use activate or deactivate agents that you've installed on your EC2 instances.
 By running this document to manage the agents, you can activate them to begin receiving performance metrics.
 Or, you can deactivate them to temporarily stop metrics from being sent,without uninstalling the agents.


The document in SSM that you can use to activate or deactivate agents is called
 **AmazonCloudWatch-NetworkFlowMonitorManageAgent**. To access and run the document, follow
 the steps in the procedure. 


###### To activate or deactivate Network Flow Monitor agents

1. In the AWS Management Console, in AWS Systems Manager, under **Change Management Tools**, choose **Documents**.
2. Under **Owned by Amazon**, locate the Network Flow Monitor document, 
 **AmazonCloudWatch-NetworkFlowMonitorManageAgent**, and select the document.
3. In the **Target selection** section, choose how you want to select your EC2 instances to install agents on. You can select instances based on tags,
 choose instances manually, or base the choice on resource groups.
4. In the **Command parameters** section, under **Action**, choose **Activate** or **Deactivate**, 
 depending on the action that you want to take for the agents.
5. Scroll down, if necessary, and then choose **Run** to start the installation.
