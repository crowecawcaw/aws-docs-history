# Configuring a firewall, proxy server, or data perimeter for Amazon Q Developer

If you're using a firewall, proxy server, or [data perimeter](https://aws.amazon.com/identity/data-perimeters-on-aws/ "https://aws.amazon.com/identity/data-perimeters-on-aws/"), make sure to
allowlist traffic to the following URLs and Amazon Resource Names (ARNs) so that Amazon Q works as
expected.

## General URLs to allowlist

In the following URLs, replace:

- `idc-directory-id-or-alias` with your IAM Identity Center instance's
  directory ID or alias. For more information about IAM Identity Center, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the
  _AWS IAM Identity Center User Guide_.
- `sso-region` with the AWS Region where your IAM Identity Center instance is
  enabled. For more information, see [IAM Identity Center Regions supported by Amazon Q Developer](q-admin-setup-subscribe-regions.md#pro-subscription-regions "q-admin-setup-subscribe-regions.md#pro-subscription-regions").
- `profile-region` with the AWS Region where your Amazon Q Developer
  profile is installed. For more information about the Amazon Q Developer profile, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md "subscribe-understanding-profile.md") and [Supported Regions for the Q Developer console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions "q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions").

| URL                                                      | Purpose                                            |
| -------------------------------------------------------- | -------------------------------------------------- |
| ``idc-directory-id-or-alias`.awsapps.com`                | Authentication                                     |
| `oidc.`sso-region`.amazonaws.com`                        | Authentication                                     |
| `*.sso.`sso-region`.amazonaws.com`                       | Authentication                                     |
| `*.sso-portal.`sso-region`.amazonaws.com`                | Authentication                                     |
| `*.aws.dev`                                              | Authentication                                     |
| `*.awsstatic.com`                                        | Authentication                                     |
| `*.console.aws.a2z.com`                                  | Authentication                                     |
| `*.sso.amazonaws.com`                                    | Authentication                                     |
| `https://codewhisperer.us-east-1.amazonaws.com`          | Amazon Q Developer features                        |
| `https://q.`profile-region`.amazonaws.com`               | Amazon Q Developer features                        |
| `https://idetoolkits-hostedfiles.amazonaws.com/*`        | Amazon Q Developer in the IDE, configuration       |
| `https://idetoolkits.amazonwebservices.com/*`            | Amazon Q Developer in the IDE, endpoints           |
| `q-developer-integration.us-east-1.api.aws`              | Amazon Q Developer in the IDE, endpoints           |
| `https://aws-toolkit-language-servers.amazonaws.com/*`   | Amazon Q Developer in the IDE, language processing |
| `https://aws-language-servers.us-east-1.amazonaws.com/*` | Amazon Q Developer in the IDE, language processing |
| `https://client-telemetry.us-east-1.amazonaws.com`       | Amazon Q Developer in the IDE, telemetry           |
| `cognito-identity.us-east-1.amazonaws.com`               | Amazon Q Developer in the IDE, telemetry           |

## Amazon S3 bucket URLs and ARNs to allowlist

For some features, Amazon Q uploads artifacts to AWS service-owned Amazon S3 buckets. If you are
using data perimeters to control access to Amazon S3 in your environment, you might need to explicitly
allow access to these buckets to use the corresponding Amazon Q features.

The following table lists the URL and ARN of each of the Amazon S3 buckets that Amazon Q requires
access to, and the features that use each bucket. You can use the bucket URL or bucket ARN to
allowlist these buckets, depending on how you control access to Amazon S3.

You only need to allowlist the bucket in the AWS Region where the Amazon Q Developer profile is
installed. For more information about the Amazon Q Developer profile, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md "subscribe-understanding-profile.md").

| Amazon S3 bucket URL and ARN                                                                                                                                                                                                                                                                                                                                          | Purpose                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia):<br>• `https://amazonq-code-scan-us-east-1-29121b44f7b.s3.amazonaws.com/`<br>• `arn:aws:s3:::amazonq-code-scan-us-east-1-29121b44f7b`<br>Europe (Frankfurt):<br>• `https://amazonq-code-scan-eu-central-1-9374e402cc5.s3.amazonaws.com/`<br>• `arn:aws:s3:::amazonq-code-scan-eu-central-1-9374e402cc5`                                         | An Amazon S3 bucket used to upload artifacts for [Amazon Q code reviews](code-reviews.md "code-reviews.md")                       |
| US East (N. Virginia):<br>• `https://amazonq-code-transformation-us-east-1-c6160f047e0.s3.amazonaws.com/`<br>• `arn:aws:s3:::amazonq-code-transformation-us-east-1-c6160f047e0`<br>Europe (Frankfurt):<br>• `https://amazonq-code-transformation-eu-central-1-a0a89cc2b94.s3.amazonaws.com/`<br>• `arn:aws:s3:::amazonq-code-transformation-eu-central-1-a0a89cc2b94` | An Amazon S3 bucket used to upload artifacts for [Amazon Q code transformations](code-transformation.md "code-transformation.md") |

## Configuring a corporate proxy in Amazon Q

If your end users are working behind a corporate proxy, have them complete the following steps
to successfully connect to Amazon Q.

