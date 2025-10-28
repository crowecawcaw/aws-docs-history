# Configuring AWS calls to go through

your VPC

The special job parameter `disable-proxy-v2` allows you to route your
calls to services such as Amazon S3, CloudWatch, and AWS Glue through your VPC. By
default, AWS Glue uses a local proxy to send traffic through the AWS Glue VPC to download
scripts and libraries from Amazon S3, to send requests to CloudWatch for publishing logs and
metrics, and to send requests to AWS Glue for accessing data catalogs. This
proxy allows the job to function normally even if your VPC doesn't configure a proper
route to other AWS services, such as Amazon S3, CloudWatch, and AWS Glue. AWS Glue now
offers a parameter for you to turn off this behavior. For more information, see [Job parameters used
by AWS Glue](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md"). AWS Glue will continue to use local proxy for publishing CloudWatch logs
of your AWS Glue jobs.

###### Note

- This feature is supported for AWS Glue jobs with AWS Glue version 2.0 and
  above. When using this feature, you need to ensure that your VPC has
  configured a route to Amazon S3 through a NAT or service VPC endpoint.
- The deprecated job parameter `disable-proxy` only routes your
  calls to Amazon S3 for downloading scripts and libraries through your VPC. It’s
  recommended to use the new parameter `disable-proxy-v2` instead.

###### Example usage

Create an AWS Glue job with `disable-proxy-v2`:

```
aws glue create-job \
    --name no-proxy-job \
    --role GlueDefaultRole \
    --command "Name=glueetl,ScriptLocation=s3://my-bucket/glue-script.py" \
    --connections Connections="traffic-monitored-connection" \
    --default-arguments '{"--disable-proxy-v2" : "true"}'

```
