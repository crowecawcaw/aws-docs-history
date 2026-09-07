

# LSOPS03-BP02 Limit available services to improve regulatory adherence
<a name="lsops03-bp02"></a>

 Use infrastructure tooling to allow only services that fit into required regulatory frameworks. 

 **Desired outcome:** Only approved services will be available for use. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Verify components and services used as available to comply with identified frameworks. Check vendor documentation to confirm that the products you use are approved at the vendor level. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Identify the available services by referring to [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). 

1.  Review audit guides for the available services. 

1.  Setup an AWS Organization to be able to centrally manage policies and controls. 

1.  Implement service control policies (SCP) limiting access to only the available services. 

## Resources
<a name="resources"></a>

 **Related guides, videos, and documentation:** 
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) 
+  [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) 
+  [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) 

 **Related tools:** 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) 