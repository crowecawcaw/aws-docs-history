# Create quick connects in Amazon Connect

Quick connects are a way for you to create a list of destinations for common
transfers. For example, you might create a quick connect for Tier 2 support. If agents
in Tier 1 support can't solve the issue, they will transfer the contact to Tier 2.

**How many quick connects can I create?** To view your
quota of **Quick connects per instance**, open the Service Quotas console at
[https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").

## Types of quick connects

The type of a quick connect specifies the destination. You can specify one of the
following destinations.

### Phone number quick connect

Contacts are transferred to a phone number (such as an on-call pager).

### User quick connect

Contacts are transferred to a specific user, such as an agent, as part of a
flow.

###### Important

User and Queue quick connects only appear in the CCP when an agent goes to
transfer a contact.

### Queue quick connect

Contacts are transferred to a queue as part of a flow.

###### Important

User and Queue quick connects only appear in the CCP when an agent goes to
transfer a contact.

## Step 1: Create quick connects

Following are the instructions to add quick connects manually using the Amazon Connect
console. To add quick connects programmatically, use the [CreateQuickConnect](../APIReference/API_CreateQuickConnect.md "../APIReference/API_CreateQuickConnect.md")
API.

###### To add quick connects

1. Log in to the Amazon Connect admin website at https://`instance name`.my.connect.aws/. To find the name of your instance, see [Find your Amazon Connect instance ID or ARN](find-instance-arn.md "find-instance-arn.md").
2. On the navigation menu, choose **Routing**,
   **Quick connects**.
3. For each quick connect, do the following:
   1. Choose **Add new**.
   2. Enter a unique name. If desired, also enter a description.
   3. Choose a type.
   4. Enter the destination (for example, a phone number, the name of an
      agent, or the name of a queue).
   5. Enter a flow, if applicable.
   6. Enter a description.

4. When you're finished adding quick connects, choose
   **Save**.

## Step 2: Enable agents to

see quick connects

###### To enable your agents to see the quick connects in the CCP when they transfer

a contact

1. After you create the quick connect, go to **Routing**,
   **Queues** and then choose the appropriate queue for
   the contact to be routed to.
2. On the Edit queue page, in the Quick connect box, search for the quick
   connect you created.
3. Select the quick connect and then choose **Save**.

###### Tip

Agents see the quick connects of the queues in their routing profile,
including the Default outbound queue.

## Example: Create a phone

number quick connect to a mobile phone

In this example, you create a phone number quick connect to a person's mobile
phone. This might be for a supervisor, for example, so agents can call them if
needed.

###### Create a quick connect for a person's mobile phone number

1. On the navigation menu, choose **Routing**,
   **Quick connects**, **Add quick
   connect**.
2. On the **Add quick connect** page, enter a name for the
   quick connect, for example, **John Doe's cell
   phone**.
3. For **Type**, select **Phone
   number**.
4. For **Phone number**, enter the mobile phone number,
   starting with the country code. In the US, the country code is 1, as shown
   in the following image.

![The phone number on the Add quick connect page.](images/quick-connect-johndoe.png) 5. Choose **Save**.

###### Add the quick connect to a queue. Agents working this queue will see the

quick connect in their CCP.

1. Go to **Routing**, **Queues**, and
   choose the queue you want to edit.
2. On the **Edit queue** page, in **Outbound caller
   ID number**, choose a number claimed for your contact center.
   This is required to make outbound calls.
3. At the bottom of the page, in the **Quick connect** box,
   search for the quick connect you created, for example, **John Doe's
   cell phone**.
4. Select the quick connect. In the following image of the **Edit
   queue** page, a phone number has been selected for the
   **Outbound caller ID number**, and **John Doe's
   cell phone** has been selected as the quick connect.

![The Edit queue page, the quick connect for John Doe's cell phone number.](images/quick-connect-johndoe-queue.png) 5. Choose **Save**.

###### Test the quick connect

1. Open the Contact Control Panel.
2. Choose **Quick connects**.
3. Select the quick connect you created, and then choose
   **Call**.

![The quick connects page in the CCP, an entry for John Doe's cell phone.](images/quick-connect-johndoe-call.png)

## More examples

Configured Agent and Queue quick connects only appear in the CCP (Contact
Control Panel) when an agent is on an active call. External quick connects
appear in the CCP at all times.

### Agent quick connects

Let's say Agent A is on inbound call and during the conversation he would like
to transfer the call to another agent B.

1. Agent A initiates the agent quick connect by choosing
   `Transfer` on the CCP and selecting Agent B quick connect. As soon as agent A chooses
   Agent B quick connect, the CCP status of Agent A changes to
   "Connected."

Even though status of transferred call (internal transfer) shows
connected status the call is not connected to agent B. 2. The Agent transfer flow that is associated with agent quick connect gets
invoked.

The call is still not connected to Agent B. 3. Agent B gets notification in his/her CCP window to either accept or
reject the calls. 4. Agent B accepts the incoming call and the status in CCP changes to
"Connecting." 5. Agent whisper flow is played at agent A end who transferred the
call to agent B. 6. Customer whisper flow is played at agent B end.

Finally after 6th step, Agent A and B gets connected for conversation and the
status in CCP for agent B changes to "Connected."

### Queue quick connects

Let's say Agent A is on inbound call and during the conversation he would like
to transfer the call to another queue.

1. Agent A initiates the queue quick connect by choosing
   `Transfer` on the CCP and then selecting "XYZ" queue transfer. As soon as agent A clicks on
   queue quick connect, CCP status of Agent A changes to
   "Connected."

Even though status of transferred call (internal transfer) shows
connected the call is not transferred to queue. 2. The Queue transfer flow that is associated with queue quick connect gets
invoked. In this flow the Transfer to queue block is placed to
transfer the contact to required queue, in this case the "XYZ" queue. At the end
of step 2, the call is in the "XYZ" queue. Let's say Agent B is assigned to
work on contact in "XYZ" queue and agent B is in "Available"
status. 3. Agent B gets notification in the CCP to either accept or reject the
calls. 4. Agent B accepts the incoming call and the status in CCP changes to
"Connecting." 5. Agent whisper flow is played at agent A end who transferred the
call to "XYZ" queue. 6. Customer whisper flow is played at agent B end.

Finally after 6th step, Agent A and B gets connected for conversation and the
status in CCP for agent B changes to "Connected."

### External quick connects

No flows are involved in external quick connects. When agent A
uses external quick connect the call is directly connected the destination
parties (without invoking any flows).

Because no flow is involved in external quick connects you cannot set
the outbound caller id. Caller ID is used from the queue
configuration.

During invocation of Agent/Queue/External quick connects the caller of the
inbound call which Agent A was working on will hear the Customer hold
flow.
