# NetWitness

NetWitness is a leading developer of extended detection and response (XDR)
software. Their global base of highly security-conscious customers relies on
NetWitness XDR to defend against sophisticated and aggressive
adversaries. With the industry’s most complete, integrated, and mature platform to detect,
investigate, and respond to digital attacks, NetWitness XDR is the unifying
foundation of a modern and effective SOC.

Due to its highly modular architecture, NetWitness XDR detects threats
wherever they occur — in the cloud, on-premises, with mobile and remote workers, or anywhere
in between. The NetWitness Platform XDR delivers complete visibility combined
with applied threat intelligence and user behavior analytics to detect threats, prioritize
activities, investigate, and automate response. All this empowers security analysts with
better, faster efficiency to keep security operations well ahead of business-impacting
threats.

## AWS AppFabric audit log ingestion

considerations

The following sections describe the AppFabric output schema, output formats, and output
destinations to use with NetWitness.

### Schema and format

NetWitness supports the following AppFabric output schema and formats:

- Raw - JSON
  - AppFabric outputs data in the original schema used by the source
    application in the JSON format.

- OCSF - JSON
  - AppFabric normalizes the data using the Open Cybersecurity Schema
    Framework (OCSF) and outputs the data in the JSON format.

### Output locations

NetWitness supports the following AppFabric output location:

- Amazon Simple Storage Service (Amazon S3)
  - To configure NetWitness to receive data from the
    Amazon S3 bucket that contains your audit logs, follow the instructions
    in [S3 Universal Connector Event Source Log Configuration
    Guide](https://community.netwitness.com/t5/netwitness-platform-integrations/s3-universal-connector-event-source-log-configuration-guide/ta-p/595235 "https://community.netwitness.com/t5/netwitness-platform-integrations/s3-universal-connector-event-source-log-configuration-guide/ta-p/595235") on the _NetWitness Platform Integrations_
    page on the NetWitness website.
