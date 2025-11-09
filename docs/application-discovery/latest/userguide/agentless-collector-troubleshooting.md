AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Troubleshooting

Agentless Collector

This section contains topics that can help you troubleshoot known issues with
Application Discovery Service Agentless Collector (Agentless Collector).

###### Topics

- [Fixing Unable to
  retrieve manifest or certificate file error](#unable-to-retrieve-manifest-or-certificate-file "#unable-to-retrieve-manifest-or-certificate-file")
- [Addressing
  self-signed certification problems when configuring WinRM certificates](#agentless-collector-address-self-signed-certification-problems "#agentless-collector-address-self-signed-certification-problems")
- [Fixing
  Agentless Collector cannot reach AWS during setup](#agentless-collector-fix-connector-cannot-reach-aws "#agentless-collector-fix-connector-cannot-reach-aws")
- [Fixing
  self-signed certification problems when connecting to the proxy host](#agentless-collector-fix-self-signed-certification-problems "#agentless-collector-fix-self-signed-certification-problems")
- [Finding unhealthy
  collectors](#agentless-collector-fixing-unhealthy-connectors "#agentless-collector-fixing-unhealthy-connectors")
- [Fixing IP address issues](#agentless-collector-vcenter-ip-issues "#agentless-collector-vcenter-ip-issues")
- [Fixing vCenter credentials
  issues](#agentless-collector-vcenter-credentials-issues "#agentless-collector-vcenter-credentials-issues")
- [Fixing data
  forwarding issues in the database and analytics data collection module](#agentless-collector-database-analytics-forwarding-issues "#agentless-collector-database-analytics-forwarding-issues")
- [Fixing connection
  issues in the database and analytics data collection module](#agentless-collector-database-analytics-connection-issues "#agentless-collector-database-analytics-connection-issues")
- [Standalone ESX host support](#agentless-collector-standalone-esx-host "#agentless-collector-standalone-esx-host")
- [Contacting AWS Support for
  Agentless Collector issues](#agentless-collector-support "#agentless-collector-support")

## Fixing `Unable to

retrieve manifest or certificate file error`

If you receive this error when you try to deploy the OVA from the Amazon S3 URL in the VMware
vCenter UI, ensure that your vCenter server meets the following requirements:

- VMware vCenter Server version 8.0 update 1 or later
- VMware vCenter Server 7.0 Update 3q (ISO Build 23788036) or later

## Addressing

self-signed certification problems when configuring WinRM certificates

If you enable WinRM certificate checks, you might need to import a self-signed certificate
authority into the Agentless Collector.

###### To import a self-signed certificate authority

1. Open the collector’s VM web console in VMware vCenter and sign in as
   `ec2-user` with the password `collector` as shown in the following
   example.

```
username: ec2-user
password: collector
```

2. Make sure that every self-signed CA certificate that is used to sign WinRM
   certificates is under the directory `/etc/pki/ca-trust/source/anchors`.
   For example:

```
/etc/pki/ca-trust/source/anchors/https-winrm-ca-1.pem
```

3. To install the new certificates, run the following command.

```
sudo update-ca-trust
```

4. Restart the Agentless Collector by running the following command

```
sudo shutdown -r now
```

5. (Optional) To verify that certificates have been successfully imported, you can run
   the following command.

```
sudo trust list --filter=ca-anchors | less
```

## Fixing

Agentless Collector cannot reach AWS during setup

Agentless Collector requires outbound access over TCP port 443 to several AWS
domains. When configuring Agentless Collector in the console you can get the
following error message.

###### Could Not Reach AWS

AWS cannot be reached. Please verify network settings.

This error occurs because of a failed attempt by Agentless Collector to establish
an HTTPS connection to an AWS domain that the collector needs to communicate with during the
setup process. The Agentless Collector configuration fails if a connection can't be
established.

###### To fix the connection to AWS

1. Check with your IT admin to see if your company firewall is blocking outbound traffic
   on port 443 to any of the AWS domains that require outbound access. Which AWS domains
   require outbound access depend on if your home Region is US West (Oregon) Region, us-west-2, or
   some other Region.

###### The following domains require outbound access if your AWS account home Region is

us-west-2:

    * `arsenal-discovery.us-west-2.amazonaws.com`
    * `migrationhub-config.us-west-2.amazonaws.com`
    * `api.ecr-public.us-east-1.amazonaws.com`
    * `public.ecr.aws`

###### The following domains require outbound access if your AWS account home Region is

not `us-west-2`:

    * `arsenal-discovery.us-west-2.amazonaws.com`
    * `arsenal-discovery.`your-home-region`.amazonaws.com`
    * `migrationhub-config.us-west-2.amazonaws.com`
    * `api.ecr-public.us-east-1.amazonaws.com`
    * `public.ecr.aws`

If your firewall is blocking outbound access to the AWS domains that
Agentless Collector needs to communicate with, configure a proxy host in the
**Data synchronization** section under **Collector
configuration**. 2. If updating the firewall does not resolve the connection issue, use the following
steps to ensure that the collector virtual machine has outbound network connectivity to
the domains listed in the previous step.

    1. Get the IP address of the Agentless Collector from VMware vCenter.
    2. Open the collector’s VM web console and sign in as `ec2-user`
     using the password `collector` as shown in the following
     example.



    ```
    username: ec2-user
    password: collector
    ```
    3. Test the connection to the listed domains by running telnet on ports 443 as shown
     in the following example.



    ```
    telnet migrationhub-config.us-west-2.amazonaws.com 443
    ```

3. If telnet cannot resolve the domain, try configuring a static DNS server using the
   [instructions for
   Amazon Linux 2](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-static-dns-ubuntu-debian/ "https://aws.amazon.com/premiumsupport/knowledge-center/ec2-static-dns-ubuntu-debian/").
4. If the error continues, for further support, see [Contacting AWS Support for
   Agentless Collector issues](#agentless-collector-support "#agentless-collector-support").

## Fixing

self-signed certification problems when connecting to the proxy host

If communication with the optionally provided proxy is via HTTPS and the proxy has a
self-signed certificate, you might need to provide a certificate.

1. Get the IP address of the Agentless Collector from VMware vCenter.
2. Open the collector’s VM web console and sign in as `ec2-user` with the
   password `collector` as shown in the following example.

```
username: ec2-user
password: collector
```

3. Paste the body of the certificate that is associated with the secure proxy, including
   both `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`,
   into the following file:

```
/etc/pki/ca-trust/source/anchors/https-proxy-ca.pem
```

4. To install the new certificate, run the following commands:

```
sudo update-ca-trust
```

5. Restart the Agentless Collector by running the following command:

```
sudo shutdown -r now
```

## Finding unhealthy

collectors

Status information for every collector is found on the [Data collectors](https://console.aws.amazon.com/migrationhub/discover/datacollectors?type=connector "https://console.aws.amazon.com/migrationhub/discover/datacollectors?type=connector") page of
the AWS Migration Hub (Migration Hub) console. You can identify collectors with problems by finding any
collectors with a **Status** of **Requires attention**.

The following procedure describes how to access the Agentless Collector console
to identify health issues.

###### To access the Agentless Collector console

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane under **Discover**, choose
   **Data collectors**.
3. From the **Agentless collectors** tab, make a note of the
   **IP address** for each connector that has a status of
   **Requires attention**.
4. To open the Agentless Collector console, open a web browser. Then type the
   following URL in the address bar: 
   `https://``<ip_address>``/`,
   where _ip_address_ is the IP address of an unhealthy
   collector.
5. Choose **Log in**, and then enter the Agentless Collector
   password, which was set up when the collector was configured in [Configuring
   Agentless Collector](agentless-collector-gs-configure.md "agentless-collector-gs-configure.md").
6. On the **Agentless Collector** dashboard page, under
   **Data collection**, choose **View and edit** in the
   **VMware vCenter** section.
7. Follow the instructions in [Editing VMware vCenter
   credentials](agentless-collector-vcenter-edit.md "agentless-collector-vcenter-edit.md") to correct the URL and
   credentials.

After correcting the health issues, the collector will re-establish connectivity with
vCenter server, and the collector's status will change to the **Collecting**
state. If the issues persist, see [Contacting AWS Support for
Agentless Collector issues](#agentless-collector-support "#agentless-collector-support").

The most common causes for unhealthy collectors are IP address and credentials issues.
[Fixing IP address issues](#agentless-collector-vcenter-ip-issues "#agentless-collector-vcenter-ip-issues") and [Fixing vCenter credentials
issues](#agentless-collector-vcenter-credentials-issues "#agentless-collector-vcenter-credentials-issues") can help you resolve these
issues and return a collector to a healthy state.

## Fixing IP address issues

A collector can go into an unhealthy state if the vCenter endpoint provided during
collector setup is malformed, invalid, or if the vCenter server is currently down and not
reachable. In this case, you'll receive a **Connection error** message .

The following procedure can help you resolve IP address issues.

###### To fix collector IP address issues

1. Get the IP address of the Agentless Collector from VMware vCenter.
2. Open the Agentless Collector console by opening a web browser, and then type
   the following URL in the address bar: 
   `https://``<ip_address>``/`,
   where _ip_address_ is the IP address of the collector
   from [Deploy
   Agentless Collector](agentless-collector-deploying.md#agentless-collector-gs-deploy "agentless-collector-deploying.md#agentless-collector-gs-deploy").
3. Choose **Log in**, and then enter the Agentless Collector
   password, which was set up when the collector was configured in [Configuring
   Agentless Collector](agentless-collector-gs-configure.md "agentless-collector-gs-configure.md").
4. On the **Agentless Collector** dashboard page, under
   **Data collection**, choose **View and edit** in the
   **VMware vCenter** section.
5. On the **VMware data collection details** page, under
   **Discovered vCenter servers**, make a note of the IP address in the
   **vCenter** column.
6. Using a separate command line tool like `ping` or `traceroute`,
   validate that the associated vCenter server is active and the IP is reachable from the
   collector VM.
   - If the IP address is incorrect and the vCenter service is active, then update the
     IP address in the collector console, and choose **Next**.
   - If the IP address is correct but the vCenter server is inactive, activate
     it.
   - If the IP address is correct and the vCenter server is active, check if it is
     blocking ingress network connections due to firewall issues. If yes, update your
     firewall settings to allow incoming connections from the collector VM.

## Fixing vCenter credentials

issues

Collectors can go into an unhealthy state if the vCenter user credentials provided when
configuring a collector are invalid, or do not have vCenter Read and View account
privileges.

If you experience issues related to vCenter credentials, check to make sure that you have
vCenter Read and View permissions set for the System group.

For information about editing vCenter credentials, see [Editing VMware vCenter
credentials](agentless-collector-vcenter-edit.md "agentless-collector-vcenter-edit.md").

## Fixing data

forwarding issues in the database and analytics data collection module

The home page of the database and analytics data collection module in
Agentless Collector displays the connection status for **Access to
DMS** and **Access to S3**. If you see **No
access** for **Access to DMS** and **Access to
S3**, then configure data forwarding. For more information, see [Configuring data forwarding](agentless-collector-gs-database-analytics-collection-prerequisites.md "agentless-collector-gs-database-analytics-collection-prerequisites.md").

If you experience this issue after you configure data forwarding, then check to make sure
that your data collection module can access to the internet. Then, make sure that you added
the **DMSCollectorPolicy** and **FleetAdvisorS3Policy**
policies to your IAM user. For more information, see [Deploying
Application Discovery Service Agentless Collector](agentless-collector-deploying.md#agentless-collector-gs-iam-user "agentless-collector-deploying.md#agentless-collector-gs-iam-user").

If your data collection module can't connect to AWS, then provide outbound access to the
following domains.

- `dms.`your-home-region`.amazonaws.com`
- `s3.amazonaws.com`

## Fixing connection

issues in the database and analytics data collection module

The database and analytics data collection module in Agentless Collector connects
to your LDAP servers to discover OS servers in your data environment. Then, the data
collection module connects to your OS servers to discover database and analytics servers. From
these database servers, the data collection module gathers capacity and performance metrics.
If your data collection module can't connect to these servers, then verify that you can
connect to your servers.

In the following examples, replace `replaceable` values with your
values.

- To verify that you can connect to your LDAP server, install the `ldap-util`
  package. To do so, run the following command.

```
sudo apt-get install ldap-util
```

Then, run the following command.

```
ldapsearch -x -D "`CN=user,CN=Users,DC=example,DC=com`" -w "`password`" -b "`dc=example,dc=com`" -h
```

- To verify that you can connect to a Linux OS server, use the following
  commands.

```
ssh -i C:\Users\`user`\private_key.pem -p 22 `username@my-linux-host.domain.com`
```

Run the previous example as an administrator in Windows.

```
ssh `username@my-linux-host.domain.com`
```

Run the previous example in Linux.

- To verify that you can connect to a Windows OS server, use the following
  commands.

```
winrs -r:`[hostname or ip]` -u:`username` -p:`password` cmd
```

Run the previous example as an administrator in Windows.

```
sudo apt install -y winrm
winrm --user=`username` --password=`password` [http or https]://`[hostname or ip]`:`[port]` "[cmd.exe or any other CLI command]"
```

Run the previous example in Linux.

- To verify that you can connect to a SQL Server database, use the following
  commands.

```
sqlcmd -S `[hostname or IP]` -U `username` -P '`password`'
SELECT GETDATE() AS sysdate
```

- To verify that you can connect to a MySQL database, use the following commands.

```
mysql -u `username` -p '`password`' -h `[hostname or IP]` -P `[port]`
SELECT NOW() FROM DUAL
```

- To verify that you can connect to an Oracle database, use the following
  commands.

```
sqlplus `username`/`password`@`[hostname or IP]`:`port/servicename`
SELECT SYSDATE FROM DUAL
```

- To verify that you can connect to a PostgreSQL database, use the following
  commands.

```
psql -U `username` -h `[hostname or IP]` -p `port` -d `database`
SELECT CURRENT_TIMESTAMP AS sysdate
```

If you can't connect to your database and analytics servers, then make sure that you
provide the required permissions. For more information, see [Discovering your database servers](agentless-collector-gs-database-analytics-collection-discovery.md "agentless-collector-gs-database-analytics-collection-discovery.md").

## Standalone ESX host support

The Agentless Collector does not support a standalone ESX host. The ESX host must
be part of the vCenter Server instance.

## Contacting AWS Support for

Agentless Collector issues

If you encounter issues with Application Discovery Service Agentless Collector
(Agentless Collector) and need help, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") You'll be contacted and might be asked to send the
collector logs.

###### To obtain Agentless Collector logs

1. Get the IP address of the Agentless Collector from VMware vCenter.
2. Open the collector’s VM web console and sign in as `ec2-user`
   using the password `collector` as shown in the following
   example.

```
username: ec2-user
password: collector
```

3. Use the following command to navigate to the log folder.

```
cd /var/log/aws/collector
```

4. Zip the log files by using the following commands.

```
sudo cp /local/agentless_collector/compose.log .
docker inspect $(docker ps --format {{.Names}}) | sudo tee docker_inspect.log >/dev/null
sudo tar czf logs_$(date '+%d-%m-%Y_%H.%M.%S').tar.gz --exclude='db.mv*' *
```

5. Copy the log file from the Agentless Collector VM.

```
scp logs*.tar.gz `targetuser`@`targetaddress`
```

6. Give the `tar.gz` file to AWS Enterprise Support.
