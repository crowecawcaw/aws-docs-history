# Requirements

You can bring up to two qualifying IP address ranges to AWS Global Accelerator per AWS account.

To qualify, your IP address range must meet the following requirements:

- The IP address range must be registered with one of the following regional internet registries
  (RIRs): the American Registry for Internet Numbers (ARIN), Réseaux IP Européens Network
  Coordination Centre (RIPE), or Asia-Pacific Network Information Centre (APNIC). The address
  range must be registered to a business or institutional entity. It can’t be registered to
  an individual.
- The only address range that you can bring is /24. The first 24 bits of the
  IP address specify the network number. For example, 198.51.100 is the network number for IP
  address 198.51.100.0.
- The IP addresses in the address range must have a clean history. That is, they can’t have a
  poor reputation or be associated with malicious behavior. We reserve the right
  to reject the IP address range if we investigate the reputation of the IP
  address range and find that it contains an IP address that doesn’t have a clean
  history.
  Also, we require the following allocation and assignment network types or statuses,
  depending on where you registered your IP address range:

- ARIN: `Direct Allocation` and `Direct Assignment` network types
- RIPE: `ALLOCATED PA`, `LEGACY`, and `ASSIGNED PI` allocation
  statuses
- APNIC: `ALLOCATED PORTABLE` and `ASSIGNED PORTABLE` allocation
  statuses
