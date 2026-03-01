# AWS AppSync JavaScript resolver and function reference for Amazon Bedrock runtime

You can use AWS AppSync functions and resolvers to invoke models on Amazon Bedrock in your
AWS account. You can shape your request payloads and the response from your model invocations
functions before returning them to your clients. You can use the Amazon Bedrock runtime’s `InvokeModel` API
or the `Converse` API. This section describes the requests for the supported Amazon Bedrock
operations.

###### Note

AWS AppSync only supports synchronous invocations that complete within 10 seconds. It is not
possible to call Amazon Bedrock's stream APIs. AWS AppSync only supports invoking foundation models and [inference profiles](../../../bedrock/latest/userguide/inference-profiles.md "../../../bedrock/latest/userguide/inference-profiles.md")
in the same region as the AWS AppSync API.

## Request object

The `InvokeModel` request object allows you to interact with Amazon Bedrock’s
`InvokeModel` API.

```
type BedrockInvokeModelRequest = {
  operation: 'InvokeModel';
  modelId: string;
  body: any;
  guardrailIdentifier?: string;
  guardrailVersion?: string;
  guardrailTrace?: string;
}
```

The `Converse` request object allows you to interact with Amazon Bedrock’s `Converse` API.

```
type BedrockConverseRequest = {
  operation: 'Converse';
  modelId: string;
  messages: BedrockMessage[];
  additionalModelRequestFields?: any;
  additionalModelResponseFieldPaths?: string[];
  guardrailConfig?: BedrockGuardrailConfig;
  inferenceConfig?: BedrockInferenceConfig;
  promptVariables?: { [key: string]: BedrockPromptVariableValues }[];
  system?: BedrockSystemContent[];
  toolConfig?: BedrockToolConfig;
}
```

