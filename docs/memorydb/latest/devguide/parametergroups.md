# Parameter group tiers

_MemoryDB parameter group tiers_

**Global Default**

The top-level root parameter group for all MemoryDB customers in the region.

The global default parameter group:

- Is reserved for MemoryDB and not available to the customer.
  **Customer Default**

A copy of the Global Default parameter group which is created for the customer's use.

The Customer Default parameter group:

- Is created and owned by MemoryDB.
- Is available to the customer for use as a parameter group for any clusters
  running an engine version supported by this parameter group.
- Cannot be edited by the customer.
  **Customer Owned**

A copy of the Customer Default parameter group.
A Customer Owned parameter group is created whenever the customer creates a parameter group.

The Customer Owned parameter group:

- Is created and owned by the customer.
- Can be assigned to any of the customer's compatible clusters.
- Can be modified by the customer to create a custom parameter group. ‡

‡ Not all parameter values can be modified. For more information, see [Engine specific parameters](parametergroups.md "parametergroups.md").
