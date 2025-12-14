**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Creating a Shield Advanced protection group

###### To create a protection group

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").
2. In the AWS Shield navigation pane, choose **Protected resources**.
3. Choose the **Protection groups** tab, then choose **Create
   protection group**.
4. In the **Create protection group** page, provide a name for your group. You'll use this name to identify the group in your list of protected resources. You can't change the name of a protection group after you create it.
5. For **Protection grouping criteria**, select the criteria
   that you want Shield Advanced to use to identify the protected resources to include in
   the group. Make your additional selections based on the criteria that you've
   chosen.
6. For **Aggregation**, select how you want Shield Advanced to combine resource
   data for the group in order to detect, mitigate, and report events.
   - **Sum** – Use the total traffic across the group.
     This is a good choice for most cases. Examples include Elastic IP
     addresses for Amazon EC2 instances that scale manually or automatically.
   - **Mean** – Use the average of the traffic
     across the group. This is a good choice for resources that share traffic
     uniformly. Examples include accelerators and load balancers.
   - **Max** – Use the highest traffic from each
     resource. This is useful for resources that don't share traffic, and for
     resources that share traffic in a non-uniform way. Examples include
     Amazon CloudFront distributions and origin resources for CloudFront distributions.

7. Choose **Save** to save your protection group and return to
   the **Protected resources** page.
   In the **Shield**
   **Events** page, you can view events for your protection group and
   drill down to see additional information for the protected resources that are in the
   group.
