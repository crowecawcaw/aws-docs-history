

# OPS07-BP03 Perform knowledge management

 Teams lose time and repeat mistakes when the knowledge they need is scattered or out of date. Knowledge management gives your organization a single, searchable place for cross-organization knowledge and a process to keep that information current. When people find accurate information quickly, they make better decisions, onboard faster, and depend less on individual memory. 

 **Desired outcome:** 
+  You have mechanisms to add, update, and archive information, and your teams use them consistently. 
+  Your team members find timely, accurate information when they need it. 
+  Your knowledge is searchable across the organization. 
+  Your content has clear ownership and a review cadence that keeps it current, driven by signals produced automatically rather than gathered manually, so the cadence holds even when the team is busy. 
+  You make following the documented path the easiest option available, so people reach for it under pressure instead of working around it. 
+  When a documented procedure diverges from your actual practice, you route the correction to the runbook or playbook it belongs to, not just the page a reader happened to be viewing. 

 **Common anti-patterns:** 
+  Team members keep notes on their own machines, so knowledge disappears when they are unavailable or leave. 
+  An organization runs a wiki but has no process to maintain it, so information becomes stale and untrusted, or it drives the review from page age alone and treats a page that is old because it is stable and correct the same as one that was abandoned. 
+  A contributor adds missing information without following an agreed process and omits a critical detail, which leads to an incident. 
+  Documentation exists but is not searchable, so people recreate work that already exists. 
+  Several overlapping pages describe the same procedure, so a responder has to work out which one is authoritative before they can act. 
+  The documented procedure describes an idealised path while the method people actually use lives in a chat thread or tribal knowledge, and the difference is treated as individuals being non-compliant rather than as a defect in the document. 
+  Contributing a correction is harder than passing the knowledge on verbally, so the repository drifts further from reality with every incident. 
+  A responder discovers that a runbook is wrong, fixes the wiki page in front of them, and the runbook itself is never revised, so the same defect misleads the next person. 

 **Benefits of establishing this best practice:** 
+  Your team members share information freely, which reduces single points of knowledge. 
+  New team members onboard faster because documentation is current and searchable. 
+  Your information stays timely, accurate, and actionable through defined maintenance processes. 
+  You reduce operational risk because procedures are documented rather than held in individual memory. 
+  You lower the mental effort required at the moment of highest pressure, because the understanding a responder needs was assembled in advance rather than during the event. 
+  You find out where documentation has diverged from practice, because the gap surfaces as a correction to make rather than as a broken rule. 
+  Your review cadence survives contact with a busy quarter, because the effort of finding what needs attention is carried by automation rather than by individual discipline. 
+  Your runbooks and playbooks improve with each use, because the divergences people discover become revisions to the procedure instead of private workarounds. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Knowledge management runs on a lifecycle where people create information, others keep it current as reality changes, and someone archives outdated content before it misleads anyone. Each stage needs an owner and an agreed mechanism. 

 Stale information is the failure mode that matters most, and it is worse than no information at all. People trust what they find in the knowledge base. A runbook that references a decommissioned system or an out-of-date escalation contact leads them confidently in the wrong direction. A review cadence and clear content ownership preserve that trust. Readers stop trusting the repository the first time accurate-looking content turns out to be wrong. 

 Every page you add is one more thing a responder has to evaluate. Several pages describing the same procedure, each with a different last-review date, become a second problem for responders, as they must decide which page to trust, under time pressure, with no reliable way to tell. That failure came from the documentation. Keep one authoritative page per procedure, show its status and last review date on the page, and treat archiving old pages as safety work. Measure the knowledge base by how quickly and confidently someone reaches the correct answer. 

 The practice pays off during an incident. A responder often has to act before fully understanding what is happening. Anything they work out from scratch, they work out under the worst conditions. Knowledge management moves that effort earlier, into calm periods, so the responder recognizes the situation during the incident. Judge the repository by how long it takes to find the right page, how often someone asks in chat because searching is slower, and whether a new team member can run a procedure independently. 

 Documented procedures diverge from what people actually do. Live procedures pick up undocumented adjustments, such as a step everyone knows to skip or a system that now answers on a different endpoint. When the document and the practice misalign, the document requires improvements. When you treat this gap as non-compliance, the actual fix does not get documented, and the next responder inherits an incorrect document. Make fixing a page easier than passing the workaround along verbally, because people take whichever route costs less effort. Capture what the team actually does. 

 Treat each gap as feedback that improves the source procedure. Route the correction to the runbook or playbook that owns the procedure. Editing the page in front of you leaves the source procedure wrong for the next reader. Make the return path explicit. Anyone who notices a gap can name the owning procedure and raise a revision against it at no more cost than writing a note. Signals include a step someone skipped, a flag that had to be set first, an escalation contact who had moved on, or the point where someone gave up on the document and asked a colleague. Rehearsals and game days surface the same signals in calm conditions, cheaper than waiting for an incident. Author procedures as runbooks and playbooks, use post-incident analysis to find where they departed from reality, then correct the authoritative source and track larger fixes as funded work. If reconciliation produces page edits but no procedure revisions, the loop is still open and the runbooks are not improving. 

 A cadence that relies on someone remembering to run it slips first when the team gets busy, which is exactly when accuracy matters most. Automate the job of finding what needs attention, even where a person still makes the call. Several checks are purely mechanical: pages past their review date, references to systems or endpoints that no longer resolve, pages with no named owner, and duplicates covering the same procedure. Run them on a schedule so that documentation curation becomes a queue of specific items with owners assigned. Generate reference material from the source of truth where you can to avoid drift. Keep knowledge in version control and change it through review, which is the same discipline you already apply to the workload. Let the checks flag and route items, but do not let them remove content on their own judgment. A page untouched for a year might be abandoned, or it might be stable and correct, and its age alone will not tell you which. Have automation propose the archive and a person confirm it. 

 Open editing keeps content current but risks consistency. Strict gatekeeping helps verify quality but slows contributions. Combine open contribution with a defined process for significant changes and periodic curation. Decide who owns curation, how contributors propose changes, and how often you audit the content. 

 Information that cannot be searched or browsed is effectively lost, no matter how well written. Consistent structure, tagging, and full-text search let people reach the right page in seconds. When search fails, people rebuild knowledge that already exists. 

 Options include a managed knowledge service, a self-hosted wiki, or a version-controlled document repository, which differ in setup effort, access control, and integration. For example, a retail company hosts an internal wiki and encourages staff to contribute during daily work. Each quarter, a cross-functional team reviews the least-updated pages and decides whether to archive or refresh them. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select and agree on a content management system:** Choose the repository where knowledge will live, and get agreement from stakeholders across the organization. If you have no existing system, consider a managed knowledge service, a self-hosted wiki, or a version-controlled document repository. 

