# Container services

## What can I do with Lightsail

container services?

Lightsail container services provide an easy way to run containerized applications in
the cloud. You can run a variety of applications on a container service, ranging from simple
web apps to multi-tiered micro services. You just specify the container image, power (CPU,
RAM) and scale (number of nodes) required for your container service. Lightsail takes care
of running the container service without you having to manage any underlying infrastructure.
Lightsail will provide you with a load balanced TLS endpoint to access the application
running on the container service.

## Can Lightsail container service run Docker

containers?

Yes. Lightsail supports Linux-based Docker containers. Windows containers are
currently not supported.

## How do I use my public

container images with Lightsail container service?

You can use container images from an online public registry, such as Amazon ECR Public
Registry, or build your own custom image and push it to Lightsail in a few easy steps
using the AWS CLI. For more information, see [Push and manage container
images](amazon-lightsail-pushing-container-images.md "amazon-lightsail-pushing-container-images.md").

## Can I pull my container images from a

private container registry?

Currently, only public container registries are supported by Lightsail container
services. Alternately, you can push your custom container images from your local machine to
Lightsail to keep them private.

## Can I change the power and scale of my

service based on demand?

Yes, container service power and scale can be changed at any time even after the service
is created.

## Can I customize the name of the HTTPS

endpoint created by Lightsail container service?

Lightsail provides a HTTPS endpoint for every container service in the format
``<service-name>`.`<random-guid>`.`<aws-region-name>`.cs.amazonlightsail.com`.
Only the service name can be customized. Alternately, you can use a custom domain name. For
more information, see [Enable and manage
custom domains](amazon-lightsail-enabling-container-services-custom-domains.md "amazon-lightsail-enabling-container-services-custom-domains.md").

## Can I use custom domains for

the HTTPS endpoint of a Lightsail container service?

Yes. You can create and attach an SSL/TLS certificate with custom domain names to your
container service in Lightsail. The certificates must be domain validated. If the DNS of
your domain uses a Lightsail DNS zone, you can route traffic for the apex of your domain
(`example.com`) or a subdomain (`www.example.com`) to your container
services. Alternately, you can use a DNS hosting provider who supports adding ALIAS records
to map the apex of your domain (`example.com`) to the default domain (public DNS)
of your Lightsail container service. For more information, see [Enable and manage
custom domains](amazon-lightsail-enabling-container-services-custom-domains.md "amazon-lightsail-enabling-container-services-custom-domains.md").

## What do Lightsail container services

cost?

Lightsail container services are billed on an on-demand hourly rate, so you pay only
for what you use. For every Lightsail container service you use, we charge you the fixed
hourly price, up to the maximum monthly service price. Maximum monthly service price can be
calculated by multiplying the base price of the power of your service with the scale of your
service. For example, a service of Micro power and scale of 2 will cost a maximum of
$10\*2=$20/month. The least expensive Lightsail container service starts at $0.0094
USD/hour ($7 USD/month). Additional data transfer charges may apply for usage above the
free-quota of 500 GB per month for each service.

## Will I be charged

for the whole month even if I run my container service for a few days?

Your Lightsail container services are charged only when they're in the running or
disabled state. If you delete your Lightsail container service before the end of the
month, we charge you a prorated cost based on the total number of hours that you used your
Lightsail container service. For example, if you use your Lightsail container service
with a power of Micro and scale of 1 for 100 hours in a month, you will be charged $1.34
($0.0134\*100)

## Will I be charged for data

transfer in and out of the container service?

Every container service comes with a data transfer quota (500 GB per month). This counts
towards both the data transfer IN and OUT of your service. When you exceed the quota, you
will get charged for data transfer OUT from a Lightsail container service to the Internet
or to another AWS Region or to AWS resources in the same Region when using public IP
addresses. The charge for these types of data transfer above the free allowance is as
follows.

###### Charges for exceeding the monthly data transfer quota

- US East (Ohio) (us-east-2): $0.090 USD/GB
- US East (N. Virginia) (us-east-1): $0.090 USD/GB
- US West (Oregon) (us-west-2): $0.090 USD/GB
- Asia Pacific (Jakarta) (ap-southeast-3): $0.132 USD/GB
- Asia Pacific (Mumbai) (ap-south-1): $0.130 USD/GB
- Asia Pacific (Seoul) (ap-northeast-2): $0.130 USD/GB
- Asia Pacific (Singapore) (ap-southeast-1): $0.120 USD/GB
- Asia Pacific (Sydney) (ap-southeast-2): $0.170 USD/GB
- Asia Pacific (Tokyo) (ap-northeast-1): $0.140 USD/GB
- Canada (Central) (ca-central-1): $0.090 USD/GB
- EU (Frankfurt) (eu-central-1): $0.090 USD/GB
- EU (Ireland) (eu-west-1): $0.090 USD/GB
- EU (London) (eu-west-2): $0.090 USD/GB
- EU (Paris) (eu-west-3): $0.090 USD/GB
- EU (Stockholm) (eu-north-1): $0.090 USD/GB

## What is the

difference between stopping and deleting my container service?

When you disable your container service, your container nodes are in a disabled state
and the public endpoint of the service returns a HTTP status code ‘503’. Enabling the
service restores it to the last active deployment. Power and scale configurations are also
retained. Public endpoint name does not change after re-enabling. Deployment history and
container images are preserved.

When you delete your container service, you are performing a destructive action. All the
container nodes of the service will be permanently deleted. The HTTPS public endpoint
address, container images, deployment history, and logs associated with your service will
also be permanently deleted. You will not be able to recover the endpoint address.

## Will I be charged if my container service is in a

disabled state?

Yes, you are charged according to the power and scale configuration of your container
service, even when it is in a disabled state.

## Can I use container services as the origin to my

Lightsail content delivery network (CDN) distributions?

Container services are currently not supported as origins for Lightsail CDN
distributions.

## Can I use container services as targets for

my Lightsail load balancer?

No. Container services are currently not available as targets for Lightsail load
balancers. However, the public endpoints of container services come with built-in load
balancing.

## Can I configure the public endpoint of

my container service to redirect HTTP requests to HTTPS?

Lightsail container service public endpoints automatically redirect all HTTP requests
to HTTPS to ensure that your content is served securely.

## Do container services support monitoring and

alerting?

Container services provide metrics for CPU utilization and memory utilization across the
nodes of your service. Alerting based on these metrics is currently not supported.

## Do Lightsail container services support

IPv6?

Lightsail container service HTTPS endpoints support both IPv4 and IPv6. Pv6 cannot be
disabled on container services.
