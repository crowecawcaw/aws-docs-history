# Deployment summary

A description of the deployment. For example:

- This account is for a Line-of-Business application deployment (as opposed to a Product application deployment).
- The deployment involves an auto-scaled ARP (authenticated reverse proxy) within the account’s public or DMZ subnet.
- Web and application servers will be deployed within the account's private subnet.
- An RDS (Amazon Relational Database Service) instance will also be deployed within the account’s private Subnet.
- The servers (ARP, web, application, database, load balancer, etc.) are separated into distinct security groups.
- The account requires an HA (high availability) design spread across availability zones (AZs) i.e. "Multi-AZ".
