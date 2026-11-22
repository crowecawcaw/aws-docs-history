

# SEC10-BP05 Establish a framework for learning from incidents

 Use a structured review to close the gaps in tools and processes that let an incident happen. Focus on fixing systems and keep reviews blameless. 

 **Desired outcome:** 
+  You hold a structured review after incidents that meet a defined threshold. 
+  Your reviews focus on improving tools and processes, not on blaming individuals. 
+  You use a consistent set of questions that produce actionable improvements. 
+  You assign an owner and a timeline to each improvement and track it to completion. 
+  You treat lessons learned as a standard part of your incident response process. 

 **Common anti-patterns:** 
+  Teams close incidents once service is restored and never review the root cause. 
+  Reviews focus on individual fault, which discourages honest participation. 
+  Reviews produce observations but no owned, tracked improvements. 
+  The same misconfiguration or exposure causes repeated incidents. 
+  Lessons are captured informally and never feed back into plans or playbooks. 

 **Benefits of establishing this best practice:** 
+  Recurring incidents drop because root causes are found and fixed. 
+  A blameless approach produces honest, useful analysis. 
+  Improvements get implemented because each has an owner and a timeline. 
+  Detection and response improve as gaps identified in reviews are closed. 
+  Security posture strengthens over time through continuous refinement. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Before you need a review, decide four things: what triggers a review, who participates, how the session runs, and who owns the resulting improvements. 

 Assume responders acted in good faith with the information they had, as blame can often derail exercises like this. Direct the analysis at the system condition that made the incident possible. AWS often uses a process called the Five Whys to get to the root cause of an incident. 

 Structure the review around three areas: people, process, and technology. For people, ask whether the right responders were available with the training, access, and context they needed, and confirm the contact list. For process, ask whether procedures were documented, followed, sufficient, and reachable during the event. For technology, ask whether detection fired as expected, whether tooling helped or hindered investigation, and what would reduce time-to-detect for the next incident. 

 Give each improvement an owner and a date. Follow up to confirm the change is in place. If you engaged AWS Security Incident Response, review the engineer's [case closure](https://docs.aws.amazon.com/security-ir/latest/userguide/case-closure.html) summary, which records the findings, the actions taken, and what to improve. The service also sends a [monthly report](https://docs.aws.amazon.com/security-ir/latest/userguide/monthly-report.html) that counts the cases you opened and closed, so you can see whether the same problems keep returning. 

 Make the review a standard, documented step in your incident response process that stakeholders expect, so your team learns from every qualifying incident. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define when and how a review runs:** Set the threshold that triggers a lessons learned review, who takes part, how the session is run, and how improvements are tracked. Make the review a documented, expected part of your incident response process. 

1.  **Reconstruct the incident timeline:** Capture what the incident was, when and how it was identified, which systems alerted, and which systems, services, and data were involved. Establish an agreed sequence of events before analyzing them. 

1.  **Run a blameless root cause analysis:** Examine what worked well, what did not, and which processes failed or did not scale. Focus on systemic causes in tools and processes rather than individual fault. 

1.  **Analyze across people, process, and technology:** For people, assess availability, training, and contact accuracy. For process, assess whether procedures existed, were followed, and were sufficient. For technology, assess whether detection and tooling were effective and how to shorten the time to detect the next incident. 

1.  **Assign, track, and test improvements:** Give each improvement an owner and a timeline, track it to completion, and verify the change works. Feed the results back into your plans, playbooks, and detection. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC10-BP04 Run simulations](sec10-bp04.md) 
+  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md) 
+  [SEC10-BP02 Develop incident management plans](sec10-bp02.md) 

 **Related documents:** 
+  [AWS Security Incident Response Guide (PDF)](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.pdf) 
+  [Case closure in AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/case-closure.html) 
+  [AWS Security Incident Response monthly report](https://docs.aws.amazon.com/security-ir/latest/userguide/monthly-report.html) 
+  [NCSC CAF Principle D2 - Lessons learned](https://www.ncsc.gov.uk/collection/cyber-assessment-framework/caf-objective-d/principle-d2-lessons-learned) 