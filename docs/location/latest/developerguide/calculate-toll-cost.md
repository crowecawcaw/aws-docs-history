# Calculate toll cost

This topic provides an overview of the fields and definitions associated with
calculating toll costs. Using these fields, you can specify parameters such as payment
methods, currency, and vehicle characteristics to customize toll cost
calculations.

| Field name      | Routes            |
| --------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Transponders    | Yes, with options |
| Vignettes       | Yes, with options |
| Currency        | Yes, with options |
| EmissionType    | Yes, with options |
| VehicleCategory | Yes, with options | ## Definitions This section provides brief definitions for each field used in toll cost calculation. \***\*Transponders\*\*** Transponders are a method of payment for tolls, potentially resulting in a different price compared to other payment methods. \***\*Vignettes\*\*** A vignette is a form of road pricing. When a user has the required vignette, no additional toll payments are necessary. \***\*Currency\*\*** The currency in which toll costs are reported. In addition to the local currency, a converted currency is included, which also impacts the currency used in the toll summary within the response. \***\*EmissionType\*\*** The emission type of the vehicle, used for calculating toll costs based on vehicle emissions. \***\*VehicleCategory\*\*** The vehicle sub-category used for toll cost calculation. |
