

# Security configurations and IAM roles
<a name="dotnet-migrating-applications-security"></a>

The **eb migrate** command manages AWS security configurations through IAM roles, instance profiles, and service roles. Understanding these components ensures proper access control and security compliance during migration.

## Instance profile configuration
<a name="dotnet-migrating-applications-security-instance"></a>

An instance profile serves as a container for an IAM role that Elastic Beanstalk attaches to EC2 instances in your environment. When executing **eb migrate**, you can specify a custom instance profile:

```
PS C:\migrations_workspace> eb migrate --instance-profile "CustomInstanceProfile"
```

If you don't specify an instance profile, **eb migrate** creates a default profile with these permissions:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::elasticbeanstalk-*",
                "arn:aws:s3:::elasticbeanstalk-*/*"
            ]
        }
    ]
}
```

------

## Service role management
<a name="dotnet-migrating-applications-security-service"></a>

A service role allows Elastic Beanstalk to manage AWS resources on your behalf. Specify a custom service role during migration with the following command:

```
PS C:\migrations_workspace> eb migrate --service-role "CustomServiceRole"
```

If not specified, **eb migrate** creates a default service role named `aws-elasticbeanstalk-service-role` with a trust policy that allows Elastic Beanstalk to assume the role. This service role is essential for Elastic Beanstalk to monitor your environment's health and perform managed platform updates. The service role requires two managed policies:
+ `AWSElasticBeanstalkEnhancedHealth` - Allows Elastic Beanstalk to monitor instance and environment health using the enhanced health reporting system
+ `AWSElasticBeanstalkManagedUpdates` - Allows Elastic Beanstalk to perform managed platform updates, including updating environment resources when a new platform version is available

With these policies, the service role has permissions to:
+ Create and manage Auto Scaling groups
+ Create and manage Application Load Balancers
+ Upload logs to Amazon CloudWatch
+ Manage EC2 instances

For more information about service roles, see [Elastic Beanstalk service role](concepts-roles-service.md) in the Elastic Beanstalk Developer Guide.

## Security group configuration
<a name="dotnet-migrating-applications-security-sg"></a>

The **eb migrate** command automatically configures security groups based on your IIS site bindings. For example, if your source environment has sites using ports 80, 443, and 8081 the following configuration results:

```
<site name="Default Web Site">
    <bindings>
        <binding protocol="http" bindingInformation="*:80:" />
        <binding protocol="https" bindingInformation="*:443:" />
    </bindings>
</site>
<site name="InternalAPI">
    <bindings>
        <binding protocol="http" bindingInformation="*:8081:" />
    </bindings>
</site>
```

The migration process completes the following actions:
+ Creates a load balancer security group allowing inbound traffic on ports 80 and 443 from the internet (0.0.0.0/0)
+ Creates an EC2 security group allowing traffic from the load balancer
+ Configures additional ports (like 8081) if `--copy-firewall-config` is specified

By default, the Application Load Balancer is configured with public access from the internet. If you need to customize this behavior, such as restricting access to specific IP ranges or using a private load balancer, you can override the default VPC and security group configuration using the `--vpc-config` parameter:

```
PS C:\migrations_workspace> eb migrate --vpc-config vpc-config.json
```

For example, the following `vpc-config.json` configuration creates a private load balancer in a private subnet:

```
{
    "id": "vpc-12345678",
    "publicip": "false",
    "elbscheme": "internal",
    "ec2subnets": ["subnet-private1", "subnet-private2"],
    "elbsubnets": ["subnet-private1", "subnet-private2"]
}
```

For more information about VPC configuration options, see [VPC configuration](dotnet-migrating-applications-network.md#dotnet-migrating-applications-network-vpc).

## SSL certificate integration
<a name="dotnet-migrating-applications-security-ssl"></a>

When migrating sites with HTTPS bindings, integrate SSL certificates through AWS Certificate Manager (ACM):

```
PS C:\migrations_workspace> eb migrate --ssl-certificates "arn:aws:acm:region:account:certificate/certificate-id"
```

This configuration completes the following actions:
+ Associates the certificate with the Application Load Balancer
+ Maintains HTTPS termination at the load balancer
+ Preserves internal HTTP communication between the load balancer and EC2 instances

## Windows authentication
<a name="dotnet-migrating-applications-security-windows"></a>

For applications using Windows Authentication, **eb migrate** preserves the authentication settings in the application's `web.config` as follows:

```
<configuration>
    <system.webServer>
        <security>
            <authentication>
                <windowsAuthentication enabled="true">
                    <providers>
                        <add value="Negotiate" />
                        <add value="NTLM" />
                    </providers>
                </windowsAuthentication>
            </authentication>
        </security>
    </system.webServer>
