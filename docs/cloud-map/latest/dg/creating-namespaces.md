# Creating an AWS Cloud Map namespace to group application

services

You can create a namespace to group services for your application under a friendly name that
allows for the discovery of application resources through API calls or DNS queries.

## Instance discovery options

The following table summarizes the different instance discovery options in AWS Cloud Map and the
corresponding namespace type that you can create, depending on your application's services and setup.

| Namespace type | Instance discovery method          | How it works                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Additional information                                                                                                                                                                                       |
| -------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| HTTP           | API calls                          | Resources in your application can discover other resources by calling the<br>`DiscoverInstances` API only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | • [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md")<br>• [CreateHttpNamespace](../api/API_CreateHttpNamespace.md "../api/API_CreateHttpNamespace.md")                   |
| Private DNS    | API calls and DNS queries in a VPC | When you create a private DNS namespace, AWS Cloud Map creates a corresponding Amazon Route 53 private hosted zone. Resources in your application can discover other resources by calling the<br>`DiscoverInstances` API, and by querying the nameservers in the private Route 53<br>hosted zone that AWS Cloud Map automatically creates.<br>The hosted zone created by AWS Cloud Map has the same name as the namespace and contains DNS<br>records that have names in the format<br>`service-name`.`namespace-name`.<br>NoteRoute 53 Resolver resolves DNS queries that originate in the VPC using records in the<br>private hosted zone. If the private hosted zone doesn't include a record that matches the<br>domain name in a DNS query, Route 53 responds to the query with `NXDOMAIN`<br>(non-existent domain). | • [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md")<br>• [CreatePrivateDnsNamespace](../api/API_CreatePrivateDnsNamespace.md "../api/API_CreatePrivateDnsNamespace.md") |
| Public DNS     | API calls and public DNS queries   | When you create a public DNS namespace, AWS Cloud Map creates a corresponding Amazon Route 53 public hosted zone. Resources in your application can discover other resources by calling the<br>`DiscoverInstances` API and by querying the nameservers in the public Route 53<br>hosted zone that AWS Cloud Map automatically creates.<br>The public hosted zone has the same name as the namespace and contains DNS records that<br>have names in the format<br>`service-name`.`namespace-name`.<br>NoteThe namespace name in this case must be a domain name that you've registered.                                                                                                                                                                                                                                    | • [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md")<br>• [CreatePublicDnsNamespace](../api/API_CreatePublicDnsNamespace.md "../api/API_CreatePublicDnsNamespace.md")    |

## Procedure

You can follow these steps to create a namespace using the AWS CLI, AWS Management Console, or the SDK for Python.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. Choose **Create namespace**.
3. For **Namespace name**, enter a name that will be used to discover
   instances.

###### Note

    * Namespaces configured for public DNS queries must end with a top level domain. For
     example, `.com`.
    * You can specify an internationalized domain name (IDN) if you convert the name to
     Punycode first. For information about online converters, perform an internet search on
     "punycode converter".


    You can also convert an internationalized domain name to Punycode when you create
     namespaces programmatically. For example, if you're using Java, you can convert a Unicode
     value to Punycode by using the `toASCII` method of the java.net.IDN
     library.

4. (Optional) For **Namespace description**, enter information about the
   namespace that will be visible on the **Namespaces** page and under
   **Namespace information**. You can use this information to easily identify
   a namespace.
5. For **Instance discovery**, you can choose between **API
   calls**, **API calls and DNS queries in VPCs**, and **API
   calls and public DNS queries** to create a HTTP, private DNS, or public DNS
   namespace respectively. For more information, see [Instance discovery options](#working-with-namespaces-instance-discovery "#working-with-namespaces-instance-discovery").

Based on your selection, follow these steps.

    * If you choose **API calls and DNS queries in VPCs**, for
     **VPC**, choose a virtual private cloud (VPC) that you want to associate
     the namespace with.
    * If you choose **API calls and DNS queries in VPCs** or **API
     calls and public DNS queries**, for **TTL**, specify a numerical
     value in seconds. The time to live (TTL) value determines how long DNS resolvers cache
     information for the start of authority (SOA) DNS record of the Route 53 hosted zone created
     with your namespace. For more information about TTL, see [TTL (seconds)](../../../Route53/latest/DeveloperGuide/resource-record-sets-values-shared.md#rrsets-values-common-ttl "../../../Route53/latest/DeveloperGuide/resource-record-sets-values-shared.md#rrsets-values-common-ttl") in the *Amazon Route 53 Developer
     Guide*.

6. (Optional) Under **Tags**, choose **Add tags** and
   then specify a key and a value to tag your namespace. You can specify one or more tags to add
   to your namespace. Tags allow you to categorize your AWS resources so you can more easily
   manage them. For more information, see [Tagging your AWS Cloud Map resources](using-tags.md "using-tags.md").
7. Choose **Create namespace**. You can view the status of the operation
   by using [ListOperations](../api/API_ListOperations.md "../api/API_ListOperations.md"). For more information, see [ListOperations](../api/API_ListOperations.md "../api/API_ListOperations.md") in the
   _AWS Cloud Map API Reference_

AWS CLI

- Create a namespace with the command for the instance discovery type you would prefer
  (replace the `red` values with your own).
  - Create an HTTP namespace using `create-http-namespace`. Service instances registered using an HTTP
    namespace can be discovered using a `DiscoverInstances` request, but they can't
    be discovered using DNS.

  ```
  `aws servicediscovery create-http-namespace --name `name-of-namespace``
  ```

  - Create a private namespace based on DNS and only visible inside a specified Amazon VPC
    using `create-private-dns-namespace`. You can discover instances that were
    registered with a private DNS namespace by using either a `DiscoverInstances`
    request or using DNS

  ```
  `aws servicediscovery create-private-dns-namespace --name `name-of-namespace` --vpc `vpc-xxxxxxxxx``
  ```

  - Create a public namespace based on DNS that is visible on the internet using
    `create-public-dns-namespace`. You can discover instances that were
    registered with a public DNS namespace by using either a `DiscoverInstances`
    request or using DNS.

  ```
  `aws servicediscovery create-public-dns-namespace --name `name-of-namespace``
  ```

AWS SDK for Python (Boto3)

1. If you don't already have `Boto3` installed, you can find instructions for
   installing, configuring, and using `Boto3`
   [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation").
2. Import `Boto3` and use `servicediscovery` as your service.

```
import boto3
client = boto3.client('servicediscovery')
```

3. Create a namespace with the command for the instance discovery type you would prefer
   (replace the `red` values with your own):
   - Create an HTTP namespace using `create_http_namespace()`. Service instances
     registered using an HTTP namespace can be discovered using
     `discover_instances()`, but they can't be discovered using DNS.

   ```
   response = client.create_http_namespace(
       Name='`name-of-namespace`',
   )
   # If you want to see the response
   print(response)
   ```

   - Create a private namespace based on DNS and only visible inside a specified Amazon VPC
     using `create_private_dns_namespace()`. You can discover instances that were
     registered with a private DNS namespace by using either `discover_instances()`
     or using DNS

   ```
   response = client.create_private_dns_namespace(
       Name='`name-of-namespace`',
       Vpc='`vpc-1c56417b`',
   )
   # If you want to see the response
   print(response)
   ```

   - Create a public namespace based on DNS that is visible on the internet using
     `create_public_dns_namespace()`. You can discover instances that were
     registered with a public DNS namespace by using either `discover_instances()` or
     using DNS.

   ```
   response = client.create_public_dns_namespace(
       Name='`name-of-namespace`',
   )
   # If you want to see the response
   print(response)
   ```

   - Example response output

   ```
   {
       'OperationId': 'gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9302yzd',
       'ResponseMetadata': {
           '...': '...',
       },
   }
   ```

## Next steps

After creating a namespace, you can create services in the namespace to group together
application resources that collectively serve a particular purpose in your application. A service
acts as a template for registering application resources as instances. For more information about
creating AWS Cloud Map services, see [Creating an AWS Cloud Map service for an application
component](creating-services.md "creating-services.md").
