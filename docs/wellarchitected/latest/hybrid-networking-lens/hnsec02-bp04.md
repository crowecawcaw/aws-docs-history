

# HNSEC02-BP04 Limit access to networking APIs
<a name="hnsec02-bp04"></a>

 Implement strict controls over network management interfaces and APIs to prevent unauthorized access and changes to critical network infrastructure. This includes limiting access based on identity, role, and network location while maintaining comprehensive audit trails of all management actions. 

 **Desired outcome:** Prevent unauthorized access and modification of sensitive networking resources by restricting API access to approved personnel and secure locations. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Minimizes risk of accidental or malicious changes to critical network resources 
+  Supports enforcement of least privilege and security boundaries 
+  Reduces attack surface and potential for misconfiguration 
+  Enables better auditability and compliance 

## Implementation guidance
<a name="implementation-guidance-13"></a>
+  Grant access to networking APIs only to authorized networking teams or accounts. For example, you can achieve this using AWS IAM policies and resource-based policies. 
+  Monitor and audit API call to sensitive networking services, using services such as AWS CloudTrail. 
+  Regularly review permissions and restrict access on a least-privilege basis. 

## Resources
<a name="resources-12"></a>
+  [Controlling Access to AWS Resources Using Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) 
+  [IAM Policy Conditions for Source IP](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html#AvailableKeys) 
+  [AWS CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) 
+  [Best Practices for IAM Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 