NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Required permissions for the MGN Connector

In order to use MGN connector, you must have the required permissions in IAM.

For security best practices, it is recommended that the MGN connector will be accessed only by allowed personnel and will have the required OS patches. It is also recommended that the servers to which the MGN connector connects, will have all the required OS patches.

If you configure [outputting logs to S3](../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md#create-iam-instance-profile-ssn-logging "../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md#create-iam-instance-profile-ssn-logging"), first [create an Amazon S3 bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"). it is recommended to apply S3 bucket security practices - following AWS official reference to [S3 security practices](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md")

Refer to the [next section](CloudFormation_Template.md "CloudFormation_Template.md") to deploy permissions using a CloudFormation template.

Alternatively, in order to create the permissions manually, create the following IAM roles:
