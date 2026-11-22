

# Creating an opportunity

You can create opportunities in AWS Partner Central in three ways. To create one, on the Opportunities page, choose **Create opportunity**, and then choose an option.
+ **Create using wizard** – Enter one opportunity in a multi-step form, and review every field before you submit. For steps, see [Create an opportunity using the wizard](#create-opportunity-procedure).
+ **Create using agent** – Describe the deal or upload a supporting document. The Partner Central agent asks for any missing details and creates the opportunity after you approve it. For steps, see [Create an opportunity using the agent](#partner-cosell-agent-create-opportunity).
+ **Create using a file** (formerly bulk create) – Create up to 500 opportunities at the same time from one CSV file. For steps, see [Creating and updating opportunities in bulk](bulk-actions.md).

You can also create and manage opportunities through a [CRM integration](https://docs.aws.amazon.com/partner-central/latest/crm/aws-partner-crm-integration.html). We encourage you to submit opportunities early in the sales cycle. The agent helps qualify and strengthen the opportunity as the deal progresses.

Opportunities can be classified as requiring AWS support or partners can choose to manage their opportunities independently. Opportunities progress through defined stages from Prospect to Launched/Closed and include data attributes such as revenue estimates, customer details and customer use case.

Partners can share opportunities with AWS sellers, which are routed through an internal validation process. Once an opportunity has been submitted, it undergoes validation to ensure it meets AWS criteria for deal size, solution alignment, and customer engagement status.

Partners can now use deal sizing when creating opportunities to receive AI-powered Monthly Recurring Revenue (MRR) forecasts and AWS product recommendations based on opportunity details. Partners can also import AWS Pricing Calculator URLs to automatically populate service selections and receive enhanced insights including Migration Acceleration Program (MAP) eligibility indicators and optimization recommendations. Partners who transact in total contract value (TCV) can submit TCV and contract duration, and deal sizing converts both to a forecasted MRR.

## Create an opportunity using the wizard
<a name="create-opportunity-procedure"></a>

1. Navigate to **Sell**, **Opportunities** in the left-side navigation.

1. Choose **Create opportunity**, and then choose **Create using wizard**.

1. Enter customer details and choose **Next**.
   + All fields are required except for **Customer DUNS**. Information such as the customer website and zip code are necessary to align the opportunity with internal stakeholders.
   + If you enter **Government** for **Industry Vertical**, make sure you select a **Classified National Security Information** option.

1. Enter project details and choose **Next**.
   + For **Customer business problem**, describe this customer's specific pain, what is forcing them to act now, and the outcome they expect. Avoid generic descriptions that could apply to any customer.
   + Select the most accurate **Use Case** and **Industry Vertical** rather than leaving them as **Other**, so AWS can route the opportunity correctly.
   + Select **Co-Sell with AWS** if you want AWS Sales support. If you select **Co-Sell with AWS**, make sure you choose one or more **Partner specific needs from AWS for Co-Sell** options.
   + For **Opportunity Type**, if there are existing contracts between the end customer and partner with the potential for incremental revenue, choose **Expansion**. Choose **Flat Renewal** if no potential for incremental revenue exists. If you select **Expansion** or **Flat Renewal**, you can enter an optional parent opportunity ID.
   + AWS Training Partners (ATPs) should enter **Training** for **Use Case**, and enter AWS revenue from AWS training kits for **Estimated AWS Monthly Recurring Revenue** on the next step as part of deal sizing.
   + Enter a future date for **Target Close Date**. Do not submit opportunities with **Launched** or **Closed Won** status.
   + In the **AWS Marketplace products and solutions** section, associate one or more of your solutions and/or one or more AWS Marketplace products to the opportunity. To associate solutions or AWS Marketplace products from an AWS Account connected via [Subsidiary account connection](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html), enter the corresponding ARNs in the **Enter solution ARNs manually** or **Enter AWS Marketplace product ARNs manually** fields.
**Note**  
You are required to associate at least one solution or AWS Marketplace product to create an opportunity. Only solutions in "Limited" or "Public" status can be associated to an Opportunity.
   + If you select **Yes: Sourced from marketing activity**, make sure you select **Yes** or **No** for **Marketing development funds**.

1. Enter APN program details and choose **Next**.

   Select the **APN program** related to this opportunity. Some APN programs may require additional details and adding contact details.

   If you select **Migration Acceleration Program**, you can provide additional details about your migration project.
   + Select **Migration workload** you plan to migrate.
   + Select **Migration source** as the platform or environment where your workload currently resides.
   + Select **Migration phase** as your current stage in the migration journey: **Assess, Mobilize, Migrate & Modernize, and Manage**.
   + Select **Managed services offered to customer** as **Yes**, if you plan to help the customer manage workloads by offering managed services after the project is delivered. Select **No**, if you do not plan to offer managed services to the customer after the project is delivered.
   + Enter **Migration details** about your migration project, including: current environment specifications, business drivers for migration, expected outcomes, and key challenges or requirements etc.

1. Configure deal size and choose **Next**.

   Deal sizing provides AI-powered insights to help you estimate opportunity value and identify relevant AWS products. You can choose between two calculation methods based on your preference and available information.

   Choose your MRR calculation method:
   + **Forecast MRR from TCV** – Enter your total contract value (TCV) and contract duration in months, and deal sizing converts both to a forecasted MRR. This method serves partners who estimate deals in TCV, such as multi-year SaaS contracts or software licensing.
   + **Manual entry with AI insights** – View AI-forecasted MRR estimates and AWS product recommendations based on your opportunity details, then enter your own MRR estimate. This method allows you to review AI forecasts while maintaining control over the final estimate.
   + **Pricing Calculator URL** – Import an AWS Pricing Calculator URL to automatically populate MRR and product selections. This method provides enhanced insights including MAP eligibility indicators, optimization recommendations, and potential cost savings analysis.

    

   **Using Forecast MRR from TCV**

   When you select Forecast MRR from TCV, you submit the total contract value of the deal and the model returns a forecasted MRR.

   1. Enter TCV and contract duration:
      + Enter the **Total contract value** in USD or EUR. The value must be greater than zero.
      + Enter the **Contract duration** in months. Supported range is 1 to 144 months.
      + Both fields are required. The system returns a validation error if you submit one without the other.

   1. Review the forecasted MRR:
      + The model converts TCV and contract duration to a forecasted MRR within 10 seconds and populates the MRR field.
      + The forecasted MRR is read-only on this method. To enter your own MRR, switch the calculation method to Manual entry with AI insights or Pricing Calculator URL. Switching methods clears the TCV and contract duration values.
      + The forecasted MRR carries the disclaimer: "Forecasted MRR is an estimate for planning purposes only and does not represent actual revenue, quota retirement, or any financial commitment."

   1. Modify your estimate:
      + To update the forecasted MRR, change the TCV value or contract duration. The model recalculates and updates the MRR field.
      + Forecast MRR from TCV and Pricing Calculator URL are mutually exclusive on the same opportunity. To switch, change the calculation method.

    

   **Using Manual entry with AI insights**

   When you select Manual entry with AI insights, the system analyzes your opportunity details to provide recommendations.
**Note**  
AI-forecasted MRR and product recommendations are available for opportunities in Prospect, Qualified, Technical Validation, and Business Validation stages. These features are not available for opportunities in Committed, Launched, or Closed Lost stages.

   1. **AI-forecasted MRR:**
      + We provide an estimate of the median monthly recurring revenue (MRR) based on your past AWS opportunities and current opportunity details, including the Customer business problem field.
      + Review the AI-forecasted MRR using your judgment and knowledge of the opportunity to assess its accuracy independently. Update the estimate as you gather more information about the deal and progress through the sales cycle.

   1. **AWS product recommendations:**

      AWS products with a purple badge are AI-recommended based on your Customer business problem and opportunity details. We analyze your customer's technical requirements and typical use cases.

      Review these suggestions and customize the product selection to match your customer's specific needs.

      **To refine your selection:**
      + Search for and add additional AWS products to associate with your opportunity.
      + Uncheck products in the AWS products table.
      + Remove products from the Selected AWS products list.

    

   **Using Pricing Calculator URL**

   When you select Pricing Calculator URL, you can import estimates directly from the AWS Pricing Calculator.

   1. **Import your Pricing Calculator URL:**
      + Copy the share URL from your AWS Pricing Calculator estimate.
      + Paste the URL into the **Estimate URL** field.
      + Choose **Calculate MRR** to import the estimate.
      + The **Total MRR** automatically populates based on the imported calculation.

   1. **Review URL-imported products:**
      + All products from your Pricing Calculator estimate are automatically included in your opportunity.
      + The products table displays detailed information for each imported product, including MRR amount, optimized spend, potential savings, and recommendations.
      + Review potential savings calculations to quantify cost optimization opportunities.
      + Review optimization recommendations to understand how to improve cost efficiency. Recommendations appear in the **Recommendation** column with specific guidance such as "Use Reserved Instances or Savings Plans."
      + Review MAP eligibility indicators to identify products that qualify for Migration Acceleration Program funding. Eligible products display an "Eligible" status in the **MAP eligible** column.
      + Modernization options display an "Eligible" status in the **Modernization** column.

   1. **Modify your estimate:**
      + To modify products or pricing after importing, you must update your Pricing Calculator estimate URL and reimport.

1. Enter optional details as desired and choose **Next**.

1. Enter optional customer contact details and choose **Next**. For more information, refer to [Opportunity contacts](contact-roles.md).

1. Review the opportunity details and choose **Submit**.

You can add up to two partner contacts to an opportunity. These contacts are your primary points of communication with AWS sellers. For who receives notifications about the opportunity, see [Managing opportunity notifications](managing-notifications.md).

Once the opportunity is accepted by AWS, partners can collaborate with assigned AWS sellers, access deal support resources, and receive guidance on technical validation and pricing assistance. See more details in the [Accepting opportunities](accepting-opportunities.md) section.

Partners can utilize the natural-language search and filter capabilities to easily sort and find specific opportunities in both the **Opportunities** and **Opportunity invitations** tabs.

Once the opportunity is submitted, an Opportunity Quality score and a co-sell motion are automatically assigned. For details, see [Agentic Co-sell engagement](co-sell-engagement.md).

**Note**  
See IAM guide for help with Access.

## Create an opportunity using the agent
<a name="partner-cosell-agent-create-opportunity"></a>

The agent creates new opportunities through a short conversation instead of completing a multi-step form, which reduces data entry and lets partner sales teams spend more time selling.

The agent also guides you to a high-quality submission. It asks for the details that the Opportunity Quality Score measures, based on the co-selling best practices. These details include the customer's business problem, dated next steps, the Partner Primary Need from AWS, and the AWS services the customer will adopt. For more information, see [Opportunity Quality score](co-sell-engagement.md#opportunity-quality-score) and [Best practices](co-sell-engagement.md#cosell-best-practices).

**To create an opportunity**

1. On the Opportunities listing page, choose **Create using agent** from the **Create opportunity** dropdown.

1. In the conversational panel, describe the deal in natural language or upload a supporting document such as meeting notes, a proposal, or a call transcript (PDF, DOCX, XLSX, TXT).

1. Answer the agent's questions about any missing details. Then review the fields the agent extracted and enriched, and confirm or correct the values.

1. Approve the draft. The agent creates the opportunity, submits it for AWS review, and returns the Opportunity ID with a status of *Pending Approval*.

To create an opportunity from an existing one, use agents to clone the opportunity.

You can also ask the agent to create many opportunities at the same time from one file. Upload the file in the chat. The agent checks the file format and template columns, and then submits the job after you approve it. The file supports up to 500 opportunities. For the full workflow, see [Create opportunities with the agent](bulk-actions.md#bulk-create-with-agent).

**Note**  
At launch, the agent supports bulk create only. To update opportunities in bulk, see [Update opportunities in bulk](bulk-actions.md#update-opportunities-bulk).

## Additional opportunity fields
<a name="opportunity-additional-fields"></a>

The following fields are available when you create an opportunity. The same rules apply in the wizard, with the agent, and in a bulk file. For every field, with its format and allowed values, see [Opportunity template field reference](bulk-actions.md#opportunity-fields).


| Field | What it's for | Rules | 
| --- | --- | --- | 
| Next steps | The next steps in the engagement. | Up to 255 characters. Applies when the partner primary need is a Co-Sell option. | 
| AWS Marketplace products | The AWS Marketplace products to associate with the opportunity. | Enter the full AWS Marketplace product ARN. In a bulk file, separate multiple ARNs with a semicolon (;). | 
| AWS Marketplace solutions | The AWS Marketplace solutions to associate with the opportunity. | Enter the full AWS Marketplace solution ARN. In a bulk file, separate multiple ARNs with a semicolon (;). | 
| APN programs | The APN program related to the opportunity. | Choose a program from the allowed list. Some programs need more details. | 
| AWS Pricing Calculator estimate | Public AWS Pricing Calculator links that size the opportunity. | Use public, shareable links. In a bulk file, separate multiple links with a comma (,). | 
| AWS partition | The AWS partition for the opportunity, for example the AWS European Sovereign Cloud. | Choose aws-eusc, or leave it blank for the standard AWS partition. | 
| Partner account manager | The partner account manager for the opportunity, one of the two partner contacts. | First name and last name, up to 80 characters each. One valid email address. Phone number in international format, starting with \+. | 
| Opportunity owner | The partner employee who owns the opportunity, the other partner contact. | First name and last name, up to 80 characters each. One valid email address. Phone number in international format, starting with \+. | 

To set the AWS partition in the console, see [Tagging AWS partition for opportunities](esc-aws-partition.md).