# Augmenting Amazon Quick Sight insights with

Amazon Q Business

Amazon Quick account admins can connect their Quick account to Amazon Q Business
to augment insights with unstructured data sources. [Amazon Q Business](https://aws.amazon.com//q/business/ "https://aws.amazon.com//q/business/") is a generative AI assistant that helps your
team work smarter. It can answer questions, provide summaries, generate content, and
securely complete tasks based on the information in your enterprise systems.

When an Quick account is integrated with Amazon Q Business, users can now
leverage this vast repository of organizational knowledge alongside their structured
data analytics. This integration allows for more comprehensive and context-rich
insights, as it combines quantitative data from Quick with qualitative
information from various business documents and applications.

For more information about connecting your Amazon Q Business account with Quick,
see [Creating an
Quick-integrated application](../../../amazonq/latest/qbusiness-ug/create-application-quicksight.md "../../../amazonq/latest/qbusiness-ug/create-application-quicksight.md").

Use the following topics to configure an Amazon Q Business application in
Quick.

###### Topics

- [Considerations](#generative-bi-q-business-considerations "#generative-bi-q-business-considerations")
- [Configuring an Amazon Q Business
  application in Amazon Quick Sight](generative-bi-q-business-configure.md "generative-bi-q-business-configure.md")
- [Connect a
  Quick account to an existing Amazon Q Business application](generative-bi-q-business-link-existing-account.md "generative-bi-q-business-link-existing-account.md")
- [Disconnect an
  Amazon Q Business application from an Amazon Quick account](generative-bi-q-business-delete-connection.md "generative-bi-q-business-delete-connection.md")

## Considerations

The following limitations apply to the Amazon Q Business application.

- Quick and Amazon Q Business must exist in the same AWS account.
  Cross account calls are not supported.
- Quick and Amazon Q Business accounts need to exist in the same AWS
  Region. Cross Region calls are not supported. For a list of all supported
  Quick Regions, see [Supported AWS Regions for Amazon Q in Quick](regions.md#regions-aqs "regions.md#regions-aqs"). For a list of all supported Amazon Q Business
  Regions, see [Service quotas for
  Amazon Q Business](../../../amazonq/latest/qbusiness-ug/quotas-regions.md "../../../amazonq/latest/qbusiness-ug/quotas-regions.md").

If your Quick account exists in more than one Region, you can
connect one Amazon Q Business application from each Region to the Quick
account. For example, if your Quick account exists in
US East (N. Virginia) and US West (Oregon), one Amazon Q Business application
located in US East (N. Virginia) and one Amazon Q Business application located in
US West (Oregon) can be connected to the Quick account.

- Quick and Amazon Q Business accounts that are integrated need to use
  the same identity methods. For example, if a Quick account uses
  IAM Identity Center for identity management, the Amazon Q Business account that it is integrating
  with must also use IAM Identity Center for identity management.
- Email addresses that are associated with Quick users and
  groups are used to perform authorization checks in Amazon Q Business.
