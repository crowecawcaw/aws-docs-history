# Item limits for Amazon Quick Sight analyses in the

Quick Sight APIs

Use the following table to review the current limits or quotas for different analysis
items in Amazon Quick Sight that are created and managed with the Amazon Quick Sight APIs. If your analysis
contains more than the supported number of analysis items, remove items to optimize the
performance of the analysis. New analysis items cannot be added to an analysis that
contains more than the supported number of analysis items.

| Analysis item                                                                              | Limit                                  |
| ------------------------------------------------------------------------------------------ | -------------------------------------- |
| [Sheets](working-with-multiple-sheets.md "working-with-multiple-sheets.md")                | 20 sheets per analysis                 |
| [Visuals](creating-a-visual.md "creating-a-visual.md")                                     | 50 visuals per sheet                   |
| [Calculated fields](working-with-calculated-fields.md "working-with-calculated-fields.md") | 500 per analysis and 200 per dataset\* |
| [Bookmarks](dashboard-bookmarks-create.md "dashboard-bookmarks-create.md")                 | 200 per dashboard                      |
| [Custom<br>actions](custom-actions.md "custom-actions.md")                                 | 10 per visual                          |
| [Filter<br>groups](add-a-compound-filter.md "add-a-compound-filter.md")                    | 2000 per analysis                      |
| [Filters](adding-a-filter.md "adding-a-filter.md")                                         | 20 filters per filter group            |
| [Parameters](parameters-in-quicksight.md "parameters-in-quicksight.md")                    | 200 per analysis                       |
| [Controls](filter-controls.md "filter-controls.md")                                        | 200 per sheet                          |
| [Text boxes](textbox.md "textbox.md")                                                      | 100 per sheet                          |
| [Image<br>components](image-component.md "image-component.md")                             | 10 per sheet                           |
| [Layer map<br>visuals](layered-maps.md "layered-maps.md")                                  | 5 per sheet                            |

\* The per dataset limit applies to calculations that were created in the analysis.
Dataset level calculations are not included in this limit. For more information about
dataset level calculations, see [Adding calculated fields](adding-a-calculated-field-analysis.md "adding-a-calculated-field-analysis.md").
