# Customer Profiles

standard air booking object fields

The following table lists all the fields in the Customer Profiles standard
air booking object.

| AirBooking            | Standard airBooking field | Type                                                             | Description               |
| --------------------- | ------------------------- | ---------------------------------------------------------------- | ------------------------- | ---------------------------- | -------------------------------- | ----------- |
| BookingId             | String                    | The unique identifier of the standard air booking                |
| ContextId             | String                    | The context-specific identifier for tracing reservation source   |
| PreferenceRef         | String                    | The identifier referencing the Preference object for the booking |
| BookingName           | String                    | The name associated with the booking                             |
| PassengerIndex        | String                    | Index for the passenger within the booking                       |
| TravellerId           | String                    | Unique identifier for traveler associated with the booking       |
| GroupBooking          | String                    | Indicates if the booking is for a group                          |
| NumberOfPassengers    | String                    | Total number of passengers in the booking                        |
| NumberOfAdults        | String                    | Total number of adults in the booking                            |
| NumberOfChildren      | String                    | Total number of children in the booking                          |
| ProcessedDate         | String                    | Date the booking was processed                                   |
| CreatedDate           | String                    | Date the booking was created                                     |
| CreatedBy             | String                    | Identity of the creator                                          |
| UpdatedDate           | String                    | Last update date                                                 |
| UpdatedBy             | String                    | Identifier of who last updated the booking                       |
| Status                | String                    | Current booking status                                           |
| PriorityStatus        | String                    | Priority tier of the booking                                     |
| ReservationStatus     | String                    | Reservation status of the booking                                |
| MarketingCode         | String                    | Code representing marketing source or campaign                   |
| MarketingName         | String                    | Marketing campaign name                                          |
| TravelAgent           | String                    | Travel agent associated with the booking                         |
| TravelAgency          | String                    | Name of corporate travel agency                                  |
| TravelCorpNumber      | String                    | Corporate customer number                                        |
| Booker                | String                    | Indicates if the person is the one who made the booking          |
| AdditionalInformation | String                    | Additional freeform info                                         |
| Email                 | String                    | Contact email for travel day updates                             |
| PhoneNumber           | String                    | Contact phone for travel day updates                             |
| CancelledDate         | String                    | Date of booking cancellation (if applicable)                     |
| Diplomat              | String                    | Indicates diplomatic status                                      |
| Child                 | String                    | Indicates if the passenger is a child                            |
| Disabled              | String                    | Indicates disability status                                      |
| Oxygen                | String                    | Indicates need for oxygen support                                |
| PetOnly               | String                    | Booking is only for transporting pet                             |
| CancellationCharge    | String                    | Cancellation charge if applicable. 0 would mean no charge        |
| Refundable            | String                    | Details on booking refund                                        |
| Inventory             | Inventory                 | Inventory details for booking                                    |
| Loyalty               | Loyalty                   | Loyalty details for booking                                      |
| Channel               | Channel                   | Channel details for booking                                      |
| Payment               | Payment                   | Payment details for booking                                      |
| BillingAddress        | Address                   | Billing address details for booking                              |
| Price                 | Price                     | Booking price details                                            |
| PaymentStatus         | PaymentStatus             | Payment status of booking                                        |
| Attributes            | Map<String, String>       | Custom or extension attributes                                   | Standard Index Fields     | Standard index name          | Standard preference record field |
| ---                   | ---                       |                                                                  | \_airBookingId            | BookingId                    |
| \_airPreferenceRef    | PreferenceRef             | Loyalty data type                                                | Standard airBooking field | Type                         | Description                      |
| ---                   | ---                       | ---                                                              |
| ProgramName           | String                    | Name of the loyalty program                                      |
| MembershipId          | String                    | Loyalty program membership number                                |
| Tier                  | String                    | Loyalty membership tier level                                    | Channel data type         | Standard airBooking field    | Type                             | Description |
| ---                   | ---                       | ---                                                              |
| CreationChannelId     | String                    | ID of the channel used to create the booking                     |
| LastUpdatedChannelId  | String                    | ID of the channel used to update the booking                     |
| Method                | String                    | Method used via the channel (e.g., web, app, phone)              | Payment data type         | Standard airBooking field    | Type                             | Description |
| ---                   | ---                       | ---                                                              |
| Type                  | String                    | Payment method type (e.g., card, voucher)                        |
| CreditCardToken       | String                    | Tokenized card for secure reference                              |
| CreditCardType        | String                    | Type of credit card used                                         |
| CreditCardExpiration  | String                    | Expiry date of the card                                          |
| Cvv                   | String                    | CVV number                                                       |
| NameOnCreditCard      | String                    | Cardholder name                                                  |
| RoutingNumber         | String                    | Bank routing number (if applicable)                              |
| AccountNumber         | String                    | Bank account number (if applicable)                              |
| VoucherId             | String                    | Voucher used for payment                                         |
| DiscountCode          | String                    | Promotional discount code applied                                |
| DiscountPercent       | String                    | Percent of discount applied to payment                           | Billing Address data type | Standard airPreference field | Data type                        | Description |
| ---                   | ---                       | ---                                                              |
| Address1              | String                    | The first line of a customer address.                            |
| Address2              | String                    | The second line of a customer address.                           |
| Address3              | String                    | The third line of a customer address.                            |
| Address4              | String                    | The fourth line of a customer address.                           |
| City                  | String                    | The city of the customer address.                                |
| Country               | String                    | The country of the customer address.                             |
| County                | String                    | The county of the customer address.                              |
| PostalCode            | String                    | The postal code of the customer address.                         |
| Province              | String                    | The province of the customer address.                            |
| State                 | String                    | The state of the customer address.                               | Price data type           | Standard airBooking field    | Type                             | Description |
| ---                   | ---                       | ---                                                              |
| TotalPrice            | String                    | Total Price of the booking                                       |
| BasePrice             | String                    | Base price of the booking                                        |
| TravellerPrice        | String                    | Price paid per traveler                                          |
| DiscountAmount        | String                    | Discount applied to base fare                                    |
| Currency              | String                    | Currency in which payment was made                               | Payment Status data type  | Standard airBooking field    | Type                             | Description |
| ---                   | ---                       | ---                                                              |
| PaidAt                | String                    | Timestamp when payment was completed                             |
| AwaitingPayment       | String                    | Indicates payment is pending                                     |
| RequiredBy            | String                    | Payment due date                                                 | Inventory data type       | Standard airBooking field    | Type                             | Description |
| ---                   | ---                       | ---                                                              |
| Seats                 | String                    | Total number of seats in booking                                 |
