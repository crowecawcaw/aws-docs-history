# AWS Service Catalog Tag Update Constraints

###### Note

AWS Service Catalog does not support tag update constraints for Terraform Open Source products.

With tag update constraints, AWS Service Catalog administrators can allow or disallow end users to update
tags on resources associated with a provisioned product. If tag updating is allowed, then new tags associated with
the product or portfolio will be applied to provisioned resources during a
provisioned product update.

###### To enable tag updates to a product

1. Open the Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").
2. Choose the portfolio that contains the product you want to update.
3. Choose the **Constraints** tab and choose **Add constraints**.
4. Under **Constraint type**, choose **Tag Update**.
5. Choose the product from **Product**, then choose **Continue**.
6. On the **Tag Updates page**, select **Enable Tag Updates**.
7. Choose **Submit**.
