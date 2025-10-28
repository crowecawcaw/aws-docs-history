# Configuring the proxy server

Elastic Beanstalk can use NGINX or Apache
HTTPD as the reverse proxy to map your application to your Elastic Load Balancing load balancer on port 80. The default is NGINX. Elastic Beanstalk
provides a default proxy configuration that you can either extend or completely override with your own configuration.

By default, Elastic Beanstalk configures the proxy to forward requests to your application on port 5000. You can override the default port by setting the
`PORT`
[environment property](create_deploy_nodejs.md#nodejs-platform-console "create_deploy_nodejs.md#nodejs-platform-console") to the port that your main application listens on.

###### Note

The port that your application listens on doesn't affect the port that the NGINX server listens to receive requests from the load
balancer.

###### Configuring the proxy server on your platform version

All AL2023/AL2 platforms support a uniform proxy configuration feature.
For more information about configuring the proxy server on your platform versions
running AL2023/AL2,
see [Reverse proxy configuration](platforms-linux-extend.md "platforms-linux-extend.md").

If your Elastic Beanstalk Node.js environment uses an Amazon Linux AMI platform version (preceding Amazon Linux 2), read the information in this section.

###### Notes

- The information in this topic only applies to platform branches based on Amazon Linux AMI (AL1). AL2023/AL2 platform branches are incompatible with previous Amazon Linux AMI
  (AL1) platform versions and _require different configuration settings_.
- On [July 18, 2022](../relnotes/release-2022-07-18-linux-al1-retire.md "../relnotes/release-2022-07-18-linux-al1-retire.md"),
  Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**.
  For more information about migrating to a current and fully supported Amazon Linux 2023 platform branch, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md").
  The Node.js platform uses a reverse proxy to relay requests from port 80 on the instance to your application that's listening
  on port 8081. Elastic Beanstalk provides a default proxy configuration that you can either extend or completely override with your own configuration.

To extend the default configuration, add `.conf` files to `/etc/nginx/conf.d` with a configuration file.
For a specific example, see [Terminating HTTPS on EC2 instances running
Node.js](https-singleinstance-nodejs.md "https-singleinstance-nodejs.md").

The Node.js platform sets the PORT environment variable to the port that the proxy server passes traffic to.
Read this variable in your code to configure the port for your application.

```
    var port = process.env.PORT || 3000;

    var server = app.listen(port, function () {
        console.log('Server running at http://127.0.0.1:' + port + '/');
    });
```

The default NGINX configuration forwards traffic to an upstream server that's named `nodejs` at
`127.0.0.1:8081`. It's possible to remove the default configuration and provide your own in a [configuration file](ebextensions.md "ebextensions.md").

###### Example .ebextensions/proxy.config

The following example removes the default configuration and adds a custom configuration that forwards traffic to port 5000, instead of 8081.

```
files:
  /etc/nginx/conf.d/proxy.conf:
    mode: "000644"
    owner: root
    group: root
    content: |
      `upstream nodejs {
 server 127.0.0.1:5000;
 keepalive 256;
 }`

      server {
        listen 8080;

        if ($time_iso8601 ~ "^(\d{4})-(\d{2})-(\d{2})T(\d{2})") {
            set $year $1;
            set $month $2;
            set $day $3;
            set $hour $4;
        }
        access_log /var/log/nginx/healthd/application.log.$year-$month-$day-$hour healthd;
        access_log  /var/log/nginx/access.log  main;

        location / {
            proxy_pass  http://nodejs;
            proxy_set_header   Connection "";
            proxy_http_version 1.1;
            proxy_set_header        Host            $host;
            proxy_set_header        X-Real-IP       $remote_addr;
            proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        gzip on;
        gzip_comp_level 4;
        gzip_types text/html text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;

        location /static {
            alias /var/app/current/static;
        }

      }

  /opt/elasticbeanstalk/hooks/configdeploy/post/99_kill_default_nginx.sh:
    mode: "000755"
    owner: root
    group: root
    content: |
      #!/bin/bash -xe
      rm -f /etc/nginx/conf.d/00_elastic_beanstalk_proxy.conf
      service nginx stop
      service nginx start

container_commands:
  removeconfig:
    command: "rm -f /tmp/deployment/config/#etc#nginx#conf.d#00_elastic_beanstalk_proxy.conf /etc/nginx/conf.d/00_elastic_beanstalk_proxy.conf"
```

The example configuration (`/etc/nginx/conf.d/proxy.conf`) uses the default configuration at
`/etc/nginx/conf.d/00_elastic_beanstalk_proxy.conf` as a base to include the default server block with compression and log
settings, and a static file mapping.

The `removeconfig` command removes the default configuration for the container so that the proxy server uses the custom
configuration. Elastic Beanstalk recreates the default configuration when each configuration is deployed. To account for this, in the following example, a
post-configuration-deployment hook (`/opt/elasticbeanstalk/hooks/configdeploy/post/99_kill_default_nginx.sh`) is added. This
removes the default configuration and restarts the proxy server.

###### Note

The default configuration might change in future versions of the Node.js platform. Use the latest version of the
configuration as a base for your customizations to ensure compatibility.

If you override the default configuration, you must define any static file mappings and GZIP compression. This is because the
platform can't apply the [standard settings](create_deploy_nodejs.md#nodejs-namespaces "create_deploy_nodejs.md#nodejs-namespaces").
