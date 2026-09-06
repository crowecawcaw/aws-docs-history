

# Managing WhatsApp Flows in AWS End User Messaging Social
<a name="managing-flows"></a>

WhatsApp Flows enable businesses to create interactive, multi-screen experiences that users can complete without leaving WhatsApp. Flows support data collection, form submissions, and complex UI components like text inputs, radio buttons, checkboxes, date pickers, and dropdown menus. Use Flows to build experiences such as appointment booking, lead generation forms, customer surveys, and shopping flows.

With AWS End User Messaging Social, you can manage your WhatsApp Flows directly through the AWS End User Messaging Social console or by using the AWS End User Messaging Social API. You can create, update, publish, preview, deprecate, and delete Flows without needing to use the Meta console or Meta's APIs directly.

Flows are associated with your WhatsApp Business Account (WABA). Each Flow is defined by a JSON schema that describes its screens, components, and logic. For more information about the Flow JSON schema, see [Flow JSON](https://developers.facebook.com/docs/whatsapp/flows/reference/flowjson) in the *Meta WhatsApp Business Platform documentation*.

**Note**  
The current release supports static Flows where all screens, components, and navigation logic are defined in the Flow JSON. Flows with endpoints that exchange data between screens and a business server (the `endpoint_uri` and `data_exchange` capabilities) are planned for an upcoming release. For more information, see [Limitations and considerations](managing-flows-limitations.md).

## Key concepts
<a name="managing-flows-concepts"></a>

Flow  
An interactive, multi-screen experience defined by a JSON schema that users complete within WhatsApp.

Flow JSON  
The JSON definition that describes the Flow's screens, components, and logic. Maximum size is 10 MB. We recommend using JSON version 7.3.

Flow category  
A classification that describes the business purpose of the Flow. Categories include: Sign Up, Sign In, Appointment Booking, Lead Generation, Contact Us, Customer Support, Survey, Shopping, and Other.

Flow status  
The lifecycle state of a Flow. See [Understanding Flow status](managing-flows-status.md).

Flow token  
A unique identifier you provide when sending a Flow to track the session. The token is returned in the Flow response webhook when the user completes the Flow.