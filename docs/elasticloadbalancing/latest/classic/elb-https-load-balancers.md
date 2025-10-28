# HTTPS listeners for your Classic Load Balancer

You can create a load balancer that uses the SSL/TLS protocol for encrypted connections
(also known as _SSL offload_). This feature enables traffic encryption
between your load balancer and the clients that initiate HTTPS sessions, and for connections
between your load balancer and your EC2 instances.

Elastic Load Balancing uses Secure Sockets Layer (SSL) negotiation configurations, known as
_security policies_, to negotiate connections between the clients and
the load balancer. When you use HTTPS/SSL for your front-end connections, you can use either
a predefined security policy or a custom security policy. You must deploy an SSL certificate
on your load balancer. The load balancer uses this certificate to terminate the connection
and then decrypt requests from clients before sending them to the instances. The load
balancer uses a static cipher suite for back-end connections. You can optionally choose to
enable authentication on your instances.

Classic Load Balancers do not support Server Name Indication (SNI). You can use one
of the following alternatives instead:

- Deploy one certificate on the load balancer, and add a Subject Alternative Name
  (SAN) for each additional website. SANs enable you to protect multiple host names
  using a single certificate. Check with your certificate provider for more
  information about the number of SANs they support per certificate and how to add and
  remove SANs.
- Use TCP listeners on port 443 for the front-end and back-end connections. The load
  balancer passes the request through as is, so you can handle HTTPS termination on
  the EC2 instance.
  Classic Load Balancers do not support mutual TLS authentication (mTLS). For mTLS support, create a TCP
  listener. The load balancer passes the request through as is, so you can implement mTLS on
  the EC2 instance.

###### Contents

- [SSL/TLS certificates](ssl-server-cert.md "ssl-server-cert.md")
- [SSL negotiation configurations](elb-ssl-security-policy.md "elb-ssl-security-policy.md")
- [Predefined SSL security policies](elb-security-policy-table.md "elb-security-policy-table.md")
- [Create an HTTPS load balancer](elb-create-https-ssl-load-balancer.md "elb-create-https-ssl-load-balancer.md")
- [Configure an HTTPS listener](elb-add-or-delete-listeners.md "elb-add-or-delete-listeners.md")
- [Replace the SSL certificate](elb-update-ssl-cert.md "elb-update-ssl-cert.md")
- [Update the SSL negotiation
  configuration](ssl-config-update.md "ssl-config-update.md")
