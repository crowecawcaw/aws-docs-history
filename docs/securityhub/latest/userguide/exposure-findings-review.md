# Reviewing exposure findings

You can review all of your exposure findings in the Security Hub console and with the
[GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") API. The **Exposures** page in
the Security Hub console shows all active exposure findings. Exposure findings are listed by
decreasing severity. You can filter your exposure findings by adding and removing
filters with the **Add filter** search bar. You can group your exposure
findings with the **Group by** dropdown. You can also filter your
exposure findings with the **Quick filters** menu.

## Details for exposure findings

You can view many details for an exposure finding. These details are divided among
tabs in the Security Hub console. The **Overview** tab provides key
details about the exposure finding. The **Traits** tab lists the
traits and signals associated with an exposure finding. The
**Resources** tab provides details about the resource and
resource tags associated with an exposure finding. The following list provides
descriptions for exposure finding details.

- **Finding title** – The title of the
  exposure finding.
- **Severity level** – The severity
  level of the exposure finding. Security Hub uses the number and combination of
  traits for a resource to determine the severity level of an exposure
  finding. The severity level can be `CRITICAL`, `HIGH`,
  `MEDIUM`, or `LOW`. Security Hub doesn't publish
  exposure findings with a severity of `INFORMATIONAL`. You can
  update the `Severity` through the Security Hub console or with the
  [BatchUpdateFindingsV2](../../1.0/APIReference/API_BatchUpdateFindingsV2.md "../../1.0/APIReference/API_BatchUpdateFindingsV2.md") API operation.
- **Description** – The description of
  the exposure finding.
- **Type** – The name of the exposure
  finding type. For example, the name might resemble `Exposure/Potential
Impact/Resource Hijacking`.
- **Account** – The ID of the
  AWS account where the exposure finding was generated.
- **Age** – Indicates how long the
  exposure finding has been active.
- **Created time** – A timestamp that
  indicates when the exposure finding was created.
- **Modified time** – A timestamp that
  indicates when the exposure finding was last updated.
- **Region** –
  The AWS Region where the exposure finding was generated.
- **Product name** – The name of the
  product that generated the exposure finding. This will always be
  **Security Hub Exposure Detection**.
- **Company name** –
  The name of the company that generated the exposure finding.
  This will always be **AWS**.
- **Activity name** –
  The name of the activity last performed against the finding.
- **Status** –
  The status of this exposure finding.
- **Finding ID** – A unique identifier
  associated with the exposure finding.
- **Potential attack path (console only)**
  – An interactive visualization showing how potential attackers can
  access and take control of resources associated with an exposure finding.
  For more information, see
  [Viewing exposures in Security Hub with the
  potential attack path graph](potential-attack-path-graph.md "potential-attack-path-graph.md").
- **Traits** – Identifies trait types
  and trait titles associated with the exposure finding. In the Security Hub
  console, you can view traits by trait type or signal. This helps you analyze
  contributing findings in the context of the related exposure.
- **Remediation** – Links to remediation
  documentation specific to traits identified in the exposure.
- **Resources** –
  Identifies the resource associated with the exposure finding.
