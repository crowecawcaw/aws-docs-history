# Creating a schema mapping

This procedure describes the process of creating a schema mapping using the [AWS Entity Resolution console](https://console.aws.amazon.com/entityresolution/home "https://console.aws.amazon.com/entityresolution/home").

There are three ways to create a schema mapping:

- Import existing input data using the **Import from AWS Glue** option
  – Use this creation method to define input fields starting with pre-populated
  columns from an AWS Glue table using a guided flow.
- Manually defining input data using the **Build custom schema** option
  – Use this creation method to manually define the input fields using a guided
  flow.
- Manually create using the **Use JSON editor** option – Use a
  JSON editor to manually create, use a sample, or import existing input data.

###### Note

The **Unique ID** and **Input fields** aren't
available with this option.

Import from AWS Glue

###### To create schema mapping by importing existing input data from AWS Glue

1.  Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2.  In the left navigation pane, under **Data preparation**, choose
    **Schema mappings**.
3.  On the **Schema mappings** page, in the upper right corner,
    choose **Create schema mapping**.
4.  For **Step 1: Specify schema details**, do the following:
    1. For **Name and creation method**, enter a **Schema
       mapping name** and an optional
       **Description**.
    2. For **Creation method**, choose **Import from
       AWS Glue**.
    3. Choose the **AWS Region**.
    4. Choose the **AWS Glue database**.
    5. Choose the **AWS Glue table**.

    To create a new table, go to the AWS Glue console [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/"). For more
    information, see [AWS Glue
    tables](../../../glue/latest/dg/tables-described.md "../../../glue/latest/dg/tables-described.md") in the _AWS Glue User
    Guide_. 6. For **Unique ID**, specify the column that distinctly
    references each row of your data.

    ###### Example

    For example: `Primary_key`,
    `Row_ID`, or `Record_ID`.

    ###### Note

    The **Unique ID** column is required. The
    **Unique ID** must be a unique identifier within a single
    table. However, across different tables, the **Unique ID**
    can have duplicate values. If the **Unique ID** isn't
    specified, isn't unique within the same source, or overlaps in terms of
    attribute names across sources, then AWS Entity Resolution rejects the record when the
    matching workflow is run. If you are using this schema mapping in a rule-based
    matching workflow, the **Unique ID** must not exceed 38
    characters. 7. For **Input fields**, choose the columns you want to use
    for matching and for optional pass through.

    You can choose a maximum of 34 columns total for both matching and pass
    through.

        1. Under **Matching**, choose the columns you to use as
         input fields for matching.


        You can choose a maximum of 24 columns total for matching.
        2. Select **Add columns for pass through** if you want to
         specify the columns that aren't used for matching.
        3. (Optional) Under **Pass through**, choose the columns
         to include as pass through columns.###### Note

    Do not use any of the following reserved names as a column name in your
    data when running machine learning-based matching workflows:
    "`MatchId`", "`MatchRule`", `RecordId`,
    `SourceId`", " and `TargetId`". Using any of these
    reserved names will result in naming conflicts and failed ML-based matching
    workflows. 8. (Optional) If you want to enable **Tags** for the resource,
    choose **Add new tag**, and then enter the
    **Key** and **Value** pair. 9. Choose **Next**.

5.  For **Step 2: Map input fields**, define the input fields you
    want to use for matching and for optional pass through.
    1. For **Input fields for matching**, for each **Input
       field**,
       - Specify the **Attribute type** to classify the
         data.
       - Specify the **Match key name** to enable input field
         comparison to your matching workflow. Certain match key names are
         automatically associated with specific attribute types by default.
       - Select the **Hashed** checkbox if the column value for
         that input field is hashed or leave the checkbox blank if the value is
         cleartext.

    ###### Note

    If you're creating a schema mapping to use with the LiveRamp provider
    service-based matching technique, then you can:

        * Specify the **Attribute type** for the Provider ID as
         **LiveRamp ID**.
        * Specify the **Attribute type** for the
         **name** field as either multiple fields (such as
         **First name**, **Last name**) or in
         one field.
        * Specify the **Attribute type** for the
         **street address** field as either multiple fields
         (such as **Street address 1**, **Street address
         2**, ) or in one field (**Full
         address**).


        If matching against an address, a zip code (**Postal
         code**) is required.
        * If you include email (**Email address**) or phone
         (**Phone number**) with a name, those fields can match
         against the street address.

    ###### Note

    If you're creating a schema mapping to use with the TransUnion provider
    service-based matching technique, then you can specify any of the following
    **Attribute types**:

        * **Full name**, **First name**,
         **Last name**
        * **Full address**, **Street address
         1**, **City**, **State**,
         **Country**, **Postal code**
        * **Phone number**
        * **Email address**
        * **Date**
        * **Digital Identifiers**: **IPV4**,
         **IPV6**, or **MAID**

    ###### Note

    If you're creating a schema mapping to use with the machine learning-based
    matching workflow, your dataset must contain at least one of the following
    **Attribute types**:

        * **Full name**
        * **Full address**
        * **Full phone**
        * **Email address**
        * **Date** with a **Match key name**
         of **Date of birth**Don't specify the **Attribute type** for any of these

    attributes as a **Custom string**. 2. (Optional) For **Input ﬁelds for pass through**, add the
    input ﬁelds that won't be matched and their corresponding **Hashing
    status**.

    The **Hashing status** indicates if the column value for
    that input field is hashed or cleartext. 3. Choose **Next**.

6.  For **Step 3: Group data**, you can group the
    **Name**, **Address**, and **Phone
    number** input fields if they have been separated into multiple
    fields.

This step concatenates the related input fields into one field, which enables
you to compare them as one field in a matching workflow.

If you don't have any data mapped to the **Name**,
**Address**, or **Phone number** input fields,
then this section will be blank.

You can also add more groups if you have more types of data.

    1. If you want to group **Name** input data:


    For **Full name**, choose two or more **Input
     fields** you want to group.


    The **Group name** and **Match key** are
     automatically associated with the data type.


    You can update the **Group name** and the **Match
     key** with a custom match key can contain up to 255 characters,
     including letters, numbers, underscores (\_), or hyphens (-).


    Choose **Add group** to add another group.


    ###### Note

    Normalization is only supported for **Full name**.

    If you want to normalize the **Full name** subtypes, then
     assign the following subtypes to the **Full name** group:
     **First name**, **Middle name**, and
     **Last name**.
    2. If you want to group **Address** input data:


    For **Full address**, choose two or more **Input
     fields** fields you want to group.


    The **Group name** and **Match key**. are
     automatically associated with the data type.


    You can update the **Group name** and the **Match
     key** with a custom match key can contain up to 255 characters,
     including letters, numbers, underscores (\_), or hyphens (-).


    Choose **Add group** to add another group.


    ###### Note

    Normalization is only supported for **Full
     address**.

    If you want to normalize the **Full address** subtypes,
     then assign the following subtypes to the **Full address**
     group: **Street address 1**, **Street address
     2**: **Street address 3 name**, **City
     name**, **State**, **Country**,
     and **Postal code**.
    3. If you want to group **Phone** input data:


    For **Full phone**, choose two or more **Input
     fields** fields you want to group.


    The **Group name** and **Match key**. are
     automatically associated with the data type.


    You can update the **Group name** and the **Match
     key** with a custom match key can contain up to 255 characters,
     including letters, numbers, underscores (\_), or hyphens (-).


    Choose **Add group** to add another group.


    ###### Note

    Normalization is only supported for **Full
     phone**.

    If you want to normalize the **Full phone** subtypes,
     then assign the following subtypes to the **Full phone**
     group: **Phone number**, and **Phone country
     code**.
    4. Choose **Next**.

7. For **Step 4: Review and create**, do the following:
   1. Review the selections that you made for the previous steps and edit if
      necessary.
   2. Choose **Create schema mapping**.

   ###### Note

   You can’t modify a schema mapping after you associate it to a workflow.
   You can clone a schema mapping if you want to use an existing configuration to
   create a new schema mapping.

After you create the schema mapping, you're ready to [create a
matching workflow](create-matching-workflow.md "create-matching-workflow.md") or [create an ID namespace](id-namespace.md "id-namespace.md").

Build custom schema

###### To create a schema mapping using the **Build custom schema**

option

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2. In the left navigation pane, under **Data preparation**, choose
   **Schema mappings**.
3. On the **Schema mappings** page, in the upper right corner,
   choose **Create schema mapping**.
4. For **Step 1: Specify schema details**, do the following:
   1. For name and creation method, enter a **Schema mapping
      name** and an optional **Description**.
   2. For **Creation method**, choose **Build custom
      schema**.
   3. For **Unique ID**, enter a unique ID to identify each row
      of your data.

   ###### Example

   For example: `Primary_key`,
   `Row_ID`, or `Record_ID`.

   ###### Note

   The **Unique ID** column is required. The
   **Unique ID** must be a unique identifier within a single
   table. However, across different tables, the **Unique ID**
   can have duplicate values. If the **Unique ID** isn't
   specified, isn't unique within the same source, or overlaps in terms of
   attribute names across sources, then AWS Entity Resolution rejects the record when the
   matching workflow is run. If you are using this schema mapping in a rule-based
   matching workflow, the **Unique ID** must not exceed 38
   characters. 4. (Optional) If you want to enable **Tags** for the resource,
   choose **Add new tag**, and then enter the
   **Key** and **Value** pair. 5. Choose **Next**.

5. For **Step 2: Map input fields**, define the input fields you
   want to use for matching and for optional pass through.

You can define a maximum of 34 columns total for both matching and pass through.

    1. For **Input fields for matching**, enter an **Input
     field**.


    ###### Note

    Do not use any of the following reserved names as a column name in your
     data when running machine learning-based matching workflows:
     "`MatchId`", "`MatchRule`", `RecordId`,
     `SourceId`", " and `TargetId`". Using any of these
     reserved names will result in naming conflicts and failed ML-based matching
     workflows.
    2. Select the **Attribute type** to classify the data.


    ###### Note

    If you're creating a schema mapping to use with the [LiveRamp provider service-based matching
     technique](create-matching-workflow-provider.md#create-mw-liveramp "create-matching-workflow-provider.md#create-mw-liveramp"), then you can specify the providerID **Attribute
     type** as **LiveRamp ID**. If you want to include
     PII data in the output, then you must specify the **Attribute
     type** as **Custom string**.


    ###### Note

    If you're creating a schema mapping to use with the TransUnion provider
     service-based matching technique, then you can specify any of the following
     **Attribute types**:



    	* **Full name**, **First name**,
    	 **Last name**
    	* **Full address**, **Street address
    	 1**, **City**, **State**,
    	 **Country**, **Postal code**
    	* **Phone number**
    	* **Email address**
    	* **Date**
    	* **Digital Identifiers**: **IPV4**,
    	 **IPV6**, or **MAID**
    ###### Note

    If you're creating a schema mapping to use with the [machine learning-based matching
     workflow](create-matching-workflow-ml.md "create-matching-workflow-ml.md"), your dataset must contain at least one of the following
     **Attribute types**:



    	* **Full name**
    	* **Full address**
    	* **Full phone**
    	* **Email address**
    	* **Date** with a **Match key name**
    	 of **Date of birth**Don't specify the **Attribute type** for any of these
     attributes as a **Custom string**.
    3. Select the **Match key name** to enable input field
     comparison to your matching workflow.


    Certain match key names are automatically associated with specific attribute
     types by default.
    4. Select the **Hashed** checkbox if the column value for that
     input field is hashed or leave the checkbox blank if the value is
     cleartext.
    5. Choose **Add input field** to add more input fields.


    You can add a maximum of 24 input fields total for matching.
    6. (Optional) For **Input fields for pass through**, add the
     input fields that won't be matched and their corresponding **Hashing
     status**.
    7. Choose **Next**.

