# Getting started with multi-Region recovery in Amazon Application Recovery Controller (ARC)

To fail over your applications by using routing control in Amazon Application Recovery Controller (ARC), you must have AWS applications
that are in multiple AWS Regions. To get started, first, make sure that your applications are set
up in siloed replicas in each Region, so that you can fail over from one to another during an event.
Then, you can create routing controls to reroute the application traffic to fail over from
a primary application to a secondary, maintaining continuity for your users.

###### Note

If you have an application that is siloed by Availability Zones, consider using zonal shift or
zonal autoshift for failover recovery. No setup is required to use zonal shift or zonal autoshift to reliably
recover applications from Availability Zone impairments. For more information, see [Use zonal shift and zonal autoshift to recover applications in ARC](multi-az.md "multi-az.md").

So that you can use ARC routing control to recover applications during an event, we recommend
that you set up at least two applications that are replicas of each other. Each replica, or _cell_,
represents an AWS Region. After you've set up your application resources to align with
Regions, make sure that your application set up for successful recovery by taking the following steps.

Tip: To help simplify setup, we provide AWS CloudFormation and HashiCorp Terraform templates that create an
application with redundant replicas that fail independently of one another. To learn more
and download the templates, see [Setting up an example app](#getting-started-example "#getting-started-example").

To prepare to use routing control, make sure that your application is set up to be resilient by
doing the following:

1. Build independent copies of your application stack (networking and compute layer) that
   are replicas of each other in each Region so that you can fail over traffic from one to the other when there's
   an event. Make sure that you don't have
   any cross-Region dependencies in your application code that would cause the failure of one replica
   to impact the other. To successfully fail over between AWS Regions, your stack
   boundaries should be within a Region.
2. Duplicate all the required stateful data for your application across the replicas.
   You can use AWS database services to help replicate your data.

## Get

started with routing control for traffic failover

Routing control in Amazon Application Recovery Controller (ARC) enables you to trigger failover for your traffic
to fail over between redundant application copies, or replicas, that are running in separate AWS Regions.
Failover is performed with DNS, using the Amazon Route 53 data plane.

After you set up your replicas in each Region, as described in the next section, you can associate each one with a
routing control. First, you associate routing controls with the top-level domain names of your replicas
in each Region. Then, you add a routing control health check to the routing control so that it can turn traffic flow
on and off. This enables you to control traffic routing across replicas of your application.

You can update routing control states in the AWS Management Console to fail over traffic, but we recommend that instead
you use ARC actions, using the API or AWS CLI, to change them. API actions aren't dependent on
the console, so they're more resilient.

For example, to fail over between Regions, from us-west-1 to
us-east-1, you can use the `update-routing-control-state` API action to set
the state of `us-west-1` to `Off` and `us-east-1` to
`On`.

Before you create routing control components to set up failover for your application, make sure
that your application is siloed into Regional replicas, so that you can fail over
from one to the other. To learn more and get started siloing a new application or creating a
example stack, see the next sections.

## Setting up an example app

To help you understand how routing control works, we provide an example application called
`TicTacToe`. The example uses AWS CloudFormation templates to simplify the
process, as well as a downloadable AWS CloudFormation template so that you can quickly explore
setting up and using ARC yourself.

After you deploy the sample app, you can use the templates to create ARC components,
and then explore using routing controls to manage traffic flow to the app. You can
adapt the template and process for your own scenario and applications.

To get started with a sample application and AWS CloudFormation templates, see the README instructions
in the [ARC GitHub
repo](https://github.com/aws-samples/r53-arc-iad "https://github.com/aws-samples/r53-arc-iad"). You can learn more about using AWS CloudFormation templates by reading [AWS CloudFormation
concepts](../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md "../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md") in the AWS CloudFormation User Guide.
