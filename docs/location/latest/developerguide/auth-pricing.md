

# Pricing
<a name="auth-pricing"></a>

The cost of using Amazon Location Service authentication depends on the API requests your applications make. API key management operations are charged under the Service Resources pricing category, with a free tier allowance. The API calls made *using* an authentication method (such as retrieving map tiles or geocoding addresses) are charged based on the underlying service. The unit price for each request depends on the service used and the response fields requested. For pricing information, see the [Amazon Location Service pricing page](https://aws.amazon.com/location/pricing/).

There are three authentication methods, each with different cost implications: **API keys**, **Amazon Cognito**, and **IAM**.

## API keys
<a name="auth-pricing-apikeys"></a>

API key management operations are charged under the **Service Resources** pricing category. All key management operations count as service resource requests, including read operations:
+ `CreateKey`, `DescribeKey`, `UpdateKey`, `DeleteKey`, `ListKeys`

The Amazon Location Service Free Tier includes a monthly allowance of service resource requests. Beyond the free tier, you are charged per request. For current pricing and free tier details, see the [Amazon Location Service pricing page](https://aws.amazon.com/location/pricing/).

You are also charged for the API calls made *using* an API key based on the pricing for the underlying service. For example:
+ When a client uses an API key to call `GetTile`, you are charged at the Maps tile request rate.
+ When a client uses an API key to call `SearchText` with `additionalFeature = Core`, you are charged at the Places Core pricing bucket rate.
+ When a client uses an API key to call `CalculateRoutes`, you are charged at the Routes pricing bucket rate determined by the travel mode and features requested.

The pricing is the same whether requests are authenticated with an API key, Amazon Cognito, or IAM. The authentication method does not affect the per-request price.

## Amazon Cognito
<a name="auth-pricing-cognito"></a>

When you use Amazon Cognito to authenticate requests to Amazon Location Service, you pay for both the Amazon Cognito service and the Amazon Location Service API requests:
+ **Amazon Cognito identity pool costs** – Free tier available for monthly active users. Beyond the free tier, you pay for each monthly active user.
+ **Amazon Location Service API request costs** – Charged based on the service used (Maps, Places, Routes, Geofences, or Trackers) at the same rate as API key or IAM authenticated requests.

For Amazon Cognito pricing details, see the [Amazon Cognito pricing page](https://aws.amazon.com/cognito/pricing/).

## IAM
<a name="auth-pricing-iam"></a>

AWS Identity and Access Management is provided at no additional charge. When using IAM credentials (including AWS STS temporary credentials) to authenticate requests to Amazon Location Service, you pay only for the Amazon Location Service API requests at the standard service rate.

## Per-service pricing
<a name="auth-pricing-service"></a>

Regardless of the authentication method used, you are charged for Amazon Location Service API requests based on the service. For detailed pricing for each service, including pricing buckets and what triggers each tier, see:
+ [Maps pricing](maps-pricing.md)
+ [Places pricing](places-pricing.md)
+ [Routes pricing](routes-pricing.md)
+ [Trackers pricing](trackers-pricing.md)
+ [Geofences pricing](geofence-price.md)
+ [Jobs pricing](jobs-pricing.md)

For a complete pricing overview and free tier information, see the [Amazon Location Service pricing page](https://aws.amazon.com/location/pricing/).