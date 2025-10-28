# Input data

This section outlines the sources of data and transformations that occur upstream of the
Customer Carbon Footprint Tool to define Scope 1, Scope 2, and Scope 3 carbon emissions for each AWS
cluster. To understand the full methodology, see the [CCFT Methodology Document](http://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology.pdf "http://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology.pdf").

**Scope 1**
Amazon generates and assures Scope 1 activity data for its annual footprint every year. To
bridge the gap between Amazon's annual reporting and CCFT's
monthly cadence, AWS uses unassured primary Scope 1 activity data to
determine monthly emissions for the current month. Some of the activity
data might not be available at the time of publishing the monthly
report, therefore translating in an underestimation of Scope 1
emissions. We update our estimates when recasting, to align Scope 1
emissions reported in the CCFT with the assured data.

**Scope 2**
Similar to Scope 1, the CCFT methodology closely follows Amazon’s footprint methodology. In line with Amazon’s approach, we prioritize accuracy of data at the time of publishing in the CCFT, only falling back to other sources (for example, estimated energy consumption) when the primary source of data (for example, actual energy consumption) is not reasonably available.

AWS first estimates cluster and month level location-based (LBM) emissions by
estimating energy consumption (MWh) and multiplies this by LBM emission
factors.

###### Note

Location-based method (LBM) is a GHG Protocol method used in Scope 2 carbon emissions accounting that reflects the average emissions intensity of grids where energy consumption occurs.

After LBM, AWS considers market-based contractual instruments such as Energy Attribute
Certificates (EACs), Power Purchase Agreements (PPA) etc., to reflect
our carbon-free energy projects and calculate market-based (MBM)
emissions. This is in line with the Quality Criteria outlined in the GHG
Protocol Scope 2 guidance.

###### Note

Market-based method (MBM) is a GHG Protocol method used in Scope 2 carbon emissions accounting that reflects supplier-specific emissions intensity after accounting for Energy Attribute Certificates (EACs). For example, a company’s renewable energy purchases.

To learn more about the differences between LBM and MBM, see [GHG Protocol Scope 2 Guidance](https://ghgprotocol.org/sites/default/files/2023-03/Scope%202%20Guidance.pdf "https://ghgprotocol.org/sites/default/files/2023-03/Scope%202%20Guidance.pdf").

**Scope 3**
Fuel and energy related activities: For upstream emissions from purchased fuels, AWS collects fuel activity data and applies emission factors for fuel extraction, production, and transportation. For upstream emissions of purchased electricity and transmission and distribution (T&D) losses using location-based emissions (LBM), AWS multiplies the estimated energy consumption (MWh) by the relevant emission factor. For market-based emissions (MBM), AWS also accounts for Energy Attribute Certificates (EACs).

IT hardware: AWS uses a comprehensive cradle-to-gate approach that tracks emissions
from raw material extraction through manufacturing and transportation to
AWS data centers. The methodology employs four calculation pathways:
process-based life cycle assessment (LCA) with engineering attributes,
extrapolation, representative category average LCA, and economic
input-output LCA. AWS prioritizes the most detailed and accurate
methods for components that contribute significantly to overall
emissions.

Buildings and equipment: AWS follows established whole building life cycle assessment (wbLCA) standards, considering emissions from construction, use, and end-of-life phases. The analysis covers data center shells, rooms, and long-lead equipment such as air handling units and generators. The methodology uses both process-based life cycle assessment models and economic input-output analysis to ensure comprehensive coverage.

The Scope 3 emissions are then amortized over the assets' service life (6 years for IT hardware, 50 years for buildings) to calculate monthly emissions that can be allocated to customers. This amortization ensures that we fairly distribute the total embodied carbon of each asset across its operational lifetime, accounting for scenarios such as early retirement or extended use.

To ensure data quality, we use a Composite Quality Score (CQS) system and perform multiple validation checks throughout our calculation process. This systematic approach lets us provide customers with detailed, verifiable carbon footprint data while maintaining transparency about our calculations and assumptions.
