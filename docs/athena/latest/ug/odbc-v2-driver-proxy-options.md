

# Proxy options
<a name="odbc-v2-driver-proxy-options"></a>

## Proxy host
<a name="odbc-v2-driver-proxy-options-proxy-host"></a>

If you require users to go through a proxy, use this parameter to set the proxy host. This parameter corresponds to the `ClientConfiguration.proxyHost` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| ProxyHost | Optional | none | ProxyHost=127.0.0.1; | 

## Proxy port
<a name="odbc-v2-driver-proxy-options-proxy-port"></a>

Use this parameter to set the proxy port. This parameter corresponds to the `ClientConfiguration.proxyPort` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| ProxyPort | Optional | none | ProxyPort=8888; | 

## Proxy user name
<a name="odbc-v2-driver-proxy-options-proxy-username"></a>

Use this parameter to set the proxy user name. This parameter corresponds to the `ClientConfiguration.proxyUserName` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| ProxyUID | Optional | none | ProxyUID=username; | 

## Proxy password
<a name="odbc-v2-driver-proxy-options-proxy-password"></a>

Use this parameter to set the proxy password. This parameter corresponds to the `ClientConfiguration.proxyPassword` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| ProxyPWD | Optional | none | ProxyPWD=password; | 

## Non proxy host
<a name="odbc-v2-driver-proxy-options-non-proxy-host"></a>

Use this optional parameter to specify a host that the driver connects to without using a proxy. This parameter corresponds to the `ClientConfiguration.nonProxyHosts` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.

The driver passes this value to the AWS SDK client configuration and applies it to HTTP clients that the SDK creates internally. On Linux and macOS, the SDK forwards the value to the `CURLOPT_NOPROXY` curl option. For information about the `CURLOPT_NOPROXY` format, see [CURLOPT\_NOPROXY](https://curl.se/libcurl/c/CURLOPT_NOPROXY.html) in the curl documentation.

**Windows behavior**  <a name="odbc-v2-driver-proxy-options-non-proxy-host-windows"></a>
In driver version 2.4.0.0, this parameter has no effect on Windows. The Windows HTTP client does not apply a proxy bypass list, so the driver routes all traffic through the proxy that you specify in `ProxyHost`.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| NonProxyHost | Optional | none. See [Windows behavior](#odbc-v2-driver-proxy-options-non-proxy-host-windows). | NonProxyHost=.amazonaws.com,localhost,.example.net,.example.com; | 

## Use proxy
<a name="odbc-v2-driver-proxy-options-use-proxy"></a>

Enables the specified proxy for AWS SDK service clients and HTTP clients that the AWS SDK creates internally. In driver version 2.4.0.0, the driver also applies this proxy to both driver-owned and SDK-created identity provider HTTP clients, even when `UseProxyForIdP` is set to `0`.

**Process-wide settings for concurrent connections**  
Proxy and CA settings applied to SDK-created clients are process-wide. If you use different DSNs for multiple connections at the same time, the settings from your most recently initialized connection apply to subsequently created SDK-internal HTTP clients.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| UseProxy | Optional | none | UseProxy=1; | 