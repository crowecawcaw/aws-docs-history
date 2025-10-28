# Design principles

The Well-Architected Framework identifies a set of general design
principles to facilitate good design in the cloud for serverless
applications:

- **Speedy, simple, singular**: Functions are concise, short,
  single-purpose, and their environment may live up to their request lifecycle. Transactions
  are efficiently cost-aware, and thus faster initiations are preferred.
- **Think concurrent requests, not total
  requests**: Serverless applications take advantage of
  the concurrency model, and tradeoffs at the design level are
  evaluated based on concurrency.
- **Share nothing**: Function
  runtime environment and underlying infrastructure are
  short-lived, therefore local resources such as temporary storage
  is not guaranteed. State can be manipulated within a state
  machine execution lifecycle, and persistent storage is preferred
  for highly durable requirements.
- **Assume no hardware affinity**: Underlying infrastructure may
  change. Use code or dependencies that are hardware-agnostic. CPU flags, for example, may not
  be available consistently.
- **Orchestrate your application with state
  machines, not functions**: Chaining Lambda executions
  within the code to orchestrate the workflow of your application
  results in a monolithic and tightly coupled application.
  Instead, use a state machine to orchestrate transactions and
  communication flows.
- **Use events to trigger transactions**: Events such as writing
  a new Amazon S3 object or an update to a database allow for transaction execution in response to
  business functionalities. This asynchronous event behavior is often consumer agnostic and
  drives just-in-time processing to achieve lean service design.
- **Design for failures and duplicates**: Operations triggered
  from requests or events must be idempotent, as failures can occur and a given request or
  event can be delivered more than once. Include appropriate retries for downstream calls.
