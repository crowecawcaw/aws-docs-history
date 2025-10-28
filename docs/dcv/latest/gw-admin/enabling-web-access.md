# Enabling Web Access

## Configuring Web Resources

The `[web-resources]` section controls how the Amazon DCV Connection Gateway forwards HTTP requests to an external Web Server.
In particular, the Web Server can be used to host the files of a [DCV Web Client](../userguide/client-web.md "../userguide/client-web.md"),
so that when a browser connects to the Connection Gateway it can retrieve the `html`, `css` and `javascript` files of the DCV Web Client.
By default, the DCV Connection Gateway package does not include the necessary web resources to support browser-based connections. If you would like to enable browser-based
connections to your DCV server fleet, follow the instructions below.

The DCV server package contains the web resources for the DCV Web Client. To obtain these resources, you will need to download the
[latest DCV server package](https://download.nice-dcv.com "https://download.nice-dcv.com") and extract the web-viewer package. Once extracted, you may host the web resources
on any web server that is reachable from the DCV Connection Gateway. The following sections provide two examples, one hosting the files on a cloud-native service, the other
configuring a local web server on the gateway.

### Using Centralized Web Resources

The following walk through will guide you on how to host the resources on the [Simple Storage Service](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")(S3) and deliver
them with [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/"). This option is the cloud-native, centralized approach.

**Prerequisites**

To perform the steps below, you will need the following:

- A provisioned S3 Bucket and [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") permissions to configure it.

###### Note

If you do not have a bucket, instructions can be found [here](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").

- IAM permissions to use [CloudShell](../../../cloudshell.md "../../../cloudshell.md").
- IAM permissions to create and configure a CloudFront distribution.

**Hosting Web Resources**

1. Open a [CloudShell](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home") terminal.
2. Create a temporary directory to store your download by running the following command:

```
`$` mkdir /tmp/dcvgw/
```

3. Download the DCV Server:

```
`$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-amzn2-aarch64.tgz
```

4. Extract your download to your temporary directory and rename it:

```
`$` tar -xvzf nice-dcv-amzn2-aarch64.tgz -C /tmp/dcvgw/
mv /tmp/dcvgw/nice-dcv* /tmp/dcvgw/dcv-server-packages
```

5. Unpack the rpm to gain access to the web resources:

```
`$` rpm2cpio /tmp/dcvgw/dcv-server-packages/nice-dcv-web-viewer*.rpm | cpio -idmv
```

6. Upload the assets to your S3 bucket:

```
`$` aws s3 cp /tmp/dcvgw/dcv-server-packages/usr/share/dcv/www/ s3://BUCKET-NAME/ --recursive
```

**Delivering Web Resources**

To keep your S3 bucket protected from the public internet, you will need to create a CloudFront distribution to deliver the web resources.
As a best practice, you should use origin access control (OAC) to configure restricted CloudFront access to your bucket. To read more about OAC,
see this [documentation](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md").

1. Navigate to the [CloudFront console](https://console.aws.amazon.com/cloudfront/v3/home "https://console.aws.amazon.com/cloudfront/v3/home").
2. Choose **Create distribution**.
3. For the **Origin domain** drop down menu, choose your S3 bucket that will host the web resources.
4. For **Origin access**, choose **Origin access control settings (recommended)**.
   1. This will populate a new section called **Origin access control**. Select **Create control setting**.
   2. Keep the default selections and choose **Create**.
   3. Choose **Create distribution** at the bottom of the page.
   4. Creating the distribution will create a banner at the top that reads “The S3 bucket policy needs to be updated”.
      Within the banner, choose the **Copy policy** button and paste the policy locally.
   5. Take note of your **Distribution domain name** within the **Details** section of your distribution.
   6. Navigate to your S3 bucket within the [S3 console](https://s3.console.aws.amazon.com/s3/home "https://s3.console.aws.amazon.com/s3/home").
   7. Within your bucket, navigate to the **Permissions** tab.
   8. Within the **Bucket policy** section, select **Edit**.
   9. Paste the policy that you acquired from the banner button within the policy editor.
   10. Choose **Save changes**.

Now that your web resources are being hosted in S3 and delivered from CloudFront, you need to point your DCV Connection Gateway to your distribution
so that it can serve the DCV static assets when users initiate browser-based connections. This can be done by adding the attribute below to the
[[web-resources]](config-reference.md#config-web-resources "config-reference.md#config-web-resources") section of
your gateway’s configuration file.

```
[web-resources]
url = `DistributionDomainName`
```

Once you have modified the configuration, [reload](manage-reload.md "manage-reload.md") the gateway.

### Using Local Web Resources

The following walk through will guide you on how to host the resources locally on the gateway. Note that since each gateway is hosting their own web resources, if you ever
need to update the resources, you will need to do so across your gateway fleet. The instructions below will target packages for ARM-based Amazon Linux 2 instances. If you have
leveraged a different distribution for your DCV Connection Gateway, you will need to replace the URL in step three with your respective distribution. This can be retrieved from
the Amazon DCV [downloads page](https://download.nice-dcv.com/latest.html "https://download.nice-dcv.com/latest.html") under Amazon DCV Server. If you need to update the web resources with this approach, since the
resources are local to the machine, you will need to either update your Amazon Machine Image ([AMI](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md"))
or push an update through a remote administration tool, such as [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/").

**Locally Hosting Web Resources**

1. SSH into your DCV Connection Gateway.
2. Create a temporary directory to hold your download by running the following command:

```
`$` mkdir /tmp/dcvgw/
```

3. Download the latest version of [DCV Server](https://download.nice-dcv.com/latest.html "https://download.nice-dcv.com/latest.html").
4. Extract your download to your temporary directory and rename it:

```
`$` tar -xvzf nice-dcv-amzn2-aarch64.tgz -C /tmp/dcvgw/
mv /tmp/dcvgw/nice-dcv* /tmp/dcvgw/dcv-server-packages
```

5. Install the web resources package:

```
`$` sudo yum localinstall -y /tmp/dcvgw/dcv-server-packages/nice-dcv-web-viewer*.rpm
```

6. Open your DCV Connection Gateway configuration file in your preferred text editor:

```
`$` sudo vi /etc/dcv-connection-gateway/dcv-connection-gateway.conf
```

7. Within your `[web-resources]` section, add the following line:

```
`$` local-resources-path = "/usr/share/dcv/www"
```

8. If your Amazon DCV Connection Gateway service is already running, restart it with the following command:

```
`$` sudo systemctl restart dcv-connection-gateway
```

9. If your DCV Connection Gateway service is stopped,
   [start it](manage-start.md "manage-start.md").

## Optional Security Settings

###### Note

If you are not interested in using the DCV Web Client or if client machines retrieve the DCV Web Client from a separate server, you can skip this section.

If the url parameter is specified, it points to the HTTP end-point of a Web Server which can serve static files, in particular the `html`,
`css` and `javascript` files of the DCV Web Client.

Similarly to the `[resolver]` section, you can also use the `ca-file` or the `tls-strict` settings to be able to connect to a Web server that
has a certificate signed by a private Certificate Authority or a self-signed certificate.

```
...
[web-resources]
ca-file = "/path/to/resolver_ca.pem"...
```
