# SSL certificates for product applications

What SSL certificates will your servers need so your applications (LoB and product) can reach everything they need to run and be accessible?

- Auto Scaling Group?
- Database (Amazon RDS)?
- Load Balancer?
- Deployment tool server?
- Web application firewall (AWS WAF)?
- Other instances?
  As an example, for each of the instances listed above you might need the following certificates:

WAF (cert 1) - > ELB-Ext (cert 2) - > ARP (cert 3) - > ELB-Int (cert 4) -> Website (cert 5) - >
ELB-Int (cert 6) -> Web service (cert 7).
