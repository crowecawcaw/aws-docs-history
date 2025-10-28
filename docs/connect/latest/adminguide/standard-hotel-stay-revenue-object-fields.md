# Customer

Profiles standard hotel stay revenue object fields

The following table lists all the fields in the Customer Profiles standard
hotel stay revenue object.

| Hotel Stay Revenue | Standard hotelStayRevenue field | Type                                                            | Description           |
| ------------------ | ------------------------------- | --------------------------------------------------------------- | --------------------- | ------------------- | -------------------------------- |
| StayRevenueId      | String                          | The unique identifier of the standard hotel stay revenue.       |
| CurrencyCode       | String                          | ISO code for the currency (e.g., USD)                           |
| CurrencyName       | String                          | Full name of the currency (e.g., US Dollar)                     |
| CurrencySymbol     | String                          | Symbol of the currency (e.g., $)                                |
| ReservationId      | String                          | Unique identifier for the hotel reservation                     |
| GuestId            | String                          | Unique identifier for the guest                                 |
| LastUpdatedOn      | String                          | Timestamp of the last update to the stay record                 |
| CreatedOn          | String                          | Timestamp of when the stay record was created                   |
| LastUpdatedBy      | String                          | Identifier of the user/system that last updated the stay record |
| CreatedBy          | String                          | Identifier of the user/system that created the stay record      |
| StartDate          | String                          | Start date of the hotel stay                                    |
| HotelCode          | String                          | Code identifying the specific hotel                             |
| Type               | String                          | Type of revenue (e.g., room rate, incidentals, taxes)           |
| Description        | String                          | Description of the revenue item                                 |
| Amount             | String                          | Amount of the revenue item                                      |
| ProcessedDate      | String                          | Date the revenue was processed                                  |
| Status             | String                          | Status of the revenue item                                      |
| Attributes         | Map<String, String>             | Additional metadata or program-specific values.                 | Standard Index Fields | Standard index name | Standard preference record field |
| ---                | ---                             |                                                                 | \_hotelStayRevenueId  | StayRevenueId       |
