# Elastic Load Balancing and AWS X-Ray

Elastic Load Balancing application load balancers add a trace ID to incoming HTTP requests in a header
named `X-Amzn-Trace-Id`.

```
X-Amzn-Trace-Id: Root=1-5759e988-bd862e3fe1be46a994272793
```

###### X-Ray trace ID format

An X-Ray `trace_id` consists of three numbers separated by hyphens. For example,
`1-58406520-a006649127e371903a2de979`. This includes:

- The version number, which is `1`.
- The time of the original request in Unix epoch time using **8 hexadecimal
  digits**.

For example, 10:00AM December 1st, 2016 PST in epoch time is `1480615200` seconds or
`58406520` in hexadecimal digits.

- A globally unique 96-bit identifier for the trace in **24 hexadecimal
  digits**.
  Load balancers do not send data to X-Ray, and do not appear as a node on your service
  map.

For more information, see [Request Tracing for Your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-request-tracing.md "../../../elasticloadbalancing/latest/application/load-balancer-request-tracing.md") in the Elastic Load Balancing Developer
Guide.
