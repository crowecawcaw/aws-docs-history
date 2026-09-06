

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with Partner Account Connections
<a name="working-with-account-connections"></a>

Partners can manage connections between their own accounts or connections with other partners' AWS accounts using the AWS Partner Connection API. The process involves two phases:

1. **Connection Invitation Phase:** Initiating and responding to connection requests

1. **Active Connection Phase:** Managing established connections and their associated business activities

## Creating and Sending a Connection Invitation
<a name="creating-and-sending-connection-invitation"></a>

### Step 1: Create a Connection Invitation
<a name="step-1-create-connection-invitation"></a>

The first step in establishing a partner connection is creating and sending a connection invitation using the `CreateConnectionInvitation` action. When creating an invitation, you must specify:
+ **Catalog:** The AWS catalog (AWS or Sandbox) where the connection will be managed
+ **ConnectionType:** The type of relationship you want to establish. Choose one of the following:
  + **`OPPORTUNITY_COLLABORATION`:** Use this type when you want to send a connection request to another partner's account so that you can send them opportunity engagement invitations for opportunity collaboration
  + **`SUBSIDIARY`:** Use this type when you want to connect multiple AWS Marketplace seller accounts that you own to your "primary" account that you have linked with APN or where you are registered as a Partner
+ **ReceiverIdentifier:** The receiver's public partner profile ID (for Opportunity Collaboration connection type) or AWS account ID (for Subsidiary connection type)
+ **Email:** Your contact email address for communication
+ **Name:** Your name as the sender
+ **Message:** A description explaining the purpose of the connection request

When created, the invitation enters the Pending state, awaiting action from the receiver.

**Important**  
By sending a connection invitation, you consent to revealing your AWS account ID to the receiver if they accept the invitation. This disclosure is necessary to establish the account-level connection.

### Step 2: Monitor Your Sent Invitations
<a name="step-2-monitor-sent-invitations"></a>

You can track the status of invitations you've sent using the `ListConnectionInvitations` action with the `ParticipantType` parameter set to `SENDER`. This allows you to:
+ View all outgoing invitations
+ Filter by status (`PENDING`, `ACCEPTED`, `REJECTED`, `EXPIRED`)
+ Filter by connection type
+ Check specific invitations to other partners

### Step 3: Cancel an Invitation (Optional)
<a name="step-3-cancel-invitation"></a>

If you need to withdraw a pending invitation before it's been accepted, you can use the `CancelConnectionInvitation` action. Note that:
+ You can only cancel invitations in the Pending state
+ Once an invitation is accepted and a connection is established, it cannot be canceled
+ To end an established connection, you must use the `CancelConnection` action instead

## Receiving and Responding to Connection Invitations
<a name="receiving-and-responding-to-invitations"></a>

### Step 1: List Incoming Invitations
<a name="list-incoming-invitations"></a>

To view connection invitations you've received, use the `ListConnectionInvitations` action with the ParticipantType parameter set to `RECEIVER`. You can filter by:
+ Connection type
+ Status (`PENDING`, `ACCEPTED`, `REJECTED`)
+ Sender's identifier

### Step 2: Review Invitation Details
<a name="review-invitation-details"></a>

Use the `GetConnectionInvitation` action to view complete details of a specific invitation, including:
+ Sender's name and contact email
+ Invitation message explaining the purpose
+ Connection type being requested
+ Expiration date
+ Sender's public profile information

### Step 3: Accept or Reject the Invitation
<a name="accept-or-reject-invitation"></a>

After reviewing the invitation details, you have two options:

#### Option A: Accept the Invitation
<a name="option-a-accept-invitation"></a>

Use the `AcceptConnectionInvitation` action to establish the connection. When you accept:
+ A new Connection is created in the Active state
+ The invitation's status changes to Accepted
+ Your AWS account ID is revealed to the sender
+ You can begin conducting business activities enabled by the connection type

**Important**  
**Important Consent:** By accepting a connection invitation, you consent to revealing your AWS account ID to the sender. This disclosure is necessary to establish the account-level connection.

#### Option B: Reject the Invitation
<a name="option-b-reject-invitation"></a>

Use the `RejectConnectionInvitation` action if you don't wish to establish the connection. You can optionally provide a reason for rejection. Once rejected:
+ The invitation's status changes to Rejected
+ No connection is established
+ The invitation will no longer appear in your list of pending invitations

### Automatic Expiration
<a name="automatic-expiration"></a>

If no action is taken within the expiration period, the system automatically transitions the invitation to the Expired state. Expired invitations cannot be accepted or rejected.

## Managing Active Connections
<a name="managing-active-connections"></a>

### Viewing Your Connections
<a name="viewing-your-connections"></a>

Once a connection is established, both parties can view and manage it using the following actions:

**`ListConnections`:** Retrieve a list of your connections with filtering options:
+ Filter by connection type and status (e.g., `OPPORTUNITY_COLLABORATION:ACTIVE`)
+ Filter by other party's identifier
+ View summary information for each connection

