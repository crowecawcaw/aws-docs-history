

# Platform hooks
<a name="platforms-linux-extend.hooks"></a>

Platform hooks are specifically designed to extend your environment's platform. These are custom scripts and other executable files that you deploy as part of your application's source code, and Elastic Beanstalk runs during various instance provisioning stages.

**Note**  
Platform hooks aren't supported on Amazon Linux AMI platform versions (preceding Amazon Linux 2).

## Application deployment platform hooks
<a name="platforms-linux-extend.hooks.appdeploy"></a>

An *application deployment* occurs when you provide a new source bundle for deployment, or when you make a configuration change that requires termination and recreation of all environment instances.

To provide platform hooks that run during an application deployment, place the files under the `.platform/hooks` directory in your source bundle, in one of the following subdirectories.
+ `prebuild` – Files here run after the Elastic Beanstalk platform engine downloads and extracts the application source bundle, and before it sets up and configures the application and web server.

  The `prebuild` files run after running commands found in the [commands](customize-containers-ec2.md#linux-commands) section of any configuration file and before running `Buildfile` commands.
+ `predeploy` – Files here run after the Elastic Beanstalk platform engine sets up and configures the application and web server, and before it deploys them to their final runtime location.

  The `predeploy` files run after running commands found in the [container\_commands](customize-containers-ec2.md#linux-container-commands) section of any configuration file and before running `Procfile` commands.
+ `postdeploy` – Files here run after the Elastic Beanstalk platform engine deploys the application and proxy server.

  This is the last deployment workflow step.

## Configuration deployment platform hooks
<a name="platforms-linux-extend.hooks.configdeploy"></a>

A *configuration deployment* occurs when you make configuration changes that only update environment instances without recreating them. The following option updates cause a configuration update.
+ [Environment properties and platform-specific settings](environments-cfg-softwaresettings.md)
+ [Static files](environment-cfg-staticfiles.md)
+ [AWS X-Ray daemon](environment-configuration-debugging.md)
+ [Log storage and streaming](environments-cfg-logging.md)
+ Application port (for details see [Reverse proxy configuration](platforms-linux-extend.proxy.md))

To provide hooks that run during a configuration deployment, place them under the `.platform/confighooks` directory in your source bundle. The same three subdirectories as for application deployment hooks apply.

## More about platform hooks
<a name="platforms-linux-extend.hooks.more"></a>

Hook files can be binary files, or script files starting with a `#!` line containing their interpreter path, such as `#!/bin/bash`. All files must have execute permission. Use `chmod +x` to set execute permission on your hook files. For all Amazon Linux 2023 and Amazon Linux 2 based platforms versions that were released on or after April 29, 2022, Elastic Beanstalk automatically grants execute permissions to all of the platform hook scripts. In this case you don't have to manually grant execute permissions. For a list of these platform versions, refer to the [April 29, 2022 ](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-04-29-linux.html#release-2022-04-29-linux.platforms) Linux release notes in the *AWS Elastic Beanstalk Release Notes Guide*.

Elastic Beanstalk runs files in each one of these directories in lexicographical order of file names. All files run as the `root` user. The current working directory (cwd) for platform hooks is the application's root directory. For `prebuild` and `predeploy` files it's the application staging directory, and for `postdeploy` files it's the current application directory. If one of the files fails (exits with a non-zero exit code), the deployment aborts and fails.

A platform hooks text script may fail if it contains Windows *Carriage Return / Line Feed* (CRLF) line break characters. If a file was saved in a Windows host, then transferred to a Linux server, it may contain Windows CRLF line breaks. For platforms released on or after [December 29, 2022](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-12-29-linux.html), Elastic Beanstalk automatically converts Windows CRLF characters to Linux *Line Feed* (LF) line break characters in platform hooks text files. If you application runs on any Amazon Linux 2 platforms that were release prior to this date, you'll need to convert the Windows CRLF characters to Linux LF characters. One way to accomplish this is to create and save the script file on a Linux host. Tools that convert these characters are also available on the internet.

Hook files have access to all environment properties that you've defined in application options, and to the system environment variables `HOME`, `PATH`, and `PORT`. 

To get values of environment variables and other configuration options into your platform hook scripts, you can use the `get-config` utility that Elastic Beanstalk provides on environment instances. For details, see [Platform script tools for your Elastic Beanstalk environments](custom-platforms-scripts.md).