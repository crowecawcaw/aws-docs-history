# CM-S06 Customer experience

management

Insights from vehicle data help provide a personalized in-cabin experience, which can
also be portable to other vehicles. Vehicle Manufacturers can also use such data to predict
customer's needs at different touch points throughout the vehicle lifecycle and provide a more
seamless experience to address those needs.

## User stories

**CM-S06-UC01 Driver experience:** By monitoring inside and
outside the vehicle, vehicle manufacturers can recommend changes to improve their customer’s
driving experience and safety. Vehicle manufacturers can also provide customized
infotainment options based on operator’s previous behavior. Allow the driver to take their
profile to other vehicles they own or rent, subject to their approval and affirmative
consent.

**CM-S06-UC02 Contact center:** Automakers need omni-channel
customer service infrastructure that streamlines the customer support process and makes it
simple for agents to resolve customer inquiries faster.

**CM-S06-UC03 Emergency response:** Vehicle drivers would like
to automatically receive help from emergency services should the vehicle experience an
accident.

**CM-S06-UC04 Retention, renewal, and churn:** Predict the
customer propensity to renew their subscription and create a personalized marketing
campaign.

**CM-S06-UC05 Service experience:** Improve vehicle service
experience based on data-driven analytics and machine learning to help OEMs build innovative
applications. For example, if the connected vehicle data shows a trend of extreme tread
wear, then the system can recommend a tire replacement on the infotainment screen, provide a
capability to shop for new tires and schedule a service appointment with a few clicks.

## Reference architecture

![Reference architecture diagram for customer experience management.](images/customer-experience-refarch-a.png)
_Customer experience management reference architecture_

**Figure 6: CM-S06-a Customer experience management reference
architecture**

![Reference architecture diagram for customer experience management.](images/customer-experience-refarch-b.png)
_Customer experience management reference architecture_

**Figure 7: CM-S06-b: Customer experience management reference
architecture**

1. Gather customer interaction and sentiment from source systems such as clickstreams,
   call center logs, vehicle sensor data, social sentiment etc.
2. Ingesting data across customer touchpoints into marketing data lake using variety
   of protocols.
3. Provide rich experience in the car, lifelike conversational services for vehicle
   breakdown, emergencies, vehicle-related questions, notifications, and concierge
   services. Vehicle manufacturers can use speech analytics powered by machine learning to
   access live call transcripts, understand customer sentiment, and identify call reasons
   in near-real time.
4. Transform raw data into consumption ready data using purpose-built data processing
   components and transformation libraries.
5. Analytics layer natively integrated with consumption ready data for quality and
   trend analysis. Customer sentiments can be analyzed using Contact Lens for Amazon
   Connect. Amazon Comprehend can also be used to perform post call analysis to gain further
   insights about the customer call.
6. For convenience and concierge services, use Amazon Alexa features. For example, an
   electric vehicle driver can use voice commands to learn the best route that will provide
   minimum charging time while enabling the driver to enjoy their favorite food while they
   wait.
7. Activate multiple customer channels such as mobile push, voice, and email for
   targeted marketing communications.
8. The companion application provides real time vehicle information, personalization
   and push notifications.
9. Use AWS IoT Device Management to implement OTA management through AWS IoT jobs data and use AWS IoT
   Fleet Indexing to manage state, connectivity, and device violations and to organize,
   investigate, and troubleshoot your fleet of devices.
