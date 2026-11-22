

# Protecting data in transit

 Data in transit is any data that moves from one system to another, whether between the components inside a workload or between the workload and the people and services that use it. While it moves, it crosses paths the organization does not fully control, and anyone positioned on that path can read or alter it unless the traffic is protected. Protecting data in transit keeps that data confidential and intact from the moment it leaves one system until it arrives at the next. 

 Protection rests on two ideas working together. Encryption makes the data unreadable to anyone who intercepts it, and authentication confirms that each party is who it claims to be before data is exchanged. Neither is sufficient alone: encrypted traffic to an unverified endpoint still reaches the wrong party, and a verified endpoint reached over plaintext still exposes its contents. Both depend on trustworthy certificates and keys, which is why managing that material well underpins everything else. 

 This capability covers establishing that protection: managing certificates and private keys across their lifecycle, enforcing encryption on traffic entering, leaving, and moving within the environment, and authenticating the parties to a communication. It does not cover protecting data once it is stored, which the data-at-rest capability addresses. 


|  SEC09: How do you protect your data in transit?  | 
| --- | 
|  [SEC09-BP01 Implement secure key and certificate management](sec09-bp01.md)  | 
|  [SEC09-BP02 Enforce encryption in transit](sec09-bp02.md)  | 
|  [SEC09-BP03 Authenticate network communications](sec09-bp03.md)  | 

## Capability intent
<a name="sec09-intent"></a>
+  Certificates and their private keys are provisioned, deployed, renewed, and revoked through an automated system, so private keys are never handled by people and certificates are replaced before they expire. 
+  Traffic that crosses a boundary is encrypted with current protocol versions and strong cipher suites, and the insecure alternatives are refused rather than merely discouraged. 
+  Internal service-to-service traffic is encrypted in proportion to the sensitivity of the data it carries, rather than left unprotected because it stays inside a private network. 
+  Each party to a communication verifies the identity of the other before exchanging data, so trust follows verified identity rather than network position. 
+  Authentication decisions feed authorization and monitoring, so every request can be attributed to a known identity and unexpected flows become visible. 

## Common issues to watch for
<a name="sec09-issues"></a>
+  An endpoint answers on both an encrypted and a plaintext port, so sensitive data occasionally travels unprotected and no one notices. 
+  Certificates are renewed manually and their expirations go unmonitored, so a lapsed certificate takes a service offline until someone reissues it. 
+  Private keys are copied to shared locations or handled by people, so an exposed key lets an unauthorized party impersonate the service it belonged to. 
+  Deprecated protocol versions and cipher suites without forward secrecy stay in use, so recorded traffic can be decrypted later if a key is later exposed. 
+  Internal service-to-service traffic is left unencrypted and unauthenticated on the assumption that a shared network implies trust, so someone who gains unauthorized access moves freely. 
+  Network location is treated as the only access control, so any request that reaches a service is accepted without verifying the caller's identity. 