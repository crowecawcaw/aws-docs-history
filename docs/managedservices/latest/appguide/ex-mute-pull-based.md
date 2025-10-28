# Mutable deployment with a pull-based deployment tool-configured AMI

This strategy relies on the `InstanceUserData` parameter in the Managed Services Create EC2 CT. For more information on using this parameter,
see [Configuring Instances with User Data](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md#instancedata-add-user-data "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md#instancedata-add-user-data").
This example assumes a pull-based application deployment tool like Chef or Puppet.

The CodeDeploy agent is supported on all AMS AMIs. Here is the list of supported AMIs:

- Amazon Linux (version 1)
- Amazon Linux 2
- RedHat 7
- CentOS 7
  IDs for all CT options can be found in the [Change Types Reference](../ctref/index.md "../ctref/index.md").

###### Note

Currently, you must use Amazon S3 storage with this solution.

The basic steps are outlined here and the procedure is detailed in the AMS User Guide.

1. Create an Amazon S3 storage bucket. CT: ct-1a68ck03fn98r. The S3 bucket must have versioning enabled (for information on doing this, see
   [Enabling Bucket Versioning](../../../AmazonS3/latest/UG/enable-bucket-versioning.md "../../../AmazonS3/latest/UG/enable-bucket-versioning.md")).
2. Put your bundled CodeDeploy artifacts on it. You can do this with the Amazon S3 console without requesting access through AMS. Or using a variation of this command:

```
aws s3 cp `ZIP_FILEPATH_AND_NAME` s3://`S3BUCKET_NAME`/
```

3. Find an AMS `customer-` AMI; use either:
   - AMS Console: The VPC details page for the relevant VPC
   - AMS API For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. or CLI: `aws amsskms list-amis`

4. Create an EC2 instance. CT: ct-14027q0sjyt1h; set a tag `Key=backup, Value=true`, and use the `InstanceUserData` parameter
   to specify a bootstrap and other scripts (download Chef/Puppet agent, etc.), and include the necessary authorization keys. You can find an example of doing
   this in the AMS User Guide, Change Mangement section examples of creating an HA Two Tier Deployment. Alternatively, request access to, and log into,
   the instance and configure it with the necessary deployment artifacts. Remember that pull-based deployment commands go from the agents on your instances
   to your corporate master server and may need authorization to go through bastions. You may need a service request to AMS to request
   security group/AD group access without bastions.
5. Repeat step 4 to create another EC2 instance and configure it with the deployment tool master server.
6. When you need to update your application, use the deployment tool to rollout the updates to your instances.
