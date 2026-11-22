

# Restricted network environments

Deadline Cloud provides tools that are used by artists or other users on their local workstations. These tools require access to AWS API and web endpoints to perform their function. If you filter access to specific AWS domains or URL endpoints by using a web content filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG), you must add the following domains or URL endpoints to your web-content filtering solution allowlists. To configure a proxy or check connectivity in the Deadline Cloud monitor desktop application, see [Configure a proxy and check connectivity in the Deadline Cloud monitor desktop application](#monitor-network-settings).

## AWS API endpoints to allowlist
<a name="aws-api-endpoints"></a>

Deadline Cloud client tools, such as the AWS Management Console, monitor, CLI, and integrated submitters, require access to AWS APIs in addition to Deadline Cloud. These endpoints only support IPv4.
+ `scheduling.deadline.{{[Region]}}.amazonaws.com`
+ `management.deadline.{{[Region]}}.amazonaws.com`
+ `logs.{{[Region]}}.amazonaws.com`
+ `ec2.{{[Region]}}.amazonaws.com`
+ `s3.{{[Region]}}.amazonaws.com`
+ `sts.{{[Region]}}.amazonaws.com`
+ `identitystore.{{[Region]}}.amazonaws.com`

## Web domains to allowlist
<a name="web-domains"></a>

The Deadline Cloud monitor requires access to the following domains to operate. 

For additional information about allowlisting domains for AWS Sign-In, see [Domains to add to your allow list](https://docs.aws.amazon.com/signin/latest/userguide/allowlist-domains.html) in the *AWS Sign-In User Guide*.
+ `downloads.deadlinecloud.amazonaws.com`
+ `d2ev1rdnjzhmnr.cloudfront.net`
+ `prod.log.shortbread.aws.dev`
+ `prod.tools.shortbread.aws.dev`
+ `prod.log.shortbread.analytics.console.aws.a2z.com`
+ `prod.tools.shortbread.analytics.console.aws.a2z.com`
+ `global.help-panel.docs.aws.a2z.com`
+ `{{[Region]}}.signin.aws`
+ `{{[Region]}}.signin.aws.amazon.com`
+ `sso.{{[Region]}}.amazonaws.com`
+ `portal.sso.{{[Region]}}.amazonaws.com`
+ `oidc.{{[Region]}}.amazonaws.com`
+ `assets.sso-portal.{{[Region]}}.amazonaws.com`

## Environment-specific endpoints to allowlist
<a name="environment-specific-endpoints"></a>

These domains vary depending on the specific configuration of Deadline Cloud. If additional Deadline Cloud monitors or queues are created, additional domains will need to be allowlisted.
+ `{{[Directory ID or alias]}}.awsapps.com`

  This domain is tied to the IAM Identity Center setup and should be the same for all setups in this using the same IAM Identity Center instance. The exact value can be found by the enterprise admin in the IAM Identity Center console under *Settings* → *AWS access portal URL*.
+ `{{[Monitor alias]}}.{{[Region]}}.deadlinecloud.amazonaws.com`

  This domain is for the Monitor setup in Deadline Cloud. Artists enter this link into their browser or Deadline Cloud monitor application. If Deadline Cloud is set up in additional accounts or regions in the future, this domain will change. You can find this value in the Deadline Cloud console in the *Dashboard* → *Monitor overview* → *Monitor details* → *URL*. The URL is reachable from any location on the internet. For information about what the URL exposes and how Deadline Cloud authorizes access to farm data, see [Access to the monitor web application](security-data-flow.md#security-data-flow-monitor).
+ `{{[Bucket name]}}.{{[Region]}}.s3.amazonaws.com`

  This is the domain for the job attachments bucket used by Deadline Cloud queues. Each queue can have its own job attachments bucket configured. The exact bucket name can be found in the Deadline Cloud console under *Queues* → *Queue details* → *Job attachments*. For more information about job attachments, see the queues documentation.

## Configure a proxy and check connectivity in the Deadline Cloud monitor desktop application
<a name="monitor-network-settings"></a>

The Deadline Cloud monitor desktop application, version 1.3.1 or later, has a **Network Settings** window. In the window, you set the proxy, certificate bundle, and environment variables that the application and the Deadline Cloud CLI commands it runs use. You can also check that each endpoint on this page is reachable. If you start the application from Finder, the Dock, the Start menu, or a desktop launcher, it doesn't receive the variables that a shell profile exports. You can set them in the window instead of in a launch script.

To open the **Network Settings** window, start the Deadline Cloud monitor desktop application, then do one of the following:
+ In Windows or Linux, on the **File** menu, choose **Network Settings**.
+ In macOS, on the application menu, choose **Network Settings**. The application menu is named for the application and appears next to the Apple menu.

When the sign-in page can't reach an endpoint that sign-in needs, or the proxy configuration has an error, the page shows a warning that names the host and the likely fix. To open the window from the warning, choose **Network settings**.

### Proxy and environment settings
<a name="monitor-network-settings-proxy"></a>

The **Proxy** and **Environment variables** sections of the window list the following settings. Changes take effect when the application restarts. After you choose **Save**, choose **Restart now**.

The following screenshot shows the **Proxy** and **Environment variables** sections on macOS. The **Proxy URL** is `http://proxy.example.com:8080`, and **Bypass proxy for** is `.example.com,10.0.0.0/8`. The **CA bundle** is empty, and no environment variables are set. On macOS, the **Also use this proxy for the monitor window** checkbox is unavailable.

![The Proxy and Environment variables sections of the Network Settings window on macOS, with an example proxy URL and bypass list entered.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor-network-settings-proxy.png)


**Proxy URL**  
The proxy for HTTP and HTTPS connections, such as `http://proxy.example.com:8080`. Leave the field empty to use the operating system's proxy settings and any proxy variables that the application was started with.  
If your proxy requires a sign-in, add your proxy user name and password to the URL. In the following example, replace {{user}} with your proxy user name and {{password}} with your proxy password. Percent-encode special characters such as `@` and `:`.  
`http://{{user}}:{{password}}@proxy.example.com:8080`  
The application stores the password in the network settings file, which only your user account can read.  
The proxy URL can start with `http://` or `https://`, and the proxy can use Basic authentication. SOCKS proxies aren't supported.  
Proxies that require NT LAN Manager (NTLM) or Kerberos (Negotiate) authentication work only in the monitor window. For the application's other connections and the Deadline Cloud CLI, ask your IT team to allow the Deadline Cloud hosts without authentication.

**Bypass proxy for**  
A comma-separated list of hosts, domains, or IP ranges that connect directly, such as `.example.com,10.0.0.0/8`. The application always bypasses the proxy for `localhost`, `127.0.0.1`, `::1`, and the Amazon Elastic Compute Cloud instance metadata address. The application saves an entry such as `*.example.com` as `.example.com`, the form that both the application and the Deadline Cloud CLI match.

**CA bundle**  
A Privacy-Enhanced Mail (PEM) file of your organization's root certificates. The application gives the file to the Deadline Cloud CLI as `AWS_CA_BUNDLE`. Set the CA bundle when your network inspects Transport Layer Security (TLS) connections. The application and the monitor window use the operating system's certificate store instead, so also install your organization's root certificate there.

**Also use this proxy for the monitor window**  
Windows and Linux only. The monitor window follows the operating system's proxy settings, including automatic proxy configuration, so the setting is off by default. Turn it on only if the connectivity checks show that the monitor window can't reach a host. The setting requires an `http://` proxy URL that includes the port. In macOS, the monitor window always follows the proxy in **System Settings**, **Network**.

**Environment variables**  
Variables that the application sets for itself and for every Deadline Cloud CLI command that it runs, such as job downloads and job submission. You can't set the variables that the preceding fields or the application itself manage, or variables that change which programs or settings files the application uses.

The **Started with** section lists the proxy and certificate variables that the application inherited when it started, such as variables set by a launch script. To copy the proxy and CA bundle into the fields, choose **Use these values**, then choose **Save**. After you save, you no longer need the launch script.

### Settings that each connection follows
<a name="monitor-network-settings-connections"></a>

The Deadline Cloud monitor desktop application connects to AWS in several ways, and each way reads proxy and certificate settings from different places. As a result, a network can load the monitor window and still fail to sign in, or the reverse. The **Proxy URL** setting gives the same proxy to the application's connections, sign-in, and the Deadline Cloud CLI. The monitor window uses it only when you turn on **Also use this proxy for the monitor window**. The following table shows the settings that each connection type follows.


| Connection | Proxy URL and proxy environment variables | Operating system proxy settings | Automatic proxy configuration | Trusted certificates | 
| --- | --- | --- | --- | --- | 
| Monitor window, which displays the monitor and makes all of its requests | On Windows and Linux, when you turn on **Also use this proxy for the monitor window**. On Linux, also through libproxy when it's installed. | Yes | Yes | Operating system store | 
| Application connections, such as checking the monitor URL, update checks, and software downloads | Yes | Manually configured proxy on macOS and Windows | No | Operating system store | 
| Sign-in with a local profile or a console sign-in profile | Yes | No, for the AWS credential requests that sign-in makes | No | Operating system store, or the file in `SSL_CERT_FILE` if set | 
| Deadline Cloud CLI commands, such as job downloads and job submission | Yes | Manually configured proxy on macOS and Windows | No | The **CA bundle** file if set, otherwise the CLI's own certificate bundle | 

If your network uses automatic proxy configuration, such as a proxy auto-config (PAC) file or Web Proxy Auto-Discovery (WPAD), only the monitor window follows it. Ask your IT team which proxy the configuration returns for AWS hosts, and enter that proxy in **Proxy URL**.

### Connectivity checks
<a name="monitor-network-settings-checks"></a>

To check each endpoint that the application uses, choose **Run checks** in the **Connectivity checks** section. The checks cover the endpoints on this page for each saved monitor and its Region. Each endpoint is checked a step at a time: Domain Name System (DNS) lookup, connection, proxy, TLS handshake, and response. For each failure, the checks show the step that failed, the likely cause, and a fix. The summary counts only endpoints with an **Error** status as unreachable. An endpoint with a **Warning** status, such as one where your network inspects connections, is still reachable.

The following screenshot shows the results on a network where a proxy re-signs secure connections. Each of the eight endpoints, from `management.deadline.us-west-2.amazonaws.com` to `downloads.deadlinecloud.amazonaws.com`, has a **Warning** status and the route `Proxy http://proxy.example.com:8080`. The details for each endpoint say that secure connections are inspected, name the issuer Example Corp Root CA, and suggest setting the CA bundle. The summary still reports that all endpoints are reachable.

![Connectivity check results with a Warning status on every endpoint, because the network inspects secure connections.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor-network-settings-checks.png)


The checks also do the following:
+ Detect TLS inspection. AWS endpoints use certificates issued by Amazon Trust Services. A certificate from any other issuer means that your network re-signs secure connections. The checks name the issuer and tell you whether to set the **CA bundle**.
+ Check whether the monitor window reaches the hosts that it uses, and tell you when the application reaches a host that the monitor window can't.
+ Compare the computer's clock with AWS. AWS rejects requests when the computer's clock is more than 5 minutes off.
+ Show the operating system's proxy settings and the proxy that the application uses, and flag proxy configuration problems, such as proxy environment variables that conflict with each other.

To share the results with your IT team or AWS Support, choose **Copy report**.