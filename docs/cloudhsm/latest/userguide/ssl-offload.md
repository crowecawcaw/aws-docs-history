# Improve your web server security with SSL/TLS offload in AWS CloudHSM

Web servers and their clients (web browsers) can use Secure Sockets Layer (SSL) or Transport Layer Security (TLS) protocols
to confirm the identity of the web server and establish a secure connection that sends and receives webpages or other data over the internet.
This is commonly known as HTTPS. The web server uses a public–private key pair and an SSL/TLS public key certificate to establish an HTTPS session with each client.
This process involves a lot of computation for web servers, but you can offload some of this to your AWS CloudHSM cluster, which is referred to as SSL acceleration.
Offloading reduces the computational burden on your web servers and provides extra security by storing servers’ private keys in HSMs.

The following topics provide an overview of how SSL/TLS offload with AWS CloudHSM works and
tutorials for setting up SSL/TLS offload with AWS CloudHSM on the following platforms.

For **Linux**, use OpenSSL Dynamic Engine on the [NGINX](https://nginx.org/en/ "https://nginx.org/en/") or [Apache HTTP Server](https://httpd.apache.org/ "https://httpd.apache.org/") web server software

For **Windows**, use the [Internet Information Services (IIS) for Windows Server](https://www.iis.net/ "https://www.iis.net/")
web server software

###### Topics

- [How SSL/TLS offload with AWS CloudHSM works](ssl-offload-overview.md "ssl-offload-overview.md")
- [AWS CloudHSM SSL/TLS offload on Linux using NGINX or
  Apache with OpenSSL](third-offload-linux-openssl.md "third-offload-linux-openssl.md")
- [AWS CloudHSM SSL/TLS offload on Linux using NGINX or HAProxy with OpenSSL Provider](third-offload-linux-openssl-provider.md "third-offload-linux-openssl-provider.md")
- [AWS CloudHSM SSL/TLS offload on Linux using Tomcat with JSSE](third-offload-linux-jsse.md "third-offload-linux-jsse.md")
- [AWS CloudHSM SSL/TLS offload on Windows using IIS with KSP](ssl-offload-windows.md "ssl-offload-windows.md")
- [Add a load balancer with ELB for AWS CloudHSM(optional)](third-offload-add-lb.md "third-offload-add-lb.md")
