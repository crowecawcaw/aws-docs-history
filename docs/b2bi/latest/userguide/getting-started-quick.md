# Quick setup using the console

This topic provides instructions on how to quickly setup B2B Data Interchange. From the B2B Data Interchange landing page
([https://console.aws.amazon.com/b2bi/](https://console.aws.amazon.com/b2bi/ "https://console.aws.amazon.com/b2bi/")), choose the
**Quick setup** option. The quick setup makes it easy for you to create the
resources needed to build and run your EDI-based workflows on AWS B2B Data Interchange. Follow the steps below to
connect with your trading partners and start transforming EDI data in JSON and XML to simplify
your downstream integrations.

###### Note

If you don't see the landing page, select AWS B2B Data Interchange at the top of the left navigation
menu.

1. The **Create profile** screen appears. Fill in your details as described
   in [Create a profile](transform-inbound-variations.md#getting-started-profile "transform-inbound-variations.md#getting-started-profile"), then
   select **Next**.
2. The **Create transformer** screen appears. Fill in your details as
   described in [Create an inbound transformer](transform-inbound-variations.md#getting-started-transformer "transform-inbound-variations.md#getting-started-transformer") or [Create an outbound transformer](transform-outbound-variations.md#outbound-transformer "transform-outbound-variations.md#outbound-transformer"), then select **Next**.
3. The **Create trading capability** screen appears. Fill in your details as
   described in [Create a trading capability for inbound
   EDI](transform-inbound-variations.md#getting-started-capability "transform-inbound-variations.md#getting-started-capability"), then select **Next**.

###### Note

Make sure to choose **Copy policy**, for both your input and output
directory, save the policy code, and then paste the policies into your input and output
directory's bucket policy. 4. The **Create partner** screen appears. Fill in your details as described
in [Create a partnership for inbound
EDI](transform-inbound-variations.md#getting-started-partnership "transform-inbound-variations.md#getting-started-partnership"),
then select **Next**. 5. The **Review and create** screen appears, showing all the details you've
entered. You can select **Cancel**, or **Previous** if
anything needs to be changed, or **Complete setup** to create your profile,
transformer, trading capability and partnership.
B2B Data Interchange also provides a self-contained, AWS CloudFormation template to quickly create a B2B Data Interchange
configuration. For details on how to deploy this template, see [Configure AWS B2B Data Interchange using an CloudFormation template](quickstart-template.md "quickstart-template.md").
