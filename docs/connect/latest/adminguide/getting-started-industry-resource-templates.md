# Getting started with industry resource templates

Connect Customer Customer Profiles provides industry resource templates to help you quickly set up your domain with
calculated attributes, segments, and Profile Explorer layouts tailored to specific
industries.

## Before you begin

Before you enable industry resource templates, make sure you have:

- An Amazon Connect instance with Customer Profiles enabled
- Appropriate permissions to create resources in your Customer Profiles
  domain

## About industry resource templates

When you enable an industry template, Customer Profiles automatically creates the
following resources in your domain:

- Calculated attribute definitions - Pre-defined attributes derived from your
  customer data
- Segment definitions - Customer groupings based on common
  characteristics
- Profile Explorer layouts - Customized dashboard views for visualizing customer
  information

These resources are designed to help you quickly derive value from your customer data
without having to manually create each resource.

## Enable industry resource templates

1. On the Customer Profiles homepage, locate the Industry templates
   section.

   - If this is your first time setting up Customer Profiles, an
     announcement appears at the top of the page.

   ![Banner to enable templates appears if this is your first time using customer profiles.](images/enable-industry-resource-templates-1.png)
   - If you already have resources in your domain, the list of enabled
     templates appears in the Industry templates section.

   ![If you have used customer profiles before, then a list of enabled templates appears in the industry templates section.](images/enable-industry-resource-templates-2.png)

2. To enable a template, choose **Enable a template**.
3. In the **Select template** dropdown, choose the industry that
   best matches your business:

   - **Airline** - For air travel businesses
   - **Hotel** - For hospitality businesses

4. Review the resources that will be created in the **Review
   resources** section.

![Review the resources that will be created.](images/enable-industry-resource-templates-3.png) 5. Choose **Enable template**. 6. Wait for the resources to be created. Make sure to keep the browser tab open
while the resource creation is in progress. 7. Once complete, you'll see a confirmation message and the template will appear
in the Industry templates section with the number of resources created.

![Successful creation banner appears.](images/enable-industry-resource-templates-4.png)

## Resources created by industry templates

### Airline Industry Template

#### Calculated Attributes

The airline template creates calculated attributes across several
categories:

