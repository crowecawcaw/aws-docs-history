

# Automate your deployment

You can create Amazon Elastic VMware Service resources step by step in the Amazon EVS console or AWS CLI, or you can use a tool that runs the steps for you. Use the following table to choose the method that fits your deployment.


| Method | VCF version | Use it when | 
| --- | --- | --- | 
| EVS Deployment Orchestrator (EDO), a tool in the [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub | 9.x | You want one AWS CloudFormation stack to build the network, add the hosts, and install VMware Cloud Foundation (VCF) from end to end. On diskless hosts, EDO uses Amazon FSx for NetApp ONTAP as the principal storage. For the supported VCF versions, instance types, and storage, see [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md). | 
|  AWS CloudFormation templates | All | You want to describe Amazon EVS resources, such as an environment, in a template and create them the same way in several accounts and Regions. For more information, see [Create Amazon EVS resources with AWS CloudFormation](creating-resources-with-cloudformation.md). | 
| Amazon EVS console and AWS CLI  | All | You want to control and check each step, or you deploy a configuration that the other methods don’t cover. For instructions, see [Deploy in Self-deployed mode](getting-started-self-deployed.md) or [Deploy in EVS-deployed mode](evs-deployed-overview.md). | 

Whichever method you use, you first prepare your AWS account. For instructions, see [Prepare your AWS account](setting-up.md).

**Topics**
+ [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md)
+ [Create Amazon EVS resources with AWS CloudFormation](creating-resources-with-cloudformation.md)