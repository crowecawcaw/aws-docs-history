AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Manage transactions for AWS Mainframe Modernization

applications

With AWS Mainframe Modernization you can run an application, by request, at the same time as many other users who
submit requests to run the same application using the same files and programs. A single
transaction consists of one or more application programs that carry out the needed
processing.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md") and in [Create an AWS Mainframe Modernization application](applications-m2-create.md "applications-m2-create.md").

## Manage transactions for

applications

###### To manage transactions for applications

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the application that you want to
   run was created.
3. On the **Applications** page, choose the application where you want to
   manage transactions.
4. On the **Transactions** tab, under **Transaction
   resources**, choose how you want your resources displayed from the dropdown list.
   You can display resources according to transaction resources, groups, lists, or SITs.
   - **Transaction resources** allow you to choose the resource type
     according to file definitions, transaction definitions, program definitions, or transient
     data queue definitions.

   ###### Note

   The AWS Mainframe Modernization service supports additional resource types to manage transactions for
   applications, and can be accessed in the console.
   - **Groups** are collection of transaction resources. You can choose
     groups that you want to associate with your transaction resource.
   - **Lists** are ordered collection of groups. You can see all your
     transaction resources and groups in a list view. The **startup list**
     determines which resources are loaded when the server is initialized.
     - With AWS Blu Age refactor engine, you specify the lists to be included at the startup. There
       is no limit to number of lists.
     - With Rocket Software replatform engine, you can specify up to four lists in one SIT.

   - **SIT (System Initialization Table)** displays all available
     transaction configurations. You can find SITs according to properties (name, description,
     and startup lists). You can also choose lists to associate with your chosen SIT.

   ###### Note

   SITs are only applicable for the Rocket Software replatform engine.

5. Choose a transaction resource to display all the resource information. You can also view
   all attributes associated with your transaction resource.
