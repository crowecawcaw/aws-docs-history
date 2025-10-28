# Sample queued callback flow in Amazon Connect

###### Note

This sample flow is available in previous Amazon Connect instances. In new instances, you
can see examples of queued callback in [Sample interruptible queue flow with
callback in Amazon Connect](sample-interruptible-queue.md "sample-interruptible-queue.md") and [Sample queue configurations flow in
Amazon Connect](sample-queue-configurations.md "sample-queue-configurations.md").

Type: Flow (inbound)

This flow provides callback queue logic. Here's how it works:

1. After a voice prompt, a working queue is selected and its queue status is
   checked.
2. A voice prompt tells the customer if the wait time for the selected queue is
   longer than 5 minutes. Customers are offered a choice to wait in the queue or to
   be placed into a callback queue.
3. If the customer decides to wait in the queue, the **Set customer queue
   flow** block places them in a queue flow that provides a callback
   option. That is, it places them in **Sample interruptible queue flow
   with callback**.
4. If the customer chooses to be placed into a callback queue, their number is
   stored in the **Store customer input** block. Then their
   callback number is set, and they are transferred to the callback queue.
   For information about queued callbacks, see the following topics:

- [Set up queued callback by creating flows, queues, and
  routing profiles in Amazon Connect](setup-queued-cb.md "setup-queued-cb.md")
- [Flow block in Amazon Connect: Transfer to queue](transfer-to-queue.md "transfer-to-queue.md")
- [Queued callbacks in real-time metrics in
  Amazon Connect](about-queued-callbacks.md "about-queued-callbacks.md")
