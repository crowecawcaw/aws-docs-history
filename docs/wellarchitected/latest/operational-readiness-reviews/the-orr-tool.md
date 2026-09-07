

# The ORR tool
<a name="the-orr-tool"></a>

The main tool for ORR is the checklist of questions itself. AWS has built a web service around this checklist to create templates, provide a consistent user interface (UI), links to cautionary tales, and set up integrations with the AWS ticketing system. This allows teams to perform a self-service review of their workload, record the results, understand their residual risk, and track action items that result from the review, which can be directly added to their backlog. 

Let’s take a look at an example of a question AWS might ask in one of those checklists. Some systems choose to implement [certificate pinning](https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-pinning). While there are some potential security benefits, this practice poses a significant availability risk if the pinned certificate is replaced, which can occur for any number of reasons. A question and guidance in your ORR checklist for certificate pinning might look like the following. 


| **Question:** Do any of your hosts pin certificates?  | 
| --- | 
| **Guidance**<br />We recommend against using certificate pinning because it introduces a potential availability risk. If the certificate to which you pin is replaced, your application will fail to connect. If your use case requires pinning, we recommend that you pin to a certificate authority (CA) rather than to an individual certificate. <br />☐ Yes \| High Risk <br />☐ No \| No Risk  | 

If you haven’t had an incident related to certificate pinning, or it’s not a high-priority item to address across your enterprise, then don’t include this question. The ORR checklist is most effective when it’s focused on incidents that present critical risks. These are the types of risks that would prevent a General Availability (GA) launch of a service. Medium or low risks aren’t included in the ORR to keep it a lightweight process that doesn’t overburden teams and reduce their agility and ability to innovate. 

## Customer recommendations
<a name="customer-recommendations"></a>

To get started with an ORR program, you don’t need the same level of tooling that AWS has built. The most important component is generating the questions themselves. It is recommended to review three different categories: 
+ Real incidents that you’ve had in the past 
+ Near-misses that you’ve had in the past 
+ The failure modes that haven’t occurred, but that you’re concerned about 

Out of this set of categories, you can begin to develop questions and associated best practices that can either prevent, or reduce in scope of impact or duration of, those incidents in the future. You can take lessons you’ve learned in both AWS as well as on-premises environments, they aren’t exclusive to operating in the cloud. See [Appendix A: Creating ORR guidance from an incident](appendix-a-creating-orr-guidance-from-an-incident.md) for a complete example of how you can generate ORR guidance from an incident. See [Appendix B: Example ORR questions](appendix-b-example-orr-questions.md) for example questions that you can use to start building your own ORR checklist, keeping in mind that these are only examples and you should tailor the checklist for your specific use cases, environment, and workloads. 

To get started building your own checklist, it is suggested to group your questions and develop content in the following areas. 
+ **Architecture** — The focus is on how you’ve built your architecture, the dependencies your workload has taken, how you scale and manage capacity, and how you protect your workload from its customers (for example, preventing overload). 
+ **Release quality** — This section focuses on how you test and deploy changes to your workload including detecting problems, automated and manual rollback procedures, and how you phase changes incrementally to your systems. 
+ **Event management** — These questions focus on the processes and procedures required to deal with an event when it does occur, including topics like paging an on-call operator, the location and coverage of runbooks, the instrumentation and alarms associated with your workload, and metrics and dashboards you use to understand your workload’s state. 

Your questions may address people, process, and technology in each area. You may also choose to organize the checklist content in more granular categories, such as the following: 
+ Deployment safety 
+ Defense against customers 
+ Defense against dependencies 
+ Data recovery 
+ Operator safety 
+ Blast radius containment 
+ Event detection 
+ Service restart 
+ Forensics 
+ Escalation 

Using [custom lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-custom.html), you can build your checklists into the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/). You might decide to track action items from your ORR in a tool such as [AWS System Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html). You also might choose to use the results of [post-incident analysis](https://docs.aws.amazon.com/incident-manager/latest/userguide/analysis.html) in [AWS System Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html) as inputs to developing your questions. AWS offers several different engagement models to help you build your own ORR checklist to complement what you’re doing with Well-Architected. Contact your account team for additional details. 