Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Account takeover insights

The Account Takeover Insights (ATI) model type identifies fraudulent online activity by detecting if accounts were compromised
through malicious takeovers, phishing, or from credentials being stolen. Account Takeover Insights is a machine learning model that
uses login events from your online business to train the model.

You can embed a trained Account Takeover Insights model within your real time login flow to detect if an account is compromised.
The model assesses a variety of authentication and login types. They include web application logins, API-based authentications, and
single-sign-on (SSO). To use the Account Takeover Insights model, call the [GetEventPrediction](../api/API_GetEventPrediction.md "../api/API_GetEventPrediction.md") API
after a valid login credentials is presented. The API generates a score that quantifies the risk of the account being compromised.
Amazon Fraud Detector uses the score and the rules that you defined to return one or more outcomes for the login events. The outcomes are ones that
you configured. Based on the outcomes you receive, you can take appropriate actions for each login. That is, you can either approve or
challenge the credentials presented for the login. For example, you can challenge the credentials by asking for an account PIN as an additional
verification.

You can also use the Account Takeover Insights model to evaluate account logins asynchronously and take actions on high-risk
accounts. For example, a high-risk account can be added to investigation queue for a human reviewer to determine if further action
needs to be taken, such as suspend the account.

The Account Takeover Insights model is trained using a dataset that contains the historical login events of your business. You
provide this data. You can optionally label the accounts as legitimate or fraudulent. However, this isn’t required to train the model.
The Account Takeover Insights model detects anomalies based on the history of successful logins of an account. It also learns how to
detect anomalies in a user’s behavior that suggest increased risk of an event of malicious account takeover. For example, a user that
typically logs in from the same set of devices and IP addresses. A fraudster typically logs in from a different device and geolocation.
This technique produces a risk score of an activity being anomalous, which typically is a primary characteristic of malicious account takeovers.

Before training an Account Takeover Insights model, Amazon Fraud Detector uses a combination of machine learning techniques to perform data
enrichment, data aggregation, and data transformation . Then, during the training process, Amazon Fraud Detector enriches the raw
data elements that you provide. Examples of raw data elements include IP address and user agent. Amazon Fraud Detector uses these elements to create
additional inputs that describe the login data. These inputs include the device, browser, and geolocation inputs. Amazon Fraud Detector also uses the
login data that you provide to continuously compute aggregated variables that describe the past user behavior. Examples of user
behavior include the number of times that the user signed in from a specific IP address. Using these additional enrichments and
aggregates, Amazon Fraud Detector can generate strong model performance from a small set of inputs from your login events.

The Account Takeover Insights model detects instances where a legitimate account is accessed by a bad actor, regardless of
whether the bad actor is human or a robot. The model produces a single score that indicates the relative risk of account compromise.
Accounts that might have been compromised are flagged as high-risk accounts. You can process high-risk accounts by one of two ways.
Either, you can enforce an additional identity verification. Or, you can send the account to a queue for manual investigation.

## Selecting data source

Account Takeover Insights models are trained on a dataset that’s stored internally, in Amazon Fraud Detector. To store your login events data with Amazon Fraud Detector,
create a CSV file with login events of users. For each event, include login data such as the event timestamp, user ID, IP address, user agent,
and whether the login data is valid. After creating the CSV file, first upload the file to Amazon Fraud Detector, and then use import feature
to store the data. You can then train your model using the stored data. For more information on storing your event dataset with Amazon Fraud Detector see [Store your event data internally with Amazon Fraud Detector](storing-event-data-afd.md "storing-event-data-afd.md")

## Preparing data

Amazon Fraud Detector requires that you provide your user account login data in a comma-separated values (CSV) file that’s encoded in the
UTF-8 format. The first line of your CSV file must contain a file header. The file header consists of event metadata and event variables
that describe each data element. Event data follows the header. Each line in the event data consists of data from a single login event.

For the Accounts Takeover Insights model, you must provide the following event metadata and event variables in the header line of your CSV file.

**Event metadata**

We recommend that you provide the following metadata in your CSV file header. The event metadata must be in uppercase letters.

- EVENT_ID - A unique identifier for the login event.
- ENTITY_TYPE - The entity that performs the login event, such as a merchant or a customer.
- ENTITY_ID - An identifier for the entity performing the login event.
- EVENT_TIMESTAMP - The timestamp when the login event occurred. The timestamp must be in ISO 8601 standard in UTC.
- EVENT_LABEL (recommended) - A label that classifies the event as fraudulent or legitimate. You can use any labels, such as "fraud", "legit", "1", or "0".

