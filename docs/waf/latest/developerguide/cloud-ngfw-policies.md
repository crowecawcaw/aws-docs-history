

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Using Palo Alto Networks Cloud NGFW policies for Firewall Manager
<a name="cloud-ngfw-policies"></a>

The Palo Alto Networks Cloud Next Generation Firewall (NGFW) is a third-party firewall service that you can use for your AWS Firewall Manager policies. With Palo Alto Networks Cloud NGFW for Firewall Manager, you can create and centrally deploy Palo Alto Networks Cloud NGFW resources and rulestacks across all of your AWS accounts.

To use Palo Alto Networks Cloud NGFW with Firewall Manager, you first subscribe to the [Palo Alto Networks Cloud NGFW Pay-As-You-Go](http://aws.amazon.com/marketplace/pp/prodview-nkug66dl4df4i) service in the AWS Marketplace. After subscribing, you perform a series of steps in the Palo Alto Networks Cloud NGFW service to configure your account and Cloud NGFW settings. Then, you create a Firewall Manager Cloud FMS policy to centrally deploy and manage Palo Alto Networks Cloud NGFW resources and rules across all of the accounts in your AWS Organizations.

For the procedure for creating the Firewall Manager policy, see [Creating an AWS Firewall Manager policy for Palo Alto Networks Cloud NGFW](create-policy.md#creating-cloud-ngfw-policy). For information about how to configure and manage Palo Alto Networks Cloud NGFW for Firewall Manager, see the *[Palo Alto Networks Palo Alto Networks Cloud NGFW on AWS](https://docs.paloaltonetworks.com/cloud-ngfw/aws/cloud-ngfw-on-aws)* documentation. For supported AWS Regions, see *[Cloud NGFW for AWS Supported Regions and Zones](https://docs.paloaltonetworks.com/cloud-ngfw/aws/cloud-ngfw-on-aws)*.