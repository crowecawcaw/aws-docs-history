# Updating the Service Account Used for

Joining the Domain

To update the service account that AppStream 2.0 uses for joining the domain, we
recommend using two separate service accounts for joining image builders and fleets
to your Active Directory domain. Using two separate service accounts ensures that
there is no disruption in service when a service account needs to be updated (for
example, when a password expires).

###### To update a service account

1. Create an Active Directory group and delegate the correct permissions to
   the group.
2. Add your service accounts to the new Active Directory group.
3. When needed, edit your AppStream 2.0 Directory Config object by entering the
   sign-in credentials for the new service account.
   After you've set up the Active Directory group with the new service account, any
   new streaming instance operations will use the new service account, while in-process
   streaming instance operations continue to use the old account without interruption.

The service account overlap time while the in-process streaming instance
operations complete is very short, no more than a day. The overlap time is needed
because you shouldn't delete or change the password for the old service account
during the overlap period, or existing operations can fail.