</configuration>
```

**Important**  
The **eb migrate** command does not copy over user profiles or accounts from your source environment to the target Elastic Beanstalk instances. Any custom user accounts or groups that you've created on your source server will need to be recreated on the target environment after migration.

Built-in Windows accounts like `IUSR` and groups like `IIS_IUSRS`, as well as all other built-in accounts and groups, are included by default on the target Windows Server instances. For more information about built-in IIS accounts and groups, see [Understanding Built-In User and Group Accounts in IIS](https://learn.microsoft.com/en-us/iis/get-started/planning-for-security/understanding-built-in-user-and-group-accounts-in-iis) in the Microsoft documentation.

If your application relies on custom Windows user accounts or Active Directory integration, you will need to configure these aspects separately after the migration is complete.

## Best practices and troubleshooting
<a name="dotnet-migrating-applications-security-best"></a>

### Role management
<a name="dotnet-migrating-applications-security-best-role"></a>

Implement AWS IAM best practices when managing roles for your Elastic Beanstalk environments:

Role creation and management  
+ Create roles using AWS managed policies where possible
+ Follow the [IAM Security Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+ Use the [AWS Policy Generator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) for custom policies
+ Implement [permission boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) for additional security

Monitoring and auditing  
Enable AWS CloudTrail to monitor role usage:  
+ Follow the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ Configure CloudWatch Logs integration for real-time monitoring
+ Set up alerts for unauthorized API calls

Regular review process  
Establish a quarterly review cycle to do the following tasks:  
+ Audit unused permissions using [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
+ Remove outdated permissions
+ Update roles based on least-privilege principles

### Certificate management
<a name="dotnet-migrating-applications-security-best-cert"></a>

Implement these practices for SSL/TLS certificates in your Elastic Beanstalk environments:

Certificate lifecycle  
+ Use [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) for certificate management
+ Enable [automatic renewal](https://docs.aws.amazon.com/acm/latest/userguide/check-certificate-renewal-status.html) for ACM-issued certificates
+ Set up [expiration notifications](https://docs.aws.amazon.com/acm/latest/userguide/notifications-for-ACM.html)

Security standards  
+ Use TLS 1.2 or later
+ Follow [AWS security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies) for HTTPS listeners
+ Implement HTTP Strict Transport Security (HSTS) if required

### Security group management
<a name="dotnet-migrating-applications-security-best-sg"></a>

Implement these security group best practices:

Rule management  
+ Document all custom port requirements
+ Use [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) to monitor traffic
+ Use [Security Group reference rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) instead of IP ranges where possible

Regular auditing  
Establish monthly reviews to do the following tasks:  
+ Identify and remove unused rules
+ Validate source/destination requirements
+ Check for overlapping rules

### Logging and monitoring
<a name="dotnet-migrating-applications-security-best-logging"></a>

For effective security monitoring, configure the following logs:

Windows event logs on EC2 instances  

```
# Review Security event log
PS C:\migrations_workspace> Get-EventLog -LogName Security -Newest 50

# Check Application event log
PS C:\migrations_workspace> Get-EventLog -LogName Application -Source "IIS*"
```

CloudWatch Logs integration  
Configure CloudWatch Logs agent to stream Windows event logs to CloudWatch for centralized monitoring and alerting.

For persistent issues, gather these logs and contact AWS Support with the following information:
+ Environment ID
+ Deployment ID (if applicable)
+ Relevant error messages
+ Timeline of security changes