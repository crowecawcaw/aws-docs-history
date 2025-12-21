# Third-party integrations with Security Lake

Amazon Security Lake integrates with multiple third-party providers. A provider may offer a
_source integration_, a _subscriber integration_,
or a _service integration_. Providers may offer one or more integration
types.

Source integrations have the following properties:

- Send data to Security Lake
- Data arrives in Apache Parquet format
- Data arrives in the [Open Cybersecurity Schema Framework (OCSF) in Security Lake](open-cybersecurity-schema-framework.md "open-cybersecurity-schema-framework.md") schema
  Subscriber integrations have the following properties:

- Read source data from Security Lake at an HTTPS endpoint or Amazon Simple Queue Service (Amazon SQS) queue,
  or by directly querying source data from AWS Lake Formation
- Able to read data in Apache Parquet format
- Able to read data in OCSF schema
  Service integrations can help you implement Security Lake and other AWS services in your
  organization. They can also provide assistance with reporting, analytics, and other use
  cases.

To search for a specific partner provider, see the [Partner Solutions Finder](https://partners.amazonaws.com/search/partners/ "https://partners.amazonaws.com/search/partners/").
To purchase a third-party product, see the [AWS
Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

To request to be added as a partner integration or become a Security Lake partner, send an email to
`<securitylake-partners@amazon.com>`.

If you use third-party integrations that send findings to AWS Security Hub CSPM, you can also review
those findings in Security Lake if the Security Hub CSPM integration for Security Lake is enabled. For
instructions on enabling the integration, see [Integration with AWS Security Hub CSPM](securityhub-integration.md "securityhub-integration.md"). For a list of third-party integrations that
send findings to Security Hub CSPM, see [Available
third-party partner product integrations](../../../securityhub/latest/userguide/securityhub-partner-providers.md "../../../securityhub/latest/userguide/securityhub-partner-providers.md") in the
_AWS Security Hub User Guide_.

Before setting up your subscribers verify your subscriber's OCSF log support. For the latest details, review
your subscriber's documentation.

## Query integration

You can query the data that Security Lake stores in AWS Lake Formation databases and tables. You can also
create third-party subscribers in the Security Lake console, API, or AWS Command Line Interface.

The Lake Formation data lake administrator must grant `SELECT` permissions on the
relevant databases and tables to the IAM identity that queries the data. You must
create a subscriber in Security Lake before querying data. For more information about how to
create a subscriber with query access, see [Managing query access for Security Lake
subscribers](subscriber-query-access.md "subscriber-query-access.md").

You can configure query integration with Security Lake for the following third-party
partners.

- Cribl –
  Search
- IBM –
  QRadar
- Palo Alto Networks – XSOAR
- Query.AI – Query Federated Search
- SOC Prime
- [Splunk](https://www.splunk.com/en_us/blog/conf-splunklive/federated-analytics-balancing-cost-efficiency-and-performance-with-data-lakes.html "https://www.splunk.com/en_us/blog/conf-splunklive/federated-analytics-balancing-cost-efficiency-and-performance-with-data-lakes.html") – Federated Analytics
- Tego Cyber

## Accenture –

MxDR

**Integration type:** Subscriber, Service

Accenture's MxDR integration with Security Lake offers real-time data
ingestion of logs and events, managed anomaly detection, threat hunting, and security
operations. This aids analytics and managed detection and response (MDR).

As a service integration, Accenture can also help you implement
Security Lake in your organization.

[Integration documentation](https://www.accenture.com/us-en/services/cloud/aws-business-group "https://www.accenture.com/us-en/services/cloud/aws-business-group")

## Aqua Security

**Integration type:** Source

Aqua Security can be added as a custom source to send audit events to
Security Lake. The audit events are converted into OCSF schema and Parquet format.

[Integration documentation](https://support.aquasec.com/support/solutions/articles/16000151820-amazon-security-lake-integration "https://support.aquasec.com/support/solutions/articles/16000151820-amazon-security-lake-integration")

## Barracuda – Email

Protection

**Integration type:** Source

Barracuda Email Protection can send events to Security Lake when new
phishing email attacks are detected. You can receive these events alongside other
security data in your data lake.

[Integration documentation](https://campus.barracuda.com/product/emailprotection/doc/98214513/integrate-amazon-security-lake-with-email-protection/ "https://campus.barracuda.com/product/emailprotection/doc/98214513/integrate-amazon-security-lake-with-email-protection/")

## Booz Allen

Hamilton

**Integration type:** Service

As a service integration, Booz Allen Hamilton uses a data-driven
approach to cybersecurity by fusing data and analytics with the Security Lake
service.

[Partner link](https://www.boozallen.com/s/solution/booz-allen-s-amazon-web-services-premier-partnership.html "https://www.boozallen.com/s/solution/booz-allen-s-amazon-web-services-premier-partnership.html")

## Bosch Software and Digital Solutions – AIShield

**Integration type:** Source

AIShield powered by Bosch provides automated
vulnerability analysis and endpoint protection for AI assets through its integration
with Security Lake.

[Integration documentation](https://docs.boschaishield.com/amazon-security-lake "https://docs.boschaishield.com/amazon-security-lake")

## ChaosSearch

**Integration type:** Subscriber

ChaosSearch offers multi-model data access to users with open APIs such
as Elasticsearch and SQL, or with the Kibana and Superset UIs included natively. You can
consume your Security Lake data in ChaosSearch without retention limits to
monitor, alert, and threat hunt. This helps you face today’s complex security
environments and persistent threats.

[Integration documentation](https://www.chaossearch.io/platform/integrations/amazon-security-lake "https://www.chaossearch.io/platform/integrations/amazon-security-lake")

## Cisco Security –

Secure Firewall

**Integration type:** Source

By integrating Cisco Secure Firewall with Security Lake, you can store
firewall logs in a structured and scalable manner. Cisco's eNcore client streams
firewall logs from the Firewall Management Center, performs schema conversion to OCSF
schema, and stores them in Security Lake.

[Integration documentation](https://github.com/CiscoSecurity/fp-05-firepower-cli/tree/ocsf "https://github.com/CiscoSecurity/fp-05-firepower-cli/tree/ocsf")

## Claroty –

xDome

**Integration type:** Source

Claroty xDome sends alerts detected within networks to Security Lake with
minimal configuration. Flexible and rapid deployment options help xDome
protect extended Internet of Things (XIoT) assets—consisting of IoT, IIoT, and
BMS assets—within your network, while automatically detecting early indicators of
threats.

[Integration documentation](https://claroty.com/resources/integration-briefs/claroty-xdome-and-amazon-security-lake "https://claroty.com/resources/integration-briefs/claroty-xdome-and-amazon-security-lake")

## CMD Solutions

**Integration type:** Service

CMD Solutions helps businesses increase their agility by integrating
security early and continuously through design, automation, and continuous assurance
processes. As a service integration, CMD Solutions can help you implement
Security Lake in your organization.

[Partner
link](https://www.cmdsolutions.com.au/service/security/ "https://www.cmdsolutions.com.au/service/security/")

## Confluent – Amazon S3

Sink Connector

**Integration type:** Source

Confluent automatically connects, configures, and orchestrates data
integrations with fully-managed, pre-built connectors. The Confluent S3 Sink
Connector lets you take raw data and sink it into Security Lake at scale in
native parquet format.

[Integration documentation](https://www.confluent.io/resources/brief/amazon-security-lake/?utm_campaign=tm.partner_cd.cwc-securitylake-newuser&utm_medium=partnerref "https://www.confluent.io/resources/brief/amazon-security-lake/?utm_campaign=tm.partner_cd.cwc-securitylake-newuser&utm_medium=partnerref")

## Contrast Security

**Integration type:** Source

**Partner product for the integration:** Contrast
Assess

Contrast Security Assess is an IAST tool offering real-time
vulnerability detection in web apps, APIs, and microservices. Assess integrates with
Security Lake to help provide centralized visibility for all your workloads.

[Integration
documentation](https://docs.contrastsecurity.com/en/aws-security-lake.html "https://docs.contrastsecurity.com/en/aws-security-lake.html")

## Cribl –

Search

**Integration type:** Subscriber

You can use Cribl Search to search Security Lake data.

[Integration
documentation](https://docs.cribl.io/search/set-up-amazon-security-lake/ "https://docs.cribl.io/search/set-up-amazon-security-lake/")

## Cribl –

Stream

**Integration type:** Source

You can use Cribl Stream to send data from any Cribl
supported third-party sources to Security Lake in OCSF schema.

[Integration
documentation](https://docs.cribl.io/stream/usecase-security-lake/ "https://docs.cribl.io/stream/usecase-security-lake/")

## CrowdStrike –

Falcon Data Replicator

**Integration type:** Source

This integration pulls data from the CrowdStrike Falcon Data Replicator
on a continuous streaming basis, transforms the data into OCSF schema, and sends it to
Security Lake.

[Integration
documentation](https://github.com/CrowdStrike/aws-security-lake "https://github.com/CrowdStrike/aws-security-lake")

## CrowdStrike –

Next Gen SIEM

**Integration type:** Subscriber

Simplify ingestion of Security Lake data with the CrowdStrike Falcon Next-Gen
SIEM data connector featuring native OCSF schema parsers. Falcon NG
SIEM revolutionizes threat detection, investigation and response by bringing
together unmatched security depth and breadth in one unified platform to stop breaches.

[Integration
documentation](https://marketplace.crowdstrike.com/listings/amazon-security-lake-data-connector " https://marketplace.crowdstrike.com/listings/amazon-security-lake-data-connector")

## CyberArk – Unified

Identify Security Platform

**Integration type:** Source

CyberArk Audit Adapter, an AWS Lambda function, collects security events
from CyberArk Identity Security Platform and sends the data to Security Lake
in OCSF schema.

[Integration documentation](https://cyberark-customers.force.com/mplace/s/#a352J000001I8I1QAK-a392J000001pB1lQAE "https://cyberark-customers.force.com/mplace/s/#a352J000001I8I1QAK-a392J000001pB1lQAE")

## Cyber Security Cloud – Cloud Fastener

**Integration type:** Subscriber

CloudFastener leverages Security Lake to make it easier
to consolidate security data from your cloud environments.

[Integration documentation](https://cloud-fastener.com/en/#securityLake "https://cloud-fastener.com/en/#securityLake")

## DataBahn

**Integration type:** Source

Centralize your security data in Security Lake using
DataBahn’s Security Data Fabric.

[Integration documentation (sign in to the DataBahn portal to review
the documentation)](https://app.cp-us01-prod01-aws.databahn.app/help/docs/highway/destinations/amazon-web-services/aws-security-lake "https://app.cp-us01-prod01-aws.databahn.app/help/docs/highway/destinations/amazon-web-services/aws-security-lake")

## Darktrace – Cyber

AI Loop

**Integration type:** Source

The Darktrace and Security Lake integration brings the power of
Darktrace self-learning to Security Lake. Insights from Cyber AI
Loop can be correlated against other data streams and elements of your
organization's security stack. The integration logs Darktrace model
breaches as security findings.

[Integration documentation (sign in to the Darktrace portal to review
the documentation)](https://customerportal.darktrace.com/product-guides/main/aws-security-lake-alerts-intro "https://customerportal.darktrace.com/product-guides/main/aws-security-lake-alerts-intro")

## Datadog

**Integration type:** Subscriber

Datadog Cloud SIEM detects real-time threats to your cloud environment,
including data in Security Lake, and unifies DevOps and security teams in one
platform.

[Integration
documentation](https://docs.datadoghq.com/integrations/amazon_security_lake "https://docs.datadoghq.com/integrations/amazon_security_lake")

## Deloitte – MXDR

Cyber Analytics and AI Engine (CAE)

**Integration type:** Subscriber, Service

Deloitte MXDR CAE helps you quickly store, analyze, and visualize your
standardized security data. The CAE suite of customized analytic, AI, and ML
capabilities automatically provide actionable insights based on models that run against
the OCSF-formatted data in Security Lake.

As a service integration, Deloitte can also help you implement
Security Lake in your organization.

[Integration documentation](https://www2.deloitte.com/us/en/pages/about-deloitte/solutions/deloitte-aws-relationship.html "https://www2.deloitte.com/us/en/pages/about-deloitte/solutions/deloitte-aws-relationship.html")

## Devo

**Integration type:** Subscriber

The Devo collector for AWS supports ingestion from Security Lake. This
integration can help you analyze and address a variety of security use cases, such as
threat detection, investigation, and incident response.

[Integration documentation](https://docs.devo.com/space/latest/324337730/Amazon+Security+Lake+collector "https://docs.devo.com/space/latest/324337730/Amazon+Security+Lake+collector")

## DXC –

SecMon

**Integration type:** Subscriber, Service

DXC SecMon collects security events from Security Lake and monitors them to
detect and alert on potential security threats. This helps organizations gain a better
understanding of their security posture and proactively identify and respond to
threats.

As a service integration, DXC can also help you implement Security Lake in
your organization.

[Integration
documentation](https://dxc.com/us/en/about-us/partner-ecosystem/aws "https://dxc.com/us/en/about-us/partner-ecosystem/aws")

## Eviden –

AIsaac (formerly Atos)

**Integration type:** Subscriber

The AIsaac MDR platform consumes VPC Flow Logs ingested in OCSF schema
in Security Lake and utilizes AI models for detecting threats.

[Integration documentation](https://eviden.com/solutions/digital-security/managed-security-services/managed-detection-and-response/ "https://eviden.com/solutions/digital-security/managed-security-services/managed-detection-and-response/")

## ExtraHop – Reveal(x)

360

**Integration type:** Source

You can enhance your workload and application security by integrating network data,
including detections of IOCs, from ExtraHop Reveal(x) 360, to Security Lake
in OCSF schema

[Integration
documentation](https://forums.extrahop.com/t/aws-security-lake "https://forums.extrahop.com/t/aws-security-lake")

## Falcosidekick

**Integration type:** Source

Falcosidekick collects and sends Falco events to Security Lake. This
integration exports security events using the OCSF schema.

[Integration
documentation](https://falco.org/blog/falco-aws-security-lake/ "https://falco.org/blog/falco-aws-security-lake/")

## Fortinet - Cloud Native Firewall

**Integration type:** Source

When creating FortiGate CNF instances in AWS, you can specify
Amazon Security Lake as a log output destination.

[Integration documentation](https://docs.fortinet.com/document/fortigate-cnf/latest/administration-guide/248370 "https://docs.fortinet.com/document/fortigate-cnf/latest/administration-guide/248370")

## Gigamon – Application

Metadata Intelligence

**Integration type:** Source

Gigamon Application Metadata Intelligence (AMI) empowers your
observability, SIEM, and network performance monitoring tools with critical metadata
attributes. This helps provide deeper application visibility so you can pinpoint
performance bottlenecks, quality issues, and potential network security risks.

[Integration documentation](https://www.gigamon.com/content/dam/resource-library/english/deployment-guide/gigamon-amazon-security-lake-integration-quick-start-guide.pdf "https://www.gigamon.com/content/dam/resource-library/english/deployment-guide/gigamon-amazon-security-lake-integration-quick-start-guide.pdf")

## Hoop Cyber

**Integration type:** Service

Hoop Cyber FastStart includes a data source assessment, prioritization,
onboarding of data sources and helps customers query their data with existing tools and
integrations offered through Security Lake.

[Partner
link](https://aws.amazon.com/marketplace/pp/prodview-5dm5aecyvpn2i "https://aws.amazon.com/marketplace/pp/prodview-5dm5aecyvpn2i")

## HTCD –

AI-First Cloud Security Platform

**Integration type:** Subscriber

Gain instantaneous compliance automation, prioritization of security findings, and tailored patches. HTCD can query Security Lake to help you uncover threats with natural language queries and AI-driven insights.

[Integration documentation](https://www.htcd.com/post/secdataops-with-aws-security-lake "https://www.htcd.com/post/secdataops-with-aws-security-lake")

## IBM –

QRadar

**Integration type:** Subscriber

IBM Security QRadar SIEM with UAX integrates Security Lake with an
analytics platform that identifies and prevents threats across hybrid clouds. This
integration supports both data access and query access.

[Integration documentation on consuming AWS CloudTrail logs](https://www.ibm.com/docs/en/dsm?topic=aac-configuring-amazon-aws-cloudtrail-log-source-that-uses-amazon-security-lake "https://www.ibm.com/docs/en/dsm?topic=aac-configuring-amazon-aws-cloudtrail-log-source-that-uses-amazon-security-lake")

[Integration documentation on using Amazon Athena for queries](https://www.ibm.com/docs/en/cloud-paks/cp-security/1.10?topic=connectors-amazon-athena "https://www.ibm.com/docs/en/cloud-paks/cp-security/1.10?topic=connectors-amazon-athena")

## Infosys

**Integration type:** Service

Infosys helps you customize your Security Lake implementation for your
organizational needs and provides custom insights.

[Partner link](https://www.infosys.com/services/cloud-cobalt/offerings/managed-security-services.html "https://www.infosys.com/services/cloud-cobalt/offerings/managed-security-services.html")

## Insbuilt

**Integration type:** Service

Insbuilt specializes in cloud consulting services and can help you
understand how to implement Security Lake in your organization.

[Partner link](https://insbuilt.com/en/security-lake-eng/ "https://insbuilt.com/en/security-lake-eng/")

## Kyndryl –

AIOps

**Integration type:** Subscriber, Service

Kyndryl integrates with Security Lake to provide interoperability of
cyberdata, threat intelligence, and AI-powered analytics. As a data access subscriber,
Kyndryl ingests AWS CloudTrail Management Events from Security Lake for
analytics purposes.

As a service integration, Kyndryl can also help you implement Security Lake
in your organization.

[Integration documentation](https://www.kyndryl.com/us/en/about-us/news/2022/11/kyndryl-aws-data-security "https://www.kyndryl.com/us/en/about-us/news/2022/11/kyndryl-aws-data-security")

## Lacework –

Polygraph

**Integration type:** Source

Lacework Polygraph® Data Platform integrates with Security Lake as a data
source and provides security findings about vulnerabilities, misconfigurations, and
known and unknown threats across your AWS environment.

[Integration
documentation](https://docs.lacework.com/onboarding/amazon-security-lake "https://docs.lacework.com/onboarding/amazon-security-lake")

## Laminar

**Integration type:** Source

Laminar sends data security events to Security Lake in OCSF schema, making
them available for additional analytics use cases, such as incident response and
investigation.

[Integration documentation](https://laminar-docs.s3.us-east-2.amazonaws.com/security_lake_manual/Laminar+Integration+with+Amazon+Security+Lake+c67638221f6e476d8d2c36aee447864c.html "https://laminar-docs.s3.us-east-2.amazonaws.com/security_lake_manual/Laminar+Integration+with+Amazon+Security+Lake+c67638221f6e476d8d2c36aee447864c.html")

## MegazoneCloud

**Integration type:** Service

MegazoneCloud specializes in cloud consulting services and can help you
understand how to implement Security Lake in your organization. We connect Security Lake with integrated
ISV solutions to build custom tasks, and build customized insights related with customer
needs.

[Integration
documentation](https://www.megazone.com/us/amazon_security_lake/ "https://www.megazone.com/us/amazon_security_lake/")

## Monad

**Integration type:** Source

Monad automatically transforms your data into OCSF schema and sends it
to your Security Lake data lake.

[Integration
documentation](https://docs.monad.security/output/security-lake/ "https://docs.monad.security/output/security-lake/")

## NETSCOUT – Omnis

Cyber Intelligence

**Integration type:** Source

By integrating with Security Lake, NETSCOUT becomes a custom source of
security findings and detailed security insights into what’s happening in your
enterprise, such as cyberthreats, security risks, and attack surface changes. These
findings are produced in the customer account by NETSCOUT CyberStreams
and Omnis Cyber Intelligence, and then sent to Security Lake in OCSF schema.
The ingested data also meets other requirements and best practices for a Security Lake
source, including format, schema, partitioning, and performance-related aspects.

[Integration
documentation](https://www.netscout.com/resources/amazon-data-lake "https://www.netscout.com/resources/amazon-data-lake")

## Netskope –

CloudExchange

**Integration type:** Source

Netskope helps you strengthen your security posture by sharing
security-related logs and threat information with Security Lake. Netskope
findings are sent to Security Lake with a CloudExchange Plugin, which can be
launched as a docker-based environment within AWS or in a local data center.

[Integration documentation](https://docs.netskope.com/en/netskope-help/integrations-439794/netskope-cloud-exchange/log-shipper-module/configure-3rd-party-log-shipper-plugins/amazon-security-lake-v1-1-0-plugin-for-log-shipper/ "https://docs.netskope.com/en/netskope-help/integrations-439794/netskope-cloud-exchange/log-shipper-module/configure-3rd-party-log-shipper-plugins/amazon-security-lake-v1-1-0-plugin-for-log-shipper/")

## New Relic ONE

**Integration type:** Subscriber

New Relic ONE is a Lambda-based subscriber application. It's deployed in
your account, triggered by Amazon SQS, and sends data to New Relic using
New Relic license keys

[Integration documentation](https://docs.newrelic.com/docs/infrastructure/amazon-integrations/aws-integrations-list/aws-security-lake-monitoring-integration/ "https://docs.newrelic.com/docs/infrastructure/amazon-integrations/aws-integrations-list/aws-security-lake-monitoring-integration/")

## Okta – Workforce

Identity Cloud

**Integration type:** Source

Okta sends identity logs to Security Lake in OCSF schema through an
Amazon EventBridge integration. Okta System Logs in OCSF schema will help security
and data scientist teams to query security events by an open source standard. Generating
standardized OCSF logs from Okta helps you perform audit activities and generate reports
related to authentication, authorization, account changes, and entity changes under a
consistent schema.

[Integration documentation](https://www.okta.com/blog/2022/11/an-automated-approach-to-convert-okta-system-logs-into-open-cybersecurity-schema/ "https://www.okta.com/blog/2022/11/an-automated-approach-to-convert-okta-system-logs-into-open-cybersecurity-schema/")

[AWS CloudFormation template to add
Okta as a custom source in Security Lake](https://github.com/okta/okta-ocsf-syslog "https://github.com/okta/okta-ocsf-syslog")

## Orca – Cloud Security

Platform

**Integration type:** Source

The Orca agentless cloud security platform for AWS integrates with
Security Lake by sending Cloud Detection and Response (CDR) events in OCSF schema.

[Integration documentation (sign in to the Orca portal to review the
documentation)](https://docs.orcasecurity.io/v1/docs/integrating-amazon-security-lake "https://docs.orcasecurity.io/v1/docs/integrating-amazon-security-lake")

## Palo Alto

Networks – Prisma Cloud

**Integration type:** Source

Palo Alto Networks Prisma Cloud aggregates vulnerability detection data
across VMs in your cloud-native environments and sends it to Security Lake.

[Integration
documentation](https://docs.prismacloud.io/en/enterprise-edition/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-amazon-security-lake "https://docs.prismacloud.io/en/enterprise-edition/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-amazon-security-lake")

## Palo Alto Networks – XSOAR

**Integration type:** Suscriber

Palo Alto Networks XSOAR has built a subscriber integration with XSOAR
and Security Lake.

[Integration
documentation](https://xsoar.pan.dev/docs/reference/integrations/aws-security-lake/ "https://xsoar.pan.dev/docs/reference/integrations/aws-security-lake/")

## Panther

**Integration type:** Subscriber

Panther supports ingesting Security Lake logs for use in
search and detection.

[Integration
documentation](https://docs.panther.com/data-onboarding/supported-logs/aws/security-lake "https://docs.panther.com/data-onboarding/supported-logs/aws/security-lake")

## Ping Identity –

PingOne

**Integration type:** Source

PingOne sends account modification alerts to Security Lake in OCSF schema
and Parquet format, allowing you to discover and act upon account changes.

[Integration documentation](https://github.com/pingone-davinci/pingone-amazon-security-lake/blob/main/README.md "https://github.com/pingone-davinci/pingone-amazon-security-lake/blob/main/README.md")

## PwC – Fusion

center

**Integration type:** Subscriber, Service

PwC brings knowledge and expertise to aid clients in implementing a fusion center to
meet their individual needs. Built on Amazon Security Lake, a fusion center provides the
ability to combine data from a variety of sources to create a centralized, near
real-time view.

[Integration documentation](https://www.pwc.com/us/en/services/alliances/amazon-web-services/fusion-center.html "https://www.pwc.com/us/en/services/alliances/amazon-web-services/fusion-center.html")

## Query.AI – Query Federated Search

**Integration type:** Subscriber

Query Federated Search can directly query any Security Lake table via Amazon Athena to support incident response, investigations, threat hunting, and general search across a variety of Observables, Events, and Objects in the OCSF schema.

[Integration documentation](https://docs.query.ai/docs/amazon-security-lake#overview "https://docs.query.ai/docs/amazon-security-lake#overview")

## Rapid7 –

InsightIDR

**Integration type:** Subscriber

InsightIDR, the Rapid7 SIEM/XDR solution, can ingest
logs in Security Lake for threat detection and investigation of suspicious activity.

[Integration
documentation](https://docs.rapid7.com/insightidr/aws-security-lake/ "https://docs.rapid7.com/insightidr/aws-security-lake/")

## RipJar – Labyrinth for

Threat Investigations

**Integration type:** Subscriber

Labyrinth for Threat Investigations provides an enterprise-wide
approach to threat exploration at scale based on data fusion, with fine-grained
security, adaptable workflows, and reporting.

[Integration
documentation](https://github.com/ripjar/aws-security-lake "https://github.com/ripjar/aws-security-lake")

## Sailpoint

**Integration type:** Source

**Partner product for the integration:** SailPoint
IdentityNow

This integration enables customers to transform event data from SailPoint
IdentityNow. The integration is intended to provide an automated process to
bring IdentityNow user activity and governance events into Security Lake to
improve insights from security incident and event monitoring products.

[Integration documentation](https://community.sailpoint.com/t5/IdentityNow-Wiki/SailPoint-IdentityNow-AuditEvent-Integration-for-Amazon-Security/ta-p/241725 "https://community.sailpoint.com/t5/IdentityNow-Wiki/SailPoint-IdentityNow-AuditEvent-Integration-for-Amazon-Security/ta-p/241725")

## Securonix

**Integration type:** Subscriber

Securonix Next-Gen SIEM integrates with Security Lake, empowering security
teams to ingest data more quickly and expand their detection and response
capabilities.

[Integration documentation](https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/active-deployment-guides/amazon-security-lake-cloud-trail-logs-in-ocsf-format_.htm "https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/active-deployment-guides/amazon-security-lake-cloud-trail-logs-in-ocsf-format_.htm")

## SentinelOne

**Integration type:** Subscriber

The SentinelOne Singularity™ XDR Platform extends real-time detection
and response to endpoint, identity, and cloud workloads running on on-premises and
public cloud infrastructure, including Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Container Service (Amazon ECS), and
Amazon Elastic Kubernetes Service (Amazon EKS).

[Integration documentation (sign in to the SentinelOne portal to
review the documentation)](https://support.sentinelone.com/hc/en-us/articles/10249372394519 "https://support.sentinelone.com/hc/en-us/articles/10249372394519")

## Sentra – Data Lifecyle

Security Platform

**Integration type:** Source

After deploying the Sentra scanning infrastructure in your account,
Sentra fetches findings and ingest them into your SaaS. These
findings are metadata that Sentra stores and later streams to Security Lake
in OCSF schema for querying.

[Integration
documentation](https://docs.sentra.io/integrations/amazon-security-lake "https://docs.sentra.io/integrations/amazon-security-lake")

## SOC Prime

**Integration type:** Subscriber

SOC Prime integrates with Security Lake through Amazon OpenSearch Service and Amazon Athena to
facilitate smart data orchestration and threat hunting based on zero trust milestones.
SOC Prime empowers security teams to increase threat visibility and
investigate incidents without an overwhelming volume of alerts. You can save development
time with reusable rules and queries that are automatically convertible to Athena and
OpenSearch Service in the OCSF schema.

[Integration
documentation](https://tdm.socprime.com/attack-detective/start-page "https://tdm.socprime.com/attack-detective/start-page")

## Splunk

**Integration type:** Subscriber

The Splunk AWS Add-On for Amazon Web Services (AWS) supports ingestion from
Security Lake. This integration helps you accelerate threat detection, investigation, and
response by subscribing to data in OCSF schema from Security Lake.

[Integration
documentation](https://splunkbase.splunk.com/app/1876 "https://splunkbase.splunk.com/app/1876")

## Stellar Cyber

**Integration type:** Subscriber

Stellar Cyber consumes logs from Security Lake and adds the records to the
Stellar Cyber data lake. This connector uses OCSF schema.

[Integration documentation](https://stellarcyber.ai/news/press-releases/stellar-cyber-announces-support-for-amazon-security-lake-to-speed-data-processing-and-threat-detection-2/ "https://stellarcyber.ai/news/press-releases/stellar-cyber-announces-support-for-amazon-security-lake-to-speed-data-processing-and-threat-detection-2/")

## Sumo Logic

**Integration type:** Subscriber

Sumo Logic consumes data from Security Lake and provides broad visibility
across AWS, on-premise, and hybrid cloud environments. Sumo Logic gives security teams
comprehensive visibility, automation, and threat monitoring across all of their security
tools.

[Integration documentation](https://help.sumologic.com/docs/send-data/hosted-collectors/amazon-aws/amazon-security-lake-source/ "https://help.sumologic.com/docs/send-data/hosted-collectors/amazon-aws/amazon-security-lake-source/")

## Swimlane –

Turbine

**Integration type:** Subscriber

Swimlane ingests data from Security Lake in OCSF schema, and sends the data
through low-code playbooks and case management to facilitate faster threat detection,
investigation, and incident response.

[Integration documentation
(sign in to the Swimlane portal to review the
documentation)](https://swimlane.freshdesk.com/support/login "https://swimlane.freshdesk.com/support/login")

## Sysdig Secure

**Integration type:** Source

Sysdig Secure's cloud-native application protection platform (CNAPP) sends security events to Security Lake to maximize oversight, streamline investigations, and simplify compliance.

[Integration documentation](https://sysdig.com/content/c/pf-forwarding-sysdig-events-to-amazon-security-lake?x=u_WFRi "https://sysdig.com/content/c/pf-forwarding-sysdig-events-to-amazon-security-lake?x=u_WFRi")

## Talon

**Integration type:** Source

**Partner product for the integration:** Talon Enterprise
Browser

Talon's Enterprise Browser, a secure and isolated browser-based
endpoint environment, sends Talon Access, data protection, SaaS actions,
and security events to Security Lake providing visibility and options to cross-correlate events
for detection, forensics, and investigations.

[Integration documentation (sign in to the Talon portal to review the
documentation)](https://docs.console.talon-sec.com/en/articles/355-event-forwarding-with-amazon-security-lake "https://docs.console.talon-sec.com/en/articles/355-event-forwarding-with-amazon-security-lake")

## Tanium

**Integration type:** Source

Tanium Unified Cloud Endpoint Detection, Management, and Security
Platform provides inventory data to Security Lake in OCSF schema.

[Integration documentation](https://help.tanium.com/bundle/aws-integration/page/AWS-Integration/Introduction.htm "https://help.tanium.com/bundle/aws-integration/page/AWS-Integration/Introduction.htm")

## TCS

**Integration type:** Service

The TCS AWS Business Unit offers innovation, experience, and talent.
This integration is powered by a decade of joint value creation, deep industry
knowledge, technology expertise, and delivery wisdom. As a service integration,
TCS can help you implement Security Lake in your organization.

[Integration
documentation](https://aws.amazon.com/partners/tataconsultancyservices/ "https://aws.amazon.com/partners/tataconsultancyservices/")

## Tego Cyber

**Integration type:** Subscriber

Tego Cyber integrates with Security Lake to help you swiftly detect and
investigate potential security threats. By correlating diverse threat indicators across
extensive time frames and log sources, Tego Cyber uncovers hidden threats. The platform
is enriched with highly contextual threat intelligence, providing precision and insight
in threat detection and investigations.

[Integration
documentation](https://www.tegocyber.com/product/amazon/aws-technical "https://www.tegocyber.com/product/amazon/aws-technical")

## Tines – No-code

security automation

**Integration type:** Subscriber

Tines No-code security automation helps you make more accurate
decisions by leveraging security data centralized in Security Lake.

[Integration documentation](https://explained.tines.com "https://explained.tines.com")

## Torq – Enterprise

Security Automation Platform

**Integration type:** Source, Subscriber

Torq seamlessly integrates with Security Lake as both a custom source and a
subscriber. Torq helps you implement enterprise-scale automation and
orchestration with a simple no-code platform.

[Integration
documentation](https://torq.io/blog/secops-pipelines-aws/ "https://torq.io/blog/secops-pipelines-aws/")

## Trellix –

XDR

**Integration type:** Source, Subscriber

As an open XDR platform, Trellix XDR supports the Security Lake
integration. Trellix XDR can leverage data in OCSF schema for security
analytics use cases. You can also augment your Security Lake data lake with 1,000+ sources
of security events in Trellix XDR. This helps you extend detection and
response capabilities for your AWS environment. Ingested data is correlated with other
security risks, providing you with the necessary playbooks to respond to a risk in a
timely manner.

[Integration documentation](https://www.trellix.com/en-us/assets/docs/trellix-helix-amazon-security-lake-instructions.pdf "https://www.trellix.com/en-us/assets/docs/trellix-helix-amazon-security-lake-instructions.pdf")

## Trend Micro –

CloudOne

**Integration type:** Source

Trend Micro CloudOne Workload Security sends the following information
to Security Lake from your Amazon Elastic Compute Cloud (EC2) instances:

- DNS Query activity
- File activity
- Network activity
- Process activity
- Registry Value activity
- User Account activity

[Integration documentation](https://cloudone.trendmicro.com/docs/integrations/aws-security-lake/ "https://cloudone.trendmicro.com/docs/integrations/aws-security-lake/")

## Uptycs – Uptycs

XDR

**Integration type:** Source

Uptycs sends a wealth of data in OCSF schema from on-premises and cloud
assets to Security Lake. The data includes behavioral threat detections from endpoints and
cloud workloads, anomaly detections, policy violations, risky policies,
misconfigurations, and vulnerabilities.

[Integration
documentation](https://www.uptycs.com/partners/aws "https://www.uptycs.com/partners/aws")

## Vectra AI – Vectra

Detect for AWS

**Integration type:** Source

By using Vectra Detect for AWS, you can send high-fidelity alerts to
Security Lake as a custom source using a dedicated CloudFormation template.

[Integration
documentation](https://support.vectra.ai/s/article/KB-VS-1621 "https://support.vectra.ai/s/article/KB-VS-1621")

## VMware Aria Automation for Secure

Clouds

**Integration type:** Source

With this integration, you can detect cloud misconfigurations and send them to
Security Lake for advanced analysis.

[Integration documentation](https://docs.vmware.com/en/CloudHealth-Secure-State/services/chss-getting-started/GUID-integrations-s3.html "https://docs.vmware.com/en/CloudHealth-Secure-State/services/chss-getting-started/GUID-integrations-s3.html")

## Wazuh

**Integration type:** Subscriber

Wazuh aims to securely handle user data, provide query access for each
source, and optimize querying costs.

[Integration documentation](https://wazuh.com/blog/wazuh-integration-with-amazon-security-lake/ "https://wazuh.com/blog/wazuh-integration-with-amazon-security-lake/")

## Wipro

**Integration type:** Source, Service

This integration allows you to collect data from the Wipro Cloud Application
Risk Governance (CARG) platform to provide a unified view of your cloud
applications and compliance postures across an enterprise.

As a service integration, Wipro can also help you implement Security Lake
in your organization.

[Integration documentation](https://www.wipro.com/newsroom/press-releases/2022/wipro-to-support-new-aws-cybersecurity-data-lake-service/ "https://www.wipro.com/newsroom/press-releases/2022/wipro-to-support-new-aws-cybersecurity-data-lake-service/")

## Wiz –

CNAPP

**Integration type:** Source

The integration between Wiz and Security Lake facilitates cloud security
data collection in a single security data lake by leveraging the OCSF schema, an open
source standard designed for extensible and normalized security data exchange.

[Integration
documentation (sign in to the Wiz portal to review the
documentation)](https://docs.wiz.io/wiz-docs/docs/security-lake-integration "https://docs.wiz.io/wiz-docs/docs/security-lake-integration")

## Zscaler – Zscaler

Posture Control

**Integration type:** Source

Zscaler Posture Control™, a cloud native application protection
platform, sends security findings to Security Lake in OCSF schema.

[Integration
documentation](https://help.zscaler.com/zpc/integrating-amazon-security-lake "https://help.zscaler.com/zpc/integrating-amazon-security-lake")
