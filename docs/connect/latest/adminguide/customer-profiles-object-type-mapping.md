

# Object type mapping in Connect Customer Customer Profiles
<a name="customer-profiles-object-type-mapping"></a>

Object type mapping tells Customer Profiles how to ingest a specific type of data into a unified customer profile. A mapping provides Customer Profiles with two essential pieces of information:
+ How values from a source object populate **standard objects**—the standard profile, and (optionally) other standard objects such as assets, orders, cases, and loyalty records. For more information, see [Reference for standard objects in Customer Profiles](standard-objects.md).
+ Which fields to index for searching, and how those fields are used to assign objects of this type to a specific profile (and, when applicable, to a specific standard object such as an asset or order).

With a mapping in place, you can ingest data from sources such as Salesforce, Zendesk, ServiceNow, Marketo, Amazon S3, or your own applications, and present a single unified view of each customer to your agents, flows, and downstream applications.

**Topics**
+ [How object type mapping works in Customer Profiles](how-object-type-mapping-works.md)
+ [Object type mapping terminology and concepts](customer-profiles-terminology.md)
+ [Create an object type mapping in Connect Customer Customer Profiles](create-object-type-mapping.md)
+ [Object type mapping rules in Connect Customer Customer Profiles](object-type-mapping-rules.md)
+ [How mappings create and update profiles in Connect Customer Customer Profiles](how-mappings-create-update-profiles.md)
+ [Quotas and troubleshooting for object type mapping in Connect Customer Customer Profiles](object-type-mapping-quotas-troubleshooting.md)