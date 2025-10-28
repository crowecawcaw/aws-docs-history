# Understanding IIS to Elastic Beanstalk migration mapping

The migration from IIS to Elastic Beanstalk involves mapping your on-premises Windows server configuration to AWS cloud resources. Understanding this mapping is crucial for successful migrations and post-migration management.

## IIS sites and applications in Elastic Beanstalk

In IIS, a website represents a collection of web applications and virtual directories, each with its own configuration and content. When migrating to Elastic Beanstalk, these components are transformed as follows:

**IIS websites**

Your IIS websites become applications within Elastic Beanstalk. Each website's configuration, including its bindings, application pools, and authentication settings, is preserved through Elastic Beanstalk's deployment manifest (`aws-windows-deployment-manifest.json`).

For example, if you have multiple sites like _Default Web Site_ and _IntranetSite_, **eb migrate** packages each site's content and configuration while maintaining their isolation.

The command creates appropriate Application Load Balancer (ALB) listener rules to handle routing
requests to your applications. It also configures security groups to ensure proper port
access based on your original IIS bindings.

**Application pools**

IIS application pools provide worker process isolation, runtime management, and recycling capabilities for your applications. In Elastic Beanstalk, these are mapped to environment processes defined through the `aws:elasticbeanstalk:environment:process` namespace and configured via IIS on the EC2 instances.

The migration preserves critical application pool settings including the
following:

- Process model configurations - Identity (ApplicationPoolIdentity, NetworkService, or custom accounts), idle timeout settings, and process recycling intervals
- .NET CLR version settings - Maintains your specified .NET Framework version (v2.0, v4.0, or No Managed Code) to ensure application compatibility
- Managed pipeline mode - Preserves Integrated or Classic pipeline mode settings to maintain your HTTP request processing architecture
- Advanced settings - Queue length, CPU limits, rapid-fail protection thresholds, and startup time limits

The **eb migrate** command preserves mappings between sites and application pools during the migration to your Elastic Beanstalk environment.

If your application pools use custom recycling schedules (specific times or memory thresholds), these are implemented through PowerShell scripts in the deployment package that configure the appropriate IIS settings on the EC2 instances.

**Website bindings**

IIS website bindings, which define how clients access your applications, are
transformed into the following Application Load Balancer (ALB) configurations:

- Port bindings are mapped to corresponding ALB listener rules
- Host header configurations are translated into ALB routing rules
- SSL-enabled sites use AWS Certificate Manager (ACM) for certificate management

## Virtual directory and application path management

IIS virtual directories and applications provide URL path mapping to physical directories. Elastic Beanstalk maintains these relationships through the following constructs:

**Virtual directories**

The migration process preserves the physical paths of your virtual directories in the deployment package.

Path mappings are configured in the IIS configuration on the EC2 instances, ensuring that your URL structure remains intact after migration.

**Non-system drive physical paths**

###### Important

By default, Elastic Beanstalk Windows environments only provision the C:\ drive (root volume). In the current version, applications with content on non-system drives (D:\, E:\, etc.) are not supported for migration.

The **eb migrate** command automatically detects physical paths
located on non-system drives and warns you about potential issue like the following
example:

```
`ERROR: Detected physical paths on drive D:\ which are not supported in the current version:
 - D:\websites\intranet
 - D:\shared\images

Migration of content from non-system drives is not supported. Please relocate this content to the C:\ drive before migration. Otherwise, select only those sites that are on C:\.`
```

If your application has dependencies on non-system drives, you will need to modify your application to store all content on the C:\ drive before migration.

**Nested applications**

Applications nested under websites are deployed with their correct path
configurations and appropriate application pool assignments. The migration process
preserves all `web.config` settings, ensuring that
application-specific configurations continue to function as expected in the cloud
environment.

## URL rewrite and application request routing (ARR)

If your IIS deployment uses URL Rewrite or Application Request Routing (ARR), **eb
migrate** handles these configurations through the following rules and
configuration:

**URL rewrite rules**

URL rewrite rules from your `web.config` files are translated
into ALB routing rules where possible. For example, the following entry becomes an ALB
listener rule directing traffic based on host headers and path patterns.:

```
<!-- Original IIS URL Rewrite Rule -->
<rule name="Redirect to WWW" stopProcessing="true">
    <match url="(.*)" />
    <conditions>
        <add input="{HTTP_HOST}" pattern="^example.com$" />
    </conditions>
    <action type="Redirect" url="http://www.example.com/{R:1}" />
</rule>
```

**Application request routing**

ARR configurations are preserved through the installation of ARR features on EC2
instances. The migration process completes the following tasks:

- Configures proxy settings to match your source environment
- Maintains URL rewrite rules associated with ARR

## Migration artifact structure

When you run **eb migrate**, it creates a structured directory containing
all necessary deployment components. The following listing describes the directory
structure:

```
C:\migration_workspace\
└── .\migrations\latest\
    └── upload_target\
        ├── [SiteName].zip                 # One ZIP per IIS site
        ├── aws-windows-deployment-manifest.json
        └── ebmigrateScripts\
            ├── site_installer.ps1         # Site installation scripts
            ├── arr_configuration.ps1      # ARR configuration scripts
            ├── permission_handler.ps1     # Permission management
            └── firewall_config.ps1        # Windows Firewall rules
```

The `aws-windows-deployment-manifest.json` file is the core
configuration file that instructs Elastic Beanstalk how to deploy your applications. Refer to the
following example structure:

```
{
    "manifestVersion": 1,
    "deployments": {
        "msDeploy": [
            {
                "name": "Primary Site",
                "parameters": {
                    "appBundle": "DefaultWebSite.zip",
                    "iisPath": "/",
                    "iisWebSite": "Default Web Site"
                }
            }
        ],
        "custom": [
            {
                "name": "ConfigureARR",
                "scripts": {
                    "install": {
                        "file": "ebmigrateScripts\\arr_configuration.ps1"
                    },
                    "uninstall": {
                        "file": "ebmigrateScripts\\noop.ps1"
                    },
                    "restart": {
                        "file": "ebmigrateScripts\\noop.ps1"
                    }
                }
            }
        ]
    }
}
```

This manifest ensures these results for your migration:

- Applications are deployed to correct IIS paths
- Custom configurations are applied
- Site-specific settings are preserved
- Deployment order is maintained