6. For **Step 3: Group data**, you can group the
   **Name**, **Address**, **Phone
   number** input fields if they have been separated into multiple fields.

This step concatenates the related input fields into one field, which enables
you to compare them as one field in a matching workflow.

If you don't have any data mapped to **Name**,
**Address**, **Phone number** input fields, then
this section will be blank.

You can also add more groups if you have more types of data.

    1. If you want to group **Name** input data:


    For **Full name**, choose two or more **Input
     fields** you want to group.


    The **Group name** and **Match key** are
     automatically associated with the data type.


    You can update the **Group name** and the **Match
     key** with a custom match key can contain up to 255 characters,
     including letters, numbers, underscores (\_), or hyphens (-).


    Choose **Add group** to add another group.


    ###### Note

    Normalization is only supported for **Full name**.

    If you want to normalize the **Full name** subtypes, then
     assign the following subtypes to the **Full name** group:
     **First name**, **Middle name**, and
     **Last name**.
    2. If you want to group **Address** input data:


    For **Full address**, choose two or more **Input
     fields** fields you want to group.


    The **Group name** and **Match key**. are
     automatically associated with the data type.


    You can update the **Group name** and the **Match
     key** with a custom match key can contain up to 255 characters,
     including letters, numbers, underscores (\_), or hyphens (-).


    Choose **Add group** to add another group.


    ###### Note

    Normalization is only supported for **Full
     address**.

    If you want to normalize the **Full address** subtypes,
     then assign the following subtypes to the **Full address**
     group: **Street address 1**, **Street address
     2**: **Street address 3 name**, **City
     name**, **State**, **Country**,
     and **Postal code**.
    3. If you want to group **Phone** input data:


    For **Full phone**, choose two or more **Input
     fields** fields you want to group.


    The **Group name** and **Match key**. are
     automatically associated with the data type.


    You can update the **Group name** and the **Match
     key** with a custom match key can contain up to 255 characters,
     including letters, numbers, underscores (\_), or hyphens (-).


    Choose **Add group** to add another group.


    ###### Note

    Normalization is only supported for **Full
     phone**.

    If you want to normalize the **Full phone** subtypes,
     then assign the following subtypes to the **Full phone**
     group: **Phone number**, and **Phone country
     code**.
    4. Choose **Next**.

