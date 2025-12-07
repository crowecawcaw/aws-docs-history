# Using 5 Whys analysis in incident

reports

When generating incident reports, CloudWatch investigations can perform a 5 Whys root cause analysis to
systematically identify the underlying causes of operational issues. This structured
approach enhances your incident reports with deeper insights and actionable remediation
steps.

This feature uses Amazon Q to provide a conversational chat. The user signed into the
AWS Management Console must have the following permissions:

```
{
    "Sid" : "AmazonQAccess",
    "Effect" : "Allow",
    "Action" : [
       "q:StartConversation",
       "q:SendMessage",
       "q:GetConversation",
       "q:ListConversations",
       "q:UpdateConversation",
       "q:DeleteConversation",
       "q:PassRequest"
     ],
    "Resource" : "*"
 }
```

You can add these permissions directly, or by attaching either the [AIOpsConsoleAdminPolicy](../../../aws-managed-policy/latest/reference/AIOpsConsoleAdminPolicy.md "../../../aws-managed-policy/latest/reference/AIOpsConsoleAdminPolicy.md") or [AIOpsOperatorAccess](../../../aws-managed-policy/latest/reference/AIOpsOperatorAccess.md "../../../aws-managed-policy/latest/reference/AIOpsOperatorAccess.md") managed policy to the user or role.

## What is 5 Whys analysis?

The 5 Whys is a root cause analysis technique that asks "why" repeatedly to drill
down from incident symptoms to fundamental causes. Each answer becomes the basis for
the next question, creating a logical chain that reveals the true root cause rather
than just surface-level symptoms.

During incident report generation, CloudWatch investigations uses this method to analyze investigation
findings and provide structured root cause analysis that goes beyond immediate
technical failures to identify process, configuration, or systemic issues.

## Benefits for incident reporting

Including 5 Whys analysis in incident reports provides several advantages:

- **Comprehensive root cause identification** -
  Moves beyond immediate technical causes to identify underlying process or
  system issues
- **Actionable remediation plans** - Provides
  specific, targeted actions to prevent recurrence rather than temporary
  fixes
- **Organizational learning** - Documents the
  complete causal chain for future reference and team knowledge sharing
- **Structured analysis** - Ensures systematic
  investigation rather than ad-hoc problem solving

## Example scenarios in incident

reports

### Database connection failure

incident

**Initial incident:** E-commerce application
experiencing widespread 500 errors

1. **Why 1:** Why are users getting 500
   errors? The application cannot connect to the primary database.
2. **Why 2:** Why can't the application
   connect to the database? The database instance ran out of available
   connections.
3. **Why 3:** Why did the database run out
   of connections? A batch processing job opened many connections without
   properly closing them.
4. **Why 4:** Why didn't the batch job close
   connections properly? The job's error handling doesn't include
   connection cleanup in failure scenarios.
5. **Why 5:** Why wasn't proper error
   handling implemented? Code review process doesn't include specific
   checks for resource management patterns.

**Root cause:** Inadequate code review standards
for resource management

**Recommended actions:** Update code review
checklist, implement connection pooling monitoring, add automated resource leak
detection

### Performance degradation incident

**Initial incident:** API response times
increased from 200ms to 5000ms during traffic spike

1. **Why 1:** Why did response times
   increase? CPU utilization reached 100% on all application
   instances.
2. **Why 2:** Why didn't auto scaling add
   more instances? Auto scaling was triggered but new instances failed
   health checks.
3. **Why 3:** Why did new instances fail
   health checks? The application startup process takes 8 minutes, longer
   than the health check timeout.
4. **Why 4:** Why does startup take so long?
   The application downloads large configuration files from S3 on every
   startup.
5. **Why 5:** Why wasn't this startup delay
   considered in auto scaling configuration? Performance testing was done
   with pre-warmed instances, not cold starts.

**Root cause:** Performance testing methodology
doesn't reflect production auto scaling scenarios

**Recommended actions:** Include cold start
testing, optimize application startup, adjust health check timeouts, implement
configuration caching

### Complex incident with branch

analysis

**Initial incident:** OpenSearch Serverless
customers experienced 48.3% availability degradation for 11 hours

**Main analysis chain:**

1. **Why 1:** Why did customers experience
   service degradation? Service availability dropped to 48.3% due to
   incorrect ingester scaling.
2. **Why 2:** Why was ingester scaling
   incorrect? CortexOperator reduced ingesters from 223 to 174 due to AZ
   balance miscalculation.
3. **Why 3:** Why did CortexOperator
   miscalculate AZ balance? The code couldn't process new Kubernetes label
   formats after version 1.17 upgrade.
4. **Why 4 (Branch A - Technical):** Why
   didn't the code handle new label formats? The code expected
   'failure-domain.beta.kubernetes.io/zone' labels but Kubernetes 1.17
   changed to 'topology.kubernetes.io/zone'.
5. **Why 5 (Branch A):** Why wasn't backward
   compatibility implemented? The label format change wasn't documented in
   the upgrade notes reviewed during deployment planning.

**Branch B - Process Analysis:**

1. **Why 4 (Branch B - Process):** Why
   wasn't this caught in testing? Integration tests used pre-configured
   clusters with old label formats.
2. **Why 5 (Branch B):** Why didn't testing
   include label format validation? Test environment setup didn't mirror
   production Kubernetes version upgrade sequence.