**`GetConnection`:** Retrieve complete details of a specific connection, including:
+ All connection types associated with this partner relationship
+ Status of each connection type (Active or Terminated)
+ Contact information from the original invitation
+ AWS account IDs and public profile IDs of both parties
+ Creation and termination timestamps for each connection type

### Adding Connection Types to an Existing Connection
<a name="adding-connection-types"></a>

If you already have an active connection with a partner and want to establish a new type of relationship, you can send a new connection invitation with a different connection type. Upon acceptance:
+ The new connection type is added to the existing connection
+ Both connection types remain independently manageable
+ The same connection ID is maintained for the relationship

**Note**  
There can only be one active connection of any given type between two accounts in a given catalog at any time.

### Terminating Connection Types
<a name="terminating-connection-types"></a>

Either party can terminate a specific connection type using the `CancelConnection` action. When terminating:
+ Specify the connection ID and the connection type to terminate
+ Provide a reason for the termination
+ The connection type's status changes to `CANCELED`
+ Other connection types within the same connection remain unaffected

### Complete Connection Termination
<a name="complete-connection-termination"></a>

When all connection types within a connection are terminated, the connection itself transitions to the Terminated state. A completely terminated connection:
+ Cannot be reactivated, but you can send a new connection request to continue business with that account
+ Remains in the system for historical record-keeping
+ Can be viewed using the `GetConnection` API
+ Requires a new invitation to re-establish the relationship

## Monitoring Connection Events
<a name="monitoring-connection-events"></a>

Partners should monitor connection-related events using Amazon EventBridge to stay informed of:
+ New incoming connection invitations
+ Status changes to sent invitations (`ACCEPTED`, `REJECTED`, `EXPIRED`)
+ Connection terminations initiated by the other party

Upon receiving an event, use the appropriate Get API action to fetch the latest details:
+ `GetConnectionInvitation` for invitation updates
+ `GetConnection` for connection updates

### Possible Events
<a name="possible-events"></a>
+ **Connection Invitation Created:** Notifies the recipient account of incoming connection invitations.
+ **Connection Invitation Cancelled:** Notifies the recipient account when a sender cancels an incoming connection invitation.
+ **Connection Invitation Expired:** Notifies both sender and recipient accounts when a connection invitation expires without action.
+ **Connection Invitation Rejected:** Notifies the sender account when their connection invitation is rejected by the recipient.
+ **Connection Invitation Accepted:** Notifies the sender account when their connection invitation is accepted and a connection is established.
+ **Connection Cancelled:** Notifies both connected parties when all a connection is fully terminated.

## Understanding Connection States
<a name="understanding-connection-states"></a>

### Connection Invitation States
<a name="connection-invitation-states"></a>


| State | Description | Can Transition To | 
| --- | --- | --- | 
| PENDING | Initial state when created; awaiting receiver action | ACCEPTED, REJECTED, EXPIRED, CANCELED | 
| ACCEPTED | Receiver accepted; connection created | None (terminal state) | 
| REJECTED | Receiver declined; contains optional rejection reason | None (terminal state) | 
| EXPIRED | System-expired due to no action within expiration period | None (terminal state) | 
| CANCELED | Sender withdrew the invitation before acceptance | None (terminal state) | 

### Connection Type States
<a name="connection-type-states"></a>


| State | Description | 
| --- | --- | 
| ACCEPTED | Connection type is operational; associated business activities enabled | 
| CANCELED | Connection type ended by either party | 

## Best Practices
<a name="best-practices"></a>

1. **Clear Communication:** Provide detailed, clear messages in your connection invitations explaining the purpose and expected collaboration.

1. **Timely Responses:** Monitor and respond to connection invitations promptly to avoid automatic expiration.

1. **Regular Review:** Periodically review your active connections to ensure they remain relevant to your current business needs.

1. **Proper Termination:** When ending a business relationship, use the CancelConnection action with a clear reason to maintain professional communication.

1. **Event Monitoring:** Set up EventBridge rules to automatically receive notifications of connection status changes, to help stay informed of important updates.

1. **Connection Type Management:** Consider which connection types are needed before establishing connections, as each type enables different business capabilities.

1. **Security Awareness:** Remember that establishing a connection reveals AWS account IDs between parties. Only connect with trusted partners.

## Connection Types and Their Purposes
<a name="connection-types-and-purposes"></a>


| Connection Type | Purpose | Use Case | 
| --- | --- | --- | 
| OPPORTUNITY\_COLLABORATION | Enables collaboration on co-selling opportunities with other partners | When you want other partner to have access to your opportunity or vice versa, use this connection type. This connection allows you to send opportunity engagement invitations to connected partners. | 
| SUBSIDIARY | Establishes connections between your multiple AWS Marketplace seller accounts and your primary Partner account | Use when you have multiple AWS Marketplace Seller Accounts you want to connect to your primary account where you are registered as a partner and seller. | 