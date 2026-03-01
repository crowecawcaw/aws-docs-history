# Sharing a custom framework in AWS Audit Manager

You can use the framework sharing feature of AWS Audit Manager to quickly replicate the custom
frameworks that you create. You can share your custom frameworks with another AWS account,
or replicate your frameworks into another AWS Region under your own account. The recipient
can then access your custom framework and use it to create assessments. They can do this
without having to repeat any of your configuration efforts for that framework.

## Key points

To share a custom framework, you create a _share
request_. The recipient of the share request then has 120 days to accept or
decline the request. When they accept the share request, Audit Manager replicates the shared custom
framework into their framework library. In addition to replicating the custom framework,
Audit Manager also replicates any custom control sets and custom controls that are part of that
framework. These custom controls are then added to the recipient’s control library. Audit Manager
doesn’t replicate standard frameworks or controls. By default, these are available in all
AWS accounts and Regions where Audit Manager is enabled.

The framework sharing feature is available on the paid tier only. However, there are no
additional charges for sharing a custom framework or accepting a share request. To learn
more about pricing for AWS Audit Manager, see the [AWS Audit Manager pricing page](https://aws.amazon.com/audit-manager/pricing "https://aws.amazon.com/audit-manager/pricing").

###### Important

You may not share a custom framework that is derived from a standard framework if the
standard framework is designated as not eligible for sharing by AWS, unless you have
obtained permission to do so from the owner of the standard framework. To see which
standard frameworks are not eligible for sharing and learn more, see [Framework sharing eligibility](share-custom-framework-concepts-and-terminology.md#eligibility "share-custom-framework-concepts-and-terminology.md#eligibility").

## Additional resources

To learn more about how to share custom frameworks in Audit Manager, see the following
resources.

- [Framework sharing concepts and terminology](share-custom-framework-concepts-and-terminology.md "share-custom-framework-concepts-and-terminology.md")
- [Sending request to share a custom framework in AWS Audit Manager](framework-sharing.md "framework-sharing.md")
- [Responding to share requests in AWS Audit Manager](responding-to-shared-framework-requests.md "responding-to-shared-framework-requests.md")
- [Deleting share requests in AWS Audit Manager](deleting-shared-framework-requests.md "deleting-shared-framework-requests.md")
