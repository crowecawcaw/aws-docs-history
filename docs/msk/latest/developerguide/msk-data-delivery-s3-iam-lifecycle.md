

# Channel lifecycle management permissions
<a name="msk-data-delivery-s3-iam-lifecycle"></a>

The following permissions are for the IAM principal (the user or role) you use to create, update, describe, delete, and list Channels. They are not part of the service execution role.


| API action | Required permission | Resource | 
| --- | --- | --- | 
| CreateChannel | `kafka:CreateChannel` | Cluster ARN | 
| DescribeChannel | `kafka:DescribeChannel` | Channel ARN | 
| UpdateChannel | `kafka:UpdateChannel` | Channel ARN | 
| DeleteChannel | `kafka:DeleteChannel` | Channel ARN | 
| ListChannels | `kafka:ListChannels` | Cluster ARN | 