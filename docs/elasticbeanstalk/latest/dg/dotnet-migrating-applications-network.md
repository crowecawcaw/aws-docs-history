# Network configuration and port settings

This section covers network configuration options for IIS migrations, including VPC settings, port configurations, and multi-site deployments.

## VPC configuration

The **eb migrate** command provides flexible VPC configuration options for
your Elastic Beanstalk environment. The tool can either detect VPC settings from a source EC2 instance or
accept custom VPC configurations through command-line parameters. Review [Using Elastic Beanstalk with Amazon VPC](vpc.md "vpc.md") to understand how to configure Elastic Beanstalk with VPC.

### Automatic VPC detection

When **eb migrate** runs on an EC2 instance, it automatically discovers
and uses the VPC configuration from the source environment's EC2 instances. The following
example output illustrates the configuration information that it detects:

```
PS C:\migrations_workspace > `eb migrate`
Identifying VPC configuration of this EC2 instance (i-0123456789abcdef0):
  id: vpc-1234567890abcdef0
  publicip: true
  elbscheme: public
  ec2subnets: subnet-123,subnet-456,subnet-789
  securitygroups: sg-123,sg-456
  elbsubnets: subnet-123,subnet-456,subnet-789
...
```

The detected configuration includes:

- VPC identifier
- Public IP assignment settings
- Load balancer scheme (public/private)
- EC2 instance subnet assignments
- Security group associations
- Load balancer subnet assignments

### On-premises or non-AWS

cloud hosts

When **eb migrate** runs from an on-premises server or a non-AWS cloud
host, the Elastic Beanstalk service will use the default VPC in your AWS account. The
following listing shows an example command and output:

```
PS C:\migrations_worspace> `eb migrate `
 -k windows-test-pem `
 --region us-east-1 `
 -a EBMigratedEnv `
 -e EBMigratedEnv-test2 `
 --copy-firewall-config`
Determining EB platform based on host machine properties
Using .\migrations\latest to contain artifacts for this migration run.
...
```

Review [Using Elastic Beanstalk with Amazon VPC](vpc.md "vpc.md") to understand how Elastic Beanstalk
configures the default VPC for your environment.

### Custom VPC configuration

For any source environment (EC2, on-premises, or non-AWS cloud) where you need
specific VPC settings, provide a VPC configuration file like the one in the following
example:

```
{
    "id": "vpc-12345678",
    "publicip": "true",
    "elbscheme": "public",
    "ec2subnets": ["subnet-a1b2c3d4", "subnet-e5f6g7h8"],
    "securitygroups": "sg-123456,sg-789012",
    "elbsubnets": ["subnet-a1b2c3d4", "subnet-e5f6g7h8"]
}
```

Apply this configuration using the following command:

```
`PS C:\migrations_workspace>` `eb migrate --vpc-config vpc-config.json`
```

###### Note

The VPC configuration file requires the `id` field that specifies the VPC
ID. All other fields are optional, and Elastic Beanstalk will use default values for any fields that
you don't specify.

###### Important

_The migration will ignore any existing VPC settings from the source environment when
you specify the_ `--vpc-config`
_parameter_. When you use this parameter, the migration will only use the VPC
settings specified in the configuration file that you're passing in. Using this parameter
overrides the default behavior of discovering the source instance's VPC configuration or using the
default VPC.

Use the `--vpc-config` parameter in these scenarios:

- When you migrate non-EC2 environments that don't have discoverable VPC
  settings
- When you migrate to a different VPC from the one used by the source
  environment
- When you need to customize subnet selections or security group configurations
- When the automatic discovery doesn't correctly identify the desired VPC settings
- When you migrate from on-premises, and you don't want to use the default VPC

### Network security configuration

By default, **eb migrate** opens port 80 on target instances but does not
copy other Windows Firewall rules from the source machine. To include all firewall
configurations use the following command:

```
`PS C:\migrations_workspace>` `eb migrate --copy-firewall-config`
```

This command does the following actions:

- Identifies ports used by IIS site bindings
- Retrieves corresponding firewall rules
- Generates PowerShell scripts to recreate rules on target instances
- Preserves any DENY rules for port 80 from the source machine (otherwise port 80 is allowed by default)

Consider a use case, where your source machine has the firewall rules specified in the
following example:

```
# Source machine firewall configuration
Get-NetFirewallRule | Where-Object {$_.Enabled -eq 'True'} | Get-NetFirewallPortFilter | Where-Object {$_.LocalPort -eq 80 -or $_.LocalPort -eq 443 -or $_.LocalPort -eq 8081}
# Output shows rules for ports 80, 443, and 8081
```

The migration creates a script (`modify_firewall_config.ps1`) that
contains the following configuration:

```
New-NetFirewallRule -DisplayName "Allow Web Traffic" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 80,443
New-NetFirewallRule -DisplayName "Allow API Traffic" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8081
```

The migration tool automatically does the following actions:

- Extracts HTTP/HTTPS ports from all IIS site bindings
- Uses the Windows Firewall [INetFwPolicy2](https://learn.microsoft.com/en-us/windows/win32/api/netfw/nn-netfw-inetfwpolicy2 "https://learn.microsoft.com/en-us/windows/win32/api/netfw/nn-netfw-inetfwpolicy2") interface to enumerate firewall rules
- Filters rules to only include those that explicitly reference the specified ports
- Only processes HTTP and HTTPS site bindings and their associated firewall rules
- Preserves rule properties including display name, action, protocol, and enabled state
- Handles both individual ports and port ranges in firewall rules
- Adds the firewall configuration script to the deployment manifest

### Load balancer configuration

You can specify Load Balancer configuration through the `--vpc-config`
argument. The examples that follow demonstrate the parameters.

Scheme selection

Choose between public and private load balancer schemes:

```
{
    "id": "vpc-12345678",
    "elbscheme": "private",
    "elbsubnets": ["subnet-private1", "subnet-private2"]
}
```

Subnet distribution

For high availability, distribute load balancer subnets across Availability Zones:

```
{
    "elbsubnets": [
        "subnet-az1", // Availability Zone 1
        "subnet-az2", // Availability Zone 2
        "subnet-az3"  // Availability Zone 3
    ]
}
```

###### Note

While Elastic Beanstalk supports environment creation with Application Load Balancers, Network Load Balancers, and Classic Load Balancers, the **eb migrate** command only supports Application Load Balancers. For more information about load balancer types, see [Load balancer for your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md").

## Multi-site deployments with port configurations

The **eb migrate** command handles complex multi-site IIS deployments where
applications might share dependencies or use non-standard ports. Consider the following
example of a typical enterprise setup with multiple sites:

```
<!-- IIS Configuration -->
<sites>
    <site name="Default Web Site" id="1">
        <bindings>
            <binding protocol="http" bindingInformation="*:80:www.example.com" />
        </bindings>
    </site>
    <site name="InternalAPI" id="2">
        <bindings>
            <binding protocol="http" bindingInformation="*:8081:api.internal" />
        </bindings>
    </site>
    <site name="ReportingPortal" id="3">
        <bindings>
            <binding protocol="http" bindingInformation="*:8082:reports.internal" />
        </bindings>
    </site>
