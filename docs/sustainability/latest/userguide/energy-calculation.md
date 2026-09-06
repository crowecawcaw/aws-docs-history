

# Calculate your energy usage
<a name="energy-calculation"></a>

**Note**  
The energy data calculated using this method is for informational purposes only. Do not use this information for optimization.
This method is not supported in the Canada (Central) and Africa (Cape Town) Regions due to their specific power infrastructure.

The AWS Sustainability service provides data to calculate the energy use of your cloud carbon footprint. By combining Scope 2 location-based emissions (LBM) data with publicly available grid emissions factors, you can determine the estimated energy footprint of your AWS workloads. For more information about energy emission factors used by Amazon, see [Amazon Carbon Methodology Document](https://sustainability.aboutamazon.com/carbon-methodology.pdf).

To determine the estimated energy consumption behind your cloud carbon footprint, divide the Scope 2 location-based emissions by the corresponding grid emissions factor. Be sure to apply unit conversions as needed:

`Energy consumption = Location‐based emissions / Grid emissions factor`

**Example calculation**  
If the grid emissions factor was 500 kg CO2e/MWh, and your cloud usage generated Scope 2 LBM emissions are 100 MTCO2e in the US West (Oregon) Region in 2025, calculate energy usage as follows:  

1. Multiply 100 MTCO2e by 1,000 to convert metric tons to kilograms.

1. Divide the result by the grid emissions factor of 500 kgCO2e for the US West (Oregon) Region.
`(100 MTCO2e * 1000) / 500 kgCO2e/MWh = 200 MWh`