Airline Calculated Attributes| Calculated Attribute Name | Display Name | Description | Object type |
| --- | --- | --- | --- |
| air\_airPreference\_departure\_airport\_last\_occurrence | Preferred departure airport | Returns customer's most recently configured preferred<br>departure airport. | \_airPreference |
| air\_airPreference\_arrival\_airport\_last\_occurrence | Preferred arrival airport | Returns customer's most recently configured preferred arrival<br>airport. | \_airPreference |
| air\_airPreference\_travel\_type\_last\_occurrence | Preferred travel type | Returns customer's most recently configured preferred type of<br>travel. | \_airPreference |
| air\_airPreference\_marketing\_opt\_in\_last\_occurrence | Marketing opt-in preference | Returns customer's most recently configured marketing opt-in<br>setting. | \_airPreference |
| air\_airPreference\_language\_in\_person\_language\_last\_occurrence | Preferred in-person language | Returns customer's most recently preferred language for<br>in-person interactions. | \_airPreference |
| air\_airPreference\_seat\_location\_last\_occurrence | Preferred seat location | Returns customer's most recently selected seat location<br>preference. | \_airPreference |
| air\_airPreference\_home\_airport\_last\_occurrence | Preferred home airport | Returns customer's most recently specified home<br>airport. | \_airPreference |
| air\_airPreference\_dining\_dietary\_restriction\_last\_occurrence | Preferred dietary restriction | Returns customer's most recently specified dietary<br>restriction. | \_airPreference |
| air\_airBookings\_number\_of\_passengers\_average | Average passengers per booking | Returns average number of passengers across customer's<br>bookings. | \_airBooking |
| air\_airBookings\_price\_total\_price\_average | Average booking price | Returns average cost across all customer's bookings. | \_airBooking |
| air\_airBookings\_count | Count of bookings | Returns the count of bookings made by a customer. | \_airBooking |
| air\_airSegments\_flight\_delay\_time\_sum | Total flight delay duration | Returns total length of flight delays experienced by<br>customer. | \_airSegment |
| air\_airSegments\_cancelled\_flights\_count\_30\_days | Cancelled flights in past 30 days | Returns count of customer flights cancelled within the last<br>30 days. | \_airSegment |
| air\_airSegments\_delayed\_flights\_count\_30\_days | Delayed flights in past 30 days | Returns count of customer flights delayed within the last 30<br>days. | \_airSegment |
| air\_airSegments\_completed\_flights\_count\_30\_days | Completed flights in past 30 days | Returns count of customer flights completed within the last<br>30 days. | \_airSegment |
| air\_airSegments\_completed\_flights\_count\_1\_year | Completed flights in past year | Returns count of customer flights completed within the last<br>year. | \_airSegment |
| air\_airSegment\_departure\_date\_last\_occurrence | Last flight departure date | Returns departure date of customer's most recent<br>flight. | \_airSegment |
| air\_airSegments\_miles\_to\_earn\_sum | Total miles flown | Returns sum of all flight distances in miles for a<br>customer. | \_airSegment |
| air\_airSegments\_miles\_to\_earn\_sum\_1\_year | Miles flown in past year | Returns sum of flight miles flown by customer in the past<br>year. | \_airSegment |
| air\_airSegments\_business\_first\_class\_count | Count of premium class flights | Returns count of customer air segments booked as<br>business-class or first-class. | \_airSegment |
| air\_loyalties\_points\_redeemed\_sum | Total loyalty points redeemed | Returns total sum of points redeemed across all customer<br>loyalty programs. | \_loyalty |
| air\_loyalties\_count | Count of loyalty memberships | Returns number of loyalty program memberships held by the<br>customer. | \_loyalty |
| air\_loyalty\_tier\_points\_to\_next\_tier\_last\_occurrence | Points to next tier | Returns customer's most recent record of points needed to<br>reach next loyalty tier. | \_loyalty |
| air\_loyalty\_points\_balance\_last\_occurrence | Current loyalty points balance | Returns customer's most recent loyalty points<br>balance. | \_loyalty |
| air\_loyalty\_membership\_id\_last\_occurrence | Current loyalty membership ID | Returns customer's most recent loyalty membership<br>identifier. | \_loyalty |
| air\_loyalty\_program\_name\_last\_occurrence | Current loyalty program name | Returns customer's most recent loyalty program name. | \_loyalty |
| air\_loyalty\_enrollment\_date\_last\_occurrence | Most recent loyalty enrollment date | Returns customer's most recent loyalty program enrollment<br>date. | \_loyalty |
| air\_loyalty\_tier\_current\_tier\_last\_occurrence | Current loyalty tier | Returns customer's most recent loyalty program tier<br>status. | \_loyalty |
| air\_loyalties\_silver\_gold\_platinum\_tier\_count | Count of premium tier memberships | Returns count of customer loyalty programs with<br>Silver | \_loyalty |
| air\_loyaltyPromotions\_count | Count of loyalty promotions | Returns total number of loyalty promotions received by the<br>customer. | \_loyaltyPromotion |

#### Segments

The airline template creates the following segments:

- [Airline] Marketing subscribers
- [Airline] Customers with cancelled flights in the past 30 days
- [Airline] Customers with delayed flights in the past 30 days
- [Airline] Customers with completed flights in the past 30 days
- [Airline] Dormant members

#### Profile Explorer Layout

A demo profile explorer layout is created with layout name:
`DEMO-Airline-Layout` that consists of the following
widgets:

- Customer details and contact information
- Loyalty program status and points
- Recent bookings and flights
- Customer preferences
- Customer value metrics
- Customer satisfaction indicators

### Hotel Industry Template

#### Calculated Attributes

The hotel template creates calculated attributes across several
categories:

