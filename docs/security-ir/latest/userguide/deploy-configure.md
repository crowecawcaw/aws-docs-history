# Step 1: Enable AWS Security Incident Response

The onboarding process takes approximately 10 to 15 minutes per AWS organization. For a walkthrough, see the [Getting Started video](getting-started.md "getting-started.md") in the service documentation.

###### Note

The instructions in this section outline how to enable Security Incident Response and set up your team using the AWS Security Incident Response console (Step 1 and Step 2). You can also perform these steps using the API/CLI. For instructions on using the API/CLI, see [Enable Security Incident Response and configure your incident response team using the API/CLI](enable-sir-using-cli.md "enable-sir-using-cli.md").

###### Enable AWS Security Incident Response using the AWS Security Incident Response console

1. Sign in to the AWS Management Console using your management account.
2. Open the AWS Security Incident Response console and choose **Sign up**.

![AWS Security Incident Response sign-up page with the Sign up button.](images/AWS_Security_incident_Response.png) 3. Setup your central membership account. For guidance, see [Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md") in _AWS Prescriptive Guidance_ and [Considerations and
recommendations](considerations_important.md "considerations_important.md") on how a delegated Security Incident Response administrator account operates.

![Set up central membership account page for selecting a delegated administrator account.](images/Set_Up_Central_Membership_Account.png) 4. Sign in to the delegated administrator account. 5. Enter your membership details and associate the relevant accounts. 6. For **Account scope**, choose to enable AWS Security Incident Response for your entire AWS organization or for specific OUs. You can select coverage at the OU level, but not at the individual account level. 7. **Proactive response** is on by default and creates a service-linked role that allows AWS SIRT to ingest GuardDuty findings and open proactive investigation cases when threats are detected. For more information, see [Proactive response](proactive-response.md "proactive-response.md").

AWS Security Incident Response automatically creates the `AWSServiceRoleForSecurityIncidentResponse_Triage` service-linked role in your AWS Organizations management account and in all accounts that are in scope. 8. (Optional) Choose to pre-authorize AWS SIRT to perform containment actions on your behalf during active incidents. Supported containment actions include runbooks for compromised S3 buckets, EC2 instances, and IAM principals. If you skip this step, SIRT will provide manual guidance during investigations. For more information, see [Containment actions](containment.md "containment.md"). 9. Review the service permissions and onboarding configuration, then choose **Sign up**.

![Review service permissions screen showing the permissions that AWS Security Incident Response requires to monitor findings.](images/Review_Service_Permissions.png)

![Sign up confirmation screen for enabling proactive response monitoring.](images/Review_and_Sign_Up.png)
