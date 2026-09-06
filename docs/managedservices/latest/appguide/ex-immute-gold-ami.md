

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Immutable deployment with a golden AMI
<a name="ex-immute-gold-ami"></a>

This strategy employs a "golden" AMI that you have configured to behave as you want all of your application instances to. For example, the instances created with this golden AMI would self-join the correct domain and DNS, self-configure, reboot and launch all necessary systems. When you want to update your application instances, you re-create the golden AMI and rollout all-new application instances with it.

The CodeDeploy agent is supported on all AMS AMIs. Here is the list of supported AMIs:
+ Amazon Linux (version 1)
+ Amazon Linux 2
+ RedHat 7
+ CentOS 7

IDs for all CT options can be found in the [Change Type Reference](https://docs.aws.amazon.com/managedservices/latest/ctref/index.html).
**Note**  
Currently, you must use Amazon S3 storage with this solution.

1. Create an Amazon S3 storage bucket. CT: ct-1a68ck03fn98r. The S3 bucket must have versioning enabled (for information on doing this, see [Enabling Bucket Versioning](https://docs.aws.amazon.com/AmazonS3/latest/UG/enable-bucket-versioning.html)).

1. Put your bundled application artifacts on it (everything your application needs to start on boot and work). You can do this with the Amazon S3 console without requesting access through AMS. Or using a variation of this command:

   ```
   aws s3 cp {{ZIP_FILEPATH_AND_NAME}} s3://{{S3BUCKET_NAME}}/
   ```

1. Find an AMS `customer-` AMI; use either:
   + AMS Console: The VPC details page for the relevant VPC
   + AMS API For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. or CLI: `aws amsskms list-amis`

1. Create an EC2 instance with that AMI. CT: ct-14027q0sjyt1h. Specify the AMS AMI, set a tag `Key=backup, Value=true` and specify `customer-mc-ec2-instance-profile` for the `InstanceProfile`. Note the instance ID that is returned.

1. Request admin access to the instance. CT: ct-1dmlg9g1l91h6. You'll need the FQDN for your account. If you’re unsure what your FQDN is, you can find it by:
   + Using the AWS Management Console for Directory Services (under Security and Identity) Directory Name tab.
   + Running one of these commands (return directory classes; DC\+DC\+DC=FQDN): Windows: `whoami /fqdn` or Linux: `hostname --fqdn`.

1. Log into the instance, see [Accessing Instances](https://docs.aws.amazon.com/managedservices/latest/userguide/using-bastions.html) in the AMS User Guide.

1. Download to the instance your bundled application files from your S3 bucket. Configure the instance so that it self-deploys the fully-functioning application on boot.

1. Create the golden AMI on the instance. CT: ct-3rqqu43krekby. For details, see [AMI \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-ami-create.html). 

1. Configure an Auto Scaling group to create new instances using that AMI. CT: ct-2tylseo8rxfsc. When you need to update your application, follow this procedure and request AMS to update the ASG to use the new golden AMI; use a Management \| Other \| Other \| Update CT for this. 