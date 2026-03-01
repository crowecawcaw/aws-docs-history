# Use CloudFront continuous deployment to safely test CDN configuration changes

With Amazon CloudFront _continuous deployment_ you can safely
deploy changes to your CDN configuration by testing first with a subset of production
traffic. You can use a _staging distribution_ and a
_continuous deployment policy_ to send some traffic from
real (production) viewers to the new CDN configuration and validate that it works as
expected. You can monitor the performance of the new configuration in real time, and promote
the new configuration to serve all traffic via the _primary
distribution_ when you're ready.

The following diagram shows the benefit of using CloudFront continuous deployment. Without it,
you would have to test CDN configuration changes with simulated traffic. With continuous
deployment you can test the changes with a subset of production traffic, then promote the
changes to the primary distribution when you're ready.

![Graphic of CloudFront continuous deployment that sends production traffic to a staging distribution.](images/cloudfront-continuous-deployment.png)
Learn more about working with continuous deployment in the following topics.

###### Topics

- [CloudFront continuous deployment workflow](continuous-deployment-workflow.md "continuous-deployment-workflow.md")
- [Work with a staging distribution and continuous deployment policy](working-with-staging-distribution-continuous-deployment-policy.md "working-with-staging-distribution-continuous-deployment-policy.md")
- [Monitor a staging distribution](monitoring-staging-distribution.md "monitoring-staging-distribution.md")
- [Learn how continuous deployment works](understanding-continuous-deployment.md "understanding-continuous-deployment.md")
- [Quotas and other considerations for continuous deployment](continuous-deployment-quotas-considerations.md "continuous-deployment-quotas-considerations.md")
