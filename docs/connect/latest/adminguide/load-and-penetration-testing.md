# Load and penetration / security testing

policies for Amazon Connect

Amazon Connect regularly performs rigorous testing to ensure our service delivers the security,
reliability, and availability required to support world-class contact centers of all
sizes.

Amazon Connect has developed policies and requirements governing your the ability to conduct
your own security assessments (such as penetration tests) and load testing to validate
your environments and ensure they are production-ready. This topic explains the policies
and requirements.

## Security and penetration

testing

Due to the inherent risk of damage from security testing, Amazon Connect does not support
any customer security or penetration tests, as explained on this AWS Cloud
Security page: [Penetration Testing](https://aws.amazon.com/security/penetration-testing "https://aws.amazon.com/security/penetration-testing"). It is not listed as a permitted service under
**Customer Service Policy for Penetration Testing**.

Amazon Connect has a rigorous security and penetration test routine. If you have
requirements related to security, ask your AWS account team (Technical Account
Manager or Solution Architect) for assistance.

## Load testing

Amazon Connect considers load tests as any tests that:

- Target specific endpoints
- Generate synthetic traffic targeted at concentrated sources
- Maintain a higher than normal sustained volume of traffic
- Can accidentally exceed expected limits

These differences present potential risks for unintended impact to external
endpoints, other customers, or AWS services. You are required to follow our load
test policy for any plans that meet this criteria.

Our load test policy requires that customers:

- Only test out of hours: from 6PM-6AM in the local timezone of the AWS
  Region being tested.
- Identify an emergency contact who is reachable during the load
  test.
- Provide a document and detailed view of the planned load test.

###### Important

**You must receive approval from AWS for your load test
a minimum of two weeks in advance of the test date.**

###### To submit a request for a load test

1. Send email to
   **Amazon-Connect-Load-Test-Requests@amazon.com**
2. Upon receipt, the Amazon Connect team will provide you with the Load Test Request
   intake form.

The Amazon Connect load test team responds to emails within 48 working hours. If
you do not receive a response within that time, please follow up.

The Amazon Connect team will review your request. We will:

- Determine whether there are any risks.
- Validate whether there are any considerations with the load test having
  the ability to be detected and/or reported as being abusive.
- Given where the test is designed, determine whether it might be
  unintentionally abusive and/or impactful to other entities.
- Determine whether you have mitigations applied to your instances, which
  can impact your tests as well as your production workloads.

If we determine there is not likely to be an impact, we will provide a **written approval** to proceed.

For tests that might have impact, we will ask you to take additional steps, such
as:

- Running the instance generating traffic from a separate AWS account or
  Region.
- Adjusting the tests to minimize risk, or working with AWS closely to
  understand the scenarios and processes.

###### Important

Even with approval from AWS, you are responsible for:

- Any damages to AWS, other AWS customers, or external entities that
  are caused by your testing activities.
- Compliance with applicable laws in jurisdictions in which you operate,
  including laws and regulations governing cybersecurity or misuse of IT
  systems.
  Any load test run without approval from AWS will result in mitigation
  actions being taken against the AWS account up to and including suspension of
  service. Unauthorized testing may also be considered a violation of law and
  subject to criminal prosecution.
