# Cancel Membership

A role having the CancelMembership permission for AWS Security Incident Response can
cancel the membership from the console, the API, or AWS Command Line Interface.

###### Important

Once a membership has been canceled, you will be unable to view
historic case data.
If you cancel during the month, your membership will be available until
the end of the month. Any resources or investigations that are `Active`
or `ready to close` will be terminated upon final membership
cancellation at the end of the billing cycle.

When you cancel a membership:

- You will be billed until the end of the current billing cycle (end of month)
- We will continue monitoring alerts during this period to prevent security gaps
- Example: Your membership cancellation will take effect on 2025-08-29. You will be billed until this date.
  After 2025-08-29, your membership and associated case resources will no longer be available.
  This helps protect your organization by ensuring continuous security monitoring and provides time to respond
  to unauthorized users disabling your security services without proper authorization.

###### Important

AWS Security Incident Response does not follow standard anniversary billing cycle
that happens every month. Service billing runs month to month. Some examples:

- Dec 29, Jan 29
- Jan 29, Feb 26 (Non leap year)
- Feb 26, March 29

###### Important

If you resubscribe to the service, a new membership will be created and the
case resources that lived under the prior membership are only accessible if
you downloaded them prior to cancellation.

After the membership has been canceled, everyone in the membership incident response
team are notified by email.

###### Important

If you created a membership using a delegated administrator account and you use the
AWS Organizations API to remove the delegated administrator designation from the account,
the membership will be terminated immediately.