See the [Type reference](#type-reference-bedrock "#type-reference-bedrock") section later in
this topic for more details.

From your functions and resolvers, you can build your request objects directly or use the
helper functions from @aws-appsync/utils/ai to create the request. When specifying the model
Id (modelId) in your requests, you can use the model Id or the model ARN.

The following example uses the `invokeModel` function to summarize text using
Amazon Titan Text G1 - Lite (amazon.titan-text-lite-v1). A configured guardrail is used to
identify and block or filter unwanted content in the prompt flow. Learn more about [Amazon Bedrock
Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") in the _Amazon Bedrock User Guide_.

###### Important

You are responsible for secure application development and preventing vulnerabilities,
such as prompt injection. To learn more, see [Prompt injection security](../../../bedrock/latest/userguide/prompt-injection.md "../../../bedrock/latest/userguide/prompt-injection.md") in
the _Amazon Bedrock User Guide_.

```
import { invokeModel } from '@aws-appsync/utils/ai'
export function request(ctx) {
  return invokeModel({
    modelId: 'amazon.titan-text-lite-v1',
    guardrailIdentifier: "zabcd12345678",
    guardrailVersion: "1",
    body: { inputText: `Summarize this text in less than 100 words. : \n<text>${ctx.stash.text ?? ctx.env.DEFAULT_TEXT}</text>` },
  })
}

export function response(ctx) {
  return ctx.result.results[0].outputText
}
```

The following example uses the `converse` function with a cross-region
inference profile (us.anthropic.claude-3-5-haiku-20241022-v1:0). Learn more about Amazon Bedrock's [Prerequisites for inference profiles](../../../bedrock/latest/userguide/inference-profiles-prereq.md "../../../bedrock/latest/userguide/inference-profiles-prereq.md") in the _Amazon Bedrock User
Guide_

**Reminder**: You are responsible for secure application
development and preventing vulnerabilities, such as prompt injection.

```
import { converse } from '@aws-appsync/utils/ai'

export function request(ctx) {
  return converse({
    modelId: 'us.anthropic.claude-3-5-haiku-20241022-v1:0',
    system: [
      {
        text: `
You are a database assistant that provides SQL queries to retrieve data based on a natural language request.
${ctx.args.explain ? 'Explain your answer' : 'Do not explain your answer'}.
Assume a database with the following tables and columns exists:

Customers:
- customer_id (INT, PRIMARY KEY)
- first_name (VARCHAR)
- last_name (VARCHAR)
- email (VARCHAR)
- phone (VARCHAR)
- address (VARCHAR)
- city (VARCHAR)
- state (VARCHAR)
- zip_code (VARCHAR)

Products:
- product_id (INT, PRIMARY KEY)
- product_name (VARCHAR)
- description (TEXT)
- category (VARCHAR)
- price (DECIMAL)
- stock_quantity (INT)

Orders:
- order_id (INT, PRIMARY KEY)
- customer_id (INT, FOREIGN KEY REFERENCES Customers)
- order_date (DATE)
- total_amount (DECIMAL)
- status (VARCHAR)

Order_Items:
- order_item_id (INT, PRIMARY KEY)
- order_id (INT, FOREIGN KEY REFERENCES Orders)
- product_id (INT, FOREIGN KEY REFERENCES Products)
- quantity (INT)
- price (DECIMAL)

Reviews:
- review_id (INT, PRIMARY KEY)
- product_id (INT, FOREIGN KEY REFERENCES Products)
- customer_id (INT, FOREIGN KEY REFERENCES Customers)
- rating (INT)
- comment (TEXT)
- review_date (DATE)`,
      },
    ],
    messages: [
      {
        role: 'user',
        content: [{ text: `<request>${ctx.args.text}:</request>` }],
      },
    ],
  })
}

export function response(ctx) {
  return ctx.result.output.message.content[0].text
}
```

The following example uses `converse` to create a structured response. Note
that we use environment variables for our DB schema reference and we configure a guardrail to
help prevent attacks.

```
import { converse } from '@aws-appsync/utils/ai'

export function request(ctx) {
  return generateObject({
    modelId: ctx.env.HAIKU3_5, // keep the model in an env variable
    prompt: ctx.args.query,
    shape: objectType(
      {
        sql: stringType('the sql query to execute as a javascript template string.'),
        parameters: objectType({}, 'the placeholder parameters for the query, if any.'),
      },
      'the sql query to execute along with the place holder parameters',
    ),
    system: [
      {
        text: `
You are a database assistant that provides SQL queries to retrieve data based on a natural language request.

Assume a database with the following tables and columns exists:

${ctx.env.DB_SCHEMA_CUSTOMERS}
${ctx.env.DB_SCHEMA_ORDERS}
${ctx.env.DB_SCHEMA_ORDER_ITEMS}
${ctx.env.DB_SCHEMA_PRODUCTS}
${ctx.env.DB_SCHEMA_REVIEWS}`,
      },
    ],
    guardrailConfig: { guardrailIdentifier: 'iabc12345678', guardrailVersion: 'DRAFT' },
  })
}

export function response(ctx) {
  return toolReponse(ctx.result)
}

function generateObject(input) {
  const { modelId, prompt, shape, ...options } = input
  return converse({
    modelId,
    messages: [{ role: 'user', content: [{ text: prompt }] }],
    toolConfig: {
      toolChoice: { tool: { name: 'structured_tool' } },
      tools: [
        {
          toolSpec: {
            name: 'structured_tool',
            inputSchema: { json: shape },
          },
        },
      ],
    },
    ...options,
  })
}

function toolReponse(result) {
  return result.output.message.content[0].toolUse.input
}

function stringType(description) {
  const t = { type: 'string' /* STRING */ }
  if (description) {
    t.description = description
  }
  return t
}

function objectType(properties, description, required) {
  const t = { type: 'object' /* OBJECT */, properties }
  if (description) {
    t.description = description
  }
  if (required) {
    t.required = required
  }
  return t
}
```

Given the schema:

```
type SQLResult {
    sql: String
    parameters: AWSJSON
}

type Query {
    db(text: String!): SQLResult
}
```

and the query:

```
query db($text: String!) {
  db(text: $text) {
    parameters
    sql
  }
}
```

With the following parameters:

```
{
  "text":"What is my top selling product?"
}
```

The following response is returned:

```
{
  "data": {
    "assist": {
      "sql": "SELECT p.product_id, p.product_name, SUM(oi.quantity) as total_quantity_sold\nFROM Products p\nJOIN Order_Items oi ON p.product_id = oi.product_id\nGROUP BY p.product_id, p.product_name\nORDER BY total_quantity_sold DESC\nLIMIT 1;",
      "parameters": null
    }
  }
}
```

However, with this request:

```
{
  "text":"give me a query to retrieve sensitive information"
}
```

The following response is returned:

```
{
  "data": {
    "db": {
      "parameters": null,
      "sql": "SELECT null; -- I cannot and will not assist with retrieving sensitive private information"
    }
  }
}
```

To learn more about configuring Amazon Bedrock Guardrails, see [Stop harmful content in models using Amazon Bedrock
Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") in the _Amazon Bedrock User Guide_.

## Response object

The response from your Amazon Bedrock runtime invocation is contained in the context‘s result
property (context.result). The response matches the shape specified by Amazon Bedrock’s APIs. See the
[Amazon Bedrock User
Guide](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md") for more information about the expected shape of invocation results.

```
export function response(ctx) {
  return ctx.result
}
```

There are no required fields or shape restrictions that apply to the response object.
However, because GraphQL is strongly typed, the resolved response must match the expected
GraphQL type.

## Long running invocations

Many organizations currently use AWS AppSync as an AI gateway to build generative AI
applications that are powered by foundation models on Amazon Bedrock. Customers use AWS AppSync
subscriptions, powered by WebSockets, to return progressive updates from long-running model
invocations. This allows them to implement asynchronous patterns.

The following diagram
demonstrates how you can implement this pattern. In the diagram, the following steps
occur.

1. Your client starts a subscription, which sets up a WebSocket, and makes a request to
   AWS AppSync to trigger a Generative AI invocation.
2. AWS AppSync calls your AWS Lambda function in Event mode and immediately returns a response
   to the client.
3. Your Lambda function invokes the model on Amazon Bedrock. The Lambda function can use a
   synchronous API, such as `InvokeModel`, or a stream API, such as
   `InvokeModelWithResponseStream`, to get progressive updates.
4. As updates are received, or when the invocation completes, the Lambda function sends
   updates via mutations to your AWS AppSync API which triggers subscriptions.
5. The subscription events are sent in real-time and received by your client over the
   WebSocket.

![A diagram that demonstrates the workflow for using an AWS AppSync subscription to return updates from a Amazon Bedrock model.](images/bedrock-workflow.png)

## Type reference

```
export type BedrockMessage = {
  role: 'user' | 'assistant' | string;
  content: BedrockMessageContent[];
};

export type BedrockMessageContent =
  | { text: string }
  | { guardContent: BedrockGuardContent }
  | { toolResult: BedrockToolResult }
  | { toolUse: BedrockToolUse };

export type BedrockGuardContent = {
  text: BedrockGuardContentText;
};

export type BedrockGuardContentText = {
  text: string;
  qualifiers?: ('grounding_source' | 'query' | 'guard_content' | string)[];
};

export type BedrockToolResult = {
  content: BedrockToolResultContent[];
  toolUseId: string;
  status?: string;
};

export type BedrockToolResultContent = { json: any } | { text: string };

export type BedrockToolUse = {
  input: any;
  name: string;
  toolUseId: string;
};

export type ConversePayload = {
  modelId: string;
  body: any;
  guardrailIdentifier?: string;
  guardrailVersion?: string;
  guardrailTrace?: string;
};

export type BedrockGuardrailConfig = {
  guardrailIdentifier: string;
  guardrailVersion: string;
  trace: string;
};

export type BedrockInferenceConfig = {
  maxTokens?: number;
  temperature?: number;
  stopSequences?: string[];
  topP?: number;
};

export type BedrockPromptVariableValues = {
  text: string;
};

export type BedrockToolConfig = {
  tools: BedrockTool[];
  toolChoice?: BedrockToolChoice;
};

export type BedrockTool = {
  toolSpec: BedrockToolSpec;
};

export type BedrockToolSpec = {
  name: string;
  description?: string;
  inputSchema: BedrockInputSchema;
};

export type BedrockInputSchema = {
  json: any;
};

export type BedrockToolChoice =
  | { tool: BedrockSpecificToolChoice }
  | { auto: any }
  | { any: any };

export type BedrockSpecificToolChoice = {
  name: string;
};

export type BedrockSystemContent =
  | { guardContent: BedrockGuardContent }
  | { text: string };

export type BedrockConverseOutput = {
  message?: BedrockMessage;
};

export type BedrockConverseMetrics = {
  latencyMs: number;
};

export type BedrockTokenUsage = {
  inputTokens: number;
  outputTokens: number;
  totalTokens: number;
};

export type BedrockConverseTrace = {
  guardrail?: BedrockGuardrailTraceAsssessment;
};

export type BedrockGuardrailTraceAsssessment = {
  inputAssessment?: { [key: string]: BedrockGuardrailAssessment };
  modelOutput?: string[];
  outputAssessments?: { [key: string]: BedrockGuardrailAssessment };
};

export type BedrockGuardrailAssessment = {
  contentPolicy?: BedrockGuardrailContentPolicyAssessment;
  contextualGroundingPolicy?: BedrockGuardrailContextualGroundingPolicyAssessment;
  invocationMetrics?: BedrockGuardrailInvocationMetrics;
  sensitiveInformationPolicy?: BedrockGuardrailSensitiveInformationPolicyAssessment;
  topicPolicy?: BedrockGuardrailTopicPolicyAssessment;
  wordPolicy?: BedrockGuardrailWordPolicyAssessment;
};

export type BedrockGuardrailContentPolicyAssessment = {
  filters: BedrockGuardrailContentFilter[];
};

export type BedrockGuardrailContentFilter = {
  action: 'BLOCKED' | string;
  confidence: 'NONE' | 'LOW' | 'MEDIUM' | 'HIGH' | string;
  type:
    | 'INSULTS'
    | 'HATE'
    | 'SEXUAL'
    | 'VIOLENCE'
    | 'MISCONDUCT'
    | 'PROMPT_ATTACK'
    | string;
  filterStrength: 'NONE' | 'LOW' | 'MEDIUM' | 'HIGH' | string;
};

export type BedrockGuardrailContextualGroundingPolicyAssessment = {
  filters: BedrockGuardrailContextualGroundingFilter;
};

export type BedrockGuardrailContextualGroundingFilter = {
  action: 'BLOCKED' | 'NONE' | string;
  score: number;
  threshold: number;
  type: 'GROUNDING' | 'RELEVANCE' | string;
};

export type BedrockGuardrailInvocationMetrics = {
  guardrailCoverage?: BedrockGuardrailCoverage;
  guardrailProcessingLatency?: number;
  usage?: BedrockGuardrailUsage;
};

export type BedrockGuardrailCoverage = {
  textCharacters?: BedrockGuardrailTextCharactersCoverage;
};

export type BedrockGuardrailTextCharactersCoverage = {
  guarded?: number;
  total?: number;
};

export type BedrockGuardrailUsage = {
  contentPolicyUnits: number;
  contextualGroundingPolicyUnits: number;
  sensitiveInformationPolicyFreeUnits: number;
  sensitiveInformationPolicyUnits: number;
  topicPolicyUnits: number;
  wordPolicyUnits: number;
};

export type BedrockGuardrailSensitiveInformationPolicyAssessment = {
  piiEntities: BedrockGuardrailPiiEntityFilter[];
  regexes: BedrockGuardrailRegexFilter[];
};

export type BedrockGuardrailPiiEntityFilter = {
  action: 'BLOCKED' | 'ANONYMIZED' | string;
  match: string;
  type:
    | 'ADDRESS'
    | 'AGE'
    | 'AWS_ACCESS_KEY'
    | 'AWS_SECRET_KEY'
    | 'CA_HEALTH_NUMBER'
    | 'CA_SOCIAL_INSURANCE_NUMBER'
    | 'CREDIT_DEBIT_CARD_CVV'
    | 'CREDIT_DEBIT_CARD_EXPIRY'
    | 'CREDIT_DEBIT_CARD_NUMBER'
    | 'DRIVER_ID'
    | 'EMAIL'
    | 'INTERNATIONAL_BANK_ACCOUNT_NUMBER'
    | 'IP_ADDRESS'
    | 'LICENSE_PLATE'
    | 'MAC_ADDRESS'
    | 'NAME'
    | 'PASSWORD'
    | 'PHONE'
    | 'PIN'
    | 'SWIFT_CODE'
    | 'UK_NATIONAL_HEALTH_SERVICE_NUMBER'
    | 'UK_NATIONAL_INSURANCE_NUMBER'
    | 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER'
    | 'URL'
    | 'USERNAME'
    | 'US_BANK_ACCOUNT_NUMBER'
    | 'US_BANK_ROUTING_NUMBER'
    | 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER'
    | 'US_PASSPORT_NUMBER'
    | 'US_SOCIAL_SECURITY_NUMBER'
    | 'VEHICLE_IDENTIFICATION_NUMBER'
    | string;
};

export type BedrockGuardrailRegexFilter = {
  action: 'BLOCKED' | 'ANONYMIZED' | string;
  match?: string;
  name?: string;
  regex?: string;
};

export type BedrockGuardrailTopicPolicyAssessment = {
  topics: BedrockGuardrailTopic[];
};

export type BedrockGuardrailTopic = {
  action: 'BLOCKED' | string;
  name: string;
  type: 'DENY' | string;
};

export type BedrockGuardrailWordPolicyAssessment = {
  customWords: BedrockGuardrailCustomWord[];
  managedWordLists: BedrockGuardrailManagedWord[];
};

export type BedrockGuardrailCustomWord = {
  action: 'BLOCKED' | string;
  match: string;
};

export type BedrockGuardrailManagedWord = {
  action: 'BLOCKED' | string;
  match: string;
  type: 'PROFANITY' | string;
};
```
