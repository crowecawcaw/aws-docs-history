# Configure proxy settings during

AWS IoT SiteWise Edge gateway installation

You can configure AWS IoT SiteWise Edge to work with a proxy server during gateway
installation. The installation script supports both HTTP and HTTPS proxies and can
automatically configure trust stores for secure proxy connections.

When you run the installation script with proxy settings, it performs several
important tasks:

- Validates the proxy URL format and parameters to ensure they are correctly
  specified.
- Downloads and installs required dependencies through the configured
  proxy.
- If a proxy CA certificate is provided, it's appended to the AWS IoT Greengrass root CA
  certificate and imported into the Java KeyStore.
- Configures AWS IoT Greengrass (which SiteWise Edge uses) to use the proxy for all outbound
  connections.
- Completes the SiteWise Edge installation with the appropriate proxy and trust
  store configurations.

###### To configure proxy settings when installing gateway software

1. Create a SiteWise Edge gateway. For more information, see [Create a self-hosted SiteWise Edge gateway](create-gateway-ggv2.md "create-gateway-ggv2.md") and
   [Install the AWS IoT SiteWise Edge
   gateway software on your local device](install-gateway-software-on-local-device.md "install-gateway-software-on-local-device.md").
2. Run the installation script with the appropriate proxy settings for your
   environment. Replace the placeholders with your specific proxy information

Replace each of the following items:

    * `-p`, `--proxy-url` – The URL of the
     proxy server. The URL must be either `http` or
     `https`.
    * `-n`, `--no-proxy` – A
     comma-separated list of addresses to bypass the proxy.
    * (Optional)`-c`, `--proxy-ca-cert` –
     Path to the proxy CA certificate file.
    * (Optional)`-j`, `--javastorepass` –
     The Java KeyStore password. The default password is
     `changeit`.

Linux
For Linux systems, use the following command structure:

```
sudo ./install.sh -p `proxy-url` -n `no-proxy-addresses` [-c `proxy-ca-cert-path`] [-j `javastorepass`]
```

Windows
For Microsoft Windows systems using PowerShell,
use this command structure:

```
.\install.ps1 -ProxyUrl `proxy-url` -NoProxyAddresses `no-proxy-addresses` [-ProxyCaCertPath `proxy-ca-cert-path`] [-JavaStorePass `javastorepass`]
```

## Troubleshooting during proxy-enabled installation

For more information on resolving trust store issues related to a SiteWise Edge
gateway, see [Proxy-enabled installation
issues](troubleshooting-gateway.md#troubleshoot-proxy-during-installation "troubleshooting-gateway.md#troubleshoot-proxy-during-installation").
