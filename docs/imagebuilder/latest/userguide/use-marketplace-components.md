# Use AWS Marketplace components to customize your image

In addition to a large selection of images created by Independent Software Vendors
(ISVs), the AWS Marketplace offers components that you can use to customize your own Image Builder
images. You must subscribe to these AWS Marketplace components before you can use
them in your image recipe to build a new image.

When you specify an AWS Marketplace component in an image recipe, Image Builder validates
the subscription and performs dependency checks to ensure that you have
the resources that you need to use it. When validation succeeds, Image Builder creates secure
downloads for the component and its artifacts for use by image pipeline builds.

## Discover AWS Marketplace components

You can discover AWS Marketplace software components to use in your recipes from the
**Discover products** page in the Image Builder console, as follows.

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. From the navigation pane, choose **Discover products** in the
   **AWS Marketplace** section.
3. Select the **Components** tab. This tab lists all of the AWS Marketplace
   products that use the delivery option that includes associated components
   in AWS Marketplace.
4. To search for specific software products that include components, you can
   enter part of the name in the search bar or filter by `Status`,
   `Operating System`, `Publisher`, or `Categories`.
   The search bar also contains pagination controls for your results.

### Results

Each AWS Marketplace product has its own detail panel that includes the following information.

**The AWS Marketplace product name and logo**

The software product name is linked to the product detail in AWS Marketplace. You can
select the link to learn more about the product in AWS Marketplace. Alternatively, you
can view a summary of subscription options and subscribe directly from the search
results with the **View subscription options** button if you've
already done your research.

**Version**

This contains the primary version of the component.

**Operating system**

The operating system that the component is designed to run on.

**Publisher**

The publisher of the component. This is linked to the publisher detail page in AWS Marketplace. The
publisher detail page opens in a new tab in your browser.

**Categories**

One or more AWS Marketplace product categories that apply for the component.

**Status**

Shows whether you are subscribed to this product. If you're not subscribed,
you can choose **View subscription options** to see a summary of
the subscription options for the AWS Marketplace product, and optionally subscribe directly
from the Image Builder console.

**Associated components**

If the AWS Marketplace product has one or more versions that are included with your
subscription, they are shown in the **Associated components**
section. The section is collapsed initially, and displays a count of the associated
components. You can expand the section to see more details.

###### Note

The Center for Internet Security (CIS) component that's associated with
their AWS Marketplace image product is not shown in the **Discover products**
results. If you subscribe to their image product, the associated component is shown
in the **Subscriptions** page, and as a third-party component
in the **Create image recipe** dialog. For more information about
the component, see [CIS hardening components](toe-cis.md "toe-cis.md").

## Subscribe to AWS Marketplace components

After you've found an AWS Marketplace product with components that you want to use in your
recipes, you can subscribe to it directly from the Image Builder console, as follows, or you can
subscribe from the AWS Marketplace console.

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. From the navigation pane, choose **Discover products** in the
   **AWS Marketplace** section.
3. Select the **Components** tab. This tab lists all of the AWS Marketplace
   products that use the delivery option that includes associated components
   in AWS Marketplace.
4. To search for a specific AWS Marketplace product, enter part of the name in the
   search bar. If you know the publisher, but not the exact product name or
   how to spell it, you can also filter by `Publisher` to get a list
   of products that the publisher has available.
5. Select the product that you want to subscribe to from the results list,
   and choose **View subscription options**. This shows a
   summary of subscription options for the AWS Marketplace product.
6. Select **Subscribe** to subscribe to the product without
   leaving the Image Builder console. You are notified that the subscription is being
   processed. After you're subscribed, the **Status** is
   updated to `Subscribed`.

For more information about the AWS Marketplace products that you're currently subscribed to, see the
console steps described in [AWS Marketplace subscriptions in Image Builder](integ-marketplace.md#integ-marketplace-subs "integ-marketplace.md#integ-marketplace-subs").

## Use an AWS Marketplace component in an Image Builder image recipe

You can use AWS Marketplace components in your Image Builder image recipes the same way that you
use other types of components. For most of the components that are associated with
an AWS Marketplace image product, the ownership category is `AWS Marketplace`. For example, to
use a build component from an AWS Marketplace product that you've subscribed to, choose
**Add build components**, and select `AWS Marketplace` from the list.
This opens a selection panel on the right side of the console interface that lists AWS Marketplace
components.

###### Note

If you're looking for the CIS hardening component, select `Third party 
 managed`, from the ownership list instead of `AWS Marketplace`.

For more information about how to select, arrange, and configure parameters for
your components, see [Create a new version of an image recipe](create-image-recipes.md "create-image-recipes.md").
