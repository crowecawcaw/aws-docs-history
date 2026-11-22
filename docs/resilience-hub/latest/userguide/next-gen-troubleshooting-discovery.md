

# Troubleshooting dependency discovery

If dependency discovery is not returning expected results, review the following common issues:
+ **Discovery not returning expected dependencies for EC2 instances** – Verify the dependency uses DNS resolution (not a direct IP), confirm that the compute resources are in a VPC with a Route 53 resolver, and check that the dependency was called within the 35-day lookback window.
+ **Discovery not returning expected dependencies for ECS Fargate** – Verify that Service topology includes the VPC for the ECS Fargate Service.
+ **Discovery not returning expected dependencies for Lambda functions** – Verify that Service topology includes the function, and that the function ran after you enabled dependency discovery. For a function connected to a VPC, also verify that Service topology includes the VPC. Dependency discovery attributes the queries of some of these functions to their VPC, as described in [Coverage and known limitations](next-gen-discovery-limitations.md).
+ **Unexpected cross-region dependencies** – Cross-region dependencies are flagged automatically in the console. Common causes include hardcoded regional endpoints in application code, AWS SDK clients configured for a specific region, and third-party services routing to non-local endpoints.
+ **Dependencies appearing for the wrong service** – This typically occurs with shared VPCs or Amazon EKS clusters. Verify that compute resource attribution is correctly mapping resources to services.
+ **Fewer dependencies on a service that shares a VPC with Lambda functions** – In the Regions listed in [Coverage and known limitations](next-gen-discovery-limitations.md), dependency discovery attributes the queries of supported Lambda functions connected to a VPC to the function. Those queries appear only on services that include the function, not on other services that include the same VPC.

For additional troubleshooting guidance, see [Troubleshooting Next generation Resilience Hub](next-gen-troubleshooting.md).