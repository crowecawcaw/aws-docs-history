

# Implement change

 Controlled change is how you deploy new functionality and keep workloads running known, properly patched software. When change is uncontrolled, the effect of each release becomes hard to predict, and problems that surface are hard to trace back to what caused them. The same procedure run manually produces different results depending on who runs it, and a reversal that was never tested is an assumption rather than a capability. 

 This capability covers how an organization implements change safely: documenting standard activities as version-controlled runbooks, gating releases on automated functional and resilience tests, replacing infrastructure from code rather than editing it in place, and running deployments and patching through automation with tested rollback. 


|  REL08: How do you implement change?  | 
| --- | 
|  [REL08-BP01 Use runbooks for standard activities such as deployment](rel08-bp01.md)  | 
|  [REL08-BP02 Integrate functional testing as part of your deployment](rel08-bp02.md)  | 
|  [REL08-BP03 Integrate resilience testing as part of your deployment](rel08-bp03.md)  | 
|  [REL08-BP04 Deploy using immutable infrastructure](rel08-bp04.md)  | 
|  [REL08-BP05 Deploy changes with automation](rel08-bp05.md)  | 

## Capability intent
<a name="rel08-intent"></a>
+  Standard operational activities such as deployments have version-controlled runbooks with tested rollback and validation checkpoints. 
+  Functional tests run automatically in the deployment pipeline, and a failure stops the release before it reaches customers. 
+  Resilience testing injects failure and measures recovery as part of deployment, from pre-production through controlled experiments in production. 
+  Changes deploy through immutable infrastructure, replacing resources from code rather than modifying them in place. 
+  Releases and patching run through automation with pre-production testing, automatic rollback, and staggered production rollout. 

## Common issues to watch for
<a name="rel08-issues"></a>
+  Teams make manual, unplanned changes directly in production, so the effect of a change is hard to predict or reverse. 
+  Rollback steps are documented but never run, so the reversal fails at the moment it is needed most. 
+  Test failures are bypassed under deadline pressure, or tests run in an environment that does not resemble production. 
+  Teams patch and reconfigure running resources in place, so configuration drifts away from its defined state. 
+  Deployments run without bake time, stacking unverified changes so the cause of a failure cannot be isolated. 
+  Resilience weaknesses are found but left undocumented and unmitigated, so the same failure recurs. 