# Creating an index for an Amazon Q Business application

Before you can add data in your Amazon Q Business application, you need to
connect it to the following components:

- An **index** – This is where the data you
  add is stored and organized.
- A **retriever** – This is the tool that
  fetches data from an index during conversations.
  Once these are created, you can then add data sources and configure features like
  metadata boosting or document enrichment.

You have two options for indices and retrievers to connect to your application:

- **Amazon Q Business native index and
  retriever** – Amazon Q Business provides a native
  index you can add your data to. Choosing this index creates an Amazon Q Business index that can connect to the Amazon Q Business
  supported data sources that you choose.
- **Amazon Kendra index and retriever** – If you're
  already an Amazon Kendra customer, you can connect your Amazon Kendra index with data sources
  attached to your Amazon Q Business application and use it as a retriever.
  You create an Amazon Kendra index using the Amazon Kendra console or API, and add it as a
  retriever when using the Amazon Q Business console or API.

###### Note

The option to create an Amazon Kendra index is visible on the console only if
you're already an Amazon Kendra user.

If you're connecting a Amazon Kendra GenAI Enterprise Edition index from an
Amazon Q Business application, you can detach it and use it with other AWS Gen AI
services, like Amazon Bedrock. Detaching an Amazon Kendra index automatically
deletes the retriever Amazon Q Business created for it. For a list of features
supported by Amazon Kendra GenAI Enterprise indices, see [Amazon Kendra GenAI Enterprise Edition
index](../../../kendra/latest/dg/hiw-index-types.md#kendra-gen-ai-index "../../../kendra/latest/dg/hiw-index-types.md#kendra-gen-ai-index").

###### Note

Amazon Q Business uses user email ID to determine end user access to
documents in an index. When you connect an Amazon Kendra index to Amazon Q Business, Amazon Q Business relays the user’s identifying
email ID to Amazon Kendra to enable document filtering for end users. If data
sources connected to your Amazon Kendra index don’t use email-ID based document
filtering, or the email ID is not present, Amazon Q Business generates
responses only from public documents.
**For instructions on how to select an index and
retriever,** choose a topic based on your index preference for Amazon Q.

###### Topics

- [Creating an Amazon Q Business index](#native-retriever "#native-retriever")
- [Connecting an Amazon Kendra index as retriever](#add-kendra-retriever "#add-kendra-retriever")

## Creating an Amazon Q Business index

To create a Amazon Q Business index and retriever, you can use either the
AWS Management Console, or the [CreateIndex](../api-reference/API_CreateIndex.md "../api-reference/API_CreateIndex.md") and [CreateRetriever](../api-reference/API_CreateRetriever.md "../api-reference/API_CreateRetriever.md") API operations.

If you use the AWS Management Console, Amazon Q Business creates a retriever for you when
you create the index. When you use the API, you need to create a retriever for your
index separately.

The following tabs provide a procedure for the AWS Management Console and code examples for the
AWS CLI.

Console
**To create an Amazon Q Business
retriever**

1.  Sign in to the AWS Management Console and open the Amazon Q Business
    console.
2.  Complete the steps to create your Amazon Q Business
    application.
3.  In **Applications**, select the name of your
    application from the list of applications.
4.  From the left navigation menu, choose **Data
    sources**.
5.  From the **Data sources** page, choose
    **Add index**.
6.  From the **Add index** page, choose
    **Create a new index** and then do the
    following:
    1. In **Name your index with a unique
       identifier**, for **Index
       name**, input a name for your Amazon Q Business application.

    You can include hyphens (-), but not spaces. Maximum
    of 1000 alphanumeric characters.

    ###### Important

    You can't change the name of the index after it's
    created.

    ###### Note

    Available data sources when you select this option
    include all [Amazon Q Business
    supported data connectors](supported-connectors.md "supported-connectors.md") and direct
    document upload. 2. In **Index provisioning**, do the
    following:

        1. Choose between **Enterprise**
         and **Starter** index types based
         on your use case. For more information on index
         types, see [Index types](tiers.md#index-tiers "tiers.md#index-tiers").
        2. For **Number of units**
         – Choose the number of index units that you
         need. Amazon Q Business charges you based on
         the document capacity that you choose. If you
         choose an Enterprise index, You can choose up to
         50 units. If you choose a Starter index, you can
         choose up to 5 units. Each unit is 20,000
         documents or 200 MB, whichever is reached first.
         For more information on index provisioning
         pricing, see [Amazon Q Business pricing](https://aws.amazon.com/q/business/pricing/ "https://aws.amazon.com/q/business/pricing/").

7.  To create your index and retriever, choose **Add
    index**.

AWS CLI
**To create an Amazon Q Business
index**

```

aws qbusiness create-index \
--application-id `application-id` \
--display-name `display-name` \
--description `index-description` \
--capacity-configuration units `=<index-capacity-units>` \
--type `ENTERPRISE | STARTER`

```

**To create an Amazon Q Business
retriever**

```

aws qbusiness create-retriever \
--application-id `application-id` \
--display-name `display-name` \
--type `NATIVE_INDEX` \
--role-arn `roleArn` \
--configuration `nativeIndexConfiguration="{indexId=<created-index-id>}" \`
--tags `tags`

```

## Connecting an Amazon Kendra index as retriever

If you use Amazon Kendra, you can connect an existing Amazon Kendra index as a
retriever to your Amazon Q Business application environment.

You [create a
Amazon Kendra index](../../../kendra/latest/dg/create-index.md "../../../kendra/latest/dg/create-index.md") using the Amazon Kendra console and API. To connect a Amazon Kendra index to
Amazon Q Business, you can use the Amazon Q Business console or the [CreateRetriever](../api-reference/API_CreateRetriever.md "../api-reference/API_CreateRetriever.md") API operation.

If you're connecting a Amazon Kendra GenAI Enterprise Edition index from an Amazon Q Business
application, you can detach it and use it with other AWS Gen AI services, like
Amazon Bedrock. Detaching an Amazon Kendra index automatically deletes the retriever
Amazon Q Business created for it. For a list of features supported by Amazon Kendra GenAI
Enterprise indices, see [Amazon Kendra GenAI Enterprise Edition
index](../../../kendra/latest/dg/hiw-index-types.md#kendra-gen-ai-index "../../../kendra/latest/dg/hiw-index-types.md#kendra-gen-ai-index").

###### Note

If you choose to use an Amazon Kendra index as retriever, data in your
Amazon Kendra will be connected to your Amazon Q Business
application environment. If you use an Amazon Kendra index, you can't use Amazon Q Business
data connectors or direct document upload for your application environment.

###### Note

Amazon Q Business uses user email ID to determine end user access to
documents in an index. When you connect an Amazon Kendra index to Amazon Q Business, Amazon Q Business relays the user’s identifying email ID to Amazon Kendra to
enable document filtering for end users. If data sources connected to your Amazon Kendra
index don’t use email-ID based document filtering, or the email ID is not
present, Amazon Q Business generates responses only from public
documents.

For more information about Amazon Kendra, see the following topics in the
Amazon Kendra User Guide and API Reference:

- [What is
  Amazon Kendra?](../../../kendra/latest/dg/what-is.md "../../../kendra/latest/dg/what-is.md")
- [Creating a data source connector](../../../kendra/latest/dg/data-source.md "../../../kendra/latest/dg/data-source.md")
- [Amazon Kendra API Reference](../../../kendra/latest/APIReference/welcome.md "../../../kendra/latest/APIReference/welcome.md")

The following tabs provide a procedure for the AWS Management Console and code samples for the
AWS CLI.

Console
**To connect an Amazon Kendra
index**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. Complete the steps to create your Amazon Q Business
   application.
3. In **Applications**, select the name of your
   application from the list of applications.
4. From the left navigation menu, choose **Data
   sources**.
5. From the **Data sources** page, choose
   **Add index**.
6. From the **Add index** page, choose
   **Use an existing Amazon Kendra index** and then do
   the following:
   1. In **Select an index**, select an
      existing Amazon Kendra index. All data sources
      synced to your Amazon Kendra index will be
      connected to your Amazon Q Business
      application environment.
   2. For **Authorization** – Create
      and use a new service role to connect Amazon Kendra
      to Amazon Q Business or use an existing
      one.
   3. For **Service role name** –
      Provide a name for your IAM access role.
      Or, choose to use the auto-generated role that's
      provided.

7. Select **Add index**, to connect your Amazon Kendra
   index to your application.

AWS CLI
**To connect an Amazon Kendra
index**

```

aws qbusiness create-retriever \
--display-name `display-name` \
--type `KENDRA_INDEX` \
--role-arn `roleArn` \
--configuration `kendraIndexConfiguration="{indexId=<kendra-index-id>`

```