Hotel Calculated Attributes| Calculated Attribute Name | Display Name | Description | Object type |
| --- | --- | --- | --- |
| hotel\_hotelPreference\_location\_room\_type\_last\_occurrence | Preferred room type | Returns customer's most recently configured preferred room<br>type. | \_hotelPreference |
| hotel\_hotelPreference\_cleaning\_time\_last\_occurrence | Preferred cleaning time | Returns customer's most recently configured room cleaning<br>time preference. | \_hotelPreference |
| hotel\_hotelPreference\_location\_view\_last\_occurrence | Preferred room view | Returns customer's most recently configured room view<br>preference. | \_hotelPreference |
| hotel\_hotelPreference\_check\_in\_type\_last\_occurrence | Preferred check-in method | Returns customer's most recently configured check-in method<br>preference. | \_hotelPreference |
| hotel\_hotelPreference\_check\_out\_type\_last\_occurrence | Preferred check-out method | Returns customer's most recently configured check-out method<br>preference. | \_hotelPreference |
| hotel\_hotelPreference\_special\_request\_last\_occurrence | Last special request type | Returns customer's most recently requested special<br>accommodation type. | \_hotelPreference |
| hotel\_hotelPreference\_interest\_name\_of\_interest\_max\_occurrence | Most frequent interest | Returns customer's most frequently expressed interest or<br>amenity preference. | \_hotelPreference |
| hotel\_hotelPreference\_marketing\_opt\_in\_last\_occurrence | Marketing opt-in preference | Returns customer's most recently configured marketing opt-in<br>setting. | \_hotelPreference |
| hotel\_hotelReservations\_number\_of\_nights\_average | Average length of stay | Returns average duration of stay across all customer hotel<br>reservations. | \_hotelReservation |
| hotel\_hotelReservations\_number\_of\_nights\_completed\_sum\_1\_year | Total nights in past year | Returns total nights stayed in the past year across all<br>customer reservations. | \_hotelReservation |
| hotel\_hotelReservations\_number\_of\_nights\_completed\_sum | Total nights stayed | Returns total number of nights stayed across all customer<br>hotel reservations. | \_hotelReservation |
| hotel\_hotelReservation\_room\_type\_name\_last\_occurrence | Last room type booked | Returns customer's most recently booked room type. | \_hotelReservation |
| hotel\_hotelReservation\_channel\_method\_last\_occurrence | Last booking channel used | Returns customer's most recent channel used for hotel<br>reservation. | \_hotelReservation |
| hotel\_hotelReservations\_count | Count of reservations | Returns the count of hotel reservations made by a<br>customer. | \_hotelReservation |
| hotel\_hotelReservations\_total\_amount\_after\_tax\_average | Average reservation spend | Returns average amount spent per hotel reservation after<br>taxes. | \_hotelReservation |
| hotel\_hotelReservations\_total\_amount\_after\_tax\_sum | Total hotel spend | Returns total amount spent across all customer hotel<br>reservations after taxes. | \_hotelReservation |
| hotel\_hotelReservation\_number\_of\_guests\_max\_occurrence | Most common group size | Returns customer's most frequently booked number of guests<br>across all stays. | \_hotelReservation |
| hotel\_hotelReservations\_business\_travel\_count | Count of business trips | Returns count of customer reservations marked as business<br>travel. | \_hotelReservation |
| hotel\_hotelReservations\_missed\_checkin\_count | Count of missed check-ins | Returns count of reservations where customer missed<br>check-in. | \_hotelReservation |
| hotel\_hotelReservation\_cancelled\_count | Count of cancelled reservations | Returns count of hotel reservations that were cancelled by<br>the customer. | \_hotelReservation |
| hotel\_hotelStayRevenues\_amount\_sum | Total revenue generated | Returns total revenue generated from all customer hotel<br>stays. | \_hotelStayRevenue |
| hotel\_hotelStayRevenues\_amount\_average | Average revenue per stay | Returns mean revenue amount calculated across all customer<br>stays. | \_hotelStayRevenue |
| hotel\_hotelStayRevenues\_amount\_maximum | Highest revenue amount | Returns largest single revenue amount generated from any<br>customer stay. | \_hotelStayRevenue |
| hotel\_hotelStayRevenue\_revenue\_type\_max\_occurrence | Most common revenue source | Returns most frequent type of revenue generated across<br>customer hotel stays. | \_hotelStayRevenue |
| hotel\_loyalties\_points\_redeemed\_sum | Total loyalty points redeemed | Returns total sum of points redeemed across all customer<br>loyalty programs. | \_loyalty |
| hotel\_loyalties\_count | Count of loyalty memberships | Returns number of loyalty program memberships held by the<br>customer. | \_loyalty |
| hotel\_loyalty\_tier\_points\_to\_next\_tier\_last\_occurrence | Points to next tier | Returns customer's most recent record of points needed to<br>reach next loyalty tier. | \_loyalty |
| hotel\_loyalty\_points\_balance\_last\_occurrence | Current loyalty points balance | Returns customer's most recent loyalty points<br>balance. | \_loyalty |
| hotel\_loyalty\_membership\_id\_last\_occurrence | Current loyalty membership ID | Returns customer's most recent loyalty membership<br>identifier. | \_loyalty |
| hotel\_loyalty\_program\_name\_last\_occurrence | Current loyalty program name | Returns customer's most recent loyalty program name. | \_loyalty |
| hotel\_loyalty\_enrollment\_date\_last\_occurrence | Most recent loyalty enrollment date | Returns customer's most recent loyalty program enrollment<br>date. | \_loyalty |
| hotel\_loyalty\_tier\_current\_tier\_last\_occurrence | Current loyalty tier | Returns customer's most recent loyalty program tier<br>status. | \_loyalty |
| hotel\_loyalties\_silver\_gold\_platinum\_tier\_count | Count of premium tier memberships | Returns count of customer loyalty programs with<br>Silver | \_loyalty |
| hotel\_loyaltyPromotions\_count | Count of loyalty promotions | Returns total number of loyalty promotions received by the<br>customer. | \_loyaltyPromotion |

