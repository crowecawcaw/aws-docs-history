

# Amazon SageMaker Role Manager
<a name="role-manager"></a>

**Note**  
Amazon SageMaker Role Manager is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Role Manager, but we do not plan to introduce new features. For more information, see [Role Manager availability change](role-manager-availability-change.md). 

Machine learning (ML) administrators striving for least-privilege permissions with Amazon SageMaker AI must account for a diversity of industry perspectives, including the unique least-privilege access needs required for personas such as data scientists, machine learning operation (MLOps) engineers, and more. Use Amazon SageMaker Role Manager to build and manage persona-based IAM roles for common machine learning needs directly through the Amazon SageMaker AI console.

Amazon SageMaker Role Manager provides 3 preconfigured role personas and predefined permissions for common ML activities. Explore the provided personas and their suggested policies, or create and maintain roles for personas unique to your business needs. If you require additional customization, specify networking and encryption permissions for [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) resources and [AWS Key Management Service](https://aws.amazon.com/kms/) encryption keys in [Step 1. Enter role information](role-manager-tutorial.md#role-manager-tutorial-enter-role-information) of the Amazon SageMaker Role Manager.

**Topics**
+ [Role Manager availability change](role-manager-availability-change.md)
+ [Using the role manager (console)](role-manager-tutorial.md)
+ [Using the role manager (AWS CDK)](role-manager-tutorial-cdk.md)
+ [Persona reference](role-manager-personas.md)
+ [ML activity reference](role-manager-ml-activities.md)
+ [Launch Studio Classic](role-manager-launch-notebook.md)
+ [Role Manager FAQs](role-manager-faqs.md)