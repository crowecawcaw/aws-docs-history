

# Actions, resources, and condition keys for AWS IQ
<a name="list_iq"></a>

AWS IQ (service prefix: `iq`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/aws-iq/latest/user-guide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-iq/latest/user-guide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/set-up-expert-account-permissions-to-use-aws-iq.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iq/iq.json) for this service.

**Topics**
+ [Actions defined by AWS IQ](#list_iq-actions-as-permissions)
+ [Resource types defined by AWS IQ](#list_iq-resources-for-iam-policies)
+ [Condition keys for AWS IQ](#list_iq-policy-keys)

## Actions defined by AWS IQ
<a name="list_iq-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptCall](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to accept an incoming voice/video call
  - **Resource types (\*required):** [call\*](#list_iq-resource-call)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ApprovePaymentRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to approve a payment request
  - **Resource types (\*required):** [paymentRequest\*](#list_iq-resource-paymentRequest)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ApproveProposal](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to approve a proposal
  - **Resource types (\*required):** [proposal\*](#list_iq-resource-proposal)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ArchiveConversation](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to archive a conversation
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CompleteProposal](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to complete a proposal
  - **Resource types (\*required):** [proposal\*](#list_iq-resource-proposal)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateConversation](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to respond to a request or send a direct message to initiate a conversation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateExpert](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to create an expert profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateListing](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to create a listing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateMilestoneProposal](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to create a milestone proposal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePaymentRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to create a payment request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateProject](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to submit new requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to submit new requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateScheduledProposal](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to create a scheduled proposal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSeller](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to create a seller profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateUpfrontProposal](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to create an upfront proposal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeclineCall](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to decline an incoming voice/video call
  - **Resource types (\*required):** [call\*](#list_iq-resource-call)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAttachment](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to delete an existing attachment
  - **Resource types (\*required):** [attachment\*](#list_iq-resource-attachment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableIndividualPublicProfile](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to disable individual public profile page
  - **Resource types (\*required):** [expert\*](#list_iq-resource-expert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DownloadAttachment](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to download existing attachment
  - **Resource types (\*required):** [attachment\*](#list_iq-resource-attachment)
  - **Condition keys:**  
  - **Access level:** Read

- **   [EnableIndividualPublicProfile](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to enable individual public profile page
  - **Resource types (\*required):** [expert\*](#list_iq-resource-expert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [EndCall](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to end a voice/video call
  - **Resource types (\*required):** [call\*](#list_iq-resource-call)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetBuyer](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read buyer information
  - **Resource types (\*required):** [buyer\*](#list_iq-resource-buyer)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCall](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read details of a voice/video call
  - **Resource types (\*required):** [call\*](#list_iq-resource-call)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChatInfo](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read the chat environment details about a conversation
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChatMessages](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read chat messages in a conversation
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChatToken](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to request a websocket token for the conversation notifications
  - **Resource types (\*required):** [token\*](#list_iq-resource-token)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCompanyChatMessages](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read chat messages in a company conversation
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCompanyProfile](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read a company profile
  - **Resource types (\*required):** [company\*](#list_iq-resource-company)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConversation](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read details of a conversation
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetExpert](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read expert information
  - **Resource types (\*required):** [expert\*](#list_iq-resource-expert)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetListing](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read a listing
  - **Resource types (\*required):** [listing\*](#list_iq-resource-listing)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMarketplaceSeller](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read a seller profile information
  - **Resource types (\*required):** [seller\*](#list_iq-resource-seller)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPaymentRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read a payment request
  - **Resource types (\*required):** [paymentRequest\*](#list_iq-resource-paymentRequest)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProposal](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read a proposal
  - **Resource types (\*required):** [proposal\*](#list_iq-resource-proposal)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to get a created request
  - **Resource types (\*required):** [request\*](#list_iq-resource-request)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetReview](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to read a review for an expert
  - **Resource types (\*required):** [seller\*](#list_iq-resource-seller)
  - **Condition keys:**  
  - **Access level:** Read

- **   [HideRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to hide a request
  - **Resource types (\*required):** [request\*](#list_iq-resource-request)
  - **Condition keys:**  
  - **Access level:** Write

- **   [InitiateCall](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to start a voice/video call
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [LinkAwsCertification](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to link an AWS certification to individual profile
  - **Resource types (\*required):** [expert\*](#list_iq-resource-expert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListAttachments](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list existing attachments
  - **Resource types (\*required):** [attachment\*](#list_iq-resource-attachment)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConversations](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list existing conversations
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExpertAccessLogs](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list access logs of expert activity
  - **Resource types (\*required):** [permission\*](#list_iq-resource-permission)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListListings](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list listings
  - **Resource types (\*required):** [listing\*](#list_iq-resource-listing)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPaymentRequests](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list payment requests
  - **Resource types (\*required):** [paymentRequest](#list_iq-resource-paymentRequest) / **Condition keys:**  
  - **Resource types (\*required):** [paymentSchedule](#list_iq-resource-paymentSchedule) / **Condition keys:**  
  - **Access level:** Read

- **   [ListProposals](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list proposals
  - **Resource types (\*required):** [proposal\*](#list_iq-resource-proposal)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRequests](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list requests that are created
  - **Resource types (\*required):** [request\*](#list_iq-resource-request)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListReviews](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list reviews for an expert
  - **Resource types (\*required):** [seller\*](#list_iq-resource-seller)
  - **Condition keys:**  
  - **Access level:** Read

- **   [MarkChatMessageRead](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to mark a message as read in a conversation
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectPaymentRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to reject a payment request
  - **Resource types (\*required):** [paymentRequest\*](#list_iq-resource-paymentRequest)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectProposal](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to reject a proposal
  - **Resource types (\*required):** [proposal\*](#list_iq-resource-proposal)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendCompanyChatMessage](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to send a message in a conversation as a company
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendIndividualChatMessage](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to send a message in a conversation as an individual
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UnarchiveConversation](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to unarchive a conversation
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UnlinkAwsCertification](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to unlink an AWS certification from individual profile
  - **Resource types (\*required):** [expert\*](#list_iq-resource-expert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCompanyProfile](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to update a company profile
  - **Resource types (\*required):** [company\*](#list_iq-resource-company)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConversationMembers](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to add more participants into a conversation
  - **Resource types (\*required):** [conversation\*](#list_iq-resource-conversation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateExpert](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to update an expert information
  - **Resource types (\*required):** [expert\*](#list_iq-resource-expert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateListing](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to update a listing
  - **Resource types (\*required):** [listing\*](#list_iq-resource-listing)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to update a request
  - **Resource types (\*required):** [request\*](#list_iq-resource-request)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UploadAttachment](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to upload an attachment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [WithdrawPaymentRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to withdraw a payment request
  - **Resource types (\*required):** [paymentRequest\*](#list_iq-resource-paymentRequest)
  - **Condition keys:**  
  - **Access level:** Write

- **   [WithdrawProposal](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to withdraw a proposal
  - **Resource types (\*required):** [proposal\*](#list_iq-resource-proposal)
  - **Condition keys:**  
  - **Access level:** Write

- **   [WriteReview](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to write a review for an expert
  - **Resource types (\*required):** [seller\*](#list_iq-resource-seller)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS IQ
<a name="list_iq-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [attachment](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::attachment/${AttachmentId} |   | 
|  [buyer](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::buyer/${BuyerId} |   | 
|  [call](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::call/${CallId} |   | 
|  [company](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::company/${CompanyId} |   | 
|  [conversation](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::conversation/${ConversationId} |   | 
|  [expert](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::expert/${ExpertId} |   | 
|  [listing](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::listing/${ListingId} |   | 
|  [paymentRequest](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::paymentRequest/${ConversationId}/${ProposalId}/${PaymentRequestId} |   | 
|  [paymentSchedule](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::paymentSchedule/${ConversationId}/${ProposalId}/${VersionId} |   | 
|  [permission](https://aws.amazon.com/iq/)  | arn:${Partition}:iq-permission:${Region}::permission/${PermissionRequestId} |   | 
|  [proposal](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::proposal/${ConversationId}/${ProposalId} |   | 
|  [request](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::request/${RequestId} |   | 
|  [seller](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::seller/${SellerAwsAccountId} |   | 
|  [token](https://aws.amazon.com/iq/)  | arn:${Partition}:iq:${Region}::token/${TokenId} |   | 

## Condition keys for AWS IQ
<a name="list_iq-policy-keys"></a>

AWS IQ has no service-specific condition keys that can be used in the `Condition` element of policy statements.