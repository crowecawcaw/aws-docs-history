AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Additional considerations for Amazon EC2 instance

recommendations in AWS Migration Hub

Keep the following considerations in mind when generating Amazon EC2 instance
recommendations.

- Burstable instances (T2 and T3) have an additional pricing mechanism that is
  computed based on CPU credits. For the burstable instances, we use the provided
  `average` and `peak` CPU data points to compute an
  estimated number of consumed CPU credits. This is translated into an adjusted
  overall recommendation.
- Only current generation instances are recommended. The following types of
  instances are excluded from recommendations:
  - Previous generation instances (C3, for example)
  - Bare Metal instances
  - ARM instances (A1, for example)
  - 32-bit instances

- If the operating system for a server is not supported by Amazon EC2, that server's
  returned recommendation will be `Linux`. Additional information can
  be found in the `Recommendation.EC2.Remarks` column for each affected
  server.
