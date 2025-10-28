# Key inputs

Auto Replenishment relies on the following inputs to make accurate and informed
calculations for inventory replenishment:

- **Demand** – Demand data is the fundamental input for
  replenishment calculations. This data helps AWS Supply Chain understand the
  demand either in terms of past sales or future forecasts to be able to
  determine inventory requirements for future time buckets. You can provide
  demand forecasts or past sales history as an input for demand data. If
  demand forecasts are not available, you can provide sales history, and
  AWS Supply Chain will use historical consumption rate for replenishment
  calculations.
- **Inventory** – Auto Replenishment uses on-hand inventory
  and on-order inventory as an input for replenishment calculations. On-hand
  inventory is the available inventory at locations that can be used to
  fulfill demands. On-order inventory is the open purchase or transfer orders
  that are inbound to the stocking location. Demand will be calculated from
  on-hand and on-order inventory to determine net supply requirements.
- **Lead time** – Lead time is the time it takes for an
  order to be placed and the items to be received. Lead time helps
  AWS Supply Chain determine how far in advance it must place orders. For
  items that are ordered or procured from suppliers, lead time will refer to
  supplier/vendor lead time, which is the time it takes for a supplier to
  fulfill an order and deliver the goods. Any time required for internal order
  processing, quality checks, or handling should be included as part of the
  lead time. For items or products that are transferred from an enterprise’s
  internal locations, such as distribution centers or fulfillment centers,
  lead time will refer to transportation time, which is the time required for
  transportation and delivery from a source location to a destination
  location.
- **Sourcing rules** – You can use sourcing rules to model
  supply chain network topology. Use sourcing rules to define relationships
  between different levels of locations (for example, regional DC to central
  DC) or relationships between suppliers and their sites. These relationships
  can be modeled at a product group or region level, or at a product or site
  level.
- **Sourcing schedules** – Use Auto Replenishment to
  regularly monitor and replenish items with every run, or configure
  predefined schedules for items to be replenished. Use a sourcing schedule to
  define ordering schedules based on suppliers or shipping schedules, and on
  transportation schedules. You can define a sourcing schedule to replenish
  items multiple times a week, once a week, or during specific weeks of the
  month.
- **Inventory policy** – Inventory policy is a key input to
  determine the target inventory level that is used to drive replenishment
  requirements. You can configure inventory policy at the most detailed
  product level, site level, or at an aggregate level such as product group,
  product segment, site, or region. Auto Replenishment supports absolute
  inventory level, days of cover, and service level inventory policies. You
  can define the target value for the configured inventory policy, and
  AWS Supply Chain uses the target value to determine the target inventory
  level.

For more information on data fields required for supply planning, see
[Supply Planning](entities-supply-planning.md "entities-supply-planning.md").
