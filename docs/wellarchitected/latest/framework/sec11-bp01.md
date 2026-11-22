

# SEC11-BP01 Embed security ownership in workload teams, and train for application security

 Security decisions happen throughout development. When the teams that build software own its security, they catch risks during design. Give builders the authority and training to make well-informed, sound security decisions. 

 **Desired outcome:** 
+  Your workload teams own the security decisions for the software they build, and they escalate to a central security function only for high-risk or novel cases. 
+  Your builders complete training in threat modeling and secure coding, and they apply it during design rather than after a review. 
+  You run a security champions or guardians program that gives each team a local point of contact for security questions. 
+  Your security review process is documented, and every participant knows their responsibilities and when a review is required. 
+  Your teams have self-service access to approved secure configurations, so meeting security requirements does not depend on a central queue. 

 **Common anti-patterns:** 
+  Teams defer all security design decisions to a central security team. 
+  Organizations treat the security review as a gate at the end of development, so findings arrive too late to fix cheaply. 
+  Builders receive no training in threat modeling or secure coding and cannot recognize risks in their own designs. 
+  Leaders do not connect development decisions to the organization's security policies, so teams cannot tell whether a choice is compliant. 
+  Security ownership sits with one team that becomes a bottleneck as the number of workloads grows. 

 **Benefits of establishing this best practice:** 
+  Builders identify and fix security issues during design, when remediation costs the least. 
+  Feature delivery accelerates because security review stops being a late-stage bottleneck. 
+  Software quality improves as security becomes part of the definition of done. 
+  Security knowledge spreads across teams instead of concentrating in one group. 
+  A shared ownership culture reduces the friction between delivery speed and security. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A central security team cannot review every design decision in a growing organization. As the number of workloads and teams increases, a single review queue becomes the constraint that slows delivery and pushes teams to work around it. Move security decision-making to the builders themselves and reserve the central function for setting standards, handling novel risks, and auditing outcomes. 

 Teams require both skill and authority to be successful in this process. A team that cannot recognize an injection flaw will ship one, and a team without the mandate to delay a release will ship it anyway. Threat modeling gives teams a way to reason about risks before they write code, and secure coding practices provide patterns to avoid common defect classes. Pair the training with a clear statement of which decisions teams can make on their own and which require escalation. 

 A security champions or guardians program puts this model into practice. A champion is a security-focused builder in the team who takes a deeper interest in security and acts as the first point of contact for peers. The champion translates organizational policy into the team's context and routes hard questions to the central team. Naming champions without giving them time or backing turns the role into a title with no effect. 

 If meeting a security requirement means filing a ticket and waiting, teams will find a faster path that skips the control. Publish self-service guidance, code examples, and pre-approved building blocks. Use [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [AWS Cloud Development Kit (AWS CDK) (AWS CDK) constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html), and [Service Catalog](https://aws.amazon.com/servicecatalog/) to distribute vetted, secure configurations that teams deploy without custom work. For training, draw on the [AWS Threat Modeling Workshop](https://catalog.workshops.aws/threatmodel/en-US), [AWS Training and Certification](https://aws.amazon.com/training/), and the application security guidance in [AWS DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html). 

 Improve the program over time. Collect feedback on where the review process and training help and where they get in the way, and adjust. Game days and bug bashes expose real issues in your software and build team skills through practice. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess current skills and gaps:** Survey your teams, review recent code, and talk with builders to find where secure development knowledge is missing. Use the results to target training rather than delivering the same material to all builders. 

1.  **Define the security review process and responsibilities:** Work with your security team and stakeholders to document who does what, which decisions teams own, and which require escalation. State clearly when a review is required so that no one discovers the requirement late. 

1.  **Establish a security champions program:** Name a builder on each team as the local security contact, and give them dedicated time and backing from the central team. Set up a channel for champions to share findings and raise questions across teams. 

1.  **Deliver training on threat modeling and secure coding:** Run sessions using resources such as the [AWS Threat Modeling Workshop](https://catalog.workshops.aws/threatmodel/en-US) and [AWS Training and Certification](https://aws.amazon.com/training/). Favor hands-on exercises over lectures, and repeat training as tools and threats change. 

1.  **Publish self-service secure configurations:** Provide code examples, templates, and pre-approved building blocks with [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [AWS CDK constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html), and [Service Catalog](https://aws.amazon.com/servicecatalog/) so teams meet requirements without custom setup or a central queue. 

1.  **Run security exercises:** Organize game days and bug bash campaigns that uncover real issues and build skills at the same time. Feed what you learn back into training and the self-service materials. 

1.  **Gather feedback and improve:** Collect input from teams on the review process, training, and tools on a regular cadence. Use it to refine the materials, remove friction, and keep the program aligned with current practice. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC11-BP02 Follow established secure coding guidelines](sec11-bp02.md) 
+  [SEC11-BP03 Automate testing throughout the development and release lifecycle](sec11-bp03.md) 
+  [SEC11-BP05 Conduct code reviews](sec11-bp05.md) 

 **Related documents:** 
+  [How to think about cloud security governance](https://aws.amazon.com/blogs/security/how-to-think-about-cloud-security-governance/) 
+  [How to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/) 
+  [How AWS built the Security Guardians program, a mechanism to distribute security ownership](https://aws.amazon.com/blogs/security/how-aws-built-the-security-guardians-program-a-mechanism-to-distribute-security-ownership/) 
+  [How to build your own Security Guardians program to distribute security ownership](https://aws.amazon.com/blogs/security/how-to-build-your-own-security-guardians-program/) 
+  [AWS DevOps Guidance – the DevOps sagas](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/the-devops-sagas.html) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Scaling security with Sportsbet's Security Guardians program (APS204)](https://www.youtube.com/watch?v=Cf4Vj89ol1s) 
+  [AWS re:Inforce 2025 - Upskill your team with the AWS Security Champion Learning Plan (SEC222)](https://www.youtube.com/watch?v=nJugZzTrAps) 
+  [AWS re:Inforce 2025 - Build and scale a security-first engineering culture (SEC204)](https://www.youtube.com/watch?v=eoXQT_gbliw) 

 **Related examples:** 
+  [AWS Threat Modeling Workshop](https://catalog.workshops.aws/threatmodel/en-US) 
+  [OWASP Top 10 – industry awareness for developers](https://owasp.org/projects/top-ten) 

 **Related services:** 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [AWS Cloud Development Kit (AWS CDK) (AWS CDK)](https://aws.amazon.com/cdk/) 
+  [Service Catalog](https://aws.amazon.com/servicecatalog/) 