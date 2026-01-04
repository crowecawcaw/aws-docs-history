# Configuring HTTPS for your Elastic Beanstalk environment

This topics in this section explain how to configure HTTPS for your Elastic Beanstalk environment. HTTPS is a must for any application that transmits user data or
login information.

If you've purchased and configured a [custom domain name](customdomains.md "customdomains.md") for your Elastic Beanstalk environment, you can use HTTPS to allow
users to connect to your web site securely.

If you don't own a domain name, you can still use HTTPS with a self-signed certificate for development and
testing purposes. For more information, see [Server certificates](configuring-https.md "configuring-https.md").

###### Configuring HTTPS Termination at the load balancer

A load balancer distributes requests to the EC2 instances running your application. A load balancer also eliminates the need to expose your instances
directly to the internet. The simplest way to use HTTPS with an Elastic Beanstalk multi-instance environment is to configure a secure listener for the load balancer.
The connection between the client and the load balancer remains secure, so you can configure the load balancer to terminate HTTPS. The back end
connections between the load balancer and EC2 instances use HTTP, so no additional configuration of the instances is required. For detailed instructions
to configure a secure listenter, see [Configuring HTTPS Termination at the load balancer](configuring-https-elb.md "configuring-https-elb.md").

###### Configuring HTTPS Termination at the EC2 instance

If you run your application in a single instance environment, or need to secure the connection all the way to the EC2 instances behind the load
balancer, you can configure the proxy server that runs on the instance to terminate HTTPS. Configuring your instances to terminate HTTPS connections
requires the use of [configuration files](ebextensions.md "ebextensions.md") to modify the software running on the instances, and to modify security groups
to allow secure connections. For more information, see [Configuring HTTPS Termination at the instance](https-singleinstance.md "https-singleinstance.md").

###### Configuring HTTPS end-to-end

For end-to-end HTTPS in a load-balanced environment, you can combine instance and load balancer termination to encrypt both connections. By default,
if you configure the load balancer to forward traffic using HTTPS, it will trust any certificate presented to it by the backend instances. For maximum
security, you can attach policies to the load balancer that prevent it from connecting to instances that don't present a public certificate that it
trusts. For more information, see [Configuring end-to-end encryption in a load-balanced Elastic Beanstalk environment](configuring-https-endtoend.md "configuring-https-endtoend.md").

###### Configuring HTTPS with TCP Passthrough

You can also configure the load balancer to relay HTTPS traffic without decrypting it. For more information, see [Configuring your environment's load balancer for TCP Passthrough](https-tcp-passthrough.md "https-tcp-passthrough.md").

###### Note

The [Does it have Snakes?](https://github.com/awslabs/eb-tomcat-snakes "https://github.com/awslabs/eb-tomcat-snakes") sample application on GitHub includes configuration files
and instructions for each method of configuring HTTPS with a Tomcat web application. See the [readme file](https://github.com/awslabs/eb-tomcat-snakes/blob/master/README.md "https://github.com/awslabs/eb-tomcat-snakes/blob/master/README.md") and [HTTPS instructions](https://github.com/awslabs/eb-tomcat-snakes/blob/master/src/.ebextensions/inactive/HTTPS.md "https://github.com/awslabs/eb-tomcat-snakes/blob/master/src/.ebextensions/inactive/HTTPS.md") for details.

###### Topics

- [Server certificates](configuring-https.md "configuring-https.md")
- [Configuring HTTPS Termination at the load balancer](configuring-https-elb.md "configuring-https-elb.md")
- [Configuring HTTPS Termination at the instance](https-singleinstance.md "https-singleinstance.md")
- [Configuring end-to-end encryption in a load-balanced Elastic Beanstalk environment](configuring-https-endtoend.md "configuring-https-endtoend.md")
- [Configuring your environment's load balancer for TCP Passthrough](https-tcp-passthrough.md "https-tcp-passthrough.md")
- [Configuring HTTP to HTTPS redirection](configuring-https-httpredirect.md "configuring-https-httpredirect.md")
