# Blocking workers

When you identify workers that are not putting in the requested effort on your tasks
on Amazon Mechanical Turk (Mechanical Turk), you have the option to block them. This prevents them from doing any
future work for you so long as the block is in place. Workers are notified that they've
been blocked from your tasks.

The [`CreateWorkerBlock`](../AWSMturkAPI/ApiReference_CreateWorkerBlockOperation.md "../AWSMturkAPI/ApiReference_CreateWorkerBlockOperation.md") operation can be used to block a worker
by simply providing the ID of the worker and a reason for the block. Similarly, you can
remove a block by using the [`DeleteWorkerBlock`](../AWSMturkAPI/ApiReference_DeleteWorkerBlockOperation.md "../AWSMturkAPI/ApiReference_DeleteWorkerBlockOperation.md") operation. At any point you can retrieve
all of the workers that have been blocked by using the [`ListWorkerBlocks`](../AWSMturkAPI/ApiReference_ListWorkerBlocksOperation.md "../AWSMturkAPI/ApiReference_ListWorkerBlocksOperation.md") operation.

Note that we recommend you be judicious in your use of worker blocks and only block
those workers that are clearly not making an attempt to correctly respond to your task
(spamming). If a worker is simply misreading instructions or lacks the requisite skills
to complete your task successfully, we advise you to use a custom qualification
requirement to exclude them from future tasks, rather than a block. Because the blocks a
worker receives are a component of Mechanical Turk worker review policies and frequent blocks may
result in account suspension, workers are sensitive to being blocked by requesters. If
the worker community believes that you are blocking workers unfairly, they may choose to
avoid accepting your tasks in the future.
