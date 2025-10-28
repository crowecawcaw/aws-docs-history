# Understanding the Customer Carbon Footprint Tool (CCFT)

This page defines each console section, so you can understand the information provided in
depth.

The unit of measurement for carbon emissions is metric tons of carbon dioxide-equivalent
(MTCO2e), an industry-standard measure. This measurement considers multiple greenhouse
gases, including carbon dioxide, methane, and nitrous oxide. All greenhouse gas
emissions are converted to MTCO2e using their respective Global Warming Potential (GWP)
values as defined by the Intergovernmental Panel on Climate Change (IPCC). This
standardized approach enables organizations to express the climate impact of various
greenhouse gases in a single, comparable unit.

Carbon emissions data is available for the previous 38 months. This is to allow a simple
process for annual comparisons for the past three years. New data is usually published
monthly between the 15th - 25th, with a delay of three months as AWS gathers and
processes the data required to provide your carbon emissions estimates. The Customer Carbon Footprint Tool shows
your carbon footprint at the 0.001 MTCO2e (1 kgCO2e) resolution. If your emissions are
lower than 0.0005 MTCO2e (0.5 kgMTCO2e) in the reporting month, it will appear as
`0`. To see your carbon footprint at the 0.000001 MTCO2e (1 gram)
resolution, see [Data
Exports](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md").

To calculate your energy usage using the CCFT location-based emissions data, see [Calculating your energy usage](ccft-energy.md "ccft-energy.md").

To learn more about historical changes to the features, methodology, and other information, see the [_Customer Carbon Footprint Tool Release Notes_](../../../ccft/latest/releasenotes/what-is-service.md "../../../ccft/latest/releasenotes/what-is-service.md").

**Your carbon emissions summary**

This section shows your estimated AWS emissions and estimated emissions savings. The
tool shows Scope 2 and Scope 3 emissions calculated using the market-based
method (MBM) by default. You can see your emissions calculated using the
location-based method (LBM) by choosing **LBM** in the
**Calculation method filter** on the dashboard.
Emissions savings are the difference between the carbon footprint emissions
calculated using the location-based method (LBM) and the market-based method
(MBM). For more information about LBM and MBM, see [Input data](ccft-overview-input.md "ccft-overview-input.md").

**Your AWS carbon emissions**

This section shows trends in your carbon emissions over time, broken down by your top AWS Regions. You see the top 5 Regions by default and any other Regions are grouped under **Other**. To see emissions across all Regions, choose the **Emissions by AWS Region** tab.

**Your emissions by service**

This section shows the carbon emissions resulting from your usage of Amazon Elastic Compute Cloud (EC2),
Amazon Simple Storage Service (S3), and Amazon CloudFront (CloudFront). Any other AWS products and services
are grouped under **Other**.

**Your emissions by AWS Region**

This section shows the carbon emissions associated with each applicable AWS Region. For example, `US East (Ohio)`, `Europe (London)`. Emissions from global services, such as Amazon CloudFront, are reported under **Global**.

To see your emissions by scope (Scope 1, 2, 3) see [What is AWS Data Exports?](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md")

## Downloading your carbon emissions data

You can access your carbon emissions data in bulk using one of the two options available on the top right of the Customer Carbon Footprint Tool console page.

**Download CSV**

Choose this option to download a CSV file containing your historical data up to 38 months. This file includes data by month, service, and AWS Region. The data in this file is always calculated using the latest methodology version.

**Download CSV (legacy version)**

Choose the dropdown next to **Download CSV** to find this option. This
option is temporarily present after a new methodology version is
released. This contains your carbon estimates using the previous
methodology calculations. You can use this to compare data between the
different methodology versions. For example, methodology version 2 is
released on April 2025; the **Download CSV** (legacy
version) will contain data calculated with version 1.

To access your historical data using previous methodologies after a new one is released, make sure you have a **Data Export** set up. We will not override data exported to your Amazon S3 bucket that is calculated using previous methodologies.

**Create custom data export**

Choose this to navigate to the **Data Exports**. Then, you can create
carbon emissions data exports using basic SQL and visualize your data by
integrating with Quick Suite. By using custom data exports, you can access account level details for all accounts in a given organization.
