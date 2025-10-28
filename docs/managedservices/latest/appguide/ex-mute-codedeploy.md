# Mutable deployment with a CodeDeploy-enabled AMI

[AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/") is a service that automates code deployments to any instance, including Amazon EC2
instances and instances running on-premises.
You can use CodeDeploy with AMS to create and deploy a CodeDeploy application. Note that AMS provides a default instance profile for CodeDeploy applications.

- Amazon Linux (version 1)
- Amazon Linux 2
- RedHat 7
- CentOS 7
  Before you use CodeDeploy for the first time, you must complete a number of setup steps:

1. [Install or upgrade the AWS CLI](../../../codedeploy/latest/userguide/getting-started-setup-cli-config.md "../../../codedeploy/latest/userguide/getting-started-setup-cli-config.md")
2. [Create a Service Role for AWS CodeDeploy](../../../codedeploy/latest/userguide/how-to-create-service-role.md "../../../codedeploy/latest/userguide/how-to-create-service-role.md"),
   you use the Service Role ARN in the deployment
   IDs for all CT options can be found in the [Change Type Reference](../ctref/index.md "../ctref/index.md").

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

4. Create an Autoscaling group (ASG). CT: ct-2tylseo8rxfsc. Specify the AMS AMI, set the load balancer to have open ports,
   specify `customer-mc-ec2-instance-profile` for the `ASGIAMInstanceProfile`.
5. Create your CodeDeploy application. CT: ct-0ah3gwb9seqk2. Parameters include an application name; for example `WordpressProd`.
6. Create your CodeDeploy deployment group. CT: ct-2gd0u847qd9d2. Parameters include your CodeDeploy application name, ASG name,
   the configuration type name, and the service role ARN.
7. Deploy the CodeDeploy application. CT: ct-2edc3sd1sqmrb. Parameters include your CodeDeploy application name, configuration type name,
   deployment group name, revision type, and the S3 bucket location where the CodeDeploy artifacts are.
