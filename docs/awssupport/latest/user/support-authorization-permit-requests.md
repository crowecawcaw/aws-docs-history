

# Managing support permit requests
<a name="support-authorization-permit-requests"></a>

In the reactive authorization scenario, AWS Support submits a support permit request when access to information about your services is needed for support case resolution. You review each request and decide whether to approve or reject it.

## How reactive authorization works
<a name="support-authorization-permit-requests-how"></a>

The reactive authorization workflow follows these steps:

1. AWS Support identifies an issue with your resource that requires your permission to resolve.

1. AWS Support submits a support permit request, which is visible to you through AWS Support authorization. A `SupportPermitRequestCreated` event appears in your AWS CloudTrail logs.

1. You receive notifications through Amazon EventBridge events.

1. You review the request details, including the requested actions, resources, and support case context.

1. You approve the request by calling `CreateSupportPermit` with a support permit that covers the requested scope, or reject it by calling `RejectSupportPermitRequest`.

## Viewing support permit requests
<a name="support-authorization-permit-requests-view"></a>

View pending permit requests from AWS Support.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Pending access requests** section, review the list of requests. Each request shows the associated support case, service, Support Permit Request ARN, status, and request access date.

1. (Optional) Use the **Status** and **Service** dropdown filters to narrow the results, or search by resource in the search field.

------
#### [ AWS CLI ]

Use `ListSupportPermitRequests` to view permit requests. You can filter results by support case ID.

**List all support permit requests**

```
aws supportauthz list-support-permit-requests
```

**List requests for a specific support case**

```
aws supportauthz list-support-permit-requests \
    --support-case-display-id "case-12345678"
```

The response includes up to 100 results per page. Use the `nextToken` value in subsequent requests to retrieve additional pages.

------

## Approving a support permit request
<a name="support-authorization-permit-requests-approve"></a>

To approve a support permit request, create a support permit that satisfies the requested scope.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Pending access requests** section, choose **Manage support access**.

1. Review the **Request summary**, including the Support Permit Request ARN, service, status, and associated support case.

1. Review the **Access configuration**, which shows the name, description, requested actions, and access duration for the request.

1. In the **Resource access** section, choose **Approve** for each resource that you want to authorize. To approve all resources, choose **Approve all**.

1. For **Signing key**, choose an AWS KMS key from the dropdown list. To create a new key, choose **Create KMS signing key**.

1. Choose **Submit**.

------
#### [ AWS CLI ]

To approve a support permit request, create a support permit that satisfies the requested scope. Include the `supportCaseDisplayId` from the request so that the support permit automatically transitions to INACTIVE when the case closes.

```
aws supportauthz create-support-permit \
    --name "ApprovedRequest123" \
    --signing-key-info '{"kmsKey": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}' \
    --support-case-display-id "case-12345678" \
    --permit '{
        "actions": {"actions": ["rds:ReadClusterData"]},
        "resources": {"resources": ["arn:aws:rds:us-east-1:111122223333:cluster:my-cluster"]},
        "conditions": [
            {"allowBefore": "2026-06-15T00:00:00Z"}
        ]
    }'
```

When you create a support permit that covers the requested scope, the request status transitions to ACCEPTED.

------

## Rejecting a support permit request
<a name="support-authorization-permit-requests-reject"></a>

Reject a support permit request to decline an access request from AWS Support.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Pending access requests** section, choose **Manage support access**.

1. In the **Resource access** section, choose **Deny** for each resource that you want to reject. To deny all resources, choose **Deny all**.

1. Choose **Submit**.

------
#### [ AWS CLI ]

Use `RejectSupportPermitRequest` to decline an access request. The request transitions to REJECTED status and AWS Support receives notification through the support case.

```
aws supportauthz reject-support-permit-request \
    --request-arn "arn:aws:supportauthz:us-east-1:111122223333:supportpermitrequest/request-id"
```

You can only reject requests that are in PENDING status.

------

**Note**  
If you reject a support permit request or don't create a support permit that satisfies the request, AWS Support can't access the requested information and might not be able to proceed with the investigation or resolution of your support case.

## Permit request state transitions
<a name="support-authorization-permit-requests-states"></a>

A support permit request can transition to the following states from PENDING:
+ **ACCEPTED**: You created a support permit that satisfies the request.
+ **REJECTED**: You rejected the request by calling `RejectSupportPermitRequest`.
+ **CANCELLED**: AWS Support cancelled the request.