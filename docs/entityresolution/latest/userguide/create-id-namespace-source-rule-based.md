

# Creating an ID namespace source (rule-based)
<a name="create-id-namespace-source-rule-based"></a>

This topic describes the process of creating an ID namespace source using the **rule-based** method. This method uses matching rules to translate first-party data from a source to a target in an ID mapping workflow.

**Note**  
If the input data is the source, then it must have a schema mapping and an associated AWS Glue database.

**To create an ID namespace source (rule-based)**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Data preparation**, choose **ID namespaces**.

1. On the **ID namespaces** page, in the upper right corner, choose **Create ID namespace**.

1. For **Details**, do the following:

   1. For **ID namespace name**, enter a unique name.

   1. (Optional) For **Description**, enter an optional description.

   1. For **ID namespace type**, choose **Source**.

1. For the **ID namespace method**, choose **Rule-based**.

1. For **Data input**, choose the **Input type** that you want to use and then take the recommended actions.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source-rule-based.html)

1. For **Rule parameters**, do the following.

   1. Specify the **Rule controls** by choosing one of the following options based on your goal.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source-rule-based.html)

      **Rule controls** must be compatible between the source and the target to be used in an ID mapping workflow. For example, if a source ID namespace limits rules to the target but the target ID namespace limits rules to the source, this results in an error.

   1. Specify the **Matching rules** by choosing one of the following options based on your data input type.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source-rule-based.html)

1. For **Comparison and matching parameters**, do the following.

   1. Specify the **Comparison type** by choosing one of the following options based on your goal.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source-rule-based.html)

   1. Specify the **Record matching type** by choosing one of the following options based on your goal.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source-rule-based.html)
**Note**  
You must specify compatible limitations for the source and target ID namespaces. For example, if a source ID namespace limits rules to the target but the target ID namespace limits rules to the source, this results in an error.

1. Specify the **Service access permissions** by choosing an **Existing service role name** from the dropdown list.

1. (Optional) To enable **Tags** for the resource, choose **Add new tag**, and then enter the **Key** and **Value** pair.

1. Choose **Create ID namespace**.

 The ID namespace source is created. You are now ready to [create an ID namespace target](create-id-namespace-target.md).