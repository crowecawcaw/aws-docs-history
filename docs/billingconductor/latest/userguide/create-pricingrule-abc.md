# Creating pricing rules

Use the following steps to create a pricing rule.

###### To create a pricing rule

1. Open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, choose **Pricing configuration**.
3. Choose the **Pricing rules** tab.
4. Choose **Create pricing rules**.
5. For **Pricing rule details**, enter the name of the pricing rule. For naming restrictions, see [Quotas and restrictions](limits.md "limits.md").
6. (Optional) For **Description**, enter a description for the pricing rule.
7. For **Scope**, choose `Global`, `Service`, `Billing entity`, or `SKU`.
   - Global - applies to all usage.
   - Service - only applies to a given service. When choosing service, choose a service code to configure the pricing rates for. When you choose a service, choose the service code from the Price List Query API that you want to adjust.
   - Billing entity - only applies to a given billing entity. A billing entity is the seller of services provided by AWS, their affiliates, or third-party providers selling services through AWS Marketplace.
   - SKU - only applies to the unique combination of service (product) code, usage type, and/or operation.

8. For **Type**, choose **Discount**, **Markup**, or **Tiering**.

###### Note

**Tiering** is only available for global and service-scoped pricing rules. 9. For **Percentage**, enter the percentage amount.

If you enter `0` as the percentage, the pricing plan defaults to the
AWS On-Demand rate. If you enter a decimal value, it will be rounded to the nearest 2 decimal
places.

###### Note

The percentage displays on the member account's bills page. For example, `EC2 t3.micro on-demand (+20%)`. 10. For the **Tiering** type, you can check the box under **Tiering configuration** to deactivate Always Free Tier, or leave as activated. Always Free Tier will be activated unless it's explicitly deactivated. 11. (Optional) To create another pricing rule in the same workflow, choose **Add pricing
rule**. 12. Choose **Create pricing rule**.
