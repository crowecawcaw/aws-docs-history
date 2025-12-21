Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Assets

_Assets_, in Amazon Monitron, are the pieces of equipment on your
factory floor. Typically, assets are individual machines, but they can also be sections of a
larger piece of equipment, part of an industrial process, or any element of your
manufacturing model.

Amazon Monitron currently supports the following default [ISO 20186](https://www.iso.org/standard/63180.html "https://www.iso.org/standard/63180.html") standard based machine
classes:

- **Class I** – Individual parts of engines and
  machines, integrally connected to the complete machine in its normal operating
  condition, for example, production electrical motors of up to 15 kW.
- **Class II** – Medium-sized machines
  (typically electrical motors with 15 kW to 75 kW output) without special
  foundations, rigidly mounted engines or machines (up to 300 kW) on special
  foundations.
- **Class III** – Large prime-movers and other
  large machines with rotating masses mounted on rigid and heavy foundations that are
  relatively stiff in the direction of vibration.
- **Class IV** – Large prime-movers and other
  large machines with rotating masses mounted on rigid and heavy foundations that are
  relatively soft in the direction of vibration measurement, for example,
  turbo-generator sets and gas turbines with outputs greater than 10 MW.
  You can also create custom classes for your assets to fit your use case better. For more
  information, see [Creating custom classes](custom-asset-class.md "custom-asset-class.md").

An asset is also the basis for viewing the health of your machines. To monitor machine
activity, you pair one or more sensors to the asset that you want to monitor. Each sensor
gives you insight into how that part of the asset is functioning, and together they provide
an overview of the entire asset. You can assign each sensor positioned on an asset can its
own machine class.

The following diagram shows one asset, an electric motor pump set. It has four positions,
each with a sensor, two on the motor and two on the pump. Each sensor collects data on the
temperature and vibration levels of that specific position on the pump. Amazon Monitron
then analyzes that data by comparing it to the baseline temperature and vibration levels of
that position to determine when a change, or abnormality, occurs. When that happens, it
sends a notification on the Amazon Monitron app.

![Diagram of motor and pump connected by coupling, with labeled components.](/images/Monitron/latest/user-guide/images/assets-positions.png)
This chapter explains how to manage your assets with Amazon Monitron, and how to pair
them to the sensors that monitor their health.

###### Topics

- [Creating asset classes](custom-asset-class.md "custom-asset-class.md")
- [Managing assets](as-assets.md "as-assets.md")
- [Viewing the list of assets](asset-list.md "asset-list.md")
- [Adding an asset](as-add-assets.md "as-add-assets.md")
- [Changing an asset name](as-edit-assets.md "as-edit-assets.md")
- [Moving an asset](moving-assets.md "moving-assets.md")
- [Deleting an asset](as-delete-assets.md "as-delete-assets.md")
