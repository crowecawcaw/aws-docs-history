# Create asset models, component models, and interfaces for AWS IoT SiteWise

AWS IoT SiteWise asset models, component models, and interfaces drive standardization of your industrial data. Asset models define the overall asset, such as a wind turbine or a manufacturing line. Component models represent the individual components that make up the asset, such as blades, generators, or sensors. Interfaces enforce standards across different asset models. By creating these models, you can organize and structure your asset data in a way that reflects the real-world relationships and hierarchies of your industrial equipment, making it easier to monitor, analyze, and maintain.

An asset model or component model contains a name, description, asset properties, and (optionally) custom composite models that
group properties together, or that reference component models for subassemblies.

In AWS IoT SiteWise, you can create asset models, component models, and interfaces to represent the structure and properties of your industrial assets and their components.

- You use an **asset model** to create assets. In addition to the features
  listed above, an asset model can also contain hierarchy definitions that define relationships among
  assets.
- A **component model** represents a subassembly within an asset model or
  another component model. When you create a component model, you can add references to it in asset models and
  in other component models. However, you can't create assets directly from component models.
- An **interface** enforces standards across different asset models. Interfaces define common properties, metrics, and hierarchies that must be implemented by asset models. You can't create assets directly from interfaces, but they help ensure consistency across similar asset types.
  After you create an asset model or component model, you can create custom composite models
  for it to group properties together or to reference existing component models. You can also link interfaces to asset models to enforce standardization.

For details about how to create asset models, component models, and interfaces, see the following
sections.

###### Topics

- [Create asset models in AWS IoT SiteWise](create-asset-models.md "create-asset-models.md")
- [Create component models](create-component-models.md "create-component-models.md")
- [Define data properties](asset-properties.md "asset-properties.md")
- [Create custom composite models (components)](create-custom-composite-models.md "create-custom-composite-models.md")
