# MAREL 2: How are critical external

system integrations set up for high availability to maintain
your platform capabilities?

Core capabilities that come from external service integrations
should be reviewed. These are out of your control and could be a
concern, especially if they are backing mission-critical
capabilities.

## MAREL02-BP01 Establish

alternatives for each critical external service to switch over
to if needed, or balance traffic across

Amazon API Gateway can be used to front calls to backend external services and handle failover if problems are detected with the primary service.

## MAREL02-BP02 Have legal

agreements in place guaranteeing the right of continued usage of
all external services

As an example, see [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/").
