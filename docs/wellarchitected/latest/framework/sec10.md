

# Incident response

 Even with strong preventive and detective controls, incidents happen. Incident response is the organization's ability to anticipate, respond to, and recover from security events with minimal disruption. It rests on preparation done well before an event: knowing who responds, how they coordinate, and the procedures they follow. 

 Responding well in the cloud depends on capabilities the organization provides as foundations, such as emergency access when normal identity paths fail, centralized security tooling, and forensic environments, combined with the plans, playbooks, and practice that turn those capabilities into a fast, consistent response. This capability focuses on the response practices a workload team owns. The underlying capabilities are established in the Well-Architected Foundations. 

 This capability covers identifying responders, developing and testing incident management plans and playbooks, running simulations, and learning from incidents. The emergency access, security tooling, and forensic capabilities it relies on are established as foundational capabilities rather than rebuilt for each workload. 


|  SEC10: How do you anticipate, respond to, and recover from security incidents?  | 
| --- | 
|  [SEC10-BP01 Identify key personnel and external resources](sec10-bp01.md)  | 
|  [SEC10-BP02 Develop incident management plans](sec10-bp02.md)  | 
|  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md)  | 
|  [SEC10-BP04 Run simulations](sec10-bp04.md)  | 
|  [SEC10-BP05 Establish a framework for learning from incidents](sec10-bp05.md)  | 

## Capability intent
<a name="sec10-intent"></a>
+  The people who respond to incidents are known in advance, with defined roles, current contacts, and the training to act. 
+  Response follows tested management plans and scenario playbooks, so action is consistent and does not depend on improvisation under pressure. 
+  Responders draw on the emergency access, security tooling, and forensic capabilities the organization establishes as foundations, rather than assembling them during an event. 
+  Simulations exercise the plans, playbooks, access, and tooling on a regular cadence, so gaps surface before a real incident does. 
+  Every incident and simulation feeds improvements back into the plans, playbooks, and controls. 

## Common issues to watch for
<a name="sec10-issues"></a>
+  Response begins with a search for who to call, because responders and their contacts were never identified in advance. 
+  Plans and playbooks exist on paper but are never tested, so broken steps surface during a real event. 
+  Detection tools generate findings that no playbook tells responders how to handle, so alerts are ignored rather than acted on. 
+  Simulations are never run, so the first real test of the response is a real incident. 
+  Incident response is treated as a workload afterthought, so it never connects to the emergency access, tooling, and forensic foundations it depends on. 
+  Incidents close without a review, so the same weakness results in another incident and the response never improves. 