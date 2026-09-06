

# Resilience in AWS Sustainability
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In the case of a service disruption, AWS Sustainability will fail over to region `us-west-2`. When using the SDK, it is recommended to use the following authentication configuration in order to allow requests to fail over to the secondary region:

```
export AWS_AUTH_SCHEME_PREFERENCE="sigv4a,sigv4"
export AWS_SIGV4A_SIGNING_REGION_SET="*"
```

For more information on SDK Authentication, see [Authentication scheme](https://docs.aws.amazon.com/sdkref/latest/guide/feature-auth-scheme.html).