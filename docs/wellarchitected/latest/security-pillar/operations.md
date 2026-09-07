

# Operations
<a name="operations"></a>

 Operations is the core of performing incident response. This is where the actions of responding and remediating security incidents occur. Operations includes the following five phases: *detection*, *analysis*, *containment*, *eradication*, and *recovery*. Descriptions of these phases and the goals can be found in the following table. 


|  **Phase**  |  **Goal**  | 
| --- | --- | 
|  Detection  |  Identify a potential security event.  | 
|  Analysis  |  Determine if security event is an incident and assess the scope of the incident.  | 
|  Containment  |  Minimize and limit the scope of the security event.  | 
|  Eradication  |  Remove unauthorized resources or artifacts related to the security event. Implement mitigations that caused the security incident.  | 
|  Recovery  |  Restore systems to known safe state and monitor these systems to verify that the threat does not return.  | 

 The phases should serve as guidance when you respond to and operate on security incidents in order to respond in an effective and robust way. The actual actions you take will vary depending on the incident. An incident involving ransomware, for example, will have a different set of response steps to follow than an incident involving a public Amazon S3 bucket. Additionally, these phases do not necessarily happen sequentially. After containment and eradication, you might need to return to analysis to understand if your actions were effective. 

 Thorough preparation across your people, processes, and technology is key to being effective in operations. Thus, follow the best practices from the [Preparation](preparation.md) section to be able to effectively respond to an active security event. 

 To learn more, see the [Operations](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/operations.html) section of AWS Security Incident Response Guide. 