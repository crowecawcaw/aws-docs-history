

# Human-in-the-loop annotation

## What it is
<a name="ai-data-preparation-hil-overview"></a>

Amazon SageMaker Human-in-the-loop annotation (HIL) is the step where people, rather than a model, decide what a record's label should be. You give it the records that need review, the question you want answered about each one, and the annotators who should answer it. You get one labeling project for each annotator. When the annotators have answered, you export their answers and fold the corrections back into the dataset.

It fits three situations in particular:
+ **Reviewing low-confidence automated labels.** The rows that auto-labeling flagged as uncertain are the usual input to this step.
+ **Building an evaluation set.** In a held-out set that decides whether a model is good enough, every wrong label moves the score, so you usually label these sets by hand.
+ **Judgment a model cannot settle.** Domain rules, ambiguous phrasing, and classes that are genuinely easy to confuse need a person who knows the domain.

You do not have to review everything. The usual pattern is to label the whole corpus automatically and send only the uncertain rows for human review. The amount of human work then follows the amount of uncertainty rather than the size of the dataset.

**Everyone in the domain can see every project**  
Label Studio Community Edition runs here, and it has no role-based access control. If you can open the shared space, you can open every project in it, including other annotators' projects. Every annotator can do the same, so everyone who can open the application can see all of the records under review. Two things in Studio control who that is. Domain membership is what grants access, so restrict which identities have a user profile in the domain that hosts the application. For records you do not want every annotator to see, run those projects in a separate domain, with its own user profiles and its own Label Studio application. For more information, see [Security in Label Studio labeling spaces](label-studio-security.md).

## How it works
<a name="ai-data-preparation-hil-how"></a>

Four concepts carry most of the behavior.

One shared Label Studio application for each domain  
Label Studio is a first-party application in Studio. It runs in a single space that is shared across the domain, so everyone works in one Label Studio instance backed by one database. You do not run one instance for each person, and you do not install anything.

Annotators are Studio user profiles  
An annotator is an existing user profile in the same domain. They sign in to Studio as themselves and open the Label Studio application; Label Studio signs them in automatically, with no separate account and no password. Because each annotator arrives as their own user profile, every annotation is attributed to the person who submitted it.

One project for each annotator  
The agent splits the records as evenly as they divide and gives each annotator their own project holding their share. Where the count does not divide exactly, the agent spreads the remainder across the first few projects. For example, 41 records across 3 annotators become projects of 14, 14, and 13. With one project for each annotator, you can see each person's progress separately. Separate projects are not what produces attribution—that comes from the annotator's own user profile, so work done in the wrong project is still credited to whoever submitted it.

The labeling interface is generated from your question  
You describe what you want asked about each record, and the agent generates the questions, the input types, and the fields shown to the annotator from that description. You can change the interface and have the projects regenerated.

