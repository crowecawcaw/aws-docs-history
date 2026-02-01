# Managing AMI-based product availability by AWS Region

and country

When you create a product in AWS Marketplace, you choose the AWS Regions where it is available.
You also choose the countries where buyers can purchase your product from. These two properties
are similar, but they are not the same. For example, a buyer might be located in, and purchasing
from, the United States, but they might be planning to install your product in the Europe (Frankfurt) Region. In order for
this buyer to purchase your product, you must include both the United States in your list of
countries, and the Europe (Frankfurt) Region in your list of Regions. You can use the following sections to update your
product availability by Region and country.

###### Topics

- [Add an AWS Region](#single-ami-adding-regions "#single-ami-adding-regions")
- [Restrict an AWS Region](#single-ami-restricting-regions "#single-ami-restricting-regions")
- [Update support for future
  AWS Regions](#single-ami-updating-future-region-support "#single-ami-updating-future-region-support")
- [Update availability by
  country](#single-ami-update-availability-by-country "#single-ami-update-availability-by-country")

## Add an AWS Region

You can add a Region where buyers can use your product.

###### To add a Region

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, and on the
   **Current server product** tab, select the product that you
   want to modify.
3. From the **Request changes** dropdown, choose **Add
   Region**.
4. Select the Region that you want to add from the list of available Regions.
5. Choose **Submit request** to submit your request for
   review.
6. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status becomes **Succeeded**.

###### Note

When you add support for a new AWS Region, customers already subscribed to
private offers for your product won't be able to access the newly added Region
automatically. You must create another private offer with the Region you want
customers to access. After accepting the new offer, customers can access the newly
added Region. Customers who subscribe to your product at a future date can also
access the Region, as long as the Region is included in the private offer. For more
information about how to create a new private offer, see [Private offer upgrades, renewals, and amendments](private-offers-upgrades-and-renewals.md "private-offers-upgrades-and-renewals.md").

###### Note

**FPGA Regional Requirements**

When adding regions to FPGA products, regional AFI clones are automatically created
by AWS Marketplace to ensure your product is available across supported AWS Regions. This
process ensures that buyers can deploy your FPGA-accelerated product in their preferred
Region without requiring manual AFI replication. The automatic cloning process maintains
consistency across all regions where your product is available.

## Restrict an AWS Region

To prevent new buyers from using your product in a specific AWS Region, you can
restrict the Region. You can add the Region back at a later time. Existing subscribers
of the product in the Region can continue using the product from the Region as long as
they're subscribed.

###### To restrict a Region

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, and on the
   **Current server product** tab, select the product that you
   want to modify.
3. From the **Request changes** dropdown, choose
   **Restrict Region**.
4. Select the dropdown menu to view the list of Regions in which your product is
   currently available.
5. Select the Regions that you want to restrict.
6. The Regions you have selected appear as tokens. Review the list of Regions
   that you're restricting, and enter X for Regions that you don't want to
   restrict.
7. Choose **Submit change request** to submit your request for
   review.
8. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status becomes **Succeeded**.

If your request is successful, your existing users receive the following email message
notifying them of the Region to be restricted. They can continue using your product as
long as they remain subscribed, but they can’t re-subscribe if they cancel the
subscription.

```
Greetings from AWS Marketplace,

This message is a notification detailing a recent change for <ProductName>.
{{{sellerName}}} has opted to restrict the <ProductType> product in <Restricted Region(s)> beginning <DateOfChange>.

This impacts you in the following ways:

1. As long as you're subscribed to the product, you can continue using the software product in the restricted Region.
2. You can't begin new instances of the software product in the restricted Region.
3. You can continue using the software product in all available AWS Regions.

Regards,
The AWS Marketplace Team

AWS, Inc. is a subsidiary of Amazon.com, Inc. Amazon.com (http://amazon.com/) is a registered
trademark of Amazon.com, Inc. This message was produced and distributed by Amazon Web
Services Inc., 410 Terry Ave. North, Seattle, WA 98109-5210.
```

## Update support for future

AWS Regions

If you want your product to be onboarded to newly launched AWS Regions, you can use
**Update future Region support**.

###### To update future Region support

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, and on the
   **Current server product** tab, select the product that you
   want to modify.
3. From the **Request changes** dropdown, choose
   **Update future Region support**.
4. You can choose to activate future Region support to allow AWS Marketplace to onboard
   your product to newly launched AWS Regions on your behalf.
5. After activating the feature, you can choose between all future Regions or
   limit to US Regions only.
6. Choose **Submit change request** to submit your request for
   review.
7. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status becomes **Succeeded**.

## Update availability by

country

If you want to change the countries in which your product can be subscribed to and
offered, you can use **Update availability**.

###### To update availability by country

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, on the
   **Current server product** tab, then select the product
   that you want to modify.
3. From the **Request changes** dropdown, choose
   **Update availability**.
4. Choose one of the following options:
   1. **All countries** – Available in all supported
      countries.
   2. **All countries with exclusions** – Available
      in all supported countries except in selected countries.
   3. **Custom list** – Specific list of countries
      where the product is available.

5. Choose **Submit change request** to submit your request for
   review.
6. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status becomes **Succeeded**.
