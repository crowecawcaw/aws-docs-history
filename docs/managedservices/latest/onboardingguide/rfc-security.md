# Understand RFC security reviews

The AWS Managed Services (AMS) change management approval process ensures that we perform a security review of changes
we make in your accounts.

AMS evaluates all the requests for change (RFCs) against AMS technical standards.
Any change that might lower your account's security posture by deviating from the technical standards, goes through a
security review. Duringthe security review, AMS highlights relevant risk and, in cases of high or very high security risk, your authorized security personnel accepts or rejects the RFC. All changes are also evaluated to assess for adverse impact on AMS's ability to operate. If potential adverse impacts are found, then additional reviews and approvals are required within AMS.

## AMS technical standards

AMS Technical Standards define the minimum security criteria, configurations, and processes to establish the
baseline security of your accounts. These standards must be followed by both AMS and you.

Any change that could potentially lower the security posture of your account by deviating from the
technical standards, goes through a Risk Acceptance process, where relevant risk is highlighted by AMS and
accepted or rejected by the authorized security personnel from your end. All such changes are also evaluated
to assess if there would be any adverse impact on AMS's ability to operate the account and, if so, additional
reviews and approvals are required within AMS.

## RFC customer security risk management (CSRM) process

When someone from your organization requests a change to your managed environment,
AMS reviews the change to determine whether the request might deteriorate the security posture of your account by falling
outside the technical standards. If the request does lower the security posture of the account, AMS notifies
your security team contact with the relevant risk, and executes the change; or, if the change introduces high or very high security risk in the environment,
AMS seeks explicit approval from your security team contact in the form of risk acceptance (explained next).

The AMS
Customer Risk Acceptance process is designed to:

- Ensure risks are clearly identified and communicated to the right owners
- Minimize identified risks to your environment
- Obtain and document approval from the designated security contacts who understand your organization's risk profile
- Reduce ongoing operational overhead for identified risks

## How to access technical standards and high or very high risks

We have made AMS Technical Standards documentation available for your reference in
the [https://console.aws.amazon.com/artifact/](https://console.aws.amazon.com/artifact/ "https://console.aws.amazon.com/artifact/") as a report. Use the AMS Technical Standards documentation to understand whether a
change would require risk acceptance from your authorized security contact prior to submitting a request for change (RFC).

Find the Technical Standards report by searching on "AWS Managed Services (AMS) Technical Standards" in the AWS Artifact
**Reports** tab search bar after logging in with the default **AWSManagedServicesChangeManagementRole**.

###### Note

The AMS technical standard document is accessible for the Customer_ReadOnly_Role in single-account landing zone. In multi-account landing zone,
the AWSManagedServicesAdminRole used by security admins and AWSManagedServicesChangeManagementRole used by
application teams, can be used to access the document. If your team uses a custom role, create an Other | Other
RFC to request access and we will update the specified custom role.
