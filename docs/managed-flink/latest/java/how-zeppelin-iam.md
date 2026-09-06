

# Review IAM permissions for Studio notebooks
<a name="how-zeppelin-iam"></a>

Managed Service for Apache Flink creates an IAM role for you when you create a Studio notebook through the AWS Management Console. It also associates with that role a policy that allows the following access:



| Service | Access  | 
| --- | --- | 
| CloudWatch Logs | List | 
| Amazon EC2 | List | 
| AWS Glue | Read, Write | 
| Managed Service for Apache Flink | Read | 
| Managed Service for Apache Flink V2 | Read | 
| Amazon S3 | Read, Write | 