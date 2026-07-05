End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Deployment summary

A description of the deployment. For example:

- This account is for a Line-of-Business (LoB) application deployment (as opposed to a product
  application deployment).
- The deployment involves an auto-scaled ARP (authenticated reverse proxy) within the account’s public/DMZ subnet.
- Web and application servers will be deployed within the account's private subnet.
- An Amazon RDS (Amazon Relational Database Service) instance will also be deployed within the account’s private subnet.
- The servers (ARP, web, application, database, load balancer, and so on) are separated into
  distinct security groups.
- The account requires an HA (high availability) design spread across Availability Zones (AZs),
  that is, _Multi-AZ_.
