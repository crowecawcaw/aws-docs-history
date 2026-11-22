

# Protecting data at rest

 Data at rest is any data held in persistent storage, including block storage, object stores, databases, archives, and devices at the edge. Protecting it combines encryption, which renders data unreadable without the key, with access controls that decide who can reach it in the first place. Together they reduce the risk of unauthorized access and disclosure when the storage layer itself is exposed. 

 Encryption is not the only technique. Tokenization replaces sensitive values with placeholders that have no mathematical relationship to the original, which can narrow the compliance scope of the systems that handle them. Data masking redacts part of a value while keeping it usable, such as showing only the last few digits of an account number. These techniques can be combined or used on their own to match the sensitivity of the data and the obligations that apply to it. 

 Encryption protects data only as well as its keys are protected, so managing keys across their lifecycle is central to this capability. That lifecycle covers generation, storage, access, rotation, and monitoring. Auditing how keys are used confirms that access controls hold and surfaces anomalous behavior, and making protection the default state keeps it from depending on anyone remembering to turn it on. 


|  SEC08: How do you protect your data at rest?  | 
| --- | 
|  [SEC08-BP01 Implement secure key management](sec08-bp01.md)  | 
|  [SEC08-BP02 Enforce encryption at rest](sec08-bp02.md)  | 
|  [SEC08-BP03 Automate data at rest protection](sec08-bp03.md)  | 
|  [SEC08-BP04 Enforce access control](sec08-bp04.md)  | 

## Capability intent
<a name="sec08-intent"></a>
+  Data at rest is encrypted by default across every storage medium, so it stays unreadable even when the underlying storage is exposed. 
+  Encryption keys are managed across their full lifecycle with least-privilege access, automated rotation, and monitored usage, and no operator can read key material in plaintext. 
+  Keys map to data classification levels, so exposing or over-sharing one key affects only the data at that level rather than the entire estate. 
+  Access to data and to the keys that decrypt it follows least privilege, sensitive classifications are isolated, and public exposure is blocked by default. 
+  Protection controls are defined as code, validated before deployment, and monitored for drift with automated remediation. 
+  Immutable backups stored outside the source environment let the organization recover from operational failures and security events such as ransomware. 

## Common issues to watch for
<a name="sec08-issues"></a>
+  Storage is created without encrypt-by-default settings, so sensitive data lands unencrypted and stays that way until an exposure reveals it. 
+  A single key protects data of every classification, so over-sharing or exposing one key affects the whole estate rather than one segment of it. 
+  Human operators can reach key material in plaintext, so the confidentiality that encryption promises depends on trusting every administrator. 
+  Key operations run without audit logging or monitoring, so a principal under unauthorized control can decrypt data and the shift in access pattern goes unseen. 
+  Controls are configured once manually and never rechecked, so storage drifts out of compliance as it grows and changes. 
+  Backups are designed for hardware failure only, so ransomware or unauthorized deletion leaves no immutable copy to recover from. 