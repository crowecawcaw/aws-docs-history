

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# SSL certificates for product applications
<a name="ssl-certs-for-prod-apps"></a>

What SSL certificates will your servers need so your applications (LoB and product) can reach everything they need to run and be accessible?
+ Auto Scaling Group?
+ Database (Amazon RDS)?
+ Load Balancer?
+ Deployment tool server?
+ Web application firewall (AWS WAF)?
+ Other instances?

As an example, for each of the instances listed above you might need the following certificates:

WAF (cert 1) - > ELB-Ext (cert 2) - > ARP (cert 3) - > ELB-Int (cert 4) -> Website (cert 5) - > ELB-Int (cert 6) -> Web service (cert 7).