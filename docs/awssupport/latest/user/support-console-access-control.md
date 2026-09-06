

# Adding IAM policies for the Support Center Console API operations
<a name="support-console-access-control"></a>

Before November 16, 2026, you must create AWS Identity and Access Management policies for the Support Center Console API operations. If you don't create these policies by November 16, 2026, you will receive `AccessDenied` errors.

To add these operations to your IAM policies, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *AWS Identity and Access Management User Guide*.

The following table summarizes the console operations.

**Note**  
These operations are for the console only. They're not available for use in the AWS SDK or the AWS CLI.


| Operation | Access level | Description | 
| --- | --- | --- | 
| GetAccountState | READ | Grants permission for the console to show the current account state. | 
| GetAccountGovCloudEnabled | READ | Grants permission to determine if your account is GovCloud enabled. | 
| GetCaseDraft | READ | Grants permission for the console to show the case draft that you previously created. | 
| CreateCaseDraft | WRITE | Grants permission to create or update a case draft for the given case type. | 
| DeleteCaseDraft | WRITE | Grants permission to delete a case draft for the given case type. | 
| GetBanner | READ | Grants permission for the console to show the Support banner displayed during customer impacting events. | 
| DescribeDynamicHelp | READ | Grants permission for the console to show dynamic help resources for the selected service and category. | 
| CreateContact | WRITE | Grants permission for the console to create an authenticated contact for the selected contact type, such as the [Request to remove email sending limitations](https://console.aws.amazon.com/support/contacts#/rdns-limits), [Report Abusive Actvity from AWS Resources](https://console.aws.amazon.com/support/contacts#/report-abuse), and [Simulated Event Submissions](https://console.aws.amazon.com/support/contacts#/simulated-events) forms.<br />The following are examples of some of the forms that use this permission.![Request to remove email sending limitations form in the Support Center Console.](http://docs.aws.amazon.com/awssupport/latest/user/images/create-contact-rdns-form.png)![Simulated Events form in the Support Center Console.](http://docs.aws.amazon.com/awssupport/latest/user/images/create-contact-simulated-events-form.png) | 
| CheckSubscription | READ | Grants permission for the console to verify if your account has access to the selected product. | 
| GetQuestionnaire | READ | Grants permission for the console to show the customer feedback questionnaire. | 
| SaveFeedback | WRITE | Grants permission to save questionnaire feedback. | 

**Note**  
 If you have a custom VPN configuration, make sure that you configure your VPN to correctly forward your client IP address to the Support Center Console API endpoint. When using a VPN with AWS Identity and Access Management policies that include [aws:SourceIp](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.html) conditions, the client IP address specified in your IAM policy must be forwarded to the API endpoint, not the VPN's IP address. If the VPN forwards its own IP address instead of the client IP address, authorization might fail because the IP address doesn't match the `aws:SourceIp` condition in your IAM policy. The following table provides the Support Center Console API endpoints by AWS Region.  


| AWS Region | Support Center Console API endpoint | 
| --- | --- | 
| `https://api.us-east-1.prod.support-console.support.aws.dev` | US East (N. Virginia) | 
| `https://api.us-west-2.prod.support-console.support.aws.dev` | US West (Oregon) | 
| `https://api.eu-west-1.prod.support-console.support.aws.dev` | Europe (Ireland) | 