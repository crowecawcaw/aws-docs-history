

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Creating an index for an Amazon Q Business application
<a name="select-retriever"></a>

Before you can add data in your Amazon Q Business application, you need to connect it to the following components:
+ An **index** – This is where the data you add is stored and organized.
+ A **retriever** – This is the tool that fetches data from an index during conversations.

Once these are created, you can then add data sources and configure features like metadata boosting or document enrichment.

You have two options for indices and retrievers to connect to your application:
+ **Amazon Q Business native index and retriever** – Amazon Q Business provides a native index you can add your data to. Choosing this index creates an Amazon Q Business index that can connect to the Amazon Q Business supported data sources that you choose.
+ **Amazon Kendra index and retriever** – If you're already an Amazon Kendra customer, you can connect your Amazon Kendra index with data sources attached to your Amazon Q Business application and use it as a retriever. You create an Amazon Kendra index using the Amazon Kendra console or API, and add it as a retriever when using the Amazon Q Business console or API.
**Note**  
The option to create an Amazon Kendra index is visible on the console only if you're already an Amazon Kendra user.  
If you're connecting a Amazon Kendra GenAI Enterprise Edition index from an Amazon Q Business application, you can detach it and use it with other AWS generative AI services, like Amazon Bedrock. Detaching an Amazon Kendra index automatically deletes the retriever Amazon Q Business created for it. For a list of features supported by Amazon Kendra GenAI Enterprise indices, see [Amazon Kendra GenAI Enterprise Edition index](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index-types.html#kendra-gen-ai-index).
**Note**  
Amazon Q Business uses user email ID to determine end user access to documents in an index. When you connect an Amazon Kendra index to Amazon Q Business, Amazon Q Business relays the user’s identifying email ID to Amazon Kendra to enable document filtering for end users. If data sources connected to your Amazon Kendra index don’t use email-ID based document filtering, or the email ID is not present, Amazon Q Business generates responses only from public documents.

**For instructions on how to select an index and retriever,** choose a topic based on your index preference for Amazon Q.

**Topics**
+ [Creating an Amazon Q Business index](#native-retriever)
+ [Connecting an Amazon Kendra index as retriever](#add-kendra-retriever)

## Creating an Amazon Q Business index
<a name="native-retriever"></a>

To create a Amazon Q Business index and retriever, you can use either the AWS Management Console, or the [CreateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateIndex.html) and [CreateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateRetriever.html) API operations.

If you use the AWS Management Console, Amazon Q Business creates a retriever for you when you create the index. When you use the API, you need to create a retriever for your index separately.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

**To create an Amazon Q Business retriever**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. Complete the steps to create your Amazon Q Business application.

1. In **Applications**, select the name of your application from the list of applications.

1. From the left navigation menu, choose **Data sources**.

1. From the **Data sources** page, choose **Add index**.

1. From the **Add index** page, choose **Create a new index** and then do the following:

   1. In **Name your index with a unique identifier**, for **Index name**, input a name for your Amazon Q Business application.

      You can include hyphens (-), but not spaces. Maximum of 1000 alphanumeric characters.
**Important**  
You can't change the name of the index after it's created.
**Note**  
Available data sources when you select this option include all [Amazon Q Business supported data connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-connectors.html) and direct document upload.

   1. In **Index provisioning**, do the following:

      1. Choose between **Enterprise** and **Starter** index types based on your use case. For more information on index types, see [Index types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers).

      1. For **Number of units** – Choose the number of index units that you need. Amazon Q Business charges you based on the document capacity that you choose. If you choose an Enterprise index, You can choose up to 50 units. If you choose a Starter index, you can choose up to 5 units. Each unit is 20,000 documents or 200 MB, whichever is reached first. For more information on index provisioning pricing, see [Amazon Q Business pricing](https://aws.amazon.com/q/business/pricing/).

1. To create your index and retriever, choose **Add index**.

------
#### [ AWS CLI ]

**To create an Amazon Q Business index**

```
aws qbusiness create-index \
--application-id {{application-id}} \
--display-name {{display-name}} \
--description {{index-description}} \
--capacity-configuration units {{=<index-capacity-units>}} \
--type ENTERPRISE | STARTER
```

**To create an Amazon Q Business retriever**

```
aws qbusiness create-retriever \
--application-id {{application-id}} \
--display-name {{display-name}} \
--type NATIVE_INDEX \
--role-arn {{roleArn}} \
--configuration {{nativeIndexConfiguration="{indexId=<created-index-id>}" \}}    
--tags {{tags}}
```

------

## Connecting an Amazon Kendra index as retriever
<a name="add-kendra-retriever"></a>

If you use Amazon Kendra, you can connect an existing Amazon Kendra index as a retriever to your Amazon Q Business application environment.

You [create a Amazon Kendra index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html) using the Amazon Kendra console and API. To connect a Amazon Kendra index to Amazon Q Business, you can use the Amazon Q Business console or the [CreateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateRetriever.html) API operation.

If you're connecting a Amazon Kendra GenAI Enterprise Edition index from an Amazon Q Business application, you can detach it and use it with other AWS generative AI services, like Amazon Bedrock. Detaching an Amazon Kendra index automatically deletes the retriever Amazon Q Business created for it. For a list of features supported by Amazon Kendra GenAI Enterprise indices, see [Amazon Kendra GenAI Enterprise Edition index](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index-types.html#kendra-gen-ai-index).

**Note**  
If you choose to use an Amazon Kendra index as retriever, data in your Amazon Kendra will be connected to your Amazon Q Business application environment. If you use an Amazon Kendra index, you can't use Amazon Q Business data connectors or direct document upload for your application environment.

**Note**  
Amazon Q Business uses user email ID to determine end user access to documents in an index. When you connect an Amazon Kendra index to Amazon Q Business, Amazon Q Business relays the user’s identifying email ID to Amazon Kendra to enable document filtering for end users. If data sources connected to your Amazon Kendra index don’t use email-ID based document filtering, or the email ID is not present, Amazon Q Business generates responses only from public documents.

For more information about Amazon Kendra, see the following topics in the Amazon Kendra User Guide and API Reference:
+ [What is Amazon Kendra?](https://docs.aws.amazon.com/kendra/latest/dg/what-is.html)
+ [Creating a data source connector](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html)
+ [Amazon Kendra API Reference](https://docs.aws.amazon.com/kendra/latest/APIReference/welcome.html)

The following tabs provide a procedure for the AWS Management Console and code samples for the AWS CLI. 

------
#### [ Console ]

**To connect an Amazon Kendra index**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. Complete the steps to create your Amazon Q Business application.

1. In **Applications**, select the name of your application from the list of applications.

1. From the left navigation menu, choose **Data sources**.

1. From the **Data sources** page, choose **Add index**.

1. From the **Add index** page, choose **Use an existing Amazon Kendra index** and then do the following:

   1. In **Select an index**, select an existing Amazon Kendra index. All data sources synced to your Amazon Kendra index will be connected to your Amazon Q Business application environment.

   1. For **Authorization** – Create and use a new service role to connect Amazon Kendra to Amazon Q Business or use an existing one.

   1. For **Service role name** – Provide a name for your IAM access role. Or, choose to use the auto-generated role that's provided.

1. Select **Add index**, to connect your Amazon Kendra index to your application.

------
#### [ AWS CLI ]

**To connect an Amazon Kendra index**

```
aws qbusiness create-retriever \
--display-name {{display-name}} \
--type KENDRA_INDEX \
--role-arn {{roleArn}} \
--configuration {{kendraIndexConfiguration="{indexId=<kendra-index-id>}}
```

------