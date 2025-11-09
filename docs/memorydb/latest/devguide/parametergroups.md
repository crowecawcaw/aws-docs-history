# Modifying a parameter group

###### Important

You cannot modify any default parameter group.

You can modify some parameter values in a parameter group.
These parameter values are applied to clusters associated with the
parameter group.
For more information on when a parameter value change is applied to a parameter group,
see [Engine specific parameters](parametergroups.md "parametergroups.md").

## Modifying a parameter group (Console)

The following procedure shows how to change the parameter's value
using the MemoryDB console.
You would use the same procedure to change the value of any parameter.

###### To change a parameter's value using the MemoryDB console

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. To see a list of all available parameter groups,
   in the left hand navigation pane choose **Parameter Groups**.
3. Choose the parameter group you want to modify by choosing the radio button to the left
   of the parameter group's name.

Choose **Actions** and then **View details**. Alternatively, you can also choose the parameter group name to go to the details page. 4. To modify the parameter, choose **Edit**. All the editable parameters will be enabled to be edited. You may have to move across pages to find the parameter you want to change. Alternatively, you can search for the parameter by name, value or type in the search box. 5. Make any necessary parameter modifications. 6. To save your changes, choose **Save changes**. 7. If you modified parameter values across number of pages, you can review all the changes by choosing **Preview changes**. To confirm the changes, choose **Save changes**. To make more modifications, choose **back**. 8. The **Parameter details** page also gives you the option to reset to default values. To reset to default values,
choose **Reset to defaults**. Checkboxes will appear on the left side of all the parameters.
You can select the ones you want to reset and choose **Proceed to reset** to confirm.

Choose **confirm** to confirm the reset action on the dialogue box. 9. The parameter details page allows you to set the number of parameters you want to see on each page. Use the cogwheel on the right side to make those changes. You can also enable/disable the columns you want on the details page. These changes last through the session of the console.

To find the name of the parameter you changed, see [Engine specific parameters](parametergroups.md "parametergroups.md").

## Modifying a parameter group (AWS CLI)

To change a parameter's value using the AWS CLI,
use the command `update-parameter-group`.

To find the name and permitted values of the parameter you want to change, see [Engine specific parameters](parametergroups.md "parametergroups.md")

For more information, see [update-parameter-group](../../../cli/latest/reference/memorydb/update-parameter-group.md "../../../cli/latest/reference/memorydb/update-parameter-group.md").

## Modifying a parameter group (MemoryDB API)

To change a parameter group's parameter values using the MemoryDB API,
use the `UpdateParameterGroup` action.

To find the name and permitted values of the parameter you want to change, see [Engine specific parameters](parametergroups.md "parametergroups.md")

For more information, see [`UpdateParameterGroup`](../APIReference/API_UpdateParameterGroup.md "../APIReference/API_UpdateParameterGroup.md").
