# Orchestrating recovery with recovery plans

Multi-tier applications usually have to be recovered in a specific order. A database tier
must be running before the application tier starts, and the application tier must be running
before the web tier accepts traffic. Recovering these servers one at a time, in the right
order, during a disaster is slow and error-prone.

A **recovery plan** captures that order once so that you can
run it on demand. You group your source servers into ordered steps, optionally insert wait
times between steps, and then run the whole plan with a single action. AWS Elastic Disaster Recovery recovers
each step in sequence. Within a step it recovers all of the servers in parallel, and waits
for every server to reach a terminal state before it starts the next step.

You can run a recovery plan as a drill at any time to validate your disaster recovery
readiness without affecting your source servers, and run the same plan in recovery mode
during an actual event.

###### Note

Recovery plans recover source servers within a single AWS account and AWS Region.
All of the source servers in a plan must be in the same account and Region as the
plan.

###### Topics

- [Recovery plan concepts](recovery-plans-concepts.md "recovery-plans-concepts.md")
- [How a recovery plan runs](recovery-plans-how-it-works.md "recovery-plans-how-it-works.md")
- [Validation that runs before a server is recovered](recovery-plans-validation.md "recovery-plans-validation.md")
- [Controlling how server failures affect a plan](recovery-plans-impact-levels.md "recovery-plans-impact-levels.md")
- [Creating a recovery plan](recovery-plans-creating.md "recovery-plans-creating.md")
- [Adding and ordering steps](recovery-plans-steps.md "recovery-plans-steps.md")
- [Running a recovery plan](recovery-plans-executing.md "recovery-plans-executing.md")
- [Monitoring an execution](recovery-plans-monitoring.md "recovery-plans-monitoring.md")
- [Retrying, skipping, and canceling](recovery-plans-intervening.md "recovery-plans-intervening.md")
- [Editing and deleting recovery plans](recovery-plans-managing.md "recovery-plans-managing.md")
- [Recovery plan quotas](recovery-plans-quotas.md "recovery-plans-quotas.md")
