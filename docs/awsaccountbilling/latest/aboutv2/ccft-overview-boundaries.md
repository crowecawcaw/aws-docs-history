# System boundary

The system boundary defines what activities and related emissions are accounted for in the CCFT calculations. The CCFT is informed by the GHG Protocol’s classification of emissions, which breaks down a company’s emissions into three `scopes`.

- **Scope 1**: Emissions are direct emissions from owned or controlled sources.
- **Scope 2**: Emissions are indirect emissions from the production of purchased energy.
- **Scope 3**: Emissions are all indirect emissions (not included
  in scope 2) that occur in the value chain of the reporting company,
  including both upstream and downstream emissions (for example, manufacturing
  of hardware, end-of-life emissions).

**Scope 1**
The CCFT includes emissions from fuel combustion in emergency backup generators and
emissions from refrigerant use and natural gas consumption in
AWS-owned or controlled facilities. This includes locations where AWS has operational control on the server racks deployed that support cloud services (for example, "colo" data centers). The model also includes emissions from certain edge sites (CloudFront emissions are included).

**Scope 2**
The CCFT reports Scope 2 emissions from AWS owned or controlled facilities that support cloud
services, as well as certain edge sites (For example, CloudFront emissions are
included), using both the market-based
method (MBM) and location-based method (LBM) calculations.

**Scope 3**
The CCFT accounts for:

- Emissions from fuel- and energy-related activities (FERA under the GHG Protocol). This includes upstream emissions from purchased fuels and electricity, as well as emissions from transmission and distribution losses, for facilities within the system boundary.

- IT hardware embodied carbon - manufacturing emissions from server racks deployed in AWS-owned or operated data center facilities.

- Data center building embodied carbon - manufacturing emissions from AWS owned or operated data center buildings.

- Non-IT equipment embodied carbon - manufacturing emissions from non-IT equipment deployed in AWS owned or operated data center facilities.

The Customer Carbon Footprint Tool excludes emissions associated with AWS warehouses, manufacturing facilities, and offices. These emissions are not attributable to the provision of cloud services. Any emissions stemming from sites ran in customer facilities (for example, Amazon Cloud Extension, Embedded Points of Presence, AWS Outposts sites) are not covered by Customer Carbon Footprint Tool at this time. For more information, see the [CCFT Methodology Document](http://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology.pdf "http://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology.pdf").
