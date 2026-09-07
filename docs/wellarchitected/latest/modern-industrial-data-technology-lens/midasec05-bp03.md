

# MIDASEC05-BP03 Implement data authorization models
<a name="midasec05-bp03"></a>

 Design and implement scalable data authorization frameworks using attribute-based or role-based access control (ABAC or RBAC) models. 

 **Desired outcome:** Users are granted access to data based on roles, attributes, or context, supporting scalable and secure access decisions. 

 **Benefits of establishing this best practice:** Improves flexibility in data sharing, reduces over-permissions, and enhances compliance controls. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-23"></a>

 Define authorization attributes based on manufacturing context (like job function, facility, equipment type, or product line). Implement access controls using AWS Lake Formation for data-level permissions, AWS IAM conditions for resource access, and custom logic for specialized manufacturing scenarios. 

 Regularly review access patterns to verify alignment with production needs while maintaining security boundaries between IT and OT systems. 

### Implementation steps
<a name="implementation-steps-24"></a>
+  Define business roles and relevant attributes (for example, plant location or department). 
+  Implement policies in Lake Formation or Amazon S3 bucket policies using conditions. 
+  Monitor access patterns and refine authorization models over time. 
+  Log and audit access for compliance reporting. 

## Resources
<a name="resources-24"></a>
+  [ What Is AWS Lake Formation? ](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) 
+  [ Policies and permissions in IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) 