The Label Studio application has to be running in your domain before a review can start. For the steps that launch it, see [Use human-in-the-loop annotation](#ai-data-preparation-hil-use).

## Inputs
<a name="ai-data-preparation-hil-inputs"></a>

This step needs four things:
+ **The records to review.** A local file path, an Amazon S3 URI, or a dataset ARN. Each record needs the field that carries the text an annotator reads. Where a record already carries a label, name the field that holds it, and the annotator checks that label.
+ **What kind of review is needed**—for example, *confirm the automated label is correct* or *check the answer is factually accurate*. The agent drafts the annotation questions from this and asks you to approve them.
+ **The annotators.** User profile names in the same domain as the Label Studio application.
+ **A project name**, used as the prefix for each annotator's project.

Anyone with a user profile in the domain can be an annotator, and there is no separate step to add them to the shared space. Someone with no user profile in that domain cannot be an annotator until one is created. Creating user profiles is a domain administration task. If you do not administer the domain yourself, ask the person who does before you plan the split.

The records usually arrive from the step before this one, which attaches a confidence score to every row and flags the rows that fall below the bar. Those flagged rows are what you send for review. For more information, see [Auto-labeling](ai-data-preparation-autolabel.md).

You can also bring your own records with no upstream step at all, which is the usual path when you are building an evaluation set by hand rather than correcting automated output.

## Use human-in-the-loop annotation
<a name="ai-data-preparation-hil-use"></a>

Start by launching the shared Label Studio application in your Studio domain. It only needs launching once for the whole domain, so check whether somebody has already launched it before you start a new space.

The Label Studio application runs in a shared space, so the domain needs a **Space default execution role** before you can launch the application for the first time. You need domain administrator access to set the role. If you aren't a domain administrator, ask one to set it. For instructions on setting the role, see [Add shared space support to an existing domain](domain-space-create.md#domain-space-add).

Before you set the role, stop every application running in any shared space in the domain. For more information about stopping applications, see [Edit domain settings](domain-edit.md). Label Studio needs no permissions on the role. For information about what the role must not have, see [AWS Identity and Access Management for labeling spaces](label-studio-security.md#label-studio-security-iam).

**To launch the Label Studio application**

1. In the **Applications** list, choose the **Label Studio** tile.

   The **Applications** list sits at the top of the left navigation pane and holds one tile for each application in the domain. The tile carries the Label Studio icon and sits alongside tiles such as **JupyterLab** and **Code Editor**.  
![The Studio Applications list, showing the Label Studio tile used to launch the shared Label Studio application.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/ai-data-preparation-hil/hil-studio-launch-label-studio.png)

1. On the application page, check that a **Shared** badge appears next to the name. That badge confirms you are looking at the shared space rather than a private one. The page also shows the space's instance type and storage size.

   If the space is not running already, choose **Launch application**. The status reads **Starting** while the space comes up, which takes a minute or two the first time.

   While the space comes up, the application page shows **Starting** next to **Status**, the storage size in **Storage (GB)**, and the instance type in **Instance**.  
![The Label Studio application page with the status reading Starting while the shared space launches.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/ai-data-preparation-hil/hil-label-studio-app-page-starting.png)

1. Wait until the status reads **Running**, then choose **Open Label Studio** to open the labeling tool itself.

   The same page is where you stop the space and set its size. By default the space runs on an `ml.t3.medium` instance with a 5 GB storage volume, and you change both here. **Stop space** stops the running space.

   When the space is running, **Status** reads **Running** and the page offers **Open Label Studio** next to **Stop space**, with the storage size and instance type editable beside them.  
![The Label Studio application page with the Open Label Studio and Stop space buttons available.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/ai-data-preparation-hil/hil-label-studio-app-page.png)

Choose **Stop space** when a labeling push is finished. Stopping the space does not delete annotations. Label Studio holds them on the space's storage volume, which persists after the space stops.

**Stopping the space does not end volume charges**  
Stopping the space ends the charge for the instance. It does not end the charge for that volume, which is billed for as long as the space exists. When a labeling project is finished for good, deleting the space releases the volume. For what each component costs, see [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/).

**Export annotations before you delete the space**  
Deleting the space permanently deletes every annotation held on its storage volume. Export the annotations you want to keep, and register the corrected records, before you delete the space. There is no way to recover them afterward.

**Anyone can stop the shared space**  
Because the space is shared, **Stop space** is available to everyone who can open the application, not only to the person who started it, and stopping it ends everyone's labeling session. Annotations that annotators have already submitted are not lost. For who can open the application, see the Label Studio security information at the end of this topic.

Each annotator needs a user profile in the same domain as the Label Studio application. That profile needs an execution role scoped to the annotator. A domain administrator creates both. If you do not administer the domain yourself, ask the person who does before you plan the split.

The execution role is the role Studio assumes when an annotator opens the application. Do not leave `AmazonSageMakerFullAccess` attached to it. If you attach it, an annotator can open any user profile in the domain. That defeats the per-annotator scoping you are setting up.

When you add a user profile, do not choose the option that creates a new role, because that option attaches the policy.

An annotator uses a separate identity from that execution role to reach Studio. An annotator who already signs in to AWS needs only the permission to open their own user profile.

An annotator with no AWS access of their own needs no sign-in identity. In that case, you create the presigned sign-in link for them.

For information about the permissions each identity needs, see [AWS Identity and Access Management for labeling spaces](label-studio-security.md#label-studio-security-iam).

Set up these three prerequisites before an annotator can label:
+ Create an execution role for annotators, or reuse one from an earlier review. For more information, see [Create execution role](sagemaker-roles.md#sagemaker-roles-create-execution-role).
+ Add a user profile for each annotator, and choose that role for **Execution role**. For more information, see [Add user profiles](domain-user-profile-add.md).
+ Grant each annotator permission to open their own user profile, so that they sign in themselves and you share no links. Create a presigned sign-in link only for an annotator who has no AWS access of their own.

Run this step with a coding assistant and the core AI and ML skill, from the agent environment of your choice. The Amazon SageMaker Python SDK tab explains what the SDK covers instead.

------
#### [ Amazon SageMaker Python SDK ]

Unlike the other data preparation steps, human-in-the-loop annotation does not run as a `DataPreparer` job. There is no `JobCategory` for it, and so no `DataPreparer` method to call. Use the Coding assistant with the AI and ML skill tab to run the review.

What the SDK covers is the step after the review. Once the corrections are merged into your records, you transform and register them as a new dataset version, which is a `DataTransformation` job. The job publishes the fields it accepts as a schema, so print the schema rather than guessing field names. The following Python code example prints that schema, which lists the fields a `DataTransformation` job accepts.

```python
from sagemaker.ai_registry import DatasetJobConfig, JobCategory

DatasetJobConfig.print_schema(
    JobCategory.DATA_TRANSFORMATION
)
```

For the operators available and a worked transformation, see [Data transformation](ai-data-preparation-dt.md).

------
#### [ Coding assistant with the AI and ML skill ]

The core AI and ML skill is preinstalled in the JupyterLab and Code Editor spaces in your Studio domain, so open one of your own spaces and ask your coding agent there. Setup steps and how to reach the skill from a local development environment are covered in [Get started with SageMaker AI Data Preparation](ai-data-preparation-getting-started.md).

**Run the agent in your own space**  
Run the agent in your own JupyterLab or Code Editor space, not in the Label Studio space. The Label Studio space runs the labeling tool and nothing else: its terminals and notebook kernels are disabled and it does not allow creating files, so a coding agent cannot run there. The two are separate spaces in the same domain—yours runs the agent, the shared one runs Label Studio—and the agent reaches Label Studio across that boundary.

Label Studio is the recommended way to run the review, whatever the size of the batch and the length of the records, and it is what the agent recommends if you ask it to choose. It is the right choice for longer records, for more than roughly 30 records, and whenever more than one person is reviewing. For a handful of short records you can opt into reviewing in chat instead: the agent walks you through them one at a time and creates no Label Studio project.

Launch the Label Studio application first if nobody has already—the agent uses a running application and does not create one. Then ask for the review in your own words. The following example asks for a review of the low-confidence rows in an Amazon S3 location and splits the work across three annotators. Replace the Amazon S3 URI and the annotator names with your own values.

```
Run a human review for the low-confidence rows in
s3://amzn-s3-demo-bucket/banking77/low_confidence.jsonl.
Ask annotators whether the automated label is correct and, if not,
what it should be.
Split the work across annotator-a, annotator-b and annotator-c.
```

What happens next, and where you get a say:

1. The agent prints a few sample records so you can see how long they are.

1. It proposes the questions annotators will answer, and waits for you to approve or edit them.

1. It looks for Label Studio applications in your domains and asks which one to use. It uses an application you have already launched; it does not create one for you.

1. It lists the domain's user profiles so you can pick the annotators, splits the records, and creates one project for each annotator with a link to each.

Open one of those projects and check it before you send anybody their link. Check that the questions read the way you intended, and that the records are the ones you meant to send. To change either, ask the agent to update or recreate the projects.

Make those changes before annotators start answering. If you change the questions after annotators start answering, their earlier answers apply to the earlier wording.

While the review runs, ask for progress the same way—for example, "what is the status of the human review?" You get it for each annotator: who has finished, who has not started, and how many records are done out of the total. Ask for an annotator's project link again the same way whenever they need it.

When everyone is finished, ask the agent to export the annotations and apply the corrections. That export, and the merge that follows it, happen when you ask for them and not before.

------

### What an annotator does
<a name="ai-data-preparation-hil-use-annotator"></a>

Tell your annotators to do three things: sign in to Studio with their own user profile, open the **Label Studio** application, and open the project assigned to them. Each project is named for the review run and the annotator's user profile, its description names that profile too, and it shows how many records it holds. No separate sign-up or password is involved. An annotator who opens a presigned sign-in link instead is taken straight to their project, with all three of those steps handled for them.

The **Projects** page lists every project in the shared space as a card. Each card shows the project name, the count of records answered out of the total assigned, and a description naming the Studio profile the project belongs to. The project name combines the project name you chose, the annotator's user profile name, and the review run. One card therefore corresponds to one annotator.

On the **Projects** page the cards sit beside one another in a single flat list, one card for each annotator, with no grouping, no nesting, and no ordering by owner, and every annotator opens the same list in the same order. Nothing marks out the card belonging to whoever is reading the page. The user profile name is the only thing that separates one annotator's card from the rest, and it appears both in the project name and in the description beneath it. Each card's answered-of-total count reports progress for that card's project alone, so reading two cards together compares two annotators' separate shares rather than two parts of one shared queue.

![The Label Studio Projects page, headed Projects beside the Create and Migrate projects buttons, showing six project cards in one flat, ungrouped grid. Each card carries its project name, a count of answered records written as 13 / 13, and a description beginning Assigned to SageMaker profile that names the profile, the project and the run the card belongs to.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/ai-data-preparation-hil/hil-label-studio-projects.png)


Because the edition has no role-based access control, an annotator sees everyone's projects, not only their own. The project name and description are how they find the one assigned to them.

Inside a project the annotator sees the record, any label it already carries, and the questions you approved. They answer and choose **Submit**, which records the annotation and moves on to the next record. **Skip** moves on without recording an answer, so a skipped record is one nobody has decided. Tell annotators to submit each record as they finish it rather than filling in several first, so that their work is saved as they go.

A labeling task fills the center of the page. The record text appears at the top, any label it already carries appears directly beneath it, and the questions you approved follow in order. **Submit** at the bottom right records the answers and loads the next record, and **Skip** beside it moves on without recording an answer. A counter at the bottom left shows the annotator's position in the queue.

The task reads from top to bottom as a single unit: the label sits directly beneath the record it describes, every question below them asks about that same record, and no second record appears on the page to confuse it with. **Submit** and **Skip** act on the task as a whole rather than on any one question, so an annotator answers as much as applies and then chooses once. The counter beside them belongs to the project the task came from, which is why it tracks that annotator's own share and not the progress of the review as a whole.

![A Label Studio labeling task, reached through the breadcrumb Projects, then the project name, then Labeling. A Customer utterance panel at the top holds the record text, and an Auto-assigned label panel directly beneath it holds the label the record already carries. Three questions follow, labeled Q1, Q2 and Q3: Is the auto-label correct?, If No, what is the correct label?, and Notes (optional). The Skip and Submit buttons sit at the bottom right, and the counter 1 of 1 with the record number #2419 at the bottom left.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/ai-data-preparation-hil/hil-label-studio-labeling.png)


When an annotator has answered everything in their project, Label Studio shows **No More Tasks Left in Queue**. That is the signal that their share is done.

**Two ways to hand an annotator their project**  
There are two different kinds of link, and they behave differently.  

The project link  
This is the link the agent returns for each annotator's project, and it is the one to hand out. It is an ordinary link to that project in the shared space, so the 5-minute window and the single use described below do not apply to it. What it does require is that the annotator has already signed in to Studio as their own user profile and opened the Label Studio application; only then does the link take them to their project.

A presigned sign-in link  
If you would rather an annotator skipped the manual sign-in, use a presigned Studio domain URL instead. It signs the annotator in as their own user profile and lands them in their labeling project in one step. Create one for each annotator, at the moment that annotator is ready to work: either the annotator creates their own, or you create it on their behalf. The choice changes which permissions you need, which is covered in [AWS Identity and Access Management for labeling spaces](label-studio-security.md#label-studio-security-iam). Ask the agent for the AWS CLI command and run it yourself; the agent does not create the link for you.  
A presigned sign-in link works only once and expires in 5 minutes. Anything that opens it first, such as a chat client that previews links, uses it up. Those 5 minutes are the window to open the link, not the session that follows, which lasts up to 12 hours. Have the annotator open it in a new or private window, because a browser that already holds another Studio session can fail to sign in.
Ask each annotator to sign in to AWS themselves and open the Label Studio application from Studio. They find their project on the **Projects** page, so you share no links at all. Share a presigned sign-in link only with an annotator who has no AWS access of their own.

## Results
<a name="ai-data-preparation-hil-results"></a>

When you ask for the annotations to be applied, the agent exports them from Label Studio and merges the corrections into your records. Four things come back, and the agent produces all of them in the session where you work with it: it writes its files to your own project folder on the machine that runs the agent, not inside the labeling space.
+ **A summary** of how many records were reviewed, how many were confirmed as already correct, and how many were corrected. For a review of 41 flagged rows, the summary might read 41 reviewed, 32 confirmed, and 9 corrected.
+ **The list of corrections**, each showing the record, the label it had, and the label the annotator changed it to. Read this before you accept the merge.
+ **The corrected records**, with the human decision marked. A corrected row carries a field recording that a person changed it, and another holding the original automated label. You can therefore tell a human decision from a model one and measure how often they disagreed. The names of those fields come from the annotation specification the agent drafted from the questions you approved, so they are specific to this review rather than a fixed schema. Ask the agent to print that specification before you write code against the records; if the Label Studio export disagrees with it, the agent surfaces the discrepancy and asks you how to map the fields.
+ **The export itself**, written to your project folder as `data/hil/label_studio_export.jsonl`. It holds one row for each task an annotator has answered, carrying the user profile the task was assigned to, the record as it was uploaded, and the annotations with the profile of whoever submitted each one. Tasks nobody has answered are not in the file, so exporting before the review is finished gives you a snapshot of what has been decided so far. Label Studio's own user identifiers appear alongside those profile names and carry no email address. This is the file the merge reads, and it is kept whether or not you also copy it to Amazon S3.

To keep a copy of the export in Amazon Simple Storage Service (Amazon S3), give the agent a destination when it asks where the annotations should go. It writes only to a bucket that already exists in your own account, and it does not create one, so if you have no bucket the export stays in your project folder. Before it writes anything, it shows you the exact object it will create and what it could read of the bucket's public-access settings: it says plainly when the bucket is open to the public, and equally when it could not tell, because it was not allowed to read the setting that would say. It then waits for you to confirm the destination, change it, or keep the local copy only. For the encryption of the exported file and the permissions a copy to Amazon S3 needs, see [Data protection](label-studio-security.md#label-studio-security-data).

Records nobody submitted an answer for—skipped, or still in the queue—produce no correction, so they keep the label they arrived with. Ask for progress before you ask for the merge: the counts for each annotator are what tell you whether every record was decided.

You then register the merged records, which produces a **new dataset version** rather than overwriting the old one, so the state before human review stays available for comparison. For more information, see [Data transformation](ai-data-preparation-dt.md).

**Corrections are a separate step**  
Corrections are applied to your dataset as a separate step that you ask for. Nothing is rewritten as a side effect of the review finishing.

## Limits and quotas
<a name="ai-data-preparation-hil-limits"></a>

These are characteristics of the shipped Label Studio application, measured on the default instance type. They are not service quotas, and no API reports them. Treat them as guidance for sizing a labeling push.
+ **About 8 annotators can save at the same time.** The application stores annotations in a database that takes one writer at a time, so simultaneous saves queue. Past roughly 8 concurrent savers, saves slow down noticeably and the space completes less work overall, not more. The ceiling applies to saving at the same moment, not to how many people are signed in and reading.
+ **A larger instance does not raise that ceiling.** The constraint is the single-writer database, not CPU or memory, so changing the instance type will not buy more concurrency. Stagger annotators across the day instead. The setting worth changing on the application page is the storage volume, not the instance type.
+ **The application runs on 16 instance types.** Unlike the other items in this list, this is a hard limit. A launch request for any other type fails. The error message lists the supported types. This limit is not adjustable: it is not a service quota, so you can't request additional instance types through Service Quotas or AWS Support. The following table lists the supported instance types by family.


<table>
<thead>
  <tr><th>Instance family</th><th>Supported instance types</th></tr>
</thead>
<tbody>
  <tr><td>M5</td><td><code>ml.m5.large</code>, <code>ml.m5.xlarge</code>, <code>ml.m5.2xlarge</code>, <code>ml.m5.4xlarge</code></td></tr>
  <tr><td>M6i</td><td><code>ml.m6i.large</code>, <code>ml.m6i.xlarge</code>, <code>ml.m6i.2xlarge</code>, <code>ml.m6i.4xlarge</code></td></tr>
  <tr><td>M7i</td><td><code>ml.m7i.large</code>, <code>ml.m7i.xlarge</code>, <code>ml.m7i.2xlarge</code>, <code>ml.m7i.4xlarge</code></td></tr>
  <tr><td>T3 (burstable)</td><td><code>ml.t3.medium</code> (default), <code>ml.t3.large</code>, <code>ml.t3.xlarge</code>, <code>ml.t3.2xlarge</code></td></tr>
</tbody>
</table>


  For more information about pricing, see [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/).
+ **Project sizes up to 20,000 records have been tested.** A project of that size imports in seconds, so import time is rarely what you plan around. 20,000 is the largest size that has been tested rather than a proven ceiling, so for more records than that, label them in more than one run. Splitting them across more annotators instead does not help, because each annotator adds a project and the concurrency ceiling still applies.
+ **Annotation data shares the space's 5 GB default storage volume.** Estimate from your own records rather than a fixed per-record figure, because record size varies widely. For input of size `S` holding `N` records, each annotated once, expect the database to grow by about `2S + (0.5 KB × N)`. Do that arithmetic before you create projects, and leave headroom, because the volume is shared with everything else in the space.
+ **Exports accumulate on the same volume.** Every export writes a copy of the project's data to the volume, and those copies are not removed automatically. There is no supported way to delete them from inside the space. Size the volume for all the exports you expect across the life of the project rather than for a single run.
+ **You can enlarge the volume, but not shrink it**, and only while the space is stopped. Set a larger size on the application page, then start the space again. Because it cannot be shrunk, and because exports only accumulate, choose generously the first time.
+ **This step needs the Label Studio application in your domain.** If **Label Studio** does not appear in the **Applications** list for a domain, this step cannot run there. Check whether another domain in your account offers it, and ask the person who administers your domains if none does.

**Access control cannot be changed**  
The lack of role-based access control is a property of the edition, not a setting you can change. For the access boundary and what you can do about it, see the Label Studio security information at the end of this topic.

## Troubleshooting
<a name="ai-data-preparation-hil-troubleshoot"></a>

Label Studio is not in the Applications list at all  
The application is not offered in that domain, which is a different problem from the space not having been started—starting it is not the fix. Check whether another domain in your account offers it, and ask the person who administers your domains if none does. For more information, see [Limits and quotas](#ai-data-preparation-hil-limits).

This domain has no default space settings  
The Label Studio application page shows this message and disables **Launch application**. The cause is that the domain has no **Space default execution role**, which every shared space needs. Steps 1 and 2 require domain administrator access. If you aren't a domain administrator, ask one to do them.  

1. Stop every application running in the domain's shared spaces. For more information about stopping applications, see [Edit domain settings](domain-edit.md).

1. Set the **Space default execution role**. For instructions on setting the role, see [Add shared space support to an existing domain](domain-space-create.md#domain-space-add).

1. Refresh Studio in your browser.

1. Open the Label Studio application page.

1. Choose **Launch application**.
For information about what the role must not have, see [AWS Identity and Access Management for labeling spaces](label-studio-security.md#label-studio-security-iam).

The agent cannot find a Label Studio application in my domain  
Nobody has started the space yet. This step uses an application that is already running and does not create one. Open **Label Studio** from the **Applications** list in Studio, wait for the space to reach **Running**, then ask again.

The first request after the space starts is slow  
The space is still starting up, which takes a minute or two. Wait for the status on the application page to read **Running** before sending annotators their links.

An annotator's link shows an error page  
Which link it is decides what went wrong. A presigned sign-in link that reports an invalid or expired token has already been used, or has passed its 5-minute window, or was opened in a browser that already held another Studio session. Create a fresh one only when the annotator is ready to open it, and have them open it in a new or private window. A project link has no 5-minute window and no single use, so for that one check instead that the projects have been created and that the annotator has signed in to Studio and opened the Label Studio application first. An annotator who can sign in to AWS themselves can also reach the project without a link, as described in [What an annotator does](#ai-data-preparation-hil-use-annotator).

An annotator loses their session partway through labeling  
A presigned sign-in link grants a session that lasts up to 12 hours. When that session ends, the annotator has to sign in again. Create a new presigned link for them, or have them open the Label Studio application from Studio if they can sign in to AWS themselves. Creating a link is immediate, so the annotator can sign in as soon as you send it. The annotations they already submitted are unaffected.

An annotator cannot open the application at all  
Their user profile is in a different domain from the application, or their identity is not permitted to open a Studio session. The annotator must have a user profile in the same domain; if they do not, a domain administrator has to create one. For the permissions each identity needs, see the Label Studio security information at the end of this topic.

An annotator worked in someone else's project  
Nothing prevents this: the edition has no role-based access control, so every project is open to every member of the space, and annotations are attributed to whoever submitted them. Their answers are recorded under their own name in the wrong project, which means another annotator's share now holds decisions that person did not make. Ask for progress to see where the submissions landed, and decide whether to keep them.  
What happens to an answer you discard depends on where the records came from. For records that came from auto-labeling, a discarded answer has to be labeled again rather than simply dropped, because auto-labeling folds the annotations back into its own seed and spot-check and needs a trusted label for every record. The agent asks which annotator relabels the discarded records and sets up one more project in the shared space for that round, which stays there like the others. For records from any other input, you choose instead whether the discarded records keep the label they arrived with or are left out of the merge.

Saves are slow while several annotators are working at once  
This is the concurrency ceiling: the database takes one writer at a time, so simultaneous saves queue. Stagger the annotators across the day so that fewer of them are saving at the same moment. For the ceiling itself, see Limits and quotas earlier in this topic.

Saves are slow while only one or two annotators are working  
Suspect the storage volume instead. The application page shows the size you configured rather than how much is used, so compare your sizing estimate against it. Then stop the space, set a larger size, and start it again.

Everyone's labeling session ended at once  
Someone chose **Stop space**, which is available to anyone who can open the shared application. Submitted annotations are not lost; start the space again and annotators can continue from where they left off.

The questions annotators see are not the ones I want  
Ask for the change and have the projects regenerated. The agent creates new projects with the new interface, and the previous ones are left in place rather than deleted, so no submitted work disappears. The new projects carry a new review run in their titles, which is what tells them apart from the earlier ones. The earlier projects stay in the space until someone deletes them in Label Studio. Do this before annotators start rather than after, so nobody answers questions you are about to replace.

An annotator will not finish their share  
Ask for progress to see how many of their records are outstanding. You can apply the corrections that exist. In that case, unanswered records keep the label they arrived with. You can instead ask for the remaining records to be split again across the annotators who are available, which creates new projects and leaves submitted work in place.

The storage volume is filling faster than my estimate  
Exports are the usual reason: each one leaves a copy on the volume and nothing removes them. See the volume guidance in Limits and quotas earlier in this topic, and enlarge the volume while the space is stopped if you need the room.

## Where you go next
<a name="ai-data-preparation-hil-next"></a>

Human-reviewed labels are the end of data preparation and the start of the model work. After you register the corrected records, that new dataset version is what you fine-tune or evaluate against. For the full set of data preparation steps and where this one sits among them, see [Preparing Data with SageMaker AI Data Preparation](ai-data-preparation.md).
+ **Fine-tuning.** Settling the uncertain rows by hand reduces the number of incorrect labels in the training set.
+ **Evaluation.** A held-out split whose labels were all decided by people gives a score that does not depend on the accuracy of the automated labeling.
+ **Another pass at labeling.** Corrections that cluster in particular classes often point at the labeling instructions rather than at the annotators. Tighten the rules that separate the classes being confused, then label again. For more information, see [Auto-labeling](ai-data-preparation-autolabel.md).

## Related information
<a name="ai-data-preparation-hil-related"></a>
+ [Auto-labeling](ai-data-preparation-autolabel.md) – produces the confidence scores that decide which records need review.
+ [Data transformation](ai-data-preparation-dt.md) – applies the corrections to your dataset and registers the new version.
+ [Data quality evaluation](ai-data-preparation-dq.md) – can flag the records that are worth a person's time in the first place.
+ [Get started with SageMaker AI Data Preparation](ai-data-preparation-getting-started.md) – setting up the environment that the coding assistant runs in.
+ [Security in Label Studio labeling spaces](label-studio-security.md) – the access boundary, the permissions each identity needs, and data protection.
+ [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/) – what a running space and its storage volume cost.
+ [Label Studio documentation on the Label Studio website](https://labelstud.io/guide/) – the labeling interface itself, maintained by its open-source project.