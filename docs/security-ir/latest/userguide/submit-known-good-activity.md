

# Step 5: Submit known-good activity to reduce false positives
<a name="submit-known-good-activity"></a>

 As part of onboarding to AWS Security Incident Response, you can tell the service about activity in your environment that is expected and authorized. Providing information about this known-good activity in advance helps reduce repeated notifications for expected behavior, so that responders can focus on findings that need your attention. 

**Topics**
+ [What you can submit](#submit-known-good-what-to-submit)
+ [Submit a request through AWS Support](#submit-known-good-support-case)
+ [What to expect](#submit-known-good-what-to-expect)

## What you can submit
<a name="submit-known-good-what-to-submit"></a>

 Submit any activity that is authorized but can resemble suspicious behavior to a detection service. The more specific your submission, the more precisely the service can distinguish your authorized activity from genuine threats. 
+ **Trusted IP addresses and ranges**. Source IP addresses or CIDR blocks that you own or operate from, such as corporate egress ranges, VPN concentrators, or managed service providers acting on your behalf.
+ **Authorized scanning and security tooling**. Vulnerability scanners, penetration-testing tools, posture-assessment platforms, or crawlers that you run or have contracted. Include the accounts, instances, or IP ranges that they operate from.
+ **Expected activity**. Scheduled operations that can resemble an incident, such as planned penetration tests, red-team exercises, automated remediation, or bulk data operations. Include a start and end date.

To process your request accurately, provide as much of the following as applies:
+ AWS account ID or IDs in scope
+ AWS Region or Regions
+ Trusted IP addresses or CIDR ranges
+ Tool or vendor name
+ Expected activity type (for example, port scanning, credential testing, or web crawling)
+ Resources involved (such as instance IDs or role ARNs)
+ Time window (one-time with a start and end, or a recurring schedule)
+ Confirmation that the activity is authorized by your organization

## Submit a request through AWS Support
<a name="submit-known-good-support-case"></a>

You submit known-good activity by opening a case with AWS Support.

**To submit known-good activity**

1. Sign in to the AWS Management Console and open Support, then choose **Support Center**. Choose **Technical**.

1. In the **How can we help?** box under **Support interactions**, describe your request in plain language. For example: *Submitting known-good activity for Security Incident Response - approved vulnerability scanner and trusted IP addresses for account 123456789012*. Review the guidance returned under **Troubleshooting your issue**, then choose **Create a case**.

1. Choose **Technical**. For **Service**, choose **Security Incident Response Service**. For **Category**, choose **Other**.

1. Choose a severity appropriate for your support plan.

1. In the case description and subject, provide the details listed in [What you can submit](#submit-known-good-what-to-submit).

1. Choose **Submit**.

## What to expect
<a name="submit-known-good-what-to-expect"></a>

 After you submit the case, AWS Security Incident Response reviews your request. When the activity is confirmed as authorized, the service records it internally as known-good for the scope you provided (accounts, IP addresses, tools, resources, and time window). From that point on, AWS Security Incident Response doesn't notify you about activity that matches what you submitted, so expected behavior no longer generates case notifications. A responder confirms the update on your support case, or follows up if any detail needs clarifying. 

 You can see what applies to your account in two places. When AWS Security Incident Response creates an auto-archive rule in Amazon GuardDuty for a confirmed false-positive pattern, that rule is visible in the GuardDuty console. Choose **Findings**, then **Suppression rules**. The request you submitted, along with the responder's confirmation of what was recorded as known-good, remains on the support case you opened, which you can reopen or reference at any time. For a current summary of everything recorded as known-good for your account, reply on that case and ask the responder to confirm the active scope. 

 To change, extend, or remove a known-good definition, for example, when a penetration test ends, a scanning tool is decommissioned, or a trusted IP range changes, open a new case using the preceding steps (or reply on the original case if it's still open), reference the earlier request, and state what should be added, modified, or removed. A responder confirms the updated scope on the case. 

**Note**  
 Known-good handling applies only to activity that matches the scope you submitted. If activity later falls outside that scope, for example, the same source IP address performs actions beyond the expected pattern, or activity continues past a stated time window, AWS Security Incident Response might still notify you. 