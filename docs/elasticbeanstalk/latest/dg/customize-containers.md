# Configuring Elastic Beanstalk environments

This topic focuses on the configuration options available in the Elastic Beanstalk console. AWS Elastic Beanstalk provides a wide range of options for customizing the
resources in your environment, along with Elastic Beanstalk behavior and platform settings.

The following topics show how to configure your environment in the console.
They also describe the underlying namespaces that correspond to the console options for use with configuration files or API configuration options. To learn
about advanced configuration methods, see [Configuring Elastic Beanstalk environments (advanced)](beanstalk-environment-configuration-advanced.md "beanstalk-environment-configuration-advanced.md").

###### Topics

- [Provisioned resources](#customize-containers-resources "#customize-containers-resources")
- [Environment configuration using the Elastic Beanstalk console](environments-cfg-console.md "environments-cfg-console.md")
- [The Amazon EC2 instances for your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md")
- [Auto Scaling your Elastic Beanstalk environment instances](using-features.managing.md "using-features.managing.md")
- [Load balancer for your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md")
- [Adding a database to your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md")
- [Your AWS Elastic Beanstalk environment security](using-features.managing.md "using-features.managing.md")
- [Tagging resources in your Elastic Beanstalk environments](using-features.md "using-features.md")
- [Environment variables and other software settings](environments-cfg-softwaresettings.md "environments-cfg-softwaresettings.md")
- [Elastic Beanstalk environment notifications with Amazon SNS](using-features.managing.md "using-features.managing.md")
- [Configuring Amazon Virtual Private Cloud (Amazon VPC) with Elastic Beanstalk](using-features.managing.md "using-features.managing.md")
- [Your Elastic Beanstalk environment's Domain name](customdomains.md "customdomains.md")

## Provisioned resources

When you create a web server environment, Elastic Beanstalk creates multiple resources to support the operation of your application. This chapter describes how
to customize these resources for your Elastic Beanstalk environment.

- **EC2 instance** – An Amazon Elastic Compute Cloud (Amazon EC2) virtual
  machine configured to run web apps on the platform that you choose.

Each platform runs a specific set of software, configuration files, and scripts to support a specific language version, framework, web container, or
combination of these. Most platforms use either Apache or NGINX as a reverse proxy that sits in front of your web app, forwards requests to it, serves
static assets, and generates access and error logs.

- **Instance security group** – An Amazon EC2 security group configured to allow inbound traffic on port 80. This
  resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic isn't allowed on other ports.
- **Load balancer** – An Elastic Load Balancing load balancer configured to distribute requests to the instances running your
  application. A load balancer also eliminates the need to expose your instances directly to the internet.
- **Load balancer security group** – An Amazon EC2 security group configured to allow inbound traffic on port 80. This
  resource lets HTTP traffic from the internet reach the load balancer. By default, traffic isn't allowed on other ports.
- **Auto Scaling group** – An Auto Scaling group configured to replace
  an instance if it is terminated or becomes unavailable.
- **Amazon S3 bucket** – A storage location for your source
  code, logs, and other artifacts that are created when you use Elastic Beanstalk.
- **Amazon CloudWatch alarms** – Two CloudWatch alarms that monitor the load on the instances in your environment and that are
  triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
- **AWS CloudFormation stack** – Elastic Beanstalk uses AWS CloudFormation to launch the
  resources in your environment and propagate configuration changes. The resources are defined
  in a template that you can view in the [AWS CloudFormation
  console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
- **Domain name** – A domain name that routes to your
  web app in the form
  _`subdomain`.`region`.elasticbeanstalk.com_.

###### Domain security

To augment the security of your Elastic Beanstalk applications, the _elasticbeanstalk.com_ domain is registered in the
[Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/").

If you ever need to set sensitive cookies in the default domain name for your Elastic Beanstalk applications, we recommend that you use cookies with a
`__Host-` prefix for increased security. This practice defends your domain against cross-site request forgery attempts (CSRF). For more
information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla
Developer Network.
