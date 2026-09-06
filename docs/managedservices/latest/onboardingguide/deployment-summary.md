

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Deployment summary
<a name="deployment-summary"></a>

A description of the deployment. For example: 
+ This account is for a Line-of-Business application deployment (as opposed to a Product application deployment).
+ The deployment involves an auto-scaled ARP (authenticated reverse proxy) within the account’s public or DMZ subnet. 
+ Web and application servers will be deployed within the account's private subnet. 
+ An RDS (Amazon Relational Database Service) instance will also be deployed within the account’s private Subnet. 
+ The servers (ARP, web, application, database, load balancer, etc.) are separated into distinct security groups. 
+ The account requires an HA (high availability) design spread across availability zones (AZs) i.e. "Multi-AZ".