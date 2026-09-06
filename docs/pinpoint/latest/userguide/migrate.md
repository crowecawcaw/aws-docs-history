

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Amazon Pinpoint end of support
<a name="migrate"></a>

After careful consideration, we decided to end support for Amazon Pinpoint, effective October 30, 2026. Amazon Pinpoint will no longer accept new customers beginning May 20, 2025. As an existing customer with an account signed up for the service before May 20, 2025, you can continue to use Amazon Pinpoint features. After October 30, 2026, you will no longer be able to use Amazon Pinpoint.

Today, customers use Amazon Pinpoint either for its engagement capabilities (endpoints, segments, campaigns, journeys, and analytics), or its messaging channel APIs (SMS, MMS, push, WhatsApp, and text to voice messaging capabilities). We have created offboarding plans for both sets of customers.

**What this means for you**

If you are using Amazon Pinpoint engagement features (endpoints, segments, campaigns, journeys, and analytics), we recommend you to migrate to Connect Customer proactive engagement solutions (e.g., [Amazon Connect Customer outbound campaigns](https://aws.amazon.com/connect/outbound/) and [Amazon Connect Customer Customer Profiles](https://aws.amazon.com/connect/customer-profiles/)) to drive personalized, timely engagement across channels with unified performance tracking and the ability to manage inbound (e.g., customer support) and outbound (e.g., proactive communications) using one unified application. If you are using events collection and mobile analytics, we recommend to use [Amazon Kinesis](https://aws.amazon.com/kinesis).

Amazon Pinpoint communication channels (SMS, MMS, push, WhatsApp, and text to voice messaging capabilities) were renamed in Q3 2024 as [AWS End User Messaging](https://aws.amazon.com/end-user-messaging), and will continue to serve developer needs for message delivery with customers. Use of APIs related to SMS, Voice, Mobile Push, OTP and Phone Number Validate will not be affected by this change. If you are using Amazon Pinpoint to send email, we recommend you migrate to [Amazon Simple Email Service](https://aws.amazon.com/ses) (SES). If you are using email deliverability dashboard in Amazon Pinpoint, we now offer email deliverability dashboard functionality in [Amazon Simple Email Service Virtual Deliverability Manager](https://docs.aws.amazon.com/ses/latest/dg/vdm-global-deliverability.html).

**Topics**
+ [Choosing the right migration path](#choosing-migration-path)
+ [Migration steps: Transition features for Amazon Pinpoint engagement](#migration-steps)
+ [Offboarding steps: Export data to 3rd party](#offboarding-steps)
+ [Summary](#migration-summary)
+ [Additional resources](#migration-additional-resources)

## Choosing the right migration path
<a name="choosing-migration-path"></a>

Amazon Connect Customer outbound campaigns and AWS End User Messaging (EUM) with Amazon Simple Email Service serve different use cases. Before you begin migration, review your workload characteristics to determine the right destination.

**Consider Amazon Connect Customer outbound campaigns if your workload includes:**
+ Personalized customer engagement across voice, SMS, email, and WhatsApp
+ AI-driven contact strategies such as predictive dialing, progressive dialing, or customer segmentation
+ Agent-assisted outbound calling with real-time routing
+ Coordinated inbound and outbound engagement in a single application

**Consider AWS End User Messaging and Amazon Simple Email Service if your workload includes:**
+ Throughput requirements that exceed Amazon Connect Customer outbound campaign limits or needs for guaranteed delivery SLAs (see [Service quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html))
+ No requirement for agent involvement or AI-driven decisioning
+ No requirement for customer segmentation, contact orchestration, or contact limit management

For workloads that combine both patterns, you can use Amazon Connect Customer for agent-assisted engagement and AWS End User Messaging with Amazon Simple Email Service for high-volume transactional delivery.

For automated migration assistance, see [Pronetx migration tooling](https://aws.amazon.com/marketplace/pp/prodview-zzpgnprbmmnj6) on AWS Marketplace.

## Migration steps: Transition features for Amazon Pinpoint engagement
<a name="migration-steps"></a>

### Customers seeking engagement features
<a name="customer-seeking-engagement-features"></a>

To use the proactive engagement features of Connect Customer, including segments, message templates, campaigns, journeys, analytics, please follow this guide to migrate Amazon Pinpoint engagement capabilities to Connect Customer.

#### Migrate endpoints and segments
<a name="migrate-endpoints-and-segments"></a>

Amazon Pinpoint Endpoints can be modeled as Connect Customer Customer Profiles. Customer Profiles allows you to combine multiple endpoints into a single profile, allowing up to 3 email addresses and 4 phone numbers to be modeled as a single Profile. To migrate your endpoints, you can

1. Create an Amazon Pinpoint Segment with no filters, effectively encompassing all your endpoints.

1. Export that Segment to an S3 bucket or to your local machine.

1. Upload your transformed endpoints to Customer Profiles and use Customer Profiles’ S3 connector to [create a Data Integration](https://docs.aws.amazon.com/connect/latest/adminguide/integrate-external-apps-customer-profiles.html) into Customer Profiles.

In case you want to aggregate endpoints under a single Customer Profile, you can parse the downloaded Amazon Pinpoint segment to collect the email addresses and phone numbers under a single profile. Here is a sample Python script to read the exported file in JSON format and created the Profiles which can be imported to Customer Profiles.

```
from collections import defaultdict
import json

def process_pinpoint_endpoints(input_file, output_file):
    # Dictionary to store grouped endpoints by user ID
    grouped_endpoints = defaultdict(list)

    endpoints = []

    # Read the input file
    with open(input_file, 'r') as file:
        for line in file:
            endpoints.append(json.loads(line))


    # Group endpoints by user ID
    for endpoint in endpoints:
        user_id = endpoint.get('User', {}).get('UserId')
        if user_id:
            grouped_endpoints[user_id].append(endpoint)

    # Convert grouped endpoints to Customer Profiles format
    # We will assume the userId is stored as an AccountNumber
    # since the AccountNumber can be queried
    customer_profiles = []
    for user_id, user_endpoints in grouped_endpoints.items():
        profile = {
            'AccountNumber': user_id,
            'Attributes': {},
            'Address': {}
        }
        
        phone_numbers = set()
        email_addresses = set()
        
        output_dict = {}

        for endpoint in user_endpoints:
            # Extract attributes
            attributes = endpoint.get('Attributes', {})
            for key, value_list in attributes.items():
                if len(value_list) == 1:
                    output_dict[key] = value_list[0]
                else:
                    for i, item in enumerate(value_list):
                        output_dict[f"{key}_{i}"] = item

            demographics = endpoint.get('Demographic')
            for key, value in demographics.items():
                attributes[f"Demographic_{key}"] = value
            
            location = endpoint.get('Location', {})
            profile['Address']['City'] = location['City']
            profile['Address']['Country'] = location['Country']
            profile['Address']['PostalCode'] = location['PostalCode']
            profile['Address']['County'] = location['Region']
            profile['Attributes']['Latitude'] = location['Latitude']
            profile['Attributes']['Longitude'] = location['Longitude']
            
            metrics = endpoint.get('Metrics', {})
            for key, value in metrics.items():
                profile['Attributes'][f"Metrics_{key}"] = str(value)
            
            user = endpoint.get('User', {})
            user_attributes = user.get('UserAttributes', {})
            for key, value_list in user_attributes.items():
                if len(value_list) == 1:
                    output_dict[key] = value_list[0]
                else:
                    for i, item in enumerate(value_list):
                        output_dict[f"UserAttributes.{key}_{i}"] = item

            profile['Attributes'].update(output_dict)
            
            # Extract phone number
            address = endpoint.get('Address')
            if (endpoint.get('ChannelType') == 'SMS' or endpoint.get('ChannelType') == 'VOICE') and address:
                phone_numbers.add(address)

            # Extract email address
            if endpoint.get('ChannelType') == 'EMAIL' and address:
                email_addresses.add(address)
        
        # Assigning the phone numbers to the different parameters in the Customer Profile
        for i, phone_number in enumerate(phone_numbers):
            if i == 0:
                profile['PhoneNumber'] = phone_number
            elif i == 1:
                profile['HomePhoneNumber'] = phone_number
            elif i == 2:
                profile['MobilePhoneNumber'] = phone_number
            elif i == 3:
                profile['BusinessPhoneNumber'] = phone_number
            else:
                profile['Attributes'][f"PhoneNumber_{i}"] = phone_number
                
        # Assigning the email addresses to the different parameters in the Customer Profile
        for i, email_address in enumerate(email_addresses):
            if i == 0:
                profile['EmailAddress'] = email_address
            elif i == 1:
                profile['PersonalEmailAddress'] = email_address
            elif i == 2:
                profile['BusinessEmailAddress'] = email_address
            else:
                profile['Attributes'][f"EmailAddress_{i}"] = email_address
        
        customer_profiles.append(profile)

    # Write the output to a file
    with open(output_file, 'w') as f:
        json.dump(customer_profiles, f, indent=2)

    print(f"Processed {len(endpoints)} endpoints into {len(customer_profiles)} customer profiles.")

# Example usage
input_file = 'pinpoint_endpoints.json'
output_file = 'customer_profiles.json'
process_pinpoint_endpoints(input_file, output_file)
```

#### Migrate channel configurations
<a name="migrate-channel-configurations"></a>

Follow the onboarding steps to enable [SMS](https://docs.aws.amazon.com/connect/latest/adminguide/setup-sms-messaging.html) and [email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html) communications in Connect Customer.

#### Migrate templates
<a name="migrate-templates"></a>

Templates in Connect Customer use the same message rendering engine (Handlebars) as Amazon Pinpoint. However, the attribute placeholders are represented differently.

1. You can use our existing Amazon Pinpoint APIs to fetch a template (for example, [get-email-template](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-email-template.html), [get-sms-template](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-sms-template.html)). Alternatively, you can follow [this guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-edit.html) to edit a template so you can copy its content.

1. After fetching the template, update its placeholders. For example, your Amazon Pinpoint templates earlier used a placeholder like `{{User.UserAttributes.PurchaseHistory}}`. These can now be changed to `{{Attributes.Customer.Attributes.PurchaseHistory}}`.

1. Next, create templates in Q in Connect Customer using the  [create-message-template](https://docs.aws.amazon.com/cli/latest/reference/qconnect/create-message-template.html) API or using [this guide](https://docs.aws.amazon.com/connect/latest/adminguide/create-message-templates1.html) to create message templates.

To map your attributes, follow the mappings you did earlier when you mapped Endpoints to Profiles, prefixed with `Attributes.Customer`.

#### Migrate campaigns
<a name="migrate-campaigns"></a>

For every campaign, we recommend you use the [get-campaign](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-campaign.html) API to fetch its definition, and then recreate it in Connect Customer using the [campaign creation guide](https://docs.aws.amazon.com/connect/latest/adminguide/how-to-create-campaigns.html).

#### Migrate journeys
<a name="migrate-journeys"></a>

Journeys are now supported in Amazon Connect Customer outbound campaigns. You can recreate your Amazon Pinpoint journeys using Amazon Connect Customer campaign orchestration features. Use the [get-journey](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-journey.html) API to fetch your journey definitions, and then recreate them using the [Amazon Connect Customer journey creation guide](https://docs.aws.amazon.com/connect/latest/adminguide/create-a-multi-step-and-multi-channel-journey.html).

### Events collection and mobile analytics customers
<a name="events-collectgion-and-mobile-analytics-customers"></a>

#### Amplify SDK customers
<a name="amplify-sdk-customers"></a>

If you use Amplify SDK to send events to Amazon Pinpoint for updating Endpoints, triggering campaign or journeys, or analyzing your application’s usage, you can migrate to using Kinesis. Using Kinesis, you can stream events to a compute platform of your choice to them send updates to Customer Profiles, which can update the application user’s profile and trigger Connect Customer campaigns.

#### Put-Events customers
<a name="put-events-customers"></a>

If you only use Amazon Pinpoint to stream events from your web/mobile application to a Kinesis stream, you can now use Amplify SDK to directly stream the events to Kinesis.

#### Unavailable features
<a name="unavailable-features"></a>

As of now, the following Amazon Pinpoint engagement features are not available in Connect Customer.
+ In-App Messaging
+ PUSH (GCM, APNS, BAIDU, etc.) notifications are not natively supported in campaigns. However, you can send push notifications through journeys using a Lambda action with Amazon Connect Customer push templates.
+ Custom Channel is available for journeys but not for campaigns.

## Offboarding steps: Export data to 3rd party
<a name="offboarding-steps"></a>

If you would like to delete all Amazon Pinpoint data, feel free to simply delete the application using the [delete-app](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/delete-app.html) API. Following this, please delete any unused message templates using [this guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-delete.html) on deleting templates.

Alternatively, if you want to extract all your resources and store them, follow the steps below.

### Endpoints
<a name="migration-endpoints"></a>

To offboard your endpoints, you can
+ Create an Amazon Pinpoint Segment with no filters, effectively encompassing all your endpoints.
+ Export that Segment to an S3 bucket or to your local machine.

### Segments, campaigns, and journeys
<a name="segments-campaigns-journeys"></a>



To offboard your segments, campaigns, and journeys, use our APIs or our UI to retrieve them. For this, you can use our [get-segment](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-segment.html), [get-campaign](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-campaign.html), or [get-journey](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-journey.html) APIs.

### Message templates
<a name="migration-message-templates"></a>

To offboard your templates, you can use [list-templates](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/list-templates.html) API followed by the channel-specific APIs -
+ [get-email-template](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-email-template.html)
+ [get-in-app-template](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-in-app-template.html)
+ [get-push-template](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-push-template.html)
+ [get-sms-template](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-sms-template.html)

### Amazon Pinpoint and mobile analytics
<a name="pinpoint-and-mobile-analytics"></a>

To offboard your events and KPIs from Amazon Pinpoint Analytics or Mobile Analytics you can use the following options:

1. To export future raw events before migration, customers can onboard to event data stream.

1. Customers can export the KPIs for past 3 months using the following commands:
   + [get-application-date-range-kpi](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-application-date-range-kpi.html)
   + [get-journey-date-range-kpi](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-journey-date-range-kpi.html)
   + [get-campaign-date-range-kpi](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-campaign-date-range-kpi.html)
   + [get-journey-execution-activity-metrics](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-journey-execution-activity-metrics.html)
   + [get-journey-execution-metrics](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-journey-execution-metrics.html)
   + [get-journey-run-execution-activity-metrics](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-journey-run-execution-activity-metrics.html)
   + [get-journey-run-execution-metrics](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-journey-run-execution-metrics.html)

For customers who need to delete Mobile Analytics applications as part of their migration, you can use the following Python script. This script uses AWS Signature Version 4 to authenticate with the Mobile Analytics API and requires Python 3.11 or later ([Download Python 3.11](https://www.python.org/downloads/release/python-3110/)).

1. Save the following script as `delete_mobile_analytics_application.py`.

   ```
   # Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #
   # This file is licensed under the Apache License, Version 2.0 (the "License").
   # You may not use this file except in compliance with the License. A copy of the
   # License is located at
   #
   # http://aws.amazon.com/apache2.0/
   #
   # This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
   # OF ANY KIND, either express or implied. See the License for the specific
   # language governing permissions and limitations under the License.
   #
   # ABOUT THIS PYTHON SAMPLE: This sample is part of the AWS General Reference 
   # Signing AWS API Requests top available at
   # https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html
   #
   
   # AWS Version 4 signing example
   
   # Delete Mobile Analytics application
   
   # See: http://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
   # This version makes a DELETE request and passes the signature
   # in the Authorization header.
   import sys, os, base64, datetime, hashlib, hmac
   import requests # pip install requests
   import argparse
   
   # Parse command line arguments
   parser = argparse.ArgumentParser(description='Delete a Mobile Analytics application')
   parser.add_argument('--appId', type=str, help='Mobile Analytics application ID to be deleted', required=True)
   args = parser.parse_args()
   
   # ************* REQUEST VALUES *************
   delimiter = "/"
   method = 'DELETE'
   service = 'mobileanalytics'
   host = 'mobileanalytics.us-east-1.amazonaws.com'
   region = 'us-east-1'
   appId = args.appId  # Use the appId from command line arguments
   endpoint = 'https://mobileanalytics.us-east-1.amazonaws.com/2016-07-01/apps' + delimiter + appId
   request_parameters = ''
   
   
   # Function for signing. Refer the AWS documentation below for more details.
   # http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python
   def sign(key, msg):
       return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
   
   
   # Function for computing signature key. Refer the AWS documentation below for more details.
   # http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python.
   def getSignatureKey(key, dateStamp, regionName, serviceName):
       kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
       kRegion = sign(kDate, regionName)
       kService = sign(kRegion, serviceName)
       kSigning = sign(kService, 'aws4_request')
       return kSigning
   
   
   # Read AWS access key from environment variables or configuration file. Best practice is NOT
   # to embed credentials in code.
   access_key = os.environ.get('AWS_ACCESS_KEY_ID')
   secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
   session_token = os.environ.get('AWS_SESSION_TOKEN')
   if access_key is None or secret_key is None:
       print('No access key is available.')
       sys.exit()
   
   # Create a date for headers and the credential string
   t = datetime.datetime.now(datetime.UTC)
   amzdate = t.strftime('%Y%m%dT%H%M%SZ')
   datestamp = t.strftime('%Y%m%d')  # Date w/o time, used in credential scope
   
   # ************* TASK 1: CREATE A CANONICAL REQUEST *************
   # http://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html
   
   # Step 1 is to define the verb (GET, POST, etc.)--already done with defining "method" variable above.
   
   # Step 2: Create canonical URI--the part of the URI from domain to query 
   # string (use '/' if no path)
   canonical_uri = '/2016-07-01/apps' + delimiter + appId
   
   # Step 3: Create the canonical query string. In this example (a DELETE request),
   # request parameters are in the query string. Query string values must
   # be URL-encoded (space=%20). The parameters must be sorted by name.
   # For this example, the query string is pre-formatted in the request_parameters variable.
   canonical_querystring = request_parameters
   
   # Step 4: Create the canonical headers and signed headers. Header names
   # must be trimmed and lowercase, and sorted in code point order from
   # low to high. Note that there is a trailing \n.
   canonical_headers = 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n'
   
   # Step 5: Create the list of signed headers. This lists the headers
   # in the canonical_headers list, delimited with ";" and in alpha order.
   # Note: The request can include any headers; canonical_headers and
   # signed_headers lists those that you want to be included in the 
   # hash of the request. "Host" and "x-amz-date" are always required.
   signed_headers = 'host;x-amz-date'
   
   # Step 6: Create payload hash (hash of the request body content). For GET
   # requests, the payload is an empty string ("").
   payload_hash = hashlib.sha256(request_parameters.encode('utf-8')).hexdigest()
   
   # Step 7: Combine elements to create canonical request
   canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
   
   # ************* TASK 2: CREATE THE STRING TO SIGN*************
   # Match the algorithm to the hashing algorithm you use, either SHA-1 or
   # SHA-256 (recommended)
   algorithm = 'AWS4-HMAC-SHA256'
   credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
   string_to_sign = algorithm + '\n' + amzdate + '\n' + credential_scope + '\n' + hashlib.sha256(
       canonical_request.encode('utf-8')).hexdigest()
   
   # ************* TASK 3: CALCULATE THE SIGNATURE *************
   # Create the signing key using the function defined above.
   signing_key = getSignatureKey(secret_key, datestamp, region, service)
   
   # Compute signature by invoking hmac.new method by passing signingkey, string_to_sign
   signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
   
   # ************* TASK 4: ADD SIGNING INFORMATION TO THE REQUEST *************
   # The signing information can be either in a query string value or in 
   # a header named Authorization. This code shows how to use a header.
   # Create authorization header and add to request headers
   authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature
   
   # The request can include any headers, but MUST include "host", "x-amz-date", 
   # and (for this scenario) "Authorization". "host" and "x-amz-date" must
   # be included in the canonical_headers and signed_headers, as noted
   # earlier. Order here is not significant.
   # Python note: The 'host' header is added automatically by the Python 'requests' library.
   headers = {
       'x-amz-date': amzdate,
       'accept': 'application/hal+json',
       'content-type': 'application/json; charset=UTF-8',
       'Authorization': authorization_header}
   
   if session_token:
       headers['X-Amz-Security-Token'] = session_token
   
   # ************* SEND THE REQUEST *************
   request_url = endpoint + '?' + canonical_querystring
   
   print('\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++')
   print('Request URL = ' + request_url)
   print('Request Headers = ', headers)
   
   r = requests.delete(request_url, data=request_parameters, headers=headers)
   
   print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
   print('Response code: %d\n' % r.status_code)
   print(r.text)
   ```

1. Ensure you have valid AWS credentials set as environment variables.

1. Run the script with your Mobile Analytics application ID:

   ```
   python delete_mobile_analytics_application.py --appId {{<YOUR_MOBILE_ANALYTICS_APP_ID>}}
   ```

This script makes a `DELETE` request to the Mobile Analytics API to remove the specified application. Make sure to run this for each Mobile Analytics application you need to delete.

**Note**  
Active Mobile Analytics customers can continue to ingest events through `putEvents` API and view them in Amazon Pinpoint until the Amazon Pinpoint end of support date.

## Summary
<a name="migration-summary"></a>

Organizations with at least one Amazon Pinpoint account, can continue to use Amazon Pinpoint engagement features, including segments, campaigns, journeys, analytics and email  until October 30, 2026, when support for the service will end.

## Additional resources
<a name="migration-additional-resources"></a>

The following additional resources are available:
+ [Amazon Pinpoint website](https://aws.amazon.com/pinpoint/)
+ [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html)
+ [Amazon Connect Customer outbound campaigns](https://aws.amazon.com/connect/outbound/)
+ [Amazon Connect Customer Customer Profiles](https://aws.amazon.com/connect/customer-profiles/)
+ [Amazon Kinesis website](https://aws.amazon.com/kinesis/)
+ [AWS End User Messaging](https://aws.amazon.com/end-user-messaging/)
+ [Amazon Simple Email Service (SES)](https://aws.amazon.com/ses/)

If you need assistance or have feedback, contact [AWS Support](https://aws.amazon.com/support/).