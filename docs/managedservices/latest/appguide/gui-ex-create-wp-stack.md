# Console Tutorial: Deploying a Tier and Tie WordPress Website

This section describes how to deploy a high availability (HA) WordPress site into an AMS environment using the AMS console.
This set of instructions includes an example of creating the necessary WordPress CodeDeploy-compatible package (e.g. zip) file. The provisioning
of the resources follows an order that allows you to tie them together to form "tiers."

###### Note

This deployment walkthrough is designed for use with an AMZN Linux OS.

The essential variable parameters are notated as `replaceable`; however, you may want to modify other parameters to suit your situation.

Summary of tasks and required RFCs:

1. Create the infrastructure:
   1. Create a MySQL RDS database cluster
   2. Create a load balancer
   3. Create an Auto scaling group and tie it to the load balancer
   4. Create an S3 bucket for CodeDeploy applications

2. Create a WordPress application bundle (does not require an RFC)
3. Deploy the WordPress application bundle with CodeDeploy:
   1. Create a CodeDeploy application
   2. Create a CodeDeploy deployment group
   3. Upload your WordPress application bundle to the S3 bucket (does not require an RFC)
   4. Deploy the CodeDeploy application

4. Validate the deployment
5. Tear down the deployment
   Descriptions for all CT options, including ChangeTypeId can be found in [AMS Change Type Reference](../ctref/index.md "../ctref/index.md").
