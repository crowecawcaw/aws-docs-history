# Example of how to update a custom

bootstrap script for IMDSv2

In the following example, we update a custom bootstrap action script that was used with IMDSv1
for use with IMDSv2. The IMDSv1 script retrieves Amazon EC2 instance AMI ID metadata.

```
#!/bin/bash
AMI_ID=$(curl http://169.254.169.254/latest/meta-data/ami-id)
echo $AMI_ID >> /home/ami_id.txt
```

The following shows the custom bootstrap action script modified to be compatible with IMDSv2.

```
#!/bin/bash
AMI_ID=$(TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
         && curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/ami-id)
echo $AMI_ID >> /home/ami_id.txt
```

For more information, see [Retrieve instance metadata](../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md#instancedata-meta-data-retrieval-examples "../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md#instancedata-meta-data-retrieval-examples") in the _Amazon EC2 User Guide for Linux Instances_.
