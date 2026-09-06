

# Troubleshooting dependency discovery
<a name="next-gen-troubleshooting-discovery"></a>

If dependency discovery is not returning expected results, review the following common issues:
+ **Discovery not returning expected dependencies for EC2 instances** – Verify the dependency uses DNS resolution (not a direct IP), confirm that the compute resources are in a VPC with a Route 53 resolver, and check that the dependency was called within the 35-day lookback window.
+ **Discovery not returning expected dependencies for ECS Fargate** – Verify that Service topology includes the VPC for the ECS Fargate Service.
+ **Discovery not returning expected dependencies for Lambda functions** – Verify that the Lambda functions are VPC-connected, and that Service topology includes the VPC.
+ **Unexpected cross-region dependencies** – Cross-region dependencies are flagged automatically in the console. Common causes include hardcoded regional endpoints in application code, AWS SDK clients configured for a specific region, and third-party services routing to non-local endpoints.
+ **Dependencies appearing for the wrong service** – This typically occurs with shared VPCs or Amazon EKS clusters. Verify that compute resource attribution is correctly mapping resources to services.

For additional troubleshooting guidance, see [Troubleshooting Next generation Resilience Hub](next-gen-troubleshooting.md).