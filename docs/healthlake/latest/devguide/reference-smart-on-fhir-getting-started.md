# Getting started with

SMART on FHIR

The following topics describe how to get started with SMART on FHIR authorization for
AWS HealthLake. They include the resources you must provision in your AWS account, the creation
of a SMART on FHIR enabled HealthLake data store, and an example of how a SMART on FHIR client
application interacts with an authorization server and a HealthLake data store.

###### Topics

- [Setting up resources for SMART on FHIR](#smart-on-fhir-resources "#smart-on-fhir-resources")
- [Client application workflow for
  SMART on FHIR](#smart-on-fhir-client-app-workflow "#smart-on-fhir-client-app-workflow")

## Setting up resources for SMART on FHIR

The following steps define how SMART on FHIR requests are handled by HealthLake and the
resources needed for them to succeed. The following elements work together in a workflow
to make a SMART on FHIR request:

- **The end-user**: Generally, a patient or
  clinician using a third-party SMART on FHIR application to access data in a
  HealthLake data store.
- **The SMART on FHIR application (referred to as the client
  application)**: An application that wants to access data found in
  HealthLake data store.
- **The authorization server**: An OpenID Connect
  compliant server that is able to authenticate users and issue access
  tokens.
- **The HealthLake data store**: A SMART on FHIR enabled
  HealthLake data store that uses a Lambda function to respond to FHIR REST requests
  which provide a bearer token.

For these elements to work together, you must create the following resources.

###### Note

We recommend creating your SMART on FHIR enabled HealthLake data store after you've set
up the authorization server, defined the necessary [scopes](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md") on it, and created
a AWS Lambda function to handle [token](reference-smart-on-fhir-token-validation.md "reference-smart-on-fhir-token-validation.md")
introspection.

###### 1. Set up an authorization server endpoint

To use the SMART on FHIR framework you need to set up an third-party authorization
server that can validate FHIR REST requests made on a data store. For more
information, see [HealthLake authentication requirements
for SMART on FHIR](reference-smart-on-fhir-authentication.md "reference-smart-on-fhir-authentication.md").

###### 2. Define scopes on your authorization server to control HealthLake data store access

levels

The SMART on FHIR framework uses OAuth scopes to determine what FHIR resources an
authenticated request has access to and to what extent. Defining scopes are a way to
design for least-privilege. For more information, see [SMART on FHIR OAuth 2.0 scopes
supported by HealthLake](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md").

###### 3. Set up an AWS Lambda function capable of performing token introspection

A FHIR REST request sent by the client application on a SMART on FHIR enabled
data store contains a JSON Web Token (JWT). For more information, see [Decoding a
JWT](reference-smart-on-fhir-token-validation.md "reference-smart-on-fhir-token-validation.md").

###### 4. Create a SMART on FHIR enabled HealthLake data store

To create a SMART on FHIR HealthLake data store you need to provide an
`IdentityProviderConfiguration`. For more information, see [Creating a HealthLake data store](managing-data-stores-create.md "managing-data-stores-create.md").

## Client application workflow for

SMART on FHIR

The following section explains how to launch a client application and make a
successful FHIR REST request on an HealthLake data store within the context of
SMART on FHIR.

###### 1. Make a `GET` request to Well-Known Uniform Resource Identifier

using client application

A SMART enabled client application must make a `GET` request to find
the authorization endpoints of your HealthLake data store. This is done via a Well-Known
Uniform Resource Identifier (URI) request. For more information, see [Fetching the SMART on FHIR
Discovery Document](reference-smart-on-fhir-discovery-document.md "reference-smart-on-fhir-discovery-document.md").

###### 2. Request access and scopes

The client application uses the authorization endpoint of the authorization
server, so that the user can login. This process authenticates the user. Scopes are
used to define what FHIR resources in your HealthLake data store a client application
can access. For more information, see [SMART on FHIR OAuth 2.0 scopes
supported by HealthLake](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md").

###### 3. Access tokens

Now that the user has been authenticated, a client application receives a JWT
access token from the authorization server. This token is provided when the client
application sends a FHIR REST request to HealthLake. For more information, see [Token
validation](reference-smart-on-fhir-token-validation.md "reference-smart-on-fhir-token-validation.md").

###### 4. Make a FHIR REST API request on SMART on FHIR enabled HealthLake data store

The client application can now send a FHIR REST API request to a HealthLake data
store endpoint using the access token provided by the authorization server. For more
information, see [Making a FHIR REST API request on a
SMART-enabled HealthLake data store](reference-smart-on-fhir-request-example.md "reference-smart-on-fhir-request-example.md").

###### 5. Validate the JWT access token

To validate the access token sent in the FHIR REST request, use a Lambda
function. For more information, see [Token validation using
AWS Lambda](reference-smart-on-fhir-token-validation.md "reference-smart-on-fhir-token-validation.md").
