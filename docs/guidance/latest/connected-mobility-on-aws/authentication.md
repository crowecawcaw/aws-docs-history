# Authentication and Authorization

The guidance uses Amazon Cognito for user authentication and AWS IAM for service-to-service authorization, providing secure access to the fleet management dashboard and REST APIs.

**Amazon Cognito User Pools**:

Amazon Cognito User Pools manage fleet manager and administrator accounts with support for:

- **User Registration**: Self-service registration with email verification
- **Password Policies**: Configurable password complexity requirements (minimum 8 characters, uppercase, lowercase, numbers, special characters)
- **Multi-Factor Authentication (MFA)**: Optional MFA using SMS or TOTP authenticator apps
- **Account Recovery**: Password reset via email verification codes
- **Custom Attributes**: Store user metadata (fleet_id, role, permissions)
- **User Groups**: Organize users by role (administrators, fleet managers, drivers)

**Cognito Identity Pools**:

Cognito Identity Pools provide temporary AWS credentials for authenticated users to access AWS services:

- **Federated Identities**: Support for social identity providers (Google, Facebook) and SAML 2.0 enterprise identity providers
- **Temporary Credentials**: Short-lived AWS credentials (1 hour default) with automatic rotation
- **IAM Role Mapping**: Different IAM roles for authenticated vs unauthenticated users
- **Fine-Grained Access**: IAM policies control access to specific DynamoDB tables, S3 buckets, and API Gateway endpoints

**Fleet Management Dashboard Authentication**:

The React-based dashboard uses Cognito for user authentication:

1. **User Login**: User enters email and password on login page
2. **Cognito Authentication**: Cognito validates credentials and returns JWT tokens (ID token, access token, refresh token)
3. **Token Storage**: Tokens stored securely in browser session storage (not localStorage for security)
4. **API Requests**: Access token included in Authorization header for all API requests
5. **Token Refresh**: Refresh token used to obtain new access tokens when expired (1 hour default)
6. **Logout**: Tokens cleared from session storage and Cognito session invalidated

**REST API Authentication**:

API Gateway uses Cognito Authorizer to validate JWT tokens:

- **Authorization Header**: Client includes `Authorization: Bearer <access_token>` in request headers
- **Token Validation**: API Gateway validates token signature, expiration, and issuer
- **User Context**: Decoded token claims (user_id, email, groups) passed to Lambda functions
- **Rate Limiting**: Per-user rate limits based on Cognito user_id
- **CORS Configuration**: Configured to allow requests from CloudFront distribution domain

**IAM Roles and Policies**:

Service-to-service authentication uses IAM roles with least privilege:

- **Flink Execution Role**:
  **MSK access: kafka-cluster:Connect, ReadData, WriteData**DynamoDB access: PutItem, GetItem, Query, Scan
  **S3 access: GetObject (JAR files), PutObject (data lake)**CloudWatch Logs: CreateLogStream, PutLogEvents
- **IoT Core Service Role**:
  **MSK access: kafka:GetBootstrapBrokers**Secrets Manager: GetSecretValue (SCRAM credentials)
  \*\*VPC access: CreateNetworkInterface, DescribeNetworkInterfaces
- **Lambda Execution Role**:
  **DynamoDB access: Query, Scan (read-only for API endpoints)**Cognito access: AdminGetUser, ListUsers (user management)
  \*\*CloudWatch Logs: CreateLogStream, PutLogEvents

**Security Best Practices**:

- **Token Expiration**: Access tokens expire after 1 hour, requiring refresh
- **HTTPS Only**: All API requests require TLS 1.2+ encryption
- **CORS Restrictions**: API Gateway only accepts requests from authorized origins
- **Password Policies**: Enforce strong passwords with complexity requirements
- **MFA Enforcement**: Require MFA for administrator accounts
- **Audit Logging**: CloudTrail logs all Cognito and IAM authentication events

**Extensibility**:

- **Social Login**: Add Google, Facebook, or Apple authentication
- **Enterprise SSO**: Integrate with SAML 2.0 identity providers (Okta, Azure AD, Ping Identity)
- **Custom Authentication**: Implement custom authentication flows with Lambda triggers
- **API Keys**: Add API key authentication for machine-to-machine access
- **OAuth 2.0**: Implement OAuth 2.0 authorization code flow for third-party integrations
