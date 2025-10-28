# Partner data sources on SiteWise Edge

gateways

When using an AWS IoT SiteWise Edge gateway you can connect a partner data source to your
SiteWise Edge gateway and receive data from the partner in your SiteWise Edge gateway and the
AWS cloud. These partner data sources are AWS IoT Greengrass components that are developed in
partnership between AWS and the partner. When you add a partner data source,
AWS IoT SiteWise will create this component and deploy it on your SiteWise Edge gateway.

###### Note

You can add one data source for each partner in each gateway.

To add a partner data source, do the following:

1. [Add a partner data source in SiteWise Edge](cpa-add-source.md "cpa-add-source.md")
2. Go to the partner’s web portal, where applicable, and configure the
   partner data source so it connects to the SiteWise Edge gateway.

###### Topics

- [Security](#cpa-security "#cpa-security")
- [Set up Docker on your
  SiteWise Edge gateway](cpa-install-docker.md "cpa-install-docker.md")
- [Add a partner data source in SiteWise Edge](cpa-add-source.md "cpa-add-source.md")
- [SiteWise Edge gateway partner data
  source options](connect-partner-data-source.md "connect-partner-data-source.md")

## Security

As part of the [Shared Responsibility
Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") between AWS, our customers, and our partners the following
describes who is responsible for the different aspects of security:

**Customer responsibility**

- Vetting the partner.
- Configuring the network access given to the partner.
- Monitoring for reasonable usage of the SiteWise Edge gateway
  machine resources (CPU, memory, and file system).

**AWS responsibility**

- Isolating the partner from the customer AWS cloud
  resources except those needed by the partner. In this case,
  AWS IoT SiteWise ingestion.
- Restricting the partner solution to a reasonable usage of
  the SiteWise Edge gateway machine resources (CPU and
  memory).

**Partner responsibility**

- Using secure defaults.
- Keeping the solution secure over time through patches and
  other appropriate updates.
- Keeping customer data confidential.
