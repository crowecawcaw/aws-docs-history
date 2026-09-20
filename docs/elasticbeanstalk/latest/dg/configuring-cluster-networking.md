

# Configuring networking for Beanstalk Cluster environments
<a name="configuring-cluster-networking"></a>

Beanstalk Cluster runs your environment on an Amazon EKS cluster. The subnets that you select do two things: they determine where the cluster's nodes run, and they determine which cluster runs the environment. If you don't select any subnets, Elastic Beanstalk uses the public subnets of the default VPC.

This topic covers the environment's subnets, how traffic reaches your application from outside the cluster, and how your environments address each other inside the cluster.

## Environment subnets
<a name="configuring-cluster-networking-subnets"></a>

Set the `subnets` option in the `aws:elasticbeanstalk:eks:environment` namespace to a comma-separated list of subnet IDs.

Because subnets select the cluster, you set them when you create the environment:

```
$ aws elasticbeanstalk create-environment \
    --application-name {{my-app}} \
    --environment-name {{my-cluster-env}} \
    --option-settings '[{"Namespace":"aws:elasticbeanstalk:eks:environment","OptionName":"subnets","Value":"{{subnet-abc123,subnet-def456}}"}]'
```

The setting is written as JSON because the subnet list contains a comma, which the AWS CLI shorthand form treats as a separator between fields. For the forms that the AWS CLI accepts, see [Using shorthand syntax in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html).

Elastic Beanstalk groups environments onto clusters by this subnet set, so environments in the same account that use the same subnets run on the same cluster, and an environment that uses a different set runs on a different cluster. The order of the subnets doesn't matter. For the grouping rules and the events that report cluster assignment, see [Environment grouping](beanstalk-cluster-concepts.md#beanstalk-cluster-clusters-sharing).

## How traffic reaches your application
<a name="configuring-cluster-networking-lb-type"></a>

The `load-balancer-type` option in the `aws:elasticbeanstalk:eks:environment` namespace chooses how traffic reaches your application. It accepts two values:
+ `ALB`, the default. Elastic Beanstalk creates and operates an Application Load Balancer for the environment. You can configure it through the `aws:elasticbeanstalk:eks:alb` namespace, or supply an Application Load Balancer that you already own.
+ `None`. Elastic Beanstalk doesn't create a load balancer, and the environment isn't reachable from outside the cluster through Elastic Beanstalk. Other environments on the same cluster can still reach it by its in-cluster address.

## Load balancer network settings
<a name="configuring-cluster-networking-alb"></a>

The environment's Application Load Balancer has its own network settings in the `aws:elasticbeanstalk:eks:alb` namespace.


| Option | Default | Description | 
| --- | --- | --- | 
| subnets | None | A comma-separated list of subnets for the load balancer. | 
| scheme | Derived from your subnets | Whether the load balancer is reachable from the internet, either internet-facing or internal. If you don't set it, Elastic Beanstalk derives it from the subnets that you select: public subnets give an internet-facing load balancer, and private subnets give an internal one. | 
| security-groups | None | A comma-separated list of security groups for the load balancer. | 
| manage-backend-security-group-rules | true | Whether Elastic Beanstalk manages the security group rules between the load balancer and your application. | 

## Listeners and HTTPS
<a name="configuring-cluster-networking-listeners"></a>

The `listen-ports` option in the `aws:elasticbeanstalk:eks:alb` namespace lists the load balancer's listeners as a JSON array that maps each protocol to a port, for example `[{"HTTPS":443},{"HTTP":80}]`.

Elastic Beanstalk makes sure that the load balancer terminates HTTPS somewhere:
+ If you don't set `listen-ports`, Elastic Beanstalk configures an HTTPS listener on port 443.
+ If you set `listen-ports` and it already includes an HTTPS listener on any port, Elastic Beanstalk uses your configuration unchanged.
+ If you set `listen-ports` without an HTTPS listener, Elastic Beanstalk adds one on port 443. If port 443 is already taken by a listener that uses another protocol, the request fails, and the error tells you to free port 443 or add an explicit HTTPS listener on a different port.

The load balancer opens only the listeners that it is configured with. With the default configuration, that is HTTPS on port 443 and nothing on port 80, so a request to `http://` doesn't connect and waits until it times out. Your environment's URL is `https://` followed by the environment's CNAME. `DescribeEnvironments` returns the CNAME without a scheme, so add `https://` when you open it.

You don't supply a certificate for this to work. Elastic Beanstalk creates an AWS Certificate Manager (ACM) certificate for the environment's own domain, attaches it to the HTTPS listener, and renews it, so a browser trusts the environment's CNAME without any configuration. Elastic Beanstalk creates one certificate for each environment and deletes it when you terminate the environment.

