# Other considerations

- If you need to use IAM authentication between the primary and backup
  clusters, you can also set it up when you invokde the CloudFormation template.
- If encryption at rest is enabled on your primary cluster, consider how to
  manage the associated KMS keys when copying the snapshot across to the target region
  and associate a new KMS key in the target region.
- A best practice is to use DNS CNAMEs in front of the Neptune endpoints
  used in your applications. Then, if you need to manually failover to the target backup
  cluster, these CNAMEs can be changed to point to the target cluster and/or instance
  endpoints.
