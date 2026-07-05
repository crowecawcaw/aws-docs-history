End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Network architecture

AWS Managed Services (AMS) offers two network architectures:

- Multi-account landing zone (MALZ): provides common services - such as access, end point security, networking - from shared accounts for workloads that
  are deployed in separate member accounts.
- Single-account landing zone (SALZ): provides self contained accounts where common services such as access, end point security, networking are deployed
  in the same account as the workload. It is recommended for workloads that require a high level of isolation as it incurs higher AWS costs.
