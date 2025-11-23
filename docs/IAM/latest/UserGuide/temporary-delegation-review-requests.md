# Review Temporary delegation requests

After initiating a temporary delegation request, you can monitor, approve, and reject requests in the IAM console. The Temporary delegation requests page provides a centralized view of all requests, including those that are pending approval, completed, or rejected. As an administrator, you can review these requests to grant product providers access to AWS resources or reject them based on your organization's security policies, business requirements, or compliance standards. This visibility helps you track the lifecycle of product provider access and maintain oversight of temporary permissions.

###### Note

You must have the iam:AcceptDelegationRequest permission to approve temporary delegation requests.

###### To approve a temporary delegation request

1. Sign in to the AWS Management Console and open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane on the left, choose _Temporary delegation requests_.
3. The main page displays a list of your temporary delegation requests with the following information:
   - _Request ID_ – Unique identifier for the request
   - _Status_ – Current status (Pending, Approved, Rejected, Shared, Expired)
   - _Requestor_ - Product provider associated with the request
   - _Initiated by_ - IAM principal in the account who initiated the request for the product provider
   - _Request created_– When the request was submitted
   - _Request expires_ – When the request expired or will expire

4. (Optional) Use the filter options to view requests by status:
   - _All requests_ – View all your requests regardless of status
   - _Pending_ – View requests awaiting administrator approval
   - _Approved_ – View approved requests
   - _Shared_ – View requests for which access has been shared
   - _Rejected_ – View rejected requests with rejection reasons

5. To view detailed information about a specific request or to review a pending request for approval, choose the request ID.
6. Review the detailed request information:
   - Product provider information
   - Request reason and justification
   - Requested duration
   - Requested AWS permissions

7. If you are an administrator reviewing a pending request, choose one of the following options:
   - To approve the request, choose _Approve_. In the approval dialog, you can view the results of the permission simulation. For more information, see [Permission simulation beta capability](temporary-delegation-initiate-request.md#temporary-delegation-permission-simulation "temporary-delegation-initiate-request.md#temporary-delegation-permission-simulation"). After confirming access duration and your AWS identity, choose _Approve_ to grant access. If the product provider requested immediate access, they automatically receive temporary permissions and the access duration begins. Otherwise, notify the person who initiated the request to release access to the product provider.
   - To reject the request, choose _Reject_.
     - In the rejection dialog, provide a clear reason for the rejection to help the requester understand why their request was denied.
     - Choose _Reject_ to deny access.

8. The request list automatically refreshes to show the most current status information. You can also manually refresh the page to check for status updates.
