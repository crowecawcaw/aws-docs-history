# Learn how continuous

deployment works

The following topics explain how CloudFront continuous deployment works.

###### Topics

- [Route requests to
  the staging distribution](#understanding-continuous-deployment-routing "#understanding-continuous-deployment-routing")
- [Session stickiness
  for weight-based configurations](#understanding-continuous-deployment-sessions "#understanding-continuous-deployment-sessions")
- [Update primary and
  staging distributions](#updating-staging-and-primary-distributions "#updating-staging-and-primary-distributions")
- [Primary and staging
  distributions don't share a cache](#staging-and-primary-no-shared-cache "#staging-and-primary-no-shared-cache")

## Route requests to

the staging distribution

When you use CloudFront continuous deployment, you don't need to change anything about
the viewer requests. Viewers cannot send requests directly to a staging distribution
using a DNS name, IP address, or CNAME. Instead, viewers send requests to the
primary (production) distribution, and CloudFront routes some of those requests to the
staging distribution based on the traffic configuration settings in the continuous
deployment policy. There are two types of traffic configurations:

**Weight-based**

A weight-based configuration routes the specified percentage of viewer
requests to the staging distribution. When you use a weight-based
configuration, you can also enable _session
stickiness_, which helps make sure that CloudFront treats requests
from the same viewer as part of a single session. For more information,
see [Session stickiness
for weight-based configurations](#understanding-continuous-deployment-sessions "#understanding-continuous-deployment-sessions").

**Header-based**

A header-based configuration routes requests to the staging
distribution when the viewer request contains a specific HTTP header
(you specify the header and the value). Requests that don't contain the
specified header and value are routed to the primary distribution. This
configuration is useful for local testing, or when you have control over
the viewer requests.

###### Note

Headers routed to your staging distribution must contain the
prefix `aws-cf-cd-`.

## Session stickiness

for weight-based configurations

When you use a weight-based configuration to route traffic to a staging
distribution, you can also enable _session
stickiness_, which helps make sure that CloudFront treats requests from the same
viewer as a single session. When you enable session stickiness, CloudFront sets a cookie
so that all requests from the same viewer in a single session are served by one
distribution, either the primary or staging.

When you enable session stickiness, you can also specify the _idle duration_. If the viewer is idle (sends no requests)
for this amount of time, the session expires and CloudFront treats future requests from
this viewer as a new session. You specify the idle duration as a number of seconds,
from 300 (five minutes) to 3600 (one hour).

In the following cases, CloudFront resets all sessions (even active ones) and considers
all requests to be a new session:

- You disable or enable the continuous deployment policy
- You disable or enable the session stickiness setting

## Update primary and

staging distributions

When a primary distribution has an attached continuous deployment policy, the
following configuration changes are available for both primary and staging
distributions:

- All cache behavior settings, including the default cache behavior
- All origin settings (origins and origin groups)
- Custom error responses (error pages)
- Geographic restrictions
- Default root object
- Logging settings
- Description (comment)

You can also update external resources that are referenced in a distribution's
configuration—such as a cache policy, a response headers policy, a CloudFront function, or
a Lambda@Edge function.

## Primary and staging

distributions don't share a cache

The primary and staging distributions don't share a cache. When CloudFront sends the
first request to a staging distribution, its cache is empty. As requests arrive at
the staging distribution, it begins caching responses (if configured to do
so).
