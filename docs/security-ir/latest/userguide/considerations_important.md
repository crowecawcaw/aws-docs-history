# Considerations and recommendations for using

AWS Security Incident Response with AWS Organizations

The following considerations and recommendations can help you understand how a
delegated Security Incident Response administrator account operates in AWS Security Incident Response:

**A delegated Security Incident Response administrator account is regional.**

The delegated Security Incident Response administrator account and
member accounts must be added through AWS Organizations.

**Delegated administrator account for AWS Security Incident Response.**

You may designate one member account as the delegated Security Incident Response administrator account.
For example, if you designate a member
account `111122223333` in
`Europe (Ireland)`, you can't designate
another member account `555555555555` in
`Canada (Central)`. It is required that
you use the same account as delegated Security Incident Response administrator account in all other Regions.

**It is not recommended to set your organization's
management as the delegated Security Incident Response administrator account.**

Your organization's management can be the delegated Security Incident Response administrator account. However, the
AWS security best practices follow the principle of least privilege and
doesn't recommend this configuration.

**Removing a delegated Security Incident Response administrator account from a live subscription cancels
the subscription immediately.**

If you remove a delegated Security Incident Response administrator account, AWS Security Incident Response removes all the member accounts associated
with this delegated Security Incident Response administrator account. AWS Security Incident Response will not longer be enabled for all these member
accounts.
