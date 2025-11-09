# Regions, quotas, and limitations

Amazon GameLift Streams is available across multiple AWS Regions, offering dual-stack service endpoints
that support both IPv4 and IPv6 connectivity. The service operates from primary locations
including US East (Ohio), US West (Oregon), Asia Pacific (Tokyo), and Europe (Frankfurt), with
the ability to manage additional AWS Regions and locations, collectively referred to as
_remote locations_, for optimized latency and stream quality.

The service infrastructure is governed by three main categories of constraints:

- Service quotas
- API rate limits
- Fixed service limitations
  These include restrictions on application sizes, number of applications per region, file
  management capacities, and GPU allocations across different stream classes and regions. The
  service implements specific API rate limits for various operations, ranging from 1 to 20
  requests per second, ensuring stable service performance. Additionally, there are fixed
  service limitations concerning stream group configurations, GPU deployments, and application
  associations that apply uniformly across all customers.
