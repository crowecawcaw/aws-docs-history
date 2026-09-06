

# Migration from Amazon Linux AMI (AL1) to AL2 or AL2023
<a name="using-features.migration-al.generic.from-al1"></a>

If your Elastic Beanstalk application is based on an Amazon Linux AMI platform branch, use this section to learn how to migrate your application's environments to Amazon Linux 2 or Amazon Linux 2023. Previous generation platform branches based on [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami/) are now retired.

We highly recommend that you migrate to Amazon Linux 2023, since it's more recent than Amazon Linux 2. The Amazon Linux 2 operating system will reach end of support before Amazon Linux 2023 does, so you'll benefit from a longer time frame of support if you migrate to Amazon Linux 2023.

It's worthwhile to note that there is a high degree of compatibility between the Elastic Beanstalk Amazon Linux 2 and Amazon Linux 2023 platforms. Although some areas do have differences: the Instance Metadata Service Version 1 (IMDSv1) option default, support for the pkg-repo instance tool, and some Apache HTTPd configuration. For more information, see [Amazon Linux 2023](platforms-linux.md#platforms-linux.versions.al2023)

## Differences and compatibility
<a name="using-features.migration-al.generic.from-al1.differences"></a>

The AL2023/AL2 based platform branches aren't guaranteed to be backward compatible with your existing application. It's also important to be aware that even if your application code successfully deploys to the new platform version, it might behave or perform differently due to operating system and run time differences.

