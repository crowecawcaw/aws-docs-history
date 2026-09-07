

# MIDASEC03-BP02 Implement industrial data classifications and protection policies
<a name="midasec03-bp02"></a>

 Define classification tiers for industrial data (for example, public, internal, confidential, and restricted), and apply policies to control access, visibility, and protection levels accordingly. 

 **Desired outcome:** Manufacturing data is systematically classified and protected based on its criticality and sensitivity. 

 **Benefits of establishing this best practice:** Reduces risk of data leakage, safeguards sensitive data, and supports scalable governance models. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-15"></a>

 Use AWS tools like Amazon Macie and AWS IAM policies to tag, monitor, and restrict access to classified data. 

### Implementation steps
<a name="implementation-steps-16"></a>
+  Define classification categories based on business needs and risk. 
+  Tag data assets using AWS resource tags or AWS AWS Glue Data Catalog. 
+  Use Amazon Macie to identify and monitor sensitive data types. 
+  Enforce access controls and monitoring based on classification tags. 

## Resources
<a name="resources-16"></a>
+  [ What is Amazon Macie? ](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) 
+  [ Populating the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) 