7. For **Step 4: Review and create**, do the following:
   1. Review the selections that you made for the previous steps and edit if
      necessary.
   2. Choose **Create schema mapping**.

   ###### Note

   You can’t modify a schema mapping after you associate it with a workflow.
   You can clone a schema mapping if you want to use an existing configuration to
   create a new schema mapping.

After you create the schema mapping, you're ready to [create a
matching workflow](create-matching-workflow.md "create-matching-workflow.md") or [create an ID namespace](id-namespace.md "id-namespace.md").

Use JSON editor

###### To create a schema mapping by using the JSON editor

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2. In the left navigation pane, under **Data preparation**, choose
   **Schema mappings**.
3. On the **Schema mappings** page, in the upper right corner,
   choose **Create schema mapping**.
4. For **Step 1: Specify schema details**, do the following:
   1. For name and creation method, enter a **Schema mapping
      name** and an optional **Description**.
   2. For **Creation method**, choose **Use JSON
      editor**.
   3. (Optional) If you want to enable **Tags** for the resource,
      choose **Add new tag**, and then enter the
      **Key** and **Value** pair.
   4. Choose **Next**.

5. For **Step 2: Specify mapping**:
   1. Start building the schema in the JSON editor or choose one of the following
      options based on your goal:

   | Your goal                          | Recommended option                                                         |
   | ---------------------------------- | -------------------------------------------------------------------------- |
   | Start building your schema mapping | \*_Insert sample JSON_<br>• and then edit the<br>information as necessary. |
   | Use an existing JSON file          | **Import from file**                                                       |

   ###### Note

   Normalization is only supported for the following
   **types**: `NAME`, `ADDRESS`,
   `PHONE`, and `EMAIL_ADRESS`.

   If you want to normalize the `NAME` subtypes, then assign the
   following subtypes to the `NAME`
   **groupName**: `NAME_FIRST`,
   `NAME_MIDDLE`, and `NAME_LAST`

   If you want to normalize the `ADDRESS` subtypes, then assign
   the following subtypes to the `ADDRESS`
   **groupName**: `ADDRESS_STREET1`,
   `ADDRESS_STREET2`, `ADDRESS_STREET3`,
   `ADDRESS_CITY`, `ADDRESS_STATE`,
   `ADDRESS_COUNTRY`, and `ADDRESS_POSTALCODE`.

   If you want to normalize the `PHONE` subtypes, then assign the
   following subtypes to the `PHONE`
   **groupName**: `PHONE_NUMBER` and
   `PHONE_COUNTRYCODE`. 2. Choose **Next**.

6. For **Step 3: Review and create**:
   1. Review the selections that you made for the previous steps and edit if
      necessary.
   2. Choose **Create schema mapping**.

   ###### Note

   You can’t modify a schema mapping after you associate it with a workflow.
   You can clone a schema mapping if you want to use an existing configuration to
   create a new schema mapping.

After you create the schema mapping, you're ready to [create a
matching workflow](create-matching-workflow.md "create-matching-workflow.md") or [create an ID namespace](id-namespace.md "id-namespace.md").
