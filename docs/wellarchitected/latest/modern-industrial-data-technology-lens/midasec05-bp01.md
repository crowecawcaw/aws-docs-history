

# MIDASEC05-BP01 Define access permissions
<a name="midasec05-bp01"></a>

 Establish clear and granular access permissions to control who can access industrial data, based on job roles and operational responsibilities. 

 **Desired outcome:** Only authorized personnel can access specific data resources, reducing the risk of data leakage or misuse. 

 **Benefits of establishing this best practice:** Supports principle of least privilege, improves accountability, and reduces insider threats. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-21"></a>

 Use IAM policies and resource tagging strategies to enforce fine-grained permissions aligned to user roles. 

### Implementation steps
<a name="implementation-steps-22"></a>
+  Inventory data assets and define roles for access control. 
+  Apply IAM roles and permissions based on job functions. 
+  Use resource tags to apply conditional access policies. 
+  Review and refine permissions regularly using AWS IAM Access Analyzer. 

## Resources
<a name="resources-22"></a>
+  [ Policies and permissions in IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) 
+  [ Using IAM Access Analyzer ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html) 