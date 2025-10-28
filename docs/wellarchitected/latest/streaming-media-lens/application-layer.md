# Application layer

The application layer is a collection of services and business
logic that interacts with the streaming media layer to deliver
functions like authentication, authorization, search,
recommendations, or interactivity. This layer exposes a set of
application programming interfaces (APIs) and serves data in
response to requests from clients. Though your application will
have a unique set of endpoints, there are a common set of services
deployed alongside streaming media applications.

- **Subscriber Management** —
  A method for user authentication and media playback
  authorization is necessary for transnational or subscription
  services. Services like **Amazon Cognito**, when combined with URL tokenization and
  content encryption, can be used to secure access to content.
- **Content Management** — A
  purpose-built database for indexing content and associated
  metadata. AWS Database Services like
  **Amazon DynamoDB** or
  **Amazon Relational Database Service** are common backend services used for
  Content Management state.
- **Analytics** — A system for
  ingesting client analytics regarding playback behaviors
  (content preference, play-through, skip, pause, re-watch)
  and extracting business insights for decision-making. In the
  streaming media layer, telemetry data (error rates, buffer
  rates, latency etc) is used to maintain quality of
  experience during playback, but services like
  **Kinesis Data Streams** can
  also be used to populate data warehouses with
  **Amazon Redshift** or
  **Amazon S3**. These
  long-term warehouses can be examined by business
  stakeholders to make strategic decisions regarding feature
  enhancements to the service or to produce content relevant
  to viewer interests.
- **Interactivity** — A
  service, commonly aligned with video playback using embedded
  metadata, that provides audience engagement through
  interactions with the host, audience members, or metadata to
  enrich the experience. **Amazon
  IVS** and **AWS Elemental
  Live** provide timed metadata interfaces that are
  used to embed data directly within the video stream and
  initiate events to call application APIs to render relevant
  features.
