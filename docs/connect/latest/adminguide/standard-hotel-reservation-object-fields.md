# Customer Profiles

standard hotel reservation object fields

The following table lists all the fields in the Customer Profiles standard
hotel reservation object.

| Hotel Reservation    | Standard hotelReservation field | Type                                                                    | Description |
| -------------------- | ------------------------------- | ----------------------------------------------------------------------- | ----------- |
| ReservationId        | String                          | Unique identifier of the stanndard hotel<br>reservation                 |
| ConfirmationNumber   | String                          | Confirmation number provided by the hotel or booking<br>engine          |
| PreferenceRef        | String                          | The identifier referencing the Preference object for the<br>reservation |
| Status               | String                          | Current status of the reservation (e.g., confirmed,<br>cancelled)       |
| TripType             | String                          | Purpose or nature of the trip (e.g., leisure,<br>business)              |
| BrandCode            | String                          | Code representing the hotel brand                                       |
| HotelCode            | String                          | Code identifying the specific hotel                                     |
| PhoneNumber          | String                          | Contact phone number for the reservation                                |
| EmailAddress         | String                          | Contact email address for the reservation                               |
| GroupId              | String                          | ID linking the reservation to a group booking                           |
| ContextId            | String                          | Context-specific identifier for tracing reservation<br>source           |
| ProcessedDate        | String                          | Timestamp when the reservation was processed                            |
| CreatedDate          | String                          | Timestamp when the reservation was created                              |
| CreatedBy            | String                          | Identifier of the user/system that created the<br>reservation           |
| UpdatedDate          | String                          | Timestamp when the reservation was last updated                         |
| UpdatedBy            | String                          | Identifier of the user/system that updated the<br>reservation           |
| AgentId              | String                          | ID of the agent handling the booking                                    |
| Reserver             | String                          | Denotes if the profile is the reserver                                  |
| SameDayRate          | String                          | Indicates if the booking was made for the same<br>day                   |
| Refundable           | String                          | Indicates if the booking is refundable                                  |
| CancellationCharge   | String                          | Cancellation charge if applicable. 0 would mean no<br>charge            |
| TransactionId        | String                          | Unique identifier of transaction                                        |
| AmountPerNight       | String                          | Amount charged per night for room                                       |
| AdditionalNote       | String                          | Special notes or instructions                                           |
| NumberOfNights       | String                          | Number of nights in reservation                                         |
| NumberOfGuests       | String                          | Number of total guests in reservation                                   |
| TotalAmountBeforeTax | String                          | Total cost before tax                                                   |
| TotalAmountAfterTax  | String                          | Total cost after tax                                                    |
| Checkout             | CheckOut                        | Checkout details                                                        |
| Loyalty              | Loyalty                         | Loyalty details                                                         |
| Room                 | Room                            | Room details                                                            |
| CheckIn              | CheckIn                         | Check-in details                                                        |
| Payment              | Payment                         | Payment details                                                         |
| Currency             | Currency                        | Currency details                                                        |
| Cancellation         | Cancellation                    | Cancellation details                                                    |
| Channel              | Channel                         | Channel details                                                         |
| RatePlan             | RatePlan                        | Rate plan details                                                       |
| Guests               | Guests                          | Guest details                                                           |
| Services             | Service List                    | List of services                                                        |
| Attributes           | Map<String, String>             | Additional attributes                                                   |

| Standard Index Fields | Standard index name | Standard preference record field |
| --------------------- | ------------------- | -------------------------------- |
| \_hotelReservationId  | ReservationId       |
| \_hotelPreferenceRef  | preferenceRef       |

| Checkout data type | Standard hotelReservation field | Type                                     | Description |
| ------------------ | ------------------------------- | ---------------------------------------- | ----------- |
| Early              | String                          | Early checkout is scheduled or requested |
| Late               | String                          | Late checkout is scheduled or requested  |
| Self               | String                          | Self checkout is scheduled or requested  |
| Date               | String                          | Checkout date of reservation             |