Although Amazon Linux AMI and AL2023/AL2 share the same Linux kernel, they differ in the following aspects: their initialization system, the `libc` versions, the compiler tool chain, and various packages. For more information, see [Amazon Linux 2 FAQs](https://aws.amazon.com//amazon-linux-2/faqs/). 

The Elastic Beanstalk service has also updated platform specific versions of runtime, build tools, and other dependencies. 

Therefore we recommend that you take your time, test your application thoroughly in a development environment, and make any necessary adjustments.

## General migration process
<a name="using-features.migration-al.generic.from-al1.process"></a>

When you're ready to go to production, Elastic Beanstalk requires a blue/green deployment to perform the upgrade. The following are the general best practice steps that we recommend for migration with a blue/green deployment procedure.

**Preparing to test for your migration**  
Before you deploy your application and start testing, review the information in [Considerations for all Linux platforms](#using-features.migration-al.generic), which follows later in this topic. Also, review the information that applies to your platform in the [Platform specific considerations](#using-features.migration-al.specific) section that follows. Make a note of the specific information from this content that applies or may apply to your application and configuration set up.

**High level migration steps**

1. Create a new environment that's based on an AL2 or AL2023 platform branch. We recommend that you migrate to an AL2023 platform branch.

1. Deploy your application to the target AL2023/AL2 environment.

   Your existing production environment will remain active and unaffected, while you iterate through testing and making adjustments to the new environment.

1. Test your application thoroughly in the new environment.

1. When your destination AL2023/AL2 environment is ready to go to production, swap the CNAMEs of the two environments to redirect traffic to the new environment.

**More detailed migration steps and best practices**  
For a more detailed blue/green deployment procedure, see [Blue/Green deployments with Elastic Beanstalk](using-features.CNAMESwap.md).

For more specific guidance and detailed best practice steps, see [Blue/Green method](using-features.platform.upgrade.md#using-features.platform.upgrade.bluegreen).

## More references to help plan your migration
<a name="using-features.migration-al.generic.from-al1.references"></a>

The following references can offer additional information to plan your migration.
+ [Comparing Amazon Linux 2 and Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) *Amazon Linux 2023 User Guide*.
+  [What is Amazon Linux 2023?](https://docs.aws.amazon.com/linux/al2023/ug/what-is-amazon-linux.html) in the *Amazon Linux 2023 User Guide*
+ [ Elastic Beanstalk supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html) in *AWS Elastic Beanstalk Platforms*
+ [Retired platform branch history](platforms-schedule.md#platforms-support-policy.retired)
+ [Elastic Beanstalk Linux platforms](platforms-linux.md)
+ [Platform retirement FAQ](using-features.migration-al.FAQ.md)

## Considerations for all Linux platforms
<a name="using-features.migration-al.generic"></a>

The following table discusses considerations you should be aware of when planning an application migration to AL2023/AL2. These considerations apply to any of the Elastic Beanstalk Linux platforms, regardless of specific programming languages or application servers.


|  **Area**  |  **Changes and information**  | 
| --- | --- | 
| Configuration Files | On AL2023/AL2 platforms, you can use [configuration files](ebextensions.md) as before, and all sections work the same way. However, specific settings might not work the same as they did on previous Amazon Linux AMI platforms. For example:+  Some software packages that you install using a configuration file might not be available on AL2023/AL2, or their names might have changed. <br />+  Some platform specific configuration options have moved from their platform specific namespaces to different, platform agnostic namespaces. <br />+  Proxy configuration files provided in the `.ebextensions/nginx` directory should move to the `.platform/nginx` platform hooks directory. For details, see [Reverse proxy configuration](platforms-linux-extend.proxy.md). <br />We recommend using platform hooks to run custom code on your environment instances. You can still use commands and container commands in `.ebextensions` configuration files, but they aren't as easy to work with. For example, writing command scripts inside a YAML file can be cumbersome and difficult to test.<br />You still need to use `.ebextensions` configuration files for any script that needs a reference to an AWS CloudFormation resource. | 
| Platform hooks | AL2 platforms introduced a new way to extend your environment's platform by adding executable files to hook directories on the environment's instances. With previous Linux platform versions, you might have used custom platform hooks. These hooks weren't designed for managed platforms and weren't supported, but could work in useful ways in some cases. With AL2023/AL2 platform versions, custom platform hooks don't work. You should migrate any hooks to the new platform hooks. For details see [Platform hooks](platforms-linux-extend.hooks.md). | 
| Supported proxy servers | AL2023/AL2 platform versions support the same reverse proxy servers as each platform supported in its Amazon Linux AMI platform versions. All AL2023/AL2; platform versions use nginx as their default reverse proxy server, with the exception of the ECS and Docker platforms. The Tomcat, Node.js, PHP, and Python platform also support Apache HTTPD as an alternative. All platforms enable proxy server configuration in a uniform way, as described in this section. However, configuring the proxy server is slightly different than it was on Amazon Linux AMI. These are the differences for all platforms:+  **Default is nginx** – The default proxy server on all AL2023/AL2 platform versions is nginx. On Amazon Linux AMI platform versions of Tomcat, PHP, and Python, the default proxy server was Apache HTTPD. <br />+  **Consistent namespace** – All AL2023/AL2 platform versions use the `aws:elasticbeanstalk:environment:proxy` namespace to configure the proxy server. On Amazon Linux AMI platform versions this was a per-platform decision, and Node.js used a different namespace. <br />+  **Configuration file location** – You should place proxy configuration files in the `.platform/nginx` and `.platform/httpd` directories on all AL2023/AL2 platform versions. On Amazon Linux AMI platform versions these locations were `.ebextensions/nginx` and `.ebextensions/httpd`, respectively. <br />For platform-specific proxy configuration changes, see [Platform specific considerations](#using-features.migration-al.specific). For information about proxy configuration on AL2023/AL2 platforms, see [Reverse proxy configuration](platforms-linux-extend.proxy.md). | 
|  Proxy Configuration Changes  | There are proxy configuration changes that apply uniformly to all platforms in addition to proxy configuration changes that are specific to each platform. It's important to refer to both to accurately configure your environments.+  **All platforms** – see [Reverse proxy configuration](platforms-linux-extend.proxy.md) <br />+  **Platform-specific** – see [Platform specific considerations](#using-features.migration-al.specific).  | 
| Instance profile | AL2023/AL2 platforms require an instance profile to be configured. Environment creation might temporarily succeed without one, but the environment might show errors soon after creation when actions requiring an instance profile start failing. For details, see [Managing Elastic Beanstalk instance profiles](iam-instanceprofile.md). | 
| Enhanced health | AL2023/AL2 platform versions enable enhanced health by default. This is a change if you don't use the Elastic Beanstalk console to create your environments. The console enables enhanced health by default whenever possible, regardless of platform version. For details, see [Enhanced health reporting and monitoring in Elastic Beanstalk](health-enhanced.md). | 
| Custom AMI | If your environment uses a [custom AMI](using-features.customenv.md), create a new AMI based on AL2023/AL2 for your new environment using an Elastic Beanstalk AL2023/AL2 platform. | 
| Custom platforms | The managed AMIs of AL2023/AL2 platform versions don't support custom platforms. | 

## Platform specific considerations
<a name="using-features.migration-al.specific"></a>

This section discusses migration considerations specific to particular Elastic Beanstalk Linux platforms.

### Docker
<a name="using-features.migration-al.specific.docker"></a>

The Docker platform branch family based on Amazon Linux AMI (AL1) includes three platform branches. We recommend a different migration path for each. 


<table>
<thead>
  <tr><th> <b>AL1 Platform branch</b> </th><th> <b>Migration Path to AL2023/AL2</b> </th></tr>
</thead>
<tbody>
  <tr><td>Multi-container Docker managed by Amazon ECS running on Amazon Linux AMI (AL1)</td><td> ECS based Docker AL2023/AL2 platform branches The <i>ECS based Docker AL2023/AL2</i> platform branches offer a straightforward migration path for environments running on the <i>Multi-container Docker AL1</i> platform branch. <ul><li> Like the previous <i>Multi-container Docker AL1</i> branch, the AL2023/AL2 platform branches use Amazon ECS to coordinate deployment of multiple Docker containers to an Amazon ECS cluster in an Elastic Beanstalk environment.  </li><li> The AL2023/AL2 platform branches support all of the features in the previous <i>Multi-container Docker AL1</i> branch.  </li><li> The AL2023/AL2 platform branches also support the same <code>Dockerrun.aws.json</code> v2 file.  </li></ul>For more information about migrating your applications running on the <i>Multi-container Docker Amazon Linux</i> platform branch to an <i>Amazon ECS running on AL2023/AL2</i> platform branch, see <a href="migrate-to-ec2-AL2-platform.md">Migrating your Elastic Beanstalk application from ECS managed Multi-container Docker on AL1 to ECS on Amazon Linux 2023</a>.</td></tr>
  <tr><td>Docker running on Amazon Linux AMI (AL1)<br />Preconfigured Docker (Glassfish 5.0) running Amazon Linux AMI (AL1)</td><td> Docker Running on AL2023/AL2 platform branch We recommend that you migrate your applications running on environments based on <i>Preconfigured Docker (Glassfish 5.0)</i> or <i>Docker running on Amazon Linux AMI (AL1) </i> to environments that are based on the <i>Docker Running on Amazon Linux 2</i> or <i>Docker Running on AL2023</i> platform branches. If your environment is based on the <i>Preconfigured Docker (Glassfish 5.0)</i> platform branch, see <a href="create_deploy_dockerpreconfig.md#docker-glassfish-tutorial">Deploying a GlassFish application to the Docker platform: a migration path to Amazon Linux 2023</a>.<br />The following table lists migration information specific to the platform branch <i>Docker Running on AL2023/AL2</i>.
<table>
<thead>
  <tr><th> <b>Area</b> </th><th> <b>Changes and information</b> </th></tr>
</thead>
<tbody>
  <tr><td>Storage</td><td>Elastic Beanstalk configures Docker to use <a href="https://docs.docker.com/storage/storagedriver/">storage drivers</a> to store Docker images and container data. On Amazon Linux AMI, Elastic Beanstalk used the <a href="https://docs.docker.com/storage/storagedriver/device-mapper-driver/">Device Mapper storage driver</a>. To improve performance, Elastic Beanstalk provisioned an extra Amazon EBS volume. On AL2023/AL2 Docker platform versions, Elastic Beanstalk uses the <a href="https://docs.docker.com/storage/storagedriver/overlayfs-driver/">OverlayFS storage driver</a>, and achieves even better performance while not requiring a separate volume anymore.<br />With Amazon Linux AMI, if you used the <code>BlockDeviceMappings</code> option of the <code>aws:autoscaling:launchconfiguration</code> namespace to add custom storage volumes to a Docker environment, we advised you to also add the <code>/dev/xvdcz</code> Amazon EBS volume that Elastic Beanstalk provisions. Elastic Beanstalk doesn't provision this volume anymore, so you should remove it from your configuration files. For details, see <a href="create_deploy_docker.container.console.md#docker-alami">Docker configuration on Amazon Linux AMI (preceding Amazon Linux 2)</a>.</td></tr>
  <tr><td>Private repository authentication</td><td>When you provide a Docker-generated authentication file to connect to a private repository, you no longer need to convert it to the older format that Amazon Linux AMI Docker platform versions required. AL2023/AL2 Docker platform versions support the new format. For details, see <a href="docker-configuration.remote-repo.md">Authenticating with image repositories</a>.</td></tr>
  <tr><td>Proxy server</td><td>AL2023/AL2 Docker platform versions don't support standalone containers that don't run behind a proxy server. On Amazon Linux AMI Docker platform versions, this used to be possible through the <code>none</code> value of the <code>ProxyServer</code> option in the <code>aws:elasticbeanstalk:environment:proxy</code> namespace.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


### Go
<a name="using-features.migration-al.specific.go"></a>

The following table lists migration information for the AL2023/AL2 platform versions in the [Go platform](go-environment.md).


|  **Area**  |  **Changes and information**  | 
| --- | --- | 
| Port passing | On AL2023/AL2 platforms, Elastic Beanstalk doesn't pass a port value to your application process through the `PORT` environment variable. You can simulate this behavior for your process by configuring a `PORT` environment property yourself. However, if you have multiple processes, and you're counting on Elastic Beanstalk passing incremental port values to your processes (5000, 5100, 5200 etc.), you should modify your implementation. For details see [Reverse proxy configuration](platforms-linux-extend.proxy.md). | 

### Amazon Corretto
<a name="using-features.migration-al.specific.corretto"></a>

The following table lists migration information for the Corretto platform branches in the [Java SE platform](java-se-platform.md).


|  **Area**  |  **Changes and information**  | 
| --- | --- | 
| Corretto vs. OpenJDK | To implement the Java Platform, Standard Edition (Java SE), AL2023/AL2 platform branches use [Amazon Corretto](https://aws.amazon.com/corretto), an AWS distribution of the Open Java Development Kit (OpenJDK). Prior Elastic Beanstalk Java SE platform branches use the OpenJDK packages included with Amazon Linux AMI. | 
| Build tools | AL2023/AL2 platforms have newer versions of the build tools: `gradle`, `maven`, and `ant`. | 
| JAR file handling | On AL2023/AL2 platforms, if your source bundle (ZIP file) contains a single JAR file and no other files, Elastic Beanstalk no longer renames the JAR file to `application.jar`. Renaming occurs only if you submit a JAR file on its own, not within a ZIP file. | 
| Port passing | On AL2023/AL2 platforms, Elastic Beanstalk doesn't pass a port value to your application process through the `PORT` environment variable. You can simulate this behavior for your process by configuring a `PORT` environment property yourself. However, if you have multiple processes, and you're counting on Elastic Beanstalk passing incremental port values to your processes (5000, 5100, 5200 etc.), you should modify your implementation. For details see [Reverse proxy configuration](platforms-linux-extend.proxy.md). | 
| Java 7 | Elastic Beanstalk doesn't support an AL2023/AL2 Java 7 platform branch. If you have a Java 7 application, migrate it to Corretto 8 or Corretto 11. | 

### Tomcat
<a name="using-features.migration-al.specific.tomcat"></a>

The following table lists migration information for the AL2023/AL2 platform versions in the [Tomcat platform](java-tomcat-platform.md).


<table>
<thead>
  <tr><th> <b>Area</b> </th><th> <b>Changes and information</b> </th></tr>
</thead>
<tbody>
  <tr><td>Configuration options</td><td>On AL2023/AL2 platform versions, Elastic Beanstalk supports only a subset of the configuration options and option values in the <code>aws:elasticbeanstalk:environment:proxy</code> namespace. Here's the migration information for each option.
<table>
<thead>
  <tr><th> <b>Option</b> </th><th> <b>Migration information</b> </th></tr>
</thead>
<tbody>
  <tr><td><code>GzipCompression</code></td><td>Unsupported on AL2023/AL2 platform versions.</td></tr>
  <tr><td><code>ProxyServer</code></td><td>AL2023/AL2 Tomcat platform versions support both the nginx and the Apache HTTPD version 2.4 proxy servers. However, Apache version 2.2 isn't supported.<br />On Amazon Linux AMI platform versions, the default proxy was Apache 2.4. If you used the default proxy setting and added custom proxy configuration files, your proxy configuration should still work on AL2023/AL2. However, if you used the <code>apache/2.2</code> option value, you now have to migrate your proxy configuration to Apache version 2.4.</td></tr>
</tbody>
</table>
<br />The <code>XX:MaxPermSize</code> option in the <code>aws:elasticbeanstalk:container:tomcat:jvmoptions</code> namespace isn't supported on AL2023/AL2 platform versions. The JVM setting to modify the size of the permanent generation applies only to Java 7 and earlier, and is therefore not applicable to AL2023/AL2 platform versions.</td></tr>
  <tr><td>Application path</td><td>On AL2023/AL2 platforms, the path to the application's directory on Amazon EC2 instances of your environment is <code>/var/app/current</code>. It was <code>/var/lib/tomcat8/webapps</code> on Amazon Linux AMI platforms.</td></tr>
</tbody>
</table>


### Node.js
<a name="using-features.migration-al.specific.nodejs"></a>

The following table lists migration information for the AL2023/AL2 platform versions in the [Node.js platform](create_deploy_nodejs.container.md).


<table>
<thead>
  <tr><th> <b>Area</b> </th><th> <b>Changes and information</b> </th></tr>
</thead>
<tbody>
  <tr><td>Installed Node.js versions</td><td>On AL2023/AL2 platforms, Elastic Beanstalk maintains several Node.js platform branches, and only installs the latest version of the Node.js major version corresponding with the platform branch on each platform version. For example, each platform version in the Node.js 12 platform branch only has Node.js 12.x.y installed by default. On Amazon Linux AMI platform versions, we installed the multiple versions of multiple Node.js versions on each platform version, and only maintained a single platform branch.<br />Choose the Node.js platform branch that corresponds with the Node.js major version that your application needs.</td></tr>
  <tr><td>Apache HTTPD log file names</td><td>On AL2023/AL2 platforms, if you use the Apache HTTPD proxy server, the HTTPD log file names are <code>access_log</code> and <code>error_log</code>, which is consistent with all other platforms that support Apache HTTPD. On Amazon Linux AMI platform versions, these log files were named <code>access.log</code> and <code>error.log</code>, respectively.<br />For details about log file names and locations for all platforms, see <a href="AWSHowTo.cloudwatchlogs.md#AWSHowTo.cloudwatchlogs.loggroups">How Elastic Beanstalk sets up CloudWatch Logs</a>.</td></tr>
  <tr><td>Configuration options</td><td>On AL2023/AL2 platforms, Elastic Beanstalk doesn't support the configuration options in the <code>aws:elasticbeanstalk:container:nodejs</code> namespace. Some of the options have alternatives. Here's the migration information for each option.
<table>
<thead>
  <tr><th> <b>Option</b> </th><th> <b>Migration information</b> </th></tr>
</thead>
<tbody>
  <tr><td><code>NodeCommand</code></td><td>Use a <code>Procfile</code> or the <code>scripts</code> keyword in a <code>package.json</code> file to specify the start script.</td></tr>
  <tr><td><code>NodeVersion</code></td><td>Use the <code>engines</code> keyword in a <code>package.json</code> file to specify the Node.js version. Be aware that you can only specify a Node.js version that correspondes with your platform branch. For example, if you're using the Node.js 12 platform branch, you can specify only a 12.x.y Node.js version. For details, see <a href="nodejs-platform-dependencies.md#nodejs-platform-packagejson">Specifying Node.js dependencies with a package.json file</a>.</td></tr>
  <tr><td><code>GzipCompression</code></td><td>Unsupported on AL2023/AL2 platform versions.</td></tr>
  <tr><td><code>ProxyServer</code></td><td>On AL2023/AL2 Node.js platform versions, this option moved to the <code>aws:elasticbeanstalk:environment:proxy</code> namespace. You can choose between <code>nginx</code> (the default) and <code>apache</code>.<br />AL2023/AL2 Node.js platform versions don't support standalone applications that don't run behind a proxy server. On Amazon Linux AMI Node.js platform versions, this used to be possible through the <code>none</code> value of the <code>ProxyServer</code> option in the <code>aws:elasticbeanstalk:container:nodejs</code> namespace. If your environment runs a standalone application, update your code to listen to the port that the proxy server (nginx or Apache) forwards traffic to.<pre>var port = process.env.PORT || 5000;<br /><br />app.listen(port, function() {<br />  console.log('Server running at http://127.0.0.1:%s', port);<br />});</pre></td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


### PHP
<a name="using-features.migration-al.specific.php"></a>

The following table lists migration information for the AL2023/AL2 platform versions in the [PHP platform](create_deploy_PHP.container.md).


|  **Area**  |  **Changes and information**  | 
| --- | --- | 
| PHP file processing | On AL2023/AL2 platforms, PHP files are processed using PHP-FPM (a CGI process manager). On Amazon Linux AMI platforms we used mod\_php (an Apache module). | 
| Proxy server | AL2023/AL2 PHP platform versions support both the nginx and the Apache HTTPD proxy servers. The default is nginx.<br />Amazon Linux AMI PHP platform versions supported only Apache HTTPD. If you added custom Apache configuration files, you can set the `ProxyServer` option in the `aws:elasticbeanstalk:environment:proxy` namespace to `apache`. | 

### Python
<a name="using-features.migration-al.specific.python"></a>

The following table lists migration information for the AL2023/AL2 platform versions in the [Python platform](create-deploy-python-container.md).


|  **Area**  |  **Changes and information**  | 
| --- | --- | 
| WSGI server | On AL2023/AL2 platforms, [Gunicorn](https://gunicorn.org/) is the default WSGI server. By default, Gunicorn listens on port 8000. The port might be different than what your application used on the Amazon Linux AMI platform. If you're setting the `WSGIPath` option of the `[aws:elasticbeanstalk:container:python](command-options-specific.md#command-options-python)` namespace, replace the value with Gunicorn's syntax. For details, see [Python configuration namespaces](create-deploy-python-container.md#python-namespaces).<br />Alternatively, you can use a `Procfile` to specify and configure the WSGI server. For details, see [Configuring the WSGI server with a Procfile on Elastic Beanstalk](python-configuration-procfile.md). | 
| Application path | On AL2023/AL2 platforms, the path to the application's directory on Amazon EC2 instances of your environment is `/var/app/current`. It was `/opt/python/current/app` on Amazon Linux AMI platforms. | 
| Proxy server | AL2023/AL2 Python platform versions support both the nginx and the Apache HTTPD proxy servers. The default is nginx.<br />Amazon Linux AMI Python platform versions supported only Apache HTTPD. If you added custom Apache configuration files, you can set the `ProxyServer` option in the `aws:elasticbeanstalk:environment:proxy` namespace to `apache`. | 

### Ruby
<a name="using-features.migration-al.specific.ruby"></a>

The following table lists migration information for the AL2023/AL2 platform versions in the [Ruby platform](create_deploy_Ruby.container.md).


|  **Area**  |  **Changes and information**  | 
| --- | --- | 
| Installed Ruby versions | On AL2023/AL2 platforms, Elastic Beanstalk only installs the latest version of a single Ruby version, corresponding with the platform branch, on each platform version. For example, each platform version in the Ruby 2.6 platform branch only has Ruby 2.6.x installed. On Amazon Linux AMI platform versions, we installed the latest versions of multiple Ruby versions, for example, 2.4.x, 2.5.x, and 2.6.x.<br />If your application uses a Ruby version that doesn't correspond to the platform branch you're using, we recommend that you switch to a platform branch that has the correct Ruby version for your application. | 
| Application server | On AL2023/AL2 platforms, Elastic Beanstalk only installs the Puma application server on all Ruby platform versions. You can use a `Procfile` to start a different application server, and a `Gemfile` to install it.<br />On the Amazon Linux AMI platform, we supported two flavors of platform branches for each Ruby version—one with the Puma application server and the other with the Passenger application server. If your application uses Passenger, you can configure your Ruby environment to install and use Passenger.<br />For more information and examples, see [Using the Elastic Beanstalk Ruby platform](create_deploy_Ruby.container.md). | 