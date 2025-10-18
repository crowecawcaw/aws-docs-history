# Learn how to use AWS Cloud Map service discovery with DNS
 queries and API calls

The following tutorial simulates a microservice architecture with two backend services. The first
 service will be discoverable using a DNS query. The second service will be discoverable using the
 AWS Cloud Map API only.

###### Note

The resource details, like domain names and IP addresses,
 are for simulation purposes only. They can't be resolved over the internet.

For an end-to-end AWS CLI version of this tutorial, see [Learn how to use AWS Cloud Map service discovery with DNS queries and API calls using the AWS CLI](tutorial-private-namespace-cli.md "tutorial-private-namespace-cli.md").


## Prerequisites


The following prerequisites must be met to complete the tutorial successfully.



* Before you begin, complete the steps in [Set up to use AWS Cloud Map](setting-up-cloud-map.md "setting-up-cloud-map.md").
* If you have not yet installed the AWS Command Line Interface, follow the steps at [Installing or
 updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") to install it.


The tutorial requires a command line terminal or shell to run commands. In Linux and
 macOS, use your preferred shell and package manager.


###### Note

In Windows, some Bash CLI commands that you commonly use with Lambda (such as
 `zip`) are not supported by the operating system's built-in terminals. To get
 a Windows-integrated version of Ubuntu and Bash, [install the Windows
 Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install "https://learn.microsoft.com/en-us/windows/wsl/install").
* The tutorial requires a local environment with the `dig` DNS lookup utility
 command.

## Step 1: Create an AWS Cloud Map namespace


In this step, you create a public AWS Cloud Map namespace. AWS Cloud Map creates a Route 53 hosted zone on
 your behalf with this same name. This gives you the ability to discover the service instances
 created in this namespace either using public DNS records or by using AWS Cloud Map API calls.


1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. Choose **Create namespace**.
3. For **Namespace name**, specify
 `cloudmap-tutorial.com`.


###### Note

If you were going to use this in production, you'd want to ensure that you specified the
 name of a domain you owned or had access to. But for the purposes of this tutorial, it's not
 necessary for it to be an actual domain that's being used.
4. (Optional) For **Namespace description**, specify a description for what
 you intend to use the namespace for.
5. For **Instance discovery**, select **API calls and public DNS
 queries**.
6. Leave the rest of the default values and choose **Create
 namespace**.

## Step 2: Create the AWS Cloud Map services


In this step, you create two services. The first service will be discoverable using public
 DNS and API calls. The second service will be discoverable using API calls only.


1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the left navigation pane, choose **Namespaces** to list the namespaces
 you've created.
3. From the list of namespaces, select the `cloudmap-tutorial.com` namespace and
 choose **View details**.
4. In the **Services** section, choose **Create service**
 and do the following to create the first service.


	1. For **Service name**, enter `public-service`. The service
	 name will be applied to the DNS records that AWS Cloud Map creates. The format that is used is
	 ``<service-name>`.`<namespace-name>``.
	2. For **Service Discovery Configuration**, select **API and
	 DNS**.
	3. In the **DNS configuration** section, for **Routing
	 policy**, select **Multivalue answer routing**.
	
	
	###### Note
	
	The console will translate this to **MULTIVALUE** after it is
	 selected. For more information about available routing options, see [Choosing a
	 routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html") in the *Route 53 Developer Guide*.
	4. Leave the rest of the default values and choose **Create service**
	 which will return you to the namespace details page.
5. In the **Services** section, choose **Create service**
 and do the following to create the second service.


	1. For **Service name**, enter `backend-service`.
	2. For **Service Discovery Configuration**, select **API
	 only**.
	3. Leave the rest of the default values and choose **Create
	 service**.

## Step 3: Register the AWS Cloud Map service
 instances


In this step, you create two service instances, one for each service in our
 namespace.


1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. From the list of namespaces, select the namespace you created in step 1 and choose
 **View details**.
3. On the namespace details page, from the list of services, select the
 `public-service` service and choose **View details**.
4. In the **Service instances** section, choose **Register service
 instance** and do the following to create the first service instance.


	1. For **Service instance ID**, specify `first`.
	2. For **IPv4 address**, specify `192.168.2.1`.
	3. Leave the rest of the default values and choose **Register service
	 instance**.
5. Using the breadcrumb at the top of the page, select
 **cloudmap-tutorial.com** to navigate back to the namespace detail
 page.
6. On the namespace details page, from the list of services, select the
 **backend-service** service and choose **View
 details**.
7. In the **Service instances** section, choose **Register service
 instance** and do the following to create the second service instance.


	1. For **Service instance ID**, specify `second` to indicate
	 that this is the second service instance.
	2. For **Instance type**, select **Identifying information for
	 another resource**.
	3. For **Custom attributes**, add a key-value pair with
	 `service-name` as the key and `backend` as the value.
	4. Choose **Register service instance**.

## Step 4: Discover the AWS Cloud Map service
 instances


Now that the AWS Cloud Map namespace, services, and service instances are created, you can verify
 everything is working by discovering the instances. Use the `dig` command to verify
 the public DNS settings and the AWS Cloud Map API to verify the backend service. For more information
 about the `dig` command, see [dig - DNS lookup utility](https://downloads.isc.org/isc/bind9/cur/9.19/doc/arm/html/manpages.html#dig-dns-lookup-utility "https://downloads.isc.org/isc/bind9/cur/9.19/doc/arm/html/manpages.html#dig-dns-lookup-utility").


1. Sign in to the AWS Management Console and open the Route 53 console at
 [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation, choose **Hosted zones**.
3. Select the **cloudmap-tutorial.com** hosted zone. This displays the
 hosted zone details in a separate pane. Take note of the **Name servers**
 associated with your hosted zone as we will use those in the next step.
4. Using the dig command and one of the Route 53 name servers for your hosted zone, query the
 DNS records for your service instance.



```
`dig @`hosted-zone-nameserver` public-service.cloudmap-tutorial.com`
```

The `ANSWER SECTION` in the output should display the IPv4 address you
 associated with your `public-service` service.



```
;; ANSWER SECTION:
public-service.cloudmap-tutorial.com. 300 IN A	192.168.2.1
```
5. Using the AWS CLI, query the attributes for your second service instances.



```
`aws servicediscovery discover-instances --namespace-name cloudmap-tutorial.com --service-name backend-service --region `region``
```

The output displays the attributes you associated with the service as key-value
 pairs.



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

## Step 5: Clean up the resources


Once you have completed the tutorial, you can delete the resources. AWS Cloud Map requires that you
 clean them up in reverse order, the service instances first, then the services, and finally the
 namespace. AWS Cloud Map will clean up the Route 53 resources on your behalf when you go through these
 steps.


1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. From the list of namespaces, select the `cloudmap-tutorial.com` namespace and
 choose **View details**.
3. On the namespace details page, from the list of services, select the
 `public-service` service and choose **View details**.
4. In the **Service instances** section, select the `first`
 instance and choose **Deregister**.
5. Using the breadcrumb at the top of the page, select
 **cloudmap-tutorial.com** to navigate back to the namespace detail
 page.
6. On the namespace details page, from the list of services, select the
 **public-service** service and choose **Delete**.
7. Repeat steps 3-6 for the `backend-service`.
8. In the left navigation, choose **Namespaces**.
9. Select the `cloudmap-tutorial.com` namespace and choose
 **Delete**.


###### Note

Although AWS Cloud Map cleans up the Route 53 resources on your behalf, you can navigate to the
 Route 53 console to verify that the `cloudmap-tutorial.com` hosted zone is
 deleted.
