

# Cancel Membership
<a name="cancel-membership"></a>

 A role having the CancelMembership permission for AWS Security Incident Response can cancel the membership from the console, the API, or AWS Command Line Interface.

**Important**  
 After you cancel your membership, you can't view historic case data. When you cancel a membership, your membership is deleted immediately and you won't have further access to the cases on the membership. Any resources or investigations that are `Active` or `ready to close` are terminated upon membership cancellation. 

When you cancel a membership:

Your membership is deleted and you won't further access to the cases on the membership.

**Important**  
 If you resubscribe to the service, a new membership is created and the case resources that lived under the prior membership are only accessible if you downloaded them prior to cancellation. 

 After the membership has been canceled, everyone in the membership incident response team is notified by email. 

**Important**  
 If you created a membership using a delegated administrator account and you use the AWS Organizations API to remove the delegated administrator designation from the account, the membership is terminated immediately. 

**Important**  
 After you cancel your membership, the service-linked roles `AWSServiceRoleForSecurityIncidentResponse` and `AWSServiceRoleForSecurityIncidentResponse_Triage` are not automatically deleted. You must manually delete these roles from all accounts that were within the scope of the AWS Security Incident Response service. For instructions, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*. 