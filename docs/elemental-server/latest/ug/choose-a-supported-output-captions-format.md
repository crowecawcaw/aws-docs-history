

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Choosing a Supported Output Captions Format
<a name="choose-a-supported-output-captions-format"></a>

Before you set up captions in your job, make sure that the transcode you want to set up is supported. Support for a particular output caption format depends on the following factors: 
+ *Output container*. A given output caption can appear only in specific output containers.
+ *Input container*. From a given input container, AWS Elemental Server can read certain caption formats.
+ *Input captions format*. For a given caption format in the source, the AWS Elemental Server can create output captions in one or more formats.

**To find the supported output captions formats, given your output container, input container and input captions format**

1. Find the **Supported Caption Formats** table on the web interface of your AWS Elemental Server appliance. The URL for this table is <your-AWS Elemental Server-node>/help/reference\#supported\_captions.

   1. Choose the **Support** tab on the web interface. These top-level tabs are at the top of the web interface, just below the AWS Elemental logo.
**Note**  
Choose the word **Support**. Don't choose from the dropdown menu.

   1. Choose the **Reference** tab from the set of tabs just below the label **Table of Contents**. 

   1. Choose **Supported Caption Formats** from the left navigation menu on the **Reference** page.

1. Find the table with the heading that corresponds to your output container.

1. In the **Original Input Container** column, find your input container.

1. Of the rows that show your input container, find the row that shows your input captions format in the **Original Caption Format** column.
**Note**  
If your input captions format isn't shown in any row that also shows your input container, your input captions format isn't supported.

1. Find your choices for output captions formats in the third column of that row under **Supported Output Caption Formats**.