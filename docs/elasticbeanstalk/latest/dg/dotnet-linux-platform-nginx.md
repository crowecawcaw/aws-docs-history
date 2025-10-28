# Configuring the proxy server

AWS Elastic Beanstalk uses [NGINX](https://www.nginx.com/ "https://www.nginx.com/") as the reverse proxy to relay requests to your application. Elastic Beanstalk provides a default
NGINX configuration that you can either extend or override completely with your own configuration.

By default, Elastic Beanstalk configures the NGINX proxy to forward requests to your application on port 5000. You can override the default port by setting the
`PORT`
[environment property](dotnet-linux-platform.md#dotnet-linux-options-properties "dotnet-linux-platform.md#dotnet-linux-options-properties") to the port on which your main application listens.

###### Note

The port that your application listens on doesn't affect the port that the NGINX server listens on to receive requests from the load
balancer.

###### Configuring the proxy server on your platform version

All AL2023/AL2 platforms support a uniform proxy configuration feature.
For more information about configuring the proxy server on your platform versions
running AL2023/AL2,
see [Reverse proxy configuration](platforms-linux-extend.md "platforms-linux-extend.md").

The following example configuration file extends your environment's NGINX configuration. The configuration directs requests to `/api` to a second
web application that listens on port 5200 on the web server. By default, Elastic Beanstalk forwards requests to a single application that listens on port 5000.

###### Example `01_custom.conf`

```
location /api {
     proxy_pass          http://127.0.0.1:5200;
     proxy_http_version  1.1;

     proxy_set_header   Upgrade $http_upgrade;
     proxy_set_header   Connection $http_connection;
     proxy_set_header   Host $host;
     proxy_cache_bypass $http_upgrade;
     proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
     proxy_set_header   X-Forwarded-Proto $scheme;
}
```
