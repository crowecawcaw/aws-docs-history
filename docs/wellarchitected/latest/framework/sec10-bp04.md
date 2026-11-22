

# SEC10-BP04 Run simulations

 Simulations, sometimes called game days, put your team through realistic security scenarios so they practice their roles, tools, and communication before a real incident. Regular exercises reveal gaps in plans and playbooks while the stakes are low. 

 **Desired outcome:** 
+  You run security simulations on a regular schedule, not only after an incident. 
+  You choose simulation types that match your security maturity, resources, and goals. 
+  Your responders practice their roles, tools, and communication paths during each exercise. 
+  You capture findings in an after-action report and track improvements over time. 
+  Your simulations exercise less common attack vectors alongside expected ones. 

 **Common anti-patterns:** 
+  Teams write response plans and playbooks but never exercise them. 
+  Organizations run a single exercise type and never progress in realism or difficulty. 
+  Simulations produce no after-action report, so lessons are lost. 
+  Exercises test only the tools and skip the communication and escalation paths. 
+  Invasive exercises run without controls, risking harm to production systems. 

 **Benefits of establishing this best practice:** 
+  Responders build confidence and cyber readiness before facing a real event. 
+  Exercises validate the accuracy and efficiency of tools and workflows. 
+  Communication and escalation paths are refined against the response plan. 
+  Teams gain practice responding to less common attack vectors. 
+  After-action reports turn each exercise into tracked, measurable improvement. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Simulations help you fail safely. For example, you could find a stale contact list, a broken playbook step, or an alarm that never fires. These tests mimic real-world attack tactics, techniques, and procedures and measure how well plans, tools, and people hold up. 

 Simulations vary in realism and cost. 
+  A *tabletop exercise* is a discussion-based session where stakeholders walk through roles, communication, and playbooks for a scenario. Tabletops focus on people and process and rarely touch production tooling. 
+  A *purple team exercise* pairs the defenders (blue team) with a simulated offensive team (red team). It focuses on detection mechanisms, tools, and standard operating procedures. 
+  A *red team exercise* has an offensive team pursue objectives while defenders respond without knowing the scope. This produces the most realistic assessment. 

 Match the simulation type to your maturity, resources, and goals. Many teams start with tabletops and progress toward purple and red team exercises as their capability grows. More realistic scenarios carry higher cost and risk. Red team exercises can be invasive, so implement controls that keep the exercise from causing real harm to production systems and data. Not every organization needs red team exercises, so mix types over time to cover different parts of the response. 

 Produce an *after-action report* for every exercise. Record what went well, what needs improvement, and the gaps to close. Measure both the exercise and the team's response so progress is visible across future simulations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define core exercise elements:** Choose the scenario and the objectives, and secure leadership acceptance for both. The scenario must reflect a realistic threat to your workload. 

1.  **Identify key stakeholders:** Determine the facilitators and participants, and add stakeholders such as legal, communications, or executive leadership when the scenario calls for them. 

1.  **Build and test the scenario:** Develop the scenario and refine it where elements are not feasible. Produce a finalized, tested scenario as the output of this stage. 

1.  **Facilitate the simulation:** Run the exercise using facilitation that matches the type, from a paper-based tabletop to a highly technical simulation. Engage every participant wherever possible to maximize the value. 

1.  **Develop the after-action report:** Capture what went well, what needs improvement, and the gaps found. Measure the exercise and the team's response so you can track progress across future simulations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md) 
+  [SEC10-BP02 Develop incident management plans](sec10-bp02.md) 
+  [SEC10-BP05 Establish a framework for learning from incidents](sec10-bp05.md) 

 **Related documents:** 
+  [AWS Security Incident Response Guide (PDF)](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.pdf) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Testing GuardDuty's runtime detections: Hands-on with real world attack scenarios](https://www.youtube.com/watch?v=UyakYnhI0RE) 