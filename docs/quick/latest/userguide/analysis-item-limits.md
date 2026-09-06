

# Item limits for Amazon Quick Sight analyses in the Quick Sight APIs
<a name="analysis-item-limits"></a>

Use the following table to review the current limits or quotas for different analysis items in Amazon Quick Sight that are created and managed with the Amazon Quick Sight APIs. If your analysis contains more than the supported number of analysis items, remove items to optimize the performance of the analysis. New analysis items cannot be added to an analysis that contains more than the supported number of analysis items.


| Analysis item | Limit | 
| --- | --- | 
| [Sheets](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-multiple-sheets) | 20 sheets per analysis | 
| [Visuals](https://docs.aws.amazon.com/quicksuite/latest/userguide/creating-a-visual) | 50 visuals per sheet | 
| [Calculated fields](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-calculated-fields) | 500 per analysis and 200 per dataset\* | 
| [Bookmarks](https://docs.aws.amazon.com/quicksuite/latest/userguide/dashboard-bookmarks-create) | 200 per dashboard | 
| [Custom actions](https://docs.aws.amazon.com/quicksuite/latest/userguide/custom-actions) | 10 per visual | 
| [Filter groups](https://docs.aws.amazon.com/quicksuite/latest/userguide/add-a-compound-filter) | 2000 per analysis | 
| [Filters](https://docs.aws.amazon.com/quicksuite/latest/userguide/adding-a-filter) | 20 filters per filter group | 
| [Parameters](https://docs.aws.amazon.com/quicksuite/latest/userguide/parameters-in-quicksight) | 400 per analysis | 
| [Controls](https://docs.aws.amazon.com/quicksuite/latest/userguide/filter-controls) | 200 per sheet | 
| [Text boxes](https://docs.aws.amazon.com/quicksuite/latest/userguide/textbox) | 100 per sheet | 
| [Image components](https://docs.aws.amazon.com/quicksuite/latest/userguide/image-component) | 10 per sheet | 
| [Layer map visuals](https://docs.aws.amazon.com/quicksuite/latest/userguide/layered-maps) | 5 per sheet | 

\* The per dataset limit applies to calculations that were created in the analysis. Dataset level calculations are not included in this limit. For more information about dataset level calculations, see [Adding calculated fields](adding-a-calculated-field-analysis.md).