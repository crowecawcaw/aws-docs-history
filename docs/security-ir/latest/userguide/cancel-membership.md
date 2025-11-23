# Cancel Membership

A role having the CancelMembership permission for AWS Security Incident Response can
cancel the membership from the console, the API, or AWS Command Line Interface.

###### Important

Once a membership has been canceled, you will be unable to view
historic case data. When you cancel a membership, your membership will be deleted immediately
and you will not have further access to the cases on the membership. Any resources or investigations
that are `Active` or `ready to close` will also be terminated upon membership
cancellation.

When you cancel a membership:

Your membership will be deleted and you will not have further access to the cases on the membership.

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
