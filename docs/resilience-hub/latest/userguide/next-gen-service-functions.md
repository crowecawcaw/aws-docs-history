

# Service functions
<a name="next-gen-service-functions"></a>

**Service functions** are technical subsets of the service topology that represent specific workflows within a service.

For example, an authentication service might have two service functions:
+ **SSO sign-in** – involving the identity provider, session store, and token service.
+ **Registration** – involving the user database, email service, and verification flow.

Service functions help you understand which resources participate in which workflows within a single service. Service functions are identified by the next generation of Resilience Hub during assessment.