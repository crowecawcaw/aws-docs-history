# IP address and port requirements for Amazon WorkSpaces Secure Browser

To access WorkSpaces Secure Browser instances, user devices require outbound access on the following
ports:

- Port 443 (TCP)
  - Port 443 is used for HTTPS communication between user devices and streaming
    instances when using the internet endpoints. Typically, when end users browse the
    web during streaming sessions, the web browser randomly selects a source port in
    the high range for streaming traffic. You must ensure that return traffic to this
    port is allowed.
  - This port must be open to the required domains listed at [Allowed domains for Amazon WorkSpaces Secure Browser](allowed.md "allowed.md").
  - AWS publishes its current IP address ranges, including the ranges that the
    Session Gateway and CloudFront domains may resolve to, in JSON format. For information
    about how to download the .json file and view the current ranges, see [AWS IP address
    ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md"). Or, if you are using AWS Tools for Windows PowerShell, you can access the same
    information by using the **Get-AWSPublicIpAddressRange** PowerShell
    command. For more information, see [Querying the Public IP Address Ranges for AWS](https://aws.amazon.com/blogs/developer/querying-the-public-ip-address-ranges-for-aws/ "https://aws.amazon.com/blogs/developer/querying-the-public-ip-address-ranges-for-aws/").

- (Optional) Port 53 (UDP)
  - Port 53 is used for communication between user devices and your DNS servers.
  - This port is optional if you are not using DNS servers for domain name
    resolution.
  - The port must be open to the IP addresses for your DNS servers so that public
    domain names can be resolved.
