# Learn how to use AWS Cloud Map service discovery with DNS queries and API calls using the AWS CLI

This tutorial demonstrates how to use AWS Cloud Map service discovery using the AWS Command Line Interface (CLI). You'll create a microservice architecture with two backend services – one discoverable using DNS queries and another discoverable using the AWS Cloud Map API only.

For a tutorial that includes AWS Cloud Map console steps, see [Learn how to use AWS Cloud Map service discovery with DNS
queries and API calls](tutorial-private-namespace.md "tutorial-private-namespace.md").

## Prerequisites

The following prerequisites must be met to complete the tutorial successfully.

- Before you begin, complete the steps in [Set up to use AWS Cloud Map](setting-up-cloud-map.md "setting-up-cloud-map.md").
- If you have not yet installed the AWS Command Line Interface, follow the steps at [Installing or
  updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") to install it.

The tutorial requires a command line terminal or shell to run commands. In Linux and
macOS, use your preferred shell and package manager.

###### Note

In Windows, some Bash CLI commands that you commonly use with Lambda (such as
`zip`) are not supported by the operating system's built-in terminals. To get
a Windows-integrated version of Ubuntu and Bash, [install the Windows
Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install "https://learn.microsoft.com/en-us/windows/wsl/install").

- The tutorial requires a local environment with the `dig` DNS lookup utility
  command.

## Create an AWS Cloud Map namespace

First, you'll create a public AWS Cloud Map namespace. AWS Cloud Map will create a Route 53 hosted zone with the same name, enabling service discovery through both DNS records and API calls.

1. Create the public DNS namespace:

```
aws servicediscovery create-public-dns-namespace \
    --name cloudmap-tutorial.com \
    --creator-request-id cloudmap-tutorial-request-1 \
    --region us-east-2
```

The command returns an operation ID that you can use to check the status of the namespace creation:

```
{
    "OperationId": "gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9xmplyzd"
}
```

2. Check the operation status to confirm the namespace was created successfully:

```
aws servicediscovery get-operation \
    --operation-id gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9xmplyzd \
    --region us-east-2
```

3. Once the operation is successful, get the namespace ID:

```
aws servicediscovery list-namespaces \
    --region us-east-2 \
    --query "Namespaces[?Name=='cloudmap-tutorial.com'].Id" \
    --output text
```

This command returns the namespace ID, which you'll need for subsequent steps:

```
ns-abcd1234xmplefgh
```

## Create the AWS Cloud Map services

Now, create two services within your namespace. The first service will be discoverable using both DNS and API calls, while the second will be discoverable using API calls only.

1. Create the first service with DNS discovery enabled:

```
aws servicediscovery create-service \
    --name public-service \
    --namespace-id ns-abcd1234xmplefgh \
    --dns-config "RoutingPolicy=MULTIVALUE,DnsRecords=[{Type=A,TTL=300}]" \
    --region us-east-2
```

The command returns details about the created service:

```
{
    "Service": {
        "Id": "srv-abcd1234xmplefgh",
        "Arn": "arn:aws:servicediscovery:us-east-2:123456789012:service/srv-abcd1234xmplefgh",
        "Name": "public-service",
        "NamespaceId": "ns-abcd1234xmplefgh",
        "DnsConfig": {
            "NamespaceId": "ns-abcd1234xmplefgh",
            "RoutingPolicy": "MULTIVALUE",
            "DnsRecords": [
                {
                    "Type": "A",
                    "TTL": 300
                }
            ]
        },
        "CreateDate": 1673613600.000,
        "CreatorRequestId": "public-service-request"
    }
}
```

2. Create the second service with API-only discovery:

```
aws servicediscovery create-service \
    --name backend-service \
    --namespace-id ns-abcd1234xmplefgh \
    --type HTTP \
    --region us-east-2
```

The command returns details about the created service:

```
{
    "Service": {
        "Id": "srv-ijkl5678xmplmnop",
        "Arn": "arn:aws:servicediscovery:us-east-2:123456789012:service/srv-ijkl5678xmplmnop",
        "Name": "backend-service",
        "NamespaceId": "ns-abcd1234xmplefgh",
        "Type": "HTTP",
        "CreateDate": 1673613600.000,
        "CreatorRequestId": "backend-service-request"
    }
}
```

## Register the AWS Cloud Map service instances

Next, register service instances for each of your services. These instances represent the actual resources that will be discovered.

1. Register the first instance with an IPv4 address for DNS discovery:

```
aws servicediscovery register-instance \
    --service-id srv-abcd1234xmplefgh \
    --instance-id first \
    --attributes AWS_INSTANCE_IPV4=192.168.2.1 \
    --region us-east-2
```

The command returns an operation ID:

```
{
    "OperationId": "4yejorelbukcjzpnr6tlmrghsjwpngf4-k9xmplyzd"
}
```

2. Check the operation status to confirm the instance was registered successfully:

```
aws servicediscovery get-operation \
    --operation-id 4yejorelbukcjzpnr6tlmrghsjwpngf4-k9xmplyzd \
    --region us-east-2
```

3. Register the second instance with custom attributes for API discovery:

```
aws servicediscovery register-instance \
    --service-id srv-ijkl5678xmplmnop \
    --instance-id second \
    --attributes service-name=backend \
    --region us-east-2
```

The command returns an operation ID:

```
{
    "OperationId": "7zxcvbnmasdfghjklqwertyuiop1234-k9xmplyzd"
}
```

4. Check the operation status to confirm the instance was registered successfully:

```
aws servicediscovery get-operation \
    --operation-id 7zxcvbnmasdfghjklqwertyuiop1234-k9xmplyzd \
    --region us-east-2
```

## Discover the AWS Cloud Map service instances

Now that you've created and registered your service instances, you can verify everything is working by discovering them using both DNS queries and the AWS Cloud Map API.

1. First, get the Route 53 hosted zone ID:

```
aws route53 list-hosted-zones-by-name \
    --dns-name cloudmap-tutorial.com \
    --query "HostedZones[0].Id" \
    --output text
```

This returns the hosted zone ID:

```
/hostedzone/Z1234ABCDXMPLEFGH
```

2. Get the name servers for your hosted zone:

```
aws route53 get-hosted-zone \
    --id Z1234ABCDXMPLEFGH \
    --query "DelegationSet.NameServers[0]" \
    --output text
```

This returns one of the name servers:

```
ns-1234.awsdns-12.org
```

3. Use the `dig` command to query the DNS records for your public service:

```
dig @ns-1234.awsdns-12.org public-service.cloudmap-tutorial.com
```

The output should display the IPv4 address you associated with your service:

```
;; ANSWER SECTION:
public-service.cloudmap-tutorial.com. 300 IN A	192.168.2.1
```

4. Use the AWS CLI to discover the backend service instance:

```
aws servicediscovery discover-instances \
    --namespace-name cloudmap-tutorial.com \
    --service-name backend-service \
    --region us-east-2
```

The output displays the attributes you associated with the service:

```
{
    "Instances": [
        {
            "InstanceId": "second",
            "NamespaceName": "cloudmap-tutorial.com",
            "ServiceName": "backend-service",
            "HealthStatus": "UNKNOWN",
            "Attributes": {
                "service-name": "backend"
            }
        }
    ],
    "InstancesRevision": 71462688285136850
}
```

## Clean up the resources

Once you've completed the tutorial, clean up the resources to avoid incurring charges. AWS Cloud Map requires that you clean them up in reverse order: service instances first, then services, and finally the namespace.

1. Deregister the first service instance:

```
aws servicediscovery deregister-instance \
    --service-id srv-abcd1234xmplefgh \
    --instance-id first \
    --region us-east-2
```

2. Deregister the second service instance:

```
aws servicediscovery deregister-instance \
    --service-id srv-ijkl5678xmplmnop \
    --instance-id second \
    --region us-east-2
```

3. Delete the public service:

```
aws servicediscovery delete-service \
    --id srv-abcd1234xmplefgh \
    --region us-east-2
```

4. Delete the backend service:

```
aws servicediscovery delete-service \
    --id srv-ijkl5678xmplmnop \
    --region us-east-2
```

5. Delete the namespace:

```
aws servicediscovery delete-namespace \
    --id ns-abcd1234xmplefgh \
    --region us-east-2
```

6. Verify that the Route 53 hosted zone is deleted:

```
aws route53 list-hosted-zones-by-name \
    --dns-name cloudmap-tutorial.com
```
