

# SEC01-BP06 Identify threats and prioritize mitigations using a threat model

 A *threat model* is a structured way to find what can go wrong in a system and decide what to do about it before an unauthorized user does. Complex systems can obscure issues, and manual reviews might sometimes miss these threats. Model threats early in design, when fixes are cheap. 

 **Desired outcome:** 
+  You maintain a current register of potential threats to your workload and their mitigations. 
+  You prioritize threats and map mitigations across prevention, detection, and response. 
+  Your threat model is a living document that you revisit as the workload and the threats to it change. 
+  You model threats early in design, when mitigations cost the least. 

 **Common anti-patterns:** 
+  Teams rely on unstructured, one-off reviews to find threats in complex systems. 
+  Threat modeling starts late in the lifecycle, when mitigations are expensive to apply. 
+  A threat model is produced once and never revisited after the workload changes. 
+  Threats are identified but never prioritized, so limited resources are spent without focus. 
+  Mitigations ignore the shared responsibility split between the team and the provider. 

 **Benefits of establishing this best practice:** 
+  Threats are found early, when the cost and effort to mitigate them are lowest. 
+  Limited security resources go to the mitigations with the highest impact. 
+  A shared model gives the whole team a common understanding of what to protect and why. 
+  The register stays relevant as the system and its threats evolve. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The Open Web Application Security Project (OWASP) defines [threat modeling](https://community.owasp.org/Threat_Modeling) as work to identify, communicate, and understand threats and mitigations within the context of protecting something of value. As systems grow more complex, each new use case adds permutations that unstructured review cannot cover. A structured method enumerates threats and prioritizes mitigations by impact. 

 Threat modeling finds and addresses issues early in design, when mitigations cost less than later in the lifecycle (also referred to as the shift-left security principle). Treat the threat model as a living document. Revisit it when the workload changes, when the threats change, or when you adopt a new feature or service. Done consistently, threat modeling integrates with your risk management process and drives which controls you implement. 

 Pick a methodology that fits your team. Write down assumptions and set a scope boundary. This avoids detours into concerns you cannot affect, such as the boot sequence of a browser client for a web application. Under the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), you own AWS service configuration and your custom code. Pay attention to the code and its dependencies particular, since most vulnerabilities originate there. 

### Implementation steps
<a name="implementation-steps"></a>

 These implementation steps follow [Shostack's 4 Question Frame for Threat Modeling](https://github.com/adamshostack/4QuestionFrame) and add a tool for authoring the model. 

1.  **Define what you are working on:** Agree on the system you are building and the details relevant to security. Create a model such as a [data flow diagram](https://en.wikipedia.org/wiki/Data-flow_diagram) to visualize it, and write down assumptions and scope so the team focuses on the same thing and avoids out-of-scope detours. 

1.  **Identify what can go wrong:** Brainstorm threats with the team and the relevant personas involved. Use a model such as [STRIDE](https://en.wikipedia.org/wiki/STRIDE_%28security%29) to prompt categories (spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege), and draw on existing lists such as the [OWASP Top 10](https://owasp.org/projects/top-ten) and [MITRE ATT&CK](https://attack.mitre.org/) for inspiration. For threats specific to AWS, the [Threat Technique Catalog for AWS](https://aws-samples.github.io/threat-technique-catalog-for-aws/) records techniques that the AWS Customer Incident Response Team sees during security events. Each entry includes detection and mitigation guidance. 

1.  **Decide what to do about each threat:** For each identified threat, determine the mitigation and who owns it under the shared responsibility model. Consider controls across identity and access, data protection, infrastructure, logging, and monitoring, using each service's [security documentation](https://docs.aws.amazon.com/security/) for guidance, and add controls for your custom code such as [input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) and safe [session handling](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). 

1.  **Assess whether you did a good job:** Review the quality and coverage of the model with your team, and improve both the model and your velocity over time through practice, teaching, and review. Deepen skills with the [threat modeling workshop](https://catalog.workshops.aws/threatmodel/en-US) for hands-on practice. 

1.  **Author and maintain the model with tooling:** Use the [Threat Composer](https://github.com/awslabs/threat-composer) tool to write threat statements aligned to [threat grammar](https://catalog.workshops.aws/threatmodel/en-US/what-can-go-wrong/threat-grammar), generate human-readable and machine-readable models, and identify coverage gaps through its insights dashboard. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP02 Identify and validate control objectives](sec01-bp02.md) 
+  [SEC01-BP03 Stay up to date with security threats and recommendations](sec01-bp03.md) 
+  [SEC01-BP07 Evaluate and implement new security services and features regularly](sec01-bp07.md) 

 **Related documents:** 
+  [How to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/) 
+  [NIST SP 800-154: Guide to Data-Centric System Threat Modeling (initial public draft)](https://csrc.nist.gov/pubs/sp/800/154/ipd) 

 **Related videos:** 
+  [AWS Summit ANZ 2021 - How to approach threat modelling](https://www.youtube.com/watch?v=GuhIefIGeuA) 

 **Related tools:** 
+  [Threat Composer](https://github.com/awslabs/threat-composer) 
+  [ThreatForest](https://github.com/aws-samples/sample-agentic-attack-tree-generator/tree/main) 

 **Related workshops:** 
+  [Threat Modeling for Builders Workshop](https://skillbuilder.aws/learn/H3BU3X1M82/threat-modeling-for-builders-workshop/HZJDJ7M6PX) 
+  [Threat modeling for builders](https://catalog.workshops.aws/threatmodel/en-US) 