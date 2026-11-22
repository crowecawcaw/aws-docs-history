

# REL12-BP05 Conduct game days regularly

 A *game day* is a scheduled exercise where your team responds to a simulated failure in a production-like environment, using the same people and procedures you would use for a real event. Practice events like this make incident response a routine activity. 

 **Desired outcome:** 
+  You run resilience game days on a consistent, scheduled cadence. 
+  Game days are treated as a normal, expected part of operating the workload. 
+  Your teams respond to production issues with confidence because they have rehearsed the procedures. 
+  Lessons from each game day feed back into your recovery processes and runbooks. 

 **Common anti-patterns:** 
+  Teams document recovery procedures but never exercise them. 
+  Exercises exclude business decision-makers and involve only technical staff. 
+  A game day runs without informing all relevant stakeholders in advance. 
+  Teams focus solely on technical failures and ignore business impact. 
+  Lessons learned are not incorporated into recovery processes. 
+  Failures during the exercise lead to blaming teams rather than improving the system. 

 **Benefits of establishing this best practice:** 
+  Teams sharpen response and communication skills through realistic rehearsal. 
+  Hidden dependencies between systems and services surface and get addressed. 
+  Cross-functional participation builds a shared culture of resilience. 
+  Regular exercises keep recovery strategies current as the workload changes. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Rehearse failover in realistic conditions to build the habits that let your team detect and respond quickly when a real event occurs. Rehearsals also expose the gap between a procedure as written and a procedure as executed. 

 A game day that involves only engineers tests the technology but misses the coordination, decision-making, and communication that are required in real incidents. Include business decision-makers and stakeholders, and inform everyone of the date, time, and scenarios in advance. Well-scoped game days can discover previously-unknown dependencies between systems, services, and teams. They confirm that critical services are covered by runbooks and can be recovered or scaled within expected timelines. 

 Simulate events according to procedures and monitor the impact. When the design works, automated detection, scaling, and self-healing activate with little or no user impact. When negative impact appears, roll back the test and remedy the issue, either automatically or through documented manual steps. Use fault injection to create realistic failure scenarios, following the methodology in [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md). 

 End each game day with documented lessons, and use them to improve systems, processes, and teams. Keep the review blameless so people report what happened. In AWS, use infrastructure as code to build production replicas for these exercises, so you can rehearse without risking production. [AWS Fault Injection Service](https://aws.amazon.com/fis/) creates the failure scenarios, [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) observe system behavior during the exercise, [AWS Systems Manager](https://aws.amazon.com/systems-manager/) runs the playbooks, and [AWS Step Functions](https://aws.amazon.com/step-functions/) orchestrates recurring game day workflows. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a game day program:** Define the frequency, scope, and objectives of your game days as a structured program. Involve key stakeholders and subject matter experts in both planning and running the exercises. 

1.  **Prepare the game day:** Identify the business-critical services in scope, and catalog the people, processes, and technologies that support them. Set the agenda, brief the participating teams, and prepare your automation to simulate the scenarios and run recovery. Use [AWS Fault Injection Service](https://aws.amazon.com/fis/) to inject faults (see [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md) for experiment design), including cross-account experiments for multi-account architectures and multi-step experiment workflows that model cascading failures or compound scenarios. Use [AWS Step Functions](https://aws.amazon.com/step-functions/) to orchestrate the overall game day workflow, and [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to run recovery actions. 

1.  **Run the simulation:** Execute the planned scenario on the game day. Observe and document how the people, processes, and technologies respond to the simulated event. 

1.  **Conduct a blameless retrospective:** Hold a review session to capture lessons learned and identify areas to improve. Document findings and track the resulting changes to completion so they strengthen your resilience posture and preparedness. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md) 
+  [REL12-BP01 Use playbooks to investigate failures](rel12-bp01.md) 
+  [REL12-BP02 Perform post-incident analysis](rel12-bp02.md) 
+  [OPS07-BP02 Identify and drive improvements](ops07-bp02.md) 
+  [OPS07-BP03 Perform knowledge management](ops07-bp03.md) 

 **Related documents:** 
+  [What is AWS GameDay?](https://aws.amazon.com/gameday/) 
+  [Game day](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.gameday.en.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Practice like you play: How Amazon scales resilience to new heights (ARC316)](https://www.youtube.com/watch?v=r3J0fEgNCLQ) 

 **Related examples:** 
+  [Build Your Own Game Day to Support Operational Resilience](https://aws.amazon.com/blogs/architecture/build-your-own-game-day-to-support-operational-resilience/) 

 **Related workshops:** 
+  [AWS workshop - Navigate the storm: Unleashing controlled chaos for resilient systems](https://catalog.us-east-1.prod.workshops.aws/workshops/eb89c4d5-7c9a-40e0-b0bc-1cde2df1cb97) 