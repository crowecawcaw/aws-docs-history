# Troubleshooting

Some things to try if you run into trouble:

- The AMS-managed Active Directory outbound security group needs to be allowed connection through your CIDR block (e.g. 10.27.0.0/16) to your domain controller.
- Trace the route in the AWS Console from domain controller to domain controller checking all security groups along the way.
- Make sure you can ping the AMS-managed Active Directory Domain Controllers if Internet Control Message
  Protocol (ICMP) is allowed.
- Make sure your Domain Controller can communicate with AWS Directory Services.
- Make sure the conditional forwarders resolve and are validated.
- If you do not see **Forest Trust** in the New Trust wizard, then your conditional forwarders may not be working correctly:
  - Use nslookup to test resolution
  - Try rebooting the Domain Controller
