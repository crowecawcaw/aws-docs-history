# CLI Tutorial: High Availability Two-Tier Stack (Linux/RHEL)

This section describes how to deploy a high availability (HA) two-tier stack into an AMS environment using the AMS CLI.

###### Note

This deployment walkthrough has been tested in AMZN Linux and RHEL environments.

Summary of tasks and required RFCs:

1. Create infrastructure (HA two-tier stack)
2. Create an S3 bucket for CodeDeploy applications
3. Create the WordPress application bundle and upload it to the S3 bucket
4. Deploy the application with CodeDeploy
5. Access the WordPress site and log in to validate the deployment
