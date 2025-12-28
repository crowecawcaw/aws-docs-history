# Reverse proxy configuration

All Amazon Linux 2 and Amazon Linux 2023 platform versions use nginx as their default reverse proxy server. The Tomcat, Node.js, PHP, and Python platform also
support Apache HTTPD as an alternative. To select Apache on these platforms, set the `ProxyServer` option in the
`aws:elasticbeanstalk:environment:proxy` namespace to `apache`. All platforms enable proxy server configuration in a uniform way,
as described in this section.

###### Note

On Amazon Linux AMI platform versions (preceding Amazon Linux 2) you might have to configure proxy servers differently. You can find these legacy details under the
[respective platform topics](concepts-all-platforms.md "concepts-all-platforms.md") in this guide.

Elastic Beanstalk configures the proxy server on your environment's instances to forward web traffic to the main web application on the root URL of the
environment; for example, `http://my-env.elasticbeanstalk.com`.

By default, Elastic Beanstalk configures the proxy to forward requests coming in on port 80 to your main web application on port 5000. You can configure this port
number by setting the `PORT` environment property using the [aws:elasticbeanstalk:application:environment](command-options-general.md#command-options-general-elasticbeanstalkapplicationenvironment "command-options-general.md#command-options-general-elasticbeanstalkapplicationenvironment") namespace in a configuration file, as shown in the following example.

```
option_settings:
  - namespace:  aws:elasticbeanstalk:application:environment
    option_name:  PORT
    value:  `<main_port_number>`
```

For more information about setting environment variables for your application, see [Option settings](ebextensions-optionsettings.md "ebextensions-optionsettings.md").

Your application should listen on the port that is configured for it in the proxy. If you change the default port using the `PORT`
environment property, your code can access it by reading the value of the `PORT` environment variable. For example, call
`os.Getenv("PORT")` in Go, or `System.getenv("PORT")` in Java. If you configure your proxy to send traffic to multiple application
processes, you can configure several environment properties, and use their values in both proxy configuration and your application code. Another option is
to pass the port value to the process as a command argument in the `Procfile`. For more information see [Buildfile and Procfile](platforms-linux-extend.md "platforms-linux-extend.md").

## Configuring nginx

Elastic Beanstalk uses nginx as the default reverse proxy to map your application to your Elastic Load Balancing load balancer. Elastic Beanstalk provides a default nginx configuration
that you can extend or override completely with your own configuration.

###### Note

When you add or edit an nginx `.conf` configuration file, be sure to encode it as UTF-8.

To extend the Elastic Beanstalk default nginx configuration, add `.conf` configuration files to a folder named
`.platform/nginx/conf.d/` in your application source bundle. The Elastic Beanstalk nginx configuration includes `.conf`
files in this folder automatically.

```
~/workspace/my-app/
|-- .platform
|   `-- nginx
|       `-- conf.d
|           `-- myconf.conf
`-- `other source files`
```

Configuration files in `.platform/nginx/conf.d/` are included in the `http` block of the nginx configuration. Use this
location for configurations that apply globally.

To extend the default nginx `server` block configuration, add `.conf` configuration files to a folder named
`.platform/nginx/conf.d/elasticbeanstalk/` in your application source bundle. The Elastic Beanstalk nginx configuration includes
`.conf` files in this folder within the `server` block.

```
~/workspace/my-app/
|-- .platform
|   `-- nginx
|       `-- conf.d
|           `-- elasticbeanstalk
|               `-- server.conf
`-- `other source files`
```

Use this location to add server-specific configurations, such as additional location blocks, custom error pages, or server-level directives. The
following example adds a custom location block.

###### Example .platform/nginx/conf.d/elasticbeanstalk/server.conf

```
location /test {
    return 200 "Hello World!";
    add_header Content-Type text/plain;
}
```

To override the Elastic Beanstalk default nginx configuration completely, include a configuration in your source bundle at
`.platform/nginx/nginx.conf`:

```
~/workspace/my-app/
|-- .platform
|   `-- nginx
|       `-- nginx.conf
`-- `other source files`
```

If you override the Elastic Beanstalk nginx configuration, add the following line to your `nginx.conf` to pull in the Elastic Beanstalk configurations
for [Enhanced health reporting and monitoring in Elastic Beanstalk](health-enhanced.md "health-enhanced.md"), automatic application mappings, and static files.

```
 include conf.d/elasticbeanstalk/*.conf;
```

## Configuring Apache HTTPD

The Tomcat, Node.js, PHP, and Python platforms allow you to choose the Apache HTTPD proxy server as an alternative to nginx. This isn't the default.
The following example configures Elastic Beanstalk to use Apache HTTPD.

###### Example .ebextensions/httpd-proxy.config

```
option_settings:
  aws:elasticbeanstalk:environment:proxy:
    ProxyServer: apache
```

You can extend the Elastic Beanstalk default Apache configuration with your additional configuration files. Alternatively, you can override the Elastic Beanstalk default
Apache configuration completely.

To extend the Elastic Beanstalk default Apache configuration, add `.conf` configuration files to a folder named
`.platform/httpd/conf.d` in your application source bundle. The Elastic Beanstalk Apache configuration includes `.conf`
files in this folder automatically.

```
~/workspace/my-app/
|-- .ebextensions
|   -- httpd-proxy.config
|-- .platform
|   -- httpd
|      -- conf.d
|         -- port5000.conf
|         -- ssl.conf
-- index.jsp
```

For example, the following Apache 2.4 configuration adds a listener on port 5000.

###### Example .platform/httpd/conf.d/port5000.conf

```
listen 5000
<VirtualHost *:5000>
  <Proxy *>
    Require all granted
  </Proxy>
  ProxyPass / http://localhost:8080/ retry=0
  ProxyPassReverse / http://localhost:8080/
  ProxyPreserveHost on

  ErrorLog /var/log/httpd/elasticbeanstalk-error_log
</VirtualHost>
```

To override the Elastic Beanstalk default Apache configuration completely, include a configuration in your source bundle at
`.platform/httpd/conf/httpd.conf`.

```
~/workspace/my-app/
|-- .ebextensions
|   -- httpd-proxy.config
|-- .platform
|   `-- httpd
|       `-- conf
|           `-- httpd.conf
`-- index.jsp
```

###### Note

If you override the Elastic Beanstalk Apache configuration, add the following lines to your `httpd.conf` to pull in the Elastic Beanstalk
configurations for [Enhanced health reporting and monitoring in Elastic Beanstalk](health-enhanced.md "health-enhanced.md"), automatic application mappings, and static files.

```
IncludeOptional conf.d/elasticbeanstalk/*.conf
```
