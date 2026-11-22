

# REL05-BP03 Control and limit retry calls

 Retries recover from transient failures, but uncontrolled retries turn a small impairment into a large one. Retry requests at progressively longer intervals using exponential backoff, randomize those intervals with jitter, and cap the total number of attempts. Controlled retries release resources and give a struggling system time to recover. 

 **Desired outcome:** 
+  Your clients retry only errors that a retry can resolve, and stop on errors that will not. 
+  Your retries use exponential backoff with jitter and a maximum attempt or elapsed-time limit. 
+  Your backend services get relief from load during failures and recover faster because retries do not pile on. 
+  Your retry behavior is tested and monitored, so repeated failures surface the underlying issue. 

 **Common anti-patterns:** 
+  Teams implement retries without exponential backoff, jitter, and a maximum attempt limit, which produces synchronized traffic spikes. 
+  Teams implement retries without testing their effect, or assume an SDK already retries without verifying it. 
+  Clients retry every error, including permission, configuration, or validation errors that will never succeed without manual intervention. 
+  Repeated service failures are not monitored or alerted on, so the root cause stays hidden. 
+  Teams build custom retry logic when a built-in or third-party capability would serve. 
+  Retries occur at several layers of the stack at once, compounding into a retry storm. 
+  Clients retry operations that are not idempotent, producing duplicated side effects. 

 **Benefits of establishing this best practice:** 
+  Transient failures recover automatically without operator involvement. 
+  Overloaded services recover instead of degrading further, because backoff reduces load and jitter spreads it out. 
+  Metastable failures are avoided, because a maximum retry limit prevents runaway backlogs. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Retries help when failures are rare or transient, not when failures come from overload. A retry against a briefly unavailable dependency usually succeeds and costs little. A retry against a saturated system adds load to the exact resource that is struggling, cascading a minor event. Before you retry, understand the error codes published by your dependencies so you know which situation applies. 

 Three mechanisms make retries safe: 
+  *Exponential backoff* increases the wait between attempts, so a client that has already failed twice waits longer before trying again, reducing pressure on the backend. 
+  *Jitter* randomizes those waits, which prevents many clients from retrying in lockstep and creating synchronized traffic spikes. 
+  A *maximum retry count or elapsed-time limit* bounds the total work a single request can generate. This prevents the backlogs that lead to metastable failures, a state where a system stays overloaded even after the original trigger is gone. 

 Backoff and jitter without a cap still let backlogs grow, and a cap without backoff still overloads the backend, so all three mechanisms work together. 

 If a client, its SDK, and a downstream service each retry the same failing call, the attempts multiply rather than add. A single logical request can generate dozens of calls. Understand how errors propagate through your stack, then implement retries at exactly one layer. Idempotency is the other precondition: a retry of a non-idempotent operation can duplicate a payment, a record, or a message. Confirm an operation is [safe to retry](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) before you add retry logic to it. 

 Favor proven implementations over hand-written ones. Several AWS SDKs implement backoff and jitter by default, and mature libraries exist for most languages. Use them where they apply, understand their default configuration, and adjust the timeouts and attempt limits to your use case rather than accepting the defaults without review. Then test the retry paths, including the failure scenarios, because retry logic behaves differently under real load than in development. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose a single retry layer:** Determine the layer in your stack where retries belong for each dependency, and implement them there only. Verify that no other layer retries the same call, so attempts do not compound into a storm. 

1.  **Adopt proven retry libraries:** Use an SDK or library that implements exponential backoff and jitter for your language rather than writing your own. Review the related examples and tools for options. 

1.  **Confirm idempotency before retrying:** Verify that an operation is [idempotent](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) before adding retry logic. For operations that are not, add an idempotency mechanism first or do not retry them. 

1.  **Classify errors before retrying:** Read the error codes your dependencies publish and retry only errors a retry can resolve. Stop immediately on permission, configuration, and validation errors that will not succeed without manual intervention. 

1.  **Configure AWS SDK and CLI retry behavior:** When calling AWS APIs, use the [AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) and [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html) retry options. Confirm the defaults suit your use case, then test and adjust the retry mode and maximum attempts. 

1.  **Test and monitor retry behavior:** Exercise retry scenarios in testing and continue to exercise them in production. Monitor and alert on repeated failures so the underlying issue is visible and can be addressed. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL05-BP02 Throttle requests](rel05-bp02.md) 
+  [REL05-BP04 Fail fast and limit queues](rel05-bp04.md) 
+  [REL05-BP05 Set client timeouts](rel05-bp05.md) 
+  [REL04-BP04 Make mutating operations idempotent](rel04-bp04.md) 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 

 **Related documents:** 
+  [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) 
+  [The Amazon Builders' Library: Timeouts, retries, and backoff with jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter) 
+  [Exponential Backoff And Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) 
+  [The Amazon Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Try again: The tools and techniques behind resilient systems (ARC403)](https://www.youtube.com/watch?v=rvHd4Y76-fs) 

 **Related examples:** 
+  [GitHub - spring-attic/spring-retry](https://github.com/spring-attic/spring-retry) 
+  [Retry](https://resilience4j.readme.io/docs/retry) 

 **Related tools:** 
+  [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) 
+  [AWS CLI retries in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html) 