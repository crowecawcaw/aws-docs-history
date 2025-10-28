# Customizing threat detection with entity lists and

IP address lists

Amazon GuardDuty monitors the security of your AWS environment by analyzing and processing VPC
Flow Logs, AWS CloudTrail event logs, and DNS logs. By enabling one or more [Use-case focused
GuardDuty protection plans](what-is-guardduty.md#features-of-guardduty "what-is-guardduty.md#features-of-guardduty") (except [Runtime Monitoring](runtime-monitoring.md "runtime-monitoring.md"), you can expand the monitoring capabilities
within GuardDuty.

With lists, GuardDuty helps you customize the scope of threat detection in your environment.
You can configure GuardDuty to stop generating findings from your trusted sources and generate
findings for known malicious sources from your threat lists. GuardDuty continues to support
legacy IP address lists and extends support to entity lists (recommended) that can contain
IP addresses, domains, or both.

###### Topics

- [Understanding entity lists and IP address
  lists](#guardduty-threat-intel-list-entity-sets "#guardduty-threat-intel-list-entity-sets")
- [Important
  considerations for GuardDuty lists](#guardduty-lists-entity-sets-considerations "#guardduty-lists-entity-sets-considerations")
- [List formats](#prepare_list "#prepare_list")
- [Understanding list statuses](#guardduty-entity-list-statuses "#guardduty-entity-list-statuses")
- [Setting up prerequisites for entity lists and IP address
  lists](guardduty-lists-prerequisites.md "guardduty-lists-prerequisites.md")
- [Adding and activating an entity list or IP
  list](guardduty-lists-create-activate.md "guardduty-lists-create-activate.md")
- [Updating an entity list or IP address
  list](guardduty-lists-update-procedure.md "guardduty-lists-update-procedure.md")
- [De-activating entity list
  or IP address list](guardduty-lists-deactivate-procedure.md "guardduty-lists-deactivate-procedure.md")
- [Deleting entity list
  or IP address list](guardduty-lists-delete-procedure.md "guardduty-lists-delete-procedure.md")

## Understanding entity lists and IP address

lists

GuardDuty offers two implementation approaches: entity lists (recommended) and IP lists.
Both approaches help you specify trusted sources, which stop GuardDuty from generate
findings and known threats, which GuardDuty uses to generate findings.

**Entity lists** support both IP addresses and domain
names. They use direct Amazon Simple Storage Service (Amazon S3) access with a single IAM permission that
doesn't impact IAM policy size limits across multiple Regions.

**IP lists** support only IP addresses and use [GuardDuty service-linked role (SLR)](slr-permissions.md "slr-permissions.md") (SLR), requiring
IAM policy updates per Region, which may impact IAM policy size limits.

Trusted lists (both entity lists and IP address lists) include entries that you trust
for secure communication with your AWS infrastructure. GuardDuty does not generate
findings for entries listed in trusted sources. At any given time, you can add only one
trusted entity list and one trusted IP address list per AWS account per Region.

Threat lists (both entity lists and IP address lists) include entries that you have
identified as known malicious sources. When GuardDuty detects an activity involving these
sources, it generates findings to alert you of potential security issues. You can create
your own threat lists or incorporate third-party threat intelligence feeds. This list
can be supplied by third-party threat intelligence or created specifically for your
organization. In addition to generating findings because of a potentially suspicious
activity, GuardDuty also generates findings based on an activity that involves entries from
your threat lists. At any given time, you can upload up to six threat entity lists and
threat IP address lists per AWS account per Region.

###### Note

To migrate from IP address lists to entity lists, follow [Prerequisites for entity
lists](guardduty-lists-prerequisites.md#guardduty-entity-list-prerequisites "guardduty-lists-prerequisites.md#guardduty-entity-list-prerequisites"), then
add and activate the required entity list. After this, you can choose to
deactivate or delete the corresponding IP address list.

## Important

considerations for GuardDuty lists

Before you begin working with lists, read the following considerations:

- IP address lists and entity lists apply only to traffic destined for publicly
  routable IP addresses and domains.
- In an entity list, the entries apply to CloudTrail, VPC Flow Logs in Amazon VPC, and
  Route53 Resolver DNS query logs findings.

In an IP address list, the entries apply to CloudTrail and VPC Flow Logs in Amazon VPC
findings, but not to Route53 Resolver DNS query logs findings.

- If you include the same IP address or domain in both trusted and threat lists,
  then this entry in the trusted list will take precedence. GuardDuty will not
  generate a finding if there is an activity associated with this entry.
- In a multi-account environment, only the GuardDuty administrator account can manage lists. This
  setting automatically applies to the member accounts. GuardDuty generates findings
  based on an activity that involves known malicious IP addresses (and domains)
  from the administrator account's threat sources, and doesn't generate findings based on
  activity that involves IP addresses (and domains) from the administrator account's trusted
  sources. For more information, see [Multiple accounts in Amazon GuardDuty](guardduty_accounts.md "guardduty_accounts.md").
- Only IPv4 addresses are accepted. IPv6 addresses are not supported.
- After you activate, deactivate, or delete an entity list or IP address list,
  the process is estimated to complete within 15 minutes. In certain scenarios, it
  may take up to 40 minutes for this process to complete.
- GuardDuty uses a list for threat detection only when the status of the list
  becomes **Active**.
- Whenever you add or update an entry in the list's S3 bucket location, you must
  activate the list again. For more information, see [Updating an entity list or IP address
  list](guardduty-lists-update-procedure.md "guardduty-lists-update-procedure.md").
- Entity lists and IP addresses have different quotas. For more information, see
  [GuardDuty quotas](guardduty_limits.md "guardduty_limits.md").

## List formats

GuardDuty accepts multiple file formats for your lists and entity lists, with a maximum of
35 MB per file. Each format has specific requirements and capabilities.

This format supports IP addresses, CIDR ranges, and domain names. Each entry
must appear on a separate line.

###### **Example for entity list**

```
192.0.2.1
192.0.2.0/24
example.com
example.org
*.example.org
```

###### **Example for IP address list**

```
192.0.2.0/24
198.51.100.1
203.0.113.1
```

This format supports IP addresses, CIDR block, and domain names. STIX allows
you to include additional context with your threat intelligence. GuardDuty processes
IP addresses, CIDR ranges, and domain names from the STIX indicators.

###### **Example for an entity list**

```
<?xml version="1.0" encoding="UTF-8"?>
<stix:STIX_Package
    xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
    xmlns:cybox="http://cybox.mitre.org/cybox-2"
    xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2"
    xmlns:stix="http://stix.mitre.org/stix-1"
    xmlns:indicator="http://stix.mitre.org/Indicator-2"
    xmlns:stixCommon="http://stix.mitre.org/common-1"
    xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
    xmlns:DomainNameObj="http://cybox.mitre.org/objects#DomainNameObject-1"
    id="example:Package-a1b2c3d4-1111-2222-3333-444455556666"
    version="1.2">
    <stix:Indicators>
        <stix:Indicator
            id="example:indicator-a1b2c3d4-aaaa-bbbb-cccc-ddddeeeeffff"
            timestamp="2025-08-12T00:00:00Z"
            xsi:type="indicator:IndicatorType"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <indicator:Title>Malicious domain observed Example</indicator:Title>
            <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">Domain Watchlist</indicator:Type>
            <indicator:Observable id="example:Observable-0000-1111-2222-3333">
                <cybox:Object id="example:Object-0000-1111-2222-3333">
                    <cybox:Properties xsi:type="DomainNameObj:DomainNameObjectType">
                        <DomainNameObj:Value condition="Equals">bad.example.com</DomainNameObj:Value>
                    </cybox:Properties>
                </cybox:Object>
            </indicator:Observable>
        </stix:Indicator>
    </stix:Indicators>
</stix:STIX_Package>
```

###### **Example for an IP address list**

```
<?xml version="1.0" encoding="UTF-8"?>
<stix:STIX_Package
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:stix="http://stix.mitre.org/stix-1"
    xmlns:stixCommon="http://stix.mitre.org/common-1"
    xmlns:ttp="http://stix.mitre.org/TTP-1"
    xmlns:cybox="http://cybox.mitre.org/cybox-2"
    xmlns:AddressObject="http://cybox.mitre.org/objects#AddressObject-2"
    xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2"
    xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
    xmlns:example="http://example.com/"
    xsi:schemaLocation="
    http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.2/stix_core.xsd
    http://stix.mitre.org/Campaign-1 http://stix.mitre.org/XMLSchema/campaign/1.2/campaign.xsd
    http://stix.mitre.org/Indicator-2 http://stix.mitre.org/XMLSchema/indicator/2.2/indicator.xsd
    http://stix.mitre.org/TTP-2 http://stix.mitre.org/XMLSchema/ttp/1.2/ttp.xsd
    http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.2.0/stix_default_vocabularies.xsd
    http://cybox.mitre.org/objects#AddressObject-2 http://cybox.mitre.org/XMLSchema/objects/Address/2.1/Address_Object.xsd"
    id="example:STIXPackage-a78fc4e3-df94-42dd-a074-6de62babfe16"
    version="1.2">
    <stix:Observables cybox_major_version="1" cybox_minor_version="1">
        <cybox:Observable id="example:observable-80b26f43-dc41-43ff-861d-19aff31e0236">
            <cybox:Object id="example:object-161a5438-1c26-4275-ba44-a35ba963c245">
                <cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
                    <AddressObject:Address_Valuecondition="InclusiveBetween">192.0.2.0##comma##192.0.2.255</AddressObject:Address_Value>
                </cybox:Properties>
            </cybox:Object>
        </cybox:Observable>
        <cybox:Observable id="example:observable-b442b399-aea4-436f-bb34-b9ef6c5ed8ab">
            <cybox:Object id="example:object-b422417f-bf78-4b34-ba2d-de4b09590a6d">
                <cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
                    <AddressObject:Address_Value>198.51.100.1</AddressObject:Address_Value>
                </cybox:Properties>
            </cybox:Object>
        </cybox:Observable>
        <cybox:Observable id="example:observable-1742fa06-8b5e-4449-9d89-6f9f32595784">
            <cybox:Object id="example:object-dc73b749-8a31-46be-803f-71df77565391">
                <cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
                    <AddressObject:Address_Value>203.0.113.1</AddressObject:Address_Value>
                </cybox:Properties>
            </cybox:Object>
        </cybox:Observable>
    </stix:Observables>
</stix:STIX_Package>
```

This format supports CIDR block, individual IP addresses, and domains. This
file format has comma-separated values.

###### **Example for entity list**

```
Indicator type, Indicator, Description
CIDR, 192.0.2.0/24, example
IPv4, 198.51.100.1, example
IPv4, 203.0.113.1, example
Domain name, example.net, example
```

###### **Example for IP address list**

```
Indicator type, Indicator, Description
CIDR, 192.0.2.0/24, example
IPv4, 198.51.100.1, example
IPv4, 203.0.113.1, example
```

This format supports CIDR block, individual IP addresses, and domains. The
following sample lists uses a `FireEyeTM`
CSV format.

###### **Example for entity list**

```
reportId, title, threatScape, audience, intelligenceType, publishDate, reportLink, webLink, emailIdentifier, senderAddress, senderName, sourceDomain, sourceIp, subject, recipient, emailLanguage, fileName, fileSize, fuzzyHash, fileIdentifier, md5, sha1, sha256, description, fileType, packer, userAgent, registry, fileCompilationDateTime, filePath, asn, cidr, domain, domainTimeOfLookup, networkIdentifier, ip, port, protocol, registrantEmail, registrantName, networkType, url, malwareFamily, malwareFamilyId, actor, actorId, observationTime

01-00000001, Example, Test, Operational, threat, 1494944400, https://www.example.com/report/01-00000001, https://www.example.com/report/01-00000001, , , , , , , , , , , , , , , , , , , , , , , , 192.0.2.0/24, , , Related, , , , , , network, , Ursnif, 21a14673-0d94-46d3-89ab-8281a0466099, , , 1494944400

01-00000002, Example, Test, Operational, threat, 1494944400, https://www.example.com/report/01-00000002, https://www.example.com/report/01-00000002, , , , , , , , , , , , , , , , , , , , , , , , , , , Related, 198.51.100.1, , , , , network, , Ursnif, 12ab7bc4-62ed-49fa-99e3-14b92afc41bf, , ,1494944400

01-00000003, Example, Test, Operational, threat, 1494944400, https://www.example.com/report/01-00000003, https://www.example.com/report/01-00000003, , , , , , , , , , , , , , , , , , , , , , , , , , , Related, 203.0.113.1, , , , , network, , Ursnif, 8a78c3db-7bcb-40bc-a080-75bd35a2572d, , , 1494944400

 01-00000002, Malicious domain observed in test, Test, Operational, threat, 1494944400, https://www.example.com/report/01-00000002,https://www.example.com/report/01-00000002,,,,,,,,,,,,,,,,,,,,,,,, 203.0.113.0/24, example.com,, Related, 203.0.113.0, 8080, UDP,,, network,, Ursnif, fc13984c-c767-40c9-8329-f4c59557f73b,,, 1494944400
```

###### **Example for IP address list**

```
reportId, title, threatScape, audience, intelligenceType, publishDate, reportLink, webLink, emailIdentifier, senderAddress, senderName, sourceDomain, sourceIp, subject, recipient, emailLanguage, fileName, fileSize, fuzzyHash, fileIdentifier, md5, sha1, sha256, description, fileType, packer, userAgent, registry, fileCompilationDateTime, filePath, asn, cidr, domain, domainTimeOfLookup, networkIdentifier, ip, port, protocol, registrantEmail, registrantName, networkType, url, malwareFamily, malwareFamilyId, actor, actorId, observationTime

01-00000001, Example, Test, Operational, threat, 1494944400, https://www.example.com/report/01-00000001, https://www.example.com/report/01-00000001, , , , , , , , , , , , , , , , , , , , , , , , 192.0.2.0/24, , , Related, , , , , , network, , Ursnif, 21a14673-0d94-46d3-89ab-8281a0466099, , , 1494944400

01-00000002, Example, Test, Operational, threat, 1494944400, https://www.example.com/report/01-00000002, https://www.example.com/report/01-00000002, , , , , , , , , , , , , , , , , , , , , , , , , , , Related, 198.51.100.1, , , , , network, , Ursnif, 12ab7bc4-62ed-49fa-99e3-14b92afc41bf, , ,1494944400

01-00000003, Example, Test, Operational, threat, 1494944400, https://www.example.com/report/01-00000003, https://www.example.com/report/01-00000003, , , , , , , , , , , , , , , , , , , , , , , , , , , Related, 203.0.113.1, , , , , network, , Ursnif, 8a78c3db-7bcb-40bc-a080-75bd35a2572d, , , 1494944400
```

In ProofPoint CSV format, you can add IP either addresses or domain names in a
one list. The following sample list uses the `Proofpoint` CSV format.
Providing value for the `ports` parameter is optional. When you
don't provide it, leave a trailing comma (,) at the end.

###### **Example for entity list**

```
domain, category, score, first_seen, last_seen, ports (|)
198.51.100.1, 1, 100, 2000-01-01, 2000-01-01,
203.0.113.1, 1, 100, 2000-01-01, 2000-01-01, 80
```

###### **Example for IP address list**

```
ip, category, score, first_seen, last_seen, ports (|)
198.51.100.1, 1, 100, 2000-01-01, 2000-01-01,
203.0.113.1, 1, 100, 2000-01-01, 2000-01-01, 80
```

The following sample list uses the `AlienVault` format.

###### **Example for entity list**

```
192.0.2.1#4#2#Malicious Host#KR##37.5111999512,126.974098206#3
192.0.2.2#4#2#Scanning Host#IN#Gurgaon#28.4666996002,77.0333023071#3
192.0.2.3#4#2##CN#Guangzhou#23.1166992188,113.25#3
www.test.org#4#2#Malicious Host#CA#Brossard#45.4673995972,-73.4832000732#3
www.example.com#4#2#Malicious Host#PL##52.2393989563,21.0361995697#3
```

###### **Example for IP address list**

```
198.51.100.1#4#2#Malicious Host#US##0.0,0.0#3
203.0.113.1#4#2#Malicious Host#US##0.0,0.0#3
```

## Understanding list statuses

When you add an entity list or an IP address list, GuardDuty shows the status of that
list. The **Status** column indicates whether the list is effective and
if any action is required. The following list describes valid status values:

- **Active** – Indicates the list is currently in use
  for custom threat detection.
- **Inactive** – Indicates that the list is
  currently not in use. For GuardDuty to use this list for threat detection in your
  environment, see Step 3: Activating an entity list or IP address list in
  [Adding and activating an entity list or IP
  list](guardduty-lists-create-activate.md "guardduty-lists-create-activate.md").
- **Error** – Indicates that there is an issue with the
  list. Hover over the status to view the error details.
- **Activating** – Indicates that GuardDuty has initiated
  the process of activating the list. You can continue monitoring the status for
  this list. If there is no error, the status should update to
  **Active**. While the status remains **Activating**, you can't
  perform any action on this list. It might take a few minutes for the list status to change to
  **Active**.
- **Deactivating** – Indicates that GuardDuty has initiated
  the process of deactivating the list. You can continue monitoring the status for
  this list. If there is no error, the status should update to
  **Inactive**. While the status remains **Deactivating**, you can't
  perform any action on this list.
- **Delete Pending** – Indicates that the list is in the process of
  being deleted. While the status remains **Delete Pending**, you can't
  perform any action on this list.
