# Terminate an Elastic Beanstalk environment

You can terminate a running AWS Elastic Beanstalk environment using the Elastic Beanstalk console. By doing this, you avoid incurring charges for unused AWS resources.

###### Note

You can always launch a new environment using the same version later.

If you have data from an environment that you want to preserve, set the database deletion policy to `Retain` before terminating the
environment. This keeps the database operational outside of Elastic Beanstalk. After this, any Elastic Beanstalk environments must connect to it as an external database. If you
want to back up the data without keeping the database operational, set the deletion policy to take a snapshot of the database before terminating the
environment. For more information, see [Database lifecycle](using-features.managing.db.md#environments-cfg-rds-lifecycle "using-features.managing.db.md#environments-cfg-rds-lifecycle") in the
_Configuring environments_ chapter of this guide.

Elastic Beanstalk might fail to terminate your environment. One common reason is that the security group of another environment has a dependency on the security
group of the environment that you want to terminate. For instructions on how to avoid this problem, see [EC2 security groups](using-features.managing.ec2.console.md#using-features.managing.ec2.securitygroups "using-features.managing.ec2.console.md#using-features.managing.ec2.securitygroups") on the _EC2
Instances_ page of this guide.

###### Important

If you terminate an environment, you must also delete any CNAME mappings that you created, as other customers can reuse an available hostname. Be sure to
delete DNS records that point to your terminated environment to prevent a _dangling DNS entry_. A dangling DNS entry can expose internet
traffic destined for your domain to security vulnerabilities. It can also present other risks.

For more information, see [Protection from dangling
delegation records in Route 53](../../../Route53/latest/DeveloperGuide/protection-from-dangling-dns.md "../../../Route53/latest/DeveloperGuide/protection-from-dangling-dns.md") in the _Amazon Route 53 Developer Guide_. You can also learn more about dangling DNS entries in [Enhanced Domain Protections for Amazon CloudFront Requests](https://aws.amazon.com/blogs/security/enhanced-domain-protections-for-amazon-cloudfront-requests/ "https://aws.amazon.com/blogs/security/enhanced-domain-protections-for-amazon-cloudfront-requests/") in the _AWS Security Blog_.

## Elastic Beanstalk console

###### To terminate an environment

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. Choose **Actions**, and then choose **Terminate environment**.
4. Use the on-screen dialog box to confirm environment termination.

###### Note

When you terminate your environment, the CNAME that's associated with the terminated environment is freed up to be used by anyone.

It takes a few minutes for Elastic Beanstalk to terminate the AWS resources that are running in the environment.

## AWS CLI

###### To terminate an environment

- Run the following command.

```
$ `aws elasticbeanstalk terminate-environment --environment-name `my-env``
```

## API

###### To terminate an environment

- Call `TerminateEnvironment` with the following parameter:

`EnvironmentName` = `SampleAppEnv`

```
https://elasticbeanstalk.us-west-2.amazon.com/?EnvironmentName=SampleAppEnv
&Operation=TerminateEnvironment
&AuthParams
```
