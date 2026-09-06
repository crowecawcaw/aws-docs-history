

# Document revisions
<a name="revisions"></a>

The following table describes important changes to this documentation.


| Date | Change | Description | 
| --- | --- | --- | 
| July 2026 | Predictive Maintenance generalized beyond tires | Chapter title changed from "Tire Predictive Maintenance for Commercial Fleets" to "Predictive Maintenance" — matches the un-qualified title convention used by sibling use-case chapters (Customer 360, Automotive Data Mesh). Added a "Beyond tires" section framing the tire reference implementation as one instance of a domain-agnostic five-stage architecture (ingestion, feature engineering, training, inference, alert consolidation) applicable to manufacturing, HVAC, stationary battery storage, and other asset classes. Added a "Choosing an approach" comparison table surveying SageMaker-native algorithm options beyond Random Cut Forest (XGBoost, DeepAR\+, Canvas). Added a closing "Adapting this pattern to a different asset class" section identifying which parts of the tire-specific walkthrough change per asset class versus which parts carry over unchanged. | 
| July 2026 | v0.2 re-frame | Full re-frame to the v0.2 platform-foundation model: 9 governed data products via DataZone V2, 5-stack-per-stage \+ bootstrap topology, cross-cutting Lake Formation \+ Macie \+ CloudTrail governance layer. Adds new chapters "Platform foundation" and "Data products". See docs/MIGRATION-FROM-V0.1.0.md. | 
| July 2026 | Living pattern-guide convention | Retired version-gated deprecation as a convention for this guide. Customer 360, Predictive Maintenance, Automotive Data Governance, and Telemetry Normalization are restored as active use-case pattern chapters — a use case remaining in this guide does not imply it ships as deployable code in the current release; see "About This Guide" in the Guidance Overview chapter. Predictive Maintenance additionally corrected to reflect that its reference implementation code remains present, undeleted, in `guidance-for-predictive-maintenance/`. | 
| May 2026 | Predictive Maintenance content update | Updated the Predictive Maintenance guidance to reflect the publicly available source at [github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws). Title updated to "Tire Predictive Maintenance for Commercial Fleets". Vendor-specific attribution removed throughout the abstract and introduction. AWS resource name references (S3 buckets, Glue databases, IAM roles, CloudFormation stacks, SSM parameters, Lambda functions) updated to match the published source’s renamed resources. | 
| January 2026 | Initial release | Initial publication of the Automotive Data Platform on AWS Implementation Guide. Includes Customer 360 Analytics, Predictive Maintenance, and Platform Foundation guidance. | 

To be notified about updates to this documentation, subscribe to the RSS feed.