1.  **Define processes for the information lifecycle:** Develop runbooks for adding, updating, and archiving information, and assign ownership for each. Educate the team on these processes so contribution and maintenance stay consistent rather than improvised. 

1.  **Populate the repository with priority knowledge:** Document the knowledge teams use most, starting with daily runbooks and playbooks. Extend any templates your organization already provides to fit your team's needs, and work with stakeholders to prioritize what to capture first. 

1.  **Make the documented path the lowest-effort path:** Find where people currently go for answers and reduce the effort of the route you want them to use. Put the correction mechanism on the page itself so fixing an error takes seconds, surface last-reviewed status and owner inline so readers can judge currency without asking, and remove or merge duplicates so no adjudication is needed. Where asking a colleague is faster than searching, treat that as a defect in the repository rather than a habit to discourage. 

1.  **Reconcile documented procedures with actual practice:** Have a team member follow the written procedure and record where they departed from it, then correct the document to match what actually works. Capture the undocumented adjustments people have accumulated, and make it explicit that a divergence is a document defect rather than an individual's non-compliance, so the real method surfaces instead of staying private. Post-incident analysis is a reliable source of these gaps, since a procedure that misled a responder during an event is a procedure worth rewriting. 

1.  **Close the loop back to the runbook or playbook that owns the defect:** Decide where a recorded divergence goes and who acts on it, so the correction reaches the source procedure rather than stopping at the page the reader was viewing. Name the owning runbook or playbook on the page, give contributors a one-step way to raise the revision, and set the expectation that a divergence found during an event produces a revision to [OPS05-BP01 Develop and test runbooks to perform procedures](ops05-bp01.md) runbooks or [OPS05-BP02 Develop and test playbooks to respond to incidents](ops05-bp02.md) playbooks. Where the fix needs prioritizing or funding beyond a quick edit, track it through [OPS07-BP02 Identify and drive improvements](ops07-bp02.md) so it stays visible as work. Review whether the loop is actually turning by asking how many procedure revisions came out of the last quarter's reconciliation, because page edits alone mean the signal is being absorbed rather than acted on. 

1.  **Automate the currency signals, and keep the judgment human:** Schedule the mechanical checks (review date passed, references that no longer resolve, no named owner, duplicate coverage) and route each finding to the owner rather than to an unmonitored shared queue. Generate reference material from the source of truth wherever you can, and if the repository is version controlled, run the checks in the same review pipeline you use for code. Put a guardrail on anything that removes content, so automation proposes the archive and the owner confirms it. 

1.  **Review and curate on a cadence:** On a periodic basis, work with stakeholders to find out-of-date content and either archive it or bring it current. Track which pages go longest without updates, because those are the most likely to mislead. Archive decisively rather than leaving old pages in place alongside new ones, since a superseded page that stays reachable competes with its replacement. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS05-BP01 Develop and test runbooks to perform procedures](ops05-bp01.md) 
+  [OPS05-BP02 Develop and test playbooks to respond to incidents](ops05-bp02.md) 
+  [OPS05-BP04 Assess operational readiness](ops05-bp04.md) 
+  [OPS06-BP03 Define escalation paths](ops06-bp03.md) 
+  [OPS07-BP01 Perform post-incident analysis](ops07-bp01.md) 
+  [OPS07-BP02 Identify and drive improvements](ops07-bp02.md) 

 **Related tools:** 
+  [DokuWiki](https://github.com/dokuwiki/dokuwiki) 
+  [Gollum](https://github.com/gollum/gollum) 
+  [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) 
+  [Wiki.js](https://github.com/Requarks/wiki) 