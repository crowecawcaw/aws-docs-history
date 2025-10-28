# App Runner networking and compute infrastructure updates on November 18, 2024

**Release date:** November 18, 2024

## Changes

App Runner is updating its compute and networking infrastructure to enhance overall service performance and scalability. These changes include:

- Compute Update: App Runner will now launch your service on pre-warmed Amazon EC2 instances, providing dedicated resources to your
  service.
- Networking Update: App Runner will transition from shared hyperplane ENIs across services to dedicated ENIs per App Runner instance. This improves
  resource isolation, but may increase IP address utilization.

These updates will be released gradually across App Runner supported regions.

To transition your App Runner services to this new infrastructure, we will initiate an update operation on your behalf. We will contact you prior to
performing this operation. No action is required from you at this time and there are no price increases as part of this change. Review your IP address
usage in the subnets that host your App Runner services to ensure there are sufficient allocated addresses for the new networking structure. If you have any
questions or need further information about how these changes might affect your specific use case, contact Support.
