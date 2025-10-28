# Load balancers

## What can I do with Lightsail load

balancers?

Lightsail load balancers allow you to build highly available websites and
applications. By distributing traffic across instances in different Availability Zones and
pointing traffic to only healthy target instances, Lightsail load balancers reduce the
risk of your application going down due to an issue with your instance or to a datacenter
outage. With Lightsail load balancers and multiple target instances, your website or
application can also accommodate increases in web traffic and maintain good performance for
your visitors during peak load times.

In addition, you can use Lightsail load balancers to help you build secure
applications and accept HTTPS traffic. Lightsail takes the complexity out of requesting,
provisioning, and maintaining SSL/TLS certificates. The built-in certificate management
requests and renews certificates on your behalf and adds the certificate to your load
balancer automatically.

## Can I use

load balancers with instances in different AWS Regions or different Availability
Zones?

You cannot use load balancers with instances running in different AWS Regions. You
can, however, use target instances across different Availability Zones with your load
balancer. In fact, we recommend that you distribute your target instances across
Availability Zones to maximize the availability of your application.

## How does my Lightsail

load balancer deal with traffic spikes?

Lightsail load balancers scale automatically to handle traffic spikes to your
application without you having to manually adjust them. If your application experiences a
transient spike in traffic, your Lightsail load balancer will automatically scale and
continue to efficiently direct traffic to your Lightsail instances. While your Lightsail
load balancer is designed to easily manage traffic spikes, applications that consistently
experience very high volume levels of traffic may experience performance degradation or
throttling. If you expect your application consistently to manage more than 5 GB/hour of
data or consistently to have a large number of connections (>400k new connections/hour,

> 15k active, concurrent connections), we recommend using Amazon EC2 with Application Load
> Balancing instead.

## How do Lightsail load

balancers route traffic to my target instances?

Lightsail load balancers direct traffic to your healthy target instances based on a
round robin algorithm.

## How does Lightsail know if my

target instances are healthy?

After you create your load balancer and attach your instances, Lightsail sends a
health check request to the root of your web application. You can customize the location by
specifying a path (a common file or webpage URL) for Lightsail to ping. If the target
instance can be reached using this path, then Lightsail will route traffic there. If one
of your target instances is unresponsive, the health check fails and Lightsail will not
route traffic to that instance. [Learn more about health checking](enable-set-up-health-checking-for-lightsail-load-balancer-metrics.md "enable-set-up-health-checking-for-lightsail-load-balancer-metrics.md")

## How many instances I can

attach to my load balancer?

You can add as many target instances to your load balancer as you would like - up to
your Lightsail account instance quota.

## Can I assign one

instance to multiple load balancers?

Yes, Lightsail supports adding instances as target instances for more than one load
balancer, if desired.

## What happens to my

target instances when I delete my load balancer?

If you delete your load balancer, the attached target instances will continue to run
normally and will appear in the Lightsail console as regular Lightsail instances. Please
note that you will likely need to update your DNS records to direct traffic to one of your
former target instances after you delete the load balancer.

## What is session persistence?

Session persistence enables the load balancer to bind a visitor's session to a specific
target instance. This ensures that all requests from the user during the session are sent to
the same target instance. Lightsail supports session persistence for applications that
require visitors to hit the same target instances for data consistency. For example, many
applications that require user authentication can benefit from using session persistence.
You can turn on session persistence for specific load balancer from the load balancer
management screens after creation. For more information, see [Enable session
persistence for a load balancer](enable-session-stickiness-persistence-or-change-cookie-duration.md "enable-session-stickiness-persistence-or-change-cookie-duration.md").

## What kind of

connections do Lightsail load balancers support?

Lightsail load balancers support HTTP and HTTPS connections.

## Do Lightsail load balancers support

IPv6?

Lightsail load balancers created after January 12, 2021, operate in dual-stack mode by
default (i.e., they accept client traffic over both IPv4 and IPv6 protocol). IPv6 can be
enabled on load balancers created before this date through a toggle on the
**Networking** tab of the load balancer's management page. IPv6 can be
disabled on any load balancer using this toggle too.

## Do the instances behind a load

balancer need to be IPv6 enabled to use the load balancer which is IPv6 enabled?

No. Load balancers accept both IPv4 and IPv6 traffic, and seamlessly convert it to IPv4
when communicating with the instances in the backend. Hence, instances behind a load
balancer can either be dual-stack or IPv4 only.
