# Control API access with IAM policies


## Upgrade IAM policies to IPv6


AWS CloudHSM customers use IAM policies to control access to AWS CloudHSM APIs and prevent any
 IP addresses outside the configured range from being able to access AWS CloudHSM APIs.


The *cloudhsmv2.`<region>`.api.aws* dual-stack endpoint where AWS CloudHSM APIs are hosted supports IPv6 in addition to IPv4. 


Customers who need to support both IPv4 and IPv6 must update their IP address filtering policies to handle IPv6 addresses, 
 otherwise it will impact their ability to connect to AWS CloudHSM over IPv6.


### Who should upgrade?


Customers who use dual addressing with policies containing *aws:sourceIp* are 
 impacted by this upgrade. *Dual addressing*
 means that the network supports both IPv4 and IPv6. 


If you are using dual addressing, you must update your IAM policies that are currently
 configured with IPv4 format addresses to include IPv6 format addresses. 


For help with access issues, contact [Support](https://support.console.aws.amazon.com/support/home/?nc1=f_dr#/case/create "https://support.console.aws.amazon.com/support/home/?nc1=f_dr#/case/create").


###### Note

The following customers are *not* impacted by this
 upgrade:


* Customers who are on *only* IPv4 networks.

### What is IPv6?


IPv6 is the next generation IP standard intended to eventually replace IPv4. The previous
 version, IPv4, uses a 32-bit addressing scheme to support 4.3 billion devices. IPv6 instead
 uses 128-bit addressing to support approximately 340 trillion trillion trillion (or 2 to the
 128th power) devices. 


For more details, refer [VPC IPv6 webpage](https://aws.amazon.com/vpc/ipv6/ "https://aws.amazon.com/vpc/ipv6/").



```
2001:cdba:0000:0000:0000:0000:3257:9652
2001:cdba:0:0:0:0:3257:9652
2001:cdba::3257:965
```

### Updating an IAM policy for IPv6


IAM policies are currently used to set an allowed range of IP addresses using the
 `aws:SourceIp` filter. 


Dual addressing supports both IPv4 and IPv6 traffic. If your network uses dual addressing,
 you must update any IAM polices used for IP address filtering to
 include IPv6 address ranges.


For example, below policy identifies allowed IPv4 address ranges
 `192.0.2.0.*` and `203.0.113.0.*` in the `Condition`
 element. 



```
# https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.html
{
    "Version": "2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Deny",
        "Action": "*",
        "Resource": "*",
        "Condition": {
            "NotIpAddress": {
                "*aws:SourceIp*": [
                    "*192.0.2.0/24*",
                    "*203.0.113.0/24*"
                ]
            },
            "Bool": {
                "aws:ViaAWSService": "false"
            }
        }
    }
}
```

To update this policy, change the `Condition` element to include the
 IPv6 address ranges `2001:DB8:1234:5678::/64` and
 `2001:cdba:3257:8593::/64`.


###### Note

DO NOT REMOVE the existing IPv4 addresses because they are needed for backward
 compatibility.



```
"Condition": {
                "NotIpAddress": {
                    "*aws:SourceIp*": [
                        "*192.0.2.0/24*", <<DO NOT REMOVE existing IPv4 address>>
                        "*203.0.113.0/24*", <<DO NOT REMOVE existing IPv4 address>>
                        "`*2001:DB8:1234:5678::/64*`", <<New IPv6 IP address>>
                        "`*2001:cdba:3257:8593::/64*`" <<New IPv6 IP address>>
                    ]
                },
                "Bool": {
                    "aws:ViaAWSService": "false"
                }
            }
```

### Verify your client supports IPv6


Customers using the *cloudhsmv2.{region}.api.aws* endpoint are 
 advised to verify if they are able to connect to it. The following steps describe how to perform the verification. 


This examples uses Linux and curl version 8.6.0 and uses the 
 [AWS CloudHSM service endpoints](https://docs.aws.amazon.com/general/latest/gr/cloudhsm.html "https://docs.aws.amazon.com/general/latest/gr/cloudhsm.html")
 which has IPv6 enabled endpoints located at the *api.aws endpoint*. 


###### Note

Switch the AWS Region to the same Region where the client is located. 
 In this example, we use the US East (N. Virginia) – `us-east-1` endpoint.


1. Determine if the endpoint resolves with an IPv6 address using the following `dig` command. 



```
dig +short AAAA cloudhsmv2.us-east-1.api.aws
2600:1f18:e2f:4e05:1a8a:948e:7c08:c1c3
```
2. Determine if the client network can make an IPv6 connection using the following `curl` command. A 404 response code means the connection succeeded,
 while a 0 response code means the connection failed.



```
curl --ipv6 -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: %{response_code}\n" https://cloudhsmv2.us-east-1.api.aws

remote ip: 2600:1f18:e2f:4e05:1a8a:948e:7c08:c1c3
response code: 404
```

If a remote IP was identified **and** the response 
 code is not `0`, a network connection was successfully made to the endpoint using IPv6. 
 The remote IP should be an IPv6 address because the operating system should select the protocol that is 
 valid for the client. If the remote IP is not an IPv6 address, use the following command to force `curl` to use IPv4. 



```
curl --ipv4 -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: %{response_code}\n" https://cloudhsmv2.us-east-1.api.aws

remote ip: 3.123.154.250
response code: 404
```

If the remote IP is blank or the response code is `0`, the client network or 
 the network path to the endpoint is IPv4-only. You can verify this configuration with 
 the following `curl` command. 



```
curl -o /dev/null --silent -w "\nremote ip: %{remote_ip}\nresponse code: %{response_code}\n" https://cloudhsmv2.us-east-1.api.aws

remote ip: 3.123.154.250
response code: 404
```
