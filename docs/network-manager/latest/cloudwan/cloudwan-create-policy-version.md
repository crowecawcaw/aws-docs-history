# Core network policy

versions in AWS Cloud WAN

Create a version of your current network policy any time you want to make changes to your
network. Policy versions can be created using the console, through either the visual editor
mode or directly in JSON, or you can download a version of any policy and make changes to
that policy in any JSON editor. Once you create a new version of a policy you can compare
that version against an older version to view changes.

New versions of policies are not automatically deployed, so once you create a policy
version you can deploy that policy at a time of your own choosing. You can also restore any
out-of-date policy to become the new current version.

The name of each policy version you create is numbered incrementally from the LATEST
version. For example, if the LATEST policy version ID is `1`, and you create a
new version of that policy, the new version is numbered `2`. The latest version
is displayed on the Policy versions screen with a **LATEST** status,
indicating that the new policy is ready to deploy.

Change set states can be any of the following:

- **Ready to execute** — A policy version change set and a new
  policy version have been created. This policy version was verified with no issues
  and is in a state where it can be deployed as the new LIVE policy. You can have
  multiple policy versions in this state, but you can only have one LIVE policy. When
  deployed, the policy change set state changes to **Execution
  succeeded**. For the steps to deploy a policy change set state, see [Deploy an AWS Cloud WAN core network policy version](cloudwan-policy-version-deploy.md "cloudwan-policy-version-deploy.md").
- **Execution succeeded** — The policy version was deployed as the
  new LIVE policy.
- **Out of date** — If you have multiple policy version change
  sets, any policy version that's older than the current LIVE policy is set to
  out-of-date, indicating that it's older than the LIVE policy. You can restore an
  out-of-date policy. For instructions, see [Restore an out-of-date AWS Cloud WAN core network policy
  version](cloudwan-policy-version-restore.md "cloudwan-policy-version-restore.md").
- **Failed generation** — An error prevented the policy from
  generating. Choose the Failed generation link to see details about the failure.
- **Pending generation** — A policy version was created and is
  waiting to be generated. When the version has been generated, the change set state
  changes to **Ready to execute**. If policy generation failed, this
  state changes to **Failed generation**.
  You can create a core network policy version through either the AWS Cloud WAN console or by
  creating or modifying a JSON file.

###### Topics

