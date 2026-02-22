# Item limits for Amazon Quick Sight analyses in the

Quick Sight APIs

Use the following table to review the current limits or quotas for different analysis
items in Amazon Quick Sight that are created and managed with the Amazon Quick Sight APIs. If your analysis
contains more than the supported number of analysis items, remove items to optimize the
performance of the analysis. New analysis items cannot be added to an analysis that
contains more than the supported number of analysis items.

| Analysis item                                                                                                                                                        | Limit                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [Sheets](../../../quicksuite/latest/userguide/working-with-multiple-sheets.md "../../../quicksuite/latest/userguide/working-with-multiple-sheets.md")                | 20 sheets per analysis                 |
| [Visuals](../../../quicksuite/latest/userguide/creating-a-visual.md "../../../quicksuite/latest/userguide/creating-a-visual.md")                                     | 50 visuals per sheet                   |
| [Calculated fields](../../../quicksuite/latest/userguide/working-with-calculated-fields.md "../../../quicksuite/latest/userguide/working-with-calculated-fields.md") | 500 per analysis and 200 per dataset\* |
| [Bookmarks](../../../quicksuite/latest/userguide/dashboard-bookmarks-create.md "../../../quicksuite/latest/userguide/dashboard-bookmarks-create.md")                 | 200 per dashboard                      |
| [Custom<br>actions](../../../quicksuite/latest/userguide/custom-actions.md "../../../quicksuite/latest/userguide/custom-actions.md")                                 | 10 per visual                          |
| [Filter<br>groups](../../../quicksuite/latest/userguide/add-a-compound-filter.md "../../../quicksuite/latest/userguide/add-a-compound-filter.md")                    | 2000 per analysis                      |
| [Filters](../../../quicksuite/latest/userguide/adding-a-filter.md "../../../quicksuite/latest/userguide/adding-a-filter.md")                                         | 20 filters per filter group            |
| [Parameters](../../../quicksuite/latest/userguide/parameters-in-quicksight.md "../../../quicksuite/latest/userguide/parameters-in-quicksight.md")                    | 400 per analysis                       |
| [Controls](../../../quicksuite/latest/userguide/filter-controls.md "../../../quicksuite/latest/userguide/filter-controls.md")                                        | 200 per sheet                          |
| [Text boxes](../../../quicksuite/latest/userguide/textbox.md "../../../quicksuite/latest/userguide/textbox.md")                                                      | 100 per sheet                          |
| [Image<br>components](../../../quicksuite/latest/userguide/image-component.md "../../../quicksuite/latest/userguide/image-component.md")                             | 10 per sheet                           |
| [Layer map<br>visuals](../../../quicksuite/latest/userguide/layered-maps.md "../../../quicksuite/latest/userguide/layered-maps.md")                                  | 5 per sheet                            |

\* The per dataset limit applies to calculations that were created in the analysis.
Dataset level calculations are not included in this limit. For more information about
dataset level calculations, see [Adding calculated fields](adding-a-calculated-field-analysis.md "adding-a-calculated-field-analysis.md").