### Step 1: Configuring proxy settings in your IDE

Specify your proxy server's URL in your IDE.

###### Note

SOCKS proxies and Proxy Auto-Configuration (PAC) files are not supported. You must
manually configure an HTTP or HTTPS proxy using the instructions that follow.

Eclipse

1. In Eclipse, open **Preferences** as follows:
   - On Windows or Ubuntu:
     - From the Eclipse menu bar, choose
       **Window**, and then choose
       **Preferences**.

   - On macOS:
     - From the menu bar, choose **Eclipse**,
       and then choose **Settings** or
       **Preferences** depending on your
       macOS version.

2. In the search bar, enter `Amazon Q` and open Amazon Q.
3. Under **Proxy Settings**, set **HTTPS Proxy
   URL** to your corporate proxy URL.

Examples: `http://proxy.company.com:8080`,
`https://proxy.company.com:8443` 4. Leave the Amazon Q settings open and go to the next step.

JetBrains
In JetBrains, manually configure your proxy server's host name and port following
the guidance in the [HTTP
Proxy](https://www.jetbrains.com/help/idea/settings-http-proxy.html "https://www.jetbrains.com/help/idea/settings-http-proxy.html") topic of the IntelliJ IDEA documentation.

Visual Studio

1. From the Visual Studio main menu, choose **Tools**,
   then choose **Options**.
2. From the **Options** menu, expand **AWS
   Toolkit**, then choose **Proxy**.
3. From the **Proxy** menu, set **Host**
   and **Port** to your corporate proxy host and
   port.

Examples: `http://proxy.company.com:8080`,
`https://proxy.company.com:8443`

Visual Studio Code

1. From VS Code, open VS Code **Settings** by pressing
   `CMD + ,` (Mac) or `Ctrl +
,` (Windows/Linux).
2. From the **Settings** search bar, enter
   `Http: Proxy`, then locate it in the search
   results.
3. Enter your corporate proxy URL.

Examples: `http://proxy.company.com:8080`,
`https://proxy.company.com:8443` 4. (Optional) in the **Settings** search bar, enter
`HTTP: No Proxy`, then locate it in the
results. 5. Choose the **Add Item** button, then add domains that
bypass the proxy, separated by commas.

### Step 2: Configuring SSL certificate handling

Amazon Q automatically detects and uses the trusted certificates installed on your system. If
you are experiencing certificate errors, you must manually specify a certificate bundle by
completing the following procedure.

###### Note

The following are situations where manual configuration is required.

- You are encountering certificate-related errors after configuring the
  proxy.
- Your corporate proxy uses certificates that aren't in your system's trust
  store.
- Amazon Q fails to automatically detect your corporate certificates.

Eclipse

- In the Amazon Q settings in Eclipse, under **Proxy Settings**,
  set **CA Cert PEM** to the path of your corporate
  certificate file. The file must have a `.pem` file
  extension. (You cannot use a `.crt` file.)

An example path resembles the following:

`/path/to/corporate-ca-bundle.pem`

For instructions on obtaining this file, see [Getting your corporate
certificate](#proxy-get-corp-ca-cert "#proxy-get-corp-ca-cert").

JetBrains
In JetBrains, manually install your corporate certificate following the guidance
in the [Trusted root certificates](https://www.jetbrains.com/help/idea/ssl-certificates.html#manual_configuration "https://www.jetbrains.com/help/idea/ssl-certificates.html#manual_configuration") topic of the IntelliJ IDEA
documentation.

For instructions on obtaining the certificate, see [Getting your corporate
certificate](#proxy-get-corp-ca-cert "#proxy-get-corp-ca-cert").

Visual Studio

- Configure the following Windows Environment Variables:

      + `NODE_OPTIONS = --use-openssl-ca`
      + `NODE_EXTRA_CA_CERTS =
       `cert-path``

  Replace `cert-path` with the path of your
  corporate certificate file. The file must have a `.pem`
  file extension. (You cannot use a `.crt` file.)

An example path resembles the following:

`/path/to/corporate-ca-bundle.pem`

For instructions on obtaining the corporate certificate file, see [Getting your corporate certificate](#proxy-get-corp-ca-cert "#proxy-get-corp-ca-cert"). For detailed information
about the Windows Environment Variables, see the [Node.js documentation](https://nodejs.org/api/cli.html#cli_node_extra_ca_certs_file "https://nodejs.org/api/cli.html#cli_node_extra_ca_certs_file").

Visual Studio Code

1. From VS Code, open VS Code **Settings** by pressing
   `CMD + ,` (Mac) or `Ctrl +
,` (Windows/Linux).
2. From the **Settings** search bar, enter
   `Amazon Q › Proxy: Certificate Authority`, then
   locate it in the search results.
3. Enter the path of your corporate certificate file. It will have a
   `.pem` or `.crt` file
   extension.

An example path resembles the following:

`/path/to/corporate-ca-bundle.pem`

For instructions on obtaining this file, see [Getting your corporate certificate](#proxy-get-corp-ca-cert "#proxy-get-corp-ca-cert").

### Step 3: Restart your IDE

You must restart your IDE in order to update Amazon Q with your changes.

### Troubleshooting

If you completed the procedures in the previous sections and you are still experiencing
issues, use the following instructions to troubleshoot.

Eclipse

1. Make sure your proxy URL format includes `http://` or
   `https://`.
2. Make sure your certificate file path is correct and accessible.
3. Review your Amazon Q logs in the Eclipse Error Log. To navigate to the Error
   Log, do one of the following:
   - Sign in to Amazon Q in Eclipse, choose the down-arrow next to the Q
     icon at the top-right, and then choose **Help**,
     **View Logs**.
   - From the Eclipse menu, choose **Window**,
     **Show View**, **Error
     Log**.

###### Note

If you encounter the following error messages:

    * `unable to verify the first certificate`, make
     sure you followed the instructions in [Step 2: Configuring SSL certificate handling](#proxy-configure-ssl-cert "#proxy-configure-ssl-cert") to specify a
     certificate manually.
    * `self signed certificate`, make sure you followed
     the instructions in [Step 2: Configuring SSL certificate handling](#proxy-configure-ssl-cert "#proxy-configure-ssl-cert") to specify a
     certificate manually.
    * `ECONNREFUSED`, check your internet connection
     and proxy information.

JetBrains

1. Make sure your proxy URL format includes `http://` or
   `https://`.
2. Make sure your certificate file path is correct and accessible.
3. Review your Amazon Q logs in the JetBrains log file. For help on finding the
   log file, see [Locating IDE log files](https://intellij-support.jetbrains.com/hc/en-us/articles/207241085-Locating-IDE-log-files "https://intellij-support.jetbrains.com/hc/en-us/articles/207241085-Locating-IDE-log-files") on the JetBrains IDEs Support
   page.

###### Note

If you encounter the following error messages:

    * `unable to verify the first certificate`, make
     sure you followed the instructions in [Step 2: Configuring SSL certificate handling](#proxy-configure-ssl-cert "#proxy-configure-ssl-cert") to specify a
     certificate manually.
    * `self signed certificate`, make sure you followed
     the instructions in [Step 2: Configuring SSL certificate handling](#proxy-configure-ssl-cert "#proxy-configure-ssl-cert") to specify a
     certificate manually.
    * `ECONNREFUSED`, check your internet connection
     and proxy information.

Visual Studio

1. Make sure your proxy URL format includes `http://` or
   `https://`.
2. Make sure your certificate file path is correct and accessible.
3. Review the AWS Toolkit extension's logs as follows:
   - From the Visual Studio main menu, expand
     **Extensions**.
   - Choose **AWS Toolkit** to expand the AWS Toolkit
     menu, then choose **View Toolkit Logs**.
   - When the AWS Toolkit logs folder opens in your Operating System,
     sort the files by date and locate any log file that contains
     information relevant to your current issue.

4. Review your Amazon Q logs in the Visual Studio Activity Log. For more information, see
   [Troubleshooting Extensions with the Activity Log](https://devblogs.microsoft.com/visualstudio/troubleshooting-extensions-with-the-activity-log/ "https://devblogs.microsoft.com/visualstudio/troubleshooting-extensions-with-the-activity-log/").

###### Note

If you encounter the following error messages:

    * `unable to verify the first certificate`, make
     sure you followed the instructions in [Step 2: Configuring SSL certificate handling](#proxy-configure-ssl-cert "#proxy-configure-ssl-cert") to specify a
     certificate manually.
    * `self signed certificate`, make sure you followed
     the instructions in [Step 2: Configuring SSL certificate handling](#proxy-configure-ssl-cert "#proxy-configure-ssl-cert") to specify a
     certificate manually.
    * `ECONNREFUSED`, check your internet connection
     and proxy information.

Visual Studio Code

1. Make sure your proxy URL format includes `http://` or
   `https://`.
2. Make sure your certificate file path is correct and accessible.
3. Review your Amazon Q logs in the **Output panel** of
   VS Code.

###### Note

If you encounter the following error messages:

    * `unable to verify the first certificate`, make
     sure you followed the instructions in [Step 2: Configuring SSL certificate handling](#proxy-configure-ssl-cert "#proxy-configure-ssl-cert") to specify a
     certificate manually.
    * `self signed certificate`, make sure you followed
     the instructions in [Step 2: Configuring SSL certificate handling](#proxy-configure-ssl-cert "#proxy-configure-ssl-cert") to specify a
     certificate manually.
    * `ECONNREFUSED`, check your internet connection
     and proxy information.

#### Getting your corporate certificate

To obtain your corporate certificate, ask your IT team for the following
information:

- Your corporate certificate bundle, which is typically a
  `.pem` or `.crt` file.
- Your proxy server details, including your host name, port, and authentication
  method.

Or, export the certificate from your browser:

1. Visit any HTTPS site on your corporate domain.
2. Near the address bar, choose the lock icon or a similar icon. (The icon differs
   depending your browser vendor.)
3. Export the root certificate to a file. Make sure you include the whole
   certificate chain. The steps to export the root certificate will be slightly
   different depending on the browser you're using. Consult your browser's
   documentation for detailed steps.
