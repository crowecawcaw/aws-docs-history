# Firewall pricing for Amplify applications

The cost of implementing AWS WAF on an Amplify application is calculated based on the following two components:

- AWS WAF usage – You will be charged for your AWS WAF
  usage acoording to the AWS WAF pricing model. AWS WAF charges are based on the web access
  control lists (web ACLs) that you create, the number of rules that you add per web ACL, and
  the number of web requests that you receive. For pricing details, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").
- Amplify Hosting integration cost – There is a $15.00 per month, per app charge when you attach a web ACL to an Amplify application. This is prorated hourly.
