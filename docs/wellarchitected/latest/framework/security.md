

# Security

 The security pillar describes how to use cloud technologies to protect data, systems, and assets, and to improve your security posture. It covers the practices that keep the right people and machines accessing the right resources under the right conditions, that give you visibility into what is happening, that protect workloads and data throughout their lifecycle, and that prepare you to respond when something goes wrong. This guidance applies across the design, delivery, and maintenance of a workload, so that security is built in rather than added at the end. 

 This pillar groups practices into four areas, each containing one or more capabilities that are made up of several individual best practices. 

## Security governance and operations
<a name="security-governance-and-operations"></a>

 Security is an ongoing discipline of setting direction, watching what happens, and acting when something does. This area covers the capabilities that run continuously and across every workload: the governance and control objectives that guide each workload, the detection that turns raw activity into a signal you can act on, and the incident response that contains and recovers from events. These capabilities operate continuously and answer how an organization decides what secure means, how it knows whether that is being achieved, and how it responds when it is not. 
+  [Securely operate your workload](sec01.md) 
+  [Detection](sec04.md) 
+  [Incident response](sec10.md) 

## Identity and access management
<a name="identity-and-access-management"></a>

 To use AWS services, you grant people and applications access to resources in your accounts. As you run more workloads, you need dependable identity management and permissions so that the right identities have access to the right resources under the right conditions. The best practices in this area fall under two capabilities: managing the identities of people and machines, and managing what those identities are permitted to do. 
+  [Identity management](sec02.md) 
+  [Permissions management](sec03.md) 

## Data protection
<a name="data-protection"></a>

 This area categorizes data by sensitivity and applies controls suited to each level. Classification tells you what you hold and how it must be handled, and encryption renders data unintelligible to anyone without authorized access, whether the data is stored or moving between systems. Together these support objectives such as preventing mishandling and meeting regulatory obligations. The capabilities in this area cover classifying data and protecting it in both of the states it exists in, at rest and in transit. 
+  [Data classification](sec07.md) 
+  [Protecting data at rest](sec08.md) 
+  [Protecting data in transit](sec09.md) 

## Infrastructure and application protection
<a name="infrastructure-and-application-protection"></a>

 This area covers the layers that stand between unauthorized access and your running workload: the network it sits in, the compute it runs on, and the application code itself. Applying defense in depth across these layers, through trust boundaries, hardened and patched systems, and secure software practices, keeps a weakness in one layer from putting the whole workload at risk. These capabilities protect the workload from the outside in. Network and compute protection defend the environment the application runs in, and application security addresses the code and the pipeline that delivers it, so the protections hold whether a threat arrives over the network or through the software itself. 
+  [Protecting networks](sec05.md) 
+  [Protecting compute](sec06.md) 
+  [Application security](sec11.md) 

## A layered approach
<a name="a-layered-approach"></a>

 Take a layered approach across all four areas. Apply controls at every layer, from the organization and its accounts down to the network, compute, application, and data, and automate those controls so they scale consistently across workloads. Understand the [Shared responsibility](shared-responsibility.md) first, because it defines which controls AWS operates and which are yours. Where a control affects cost, performance, or operational agility, make the trade-off deliberately rather than by default. 

 This guidance is written for the technology and security roles responsible for building and protecting workloads, including chief technology officers (CTOs), chief information security officers (CISOs), security and application architects, developers, DevOps and infrastructure engineers, security engineers, security operations and incident response teams, and compliance, governance, and risk professionals. After reading it, you will understand the AWS recommendations and strategies to apply when you design cloud architectures with security in mind, so you can build workloads that protect your data and systems, control access, and detect and respond to security events. 