

# Mitigate deployment risks

 Adopt approaches that provide fast feedback on quality and provide rapid recovery from changes that do not have desired outcomes. Using these practices mitigates the impact of issues introduced through the deployment of changes. 

 The design of your workload should include how it will be deployed, updated, and operated. Implement engineering practices that align with defect reduction and quick and safe fixes. 


|  OPS04: How do you mitigate deployment risks?  | 
| --- | 
|  [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md)  | 
|  [OPS04-BP02 Automate testing and rollback](ops04-bp02.md)  | 
|  [OPS04-BP03 Develop and test rollout for consuming external dependencies](ops04-bp03.md)  | 

## Capability intent
<a name="ops04-intent"></a>
+  Production changes are released in incremental stages aligned to fault isolation boundaries, with health checks and bake time at each stage. 
+  Deployments use strategies such as blue/green or canary that preserve the previous version, so a rollout can be halted or reversed when a stage fails. 
+  Automated tests run inside the pipeline, and rollback is triggered deterministically from monitoring signals rather than manually. 
+  Change types are decoupled, so one failure does not force an unrelated change to roll back, and recovery paths are exercised regularly. 
+  Third-party and vendor updates are classified by blast radius, tested in a lower environment, and rolled out gradually with a tested recovery path. 

## Common issues to watch for
<a name="ops04-issues"></a>
+  Changes are released to all users at once, so a defect has maximum blast radius and no incremental signal to catch it early. 
+  Rollback is documented but never tested, so it fails or is too slow when it is actually needed. 
+  Rollout stages have no defined health criteria, so a bad stage proceeds instead of halting. 
+  A single failure forces a full rollback because unrelated changes were bundled together. 
+  Third-party dependency updates are pulled in without classification or testing, letting unvalidated changes into production. 