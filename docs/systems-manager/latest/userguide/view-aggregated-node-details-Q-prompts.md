

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Learning to craft effective prompts to ask Amazon Q about your fleet
<a name="view-aggregated-node-details-Q-prompts"></a>

The better quality of the question, or the prompt, that you give to Amazon Q, the better the result it provides you with.

**Tips for query prompts**  
Keep in mind the following tips when querying Amazon Q about your fleet:

1. To help improve the accuracy of your results, use the terms "managed nodes" and "managed instances" in your prompts instead of just "nodes" and "instances".

1. To query for results across multiple accounts that are part of an *organization*, as configured in AWS Organizations, you must be logged into the delegated administrator account in the designated home Region.

1. In the delegated administrator account, use terms to help Amazon Q understand that you are asking about nodes and instances across the organization by specifically using terms such as "in my organization" or "in my account 123456789012".

**Topics**
+ [Sample questions for Amazon Q](#sample-questions-Q)
+ [Supported operating system names and versions for prompts](#supported-os-names-Q)

## Sample questions for Amazon Q
<a name="sample-questions-Q"></a>

In the following table, we provide sample questions demonstrate some ways you can create queries of Amazon Q that lead to better results.

We also provide examples of the filters Amazon Q will apply when running the [ListNodes](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListNodes.html) command, which are generated from the content of your prompt.


| Sample natural language question | Amazon Q applied filters | 
| --- | --- | 
| Show me my Windows managed nodes. | <pre>PlatformType = Windows</pre> | 
| List my managed instances in account 123456789012. | <pre>AccountId = 123456789012</pre> | 
| Show me all managed nodes running Amazon Linux 2 across my organization. | <pre>PlatformName = Amazon Linux<br />PlatformVersion = 2</pre> | 
| Show me all managed instances running Microsoft Windows Server 2019 Datacenter in my organization. | <pre> PlatformName = Microsoft Windows Server 2019 Datacenter</pre> | 
| Can you show me all managed nodes with SSM Agent version 3.3.1142.0? | <pre>AgentType = amazon-ssm-agent<br />AgentVersion = 3.3.1142.0                               </pre> | 
| List all Amazon Linux 2 managed instances in account 123456789012 that have SSM Agent version 3.3.1230.0. | <pre>PlatformName = Amazon Linux<br />PlatformVersion = 2<br />AccountId = 123456789012<br />AgentType = amazon-ssm-agent<br />AgentVersion = 3.3.1230.0</pre> | 
| What Microsoft Windows Server 2012 R2 Enterprise managed nodes are running in the eu-central-1 region across my entire organization? | <pre>PlatformName = Microsoft Windows Server 2012 R2 Enterprise<br />Region = eu-central-1</pre> | 
| Show me all managed instances running Red Hat Linux 7 in ou-d6ty-gxdma6vm. | <pre>PlatformName = RHEL Linux<br />PlatformVersion = 7<br />OrganizationalUnitId = ou-d6ty-gxdma6vm</pre> | 
| What Ubuntu managed instances are in account 123456789012?  | <pre>PlatformName = Ubuntu<br />AccountId = 123456789012</pre> | 
| List my Linux managed instances. | <pre>PlatformType = Linux</pre> | 
| Find my macOS managed nodes. | <pre>PlatformType = macOS</pre> | 
| Show me all versions of Amazon Linux managed nodes in my org. | <pre>PlatformName = Amazon Linux</pre> | 
| List managed nodes running Amazon Linux 2. | <pre>PlatformName = Amazon Linux<br />PlatformVersion = 2                               </pre> | 
| List the managed nodes with Ubuntu 22.04 in account 123456789012. | <pre>PlatformName = Ubuntu<br />PlatformVersion = 22.04<br />AccountId = 123456789012</pre> | 
| Find all managed nodes that have an SSM Agent version that is not 3.3.987.0. | <pre>AgentType = amazon-ssm-agent<br />AgentVersion != 3.3.987.0                               </pre> | 
| List all managed instances that are not running a Linux operating system. | <pre>PlatformType != Linux</pre> | 

## Supported operating system names and versions for prompts
<a name="supported-os-names-Q"></a>

When you are asking Amazon Q about the managed nodes in your account, it's helpful to provide the name of an operating system as its labeled in Systems Manager. You can also provide version numbers to further narrow down your results. For example, as represented in the following tables, you could ask for results specifically about **macOS 14.5**, **Microsoft Windows Server 2019 Datacenter**, and **AlmaLinux 9.2 through 9.4**, to name just a few examples.

These lists might not be exhaustive and are offered as examples only.


**macOS**  

| Platform name | Version numbers | 
| --- | --- | 
| macOS | 13.2, 13.4, 13.7, 14.1, 14.5, 14.6.1, 15.0 | 


**Windows**  

| Releases | Version numbers | 
| --- | --- | 
| Microsoft Windows Server 2012 R2 Datacenter | 6.3.9600 | 
| Microsoft Windows Server 2012 R2 Standard | 6.3.9600 | 
| Microsoft Windows Server 2012 Standard | 6.2.9200  | 
| Microsoft Windows Server 2016 Datacenter | N/A | 
| Microsoft Windows Server 2016 Standard | 10.0.14393  | 
| Microsoft Windows Server 2019 Datacenter | N/A | 
| Microsoft Windows Server 2019 Standard | N/A | 
| Microsoft Windows Server 2022 Datacenter | N/A | 
| Microsoft Windows Server 2022 Standard | 10.0.20348  | 


**Linux**  

| Platform names | Version numbers | 
| --- | --- | 
| AlmaLinux  | 8.10, 9.2, 9.3, 9.4 | 
| Amazon Linux 2 | 2.0 and greater | 
| Amazon Linux 2023 | 2023.0.20230315.0 and greater | 
| BottleRocket | 1.14.3, 1.16.1, 1.18.0, 1.19.1, 1.19.2, 1.19.5, 1.20.0, 1.20.1, 1.20.2, 1.20.3, 1.20.5, 1.21.1, 1.23.0, 1.24.0, 1.24.1, 1.25.0, 1.26.1, | 
| CentOS Stream | 9  | 
| Debian GNU/Linux  | 11-12 | 
| Oracle Linux Server  | 7.8, 8.2, 8.3, 8.8, 8.9, 8.10, 9.4 | 
| Red Hat Enterprise Linux | 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 8.10, 9.2, 9.3, 9.4 | 
| Red Hat Enterprise Linux Server | 17.3, 7.6, 7.7, 7.8,7.9 | 
| Rocky Linux | 8.6, 8.7, 8.8, 8.9, 8.10, 9.1, 9.2, 9.3, 9.4 | 
| Ubuntu Server  | 18.04, 20.04, 22.04, 24.04 | 