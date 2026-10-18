

# How distribution settings work
<a name="distribution-settings-concepts"></a>

A distribution configuration contains a list of *distributions*. Each distribution applies to exactly one target Region and defines the outputs for that Region.

One distribution per Region  
A Region can appear in a distribution configuration at most once. To apply several outputs to the same Region – for example, an AMI copy and a VM export – combine them in a single distribution for that Region.

At least one output per Region  
Each distribution must define at least one output. The available outputs are AMI distribution, container distribution, AWS License Manager configurations, Amazon S3 VM export, launch template configurations, EC2 Fast Launch configurations, and SSM parameter configurations. If a distribution defines no outputs, the request fails.

Where distribution-phase encryption applies  
The AWS KMS key that you set in a distribution applies only to the AMI copies that Image Builder sends to *other accounts or Regions*. It does not encrypt the original AMI that the build creates in your account in the source Region. To encrypt the source-Region AMI, set the KMS key in the image recipe block device mapping (**Storage (volumes)** in the console) instead.

Changes don't affect images that you already distributed  
Image Builder saves a copy of the distribution settings with each image when it creates the image. When you update a distribution configuration, the changes apply only to images that Image Builder creates after the update. Earlier images keep their saved settings, including builds that are still in progress and retries that you start with **RetryImage**. To distribute with the updated settings, create a new image or run **DistributeImage**.  
Images that Image Builder already distributed remain in place until you remove them, either manually or with an Image Builder lifecycle policy. For example, if you remove a Region, the AMI that Image Builder already copied to that Region stays there.

Image Builder enforces the following default service quotas for each Region in a distribution configuration. For the current values, and whether each quota is adjustable, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html).


| Setting | Default quota per Region | 
| --- | --- | 
| Launch template configurations | 5 | 
| SSM parameter configurations | 10 | 
| Concurrent AMI copies (target accounts in targetAccountIds) | 50 | 