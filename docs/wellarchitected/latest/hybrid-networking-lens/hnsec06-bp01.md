

# HNSEC06-BP01 Monitor your environment for malicious behavior
<a name="hnsec06-bp01"></a>

 Responding to any cyber incident requires the ability to detect threats and establish a baseline for normal operations in a hybrid environment. Continuously monitors your environment for malicious behavior to protect your accounts and workloads. 

 **Desired outcome:** Quick detection of malicious activity enables fast containment and limits the impact of ransomware and other security incidents. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Early identification of threats and abnormal behaviors 
+  Reduces containment and remediation time 
+  Enhances overall security posture with automated, continuous monitoring 

## Implementation guidance
<a name="implementation-guidance-25"></a>
+  Monitor flow logs, API activity, and DNS logs for threats, such as using Amazon GuardDuty that monitors and reports findings from these sources. 
+  Regularly review and baseline findings to distinguish normal from abnormal activity. 

## Resources
<a name="resources-23"></a>
+  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) 