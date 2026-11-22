

# Access management for EDI

To protect your resources, access management allows only authorized and authenticated access. 

ECO operators can access your account console and instances only in certain circumstances. The following graphic shows the authentication process that ECO operators complete before they can log into the AWS console for an EDI account.

![ECO console access method.](https://docs.aws.amazon.com/EDI/latest/eco-support-guide/images/acc-op-console-access-method2.png)


For more information about access management, see [Access management in AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-access.html) in the *AMS Accelerate User Guide*.

## EDI customer account access
<a name="eco-access-how-works"></a>

**Note**  
During the EDI account onboarding and deployment, ECO requests root user permission.

When you first create an AWS account, you begin with one sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the AWS account *root user* and is accessed by signing in with the email address and password that you used to create the account.

**Important**  
We strongly recommend that you don't use the root user for your everyday tasks. Safeguard your root user credentials and use them to perform the tasks that only the root user can perform. For the complete list of tasks that require you to sign in as the root user, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*.

ECO uses a predefined access model to access your EDI account. For more information, see [How AMS accesses your account](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-access-operator.html).

For more information about ECO customer account access, see [Why and when AMS accesses your account](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/access-justification.html).

## EDI Cloud Operations UI access
<a name="eco-ui-access"></a>

During onboarding, an EDI Cloud Operations (ECO) operator assumes an administrator role to access your UI and fulfill initial user management requests. The ECO operator uses this role only to administer the UI, with no access to customer data.

## EDI Cloud Operations customer account access reasons
<a name="eco-access-triggers"></a>

In certain circumstances ECO operators can access your account console and instances to manage your resources. You can view these access events in your AWS CloudTrail logs.

EDI customer account access activity is driven by triggers in response to CloudWatch alarms and events, and incident reports or service requests that you submit. The ECO operator might perform multiple service calls and host-level activities for each access.

Access justiﬁcation, the triggers, and the initiator of the trigger are listed in the following table.


| Access | Initiator | Trigger | 
| --- | --- | --- | 
| Internal problem investigation | ECO | Problem issue (an issue that has been identiﬁed as systemic) | 
| Alert investigation and remediation | ECO | AWS Systems Manager operational work items (SSM OpsItems) | 
| Incident investigation and remediation | You | Inbound support case (an incident or service request that you submit) | 
| Inbound service request fulﬁllment | You | Inbound support case (an incident or service request that you submit) | 

For information about how to review ECO operations and automation activity in your account, see [Tracking changes in your AMS Accelerate accounts](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-change-record.html), in the *AMS Accelerate User Guide*.

## EDI Cloud Operations customer account access IAM roles
<a name="eco-access-roles"></a>

The ECO operators require the following roles to service your account.

**Important**  
Don't modify or delete these roles.



| Role name | Description | 
| --- | --- | 
| `ams-access-admin` | This role has full administrative access to your account without restrictions. AMS services use this role with restrictive session policies that limit access to deploy AMS infrastructure and operate your account. | 
| `ams-access-admin-operations` | This role grants AMS operators administrative permissions to operate your account. This role doesn't grant read, write, or delete permissions to customer content in AWS services that are commonly used as data stores, such as Amazon Simple Storage Service (Amazon S3), Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB, Amazon Redshift, and Amazon ElastiCache. Only qualiﬁed AMS operators who have a strong understanding of access management can assume this role. These operators serve as an escalation point for access management issues and access your accounts to troubleshoot AMS operator access issues. | 
| `ams-access-management` | AMS operators manually deploy this role during onboarding. The AMS Access system requires this role to manage ams- access-roles and ams-access-managed- policies stacks. | 
| `ams-access-operations` | This role has permissions to perform administrative tasks in your accounts. This role doesn't have read, write, or delete permissions to customer content in AWS services that are commonly used as data stores, such as Amazon S3, Amazon RDS, Amazon DynamoDB, Amazon Redshift, and ElastiCache. Permissions to perform AWS Identity and Access Management (IAM) write operations are also excluded from this role. AMS operators and cloud architects (CAs) can assume this role. | 
| `ams-access-read-only` | This role has read-only access to your account. AMS operators and CAs can assume this role. Read permissions to customer content in AWS services that are commonly used as data stores, such as Amazon S3, Amazon RDS, DynamoDB, Amazon Redshift, and ElastiCache, are not granted this role. | 
| `ams-access-security-analyst` | This AMS security role has permissions in your AMS account to perform dedicated security alert monitoring and security incident handling. Only a few AMS Security individuals can assume this role. | 
| `ams-access-security-analyst-read-only` | This AMS security role is limited to read-only permissions in your AMS account to perform dedicated security alert monitoring and security incident handling. | 
| `eks-osdu-{{$region}}-cluster-management-role` | This role has permissions to perform administrative tasks on the Amazon EKS cluster. AMS operators assume this role to access the cluster and perform any change activity. | 
| `ams_ssm_automation_role` | Assumed by AWS Systems Manager to execute SSM Automation documents within your account. | 
| `ams-container-connector-lambda-role-{{$region}}` | AMS operators assume this role to access the cluster for any read-only operations. This role is used to access the Amazon EKS cluster through the AWSManagedServices-RunKubernetesScript document. | 
| `EDIDeploymentFulfillmentRole` | AMS operators use this role to deploy the EDI solution on the respective accounts. | 
| `osdu-*`, `*edi*` | Don't modify or delete roles or policies starting with or having the term “osdu”, “edi” in their names. EDI services use these terms to connect between the AWS resources. These terms can be case sensitive. | 