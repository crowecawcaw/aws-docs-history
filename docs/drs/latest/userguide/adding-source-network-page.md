# Adding source networks to Elastic Disaster Recovery

Available source networks are presented automatically on the **Source
networks** page, along with their details: replication status, pending action,
CloudFormation stack name, and more.

When adding a source server to AWS Elastic Disaster Recovery, and after an agent is installed, the VPC network will be automatically identified and created.

To replicate and recover your network configurations, take the following steps:

1. Install the AWS Replication agent on your source servers. Alternatively, source
   networks can be added manually by calling the CreateSourceNetwork API.
2. Create the required role.
3. Select the relevant network.
4. Start replication.
5. Select an S3 bucket.

###### Important

You only need to configure your S3 bucket once. Configurations will apply to all existing and
newly added source networks. 6. Test or recover your network configurations by initiating a recovery job. This will
include creating or updating your CloudFormation stack.
