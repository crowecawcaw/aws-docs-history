# Partner Analytics and Seller Insights Frequently Asked Questions (FAQs)

Review the below FAQs for answers to common questions.

## General FAQs

### 'No Data' is displayed on any of the KPIs, how do I fix this issue?

Please select the reset button (circular arrow). Note, this is different from the refresh button on the web browser page.

### I see there are data discrepancies? What do I do?

File a ticket with APN Support to resolve discrepancies. From the left navigation panel, choose [AWS Partner Central support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support") to file a ticket.

### Why doesn't the Partner Scorecard data match what is shown in Partner Analytics dashboard data?

Data discrepancies between Partner Analytics and the Partner Scorecard stem from several key differences in measurement methodologies and scope. The Scorecard's measurement period aligns with the organization's last tier review date, creating potential mismatches when date filters differ. Additionally, the Scorecard maintains broader inclusivity by counting all opportunities where partners are tagged in AWS internal systems, regardless of entry status. Training and Certification data variations occur as the Partner Scorecard specifically tracks progress within selected Partner Paths, focusing on Unique Individuals with Foundational, Technical Certifications, and Business/Technical Accreditations. Partner Analytics provides expanded functionality through comprehensive achievement tracking, including Total achievement counts via Type filtering, Level-based certification aggregation rather than technical definitions, and inclusion of non-APN Tier requirement credentials including the AWS Partner: Cloud Economics accreditation, which remains absent from the Partner Scorecard.

## Opportunities dashboard FAQs

### Why does the Opportunity Win Rate visual show a different count of Launched and Closed Lost opportunities (and a different Win Rate) than the count displayed on the Opportunities Analysis bar chart split by Stage?

Opportunity win rate metrics are calculated based on the Close Date of opportunities (date an opportunity launches or becomes Closed Lost) and so includes all opportunities closed within the selected timeframe, regardless of when they were submitted. The Opportunities Analysis bar chart is filtered by the opportunity Submitted date (close dates do not exist for opportunities still open), so the Launched and Closed Lost opportunity counts shown in the Opportunities Analysis only include opportunities submitted within the selected timeframe.

### Why does the Partner Referrals Approval Rate visual show a different count of Approved and Rejected opportunities than the count displayed on the Opportunities Analysis donut chart split by Status?

Partner Referrals Approval Rate metrics are calculated based on the date opportunities are approved/rejected and so includes all opportunities approved within the selected timeframe, regardless of when they were submitted. The Opportunities Analysis bar chart is filtered by the opportunity submitted date, so Approved and Rejected opportunity counts shown in the Opportunities Analysis only include opportunities summitted within the selected timeframe.

### Why are Stage and AWS Stage values different for some opportunities?

AWS Stage reflects AWS record keeping in the AWS Seller CRM, while the overall Stage value reflects the opportunity stage in the ACE Opportunities Page. If these two values are different for an opportunity Closed at least 48 hours earlier, please reach out to the AWS Partner Development team to resolve any operational/record-keeping discrepancies. For Open opportunities, some difference in status recording may be expected due to different systems being updated at different times with manual input.

## AWS Co-sell recommendation score FAQs

### How do I see AWS Co-Sell Recommendation Scores on Partner Analytics?

This feature is currently available to ACE-Eligible Partners in AWS Specialization programs.

### How does the recommendation logic work?

The recommendation logic is powered by machine learning that is trained on partner capabilities using a predictive model that evaluates these attributes to assess the best-fit partners by geography, industry, size, and capability. The recommendation score assesses the likelihood of success in engaging with AWS for co-sell.

### What do I need to do to receive a higher score?

For Services path partners, the key is providing high-quality, detailed information in the opportunity record. Ensure that the entire pipeline in ACE and that opportunity details are up to date. Opportunity hygiene should include opportunity details: opportunity title should include a summary of the project [customer name, workload, delivery], a detailed description of the customer use case (a few short sentences are better than lengthy filler), business outcome includes desired end result of the AWS Customer, include next steps and update this as more information is acquired, true estimated or exact opportunity value. Ensure that any relevant AWS services used to deliver the opportunity are listed in the opportunity text fields (e.g., Description) and provide quality over quantity of information.

For Software path partners, Marketplace Solution Listings are used within the algorithm, so ensure hygiene of the solution listing and up to date information. Attach a solution listing to ACE opportunities (link the marketplace listing to any relevant opportunities) and try to process deals through Marketplace for higher recommendations.

### How does AWS Marketplace influence my recommendations?

For Software path partners, a public AWS Marketplace listing is a necessary condition to be evaluated by the model. The model uses the product category, product description, and current customer deployments to evaluate where the listing can meet AWS customer needs. The more data we can gather with the listing and customer activity, the more likely the listings will be recommended.

### How does the model evaluate my capabilities? What do I need to focus on?

For Services path partners, the model uses the following fields from the opportunity record: Title, Description, Details, Need, Next Step, and Value. The model can also derive capabilities based on AWS Product tags. To evaluate where partners are well-suited for co-selling, the model inspects open AWS customer opportunities and predicted customer use cases, to find partners that have demonstrated success with similar customers.

For example, the model currently runs upon all open AWS Originated (AO) opportunities. For each given customer account and opportunity, the model predicts the partner based on their past success delivering with similar customers and use cases. Where available, the model will return to partners that have done work in the same region, segment, and/or industry.

### How do Service Validations, Competencies, and Programs affect my recommendation score?

AWS Co-Sell Recommendation Scores are provided as a benefit for ACE Eligible and AWS Specializations partners. Service Validations and AWS Competencies with corresponding ACE launches provide the model with confidence about partners' capabilities. The model also use validated case studies, either to improve recommendation relevance or to provide additional explanation for why a recommendation was made. This means that partners with validated and published case studies can potentially see shifts in their recommendation scores.

### What if the wrong use case was tagged to my opportunity?

An update can be made to open opportunities only, per [ACE guidelines](https://partnercentral.awspartner.com/partnercentral2/s/article?category=ACE_Get_Started&article=Introduction-to-the-ACE-Pipeline-Manager "https://partnercentral.awspartner.com/partnercentral2/s/article?category=ACE_Get_Started&article=Introduction-to-the-ACE-Pipeline-Manager"). The machine learning model is re-trained weekly to capture new data on launched opportunities and marketplace offers. Ensure that the information is accurate before moving the PO or AO to "Launched" state.

### Should I submit more opportunities, including for-visibility-only (FVO) with no co-sell support?

Yes. The model is enriched as partners share more data about their capabilities.

### How does win rate, deal size, and solution data impact recommendations?

A minimum of one high quality launched deal (Partner Originated or AWS Originated) is required by the model. Additional high quality opportunity submissions (or referrals) will strengthen the connection between customers, their needs, and capabilities. Follow the guidelines outlined earlier in this doc to maximize data quality.

### I am ACE-Eligible and AWS Specialized, but only see "Low" or no scores?

For Software Path Partners:

1. Have at least 1 Marketplace listing in any category, except for ProServe, and
2. Have lifetime EC2+GSS (private offers or public subscriptions) over $100, and

For Services Path Partners:

1. Include relevant AWS Product tags and/or keywords in the description
2. Submit more opportunities in areas that are specialized.

If a score still doesn't populate, it is also possible that we have not identified current / potential customer use cases that match the partner's capabilities.

### I am ACE eligible and have submitted 100's of POs but received no AWS Co-Sell Recommendation Score. Why?

Data quality supersedes quantity in all documentation processes. Strict adherence to established guidelines ensures optimal system performance through accurate customer problem documentation and precise AWS service implementation details. Critical documentation parameters must include specific technical solutions, deployed AWS services in designated fields, and accurate opportunity valuations. When addressing specialized customer challenges, detailed documentation of technical implementations and solution architectures enables the AWS Co-Sell Recommendation Score to establish precise connections between solutions and future opportunities.

### As a Software partner, do I need a public AWS Marketplace listing to be included in the model?

Yes and No. AWS Marketplace Listings is currently the primary source used by the model to evaluate Software path partner capabilities. The model supplements this data with ACE opportunity launches for Software partners.

### As a Services partner, do I need a public listing on Marketplace to be recommended?

Not currently.

## AWS Marketplace Engagement Score FAQs

### What is the AWS Marketplace solution engagement score?

The AWS Marketplace solution engagement score predicts a customer's likelihood to purchase a solution from a partner. The output of the model is a probability that demonstrates the likelihood for the customer to need a solution from the partner. These probabilities are transformed into HIGH / MEDIUM / LOW / "-" groupings.

### How do I act on the AWS Marketplace Engagement Score?

AWS Marketplace streamlines procurement and onboarding processes, creating significant value for customer purchasing workflows. The AWS Marketplace Engagement Score serves as a prioritization tool for identifying opportunities aligned with marketplace procurement preferences. While the score provides directional insights, it does not guarantee transaction outcomes through AWS Marketplace. Optimization of co-sell opportunities requires direct engagement with the AWS Partner Development team for strategic prioritization and execution planning. The scoring mechanism functions as one component within a comprehensive evaluation framework, supporting data-driven decision-making while acknowledging the dynamic nature of customer purchasing behaviors and preferences.

### Many of my opportunities show "-" for the AWS Marketplace Engagement Score?

The "-" value indicates that AWS was either 1) Unable to determine the AWS Marketplace Engagement Score for that opportunity based on currently available information; or 2) Unable to assign an AWS Marketplace Engagement Score, as it is not applicable for that opportunity. This flag is only available for partners registered on the AWS Marketplace, as it covers AWS Marketplace listings.