| Loyalty data type | Standard hotelReservation field | Type                               | Description |
| ----------------- | ------------------------------- | ---------------------------------- | ----------- |
| ProgramName       | String                          | Name of the loyalty program        |
| MembershipId      | String                          | Member's ID in the loyalty program |
| Tier              | String                          | Loyalty tier or level              |

| Room data type    | Standard hotelReservation field | Type                                        | Description |
| ----------------- | ------------------------------- | ------------------------------------------- | ----------- |
| TypeCode          | String                          | Code for room type/category                 |
| TypeName          | String                          | Name of room type                           |
| TypeDesc          | String                          | Description of room type                    |
| Number            | String                          | Assigned room number                        |
| Capacity          | String                          | Maximum capacity of the room                |
| AccessibilityType | String                          | Accessibility features                      |
| SmokingAllowed    | String                          | Indicates if smoking is allowed in the room |

| CheckIn data type | Standard hotelReservation field | Type                                       | Description |
| ----------------- | ------------------------------- | ------------------------------------------ | ----------- |
| Date              | String                          | Check-in date of reservation               |
| DigitalKey        | String                          | Indicates if a digital room key was issued |
| Early             | String                          | Indicates if early check-in was requested  |
| Late              | String                          | Indicates if late check-in was requested   |
| RoomKeys          | String                          | Number of room keys issued                 |
| UserSelectedRoom  | String                          | True if guest selected their own room      |

| Payment data type    | Standard hotelReservation field | Type                                                  | Description |
| -------------------- | ------------------------------- | ----------------------------------------------------- | ----------- |
| Type                 | String                          | Payment method type (e.g., credit, debit,<br>voucher) |
| CreditCardToken      | String                          | Tokenized credit card number                          |
| CreditCardType       | String                          | Type of credit card (e.g., Visa, Amex)                |
| CreditCardExpiration | String                          | Credit card expiration date                           |
| Cvv                  | String                          | Card verification value                               |
| NameOnCreditCard     | String                          | Name printed on the credit card                       |
| RoutingNumber        | String                          | Bank routing number                                   |
| AccountNumber        | String                          | Bank account number                                   |
| VoucherId            | String                          | Voucher identifier if used                            |
| DiscountCode         | String                          | Applied discount code                                 |
| DiscountPercent      | String                          | Percentage discount applied                           |

| Currency data type | Standard hotelReservation field | Type                                        | Description |
| ------------------ | ------------------------------- | ------------------------------------------- | ----------- |
| Code               | String                          | ISO code for the currency (e.g., USD)       |
| Name               | String                          | Full name of the currency (e.g., US Dollar) |
| Symbol             | String                          | Symbol of the currency (e.g., $)            |

| Cancellation data type | Standard hotelReservation field | Type                          | Description |
| ---------------------- | ------------------------------- | ----------------------------- | ----------- |
| Reason                 | String                          | Reason for cancellation       |
| Comment                | String                          | Additional cancellation notes |

| Channel data type    | Standard hotelReservation field | Type                                                         | Description |
| -------------------- | ------------------------------- | ------------------------------------------------------------ | ----------- |
| CreationChannelId    | String                          | ID for the channel through which the reservation was<br>made |
| LastUpdatedChannelId | String                          | ID for the channel that last updated the<br>reservation      |
| Method               | String                          | Method used for booking (e.g., web, mobile app)              |

| RatePlan data type | Standard hotelReservation field | Type                                    | Description |
| ------------------ | ------------------------------- | --------------------------------------- | ----------- |
| Code               | String                          | Code Identifier of the rate plan booked |
| Name               | String                          | Name of the rate plan booked            |
| Description        | String                          | Description of the rate plan            |

| Service data type | Standard hotelReservation field | Type                                   | Description |
| ----------------- | ------------------------------- | -------------------------------------- | ----------- |
| ServiceType       | String                          | Type of service (e.g., spa, breakfast) |
| Description       | String                          | Description of the service             |
| Cost              | String                          | Cost of the service                    |

| Guest data type | Standard hotelReservation field | Type                   | Description |
| --------------- | ------------------------------- | ---------------------- | ----------- |
| Adults          | String                          | Number of adult guests |
| Children        | String                          | Number of child guests |
