

# What is Amazon Connect Talent?
<a name="what-is-talent"></a>

Amazon Connect Talent is an agentic AI hiring solution built for talent acquisition leaders managing scaled hiring. It delivers AI-led interviews, science-backed assessments, and consistent evaluation, helping recruiters hire high quality candidates faster while providing applicants with a flexible interview experience that reduces human preconceptions.

This guide is for administrators. It describes how to set up and manage Amazon Connect Talent. For tasks that recruiters perform day to day, such as creating evaluations and reviewing candidate results, see the [Amazon Connect Talent User Guide](https://docs.aws.amazon.com/talent/latest/userguide/what-is-talent.html).

**Topics**
+ [Features of Amazon Connect Talent](#talent-features)
+ [Evaluations](#talent-evaluations-overview)
+ [AI-led interviews](#talent-interviews-overview)
+ [Assessments](#talent-assessments-overview)
+ [Supported Regions and endpoints](#talent-regions-endpoints)
+ [Supported languages](#supported-languages)
+ [Accessibility](#talent-accessibility)

## Features of Amazon Connect Talent
<a name="talent-features"></a>

Amazon Connect Talent provides the following features that you administer:
+ **AI-generated candidate evaluations** – Recruiters create evaluations that use assessments, an AI-led interview, or both to measure candidates against a job's competencies.
+ **Applicant tracking system (ATS) integration** – Connect your ATS to synchronize jobs and candidates and to return evaluation results.
+ **SAML-based single sign-on** – Use your existing identity provider to give users single sign-on access to Amazon Connect Talent.
+ **User management and security profiles** – Add users and control what they can do with role-based security profiles.
+ **Knowledge bases** – Add your company values and information to personalize candidate evaluations.
+ **Candidate-facing branding** – Personalize the candidate experience with your organization's name, logo, and color.
+ **Data governance** – Review encryption, data residency, and data retention policies, and request changes to meet your compliance requirements.

## Evaluations
<a name="talent-evaluations-overview"></a>

An evaluation is how Amazon Connect Talent measures a candidate for a job. An evaluation can include an AI-led interview, assessments, or both. A recruiter builds an evaluation with a step-by-step builder: they select or describe a job, and Amazon Connect Talent generates a draft evaluation. The draft is organized into three parts:
+ **Overview** – The job, the key competencies to measure, and the evaluation language.
+ **Assessments** – A set of digital tests selected for the job's competencies.
+ **AI-led interview** – A set of behavioral questions grouped by competency.

Recruiters review and adjust the draft, then publish it. A published evaluation can be sent to candidates. For how Amazon Connect Talent generates evaluation scoring and criteria, see [Managing evaluations](managing-evaluations.md).

## AI-led interviews
<a name="talent-interviews-overview"></a>

The AI-led interview is a set of behavioral questions that Amazon Connect Talent generates for each competency a job requires. During the interview, Amazon Connect Talent will ask dynamic follow-up questions to explore a candidate's answer. Every question is tagged with the competency it measures and includes a short rationale. Amazon Connect Talent writes questions to be clear, fair, and focused on a single competency, and it can generate them in multiple languages.

## Assessments
<a name="talent-assessments-overview"></a>

Assessments measure candidates against a job's competencies. Amazon Connect Talent reports assessment results on a four-level scale: Low, Moderate, High, and Very High. Amazon Connect Talent offers the following assessment types:
+ **Work approach** – Measures how a candidate approaches their work.
+ **Problem solving** – Measures how a candidate works through problems.

For Work approach and Problem solving, recruiters see a per-competency breakdown and an overall fit summary. When a candidate does not provide enough signal on a competency, Amazon Connect Talent excludes it rather than guessing.

## Supported Regions and endpoints
<a name="talent-regions-endpoints"></a>

Amazon Connect Talent is available in the following AWS Regions. You create and manage your instance in a supported AWS Region, and your data resides in that AWS Region.


| Region name | Region code | 
| --- | --- | 
| US East (N. Virginia) | us-east-1 | 
| US West (Oregon) | us-west-2 | 

For the service endpoints and quotas that apply to Amazon Connect Talent, see [Endpoints and quotas for Amazon Connect Talent](endpoints-quotas.md).

## Supported languages
<a name="supported-languages"></a>

Amazon Connect Talent localizes two separate experiences: the recruiter experience and the candidate experience. The recruiter experience is the application that recruiters and administrators use. The candidate experience is the evaluation that candidates complete. These two experiences support different sets of languages. The candidate experience supports a different set of languages than the recruiter experience. Use the following tables separately, and do not assume the two sets match.

### Recruiter experience languages
<a name="supported-languages-recruiter"></a>

The recruiter experience supports the following languages.


| Language | English name | 
| --- | --- | 
| English | English | 
| Deutsch | German | 
| Español | Spanish | 
| Français | French | 
| Italiano | Italian | 
| 日本語 | Japanese | 
| 한국어 | Korean | 
| Português (BR) | Portuguese (Brazil) | 
| 中文 (简体) | Chinese (Simplified) | 
| 中文 (繁体) | Chinese (Traditional) | 

### Candidate experience languages
<a name="supported-languages-candidate"></a>

The candidate experience supports a different set of languages than the recruiter experience. An evaluation can be delivered to a candidate in the following languages.


| Language | Locale | 
| --- | --- | 
| English (United States) | en-US | 
| English (Australia) | en-AU | 
| English (United Kingdom) | en-GB | 
| Portuguese (Brazil) | pt-BR | 
| French (France) | fr-FR | 
| Italian (Italy) | it-IT | 
| German (Germany) | de-DE | 
| Spanish (United States) | es-US | 

## Accessibility
<a name="talent-accessibility"></a>

Amazon Connect Talent supports screen readers and keyboard navigation across the recruiter and candidate experiences. The AI-led interview, however, is not optimized for screen readers. Candidates who use a screen reader or other assistive technology incompatible with the AI-led interview can opt out and complete the remaining parts of the evaluation. Opting out keeps the candidate's application Active and preserves their place in your pipeline. For more information, see [How a candidate opts out](https://docs.aws.amazon.com/talent/latest/userguide/candidate-experience.html#candidate-experience-opt-out).