###### Note

- Event metadata must be in uppercase letters. It’s case sensitive.
- Labels aren’t required for login events. However, we recommend that you include EVENT_LABEL metadata and provide labels for your login events.
  It’s fine if the labels are incomplete or sporadic. If you provide labels, Amazon Fraud Detector will use them to automatically calculate an Account Takeover Discovery Rate and display
  it in model performance chart and table.

  **Event variables**

For Accounts Takeover Insights model, there are both required (mandatory) variables that you must provide and optional variables.
When you create your variables, make sure to assign the variable to the right variable type. As part of the model training process,
Amazon Fraud Detector uses the variable type that’s associated with the variable to perform variable enrichment and feature engineering.

###### Note

Event variable names must be in lowercase letters. They’re case sensitive.

**Mandatory variables**

The following variables are required for training an Accounts Takeover Insights model.

| Category           | Variable type   | Description                                                                                                                   |
| ------------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IP address         | IP_ADDRESS      | The IP address used in the login event                                                                                        |
| Browser and device | USERAGENT       | The browser, device, and OS used in the login event                                                                           |
| Valid credentials  | VALIDCRED       | Indicates if the credentials that were used for login are valid                                                               | **Optional variables** The following variables are optional for training an Accounts Takeover Insights model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Category           | Type            | Description                                                                                                                   |
| ---                | ---             | ---                                                                                                                           |
| Browser and device | FINGERPRINT     | The unique identifier for a browser or device fingerprint                                                                     |
| Session Id         | SESSION_ID      | The identifier for an authentication session                                                                                  |
| Label              | EVENT_LABEL     | A label that classifies the event as fraudulent or legitimate. You can use any labels, such as "fraud", "legit", "1", or "0". |
| Timestamp          | LABEL_TIMESTAMP | The timestamp when the label was last updated. This is required if EVENT_LABEL is provided.                                   | ###### Note <br>• You can provide any variable names for both mandatory variables optional variables. It’s important that each mandatory and optional variable is assigned to the right variable type. <br>• You can provide additional variables. However, Amazon Fraud Detector won’t include these variables for training an Accounts Takeover Insights model. ## Selecting data Gathering data is an important step to creating your Account Takeover Insights model. As you start to gather your login data, consider the following requirements and recommendations: **Required** <br>• Provide at least 1,500 user account examples, each with at least two associated login events. <br>• Your dataset must cover at least 30 days of login events. You can later specify the specific time range of the events to use to train the model. **Recommended** <br>• Your dataset includes examples of unsuccessful login events. You can optionally label these unsuccessful logins as “fraudulent” or “legitimate.” <br>• Prepare historic data with login events spanning more than six months and include 100K entities. If you don’t have a dataset that already meets the minimum requirements, consider streaming event data to Amazon Fraud Detector by calling the [SendEvent](../api/API_SendEvent.md "../api/API_SendEvent.md") API operation. ## Validating data Before creating your Account Takeover Insights model, Amazon Fraud Detector checks if the metadata and variables you included in your dataset for training the model meet size and format requirements. For more information, see [Dataset validation](create-event-dataset.md#dataset-validation "create-event-dataset.md#dataset-validation"). It also checks for other requirements. If the dataset doesn’t pass validation, model isn’t created. For the model to be successfully created, make sure to fix the data that didn’t pass the validation before you train again. **Common dataset errors** When validating a dataset for training an Account Takeover Insights model, Amazon Fraud Detector scans for these and other issues and throws an error if it encounters one or more of the issues. <br>• CSV file isn’t in the UTF-8 format. <br>• The CSV file header doesn’t contain at least one of the following metadata: `EVENT_ID`, `ENTITY_ID`, or `EVENT_TIMESTAMP`. <br>• The CSV file header doesn’t contain at least one variable of the following variable types: `IP_ADDRESS`, `USERAGENT`, or `VALIDCRED`. <br>• There’s more than one variable that’s associated with the same variable type. <br>• More than 0.1% of values in `EVENT_TIMESTAMP` contains nulls or values other than the supported date and timestamp formats. <br>• The number of days between the first and last event is fewer than 30 days. <br>• More than 10% of variables of the `IP_ADDRESS` variable type are either invalid or null. <br>• More than 50% of variables of the `USERAGENT` variable type contain nulls. <br>• All of the variables of the `VALIDCRED` variable type are set to `false`. |
