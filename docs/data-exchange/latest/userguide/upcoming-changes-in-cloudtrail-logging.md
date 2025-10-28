# Upcoming changes in AWS Data Exchange CloudTrail

logging

This section summarizes the upcoming changes for logging API calls in AWS CloudTrail for AWS Data Exchange.
The effective date for the change is on or after September 1, 2023. We recommend reviewing your
CloudTrail usage to make sure this change will not impact your monitoring, analysis, or auditing. For
questions or concerns, please send an email message to [Support](https://console.aws.amazon.com/support/home#/case/create%3FissueType=customer-service "https://console.aws.amazon.com/support/home#/case/create%3FissueType=customer-service").

| Customer persona | Event description                         | Previous eventName               | New eventName                                         | Previous eventSource          | New eventSource                     |
| ---------------- | ----------------------------------------- | -------------------------------- | ----------------------------------------------------- | ----------------------------- | ----------------------------------- |
| Subscriber       | Subscribe to a product                    | `Subscribe`                      | `CreateAgreementRequest` and `AcceptAgreementRequest` | aws-marketplace.amazonaws.com | agreement-marketplace.amazonaws.com |
| Subscriber       | Send subscription verification request    | `Subscribe`                      | `CreateAgreementRequest` and `AcceptAgreementRequest` | aws-marketplace.amazonaws.com | agreement-marketplace.amazonaws.com |
| Subscriber       | Enable subscription auto-renewal          | `Subscribe`                      | `CreateAgreementRequest` and `AcceptAgreementRequest` | aws-marketplace.amazonaws.com | agreement-marketplace.amazonaws.com |
| Subscriber       | Disable subscription auto-renewal         | `Unsubscribe`                    | `CreateAgreementRequest` and `AcceptAgreementRequest` | aws-marketplace.amazonaws.com | agreement-marketplace.amazonaws.com |
| Subscriber       | Cancel subscription verification request  | `CancelAgreementRequest`         | `CancelAgreementRequest`                              | aws-marketplace.amazonaws.com | agreement-marketplace.amazonaws.com |
| Provider         | Publish a product                         | `StartChangeSet`                 | `StartChangeSet`                                      | aws-marketplace.amazonaws.com | marketplacecatalog.amazonaws.com    |
| Provider         | Edit a product                            | `StartChangeSet`                 | `StartChangeSet`                                      | aws-marketplace.amazonaws.com | marketplacecatalog.amazonaws.com    |
| Provider         | Unpublish a product                       | `StartChangeSet`                 | `StartChangeSet`                                      | aws-marketplace.amazonaws.com | marketplacecatalog.amazonaws.com    |
| Provider         | Create custom offer                       | `StartChangeSet`                 | `StartChangeSet`                                      | aws-marketplace.amazonaws.com | marketplacecatalog.amazonaws.com    |
| Provider         | Edit custom offer                         | `StartChangeSet`                 | `StartChangeSet`                                      | aws-marketplace.amazonaws.com | marketplacecatalog.amazonaws.com    |
| Provider         | Approve subscription verification request | `AcceptAgreementApprovalRequest` | `AcceptAgreementApprovalRequest`                      | aws-marketplace.amazonaws.com | agreement-marketplace.amazonaws.com |
| Provider         | Decline subscription verification request | `RejectAgreementApprovalRequest` | `RejectAgreementApprovalRequest`                      | aws-marketplace.amazonaws.com | agreement-marketplace.amazonaws.com |
| Provider         | Delete subscriber contact information     | `UpdateAgreementApprovalRequest` | `UpdateAgreementApprovalRequest`                      | aws-marketplace.amazonaws.com | agreement-marketplace.amazonaws.com |
