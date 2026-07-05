# Creating an opportunity

Opportunities can be added individually, by [bulk import](bulk-actions.md "bulk-actions.md") or managed through a [CRM integration](../crm/aws-partner-crm-integration.md "../crm/aws-partner-crm-integration.md"). We encourage AWS Partners to submit opportunities early in the sales cycle and let the agent help qualify and strengthen the opportunity as the deal progresses.

Opportunities can be classified as requiring AWS support or partners can choose to manage their opportunities independently. Opportunities progress through defined stages from Prospect to Launched/Closed and include data attributes such as revenue estimates, customer details and customer use case.

Partners can also create opportunities through a short conversation with the AWS Partner Central agent. Describe the deal or upload a supporting document, and the agent extracts the fields, enriches customer details, and creates the opportunity after you approve. For details, see [Agents for opportunity management](partner-cosell-agent.md "partner-cosell-agent.md").

Partners can share opportunities with AWS sellers, which are routed through an internal validation process. Once an opportunity has been submitted, it undergoes validation to ensure it meets AWS criteria for deal size, solution alignment, and customer engagement status.

Partners can now use deal sizing when creating opportunities to receive AI-powered Monthly Recurring Revenue (MRR) forecasts and AWS product recommendations based on opportunity details. Partners can also import AWS Pricing Calculator URLs to automatically populate service selections and receive enhanced insights including Migration Acceleration Program (MAP) eligibility indicators and optimization recommendations. Partners who transact in total contract value (TCV) can submit TCV and contract duration, and deal sizing converts both to a forecasted MRR.

## Create an opportunity

1. Navigate to **Sell**, **Opportunities** in the left-side navigation.
2. Choose **Create opportunity**, then select one of the following options from the dropdown:

   - **Create using wizard** – Continue with the multi-step form described in the steps below.
   - **Create using agent** – Create the opportunity through a short conversation with the AWS Partner Central agent. Describe the deal or upload a supporting document, review the fields the agent extracts, and approve to submit. For details, see [Agents for opportunity management](partner-cosell-agent.md "partner-cosell-agent.md").

3. Enter customer details and choose **Next**.

   - All fields are required except for **Customer DUNS**. Information such as the customer website and zip code are necessary to align the opportunity with internal stakeholders.
   - If you enter **Government** for **Industry Vertical**, make sure you select a **Classified National Security Information** option.

4. Enter project details and choose **Next**.

   - For **Customer business problem**, describe this customer's specific pain, what is forcing them to act now, and the outcome they expect. Avoid generic descriptions that could apply to any customer.
   - Select the most accurate **Use Case** and **Industry Vertical** rather than leaving them as **Other**, so AWS can route the opportunity correctly.
   - Select **Co-Sell with AWS** if you want AWS Sales support. If you select **Co-Sell with AWS**, make sure you choose one or more **Partner specific needs from AWS for Co-Sell** options.
   - For **Opportunity Type**, if there are existing contracts between the end customer and partner with the potential for incremental revenue, choose **Expansion**. Choose **Flat Renewal** if no potential for incremental revenue exists. If you select **Expansion** or **Flat Renewal**, you can enter an optional parent opportunity ID.
   - AWS Training Partners (ATPs) should enter **Training** for **Use Case**, and enter AWS revenue from AWS training kits for **Estimated AWS Monthly Recurring Revenue** on the next step as part of deal sizing.
   - Enter a future date for **Target Close Date**. Do not submit opportunities with **Launched** or **Closed Won** status.
   - In the **AWS Marketplace products and solutions** section, associate one or more of your solutions and/or one or more AWS Marketplace products to the opportunity.
     To associate solutions or AWS Marketplace products from an AWS Account connected via
     [Subsidiary account connection](../getting-started/account-linking.md "../getting-started/account-linking.md"), enter the corresponding ARNs in the **Enter solution ARNs manually** or **Enter AWS Marketplace product ARNs manually** fields.

   ###### Note

   You are required to associate at least one solution or AWS Marketplace product to create an opportunity. Only solutions in "Limited" or "Public" status can be associated to an Opportunity.
   - If you select **Yes: Sourced from marketing activity**, make sure you select **Yes** or **No** for **Marketing development funds**.

5. Enter APN program details and choose **Next**.

Select the **APN program** related to this opportunity. Some APN programs may require additional details and adding contact details.

If you select **Migration Acceleration Program**, you can provide additional details about your migration project.

    * Select **Migration workload** you plan to migrate.
    * Select **Migration source** as the platform or environment where your workload currently resides.
    * Select **Migration phase** as your current stage in the migration journey: **Assess, Mobilize, Migrate & Modernize, and Manage**.
    * Select **Managed services offered to customer** as **Yes**, if you plan to help the customer manage workloads by offering managed services after the project is delivered. Select **No**, if you do not plan to offer managed services to the customer after the project is delivered.
    * Enter **Migration details** about your migration project, including: current environment specifications, business drivers for migration, expected outcomes, and key challenges or requirements etc.

6. Configure deal size and choose **Next**.

Deal sizing provides AI-powered insights to help you estimate opportunity value and identify relevant AWS products. You can choose between two calculation methods based on your preference and available information.

