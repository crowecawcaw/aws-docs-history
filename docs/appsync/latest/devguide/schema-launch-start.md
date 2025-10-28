# Launching a

schema
in the AWS AppSync console

In this example, you will create a `Todo` API that allows users to create `Todo` items
for daily chore reminders like `Finish task` or `Pick up
 groceries`. This API will demonstrate how to use GraphQL operations where the state persists in
a DynamoDB table.

Conceptually, there are three major steps to creating your first GraphQL API. You must define the schema
(types and fields), attach your data source(s) to your field(s), then write the resolver that handles the
business logic. However, the console experience changes the order of this. We will begin by defining how we
want our data source to interact with our schema, then define the schema and resolver later.

###### To create your GraphQL API

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
2. In the **Dashboard**, choose **Create
   API**.
3. While **GraphQL APIs** is selected, choose **Design from scratch**.
   Then, choose **Next**.
4. For **API name**, change the prepopulated name to `Todo API`,
   then choose **Next**.

###### Note

There are also other options present here, but we won't be using them for this example. 5. In the **Specify GraphQL resources** section, do the following:

    1. Choose **Create type backed by a DynamoDB table now**.


    ###### Note

    This means we are going to create a new DynamoDB table to attach as a data source.
    2. In the **Model Name** field, enter `Todo`.


    ###### Note

    Our first requirement is to define our schema. This **Model
     Name** will be the type name, so what you're really doing is creating a
     `type` called `Todo` that will exist in the schema:


    ```
    type Todo {}
    ```
    3. Under **Fields**, do the following:


    	1. Create a field named `id`, with the type `ID`, and
    	 required set to `Yes`.


    	###### Note

    	These are the fields that will exist within the scope of your `Todo` type.
    	 Your field name here will be called `id` with a type of
    	 `ID!`:


    	```
    	type Todo {
    		id: ID!
    	}
    	```
    	AWS AppSync supports multiple scalar values for different use cases.
    	2. Using **Add new field**, create four additional fields with
    	 the `Name` values set to `name`, `when`,
    	 `where`, and `description`. Their
    	 `Type` values will be `String`, and the `Array` and
    	 `Required` values will both be set to `No`. It will look like
    	 this:



    	![Model information form showing fields for a Todo model with ID, name, when, where, and description.](images/model-information-tutorial.png)

    	###### Note

    	The full type and its fields will look like this:


    	```
    	type Todo {
    		id: ID!
    		name: String
    		when: String
    		where: String
    		description: String
    	}
    	```
    	Because we're creating a schema using this predefined model, it will also be populated
    	 with several boilerplate mutations based on the type such as `create`,
    	 `delete`, and `update` to help you populate your data source
    	 easily.
    4. Under **configure model table**, enter a table name, such as
     `TodoAPITable`. Set the **Primary Key** to
     `id`.


    ###### Note

    We're essentially creating a new DynamoDB table called `TodoAPITable`
     that will be attached to the API as our primary data source. Our primary key is set to the
     required `id` field that we defined before this. Note that this new table is blank
     and doesn't contain anything except for the partition key.
    5. Choose **Next**.

6. Review your changes and choose **Create API**. Wait a moment to let the AWS AppSync
   service finish creating your API.
   You have successfully created a GraphQL API with its schema and DynamoDB data source. To summarize the steps
   above, we chose to create a completely new GraphQL API. We defined the name of the API, then added our schema
   definition by adding our first type. We defined the type and its fields, then chose to attach a data source to
   one of the fields by creating a new DynamoDB table with no data in it.
