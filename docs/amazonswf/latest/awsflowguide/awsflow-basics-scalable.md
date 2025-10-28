# AWS Flow Framework Basic Concepts: Scalable Applications

Amazon SWF has two key features that make it easy to scale a workflow application to handle the
current load:

- A complete workflow execution history, which allows you to implement a stateless application.
- Task scheduling that is loosely coupled to task execution, which makes it easy to scale your application
  to meet current demands.
  Amazon SWF schedules tasks by posting them to dynamically allocated task lists, not by communicating directly with
  workflow and activity workers. Instead, the workers use HTTP requests to poll their respective lists for tasks. This
  approach loosely couples task scheduling to task execution and allows workers to run on any suitable system,
  including Amazon EC2 instances, corporate data centers, client computers, and so on. Because the HTTP requests originate
  with the workers, there is no need for externally visible ports, which enables workers to even run behind a firewall.

The long-polling mechanism that workers use to poll for tasks ensures that workers don't get overloaded. Even
if there is a spike in scheduled tasks, workers pull tasks at their own pace. However, because workers are stateless,
you can dynamically scale an application to meet increased load by starting additional worker instances. Even if
they are running on different systems, each instance polls the same task list and the first available worker instance
executes each task, regardless of where the worker is located or when it started. When the load declines, you can
reduce the number of workers accordingly.
