

# Back up data

 Data can be lost or corrupted at any point, through a hardware fault, an operator error, a failed deployment, or a deliberate attack. Some of that data can be recreated from an authoritative source, but much of it cannot, and the copy you hold in a backup is the only path back to a working system. A backup that is untested, unencrypted, or reachable by the same credentials that run production offers far less protection than teams assume. 

 This capability covers how an organization protects the data its workloads depend on: identifying and classifying each source, deciding whether to back it up or reproduce it, running backups automatically to meet recovery point and recovery time objectives, securing and encrypting the copies, keeping critical copies immutable and isolated from production, and testing recovery on a schedule so a backup is a verified capability rather than an assumption. 


|  REL09: How do you back up data?  | 
| --- | 
|  [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md)  | 
|  [REL09-BP02 Secure and encrypt backups](rel09-bp02.md)  | 
|  [REL09-BP03 Perform data backup automatically](rel09-bp03.md)  | 
|  [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md)  | 
|  [REL09-BP05 Implement cyber resilience for backup data](rel09-bp05.md)  | 

## Capability intent
<a name="rel09-intent"></a>
+  Every data source in the workload is identified and classified by criticality, with a decision to back it up or reproduce it from an authoritative source. 
+  Backup frequency and recovery method meet the recovery point objective (RPO) and recovery time objective (RTO) for each source. 
+  Backups run automatically, and a backup that does not complete raises an alert rather than passing unnoticed. 
+  Backups are encrypted at rest and in transit, and access to them is separated from access to production data. 
+  Critical backup copies are immutable and isolated from production, so recovery is possible even after a cyber attack. 
+  Recovery is tested on a regular schedule, confirming the restored data is complete and falls within the RTO and RPO. 

## Common issues to watch for
<a name="rel09-issues"></a>
+  Teams back up only some data sources, without using criticality to decide what to protect or what to reproduce. 
+  Backup frequency is set once for everything, so it cannot meet the RPO of the most critical data. 
+  Backups are created manually, so a missed backup goes unnoticed until someone needs to recover. 
+  Backups carry the same access and credentials as production, so one breached identity puts both the data and its only copy at risk. 
+  A backup is trusted without ever being restored, and corruption or a slow restore surfaces only when you actually need to recover. 
+  Backups can be deleted or encrypted during an incident because they are not immutable or isolated from production. 