Choose your MRR calculation method:

    * **Forecast MRR from TCV** – Enter your total contract value (TCV) and contract duration in months, and deal sizing converts both to a forecasted MRR. This method serves partners who estimate deals in TCV, such as multi-year SaaS contracts or software licensing.
    * **Manual entry with AI insights** – View AI-forecasted MRR estimates and AWS product recommendations based on your opportunity details, then enter your own MRR estimate. This method allows you to review AI forecasts while maintaining control over the final estimate.
    * **Pricing Calculator URL** – Import an AWS Pricing Calculator URL to automatically populate MRR and product selections. This method provides enhanced insights including MAP eligibility indicators, optimization recommendations, and potential cost savings analysis.

**Using Forecast MRR from TCV**

When you select Forecast MRR from TCV, you submit the total contract value of the deal and the model returns a forecasted MRR.

    1. Enter TCV and contract duration:




    	* Enter the **Total contract value** in USD or EUR. The value must be greater than zero.
    	* Enter the **Contract duration** in months. Supported range is 1 to 144 months.
    	* Both fields are required. The system returns a validation error if you submit one without the other.
    2. Review the forecasted MRR:




    	* The model converts TCV and contract duration to a forecasted MRR within 10 seconds and populates the MRR field.
    	* The forecasted MRR is read-only on this method. To enter your own MRR, switch the calculation method to Manual entry with AI insights or Pricing Calculator URL. Switching methods clears the TCV and contract duration values.
    	* The forecasted MRR carries the disclaimer: "Forecasted MRR is an estimate for planning purposes only and does not represent actual revenue, quota retirement, or any financial commitment."
    3. Modify your estimate:




    	* To update the forecasted MRR, change the TCV value or contract duration. The model recalculates and updates the MRR field.
    	* Forecast MRR from TCV and Pricing Calculator URL are mutually exclusive on the same opportunity. To switch, change the calculation method.

**Using Manual entry with AI insights**

When you select Manual entry with AI insights, the system analyzes your opportunity details to provide recommendations.

###### Note

AI-forecasted MRR and product recommendations are available for opportunities in Prospect, Qualified, Technical Validation, and Business Validation stages. These features are not available for opportunities in Committed, Launched, or Closed Lost stages.

    1. **AI-forecasted MRR:**




    	* We provide an estimate of the median monthly recurring revenue (MRR) based on your past AWS opportunities and current opportunity details, including the Customer business problem field.
    	* Review the AI-forecasted MRR using your judgment and knowledge of the opportunity to assess its accuracy independently. Update the estimate as you gather more information about the deal and progress through the sales cycle.
    2. **AWS product recommendations:**


    AWS products with a purple badge are AI-recommended based on your Customer business problem and opportunity details. We analyze your customer's technical requirements and typical use cases.


    Review these suggestions and customize the product selection to match your customer's specific needs.


    **To refine your selection:**




    	* Search for and add additional AWS products to associate with your opportunity.
    	* Uncheck products in the AWS products table.
    	* Remove products from the Selected AWS products list.

**Using Pricing Calculator URL**

When you select Pricing Calculator URL, you can import estimates directly from the AWS Pricing Calculator.

    1. **Import your Pricing Calculator URL:**




    	* Copy the share URL from your AWS Pricing Calculator estimate.
    	* Paste the URL into the **Estimate URL** field.
    	* Choose **Calculate MRR** to import the estimate.
    	* The **Total MRR** automatically populates based on the imported calculation.
    2. **Review URL-imported products:**




    	* All products from your Pricing Calculator estimate are automatically included in your opportunity.
    	* The products table displays detailed information for each imported product, including MRR amount, optimized spend, potential savings, and recommendations.
    	* Review potential savings calculations to quantify cost optimization opportunities.
    	* Review optimization recommendations to understand how to improve cost efficiency. Recommendations appear in the **Recommendation** column with specific guidance such as "Use Reserved Instances or Savings Plans."
    	* Review MAP eligibility indicators to identify products that qualify for Migration Acceleration Program funding. Eligible products display an "Eligible" status in the **MAP eligible** column.
    	* Modernization options display an "Eligible" status in the **Modernization** column.
    3. **Modify your estimate:**




    	* To modify products or pricing after importing, you must update your Pricing Calculator estimate URL and reimport.

7. Enter optional details as desired and choose **Next**. 8. Enter optional customer contact details and choose **Next**. For more information, refer to [Opportunity contacts](contact-roles.md "contact-roles.md"). 9. Review the opportunity details and choose **Submit**.

Partners can add up to two (2) partner contacts on a given opportunity. These designated contacts serve as the primary points of communication with AWS sellers and receive all relevant notifications about the opportunity's progression. This includes automated alerts for status changes, requests for additional information, and validation updates.

Once the opportunity is accepted by AWS, partners can collaborate with assigned AWS sellers, access deal support resources, and receive guidance on technical validation and pricing assistance. See more details in the [Accepting opportunities](accepting-opportunities.md "accepting-opportunities.md") section.

Partners can utilize the natural-language search and filter capabilities to easily sort and find specific opportunities in both the **Opportunities** and **Opportunity invitations** tabs.

Once the opportunity is submitted, an Opportunity Quality score and a co-sell motion are automatically assigned. For details, see [Co-sell engagement](co-sell-engagement.md "co-sell-engagement.md").

###### Note

See IAM guide for help with Access.