- [Core network policy sections](#cloudwan-policy-sections "#cloudwan-policy-sections")
- [Cloud WAN service insertion](cloudwan-policy-service-insertion.md "cloudwan-policy-service-insertion.md")
- [Create a policy version using the console](cloudwan-create-policy-console.md "cloudwan-create-policy-console.md")
- [Create a policy version using JSON](cloudwan-create-policy-json.md "cloudwan-create-policy-json.md")
- [View a core network policy change set](cloudwan-policy-version-view.md "cloudwan-policy-version-view.md")
- [Compare policy change set versions](cloudwan-policy-version-compare.md "cloudwan-policy-version-compare.md")
- [Deploy a core network policy version](cloudwan-policy-version-deploy.md "cloudwan-policy-version-deploy.md")
- [Delete a policy version](cloudwan-policy-version-delete.md "cloudwan-policy-version-delete.md")
- [Download a core network policy](ccloudwan-policy-version-download.md "ccloudwan-policy-version-download.md")
- [Restore an out-of-date core network policy version](cloudwan-policy-version-restore.md "cloudwan-policy-version-restore.md")

## Core network policy sections

The following are the parts of a core network policy and describe how each of these work. If you're using either the console or a JSON file, a policy version is always composed of these sections.

###### Topics

- [Network configuration](#cloudwan-policy-config "#cloudwan-policy-config")
- [Segments](#cloudwan-policy-create-segment "#cloudwan-policy-create-segment")
- [Network function groups](#cloudwan-core-network-function "#cloudwan-core-network-function")
- [Segment actions](#cloudwan-policy-create-action "#cloudwan-policy-create-action")
- [Attachment policies](#cloudwan-policy-create-attachment "#cloudwan-policy-create-attachment")

### Network configuration

Use **Network configuration** to configure the Border Gateway
Protocol (BGP) Autonomous System Number (ASN) for your core network. The valid ranges
are `64512 - 65534` and `4200000000 -
 4294967294`. You can also configure the Inside CIDR blocks that are used
for BGP peering on Connect peers. For more information on Transit Gateway Connect
attachment and Connect peers, see the [Transit Gateway
Connect](../../../vpc/latest/tgw/tgw-connect.md "../../../vpc/latest/tgw/tgw-connect.md") documentation. Using the network configuration, you can also
configure the edge locations where you want the Core Network Edges to be available. At
any time, you can add or remove edge locations through the network configuration.

See the following for the steps to configure your network:

- To configure your network using the console, see [Configure the core network settings in an AWS Cloud WAN policy
  version](cloudwan-core-network-config.md "cloudwan-core-network-config.md").
- To configure your network using a JSON file, see [core-network-configuration](cloudwan-policies-json.md#cloudwan-network-config-json "cloudwan-policies-json.md#cloudwan-network-config-json") in [Core network policy version parameters in
  AWS Cloud WAN](cloudwan-policies-json.md "cloudwan-policies-json.md").

### Segments

The Segments section of a policy allows to divide your global network into separate
isolated networks. Here you create a segment, and then define the attachment
communication mapping. Each segment creates a dedicated routing domain. You can create
multiple network segments within your global network. Resources that are connected to
the same segment can only communicate within the segment. Optionally, you can also set
resources in the same segment to be isolated from each other, with access only to shared
services. With segments, AWS maintains a consistent configuration across AWS Regions
for you, meaning that you don't need to synchronize configuration across every device in
your network.

See the following for the steps to add segments to your core network:

- To add a segment using the console, see [Add a segment to an AWS Cloud WAN core network policy version](cloudwan-policy-segments.md "cloudwan-policy-segments.md").
- To add a segment using a JSON file, see [segments](cloudwan-policies-json.md#cloudwan-segments-json-about "cloudwan-policies-json.md#cloudwan-segments-json-about") in [Core network policy version parameters in
  AWS Cloud WAN](cloudwan-policies-json.md "cloudwan-policies-json.md").

### Network function groups

A network function group is composed of a group of attachments used to steer those
attachments to network security group functions. For example, you might create a network
function group that steers traffic from a production segment through an inspection VPC
directly to the Internet.

Optionally use the **Network function groups** page to create a group
that allows you to insert AWS and third-party networking and security services on
Cloud WAN using your policy document. After creating a network function group you'll
create a segment action that defines how you want to steer the segments and attachments
for the network function group.

- For the steps to create a network function group using the console, see [Create a network function group in
  an AWS Cloud WAN policy version](cloudwan-policy-network-function-groups.md "cloudwan-policy-network-function-groups.md").
- For the steps to create a network function group using JSON, see [network-function-groups](cloudwan-policies-json.md#cloudwan-network-functions-json "cloudwan-policies-json.md#cloudwan-network-functions-json") in [Core network policy version parameters in
  AWS Cloud WAN](cloudwan-policies-json.md "cloudwan-policies-json.md").

### Segment actions

Segment actions allow you to optionally share your segments, create routes, or create
a service insertion action for a network functions group.

- **Segment sharing** — Segment sharing is
  bidirectional by default. When you create a segment share between two segments,
  routes from both segments are automatically advertised to each other. For
  example, you might share a segment named `test` with another
  segment named `dev`. Routes from `test` are
  advertised to `dev`, and vice versa. To make routes in shared
  segments unidirectional, create a deny list filter to share routes from one
  segment to the other, but not vice versa. Using the previous example, you could
  make a deny list filter that prevents routes from `test` being
  advertised to `dev`. For more information on creating the deny
  list for a segment, see [Add a segment to an AWS Cloud WAN core network policy version](cloudwan-policy-segments.md "cloudwan-policy-segments.md").
- **Segment routes** — Create a segment route to define a
  static route within a segment.
- **Service insertion** — Create a service insertion action
  that allows you to insert a network function within a segment or across
  segments. This action can either be send via (east-west) or send to
  north-south). For more information about traffic actions and modes see [Traffic actions and
  modes](cloudwan-policy-service-insertion.md#cloudwan-policy-service-insertion-modes "cloudwan-policy-service-insertion.md#cloudwan-policy-service-insertion-modes"). You can additionally
  choose to specify which edge locations you want to use. Service insertion uses a
  default order for choosing the edgte locations. However, you can specify which
  edges you want to use as well as which edge is the preferred edge.

See the following for the steps to set segment actions:

- To add a segment using the console, see [Add a segment action in an AWS Cloud WAN core network policy version](cloudwan-policy-network-actions-routes.md "cloudwan-policy-network-actions-routes.md").
- To add a segment using a JSON file, see [segments](cloudwan-policies-json.md#cloudwan-segments-json-about "cloudwan-policies-json.md#cloudwan-segments-json-about") in [segment-actions](cloudwan-policies-json.md#cloudwan-segment-actions-json "cloudwan-policies-json.md#cloudwan-segment-actions-json") in [Core network policy version parameters in
  AWS Cloud WAN](cloudwan-policies-json.md "cloudwan-policies-json.md").

### Attachment policies

Attachment policies control how your attachments map to your segments or network function
groups. You create a network function group attachment policy using either the AND or OR
subset of conditions along with either the full tag name or tag value.

See the following for the steps to create a network functions group attachment
policy:

- To add an attachment policy using the console, see [Create an attachment policy in an AWS Cloud WAN core
  network policy version](cloudwan-policy-attachments.md "cloudwan-policy-attachments.md").
- To add an attachment policy using a JSON file, see [attachment-policies](cloudwan-policies-json.md#cloudwan-attach-policies-json "cloudwan-policies-json.md#cloudwan-attach-policies-json") in [segment-actions](cloudwan-policies-json.md#cloudwan-segment-actions-json "cloudwan-policies-json.md#cloudwan-segment-actions-json").
