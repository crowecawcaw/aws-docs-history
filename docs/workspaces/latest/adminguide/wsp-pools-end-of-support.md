# Amazon WorkSpaces Pools end of support

After careful consideration, we decided to end support for Amazon WorkSpaces Pools, effective
December 31, 2027. Amazon WorkSpaces Pools will no longer accept new customers beginning July 31, 2026. As an existing customer, you can continue to use the service as normal until
December 31, 2027. After December 31, 2027, you will no longer be able to access the
Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources.

This page provides important information to help you understand the impact of this change
and plan your transition to Amazon WorkSpaces Applications before the end-of-support date.

## Service updates until end of support

If you are an existing Amazon WorkSpaces Pools customer who created WorkSpaces Pools resources and
desktops before June 30, 2026, you can continue to use the service as normal until
December 31, 2027, including creating WorkSpaces Pools resources or desktops. During this
period, AWS will focus on maintaining service availability and addressing critical
functional or security issues. No new features or major enhancements will be introduced
prior to the end-of-support date. Customers can continue to use existing WorkSpaces Pools
resources until support ends on December 31, 2027.

## Alternative to Amazon WorkSpaces Pools

We recommend migrating to Amazon WorkSpaces Applications, a fully managed, secure application
streaming service that provides users with instant access to their desktop applications
and non-persistent virtual desktops from anywhere. WorkSpaces Applications provides:

- Non-persistent virtual desktops for end users centrally managed by IT
  administrators
- Broad [AWS
  Region support](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/"), [instance type
  selections](../../../appstream2/latest/developerguide/instance-types.md "../../../appstream2/latest/developerguide/instance-types.md"), and [pay-as-you-go
  pricing](https://aws.amazon.com/workspaces/applications/pricing/ "https://aws.amazon.com/workspaces/applications/pricing/")
- [Multi-session
  support](../../../appstream2/latest/developerguide/multi-session-recs.md "../../../appstream2/latest/developerguide/multi-session-recs.md") and [Bring-your-own-license
  support](../../../appstream2/latest/developerguide/byol-windows-images.md "../../../appstream2/latest/developerguide/byol-windows-images.md") for Windows desktop
- Automatic scaling of compute resources based on user demand, with no
  infrastructure to provision or maintain
- Access from any device using the [WorkSpaces
  Applications client](../../../appstream2/latest/developerguide/clients-access-methods-user.md "../../../appstream2/latest/developerguide/clients-access-methods-user.md") or a [supported web
  browser](../../../appstream2/latest/developerguide/web-browser-user.md "../../../appstream2/latest/developerguide/web-browser-user.md")

Using WorkSpaces Applications allows you to continue delivering non-persistent cloud
desktops to your users. For more information about WorkSpaces Applications, see
[What Is WorkSpaces
Applications?](../../../appstream2/latest/developerguide/what-is-appstream.md "../../../appstream2/latest/developerguide/what-is-appstream.md")

## Migrate from WorkSpaces Pools to WorkSpaces Applications

To prepare for the end of support, customers should complete the following steps
before December 31, 2027.

If you created a custom image for WorkSpaces Pools, you can import that image into WorkSpaces
Applications for use with your new environment. To migrate your image:

1. Navigate to **WorkSpaces Applications** >
   **Images** > **Import image**.
2. Select **Amazon WorkSpaces Image** as the image
   source.
3. Enter your WorkSpaces Image ID (starting with "wsi-").

This creates a WorkSpaces Applications image from your existing WorkSpaces Pools image. For
details, see [To
import an image](../../../appstream2/latest/developerguide/import-image.md#import-image-procedure "../../../appstream2/latest/developerguide/import-image.md#import-image-procedure").
Alternatively, you can create a new image in WorkSpaces Applications using [Image
Builder](../../../appstream2/latest/developerguide/managing-image-builders.md "../../../appstream2/latest/developerguide/managing-image-builders.md").

Follow the [WorkSpaces Applications setup
guide](../../../appstream2/latest/developerguide/setting-up.md "../../../appstream2/latest/developerguide/setting-up.md") to configure the remaining resources for your WorkSpaces Applications
environment, including VPC and networking, fleets, stacks, and user access settings.
After you complete the setup, you can provide your users with access to WorkSpaces
Applications, and they can begin streaming sessions.

We recommend testing with a select group of end users to validate your business
applications and user experience before migrating all users from WorkSpaces Pools to WorkSpaces
Applications. After validating migration is complete and WorkSpaces Pools resources are no
longer used, you can review and clean up your WorkSpaces Pools resources.

AWS encourages customers to begin planning their transition as early as possible to
ensure a smooth experience before the end-of-support date.

## Need help or have questions?

If you have questions about this change or need assistance planning your migration,
contact us through [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support") or reach out to your AWS account manager. You can also review
the following FAQs for more information.

## FAQs

What happens if I don't migrate by December 31, 2027?

You will no longer be able to use Amazon WorkSpaces Pools to stream desktops to
your end users, or manage Amazon WorkSpaces Pools resources using the console after
December 31, 2027.

How can I get help with migration?

If you have questions about migrating to WorkSpaces Applications, contact
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support") or reach out to your AWS account manager for assistance.

Will I continue to receive support before December 31, 2027?

Yes, you will continue to receive support through [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support") before
December 31, 2027.
