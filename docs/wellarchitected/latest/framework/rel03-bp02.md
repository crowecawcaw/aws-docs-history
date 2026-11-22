

# REL03-BP02 Build services focused on specific business domains and functionality

 Where you draw service boundaries decides how independently your teams and services can operate. Boundaries that follow business domains provide ownership to each team of a coherent slice of functionality so that they can set their own reliability requirements. Boundaries drawn along technical layers, such as user interface or database, force many teams to coordinate on a single change. Aligning services to business capabilities keeps failures and updates contained within one domain. 

 **Desired outcome:** 
+  Your services align to business domains, so each fulfills a specific business function with its own reliability requirements. 
+  Your engineers and business stakeholders define bounded contexts together using practices such as event storming. 
+  Your new applications are designed as services with well-defined boundaries and loose coupling. 
+  Your existing monoliths are decomposed into bounded contexts using established patterns rather than ad hoc splits. 
+  Your domain services run as independent processes that do not share state and handle demand and faults on their own. 

 **Common anti-patterns:** 
+  Teams are organized around technical layers such as user interface, middleware, or database instead of business domains. 
+  Applications span multiple domains, so a single change requires larger testing efforts and coordination across several domain teams. 
+  Shared domain libraries couple services together, so a change for one domain forces changes in others. 
+  Service contracts and business logic express entities inconsistently, which forces translation layers that complicate systems and increase debugging effort. 

 **Benefits of establishing this best practice:** 
+  Applications are bounded by business domains and share a common business language, which improves clarity across teams. 
+  Services are independently testable and deployable. 
+  Each service meets the resilience requirements specific to its domain. 
+  Teams reason about failure handling within a single domain rather than across the whole system. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 *Domain-driven design (DDD)* is the practice of modeling software around business domains. Its central concept is the bounded context: a boundary within which a domain model and its language stay consistent and self-contained. When a service maps to one bounded context, the team that owns it can reason about failures, define reliability requirements, and deploy changes without negotiating with other domains. The alternative, organizing around technical layers, spreads a single business capability across many teams and turns every change into a coordination problem. 

 A common failure mode is the shared domain library. When services depend on the same entity definitions, a change in one domain forces changes and redeployments in others, which reintroduces the coupling that segmentation was meant to remove. A related problem appears when contracts and logic do not use a consistent domain language. Teams then build translation layers between services, which add code, obscure meaning, and complicate debugging. DDD addresses both problems by giving each context its own model and a shared vocabulary, sometimes called a ubiquitous language, that the code and the business both use. 

 For new systems, teams identify domains up front and design services around them. For existing monoliths, a full rewrite is rarely justified and often fails, so decomposition patterns provide safer paths. The bubble context introduces a small bounded context alongside a legacy system, protected by an anti-corruption layer that keeps the legacy model from leaking into the new one. This lets a team adopt DDD in stages without an up-front commitment to rewrite everything. 

![Diagram showing how domain analysis defines entities and contracts, which then inform decisions about service boundaries that AWS services implement as running systems.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/domain-driven-decision.png)

*Domain analysis leading to service boundary decisions*


 Figure 1 shows how domain analysis leads to a decision about service boundaries. After teams define entities and contracts, AWS services implement those domains as running systems. Serverless and container services remove infrastructure management so teams concentrate on domain logic, and purpose-built databases let each service match its storage to its domain. [Building hexagonal architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/) describes a pattern that separates business logic from integration details, which keeps the domain model independent of the services around it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Run event storming to map the domain:** Bring engineers and business stakeholders together to identify events, commands, aggregates, and domains in a lightweight sticky-note format. See [event storming](https://serverlessland.com/event-driven-architecture/visuals/event-storming). This session produces the raw material for drawing bounded contexts. 

1.  **Group entities into bounded contexts:** Divide the domain into services by grouping entities that share features and attributes into the same context. For example, a retail site might place package, delivery, and schedule in a shipping context, and price, discount, and currency in a pricing context. These contexts become the template for service boundaries. 

1.  **Apply decomposition patterns to existing monoliths:** For legacy applications, refactor along business capability, subdomain, or transaction boundaries rather than splitting arbitrarily. See [Decomposing monoliths into microservices](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/). To adopt DDD without an up-front rewrite, introduce a [bubble context](https://www.domainlanguage.com/wp-content/uploads/2016/04/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf) protected by an [anti-corruption layer](https://serverlessland.com/event-driven-architecture/visuals/messages-between-bounded-context). 

1.  **Drive service design with domain tests:** Start development by writing tests that exercise the business rules of each domain. Test-driven development (TDD) and behavior-driven development (BDD) keep services focused on solving business problems rather than technical concerns. 

1.  **Select AWS services that fit each domain:** Match each service to its domain requirements. [AWS Serverless](https://aws.amazon.com/serverless/) and [containers at AWS](https://aws.amazon.com/containers/) let teams focus on domain logic instead of infrastructure, and [purpose-built databases](https://aws.amazon.com/products/databases/) let each service use the store that fits its data. For architecture options, see [microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html). 

1.  **Separate business logic from integrations:** Build domain logic first and attach integration adapters afterward, so interface details do not bleed into the domain model. For the pattern, see [Building hexagonal architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/introduction.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL03-BP01 Choose how to segment your workload](rel03-bp01.md) 
+  [REL03-BP03 Provide service contracts per API](rel03-bp03.md) 
+  [REL04-BP02 Implement loosely coupled dependencies](rel04-bp02.md) 

 **Related documents:** 
+  [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/) 
+  [How to break a Monolith into Microservices](https://martinfowler.com/articles/break-monolith-into-microservices.html) 
+  [Microservices](https://www.martinfowler.com/articles/microservices.html) 
+  [Domain-Driven Design: Tackling Complexity in the Heart of Software: Evans, Eric: 9780321125217: Amazon.com: Books](https://www.amazon.com/gp/product/0321125215) 
+  [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) 
+  [Behavior-driven development](https://en.wikipedia.org/wiki/Behavior-driven_development) 

 **Related examples:** 
+  [GitHub - aws-samples/designing-cloud-native-microservices-on-aws: Introduce a fluent way to design cloud native microservices via EventStorming workshop, this is a hands-on workshop. Contains such topics: DDD, Event storming, Specification by example. Including the AWS product : Serverless Lambda , DynamoDB, Fargate, CloudWatch.](https://github.com/aws-samples/designing-cloud-native-microservices-on-aws/tree/main) 

 **Related services:** 
+  [Microservices on AWS](https://aws.amazon.com/microservices/) 