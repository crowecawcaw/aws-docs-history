# Understanding the Amazon SQS console

When you open the Amazon SQS console, choose **Queues** from the navigation
pane. The **Queues** page provides information about all of your queues in
the active region.

Each queue entry provides essential information about the queue, including its type and
key attributes. [Standard queues](standard-queues.md "standard-queues.md"), optimized for
maximum throughput and best-effort message ordering, are distinguished from [First-In-First-Out (FIFO)](sqs-fifo-queues.md "sqs-fifo-queues.md") queues, which prioritize
message ordering and uniqueness for applications requiring strict message sequencing.

![Queues page in the Amazon SQS console.](images/sqs-config-queue-list.png)
**Interactive elements and actions**

From the Queues page, you have multiple options for managing your queues:

1. **Quick Actions** – Adjacent to each queue
   name, a dropdown menu offers quick access to common actions such as sending
   messages, viewing or deleting messages, configuring triggers, and deleting the queue
   itself.
2. **Detailed View and Configuration** – Clicking
   on a queue name opens its Details page, where you can delve deeper into queue
   settings and configurations. Here, you can adjust parameters like message retention
   period, visibility timeout, and maximum message size to tailor the queue to your
   application's requirements.

![Queue details page in the Amazon SQS console.](images/queue-details-page.png)
**Region selection and resource tags**

Ensure you're in the correct AWS Region to access and manage your queues effectively.
Additionally, consider utilizing resource tags to organize and categorize your queues,
enabling better resource management, cost allocation, and access control within your AWS shared environment.

By leveraging the features and functionalities offered within the Amazon SQS console, you can
efficiently manage your messaging infrastructure, optimize queue performance, and ensure
reliable message delivery for your applications.
