

# Data classification

 Data classification categorizes the data an organization holds by its sensitivity and criticality, so the protection and retention it receives match the risk it carries. Without it, teams protect data by intuition. That intuition varies between people, lives in one person's head, and cannot be verified in an audit. 

 Classification is usually an organizational decision that individual workloads inherit. A central function defines the sensitivity levels and their handling rules, and each workload maps its data onto them and reports back where the scheme does not fit reality. Getting the level right matters in both directions. Classify too low and data that carries legal or contractual obligations is underprotected. Classify too high and ordinary data carries expensive controls that slow the people who need access and train teams to treat the policy as an obstacle. 

 This capability covers naming sensitivity levels and recording where sensitive data resides, sizing controls to each level, automating identification as data grows and moves, and managing data through its lifecycle from ingestion to destruction. It does not cover the specific encryption and access controls for data at rest or in transit, which later capabilities address. 


|  SEC07: How do you classify your data?  | 
| --- | 
|  [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md)  | 
|  [SEC07-BP02 Apply data protection controls based on data sensitivity](sec07-bp02.md)  | 
|  [SEC07-BP03 Automate identification and classification](sec07-bp03.md)  | 
|  [SEC07-BP04 Define scalable data lifecycle management](sec07-bp04.md)  | 

## Capability intent
<a name="sec07-intent"></a>
+  The organization maintains a classification scheme that names sensitivity levels and their handling rules, and every workload maps its data onto that scheme. 
+  Teams know what data they hold, where it resides, and the legal and compliance obligations attached to it, recorded in a catalog that stays current as workloads change. 
+  Protection controls and isolation boundaries are sized to the sensitivity of the data they guard, concentrating investment on the highest-risk data while keeping lower-sensitivity data accessible. 
+  Sensitive data is identified and classified automatically before it reaches production and continuously in running environments, with alerts when data appears in unauthorized places. 
+  Data is retained, transformed, and destroyed according to rules tied to its classification, and backups are isolated and protected so they remain trustworthy after an event. 
+  The provenance of a data set is tracked, so its origin and the transformations applied to it can be reconstructed during an investigation. 

## Common issues to watch for
<a name="sec07-issues"></a>
+  No formal classification scheme exists, so teams protect data by intuition that varies between people and cannot be audited. 
+  The same controls are applied to all data, so the most sensitive data is underprotected while ordinary data carries expensive controls that slow the people who need it. 
+  Data of different sensitivity shares a single boundary enforced only by policy, so one misconfiguration exposes data that should have been isolated. 
+  Classification depends on manual effort, so it cannot keep pace as data grows and moves, and sensitive data slips through unclassified. 
+  Data is classified once and never revisited, so controls drift out of alignment as data is transformed, copied, or aged into a different sensitivity. 
+  Data is retained beyond its usefulness and backups are left in the environment they came from, so storage costs rise and a single event can corrupt both the live data and its backup. 