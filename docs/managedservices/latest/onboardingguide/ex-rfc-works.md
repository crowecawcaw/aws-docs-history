

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Learn about RFCs
<a name="ex-rfc-works"></a>

Requests for change, or RFCs, work in a two-fold manner. First, there are parameters required for the RFC itself. These are the options in the `CreateRfc` API. And second, there are parameters required for the action of the RFC (the execution parameters). To learn about the `CreateRfc` options, see the [CreateRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html) section of the *AMS API Reference*. These options typically appear in the **Additional configurations** area of the Create RFC pages.

You can create and submit an RFC with the `CreateRfc` API, `aws amscm create-rfc` CLI, or using the AMS console Create RFC pages. For a tutorial on creating an RFC, see [Create an RFC](ex-rfc-create-col.md).

**Topics**
+ [What are RFCs?](what-r-rfcs.md)
+ [Authenticate when using the AMS API/CLI](ex-rfc-authentication.md)
+ [Understand RFC security reviews](rfc-security.md)
+ [Understand RFC change type classifications](ex-rfc-csio.md)
+ [Understand RFC action and activity states](ex-rfc-action-state.md)
+ [Understand RFC status codes](ex-rfc-status-codes.md)
+ [Understand RFC update CTs and CloudFormation template drift detection](ex-rfc-updates-and-dd.md)
+ [Schedule RFCs](ex-rfc-scheduling.md)
+ [Approve or reject RFCs](ex-rfc-approvals.md)
+ [Request RFC restricted run periods](ex-rfc-restrict-execute.md)
+ [Create, clone, update, find, and cancel RFCs](ex-rfc-use-examples.md)
+ [Use the AMS console with RFCs](ex-rfc-gui.md)
+ [Learn about common RFC parameters](rfc-common-params.md)
+ [Sign up for the RFC daily email](rfc-digest.md)