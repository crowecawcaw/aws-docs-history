# Reliability pillar

The reliability pillar for connected mobility encompasses the ability of connected vehicles
to deliver the services as intended and consistently. Resiliency is a [shared responsibility](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.md") between AWS and the customer. It is important that you
understand how high availability (HA) and disaster recovery (DR), as part of resiliency, operate
under this shared model. 

As an Auto OEM, your responsibility would change based on the configuration that is needed
for a particular service. If your connected mobility uses Amazon EC2 for the connectivity gateway and
vehicle data platform, then you are responsible for deploying EC2 instances across multiple
locations such as Availability Zones and Regions,  implementing [self-healing systems](../reliability-pillar/design-your-workload-to-withstand-component-failures.md "../reliability-pillar/design-your-workload-to-withstand-component-failures.md") like AWS Auto Scaling. If you have managed services, such as API Gateway,
AWS IoT, Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system,
and platforms, and you access the endpoints to store and retrieve data. In both cases, you are
responsible for managing resiliency of your data including backup, versioning, and replication
strategies.
