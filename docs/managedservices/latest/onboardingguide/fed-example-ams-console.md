

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Configuring federation to the AMS console
<a name="fed-example-ams-console"></a>

The IAM roles and SAML identity provider (Trusted Entity) detailed in the following table are provisioned in your new application account. These roles allow you to gain access to the new application account and file RFCs, write to S3 buckets, and perform other actions.


| **Role** | **Permissions** | 
| --- | --- | 
| AWSManagedServicesReadOnlyRole | Allows you to view the resources in your new application account. | 
| AWSManagedServicesCaseRole | Allows you to view the resources in your new application account and file AWS Support tickets. | 
| AWSManagedServicesChangeManagementRole | Allows you to view the AMS infrastructure in the application accounts, file RFCs, file AWS Support tickets, write to S3 buckets, manage Secrets Manager secrets, and manage Reserved Amazon Elastic Compute Cloud (Amazon EC2) instances. | 
| AWSManagedServicesSecurityOpsRole | Allows you to view the AMS infrastructure in the application accounts, manage Secrets Manager secrets, manage Web Application Firewall rules, manage certificates, and file AWS Support tickets. | 
| AWSManagedServicesAdminRole | Allows you to view the AMS infrastructure in the application accounts, manage Marketplace subscriptions, manage Secrets Manager secrets, manage Web Application Firewall rules, manage certificates, create RFCs, manage Reserved Amazon EC2 instances, write to S3 buckets, file AWS Support tickets, and manage AWS Artifacts agreements. | 