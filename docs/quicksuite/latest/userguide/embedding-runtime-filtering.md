# Filtering data at runtime for

Amazon Quick Sight embedded dashboards and visuals

You can use filter methods in the Amazon Quick Sight embedding SDK to leverage the power
of Amazon Quick Sight filters within your software as a service (SaaS) application at
runtime. Runtime filters allow business owners to integrate their application with
their embedded Amazon Quick Sight dashboards and visuals. To accomplish this, create
customized filter controls in your application and apply filter presets based on
data from your application. Then, developers can personalize filter configurations
for end users at runtime.

Developers can create, query, update, and remove Amazon Quick Sight filters on an
embedded dashboard or visual from their application with the Amazon Quick Sight
Embedding SDK. Create Amazon Quick Sight filter objects in your application with the
[FilterGroup](../../../quicksight/latest/APIReference/API_FilterGroup.md "../../../quicksight/latest/APIReference/API_FilterGroup.md")
data model and apply them to embedded dashboards and visuals using the filter
methods. For more information about using the Amazon Quick Sight Embedding SDK, see
the [amazon-quicksight-embedding-sdk](https://github.com/awslabs/amazon-quicksight-embedding-sdk "https://github.com/awslabs/amazon-quicksight-embedding-sdk") on GitHub.

**Prerequisites**

Before you can get started, make sure that you are using the Amazon Quick Sight
Embedding SDK version 2.5.0 or higher.

## Terminology and concepts

The following terminology can be useful when working with embedded runtime
filtering.

- _Filter group_ – A group of individual
  filters. Filters that are located within a `FilterGroup` are
  OR-ed with each other. Filters within a [FilterGroup](../../../quicksight/latest/APIReference/API_FilterGroup.md "../../../quicksight/latest/APIReference/API_FilterGroup.md") are applied to the same sheets or
  visuals.
- _Filter_ – A single filter. The filter can
  be a category, numeric, or datetime filter type. For more information on
  filters, see [Filter](../../../quicksight/latest/APIReference/API_Filter.md "../../../quicksight/latest/APIReference/API_Filter.md").

## Setting up

Before you begin, make sure that you have the following assets and information
prepared.

- The sheet ID of the sheet that you want to scope the
  `FilterGroup` to. This can be obtained with the
  `getSheets` method in the Embedding SDK.
- The dataset and column identifier of the dataset that you want to
  filter. This can be obtained through the [DescribeDashboardDefinition](../../../APIReference/API_DescribeDashboardDefinition.md "../../../APIReference/API_DescribeDashboardDefinition.md") API operation.

Depending on the column type that you use, there might be restrictions
on the types of filters that can be added to an embedded asset. For more
information on filter restrictions, see [Filter](../../../quicksight/latest/APIReference/API_Filter.md "../../../quicksight/latest/APIReference/API_Filter.md").

- The visual ID of the visual that you want to scope the
  `FilterGroup` to, if applicable. This can be obtained by
  using the `getSheetVisuals` method in the Embedding
  SDK.

In addition to the `getSheetVisuals` method, the
`FilterGroup` that you add can only be scoped to the
currently selected sheet.

To use this feature, you must already have a dashboard or visual embedded into
your application through the Amazon Quick Sight Embedding SDK. For more
information about using the Amazon Quick Sight Embedding SDK, see the [amazon-quicksight-embedding-sdk](https://github.com/awslabs/amazon-quicksight-embedding-sdk "https://github.com/awslabs/amazon-quicksight-embedding-sdk") on GitHub.

## SDK method interface

**Dashboard embedding getter methods**

The following table describes different dashboard embedding getter methods
that developers can use.

| Method                                                        | Description                                                                                                                                                                                                                            |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `getFilterGroupsForSheet(sheetId: string)`                    | Returns all FilterGroups that are currently scoped to the sheet that is supplied in the parameter.                                                                                                                                     |
| `getFilterGroupsForVisual(sheetId: string, visualId: string)` | Returns all `FilterGroups` that are scoped to the visual that is supplied in the parameter.                                                                                                                                            | If the sheet that is supplied in the parameter is not the currently selected sheet of the embedded dashboard, the above methods return an error. **Visual embedding getter methods** The following table describes different visual embedding getter methods that developers can use. |
| Method                                                        | Description                                                                                                                                                                                                                            |
| ---                                                           | ---                                                                                                                                                                                                                                    |
| `getFilterGroups()`                                           | Returns all `FilterGroups` that are currently scoped to the embedded visual.                                                                                                                                                           | **Setter methods** The following table describes different setter methods that developers can use for dashboard or visual embedding.                                                                                                                                                  |
| Method                                                        | Description                                                                                                                                                                                                                            |
| ---                                                           | ---                                                                                                                                                                                                                                    |
| `addFilterGroups(filterGroups: FilterGroup[])`                | Adds and applies the supplied **FilterGroups** to the embedded dashboard or visual. A `ResponseMessage` that indicates whether the addition was successful is returned.                                                                |
| `updateFilterGroups(filterGroups: FilterGroup[])`             | Updates the `FilterGroups` on the embedded experience that contains the same `FilterGroupId` as the `FilterGroup` that is supplied in the parameter. A `ResponseMessage` that indicates whether the update was successful is returned. |
| `removeFilterGroups(filterGroupsOrIds: FilterGroup[]          | string[])`                                                                                                                                                                                                                             | Removes the supplied FilterGroups from the dashboard and returns a `ResponseMessage` that indicates whether the removal attempt is successful.                                                                                                                                        | The `FilterGroup` that is supplied must be scoped to the embedded sheet or visual that is currently selected. |
