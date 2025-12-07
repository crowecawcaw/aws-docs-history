# Configuration files

You can add [configuration files](ebextensions.md "ebextensions.md") to the `.ebextensions` directory of your application's source code to
configure various aspects of your Elastic Beanstalk environment. Among other things, configuration files let you customize software and other files on your
environment's instances and run initialization commands on the instances. For more information, see [Customizing software on Linux servers](customize-containers-ec2.md "customize-containers-ec2.md").

You can also set [configuration options](command-options.md "command-options.md") using configuration files. Many of the options control platform
behavior, and some of these options are [platform specific](command-options-specific.md "command-options-specific.md").

For platforms based on Amazon Linux 2 and Amazon Linux 2023, we recommend using _Buildfile_, _Procfile_, and _platform
hooks_ to configure and run custom code on your environment instances during instance provisioning. These mechanisms are described in the
previous sections on this page. You can still use commands and container commands in `.ebextensions` configuration files, but they
aren't as easy to work with. For example, writing command scripts inside a YAML file can be challenging from a syntax standpoint. You still need to use
`.ebextensions` configuration files for any script that needs a reference to a AWS CloudFormation resource.
