

# Override a capacity plan in Connect Customer
<a name="override-capacity-plan"></a>

**Note**  
Plan override is not available for Scheduling plans. The following procedure applies to Hiring plans only.

You can upload a .csv file that overrides the **Required FTEs (without Shrinkage)** data in the **Plan outputs** section of a capacity plan. This section is shown in the following image. 

![The Plan Outputs section of the capacity plan, the Required FTEs (without Shrinkage).](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-override-without-shrinkage.png)


You might want to do this, for example, to give your team of agents a buffer.

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Analytics**, **Capacity planning - Edit**. 

   For more information, see [Assign permissions](required-optimization-permissions.md). 

1. On the Connect Customer navigation menu, select **Analytics and optimization**, **Capacity Planning**.

1. On the **Capacity Plans** tab, choose the plan. 

1. On the detailed page for the capacity plan, choose **Actions**, **Upload plan override**, and then choose **download the CSV template file**. This option is shown in the following image.  
![The apply override section, the link to download the .csv template file.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-download-override-template2.png)

   The .csv file template has one row. It contains the values that were displayed in the **Required FTEs (without Shrinkage)** row of the **Plan outputs** table. The following image shows an example of this data in a .csv file  
![A csv file, the data for the Required FTEs without shrinkage.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-override-template.png)

1. Make your changes, and save the template file with a different name. Return to the **Upload override** dialog box (you might need to choose **Actions**, **Upload plan override** to redisplay the dialog box), choose **Upload CSV**, and then choose **Override**.

1. After you upload the .csv file, the metrics in the **Required FTEs (without Shrinkage)** row are automatically re-calculated and updated. Pause on the blue triangle to see the original value, as shown in the following image.   
![The Plan Outputs section showing a triangle indicator that displays the original value for the required FTEs.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-override-without-shrinkage-blue.png)

1. The rest of the metrics are updated automatically to reflect the latest change for **Required FTEs (without Shrinkage)**.