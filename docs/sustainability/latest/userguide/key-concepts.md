# Key concepts

Described below are the key concepts and terms that apply to all visualizations within the AWS Sustainability console and the corresponding API.

**Water withdrawals**

The total volume of water taken from any source (e.g., surface water, groundwater, rainwater, third-party/municipal supply, and reclaimed water)
for data center operations, regardless of whether it is eventually returned to the environment.
A significant portion of withdrawn water is returned to the environment or recycled.

**Unit of measure**

Carbon: The unit of measurement for carbon emissions is metric tons of carbon dioxide-equivalent (MTCO2e), an industry-standard measure. This measurement considers multiple greenhouse gases, including carbon dioxide, methane, and nitrous oxide. All greenhouse gas emissions are converted to MTCO2e using their respective Global Warming Potential (GWP) values as defined by the Intergovernmental Panel on Climate Change (IPCC). This standardized approach enables organizations to express the climate impact of various greenhouse gases in a single, comparable unit.

Water withdrawals: The unit of measurement for water withdrawals is cubic meters (m³), an industry-standard measure used by organizations such as the Organisation for Economic Co-operation and Development (OECD) and the World Bank

**Publishing timing**

Carbon: Data is available back to January 2022, though we limit how many records are displayed in the **Carbon emissions** page to maintain legibility of the data (the full historical dataset can be accessed via API or Data Exports). New data is published monthly by the 21st of the month following the usage (e.g. January data is published by February 21st).

Water withdrawals: Data is available back to 2023, published with an annual granularity on a yearly basis. For example, 2025 data is published in Q2 2026.

**Data resolution**

Carbon: The AWS Sustainability service shows your carbon footprint at the 0.000001 MTCO2e (1 gram CO2e) resolution. If your emissions are lower than 0.0000005 MTCO2e (0.5 grams CO2e) in the reporting month, it will appear as `0`.

Water withdrawals: The AWS Sustainability service shows your water withdrawals at the 0.000001 m³ (1 milliliter) resolution. If your water withdrawals are lower than 0.0000005 m³ (0.5 milliliters) in the reporting year, it will appear as `0`.

**AWS Region**

AWS services are hosted in multiple locations world-wide. These locations are composed of AWS Regions, Availability Zones, Local Zones, and Wavelength Zones. Each Region is a separate geographic area. The AWS Sustainability service shows the environmental impact associated with each applicable AWS Region. For example, `US East (Ohio)`, `Europe (London)`. Emissions from global services, such as Amazon CloudFront, are reported under `Global`.

**Services**

AWS offers a broad set of services including compute, storage, databases, analytics, networking, mobile, developer tools, management tools, IoT, security, and enterprise applications. The AWS Sustainability service metrics include impact from all AWS Services. Currently, Amazon Elastic Compute Cloud (EC2), Amazon Simple Storage Service (S3), and Amazon CloudFront are broken out in the AWS Sustainability console, while all other products are displayed as **Other**.

**Fiscal year**

By default, the AWS Sustainability service uses calendar year (January to December) for quarter and year aggregations. You can customize your own fiscal year if it differs from calendar year, for example, March to February. The label for this field corresponds to the year of the ending month. For example, a fiscal year that runs from March 2025 to February 2026 will be shown as FY 2026. Fiscal quarters are calculated from the fiscal year starting month. For example, for a fiscal year that runs from March 2025 to February 2026, Q1 will be March, April, and May 2025.

Water withdrawals data is available at a calendar year granularity only, so fiscal year configuration is not available.

**Methodology version**

The environmental data presented in the AWS Sustainability service reflects the most recent methodology version available for a given month.
When AWS releases a new version of the methodology, the release notes page is updated with information about the changes and historical data is recalculated using the updated version to ensure accurate comparisons over time.
If you want to keep carbon data calculated using previous versions of the methodology we recommend creating a [Data Export](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md"), which exports your carbon data to Amazon S3.
When a new version is released it has its own prefix and previous versions remain available. Water data is not available in Data Exports at this time.

**AWS Organizations**

If you're signed in as a management account of AWS Organizations, the AWS Sustainability service will report the consolidated environmental impact of all the member accounts within that management account, for the duration that those member accounts were a part of your organization. The field **usage account** shows the breakdown of each account with usage within the management account, so you can understand where your environmental impact comes from.

If you're signed in as a member account, the AWS Sustainability service will report emission data for the member account only.
