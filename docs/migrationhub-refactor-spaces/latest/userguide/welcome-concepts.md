AWS Migration Hub Refactor Spaces will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Refactor Spaces concepts

This section describes the key components that you can create and manage when using
AWS Migration Hub Refactor Spaces.

###### Topics

- [Environment](#welcome-concepts-environment "#welcome-concepts-environment")
- [Applications](#welcome-concepts-application "#welcome-concepts-application")
- [Services](#welcome-concepts-service "#welcome-concepts-service")
- [Route](#welcome-concepts-route "#welcome-concepts-route")

## Environment

The Refactor Spaces environment contains Refactor Spaces applications and services. The environment
provides the infrastructure, multi-account networking, and routing that you need to modernize
incrementally, along with a unified view of networking, applications, and services across
multiple AWS accounts. Refactor Spaces also includes a multi-account network fabric consisting of
bridged virtual private clouds (VPCs). This way, resources within the fabric can interact
through private IP addresses.

The _environment owner_ is the account that the Refactor Spaces environment is
created in. The environment owner has cross-account visibility into applications, services, and
routes created in the environment, regardless of the account that creates the resource.

## Applications

A Refactor Spaces application contains services and routes and provides a single external
endpoint to expose the application to external callers. The application provides a Strangler Fig
proxy for incremental application refactoring. For information about Strangler Fig, see [Strangler Fig
Application](https://martinfowler.com/bliki/StranglerFigApplication.html "https://martinfowler.com/bliki/StranglerFigApplication.html").

The Refactor Spaces application models the Strangler Fig pattern and orchestrates Amazon API Gateway,
API Gateway VPC links, Network Load Balancer, and resource-based AWS Identity and Access Management (IAM) policies so that you can
transparently add new services to the application’s HTTP endpoint. It also incrementally routes
traffic away from your existing application to the new services. This keeps the underlying
architecture changes transparent to the application consumer.

## Services

Refactor Spaces services provide your application’s business capabilities and are reachable
through unique endpoints. Service endpoints are one of two types: an HTTP/HTTPS URL, or an
AWS Lambda function.

After the services are created, Refactor Spaces handles automatic Domain Name System (DNS)
resolution for these services. This periodic DNS resolution ensures that the route configuration
remains up-to-date and it enables users to create services with DNS names in the URL. Refactor Spaces
automatically updates the DNS name when the DNS time-to-live (TTL) expires (or every 60 seconds
for TTLs less than 60 seconds).

## Route

A Refactor Spaces route is a proxy matching rule that forwards a request to a service. Each
request is run against the set of routes configured in the application. If a rule matches, the
request is sent to the target service configured for that rule. Applications have a default
route that forwards requests to a default service if they don’t match any of the rules.

Routes can be toggled between either an active or inactive state as you prepare and release
the routes for traffic. Routes are configured on the application's Amazon API Gateway proxy.

You can create routes with path parameters. Refactor Spaces forwards the path parameters that
you define to the target service.
