This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Choosing a Supported Output Captions

Format

Before you set up captions in your job, make sure that the transcode you want to set
up is supported. Support for a particular output caption format depends on the following factors:

- _Output container_. A given output caption can appear only in specific
  output containers.
- _Input container_. From a given input container, AWS Elemental Server can read
  certain caption formats.
- _Input captions format_. For a given caption format in the source, the
  AWS Elemental Server can create output captions in one or more formats.

###### To find the supported output captions formats, given your output container, input

container and input captions format

1. Find the **Supported Caption Formats** table on the web interface of your
   AWS Elemental Server appliance. The URL for this table is
   <your-AWS Elemental Server-node>/help/reference#supported_captions.
   1. Choose the **Support** tab on the web interface. These top-level tabs
      are at the top of the web interface, just below the AWS Elemental logo.

   ###### Note

   Choose the word **Support**. Don't choose from the dropdown
   menu. 2. Choose the **Reference** tab from the set of tabs just below the label
   **Table of Contents**. 3. Choose **Supported Caption Formats** from the left navigation menu on
   the **Reference** page.

2. Find the table with the heading that corresponds to your output container.
3. In the **Original Input Container** column, find your input
   container.
4. Of the rows that show your input container, find the row that shows your input captions
   format in the **Original Caption Format** column.

###### Note

If your input captions format isn't shown in any row that also shows your input
container, your input captions format isn't supported. 5. Find your choices for output captions formats in the third column of that row under
**Supported Output Caption Formats**.
