# Key inputs

Manufacturing Plans depends on various inputs to make accurate and informed
calculations for generating material, transfer, and production plans. Manufacturing
Plans uses the same list of inputs as Auto Replenishment for inventory target
calculation and net requirements determination for a product or site combination.
For information on Auto Replenishment inputs, see [Key inputs](key-input.md "key-input.md"). In addition, Manufacturing Plans also requires the
following inputs:

- **Bill of Material (BOM)** – The BOM data entity is used
  to capture relationships between finished goods and various sub-assemblies
  and components that are required to make the finished goods. BOMs can
  contain multiple levels of components under a finished good, including
  alternates. Alternate or substitute components can be modeled under the same
  parent by using the _alternate_group_
  field. AWS Supply Chain only supports priority-based alternates. Components
  with the lowest priority are selected by the planning process. Suppliers or
  vendors that supply components are not part of the BOM. This information is
  derived from sourcing rules and vendor management-related data
  entities.
- **Production process** – This process is used to model the
  production step for manufacturing finished goods. The sourcing rule contains
  a reference to the production process that's used to support the
  _Manufacture_ type of rule. AWS Supply Chain only
  supports a single step manufacturing process. The component requirement date
  is determined based on production lead time and setup time, as defined in
  the production process entity. Lead time is the offset from the finished
  goods demand date, which is used to determine the requirement date for
  components.

For information on data fields required for Supply Planning, see [Supply Planning](entities-supply-planning.md "entities-supply-planning.md").
