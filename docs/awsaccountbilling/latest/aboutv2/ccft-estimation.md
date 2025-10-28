# Understanding your carbon emission estimations

The Customer Carbon Footprint Tool quantifies customer-specific greenhouse gas (GHG) emissions associated with the use of AWS cloud services. The tool covers the full range of cloud products.

The methodology adopted in the Customer Carbon Footprint Tool is based on the data sources and allocation methods outlined in the following standards:

- [GHG Protocol](https://ghgprotocol.org/ "https://ghgprotocol.org/") and its underlying standard [ISO 14064](https://www3.epa.gov/ttnchie1/conference/ei16/session13/wintergreen.pdf "https://www3.epa.gov/ttnchie1/conference/ei16/session13/wintergreen.pdf")
- [GHG Protocol Product Life Cycle Accounting and Reporting Standard](https://ghgprotocol.org/product-standard/ "https://ghgprotocol.org/product-standard/") and associated [Information and Communication Technology (ICT) sector guidance](https://ghgprotocol.org/sites/default/files/2023-03/GHGP-ICTSG%20-%20ALL%20Chapters.pdf "https://ghgprotocol.org/sites/default/files/2023-03/GHGP-ICTSG%20-%20ALL%20Chapters.pdf").
- [ISO 14040](https://www.iso.org/standard/37456.html "https://www.iso.org/standard/37456.html") and [ISO 14044](https://www.iso.org/standard/38498.html "https://www.iso.org/standard/38498.html") for Life Cycle Assessment (LCA)
  The Customer Carbon Footprint Tool methodology uses elements from these standards to define our [system boundaries](ccft-overview-boundaries.md "ccft-overview-boundaries.md"), [input data](ccft-overview-input.md "ccft-overview-input.md"), and [allocation approach](ccft-overview-allocation.md "ccft-overview-allocation.md") and is updated over time based on evolving data, climate science, and more. To see the full methodology document for the current version of the methodology and the third-party verification letter see [Reports](https://sustainability.aboutamazon.com/reporting "https://sustainability.aboutamazon.com/reporting") on the
  _Amazon Sustainability_ page. When AWS releases a new version of the methodology, historical data is recalculated using the updated version to ensure accurate comparisons over time.

## Regions, usage, and billing data factors

Electricity grids in different parts of the world use various sources of power. Some use
carbon-intense fuels (for example, coal), and some are primarily low-carbon hydro or
other renewables. The locations of Amazon's renewable energy projects also play a
role, because the energy produced by these projects is accounted against our
emissions from Regions on the same grid. As a result, not all AWS Regions have the
same carbon intensity.

There are some Regions where high usage results in relatively low emissions. There are
others where the low usage results in higher emissions. For example, emissions from
usage in European AWS Regions often represents a smaller share of total emissions even if that is an area with high usage, because there are more renewables on the grid. AWS Regions in Asia Pacific can represent a larger share of total emissions even when customer usage in those Regions is smaller, given the lower availability of low carbon energy in some Asia Pacific Regions. Carbon estimates are based on usage only, and one-time charges such as
upfront Savings Plan purchases, won't result in similar increases in carbon
emissions.

## Customer Carbon Footprint Tool and Amazon's carbon footprint report

Amazon's carbon footprint report is a part of our annual sustainability report. This covers
Scope 1 through 3 emissions for all Amazon operations, including Amazon Web Services. The
customer carbon footprint report provides you with the emissions that attribute to
your own AWS usage. For more information, see [Amazon
Sustainability](https://sustainability.aboutamazon.com/ "https://sustainability.aboutamazon.com/").

###### Topics

- [System boundary](ccft-overview-boundaries.md "ccft-overview-boundaries.md")
- [Input data](ccft-overview-input.md "ccft-overview-input.md")
- [Allocation approach](ccft-overview-allocation.md "ccft-overview-allocation.md")
