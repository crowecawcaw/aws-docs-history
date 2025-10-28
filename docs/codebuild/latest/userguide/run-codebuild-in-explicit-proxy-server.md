# Run CodeBuild in an explicit proxy

server

To run AWS CodeBuild in an explicit proxy server, you must configure the proxy server to
allow or deny traffic to and from external sites, and then configure the
`HTTP_PROXY` and `HTTPS_PROXY` environment variables.

###### Topics

- [Configure Squid as an
  explicit proxy server](#use-proxy-server-explicit-squid-configure "#use-proxy-server-explicit-squid-configure")
- [Create a CodeBuild
  project](#use-proxy-server-explicit-create-acb-project "#use-proxy-server-explicit-create-acb-project")
- [Explicit proxy server
  sample squid.conf file](#use-proxy-server-explicit-sample-squid-conf "#use-proxy-server-explicit-sample-squid-conf")

## Configure Squid as an

explicit proxy server

To configure the Squid proxy server to be explicit, you must make the following
modifications to its `/etc/squid/squid.conf` file:

- Remove the following default access control list (ACL) rules.

```
acl localnet src 10.0.0.0/8
acl localnet src 172.16.0.0/12
acl localnet src 192.168.0.0/16
acl localnet src fc00::/7
acl localnet src fe80::/10
```

Add the following in place of the default ACL rules you removed. The
first line allows requests from your VPC. The next two lines grant your
proxy server access to destination URLs that might be used by AWS CodeBuild.
Edit the regular expression in the last line to specify S3 buckets or a
CodeCommit repository in an AWS Region. For example:

    + If your source is Amazon S3, use the command **acl download\_src
     dstdom\_regex .\*s3\.us-west-1\.amazonaws\.com**to grant
     access to S3 buckets in the `us-west-1` Region.
    + If your source is AWS CodeCommit, use
     `git-codecommit.<`your-region`>.amazonaws.com`
     to add an AWS Region to an allow list.

```
acl localnet src 10.1.0.0/16 #Only allow requests from within the VPC
acl allowed_sites dstdomain .github.com #Allows to download source from GitHub
acl allowed_sites dstdomain .bitbucket.com #Allows to download source from Bitbucket
acl download_src dstdom_regex .*\.amazonaws\.com #Allows to download source from Amazon S3 or CodeCommit
```

- Replace `http_access allow localnet` with the following:

```
http_access allow localnet allowed_sites
http_access allow localnet download_src
```

- If you want your build to upload logs and artifacts, do one of the
  following:
  1.  Before the `http_access deny all` statement, insert the
      following statements. They allow CodeBuild to access CloudWatch and Amazon S3. Access to
      CloudWatch is required so that CodeBuild can create CloudWatch logs. Access to Amazon S3 is
      required for uploading artifacts and Amazon S3 caching.
      - ```
        https_port 3130 cert=/etc/squid/ssl/squid.pem ssl-bump intercept
        acl SSL_port port 443
        http_access allow SSL_port
        acl allowed_https_sites ssl::server_name .amazonaws.com
        acl step1 at_step SslBump1
        acl step2 at_step SslBump2
        acl step3 at_step SslBump3
        ssl_bump peek step1 all
        ssl_bump peek step2 allowed_https_sites
        ssl_bump splice step3 allowed_https_sites
        ssl_bump terminate step2 all
        ```

      ```
      + After you save `squid.conf`, run the
       following command:



      ```

      sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 3130
      sudo service squid restart

      ```

      ```

  2.  Add `proxy` to your buildspec file. For more information,
      see [Buildspec syntax](build-spec-ref.md#build-spec-ref-syntax "build-spec-ref.md#build-spec-ref-syntax").

  ```
  version: 0.2
  proxy:
    upload-artifacts: yes
    logs: yes
  phases:
    build:
      commands:
        - command
  ```

###### Note

If you receive a RequestError timeout error, see [RequestError timeout error when running
CodeBuild in a proxy server](troubleshooting.md#code-request-timeout-error "troubleshooting.md#code-request-timeout-error").

For more information, see [Explicit proxy server
sample squid.conf file](#use-proxy-server-explicit-sample-squid-conf "#use-proxy-server-explicit-sample-squid-conf") later in this
topic.

## Create a CodeBuild

project

To run AWS CodeBuild with your explicit proxy server, set its `HTTP_PROXY`
and `HTTPS_PROXY` environment variables with the private IP address of
the EC2 instance you created for your proxy server and port 3128 at the project
level. The private IP address looks like
`http://`your-ec2-private-ip-address`:3128`.
For more information, see [Create a build project in AWS CodeBuild](create-project.md "create-project.md") and [Change build project settings in AWS CodeBuild](change-project.md "change-project.md").

Use the following command to view the Squid proxy access log:

```
sudo tail -f /var/log/squid/access.log
```

## Explicit proxy server

sample `squid.conf` file

The following is an example of a `squid.conf` file that is
configured for an explicit proxy server.

```
  acl localnet src 10.0.0.0/16 #Only allow requests from within the VPC
  # add all URLS to be whitelisted for download source and commands to be run in build environment
  acl allowed_sites dstdomain .github.com    #Allows to download source from github
  acl allowed_sites dstdomain .bitbucket.com #Allows to download source from bitbucket
  acl allowed_sites dstdomain ppa.launchpad.net #Allows to run apt-get in build environment
  acl download_src dstdom_regex .*\.amazonaws\.com #Allows to download source from S3 or CodeCommit
  acl SSL_ports port 443
  acl Safe_ports port 80		# http
  acl Safe_ports port 21		# ftp
  acl Safe_ports port 443		# https
  acl Safe_ports port 70		# gopher
  acl Safe_ports port 210		# wais
  acl Safe_ports port 1025-65535	# unregistered ports
  acl Safe_ports port 280		# http-mgmt
  acl Safe_ports port 488		# gss-http
  acl Safe_ports port 591		# filemaker
  acl Safe_ports port 777		# multiling http
  acl CONNECT method CONNECT
  #
  # Recommended minimum Access Permission configuration:
  #
  # Deny requests to certain unsafe ports
  http_access deny !Safe_ports
  # Deny CONNECT to other than secure SSL ports
  http_access deny CONNECT !SSL_ports
  # Only allow cachemgr access from localhost
  http_access allow localhost manager
  http_access deny manager
  # We strongly recommend the following be uncommented to protect innocent
  # web applications running on the proxy server who think the only
  # one who can access services on "localhost" is a local user
  #http_access deny to_localhost
  #
  # INSERT YOUR OWN RULE(S) HERE TO ALLOW ACCESS FROM YOUR CLIENTS
  #
  # Example rule allowing access from your local networks.
  # Adapt localnet in the ACL section to list your (internal) IP networks
  # from where browsing should be allowed
  http_access allow localnet allowed_sites
  http_access allow localnet download_src
  http_access allow localhost
  # Add this for CodeBuild to access CWL end point, caching and upload artifacts S3 bucket end point
  https_port 3130 cert=/etc/squid/ssl/squid.pem ssl-bump intercept
  acl SSL_port port 443
  http_access allow SSL_port
  acl allowed_https_sites ssl::server_name .amazonaws.com
  acl step1 at_step SslBump1
  acl step2 at_step SslBump2
  acl step3 at_step SslBump3
  ssl_bump peek step1 all
  ssl_bump peek step2 allowed_https_sites
  ssl_bump splice step3 allowed_https_sites
  ssl_bump terminate step2 all
  # And finally deny all other access to this proxy
  http_access deny all
  # Squid normally listens to port 3128
  http_port 3128
  # Uncomment and adjust the following to add a disk cache directory.
  #cache_dir ufs /var/spool/squid 100 16 256
  # Leave coredumps in the first cache dir
  coredump_dir /var/spool/squid
  #
  # Add any of your own refresh_pattern entries above these.
  #
  refresh_pattern ^ftp:		1440	20%	10080
  refresh_pattern ^gopher:	1440	0%	1440
  refresh_pattern -i (/cgi-bin/|\?) 0	0%	0
  refresh_pattern .		0	20%	4320
```
