# AWS Cloud Map service DNS configuration

When you create a service in a namespace that supports instance discovery by DNS
 queries, AWS Cloud Map creates Route 53 DNS records. You must specify a Route 53 routing policy and
 DNS record type that will apply to all Route 53 DNS records that AWS Cloud Map creates.


## Routing policy


A routing policy determines how Route 53 responds to the DNS queries that are used
 for service instance discovery. Supported routing policies and how they relate to
 AWS Cloud Map are as follows.




**Weighted routing**

Route 53 returns the applicable value from one randomly selected AWS Cloud Map
 service instance from among the instances that you registered using the
 same AWS Cloud Map service. All records have the same weight, so you can't
 route more or less traffic to any instances.


For example, suppose the service includes configurations for one
 **A** record and a health check, and you use the
 service to register 10 instances. Route 53 responds to DNS queries with the
 IP address for one randomly selected instance from among the healthy
 instances. If no instances are healthy, Route 53 responds to DNS queries as
 if all the instances were healthy.


If you don't define a health check for the service, Route 53 assumes that
 all instances are healthy and returns the applicable value for one
 randomly selected instance.


For more information, see [Weighted Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted") in the
 *Amazon Route 53 Developer Guide*.



**Multivalue answer routing**

If you define a health check for the service and the result of the
 health check is healthy, Route 53 returns the applicable value for up to
 eight instances.


For example, suppose that the service includes configurations for one
 **A** record and a health check. You use the
 service to register 10 instances. Route 53 responds to DNS queries with IP
 addresses for only a maximum of eight healthy instances. If fewer than
 eight instances are healthy, Route 53 responds to every DNS query with the
 IP addresses for all the healthy instances.


If you don't define a health check for the service, Route 53 assumes that
 all instances are healthy and returns the values for up to eight
 instances.


For more information, see [Multivalue Answer Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue") in the
 *Amazon Route 53 Developer Guide*.




## Record type


A Route 53 DNS record type determines the type of value Route 53 returns in response to
 the DNS queries that are used for service instance discovery. The different DNS
 record types you can specify, and the associated values returned by Route 53 in
 response to queries are as follows.




**A**

If you specify this type, Route 53 returns the IP address of the resource
 in IPv4 format, such as **192.0.2.44**.



**AAAA**

 If you specify this type, Route 53 returns the IP address of the
 resource in IPv6 format, such as
 **2001:0db8:85a3:0000:0000:abcd:0001:2345**.



**CNAME**

 If you specify this type, Route 53 returns the domain name of the
 resource (such as www.example.com).


###### Note


* To configure a **CNAME** DNS record, you
 must specify the **Weighted routing**
 routing policy.
* When you configure a **CNAME** DNS
 record, you can't configure a Route 53 health check.


**SRV**

If you specify this type, Route 53 returns the value for an
 `SRV` record. The value for an **SRV**
 record uses the following values:


`priority weight port service-hostname`


Consider the following:



* The values of `priority` and `weight`
 are both set to 1 and can't be changed.
* For `port`, AWS Cloud Map uses the value that you
 specify for **Port** (AWS\_INSTANCE\_PORT) when
 you register an instance.
* The value of `service-hostname` is a concatenation
 of the following values:




	+ The value that you specify for **Service
	 instance ID** (InstanceID) when you
	 register an instance
	+ The name of the service
	+ The name of the namespace
For example, suppose you specify **test** as
 an instance ID when you register an instance. The name of the
 service is **backend** and the name of the
 namespace is **example.com**. AWS Cloud Map
 assigns the following value to the `service-hostname`
 attribute in the **SRV** record:


`test.backend.example.com`

###### Note

If you specify values an IPv4 address, an IPv6 address, or both
 when you register an instance, AWS Cloud Map automatically creates
 **A** and/or **AAAA** records
 that have the same name as the value of
 `service-hostname` in the **SRV**
 record.




You can specify record types in the following combinations:



* **A**
* **AAAA**
* **A** and **AAAA**
* **CNAME**
* **SRV**

If you specify **A** and **AAAA** record types,
 you can specify an IPv4 IP address, an IPv6 IP address, or both when you register an
 instance.
