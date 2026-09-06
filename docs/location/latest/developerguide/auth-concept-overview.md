

# Authentication overview
<a name="auth-concept-overview"></a>

Amazon Location Service supports three authentication methods, each designed for different use cases. They differ in the APIs they can access, complexity, flexibility, and intended audience.

**API keys**  
A plain text token that grants read-only access to Maps, Places, and Routes APIs without requiring user authentication. API keys are the simplest way to enable anonymous access in client-side applications such as web pages and mobile apps.

**Amazon Cognito**  
An AWS identity service that provides temporary, scoped credentials for both authenticated and unauthenticated users. Amazon Cognito supports all Amazon Location Service APIs and enables richer authorization policies, including access to Geofences and Trackers.

**AWS Identity and Access Management (IAM)**  
The AWS access management service for server-side applications, internal tools, and administrative operations. IAM provides full control over permissions using policies, roles, and temporary credentials via AWS STS.