**Root causes identified:**

- Technical: Missing backward compatibility for Kubernetes label format
  changes
- Process: Testing methodology doesn't validate version upgrade
  impacts

**Integrated remediation plan:** Implement label
format detection logic, enhance upgrade testing procedures, add automated
compatibility validation, and establish version change impact assessment
process.

## Using the guided 5 Whys workflow

CloudWatch investigations provides a guided 5 Whys analysis workflow to help you address missing facts
and strengthen your incident reports. This feature appears as a suggested workflow
when the system identifies opportunities to enhance root cause analysis.

### Interactive analysis experience

The 5 Whys analysis in CloudWatch investigations uses an interactive, chat-based approach that
guides you through the investigation process. This conversational method helps
ensure comprehensive analysis while maintaining logical flow between
questions.

**Key features of the interactive
experience:**

- **Fact-based initialization** - The
  system presents relevant facts from your investigation upfront, using
  them to pre-populate obvious answers and clearly indicating fact-based
  versus inference-based suggestions
- **Guided probing** - For each "why"
  question, the system suggests answers based on available facts, requests
  specific additional context, and guides you to consider important
  aspects before proceeding
- **Branch management** - When multiple
  contributing factors are identified, the system clearly presents branch
  options, explains relationships between branches, and helps prioritize
  parallel investigations
- **Progressive validation** - For each
  response, the system reformulates answers for clarity, seeks
  confirmation, highlights key insights, and connects findings to broader
  context

This approach ensures that you capture all relevant information while
maintaining focus on the most critical causal relationships.

**Accessing the guided workflow:**

1. During incident report generation, review the **Facts need
   attention** section in the right panel.
2. Look for the **Guided 5-Whys analysis** suggestion under
   **Suggested workflow**.
3. Choose **Guide me** to start the interactive 5 Whys
   process.
4. Follow the guided prompts to systematically work through each "why"
   question, building a complete causal chain from symptoms to root
   cause.

The guided workflow helps ensure you capture comprehensive root cause information
by walking you through each step of the 5 Whys methodology. The analysis results are
automatically incorporated into your incident report, providing structured
documentation for post-incident reviews and organizational learning.

You can also request a 5 Whys analysis through the chat interface by asking
questions such as "Perform a 5 Whys analysis for this incident" or "What is the root
cause using 5 Whys methodology?"

## Handling complex incidents with multiple

causes

Some incidents involve multiple contributing factors that require parallel
analysis paths. CloudWatch investigations supports branch analysis to ensure all significant causes are
identified and addressed.

**When branch analysis is needed:**

- Multiple independent failures occurred simultaneously
- Different system components contributed to the same customer impact
- Both technical and process failures played significant roles
- Cascading failures created multiple causal chains

**Branch analysis process:**

1. **Branch identification** - The system
   identifies points where multiple causes converge or diverge
2. **Parallel investigation** - Each branch is
   analyzed using the complete 5 Whys methodology
3. **Connection mapping** - Relationships
   between branches are documented to show how they interact
4. **Integrated resolution** - Remediation plans
   address all identified root causes and their interactions

This comprehensive approach ensures that complex incidents receive thorough
analysis and that all contributing factors are addressed in the final remediation
plan.

## Best practices for effective 5 Whys

analysis

To maximize the effectiveness of 5 Whys analysis in your incident reports, follow
these best practices derived from operational experience:

### Question formulation guidelines

- **Start with customer impact** - Begin
  each analysis with the customer-facing problem to maintain focus on
  business impact
- **Increase technical depth
  progressively** - Move from business impact to technical
  details as you progress through the questions
- **Maintain logical continuity** - Ensure
  each answer naturally leads to the next question without logical
  gaps
- **Include supporting evidence** -
  Reference specific metrics, logs, or timeline events to validate each
  answer

### Analysis validation

Validate your 5 Whys analysis using these criteria:

- **Logical flow** - Clear progression from
  symptoms to root cause with no missing steps
- **Technical accuracy** - Correct
  terminology, accurate system behavior descriptions, and valid component
  interactions
- **Completeness** - The analysis explains
  all observed symptoms and reaches a fundamental cause that, if
  addressed, would prevent recurrence
- **Actionability** - The root cause
  identified leads to specific, implementable remediation actions

### Common pitfalls to avoid

- **Stopping at symptoms** - Don't conclude
  the analysis at the first technical failure; continue until you reach
  systemic or process causes
- **Blame-focused analysis** - Focus on
  system and process failures rather than individual actions
- **Single-path thinking** - Consider
  multiple contributing factors and use branch analysis when
  appropriate
- **Insufficient evidence** - Ensure each
  answer is supported by concrete data from your investigation

### Integration with incident report

sections

The 5 Whys analysis integrates with other sections of your incident report to
provide comprehensive documentation:

- **Timeline correlation** - Each "why"
  question can reference specific timeline events, providing temporal context
  for causal relationships
- **Metrics validation** - Answers are
  supported by metrics and graphs that demonstrate the technical behaviors
  described
- **Impact assessment alignment** - The first
  "why" directly connects to customer impact metrics documented in the impact
  assessment section
- **Lessons learned foundation** - Root causes
  identified through 5 Whys analysis directly inform the lessons learned and
  corrective actions sections

This integration ensures consistency across your incident report and provides
stakeholders with a complete, coherent narrative from initial symptoms through root
cause to remediation plans.
