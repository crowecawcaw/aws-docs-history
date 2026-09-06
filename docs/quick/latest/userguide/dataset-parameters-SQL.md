

# Creating dataset parameters in Amazon Quick
<a name="dataset-parameters-SQL"></a>

Use the following procedures to get started using dataset parameters.

**To create a new dataset parameter**

1. From the Quick start page, choose **Data** on the left, choose the ellipsis (three dots) next to the dataset that you want to change, and then choose **Edit**.

1. On the **Dataset** page that opens, choose **Parameters** on the left, and then choose the (\+) icon to create a new dataset parameter.

1. In the **Create new parameter** pop-up that appears, enter a parameter name in the **Name** box.

1. In the **Data type** dropdown, choose the parameter data type that you want. Supported data types are `String`, `Integer`, `Number`, and `Datetime`. This option can't be changed after the parameter is created.

1. For **Default value**, enter the default value that you want the parameter to have.
**Note**  
When you map a dataset parameter to an analysis parameter, a different default value can be chosen. When this happens, the default value configured here is overridden by the new default value.

1. For **Values**, choose the value type that you want the parameter to have. **Single value** parameters support single–select dropdowns, text field, and list controls. **Multiple values** parameters support multi–select dropdown controls. This option can't be changed after the parameter is created.

1. When you are finished configuring the new parameter, choose **Create** to create the parameter.