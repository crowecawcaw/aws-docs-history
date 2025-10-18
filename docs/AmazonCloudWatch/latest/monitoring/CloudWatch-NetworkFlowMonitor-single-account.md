# Initialize Network Flow Monitor for single account monitoring

To initialize Network Flow Monitor to monitor network performance metrics,
 you must grant permissions and Network Flow Monitor must create the initial topology for your account.
 When you monitor resources in just one account, Network Flow Monitor sets your account as the scope for 
 network monitoring and creates a topology for that scope. 

Initializing Network Flow Monitor does the following: 


* Grants permissions for Network Flow Monitor to use required service-linked roles with your account.
 Network Flow Monitor requires you to grant it specific permissions so that
 the feature can send metrics to Amazon CloudWatch on your behalf, as well as create topologies of network
 flows. For more information, see [Service-linked roles for Network Flow Monitor](using-service-linked-roles-network-flow-monitor.md "using-service-linked-roles-network-flow-monitor.md").
* Sets your monitoring scope for Network Flow Monitor to the AWS account that you're
 signed in with. For more information, see **Scope** in 
 [Components and features of Network Flow Monitor](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md").
* Creates an initial topology for your scope.
To initialize Network Flow Monitor by setting up the service-linked roles that provide the required permissions, 
 setting the scope to your account, and creating a topology for network flow performance monitoring,
 follow these steps.

**To initialize Network Flow Monitor**


1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, 
 choose **Flow monitors**.
3. In the **Getting started with Network Flow Monitor** section, under Step 1,
 choose **Start initialization**.
4. On the **Configure Network Flow Monitor** page, scroll down, and then 
 choose **Initialize Network Flow Monitor**.
Completing the initialization can take 20-30 minutes.

After you initialize Network Flow Monitor for your account, before you can view network flow performance metrics,
 you must also install Network Flow Monitor agents
 for your resources that send performance metrics to the Network Flow Monitor backed ingestion server. For more information, 
 see [Install Network Flow Monitor agents on instances](CloudWatch-NetworkFlowMonitor-agents.md "CloudWatch-NetworkFlowMonitor-agents.md").
