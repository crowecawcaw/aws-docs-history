

# Public discovery

Public discovery extends AWS Agent Registry beyond the boundaries of your organization. With public discovery, you can promote an approved record so that any AWS-authenticated caller — including callers outside your organization — can discover it through public search. Promotion makes a record discoverable to all such callers; you cannot restrict discovery to specific organizations. This section explains the public discovery plane, how it relates to the internal governance plane you already use, and how to publish records to it.

**Topics**
+ [Two discovery planes](#registry-public-discovery-two-planes)
+ [Two independent approval gates](#registry-public-discovery-gates)
+ [The Registry is discovery-only](#registry-public-discovery-not-hosting)
+ [Publishers](registry-publishers.md)
+ [Promote a record to public discovery](registry-promote-to-public.md)
+ [Search publicly discoverable records](registry-public-search.md)
+ [Web bot records](registry-web-bot.md)

## Two discovery planes
<a name="registry-public-discovery-two-planes"></a>

 AWS Agent Registry spans two discovery planes. The same registry and the same records participate in both planes, but each plane has its own audience and its own governance gate.

 **Internal governance plane**   
This is the registry inside your organization that the other sections of this guide describe. A publisher creates a record, submits it for approval, and a curator approves it. An approved record becomes discoverable *within your organization* through the registry’s discovery data-plane APIs and the registry’s Model Context Protocol (MCP) endpoint. The registry’s authorization configuration (IAM or JWT) controls access, and you can extend access to other accounts with AWS Resource Access Manager (RAM). For more information, see [Discovering the registry](registry-searching.md) and [Sharing a registry across accounts with AWS RAM](registry-cross-account-sharing.md).

 **Public discovery plane**   
This plane is new and is the focus of this section. An approved record can be *promoted* so that it becomes discoverable *across organizational boundaries*. Promotion is anchored to a [Publisher](registry-publishers.md) — a verified public identifier (a domain) whose ownership your organization proves. After a Publisher is verified and an approved record is associated with it (and that association is approved), the record becomes discoverable through AWS-authenticated public search. For more information, see [Search publicly discoverable records](registry-public-search.md). Several personas take part: an administrator verifies the [Publisher](registry-publishers.md), a publisher promotes an approved record, a curator approves the public association, and a client discovers the record through public search. For more information about these roles, see [Key Personas](registry-concepts.md#registry-concept-personas).

## Two independent approval gates
<a name="registry-public-discovery-gates"></a>

Each plane has its own approval gate, and the two gates are independent.
+  **Record approval** governs internal discoverability. A record is discoverable within your organization when its status is `APPROVED`. This gate is unchanged. For more information, see [Curating the registry](registry-curating.md).
+  **Publisher-association approval** governs public discoverability. Associating an approved record with a verified Publisher starts a second review. The record becomes publicly discoverable only after this association is approved.

A record is publicly discoverable only when both conditions are true: the record status is `APPROVED` **and** its Publisher association status is `PUBLIC_ASSOCIATION_APPROVED`. A record that is approved internally but not associated with a Publisher stays in the internal plane only.

## The Registry is discovery-only
<a name="registry-public-discovery-not-hosting"></a>

 AWS Agent Registry publishes metadata that makes an agent or resource discoverable. It does not host the agent, route traffic to it, or proxy requests on its behalf. You remain responsible for deploying the agent, serving its metadata at its endpoint, and operating the runtime that answers requests. A Publisher proves that your organization controls a public identifier; it does not change where or how the agent runs.