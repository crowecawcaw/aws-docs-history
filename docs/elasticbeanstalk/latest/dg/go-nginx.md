# Configuring the proxy server

Elastic Beanstalk uses nginx as the reverse proxy to map your application to your Elastic Load Balancing load balancer on port 80. Elastic Beanstalk provides a default nginx configuration
that you can either extend or override completely with your own configuration.

By default, Elastic Beanstalk configures the nginx proxy to forward requests to your application on port 5000. You can override the default port by setting the
`PORT`
[environment property](go-environment.md#go-options "go-environment.md#go-options") to the port on which your main application listens.

###### Note

The port that your application listens on doesn't affect the port that the nginx server listens to receive requests from the load balancer.

###### Configuring the proxy server on your platform version

All AL2023/AL2 platforms support a uniform proxy configuration feature.
For more information about configuring the proxy server on your platform versions
running AL2023/AL2,
see [Reverse proxy configuration](platforms-linux-extend.md "platforms-linux-extend.md").

###### Notes

- The information in this topic only applies to platform branches based on Amazon Linux AMI (AL1). AL2023/AL2 platform branches are incompatible with previous Amazon Linux AMI
  (AL1) platform versions and _require different configuration settings_.
- On [July 18, 2022](../relnotes/release-2022-07-18-linux-al1-retire.md "../relnotes/release-2022-07-18-linux-al1-retire.md"),
  Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**.
  For more information about migrating to a current and fully supported Amazon Linux 2023 platform branch, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md").
  If your Elastic Beanstalk Go environment uses an Amazon Linux AMI platform version (preceding Amazon Linux 2), read the information in this section.

Elastic Beanstalk uses nginx as the reverse proxy to map your application to your load balancer on port 80. If you want to provide your own nginx
configuration, you can override the default configuration provided by Elastic Beanstalk by including the `.ebextensions/nginx/nginx.conf`
file in your source bundle. If this file is present, Elastic Beanstalk uses it in place of the default nginx configuration file.

If you want to include directives in addition to those in the `nginx.conf`
`http` block, you can also provide additional configuration files in the `.ebextensions/nginx/conf.d/` directory of
your source bundle. All files in this directory must have the `.conf` extension.

To take advantage of functionality provided by Elastic Beanstalk, such as [Enhanced health reporting and monitoring in Elastic Beanstalk](health-enhanced.md "health-enhanced.md"), automatic
application mappings, and static files, you must include the following line in the `server` block of your nginx configuration
file:

```
include conf.d/elasticbeanstalk/*.conf;
```
