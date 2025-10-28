# Create custom asset types in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, assets represent specific types of data resources such as database
tables, dashboards, or machine learning models. To provide consistency and
standardization when describing catalog assets, an Amazon SageMaker Unified Studio domain must have a set of
asset types that define how assets are represented in the catalog. An asset type defines
the schema for a specific type of asset. An asset type has a set of required and
optional nameable metadata form types. Asset types in Amazon SageMaker Unified Studio are versioned. When
assets are created, they are validated against the schema defined by their asset type
(typically latest version), and if an invalid structure is specified, asset creation
fails.

**System asset types** - Amazon SageMaker Unified Studio provisions
service-owned system asset types. System asset types cannot be altered. Amazon SageMaker Unified Studio
includes the following system asset types:

- Amazon Bedrock chat app
- Amazon Bedrock flow app
- Amazon Bedrock inference only
- Amazon Bedrock model
- Amazon Bedrock prompt
- Databricks table
- Databricks view
- AWS Glue table
- AWS Glue view
- Amazon Redshift table
- Amazon Redshift view
- Amazon S3 object collection
- SageMaker feature group
- SageMaker model package group
- Snowflake table
- Snowflake view
- Data product
  **Custom asset types** - to create custom asset types,
  you start by creating the required metadata form types and glossaries to use in the form
  types. You can then create custom asset types by specifying a name, description, and
  associated metadata forms that can be required or optional.

For asset types with structured data, to represent the column schema in Amazon SageMaker Unified Studio, you
can use the `RelationalTableFormType` to add the technical metadata to your
columns, including column names, descriptions, and data types, and the `ColumnBusinessMetadataForm` to add the business descriptions of the columns,
including business names, glossary terms, and custom key value pairs.

To create a custom asset type in Amazon SageMaker Unified Studio, complete the following steps:

1.  Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
    using your SSO or AWS credentials.
2.  Choose **Select project** from the top navigation pane and
    select the project where you want to create a custom asset type.
3.  Navigate to the **Discover** menu in the top
    navigation.
4.  Choose **Data catalog**.
5.  Choose **View asset types**.
6.  Choose **Create asset type**.
7.  Specify the following:
    - **Name** - the name of the custom asset type
    - **Description** - the description of the custom asset
      type.
    - Choose **Add metadata form** to add metadata forms to
      this custom asset type.
    - Under **Usage permission**, restrict access, by
      specify which projects or domain units are authorized to use this asset
      type.

    ###### Note

    You must be a domain unit owner or a project owner in order to
    modify usage permissions. Project contributors can view usage
    permissions but cannot edit them.

    You can choose the following:

        + **All projects** - give permissions to all
         projects in this domain
        + **Owning project** - give permissions only to
         the owning project
        + **Selected projects or domain units** - give
         permissions to specific projects and/or domain units


        If you select this option, choose **Add usage
         permission**, and in the **Add projects and
         designations** pop up window, specify the
         authorized projects (you can choose **Select projects in
         a domain unit** or **All project in a
         domain unit**), the specific domain unit, and the
         allowed designations - which designations a project member must
         have to use this policy. You can choose
         **Owner** or
         **Contributor**.

8.  Choose **Create**. After the custom asset type is created,
    you can use it to create assets.