</sites>
```

To migrate this configuration, use the following example command and parameters:

```
`PS C:\migrations_workspace>` `eb migrate `
 --sites "Default Web Site,InternalAPI,ReportingPortal" `
 --copy-firewall-config `
 --instance-type "c5.large"`
```

The **eb migrate** command creates a deployment package that preserves each
site's identity and configuration. The command generates an
`aws-windows-deployment-manifest.json` that defines how these sites
should be deployed. The following example demonstrates a generated json file:

```
{
    "manifestVersion": 1,
    "deployments": {
        "msDeploy": [
            {
                "name": "DefaultWebSite",
                "parameters": {
                    "appBundle": "DefaultWebSite.zip",
                    "iisPath": "/",
                    "iisWebSite": "Default Web Site"
                }
            }
        ],
        "custom": [
            {
                "name": "InternalAPI",
                "scripts": {
                    "install": {
                        "file": "ebmigrateScripts\\install_site_InternalAPI.ps1"
                    },
                    "restart": {
                        "file": "ebmigrateScripts\\restart_site_InternalAPI.ps1"
                    },
                    "uninstall": {
                        "file": "ebmigrateScripts\\uninstall_site_InternalAPI.ps1"
                    }
                }
            },
            {
                "name": "ReportingPortal",
                "scripts": {
                    "install": {
                        "file": "ebmigrateScripts\\install_site_ReportingPortal.ps1"
                    },
                    "restart": {
                        "file": "ebmigrateScripts\\restart_site_ReportingPortal.ps1"
                    },
                    "uninstall": {
                        "file": "ebmigrateScripts\\uninstall_site_ReportingPortal.ps1"
                    }
                }
            }
        ]
    }
}
```

The migration process creates the following Application Load Balancer listener rules that maintain your
original routing logic:

- Port 80 traffic routes to Default Web Site
- Port 8081 traffic routes to InternalAPI
- Port 8082 traffic routes to ReportingPortal

## Shared configuration and dependencies

When sites share configurations or dependencies, **eb migrate** handles
these relationships appropriately. Reference the following example where
multiple sites share a common configuration:

```
<!-- Shared configuration in applicationHost.config -->
<location path="Default Web Site">
    <system.webServer>
        <asp enableSessionState="true" />
        <caching enabled="true" enableKernelCache="true" />
    </system.webServer>
</location>
```

The migration process completes the following tasks:

1. Identifies shared configurations across sites
2. Generates appropriate PowerShell scripts to apply these settings
3. Maintains configuration hierarchy and inheritance

## Best practices

We recommend that you follow best practices for the network configuration of your migrated
application. The following groupings provide summary guidelines.

VPC design

- Follow AWS VPC Design Best Practices
- Use separate subnets for load balancers and EC2 instances
- Implement proper route tables and NACLs
- Consider VPC endpoints for AWS services

High availability

- Deploy across multiple Availability Zones
- Use at least two subnets for load balancers
- Configure auto-scaling across AZs
- Implement proper health checks

Security

- Follow Security Best Practices
- Use security groups as primary access control
- Implement network Access Control Lists (ACLs) for additional security
- Monitor VPC Flow Logs

## Troubleshooting

Common network configuration issues include the following areas. Following each subject
are example commands to obtain more information about the network configuration and health of
your environment.

Subnet configuration

```
`# Verify subnet availability`
`PS C:\migrations_workspace>` `aws ec2 describe-subnets --subnet-ids subnet-id`

`# Check available IP addresses`
`PS C:\migrations_workspace>``aws ec2 describe-subnets --subnet-ids subnet-id --query 'Subnets[].AvailableIpAddressCount'`
```

Security group access

```
`# Verify security group rules`
`PS C:\migrations_workspace>` `aws ec2 describe-security-groups --group-ids sg-id`

`# Test network connectivity`
`PS C:\migrations_workspace>` `aws ec2 describe-network-interfaces --filters Name=group-id,Values=sg-id`
```

Load balancer health

```
`# Check load balancer health`
`PS C:\migrations_workspace>` `aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:region:account-id:targetgroup/group-name/group-id`
```
