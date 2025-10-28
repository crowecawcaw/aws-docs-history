# Configure custom health checks for DNS failover for an API Gateway API

You can use Amazon Route 53 health checks to control DNS failover from an API Gateway API in a primary AWS Region to one
in a secondary Region. This can help mitigate impacts in the event of a Regional issue. If you use a custom domain,
you can perform failover without requiring clients to change API endpoints.

When you choose [Evaluate Target Health](../../../Route53/latest/APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth>Evaluate Target Health "../../../Route53/latest/APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth>Evaluate Target Health") for an alias record, those records fail only when the API Gateway service is unavailable
in the Region. In some cases, your own API Gateway APIs can experience interruption before that time. To control DNS
failover directly, configure custom Route 53 health checks for your API Gateway APIs. For this example, you use a CloudWatch alarm
that helps operators control DNS failover. For more examples and other considerations when you configure failover,
see [Creating
Disaster Recovery Mechanisms Using Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/ "https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/") and [Performing Route 53 health checks on private resources in a VPC with AWS Lambda and CloudWatch](https://aws.amazon.com/blogs/networking-and-content-delivery/performing-route-53-health-checks-on-private-resources-in-a-vpc-with-aws-lambda-and-amazon-cloudwatch/ "https://aws.amazon.com/blogs/networking-and-content-delivery/performing-route-53-health-checks-on-private-resources-in-a-vpc-with-aws-lambda-and-amazon-cloudwatch/").

###### Topics

- [Prerequisites](#dns-failover-prereqs "#dns-failover-prereqs")
- [Step 1: Set up resources](#dns-failover-intial-setup "#dns-failover-intial-setup")
- [Step 2: Initiate failover to the secondary Region](#dns-failover-initiate "#dns-failover-initiate")
- [Step 3: Test the failover](#dns-failover-test "#dns-failover-test")
- [Step 4: Return to the primary region](#dns-failover-return "#dns-failover-return")
- [Next steps: Customize and test regularly](#dns-failover-next-steps "#dns-failover-next-steps")

## Prerequisites

To complete this procedure, you must create and configure the following resources:

- A domain name that you own.
- An ACM certificate for that domain name in two AWS Regions. For more info, see [Prerequisites for custom domain names](how-to-custom-domains.md#how-to-custom-domains-prerequisites "how-to-custom-domains.md#how-to-custom-domains-prerequisites").
- A Route 53 hosted zone for your domain name. For more information, see [Working with hosted zones](../../../Route53/latest/DeveloperGuide/hosted-zones-working-with.md "../../../Route53/latest/DeveloperGuide/hosted-zones-working-with.md") in the
  Amazon Route 53 Developer Guide.

For more information on how to create Route 53 failover DNS records for the domain names, see [Choose a routing policy](../../../Route53/latest/DeveloperGuide/routing-policy.md "../../../Route53/latest/DeveloperGuide/routing-policy.md") in the
Amazon Route 53 Developer Guide. For more information on how to monitor a CloudWatch alarm, see [Monitoring a CloudWatch alarm](../../../Route53/latest/DeveloperGuide/health-checks-creating-values.md#health-checks-creating-values-cloudwatch "../../../Route53/latest/DeveloperGuide/health-checks-creating-values.md#health-checks-creating-values-cloudwatch") in the
Amazon Route 53 Developer Guide.

## Step 1: Set up resources

In this example, you create the following resources to configure DNS failover for your domain name:

- API Gateway APIs in two AWS Regions
- API Gateway custom domain names with the same name in two AWS Regions
- API Gateway API mappings that connect your API Gateway APIs to the custom domain names
- Route 53 failover DNS records for the domain names
- A CloudWatch alarm in the secondary Region
- A Route 53 health check based on the CloudWatch alarm in the secondary Region

First, make sure that you have all of the required resources in the primary and secondary Regions. The
secondary Region should contain the alarm and health check. This way, you don't depend on the primary Region to
perform failover. For example AWS CloudFormation templates that create these resources, see [`primary.yaml`](samples/primary.md "samples/primary.md") and [`secondary.yaml`](samples/secondary.md "samples/secondary.md").

###### Important

Before failover to the secondary Region, make sure that all required resources are available. Otherwise,
your API won't be ready for traffic in the secondary Region.

## Step 2: Initiate failover to the secondary Region

In the following example, the standby Region receives a CloudWatch metric and initiates failover. We use a custom
metric that requires operator intervention to initiate failover.

```
**aws cloudwatch put-metric-data** \
    `--metric-name` `Failover` \
    `--namespace` `HealthCheck` \
    `--unit` `Count` \
    `--value` `1` \
    `--region` ``us-west-1``
```

Replace the metric data with the corresponding data for the CloudWatch alarm you configured.

## Step 3: Test the failover

Invoke your API and verify that you get a response from the secondary Region. If you used the example
templates in step 1, the response changes from `{"message": "Hello from the primary Region!"}` to
`{"message": "Hello from the secondary Region!"}` after failover.

```
**curl** ``https://my-api.example.com``

`{"message": "Hello from the secondary Region!"}`
```

## Step 4: Return to the primary region

To return to the primary Region, send a CloudWatch metric that causes the health check to pass.

```
**aws cloudwatch put-metric-data** \
    `--metric-name` `Failover` \
    `--namespace` `HealthCheck` \
    `--unit` `Count` \
    `--value` `0` \
    `--region` ``us-west-1``
```

Replace the metric data with the corresponding data for the CloudWatch alarm you configured.

Invoke your API and verify that you get a response from the primary Region. If you used the example templates
in step 1, the response changes from `{"message": "Hello from the secondary Region!"}` to
`{"message": "Hello from the primary Region!"}`.

```
**curl** ``https://my-api.example.com``

`{"message": "Hello from the primary Region!"}`
```

## Next steps: Customize and test regularly

This example demonstrates one way to configure DNS failover. You can use a variety of CloudWatch metrics or HTTP
endpoints for the health checks that manage failover. Regularly test your failover mechanisms to make sure that
they work as expected, and that operators are familiar with your failover procedures.
