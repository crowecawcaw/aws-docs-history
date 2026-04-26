# Cancel Membership

A role having the CancelMembership permission for AWS Security Incident Response can
cancel the membership from the console, the API, or AWS Command Line Interface.

###### Important

After you cancel your membership, you can't view
historic case data. When you cancel a membership, your membership is deleted immediately
and you won't have further access to the cases on the membership. Any resources or investigations
that are `Active` or `ready to close` are terminated upon membership
cancellation.

When you cancel a membership:

Your membership is deleted and you won't further access to the cases on the membership.

###### Important

If you resubscribe to the service, a new membership is created and the
case resources that lived under the prior membership are only accessible if
you downloaded them prior to cancellation.

After the membership has been canceled, everyone in the membership incident response
team is notified by email.

###### Important

If you created a membership using a delegated administrator account and you use the
AWS Organizations API to remove the delegated administrator designation from the account,
the membership is terminated immediately.
