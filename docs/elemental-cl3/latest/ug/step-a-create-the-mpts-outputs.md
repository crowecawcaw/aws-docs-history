

# Step 1: Create the MPTS
<a name="step-a-create-the-mpts-outputs"></a>

**To create an MPTS**

1. On the Conductor Live main menu, choose **MPTS**. Then choose **New MPTS**. The **Create a New MPTS** dialog appears.

1. Complete the fields in the top section of the dialog. For information about a field, hover on the upper-right corner of the field and choose the **?** icon. Pay particular attention to the following fields.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/ug/step-a-create-the-mpts-outputs.html)

1. Complete the fields in the **Output** tab and the **Advanced** tab. For more information about the significant fields, see the sections after this procedure.

1. Choose **Save**. 

   The MPTS appears in the list of MPTSes.

   If the node you selected is part of a 1-to-1 or 1-to-1 Plus redundancy group, Conductor Live automatically creates two instance of the MPTS. One instance is on the primary Elemental Statmux node, the other is on the secondary node. Both MPTS instances have the same downstream system destination or destinations.

   The next step in creating the MPTS is to [add channels](step-d-add-channels-to-the-mpts-output.md) (programs).

   Other optional steps are [adding passthrough streams](crud-mpts-pasthrough-streams.md), and [adding passthrough programs](crud-mpts-passthrough-programs.md).

**Topics**
+ [Output tab](step-create-mpts-tab-output.md)