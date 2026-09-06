

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Mutable deployment, manually configured and updated application instances
<a name="ex-mute-manual"></a>

This application deployment strategy is a simple and manual update of application instances. These are the basic steps.

IDs for all CT options can be found in the [Change Type Reference](https://docs.aws.amazon.com/managedservices/latest/ctref/index.html).
**Note**  
Currently, you must use Amazon S3 storage with this solution.

The basic steps are outlined here; the various procedures are detailed in the [AMS User Guide](https://docs.aws.amazon.com/managedservices/latest/userguide/index.html).

1. Create an Amazon S3 storage bucket. CT: ct-1a68ck03fn98r. The S3 bucket must have versioning enabled (for information on doing this, see [Enabling Bucket Versioning](https://docs.aws.amazon.com/AmazonS3/latest/UG/enable-bucket-versioning.html)).

1. Put your bundled application artifacts on it (everything your application needs to start on boot and work). You can do this with the Amazon S3 console without requesting access through AMS. Or using a variation of this command:

   ```
   aws s3 cp {{ZIP_FILEPATH_AND_NAME}} s3://{{S3BUCKET_NAME}}/
   ```

1. Find an AMS AMI, all will have CodeDeploy on them. To find a "customer-" AMI use either:
   + AMS Console: The VPC details page for the relevant VPC
   + AMS API For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. or CLI: `aws amsskms list-amis`

1. Create an EC2 instance with that AMI. CT: ct-14027q0sjyt1h. Specify the AMS AMI, set a tag `Key=backup, Value=true` and specify the `customer-mc-ec2-instance-profile` for the `InstanceProfile` parameter. Note the instance ID that is returned.

1. Request admin access to the instance. CT: ct-1dmlg9g1l91h6. You'll need the FQDN for your account. If you’re unsure what your FQDN is, you can find it by:
   + Using the AWS Management Console for Directory Services (under Security and Identity) Directory Name tab.
   + Running one of these commands (return directory classes; DC\+DC\+DC=FQDN): Windows: `whoami /fqdn` or Linux: `hostname --fqdn`.

1. Log into the instance, see [Accessing Instances via Bastions](https://docs.aws.amazon.com/managedservices/latest/userguide/using-bastions.html) in the AMS User Guide.

1. Download your bundled application files from your S3 bucket to the instance.

1. Request an immediate backup with a service request to AMS, you will need to know the instance ID.

1. When you need to update your application, load new files to your S3 bucket and then follow steps 3 through 8.