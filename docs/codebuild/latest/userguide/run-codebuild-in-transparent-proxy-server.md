# Run CodeBuild in a transparent

proxy server

To run AWS CodeBuild in a transparent proxy server, you must configure the proxy server
with access to the websites and domains it interacts with.

###### Topics

- [Configure Squid as a
  transparent proxy server](#use-proxy-server-transparent-squid-configure "#use-proxy-server-transparent-squid-configure")
- [Create a CodeBuild
  project](#use-proxy-server-transparent-create-acb-project "#use-proxy-server-transparent-create-acb-project")

## Configure Squid as a

transparent proxy server

To configure a proxy server to be transparent, you must grant it access to the
domains and websites you want it to access. To run AWS CodeBuild with a transparent
proxy server, you must grant it access to `amazonaws.com`. You must also
grant access to other websites CodeBuild uses. These vary, depending on how you create
your CodeBuild projects. Example websites are those for repositories such as GitHub,
Bitbucket, Yum, and Maven. To grant Squid access to specific domains and websites,
use a command similar to the following to update the `squid.conf`
file. This sample command grants access to `amazonaws.com`,
`github.com`, and `bitbucket.com`. You can edit this
sample to grant access to other websites.

```
cat | sudo tee /etc/squid/squid.conf ≪EOF
visible_hostname squid
#Handling HTTP requests
http_port 3129 intercept
acl allowed_http_sites dstdomain .amazonaws.com
#acl allowed_http_sites dstdomain `domain_name` [uncomment this line to add another domain]
http_access allow allowed_http_sites
#Handling HTTPS requests
https_port 3130 cert=/etc/squid/ssl/squid.pem ssl-bump intercept
acl SSL_port port 443
http_access allow SSL_port
acl allowed_https_sites ssl::server_name .amazonaws.com
acl allowed_https_sites ssl::server_name .github.com
acl allowed_https_sites ssl::server_name .bitbucket.com
#acl allowed_https_sites ssl::`server_name` [uncomment this line to add another website]
acl step1 at_step SslBump1
acl step2 at_step SslBump2
acl step3 at_step SslBump3
ssl_bump peek step1 all
ssl_bump peek step2 allowed_https_sites
ssl_bump splice step3 allowed_https_sites
ssl_bump terminate step2 all
http_access deny all
EOF
```

Incoming requests from instances in the private subnet must redirect to the Squid
ports. Squid listens on port 3129 for HTTP traffic (instead of 80) and 3130 for
HTTPS traffic (instead of 443). Use the **iptables** command to route
traffic:

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 3129
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 3130
sudo service iptables save
sudo service squid start
```

## Create a CodeBuild

project

After you configure your proxy server, you can use it with AWS CodeBuild in a private
subnet without more configuration. Every HTTP and HTTPS request goes through the
public proxy server. Use the following command to view the Squid proxy access log:

```
sudo tail -f /var/log/squid/access.log
```
