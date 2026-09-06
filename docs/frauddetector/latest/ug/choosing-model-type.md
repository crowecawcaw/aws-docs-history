

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Choose a model type
<a name="choosing-model-type"></a>

The following model types are available in Amazon Fraud Detector. Choose a model type that works for your use case. 
+ **Online Fraud Insights**

  The *Online Fraud Insights* model type is optimized to detect fraud when little historical data is available about the entity being evaluated, for example, a new customer registering online for a new account.
+ **Transaction Fraud Insights**

  The *Transaction Fraud Insights* model type is best suited for detecting fraud use cases where the entity that is being evaluated might have a history of interactions that the model can analyze to improve prediction accuracy (for example, an existing customer with history of past purchases).
+ **Account Takeover Insights**

  The *Account Takeover Insights* model type detects if an account was compromised by phishing or another type of attack. The login data of a compromised account, such as the browser and device used at login, is different from the historical login data that’s associated with the account. 