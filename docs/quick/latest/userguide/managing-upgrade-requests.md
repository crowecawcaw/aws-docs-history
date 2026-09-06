

# Managing upgrade requests
<a name="managing-upgrade-requests"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  | 

As an administrator, you can view and manage user license upgrade requests through the Amazon Quick admin console. This section describes how to approve, deny, or verify upgrade requests based on your organization's identity management setup.

## Viewing upgrade requests
<a name="viewing-upgrade-requests"></a>

To view pending upgrade requests, navigate to the User upgrades section in the admin console. The requests table displays the username, current role, requested role, request date, and available actions for each pending request.

**To view upgrade requests**

1. Sign in to the Amazon Quick console as an administrator.

1. Choose **Manage Amazon Quick** from the top right corner.

1. Navigate to the **User upgrades** section.

1. Review the pending requests in the table.

## Processing upgrade requests
<a name="processing-upgrade-requests"></a>

The process for handling upgrade requests varies depending on your organization's identity management setup.

### Processing requests for IdP identity type
<a name="idp-identity-requests"></a>

For organizations using Identity Provider (IdP) authentication, administrators can directly approve or deny requests.

**To process IdP upgrade requests**

1. In the upgrade requests table, choose **View details** for the request you want to process.

1. Review the request details in the modal that opens.

1. Choose one of the following options:
   + **Approve** — Grants the requested license upgrade immediately
   + **Deny** — Rejects the upgrade request

1. Confirm your selection. The system displays a success message and removes the processed request from the pending list.

### Processing requests for IAM Identity Center and Active Directory identity types
<a name="sso-ad-identity-requests"></a>

For organizations using IAM Identity Center or Active Directory, administrators must add users to the appropriate groups before verifying the upgrade.

**To process IAM Identity Center and Active Directory upgrade requests**

1. In the upgrade requests table, choose **View details** for the request you want to process.

1. Note the required group name(s) displayed in the modal.

1. Navigate to your IAM Identity Center or Active Directory management console.

1. Add the user to the required group for the requested license tier.

1. Return to the Amazon Quick admin console and choose **Verify**.

1. The system checks the user's group membership and completes the upgrade if verification succeeds.

Alternatively, you can choose **Deny** to reject the upgrade request without making any group changes.

## Understanding upgrade request statuses
<a name="upgrade-request-statuses"></a>

Upgrade requests can have the following statuses:
+ **Pending** — Request is awaiting administrator action
+ **Approved** — Request has been approved and the user's license has been upgraded
+ **Denied** — Request has been rejected by an administrator
+ **Verified** — For IAM Identity Center/AD setups, the user has been added to the required group and the upgrade is complete