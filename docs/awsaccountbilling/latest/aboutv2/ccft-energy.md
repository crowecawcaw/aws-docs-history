# Calculating your energy usage

###### Note

- The energy data calculated using this method is for informational purposes only. Do not use this information for optimization.
- This method is not supported in the Canada (Central) and Africa (Cape Town) Regions due to their specific power infrastructure.
  The Customer Carbon Footprint Tool (CCFT) provides data to calculate the energy use of your cloud carbon footprint. By combining the Scope 2 location-based emissions method (LBM) data with publicly available grid emissions factors, you can determine the estimated energy footprint of your AWS workloads. For more information about energy emission factors used by Amazon, see [Amazon Carbon Methodology Document](https://sustainability.aboutamazon.com/carbon-methodology.pdf "https://sustainability.aboutamazon.com/carbon-methodology.pdf").

###### Note

Do not use the total LBM emissions provided in the CCFT to calculate your energy usage, use instead Scope 2 LBM from [Data Exports](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md") (column: `total_scope_2_lbm_emissions_value`). The total LBM number includes Scope 1 and Scope 3, which are not part of the energy calculation, and using this data will result in over-estimated energy figures.

To determine the estimated energy consumption behind your cloud carbon footprint, divide the location-based emissions by the corresponding grid emissions factor. Be sure to apply unit conversions as needed:

`Energy consumption = Location‐based emissions / Grid emissions factor`

###### Example

If the grid emissions factor was 500 kg CO2e/MWh, and your cloud usage generated LBM emissions are 100 MTCO2e in the US West (Oregon) Region in 2025, calculate energy usage as follows:

1. Multiply 100 MTCO2e by 1,000 to convert metric tons to kilograms.
2. Divide the result by the grid emissions factor of 500 kgCO2e for the US West (Oregon) Region.
   `(100 MTCO2e * 1000) / 500 kgCO2e/MWh = 200 MWh`
