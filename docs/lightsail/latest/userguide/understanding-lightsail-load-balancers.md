# Distribute web traffic with Lightsail

load balancers

A Lightsail load balancer distributes incoming web traffic among multiple Lightsail
instances, in multiple Availability Zones. Load balancing increases the availability and fault
tolerance of the application on your instances. You can add and remove instances from your
Lightsail load balancer as your needs change, without disrupting the overall flow of requests
to your application.

With Lightsail load balancing, we create a DNS host name and route any requests sent to
this host name to a pool of target Lightsail instances. You can add as many target instances
to your load balancer as you like, as long as you stay within your Lightsail account quotas
for total number of instances.

## Load balancer features

Lightsail load balancers offer the following features:

- **HTTPS encryption** — By default, Lightsail
  load balancers handle unencrypted (HTTP) traffic requests through port 80. Activate HTTPS
  encryption by attaching a validated Lightsail SSL/TLS certificate to your load balancer.
  This allows your load balancer to handle encrypted (HTTPS) traffic requests through port

443.  For more information, see [SSL/TLS
      certificates](understanding-tls-ssl-certificates-in-lightsail-https.md "understanding-tls-ssl-certificates-in-lightsail-https.md").

The following features are available after you activate HTTPS encryption on your load
balancer:

    + **HTTP to HTTPS redirection** — Activate HTTP
     to HTTPS redirection to automatically redirect HTTP requests to an HTTPS encrypted
     connection. For more information, see [Configure HTTP
     to HTTPS redirection for your load balancer](amazon-lightsail-configure-load-balancer-https-redirection.md "amazon-lightsail-configure-load-balancer-https-redirection.md").
    + **TLS security policies** — Configure a TLS
     security policy on your load balancer. For more information, see [Configuring
     TLS security policies on your Amazon Lightsail load balancers](amazon-lightsail-configure-load-balancer-tls-security-policy.md "amazon-lightsail-configure-load-balancer-tls-security-policy.md").

- **Health checking** — By default, health checks
  are performed on the attached instances at the root of the web application that is running
  on them. The health checks monitor the health of the instances so that the load balancer
  can send requests only to the healthy instances. For more information, see [Health checking for a
  Lightsail load balancer](understanding-lightsail-load-balancer-health-checking.md "understanding-lightsail-load-balancer-health-checking.md").
- **Session persistence** — Configure session
  persistence if you're storing session information locally in your website visitors'
  browsers. For example, you might be running a Magento e-commerce application with a
  shopping cart on your load-balanced Lightsail instances. If your website visitors add
  items to their shopping carts, and then end their sessions, when they come back, the
  shopping cart items will still be there if you configured session persistence. For more
  information, see [Enable session
  persistence for a load balancer](enable-session-stickiness-persistence-or-change-cookie-duration.md "enable-session-stickiness-persistence-or-change-cookie-duration.md").

## When to use load balancers

You should use a load balancer when you have a website that has occasional spikes in
traffic or hosts content that can create a lot of load on an instance when many visitors are
using it at once. For example, if you have an image-heavy website, you can load balance the
image requests with the other page requests. That way, your pages load faster and your users
are happier.

You can use a load balancer to create a highly available website. _High
availability_ refers to how long your website or application stays up over a given
time period. If you have ever experienced a site outage, then a load balancer might help you
have more uptime. You can use a Lightsail load balancer to make your application highly
available by adding target instances that are distributed across multiple Availability
Zones.

_Fault tolerance_ is a related concept. If your site continues to
function even after one of your instances or your database fails, it is considered tolerant. A
load balancer can help you create a fault tolerant application or website.

## Recommended applications for load balancing

Not all Lightsail applications need load balancers. If you decide to create a
load-balanced application, you must configure your application first. For example, to prepare
a LAMP stack application for load balancing, you should first create a centralized, dedicated
database for all the target instances to read from and write to. You might also consider
creating centralized media storage, such as a Lightsail object storage bucket. For more
information, see [Configure an
instance for load balancing](configure-lightsail-instances-for-load-balancing.md "configure-lightsail-instances-for-load-balancing.md").

## Get started using load balancers

You can [create a load balancer](create-lightsail-load-balancer-and-attach-lightsail-instances.md "create-lightsail-load-balancer-and-attach-lightsail-instances.md") using the Lightsail console, the AWS Command Line Interface (AWS CLI), or the
Lightsail API. You must also [configure your instances for load
balancing](configure-lightsail-instances-for-load-balancing.md "configure-lightsail-instances-for-load-balancing.md").

After you create your load balancer and attach your configured instances, you can enable
HTTPS using the following topic. For more information, see [Create an
SSL/TLS certificate for your load balancer](create-tls-ssl-certificate-and-attach-to-lightsail-load-balancer-https.md "create-tls-ssl-certificate-and-attach-to-lightsail-load-balancer-https.md").
