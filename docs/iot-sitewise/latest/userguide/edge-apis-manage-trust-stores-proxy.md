# Configure proxy support and manage

trust stores for AWS IoT SiteWise Edge

In AWS IoT SiteWise Edge, configure and manage trust stores to set up proxy support for your
edge devices. First, set up proxy configuration, then configure trust stores. You can
configure trust stores either during gateway installation or manually after your gateway
is established.

- **Proxies** – Facilitate connectivity
  between your edge devices and AWS services in various network
  environments.
- **Trust stores** – Ensure secure
  connections by managing trusted certificates. Proper configurations help you
  comply with your network security policies, enable communication in restricted
  network environments, and optimize data transfer between edge devices and cloud
  services.
  SiteWise Edge utilizes multiple trust stores for different component types, ensuring secure
  and efficient data flow from your edge devices to the cloud. You can configure trust
  stores and proxies on an existing gateway or during the installation process when
  creating a new gateway.

## Requirements

for trust store and proxy configurations

Before you configure a trust store or install SiteWise Edge with proxy settings, ensure
that you meet the prerequisites. There are varied implementation requirements based
on your component usage and functionality requirements.

###### Proxy support requirements

- The URL of your proxy server. The URL should include the user info, the
  port number for the host. For example,
  `scheme://[userinfo@]host[:port]`.
  - `scheme` – Must be HTTP or HTTPS
  - (Optional) `userinfo` – User name and password
    information
  - `host` – The host name or IP address of the
    proxy server
  - `port` – The port number

- A list of addresses to bypass the proxy.
- (Optional) The proxy CA certificate file if you're using an HTTPS proxy
  with a self-signed certificate.

###### Trust store requirements

- For full data processing pack functionality with HTTPS proxy, you should
  update all three trust stores.
- If you only use the IoT SiteWise OPC UA collector and IoT SiteWise publisher, update
  the certificates AWS IoT Greengrass Core and Java trust stores to the latest
  version.

## Best practices for trust

store and proxy server edge configurations

For ongoing maintenance and to maintain the highest level of security in your edge
environment:

- Regularly review and update proxy settings to align with your network
  security requirements.
- Monitor gateway connectivity and data flow to ensure proper proxy
  communication
- Maintain and update trust stores according to your organization's
  certificate management policies
- You can implement and follow our recommended best practices for secure
  communication in edge environments, such as:
- Document your proxy and trust store configurations for operational
  visibility
- Follow your organization's security practices for credential
  management

These practices help maintain secure and reliable operations for your SiteWise Edge
gateways while remaining aligned with your broader security policies.
