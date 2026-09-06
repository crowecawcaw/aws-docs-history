

# Carbon emissions
<a name="methodology-carbon"></a>

The AWS Sustainability service quantifies customer-specific greenhouse gas (GHG) emissions associated with the use of AWS cloud services and covers the full range of said services.

The methodology adopted in the AWS Sustainability service is based on the data sources and allocation methods outlined in the following standards:
+ [GHG Protocol](https://ghgprotocol.org/) and its underlying standard [ISO 14064](https://www.iso.org/standard/66453.html)
+ [GHG Protocol Product Life Cycle Accounting and Reporting Standard](https://ghgprotocol.org/product-standard/) and associated [Information and Communication Technology (ICT) sector guidance](https://ghgprotocol.org/sites/default/files/2023-03/GHGP-ICTSG%20-%20ALL%20Chapters.pdf).
+ [ISO 14040](https://www.iso.org/standard/37456.html) and [ISO 14044](https://www.iso.org/standard/38498.html) for Life Cycle Assessment (LCA)

The carbon emissions calculation methodology uses elements from these standards to define our system boundaries, input data, and allocation approach and is updated over time based on evolving data, climate science, and more. To see the full methodology document for the current version of the methodology and the third-party verification letter see [Reports](https://sustainability.aboutamazon.com/reports) on the *Amazon Sustainability* page. When AWS releases a new version of the methodology, historical data is recalculated using the updated version to ensure accurate comparisons over time.

## Regions, usage, and billing data factors
<a name="regions-usage-billing"></a>

Electricity grids in different parts of the world use various sources of power. Some use carbon-intense fuels (for example, coal), and some are primarily low-carbon hydro or other renewables. The locations of Amazon's carbon-free energy projects also play a role, because the energy produced by these projects is accounted against our emissions from Regions on the same grid. As a result, not all AWS Regions have the same carbon intensity.

There are some Regions where high usage results in relatively low emissions. There are others where the low usage results in higher emissions. For example, emissions from usage in European AWS Regions often represents a smaller share of total emissions even if that is an area with high usage, because there are more renewables on the grid. AWS Regions in Asia Pacific can represent a larger share of total emissions even when customer usage in those Regions is smaller, given the lower availability of low carbon energy in some Asia Pacific Regions. Carbon estimates are based on usage only, and one-time charges such as upfront Savings Plan purchases, won't result in similar increases in carbon emissions.

## AWS Sustainability service and Amazon's carbon footprint report
<a name="sustainability-vs-amazon-footprint"></a>

Amazon's carbon footprint report is a part of our annual sustainability report. It covers Scope 1 through 3 emissions for all Amazon operations, including Amazon Web Services. The customer carbon footprint data available in the AWS Sustainability console provides you with the emissions that are attributable to your own AWS usage. For more information, see [Amazon Sustainability](https://sustainability.aboutamazon.com/).