# Best practices for OpenAPI schema definition for custom plugins

While application programming interfaces (APIs) have traditionally been used by
developers to integrate with external applications, today APIs are increasingly being
used by generative AI-powered assistants, such as Amazon Q Business custom
plugins. However, its important to note that APIs being used with AI assistants may
require design optimizations that were not critical for traditional application
integrations. Following the best practices below will help Amazon Q Business to
maximize the accuracy and improve efficiency when resolving end user requests.

###### Topics

- [Optimizing OpenAPI schema accuracy](#plugins-api-schema-accuracy "#plugins-api-schema-accuracy")
- [Best practices for OpenAPI Schema names](#plugins-api-schema-names "#plugins-api-schema-names")
- [Best practices for OpenAPI Schema descriptions](#plugins-api-schema-descriptions "#plugins-api-schema-descriptions")
- [Best practices for JSON input schemas](#plugins-api-schema-json-input "#plugins-api-schema-json-input")
- [Other important considerations for OpenAPI specifications](#plugins-api-schema-misc "#plugins-api-schema-misc")
- [Example of API Schema optimization](#plugins-api-schema-optimization "#plugins-api-schema-optimization")

## Optimizing OpenAPI schema accuracy

To create a custom plugin, you need to create or edit an OpenAPI schema outlining
the different API actions you want to enable for your custom plugin. Once the custom
plugin is deployed, Amazon Q Business will process an end user prompt and use
the OpenAPI schema to dynamically determine the appropriate APIs to call to
accomplish the user’s goal. Therefore, the OpenAPI schema definition has a big
impact on API selection accuracy.

The following are the OpenAPI schema sections you need to optimize to maximize the
accuracy of your Amazon Q Business plugins:

- **Names** – Names for operation IDs,
  parameters, object schema property keys, title in info section, and
  more.
- **Descriptions** – Descriptions for
  operations, parameters, schemas, and more.
- **JSON schemas** – JSON schemas for API
  inputs (schemas defined in parameters and request body). Within these
  schemas, important information includes the data type of each schema and
  format information (for example, date/date-time for ISO-8601 date strings),
  as well as names and descriptions mentioned above.

In the next sections, we outline how you can maximize the accuracy of your custom
plugin by following best practices for your OpenAPI schema parameters.

## Best practices for OpenAPI Schema names

- Names and IDs should be human-readable, descriptive, and unambiguous while
  being as concise as possible.
- Operation IDs provide important signals for understanding the function of
  each operation. Though not required, it is recommended to add
  `operationIds` to your API schema. The following outlines
  some Operation ID naming best practices:
  - Avoid noun-only `operationIds`, like
    `contacts`. Instead, prefix operation names with
    descriptive verbs like `get`, `find`,
    `search`, `create`, `update`,
    and `delete`. For example,
    `getContacts`.
  - Ensure `operationIds` meaningfully relate to the
    function of the operation. Avoid including `operationIds`
    with meaningless suffixes/prefixes, like `search_1` and
    `search_2`. If multiple operations perform similar
    functions, but differ only by inputs, consider creating IDs like
    `searchByName` or `searchByEmail`, or even
    merging these operations.
  - Avoid adding long, redundant prefixes to names. For example, avoid
    `contactsPlugin.getContacts` and
    `contactsPlugin.createContact`. Instead, use
    `getContacts` and `createContact`.

- Names of input request body properties and parameters are important for
  determining the role and purpose of each input needed for invoking an
  operation. The following outlines some input request naming best
  practices:
  - Avoid non-descriptive parameter names like `id`.
    Instead include a descriptive noun, like
    `contactId`.
  - It’s not necessary to include information that is redundant with
    the JSON data type of the input. For example, avoid using
    `recipientEmailsArray` and instead just use
    `recipientEmails`.

- Be consistent with parameter names. Generally, parameters and response
  properties with the same name should mean the same thing across all
  operations in your schema. The following outlines some parameter naming best
  practices:
  - Avoid using different names for parameters with the same meaning.
    For example, `start_date` in one API and
    `begin_date` in another API if they mean the same
    thing.
  - Ensure parameter names and property names in responses are
    consistent with each other. For example, if an API returns
    `begin_date`, then also use the name
    `begin_date` in the input parameters if they have the
    same meaning.

## Best practices for OpenAPI Schema descriptions

- Descriptions should be self-contained, providing sufficient guidance for
  how and when to use the operation or parameter they describe. The following
  outlines some description creation best practices:
  - Operation descriptions should describe what the operation does,
    including when, when not, and how to use it.
  - Avoid verbose descriptions. Parameter descriptions should
    concisely describe their purpose and how they impact the behavior of
    the operation. For example, rather than write “this field accepts an
    ISO-8601 date, which is of the format YYYY-MM-DD”, assign date to
    the format field.
  - Concise explanations are generally more useful than
    examples.
  - Make dependencies between operations explicit in the description.
    If an operation always requires another operation to be called first
    (such as, populating an input parameter from the other operation’s
    outputs), make this clear in the description of the operation or
    parameter.

- Use descriptions only where there is ambiguity or missing context. Avoid
  adding descriptions that provide no additional information. Restrict the
  description to information needed to use the API for the use cases Amazon Q Business custom plugin is intended to handle.
- Descriptions should not reference external links/URLs. Amazon Q Business custom plugins may not be able to access these.
- Avoid referencing operations by their _path_ or
  _verb_. Instead use their operation ID when referring
  to other operations in descriptions.
- Avoid referencing schema components or API paths (except dependency
  `operationIds`) in the description. Ensure that descriptions
  are self-contained. As an exception to this, descriptions may reference
  dependency operations by their `operationIds` but should avoid
  providing specific usage examples of the operation. The following outlines
  some referencing best practices:
  - Don’t refer to operations by their API paths (e.g.
    `/api/v1/timeoff/requests`). Instead, use
    `operationIds` to refer to operations in
    descriptions. For example, `GetTimeOffRequests`.
  - Don’t refer to schema components like
    `#/components/schemas/TimeOffRequest`.
  - If examples are necessary, describe them in abstract terms. “For
    example, use `{operationId}` to do `{X}`” or
    “Use `{operationId}` when the end user asks
    for...”.
  - Internally, Amazon Q Business may use generate API calls
    differently than described in the OpenAPI schema. So, including
    usage examples may not always be helpful.

## Best practices for JSON input schemas

- Simpler interfaces will lead to more efficient, consistent, and accurate
  plugin usage from Amazon Q Business. Thus, having fewer input
  parameters of lower complexity is best.
- Keep the total number of parameter schemas per operation low. Keeping the
  total number of parameter schemas to 10 at most, but less than 4 on average,
  will give the best results. Having more parameters may result in slower
  responses because Amazon Q Business custom plugins will need to fill
  out each field.
- Avoid including unnecessary optional input parameters. For example, for
  search APIs with many parameters for filtering results, use the most
  informative/important filters. Or, split into multiple operations to search
  by alternate criteria.
- Avoid structurally complex/nested inputs when possible. The following
  outlines some input parameter structure best practices:
  - **Instead of**
    `{"start": {"type": "object", "properties": {"date": {...},
 "time": {...}}, "end": {...}}`
    **input**
    `{"start_date": {...}, "start_time": {...}, ..., "end_time":
 {...}}`.
  - Avoid schemas containing array types, which are not supported. For
    example, schemas such as `{"type": "array", "items":
{"string"}}` are not supported..
  - Avoid circular references (`$ref` inside of
    `$ref`). Circular references can occur in nested
    structures when the same reference (`$ref`) appears
    inside of its de-referenced value. Although these are valid OpenAPI
    specifications, Amazon Q Business custom plugin may not
    reliably resolve these recursive definitions.
  - Avoid composition keywords (`allOf`, `not`,
    `oneOf`, or `anyOf` ), which are not
    supported

- Use standard values in the format field for string parameters. For
  example, `date-time` or `date` for capturing ISO-8601
  dates/times.

## Other important considerations for OpenAPI specifications

- Never expose sensitive information in the API schema or API outputs. If
  information should not be exposed to the end user, do not include it in your
  API specification or use an API that produces such outputs.
- If it is undesirable for an Amazon Q Business custom plugin to
  reference certain information in the API schemas to the end user, you can
  use instructions in the operation descriptions to help discourage this.
  However, you should not rely on this mechanism for highly sensitive
  information.
- Only include essential information in API responses. Redundant or
  excessively verbose information will reduce the efficiency of an Amazon Q Business custom plugin.
- Limit paginated search results explicitly, particularly if each result
  returned is large/complex. Large API responses may result in slower
  responses for end users. Consider setting guidance or limits in the
  description of the parameter (for example, set to five at most).
- Only 2XX responses may be shared with Amazon Q Business custom
  plugin end users. 4xx and 5xx responses will not be shared with end users.
  If you want to expose specific errors from the API, consider using a 2XX
  code for such errors. Ensure you include information that is appropriate to
  share with the end user.
- The OpenAPI specification should be self-contained. Ensure that the set of
  API operations described in the schema support complete use cases without
  relying on APIs not defined or other plugins.

## Example of API Schema optimization

This section shows you an example of an API schema before and after our best
practices are applied. The example API is used for managing Paid Time Off (PTO)
requests for employees and supports two operations: checking the status of requests
(with `api.V1.TimeOffRequest`) and making new requests (with
`api.V1.RequestTimeOff`).

The following is the example unoptimized API Schema:

```
openapi: 3.0.3
info:
  # title is too long
  title: API for PTO Request Management
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /api/v1/timeoff/requests:
    get:
      # operation ID is ambiguous (is it to get a time off request or make one?) and contains unnecessary details ("api.V1")
      operationId: example.api.V1.TimeOffRequest
      # description is not self-contained (references an external link) and does not describe what the API returns or how to use it.
      description: Existing requests for the authenticated user. See the docs <a href=https://example.com>here</a> for more details.
      parameters:
        - name: type
          in: path
          # description does not include what a "type" is
          description: type to filter by
          required: false
          schema:
            type: string
        - name: status
          in: path
          # description does not include what a "status" is
          description: status to filter by
          required: false
          schema:
            type: string
        - name: start
          in: path
          # description is ambiguous
          description: start of range to include
          required: false
          schema:
            type: string
            # no formatting information is provided, e.g. `format: date`
        - name: end
          in: path
          # description is ambiguous
          description: end of range to include
          required: false
          schema:
            type: string
            # no formatting information is provided, e.g. `format: date`
        - name: limit
          in: path
          # guidance should be provided on how many results to return by default, e.g. less than 5
          description: limit on the number of requests to return
          required: false
          schema:
            type: integer
        - name: page
          in: path
          description: specific page of results to return if results are paginated
          required: false
          schema:
            type: integer
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/TimeOffRequests"
  /api/v1/timeoff/request:
    post:
      # operation ID is ambiguous (is it to get a time off request or make one?) and contains unnecessary details ("api.V1")
      operationId: example.api.V1.RequestTimeOff
      # description is not self-contained (references an external link) and ambiguous.
      description: Make a request for the authenticated user. <a href=https://example.com/>API docs</a> for more details.-->
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                # this field adds unnecessary nesting to the inputs. Separate `start_date`, and `end_date` fields would be preferred
                range:
                  # missing a description, non-descriptive field name
                  type: object
                  properties:
                    start:
                      # start of what?
                      type: string
                      format: date
                    end:
                      # end of what?
                      type: string
                      format: dat
                  required:
                    - start
                    - end
                type:
                  description: the type of request to make, e.g. `Personal` or `Vacation`
                  type: string
                  # use enums where possible
                note:
                  description: a short note describing the reason for the request
                  type: string
      responses:
        "201":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/TimeOffRequest"
components:
  schemas:
    TimeOffRequest:
      type: object
      properties:
        # this ID is not necessary for the end user (and is used nowhere else in the API), consider removing
        id:
          type: string
        status:
          # no descriptions provided
          type: string
        type:
          type: string
        start:
          type: string
        end:
          type: string
        note:
          type: string
        duration:
          type: integer
        # this ID is not necessary for the end user (and is used nowhere else in the API), consider removing
        approver_id:
          type: string
        approver_display_name:
          type: string
    TimeOffRequests:
      type: array
      items:
        $ref: "#/components/schemas/TimeOffRequest"
```

Applying the best practices defined above, there are multiple updates that should
be made to this API schema to get the best results when using Amazon Q Business custom plugins.

First, based on guidance to make names concise, descriptive and unambiguous, we’ll
make a few updates to the operation IDs, parameter names, and schema title:

- Change `example.api.V1.RequestTimeOff` to
  `CreateTimeOffRequest`
- Change `example.api.V1.RequestTimeOff` to
  `GetTimeOffRequests`
- Change the schema title in the info section from `API for PTO Request
Management` to `TimeOff`

If you are able to change the API itself, we’d also like you to fix parameter
names. Change parameters named `type` and `status` to
`request_type` and `request_status` respectively

Next, based on best practices for descriptions, we’ll make the following
updates:

- Modify the description of `/api/v1/timeoff/requests` and
  `/api/v1/timeoff/request` to make them self-contained (remove
  URL) and describe what they do and how to use them. For example:
  - Change `Existing requests for the authenticated user. See the
docs <a href=https://example.com>here</a> for more
details.` to `Return existing time off requests
(including information like the current approval status,
dates/days used) for the authenticated user.`
  - Change `Make a request for the authenticated user. See <a
href=https://example.com/>API docs</a> for more
details.` to `Create a new time off request of a
particular type (e.g. Personal or Vacation) for the
authenticated user based on a start and end date
(inclusive)`.

- Add descriptions for ambiguous parameters. For example:
  - For the end date of a request, add a description: `Last day
for the request (inclusive) in ISO-8601 format (for example,
YYYY-MM-DD)`.
  - For the start date, add a description: `First day of the
request in ISO-8601 format (e.g. YYYY-MM-DD)`.

- Based on guidance to limit paginated search results explicitly, we’ll add
  a description to the `limit` field in
  `GetTimeOffRequests`. For example, `Limit on the number
of requests to return. Limit to 5 unless otherwise
instructed`.

Finally, we’ll apply changes based on the API input schema best practices:

- Assuming we have control over the API implementation, we’d like to apply
  guidance on avoiding unnecessary nesting. For this, we can convert
  `range` (which contains start and end dates) to two top-level
  properties called `startDate` and `endDate`.
- Following guidance to use standard format fields, we’ll add format:
  `date` to start/end date fields (assuming we are expecting
  standard date formats).

After making corrections, we end up with a vastly improved API specification that
will maximize the Amazon Q Business custom plugin accuracy and efficiency in
resolving user requests.

The following is the API Schema after we've added optimization fixes:

```
openapi: 3.0.3
info:
  title: TimeOff
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /api/v1/timeoff/requests:
    get:
      operationId: GetTimeOffRequests
      description: Return existing time off requests (including information like the current approval status, dates/days used) for the authenticated user
      parameters:
        - name: request_type
          in: path
          required: false
          schema:
            type: string
            enum:
              - Vacation
              - Personal
              - JuryDuty
              - Sick
        - name: request_status
          in: path
          required: false
          schema:
            type: string
            enum:
              - Approved
              - Pending
              - Cancelled
        - name: start
          in: path
          description: Include requests ending on or after this date
          required: false
          schema:
            type: string
            format: date
        - name: end
          in: path
          description: Include requests starting before this date
          required: false
          schema:
            type: string
            format: date
        - name: limit
          in: path
          description: Limit on the number of requests to return. Limit to 5 unless otherwise instructed
          schema:
            type: integer
        - name: page
          in: path
          description: Specific page of results to return if results are paginated
          required: false
          schema:
            type: integer
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/TimeOffRequests"
  /api/v1/timeoff/request:
    post:
      operationId: CreateTimeOffRequest
      description: Create a new time off request for the authenticated user
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                startDate:
                  description: First day of the request in ISO-8601 format (e.g. YYYY-MM-DD)
                  type: string
                  format: date
                endDate:
                  description: Last day for the request (inclusive) in ISO-8601 format (e.g. YYYY-MM-DD)
                  type: string
                  format: date
                request_type:
                  description: The type of request to make, either `Personal`, `Vacation`, `Sick` or `JuryDuty`
                  type: string
                  enum:
                    - Personal
                    - Vacation
                    - Sick
                    - JuryDuty
                note:
                  description: A short (one to two sentence) note describing the reason for the request
                  type: string
              required:
                - startDate
                - endDate
                - request_type
                - note
      responses:
        "201":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/TimeOffRequest"
components:
  schemas:
    TimeOffRequest:
      type: object
      properties:
        # this ID is not necessary for the end user (and is used nowhere else in the API), consider removing
        request_id:
          type: string
        request_status:
          description: the current status of the request, either `Pending`, `Approved`, or `Cancelled`
          type: string
          enum:
            - Pending
            - Approved
            - Cancelled
        request_type:
          type: string
        start:
          description: the start date of the request
          type: string
        end:
          description: the last date of the request (inclusive)
          type: string
        note:
          description: brief note describing the reason for the request
          type: string
        duration:
          description: the number of working days used for the request
          type: integer
        approver_display_name:
          description: the name of the person of who approved the request
          type: string
    TimeOffRequests:
      type: array
      items:
        $ref: "#/components/schemas/TimeOffRequest"
```