To serve the environment from a domain of your own, put your certificate's ARN in the `certificate-arn` option. The load balancer then carries your certificate in addition to the one that Elastic Beanstalk created, and you remain responsible for renewing and deleting yours.

To accept HTTP requests as well, add an HTTP listener to `listen-ports` and set `ssl-redirect` to the port of an HTTPS listener. Elastic Beanstalk redirects requests on HTTP listeners to your HTTPS listener. An HTTP listener never serves application traffic directly. `ssl-redirect` selects which HTTPS port the redirect targets, and if you don't set it, Elastic Beanstalk uses your HTTPS listener's port. A `listen-ports` value is itself a JSON document, so pass the settings in a file rather than writing them on the command line:

```
$ cat listeners.json
[
  {
    "Namespace": "aws:elasticbeanstalk:eks:alb",
    "OptionName": "listen-ports",
    "Value": "[{\"HTTPS\":443},{\"HTTP\":80}]"
  },
  {
    "Namespace": "aws:elasticbeanstalk:eks:alb",
    "OptionName": "ssl-redirect",
    "Value": "443"
  }
]
$ aws elasticbeanstalk update-environment \
    --environment-name {{my-cluster-env}} \
    --option-settings file://listeners.json
```

Elastic Beanstalk doesn't add the HTTPS listener when you set `load-balancer-type` to `None`, or when you supply your own load balancer with `arn`. With `None` the environment has no load balancer at all, so it has no listeners. When you supply your own load balancer, its listener configuration is yours to manage.

## Using a load balancer that you own
<a name="configuring-cluster-networking-byo-alb"></a>

To put an existing load balancer in front of the environment, set the `arn` option in the `aws:elasticbeanstalk:eks:alb` namespace to its ARN. The value must be an Application Load Balancer. Elastic Beanstalk rejects the ARN of a Network Load Balancer.

When you supply a load balancer, you own its configuration: its listeners, its TLS certificate, and its scheme. Elastic Beanstalk registers your application as a target and reports your load balancer as the environment's load balancer, so `DescribeEnvironmentResources` returns the load balancer that you supplied rather than one that Elastic Beanstalk created.

## Environments without a load balancer
<a name="configuring-cluster-networking-no-lb"></a>

When you set `load-balancer-type` to `None`, Elastic Beanstalk doesn't create a load balancer for the environment, and `DescribeEnvironmentResources` reports no load balancers. Use this for an environment that only serves other environments on the same cluster, such as an internal API or a worker that its callers reach directly.

Two consequences to plan for:
+ The load balancer health signals don't apply, because there is no load balancer to report a request rate, an error rate, or latency. Use container probes and your observability backends to judge whether the application is working. See [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md).
+ Callers reach the environment by its in-cluster address, described in the next section.

## Addressing one environment from another
<a name="configuring-cluster-networking-service-discovery"></a>

Each Beanstalk Cluster environment is reachable inside its cluster at a predictable address that is built from the environment's name:

```
service-{{environment-name}}.eb-{{environment-name}}.svc.cluster.local:{{service-port}}
```

The port is the environment's `service-port`. Elastic Beanstalk runs each environment in a Kubernetes namespace named `eb-` followed by the environment name, which is the second label of the address. Pass the addresses that your application needs as environment variables, using the `env-variables` option in the `aws:elasticbeanstalk:eks:environment` namespace:

The value of `env-variables` is itself a JSON document, so pass the option settings in a file rather than on the command line. Save the following as `options.json`:

```
[
  {
    "Namespace": "aws:elasticbeanstalk:eks:environment",
    "OptionName": "env-variables",
    "Value": "{\"NOTIFIER_URL\":\"http://service-{{my-notifier}}.eb-{{my-notifier}}.svc.cluster.local:8080\"}"
  }
]
```

Then apply it:

```
$ aws elasticbeanstalk update-environment \
    --environment-name {{my-frontend}} \
    --option-settings file://options.json
```

This addressing works only between environments that run on the same cluster, which means environments that use the same subnets. Resolving the address is not the same as being allowed to connect. Beanstalk Cluster blocks traffic between environments on a shared cluster by default, so the name resolves and the connection still fails until you permit it. See [Permitting environments to communicate](beanstalk-cluster-multi-tenancy.md#beanstalk-cluster-multi-tenancy-groups).

**Note**  
Because the address contains the environment name, you need to know the name of an environment before another environment can address it. Plan the names of a set of environments that call each other before you create them.

## Settings that you choose at creation
<a name="configuring-cluster-networking-immutable"></a>

You can't change an environment's subnets after you create it, because they select its cluster. The same applies to the cluster, node, and observability roles. To run your application in different subnets, create a new environment with the subnets that you want, and then swap the two environment CNAMEs. See [Blue/Green deployments with Elastic Beanstalk](using-features.CNAMESwap.md).