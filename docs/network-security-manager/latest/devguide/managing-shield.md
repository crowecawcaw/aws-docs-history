

# Managing DDoS protections for AWS Shield Advanced
<a name="managing-shield"></a>

With AWS Network Security Manager, you centrally configure and deploy AWS Shield Advanced protections across accounts and resources in your organization. You can define DDoS protection policies and enforce them at scale through AWS Network Security Manager policies and deployments.

**AWS Network Security Manager is billed separately**  
AWS Network Security Manager is not a part of the AWS Shield Advanced offer. For more information about pricing, see [AWS Network Security Manager pricing](https://aws.amazon.com/network-security-manager/pricing/) and [AWS Shield Advanced pricing](https://aws.amazon.com/shield/pricing/).

**AWS Shield Advanced subscription**  
When an active deployment includes an account in its scope, AWS Network Security Manager subscribes that account to AWS Shield Advanced. AWS Network Security Manager does not cancel the subscription when the account leaves the scope or when you remove the deployment. To cancel an AWS Shield Advanced subscription, see [Subscribing to AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/enable-ddos-prem.html) in the *AWS WAF Developer Guide*.