#### Segments

The hotel template creates segments such as:

- [Hotel] Preference Marketing Subscribers
- [Hotel] Solo travelers
- [Hotel] Couple or pair travelers
- [Hotel] Family or group travelers
- [Hotel] Customers with upcoming reservation in 30 days

#### Profile Explorer Layout

A customized layout that displays:

- Customer details and contact information
- Room preferences
- Stay history
- Revenue information
- Loyalty status

## Disable industry templates

You can disable an industry template to remove the resources it created from your
domain. To disable a template:

1. On the Customer Profiles homepage, locate the Industry templates
   section.
2. Find the template you want to disable and choose **Disable**
   action.
3. Review the confirmation message and choose **Confirm** to
   disable the template.

###### Important

When you disable a template, all resources created by that template will be
deleted from your domain. If any of these resources are used in Customer Segments,
Outbound Campaigns, or Contact Flows, disabling the template might impact them.

Before disabling a template, review the resources in use to understand the
potential impact.

## Troubleshooting

Troubleshooting Industry Templates| Error | Recommendation |
| --- | --- |
| Template resources failed to create | 1. Check that you have the necessary permissions to create<br>resources in your domain.<br>2. Verify that you haven't reached the limit for calculated<br>attributes or segments in your domain.<br>3. Try enabling the template again. It will only attempt to<br>create resources that don't already exist. |
| Created resources don't appear in Profile Explorer | 1. Refresh your browser.<br>2. Verify that you have the necessary Security Profiles<br>permissions to view the resources.<br>3. Check that the resources were successfully created in the<br>Industry templates section. |
| Unable to enable multiple templates | Each domain can have multiple industry templates enabled. If you're<br>experiencing issues, check that you haven't reached the resource limits<br>for your domain. |
| Need to delete template resources | Currently, the Getting Started feature does not provide a way to<br>automatically delete all resources created by a template. You can<br>manually delete individual resources through their respective management<br>pages. |

## Next steps

After enabling an industry template, you can:

- Navigate to the Profile Explorer to see your new layout in action
- View and Edit calculated attributes to better fit your specific needs
- Manage customer segments in Amazon Connect
- Edit Profile Explorer Layout based on your business requirements
- Integrate external applications with Amazon Connect Customer Profiles to start
  populating profiles
