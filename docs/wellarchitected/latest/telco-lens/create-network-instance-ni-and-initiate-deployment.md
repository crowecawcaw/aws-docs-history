# Create network instance (NI) and initiate deployment

CSPs create a new network instance (NI) using the previously ingested NSD and then
initiate the deployment process.

**Recommendation:** Implement a standardized approach for
creating NIs to verify consistency and repeatability across deployments. Leverage AWS TNB's
ability to create multiple NIs from a single NSD template to support use cases like private
network deployments.

**Practical advice:** Monitor the deployment progress and
status using the AWS TNB console or APIs. Implement automated triggering of the deployment
process as part of the CI/CD pipeline.
