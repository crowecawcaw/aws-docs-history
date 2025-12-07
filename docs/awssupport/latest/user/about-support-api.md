# About the AWS Support API

###### Important

End of Support Notice: Developer Support will be discontinued January 1, 2027. Customers with Developer Support can continue using their existing plan or choose to upgrade to Business Support+ anytime before January 1, 2027. Business Support+ delivers AI-powered assistance that understands the context of your operations, with 24/7 access to AWS experts at $29/month minimum per account. For more information, see [Business Support+ plan details](https://aws.amazon.com/premiumsupport/plans/business-plus/ "https://aws.amazon.com/premiumsupport/plans/business-plus/")

End of Support Notice: Business Support will be discontinued January 1, 2027. Customers with Business Support can continue using their existing plan or choose to upgrade to Business Support+ anytime before January 1, 2027. Business Support+ delivers AI-powered assistance that understands the context of your operations, with 24/7 access to AWS experts at $29/month minimum per account. For more information see, [Business Support+ plan details](https://aws.amazon.com/premiumsupport/plans/business-plus/ "https://aws.amazon.com/premiumsupport/plans/business-plus/")

End of Support Notice: On January 1, 2027, AWS will discontinue Enterprise On-Ramp. Throughout 2026, Enterprise On-Ramp customers will be automatically upgraded to AWS Enterprise Support during contract renewal or in periodic batches. Customers will receive an email notification a month before their upgrade. No further action is required. Enterprise Support provides designated TAM assignment, 15-minute response times, and AWS Security Incident Response available at no additional cost, all at a lower $5,000 minimum (reduced from $15,000). For more information, see [AWS Enterprise Support plan details](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/").

For more information, see [Developer, Business, and Enterprise On-Ramp end of support](support-plans-eos.md "support-plans-eos.md").

Developer Support, Business Support, and Enterprise On-Ramp will remain available in the AWS GovCloud (US) Region.

The AWS Support API provides access to some of the features in the [AWS Support Center](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

The API provides two different groups of operations:

- [Support case management](#casemanagement "#casemanagement") operations to manage the entire life cycle of your
  AWS support cases, from creating a case to resolving it
- [AWS Trusted Advisor](#trustedadvisorsection "#trustedadvisorsection")
  operations to access [AWS Trusted Advisor](trusted-advisor.md "trusted-advisor.md") checks

###### Note

You must have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. For more
information, see [Support](https://aws.amazon.com/premiumsupport "https://aws.amazon.com/premiumsupport").

For more information about the operations and data types provided by Support, see the
[AWS Support API Reference](../APIReference.md "../APIReference.md").

###### Topics

- [Support case management](#casemanagement "#casemanagement")
- [AWS Trusted Advisor](#trustedadvisorsection "#trustedadvisorsection")
- [Endpoints](#endpoint "#endpoint")
- [Support in AWS SDKs](#sdksupport "#sdksupport")

## Support case management

You can use the API to perform the following tasks:

- Open a support case
- Get a list and detailed information about recent support cases
- Filter your search for support cases by dates and case identifiers, including
  resolved cases
- Add communications and file attachments to your cases, and add the email
  recipients for case correspondences. You can attach up to three files. Each file can be up to 5 MB
- Resolve your cases

The AWS Support API supports CloudTrail logging for support case management operations. For
more information, see [Logging AWS Support API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

For code examples that demonstrate how to manage the entire life cycle of a
support case, see [Code examples for Support using AWS SDKs](service_code_examples.md "service_code_examples.md")..

## AWS Trusted Advisor

You can use the Trusted Advisor operations to perform the following tasks:

- Get the names and identifiers for the Trusted Advisor checks
- Request that a Trusted Advisor check be run against your AWS account and
  resources
- Get summaries and detailed information for your Trusted Advisor check results
- Refresh your Trusted Advisor checks
- Get the status of each Trusted Advisor check

The AWS Support API supports CloudTrail logging for Trusted Advisor operations. For more information,
see [AWS Trusted Advisor information in CloudTrail
logging](logging-using-cloudtrail.md#cloudtrail-logging-for-trusted-advisor "logging-using-cloudtrail.md#cloudtrail-logging-for-trusted-advisor").

You can use Amazon CloudWatch Events to monitor for changes to your check results for Trusted Advisor. For
more information, see [Monitoring AWS Trusted Advisor check results with
Amazon EventBridge](cloudwatch-events-ta.md "cloudwatch-events-ta.md").

For example Java code that demonstrates how to use the Trusted Advisor operations, see [Using Trusted Advisor as a web service](trustedadvisor.md "trustedadvisor.md").

## Endpoints

Support is a global service. This means that any endpoint that you use will update your
support cases in the Support Center Console.

For example, if you use the US East (N. Virginia) endpoint to create a case, you can use
the US West (Oregon) or Europe (Ireland) endpoint to add a correspondence to the
same case.

You can use the following endpoints for the Support API:

- US East (N. Virginia) – https://support.us-east-1.amazonaws.com
- US West (Oregon) – https://support.us-west-2.amazonaws.com
- Europe (Ireland) – https://support.eu-west-1.amazonaws.com

###### Important

- If you call the [CreateCase](../APIReference/API_CreateCase.md "../APIReference/API_CreateCase.md") operation to create test support cases, then we
  recommend that you include a subject line, such as **TEST CASE-Please ignore**. After you're done with your test
  support case, call the [ResolveCase](../APIReference/API_ResolveCase.md "../APIReference/API_ResolveCase.md") operation to resolve it.
- To call the AWS Trusted Advisor operations in the AWS Support API, you must use
  the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and
  Europe (Ireland) endpoints don't support the Trusted Advisor operations.

For more information about AWS endpoints, see [AWS Support endpoints
and quotas](../../../general/latest/gr/awssupport.md "../../../general/latest/gr/awssupport.md") in the _Amazon Web Services General Reference_.

## Support in AWS SDKs

The AWS Command Line Interface (AWS CLI), and the AWS Software Development Kits (SDKs) include support
for the Support API.

For a list of languages that support the AWS Support API, choose an operation name, such
as [CreateCase](../APIReference/API_CreateCase.md "../APIReference/API_CreateCase.md"), and in the [See Also](../APIReference/API_CreateCase.md#API_CreateCase_SeeAlso "../APIReference/API_CreateCase.md#API_CreateCase_SeeAlso") section, choose your preferred
language.
