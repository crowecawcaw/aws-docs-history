# Customer Profiles

standard air segment object fields

The following table lists all the fields in the Customer Profiles standard
air segment object.

| Air Segment           | Standard airSegment Field | Type                                          | Description               |
| --------------------- | ------------------------- | --------------------------------------------- | ------------------------- | ------------------------- | -------------------------------- | ----------- |
| SegmentId             | String                    | Unique identifier of the standard air segment |
| BookingRef            | String                    | Booking reference identifier                  |
| SegmentName           | String                    | Name/description of the segment               |
| PassengerIndex        | String                    | Index number of the passenger                 |
| SegmentIndex          | String                    | Index number of the segment                   |
| SeatSelection         | String                    | Seat selection detail                         |
| NumberOfPassengers    | String                    | Total number of passengers                    |
| NumberOfLegs          | String                    | Number of flight legs                         |
| Tier                  | String                    | Passenger tier/status level                   |
| Origin                | String                    | Departure airport code                        |
| OriginCountryCode     | String                    | Country code of departure                     |
| Dest                  | String                    | Destination airport code                      |
| DestCountryCode       | String                    | Country code of destination                   |
| ProcessedDate         | String                    | Date when the segment was processed           |
| CreatedDate           | String                    | Date when the record was created              |
| CreatedBy             | String                    | User who created the record                   |
| UpdatedDate           | String                    | Date when the record was last updated         |
| UpdatedBy             | String                    | User who last updated the record              |
| Status                | String                    | Current status of the segment                 |
| FlightNumber          | String                    | Flight number                                 |
| Carrier               | String                    | Operating carrier code                        |
| CarrierType           | String                    | Type of carrier                               |
| IsInternational       | String                    | Indicates if flight is international          |
| IsEticket             | String                    | Indicates if electronic ticket                |
| IsArmed               | String                    | Indicates if armed passenger                  |
| LapInfant             | String                    | Lap infant details                            |
| Pet                   | String                    | Indicates if traveling with pet               |
| PrisonerOrGuard       | String                    | Indicates prisoner or guard status            |
| Child                 | String                    | Indicates if passenger is a child             |
| Married               | String                    | Indicates if segments are married             |
| CheckinEligible       | String                    | Indicates check-in eligibility                |
| InEligibleReason      | String                    | Reason if not eligible for check-in           |
| UnEscortedMinor       | String                    | Indicates unaccompanied minor status          |
| PremiumAccess         | String                    | Indicates premium access purchase             |
| MissingData           | String                    | Indicates missing data                        |
| CurrentClassOfService | String                    | Current service class                         |
| BookedClassOfService  | String                    | Originally booked service class               |
| CodeShare             | String                    | Indicates codeshare flight                    |
| ReverseCodeShare      | String                    | Indicates reverse codeshare                   |
| MarketCarrierCode     | String                    | Marketing carrier code                        |
| OpCarrierCode         | String                    | Operating carrier code                        |
| InConnection          | String                    | Incoming connection detail                    |
| OutConnection         | String                    | Outgoing connection detail                    |
| MilesToEarn           | String                    | Miles to be earned                            |
| Duration              | String                    | Duration of the flight                        |
| DurationTimeUnit      | String                    | Time unit for duration                        |
| Distance              | String                    | Distance of the flight                        |
| DistanceUnit          | String                    | Unit for distance measurement                 |
| SellType              | String                    | Indicates if this is a forced sell            |
| GoShow                | String                    | Indicates if this is a go show                |
| Incapacitated         | String                    | Indicates if passenger is incapacitated       |
| Upgraded              | String                    | Indicates if flight was upgraded              |
| Downgraded            | String                    | Indicates if flight was downgraded            |
| BaggageInsurance      | String                    | baggage insurance                             |
| MaxAllowedBaggage     | String                    | Maximum allowed bags                          |
| BaggageQuantity       | String                    | Number of bags                                |
| BaggageFee            | String                    | Total Baggage Fee                             |
| Arrival               | Port                      | Arrival details for Segment                   |
| Departure             | Port                      | Departure details for Segment                 |
| Seat                  | Seat                      | Seat detail                                   |
| Priority              | Priority                  | Priority detail                               |
| Doc                   | Doc                       | Accompanying document information for travel  |
| Baggage               | Baggage List              | Baggage detail                                |
| Pets                  | Pet List                  | Pet details                                   |
| OtherServices         | OtherService List         | Other services detail                         |
| Attributes            | Map<String, String>       | Additional attributes                         | Standard Index Fields     | Standard index name       | Standard preference record field |
| ---                   | ---                       |                                               | \_airSegmentId            | SegmentId                 |
| \_airBookingRef       | BookingRef                | Baggage data type                             | Standard airSegment Field | Type                      | Description                      |
| ---                   | ---                       | ---                                           |
| Id                    | String                    | Baggage identifier                            |
| TagNumber             | String                    | Baggage tag number                            |
| DepartureDate         | String                    | Departure date                                |
| BaggageType           | String                    | Type of baggage                               |
| Weight                | String                    | Weight of baggage                             |
| Length                | String                    | Length of baggage                             |
| Width                 | String                    | Width of baggage                              |
| Height                | String                    | Height of baggage                             |
| PriorityBagDrop       | String                    | Priority bag drop service                     |
| PriorityBagReturn     | String                    | Priority bag return service                   |
| HandsFreeBaggage      | String                    | Hands-free baggage service                    |
| Fee                   | String                    | Baggage fee                                   |
| IsGateBag             | String                    | Indicates gate check baggage                  |
| IsHeavy               | String                    | Indicates heavy baggage                       | Seat data type            | Standard airSegment Field | Type                             | Description |
| ---                   | ---                       | ---                                           |
| SeatNumber            | String                    | Seat number                                   |
| SeatZone              | String                    | Zone of the seat                              |
| SeatType              | String                    | Type of seat                                  |
| Price                 | String                    | Seat price                                    |
| NeighborFree          | String                    | Indicates if neighboring seat is free         |
| UpgradeAuction        | String                    | Indicates auction upgrade availability        |
| Available             | String                    | Indicates seat availability                   |
| ExtraSeat             | String                    | Indicates extra seat                          |
| AdditionalInformation | String                    | Extra seat information                        | Port data type            | Standard airSegment Field | Type                             | Description |
| ---                   | ---                       | ---                                           |
| Location              | String                    | Location name                                 |
| Code                  | String                    | Airport code                                  |
| Terminal              | String                    | Airport terminal                              |
| Country               | String                    | Airport country                               |
| Date                  | String                    | Date                                          |
| Time                  | String                    | Time                                          |
| EstimatedTime         | String                    | Estimated time                                |
| ScheduledTime         | String                    | Scheduled time                                | Priority data type        | Standard airSegment Field | Type                             | Description |
| ---                   | ---                       | ---                                           |
| TransactionId         | String                    | Transaction identifier                        |
| PriorityServiceType   | String                    | Type of priority service                      |
| LoungeAccess          | String                    | Indicates lounge access                       |
| Price                 | String                    | Priority service price                        |
| AdditionalInformation | String                    | Extra priority information                    | Pet data type             | Standard airSegment Field | Type                             | Description |
| ---                   | ---                       | ---                                           |
| Species               | String                    | Pet species                                   |
| Breed                 | String                    | Pet breed                                     |
| Weight                | String                    | Pet weight                                    |
| WeightUnit            | String                    | Weight unit of measurement                    |
| TransportType         | String                    | Type of pet transport                         | OtherService data type    | Standard airSegment Field | Type                             | Description |
| ---                   | ---                       | ---                                           |
| ServiceType           | String                    | Type of service                               |
| Description           | String                    | Service description                           |
| Price                 | String                    | Service price                                 | Doc data type             | Standard airSegment Field | Type                             | Description |
| ---                   | ---                       | ---                                           |
| DocType               | String                    | Type of document                              |
| DocTypeNeeded         | String                    | Indicates if document is required             |
| Nationality           | String                    | Nationality on document                       |
| DateOfBirth           | String                    | Date of birth                                 |
| AppId                 | String                    | Application identifier                        |
| AgentId               | String                    | Agent identifier                              |
| VerifiedDateTime      | String                    | Document verification time                    |
