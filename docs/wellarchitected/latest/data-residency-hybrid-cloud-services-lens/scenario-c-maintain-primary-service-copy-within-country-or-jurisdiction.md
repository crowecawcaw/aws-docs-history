

# Scenario C: Maintain primary service copy within country or jurisdiction
<a name="scenario-c-maintain-primary-service-copy-within-country-or-jurisdiction"></a>

 In a scenario where the law mandates data residency requirements that specify that the primary copy of the data must be maintained within the country or jurisdiction, several factors should be considered. 

 In this case, in-scope data can be stored or transferred outside the borders, but the primary servicing copy must be held within the border of your jurisdiction. 

 For your deployment needs, you have two options depending on the availability of Local Zones in your [location](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/) and the specific workloads you need to deploy, as outlined in the following diagrams: 

![Reference architecture that uses Local Zones to navigate maintaining a primary service copy of data within a country or jurisdiction](http://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/images/scenario-C-local-zones.png)


The first option for deploying AWS services specifically focuses on the use of AWS Local Zones and AWS Outposts:

1.  Assess data residency requirements specific to the organization and regulatory environment, and identify regulated data. 

1.  Plan, order, and deploy [AWS Outposts racks](https://aws.amazon.com/outposts/rack/) in the corporate data centers for [high availability](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.html) alongside [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/). 

1.  (Optional) Set up the [landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/setting-up.html) for centralized management and governance. Then add the Outpost accounts to your AWS Organization. 

1.  Configure access levels for your accounts for proper permissions and security. 

1.  Deploy regulated workloads on AWS Local Zones and AWS Outposts. Optionally, you can configure backups and snapshots to be stored within the Region and synchronize your Amazon S3 data accordingly. 

![Reference architecture that uses Outposts to navigate maintaining a primary service copy of data within a country or jurisdiction](http://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/images/scenario-C-outposts.png)


 The second option for deploying AWS services focuses on the use of AWS Outposts: 

1.  Assess data residency requirements specific to the organization and regulatory environment, and identify regulated data. 

1.  Plan, order, and deploy [AWS Outposts racks](https://aws.amazon.com/outposts/rack/) in the corporate data centers with [high availability](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.html). 

1.  (Optional) Set up the [landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/setting-up.html) for centralized management and governance. Then add the Outpost accounts to your AWS Organization. 

1.  Configure access levels for your accounts for proper permissions and security. 

1.  Deploy regulated workloads on AWS Outposts. Optionally, you can configure backups and snapshots to be stored within the Region and synchronize your Amazon S3 data accordingly. 