### I am listed on AWS Marketplace, but I do not see AWS Marketplace Engagement Scores for my opportunities?

First ensure that the Display AWS Marketplace Engagement Score filter is set to Yes in the Opportunities Summary Data table in the Opportunities dashboard of Partner Insights. If there is an issue still, reach out to APN Support for help resolving this issue.

### What does HIGH/MEDIUM/LOW mean?

High means a customer's likelihood of purchasing a solution rank among the top cohort in comparison with all other customers. Medium means a customer's likelihood of purchasing a solution rank in the middle of the cohort in comparison with all other customers. Low means a customer's likelihood of purchasing a solution rank below the median in comparison with other customers.

### Does AWS Marketplace solution engagement score surface for all partners and opportunities?

No. AWS Marketplace solution engagement scores like Marketplace engagement scores are only relevant to independent software vendors (ISV) or Software path partners with Marketplace listings.

### What is the difference between AWS Marketplace engagement and AWS Marketplace solution engagement?

AWS Marketplace engagement score predicts a customer's likelihood to purchase through the AWS Marketplace. The AWS Marketplace solution engagement score is a score that predicts a customer's likelihood to purchase a solution from the partner's solution listing. One is about the procurement channel, and the other is about solution procurement.

### How frequently are AWS Marketplace solution engagement scores updated?

