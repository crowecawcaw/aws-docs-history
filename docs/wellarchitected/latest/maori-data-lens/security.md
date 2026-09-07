

# Security
<a name="security"></a>

 The Security Pillar helps you meet your business and regulatory requirements by following current AWS recommendations. It's intended for those in technology roles, such as chief technology officers (CTOs), chief information security officers (CSOs/CISOs), architects, chief information/privacy officers (CIOs/CPOs), developers, and operations team members. After reading this document, you can understand current AWS recommendations and strategies to use when designing cloud architectures with security in mind. You can find prescriptive guidance on implementation in the [Security Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html?ref=wellarchitected-wp). 

 The Security Pillar describes how to take advantage of cloud technologies to protect data, systems, and assets in a way that can improve your security posture. The Security Pillar whitepaper provides in-depth, best-practice guidance for architecting secure workloads on AWS. 

**Design principles**
+  **Implement a strong identity foundation.** Implement the principle of least privilege and enforce separation of duties with appropriate authorisation for each interaction with your AWS resources. Centralise identity management, and aim to eliminate reliance on long-term static credentials. 
+  **Maintain traceability.** Monitor, alert, and audit actions and changes to your environment in real time. Integrate log and metric collection with systems to automatically investigate and take action. 
+  **Apply security at all layers.** Apply a defence in depth approach with multiple security controls. Apply to all layers (for example, edge of network, virtual private cloud (VPC), load balancing, every instance and compute service, operating system, application, and code). 
+  **Automate security best practices.** Automated software-based security mechanisms improve your ability to securely scale more rapidly and cost-effectively. Create secure architectures, including the implementation of controls that are defined and managed as code in version-controlled templates. 
+  **Protect data in transit and at rest**. Classify your data into sensitivity levels and use mechanisms, such as encryption, tokenisation, and access control where appropriate. 
+  **Prepare for security events.** Prepare for an incident by having incident management and investigation policy and processes that align to your organisational requirements. Run incident response simulations and use tools with automation to increase your speed for detection, investigation, and recovery. 

 The preceding design principles aim to support an organisation to improve its security posture. The following specific questions are some additional security considerations from a Māori data perspective. 

**Topics**
+ [MD\_SEC 1: How is Māori data protected? ](md_sec-1-how-is-māori-data-protected.md)
+ [MD\_SEC 2: How do you design workload security for long-term safety?](md_sec-2-how-do-you-design-workload-security-for-long-term-safety.md)
+ [MD\_SEC 3: How can you identify and classify Māori data? ](md_sec-3-how-can-you-identify-and-classify-māori-data.md)
+ [MD\_SEC 4: How do you maintain privacy of personal Māori data?](md_sec-4-how-do-you-maintain-privacy-of-personal-māori-data.md)
+ [Resources](md_sec-resources.md)