# Overview

AWS has helped New Zealand organisations innovate, succeed, and grow globally since 2013.
There are thousands of active customers using AWS every month. Some customers have asked us
how to use AWS in support of indigenous data, and specifically Māori data. They have also
asked what considerations they can make to support Māori digital aspirations and interests.
These interests include protecting data that is considered taonga, or a treasured possession. In
other cultures, this can mean sacred data. Other customer interests include how data is made
available to Māori and how tools are developed, so that they can use their data to deliver
better outcomes to themselves, their communities, and Aotearoa New Zealand.

We developed this document together with Māori advisers as a practical resource for customers working with Māori data, recognising the importance of Te Tiriti o Waitangi, the Treaty of Waitangi. This is the first published
AWS lens that focuses on indigenous data. This document is intended for those in technology
and data roles, such as chief technology officers (CTOs), chief information security officers
(CSOs/CISOs), architects, developers, and operations managers.

## Pillars of the Well-Architected

Framework

The Well-Architected Framework consists of six pillars: operational excellence, security,
reliability, performance efficiency, cost optimisation and sustainability. The Framework
describes key concepts, design principles, and architectural best practices for designing and
running workloads in the cloud. The following sections provide an overview of each pillar,
important design principles, and other considerations for your organisation as it relates to
Māori data.

## Purpose

This lens is not a comprehensive guide, but instead is based on AWS and customer best
practices, combined with Māori data considerations. It is not intended to be an authoritative,
prescriptive checklist. Instead, it provides a technology-focused perspective that centres
around designing, building, and operating technology solutions. This document does not replace
the value of working with cultural advisors that have cultural knowledge and specific context
of the data. This document was developed with Māori advisers that have a deep understanding of
Māori data interests, but it should not replace other consultations with your Māori customers
that have relevant cultural context of the data or their specific tikanga (protocol) over that
data.

An AWS Well-Architected Framework lens is designed to be a specific way of looking at
or applying the [AWS Well Architected Framework](../framework/welcome.md "../framework/welcome.md")
and its six pillars. By using the lens, you can learn architectural best practices for
designing and operating reliable, secure, efficient, cost-effective, and sustainable
applications and software in the cloud. It provides a way to consistently measure your cloud
environment against best practices and identify areas for improvement. Applying
Well-Architected Framework best practices to your workload increases the likelihood of
business success and protection of cultural and historical knowledge. We developed specific
domain lenses, such as the [Government Lens](../government-lens/government-lens.md "../government-lens/government-lens.md"),
the [Healthcare Lens,](../../../pdfs/wellarchitected/latest/healthcare-industry-lens/healthcare-industry-lens.md#healthcare-industry-lens "../../../pdfs/wellarchitected/latest/healthcare-industry-lens/healthcare-industry-lens.md#healthcare-industry-lens") or the [Financial
Services Industry Lens](../financial-services-industry-lens/welcome.md "../financial-services-industry-lens/welcome.md").

Guidance and lenses are intended to help AWS customers and other organisations reflect
on their data policies and principles in the context of the industry or sector they operate
in. This document outlines general design principles, best practices, and specific guidance
for the pillars of the Framework. It offers a way to understand AWS best practices and how
these may be considered in relation to important Māori data considerations. You can apply this
lens to a workload in isolation. However, we recommend applying this lens in addition to a
Well-Architected Framework Review to fully evaluate your workload.

## AWS bringing

infrastructure to Aotearoa New Zealand

On 22 September 2021, AWS announced that the new AWS Asia Pacific (Auckland) Region.
The Region adds to the continuing AWS investment in and commitment to Aotearoa New Zealand,
and the long-term potential for New Zealand to be a leader in the global digital economy. This
region will have three Availability Zones and can provide local customers with a preference to
securely store their data in New Zealand, as well as provide even lower latency to users. We
hope customers can take advantage of this significant investment in New Zealand and the
relevant data controls to meet the needs of our Māori customers with specific data
preferences. It can also support organisations to leverage advanced technologies such as
artificial intelligence including generative AI, machine learning, internet of things (IoT),
and mobile services to drive innovation. Customers can start building out their workloads in
an existing Region now, and work with AWS or a trusted partner to get architectural and
implementation guidance that facilitates a transition to the Auckland Region in the future.

## Additional context

The first step in your Well-Architected Framework Review is deciding if you want to
separately identify Māori data from other data. From there, you can decide on a classification
system to help you identify what Māori data you already have or are intending to collect. To
do this, your organisation needs to decide on a robust definition for what is Māori data, as
well as a mechanism to help you potentially classify, within the context of your organisation,
what is and what isn't Māori data. Your organisation can also decide if it is appropriate or
not for you to start identifying data as Māori and non-Māori, and what are the specific legal
considerations you might wish to take. You can speak with Māori data specialists about this.
After you have decided to identify data separately as Māori data, you may choose to decide on
a data classification system to drive your technology choices, data governance frameworks, and
security best practices over different types of Māori data. For more information, see the
[Security Pillar](security.md "security.md").

The definitions provided in this guidance are just a starting point. Other organisations
may publish Māori data classification guidelines that you could also use as a reference. To
get you started, we suggest you look at this from some practical angles:

- Has the data been provided by someone who has identified themselves as Māori?
- Will this data be distinctly useful for Māori because it has to do with their
  community, environment or wellbeing?
- Does this data relate to a Māori individual or community that holds value to that
  individual or community?

This list of considerations is not exhaustive, and these questions may take time for your
organisation to answer. We strongly encourage you to speak with Māori data experts about your
specific context and about what data you have collected or intend to collect. This discovery
process can help you set up appropriate mechanisms for stewarding Māori data. At the heart of this is the importance of the Treaty of Waitangi (Te Tiriti o Waitangi), signed between the British Crown and more than 500 Māori chiefs in 1840. The New Zealand Government’s Cloud First policy acknowledges the Treaty and has Te Tiriti-based principles for government agencies using public cloud.

This lens is just one tool for supporting customers in considering good practices. This
lens should not be regarded as static or a stand-alone solution, and does not seek to convey
that there is any single best approach for working with Māori data. AWS reviews and updates
guidance and content continually as best practices evolve over time and we welcome feedback on
this document for future revisions. Where appropriate, this guidance also includes wider
organisational aspects technology and data teams can also consider.