Monthly.

### Why do I see different scores on each opportunity? Why does the Marketplace engagement score not match the AWS Marketplace solution engagement score?

While a customer may have a high likelihood to make a purchase through the AWS Marketplace, this does not mean a customer has a high likelihood to purchase a partner solution and vice versa.

### Does a higher Solution engagement score mean that a customer is already using this solution through similar services or my competitors?

No. The Solution engagement score protects customer confidentiality and partner data. The score reflects a comparative ranking relative to other customers. A HIGH score indicates the customer's potential alignment with the solution, not their current service usage with AWS or other providers.

### Can I see the score for both AWS originated and Partner originated opportunities?

Yes, Technology partners can view the AWS Marketplace solution engagement score for both AWS originated (AO) and Partner originated (PO) opportunities.

### Does a higher score mean that a customer has an EDP, purchased from AWS Marketplace already or has a higher spend on AWS?

No, The Solution engagement score is derived in a way to protect customer confidentiality. A HIGH score indicates the customer's potential alignment with the solution, not their confidential enterprise agreement, current service usage with AWS, or other providers.

## Marketing Campaigns FAQs

### I see more campaigns on the donut charts for Leads shared by campaign, Opportunities by campaign, ARR by campaign than the total active campaigns?

The donut chart of Leads shared by campaign shows all the leads shared with the filtered time period and the contributing campaigns can be from the same time period and prior. For example, when filtering on 2023YTD, a portion of leads shared within 2023YTD can be from campaigns run in 2022. Same reason applies to Opportunities by campaign and ARR by campaign donut charts.

### Why are some identically-named metrics in the Marketing Campaigns dashboard showing different values from metrics with the same name in other dashboards?

Metrics in the Marketing Campaigns only show data associated with AWS-led marketing campaigns, so values indicated may only be a subset of the same metrics shown in other dashboards. For example, opportunity counts in the Marketing Campaigns only show opportunities generated from AWS-led marketing campaigns, while the Opportunities dashboard will show all of the ACE opportunities.

## Training and Certifications FAQs

### Our records of certified, accredited, and/or trained individuals do not match what is shown in the Training and Certifications dashboard?

The Training and Certifications dashboard only includes data for individuals that have either 1) Achieved/completed the Certification, Accreditation or Training using a company email address whose domain is listed in their companies domains in the Training and Certification tab of AWS Partner Central Settings; or 2) Have associated the personal email address they used to achieve or complete the Certification in the AWS Training and Certification badges section of their Profile in Skill Builder. Which email they use and associated actions must be selected or taken by the individual and cannot be completed by AWS or someone else in the organization. Training and Certification totals will change if users merge company email-based profiles with other profiles or if they associate their personal email with a different employer.

### AWS Partner Central PII Certifications table does not match what is shown in the Training and Certifications dashboard?

The Personal Identifiable Information (PII) certification table in AWS Partner Central is updated through a different process because of its inclusion of PII information. The cadence of this process could cause a mismatch to what's shown in Partner Analytics, which is updated on a daily basis.
