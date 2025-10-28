# Asset model interfaces

AWS IoT SiteWise interfaces set standards across different asset models. They define a common
structure that ensures consistency while allowing for variations in implementation.

Interfaces share the same structure as asset models (properties, composite models, and
hierarchies) but you cannot create assets directly from them. Instead, interfaces are applied to
existing asset models to ensure standardization. Component models are not supported for interfaces.

Using interfaces provides several benefits:

- Standardized properties and metrics across different asset model variations
- Simplified metric definitions at the interface level
- More efficient management of complex asset hierarchies
- Independent property lifecycle management for each asset model variation
- Enhanced cross-team collaboration where operations teams focus on physical asset
  representation while data teams establish standards across equipment
  We recommend creating your asset models first to model your real-world industrial equipment.
  Every equipment type, with their own set of properties, can be represented by their own asset
  models.

## Asset model standardization use

case

Interfaces help standardize properties across different asset models while preserving
their unique characteristics.

For example, there are four stations in a powertrain shop: engine, transmission,
differential, and assembly. Each station contains various equipment types. For example, the
engine station includes CNC machines, but they differ in specifications: some are 3-axis,
while others are 5-axis.

![Diagram showing the hierarchy of the powertrain shop's equipment using only asset models and assets. The powertrain shop is at the top, then each of the asset models for the engine, transmission, differential and assemble stations on the second level down. On the third level down, there's the individual CNC machines broken down by axis stemming from the engine station asset model. Conversely, there's asset models stemming from the assemble station model as well. On the fourth level, are each of the assets representing the individual CNC machines or robotic arms by name.](images/models-interface-hierarchy.png)

However, interfaces let you create standards for commonalities seen in the CNC machines.
You can use the repeatable properties in an interface rather than create asset models for each
property.

For example, you can:

1. Create separate asset models for each category of machine types. In this example,
   that's the "CNC 3 Axis machines" and the "CNC 5 Axis machines."
2. Define a standard interface with common properties and metrics. In this example,
   `Temperature-in-C`, `Down-time`, and `Running-time` are
   all common properties that apply to both CNC machines.
3. Apply this interface to all CNC machine asset models, still allowing for
   device-specific properties on the individual asset models.

![Diagram showing how interfaces simplify the organization of asset models from previous diagram. It shows several repeatable parameters for the engine station CNC machines now governed by the interfaces carrying over to various properties to the 3-axis and 5-axis CNC machine asset models, while also allowing for device-specific properties on each.](images/models-interface-to-asset-models.png)

You can also define availability metrics at the interface level. For example, `Avail
 = avg(Down-time, Running-time)` calculates the availability based on the down time and
running time values.

Using interfaces simplifies your asset model management by ensuring consistent property
definitions and metrics across applicable equipment while maintaining the unique
characteristics of each machine type.

## Structure and components

Interfaces include the same property types as asset models: attributes, measurements,
transforms, and metrics. When overlayed on an asset model, you map existing properties to
their interface counterparts. Unmapped interface properties are automatically created in the
asset model.

Interface hierarchies define rollup metrics, while asset model hierarchies enable asset
associations. When you use an interface, the service will automatically map asset model
hierarchies to interface hierarchies when computing rollup metrics. After applying an
interface, rollup metrics are defined through the interface hierarchy rather than the asset
model's own hierarchy.

## Considerations

When working with interfaces, keep these considerations in mind:

- Asset model and interface properties can be automatically mapped by name or manually
  mapped. Hierarchies are automatically mapped by the service when computing rollup
  metrics.
- You cannot define additional metrics in the linked asset model that use interface
  metrics as inputs.
- An asset model can only be linked to one interface. However, you can have multiple
  asset models applied to the same interface.
- Alarms are not supported in interfaces.
- Component models are not supported for interfaces.

###### Topics

- [Understand the interface-asset model
  relationship](interface-asset-model-relationship.md "interface-asset-model-relationship.md")
- [Create an interface](interface-create.md "interface-create.md")
- [Apply an interface to an asset model](interfaces-link-asset-model.md "interfaces-link-asset-model.md")
- [Manage interfaces, linked asset models, and
  properties](interfaces-manage.md "interfaces-manage.md")
- [Additional interface examples](interface-additional-examples.md "interface-additional-examples.md")
