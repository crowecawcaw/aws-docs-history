# Provide examples (few-shot prompting)

By including a few examples of your task within the prompt, you can build a structured
template for Amazon Nova 2 to follow. This reduces ambiguity and enhances the accuracy and quality
of the output. The technique of providing clear examples to make the model's responses more
aligned with the desired outcome is called _few-shot prompting_.

The concept of few-shot prompting is to provide the language model with a few examples of
the task, along with the input and output format, and then ask it to generate the output for a
new input based on the provided examples. This method also helps in clarifying complex
instructions or tasks, making it easier for Amazon Nova 2 to understand and interpret what is being
asked.

**How adding examples to the prompt help:**

Adding examples can help the model with producing

- Consistent responses which are uniform to the style of the examples
- Performant responses due to reducing the chance of misinterpreting instructions, and
  minimizing hallucinations
  The amount by which model performance improves using few shot prompting will depend on the
  quality and diversity of your chosen examples. The following items demonstrate the
  characteristics of good shots in the prompt:

- **Select diverse examples**: The examples chosen should
  represent the distribution of your expected input/output in terms of diversity (ranging
  from common use cases to edge cases) to adequately cover relevant use cases. It is
  important to avoid any biases in your examples, as bias in the inputs can cause outputs to
  be biased as well.
- **Match complexity levels**: The complexity of the
  examples provided should align with the target task or scenario. It is important to make
  sure the complexity grade is mapped between expected the input and the chosen example in
  the prompt.
- **Ensure relevance**: The examples selected should be
  directly relevant to the problem or objective at hand. This ensures consistency and
  uniformity in responses.

###### Tip

If the above suggestions do not work, we recommended you build a RAG-based system that
augments the prompt with a dynamic selection of shots based on the similarities between the
user-input query and an available pool of shots.

Here, your user is trying to classify incoming customer support tickets into
predefined categories. You can provide Amazon Nova 2 models with a few examples of tickets
that are classified correctly to improve its understanding of the categories and the
language used in the tickets. The exemplar exampless should be concise and represent all
tasks targeted in your application. If there is a specific field name that is meaningful
to the tasks, such as `Ticket` or `Category` in this example, your
user can use those fields directly followed by a colon `":"`.

0-shot prompt
User:

```
Please classify the following customer support tickets into one of the categories: "Technical Issue," "Billing Inquiry," or "General Inquiry."

**Ticket:** "Can you explain why my latest bill is higher than usual? I haven't changed my plan."
```

Assistant:

```
The customer support ticket should be classified as a "Billing Inquiry."

 Here’s the reasoning:
 - The customer is asking about the reason for a change in their latest bill amount.
 - The context revolves around billing and payment, which falls under the category of "Billing Inquiry."
```

3-shot prompt
User:

```
Please classify the following customer support tickets into one of the categories: "Technical Issue," "Billing Inquiry," or "General Inquiry."
Use these examples to guide your classification:

**Ticket:** "I can't log in to my account. The system keeps giving me an error message."
**Category:** Technical Issue

**Ticket:** "I received an email saying my account will be suspended unless I make a payment. Is this a scam?"
**Category:** Billing Inquiry

**Ticket:** "What are the hours of operation for your customer support team?"
**Category:** General Inquiry

Now, classify the following ticket:
**Ticket:** "Can you explain why my latest bill is higher than usual? I haven't changed my plan."
```

Assistant:

```
Category: Billing Inquiry

Explanation: The ticket is asking for an explanation regarding a change in the billing amount, which falls under the billing category as it pertains to questions about charges or payments.
```

In this example, the exemplars are provided as turns, one turn per exemplar, where the
`User` role contains the input and `Assistant` role contains the
expected output for that exemplar.

0-shot Prompt
System:

```
Your task is to Classify the following texts into the appropriate categories. The categories to classify are:

Categories:
- Food
- Entertainment
- Health
- Wealth
- Other
```

User:

```
I have 20$ in my pocket.
```

Assistant:

```
Category: Wealth

Explanation: The text mentions a specific amount of money, which falls under the category of wealth. The presence of a monetary value directly relates to financial status or economic aspect.

```

3-shot Prompt (as turns)
System:

```
Your task is to Classify the following texts into the appropriate categories. The categories to classify are:

Categories:
- Food
- Entertainment
- Health
- Wealth
- Other
```

User:

```
I love to eat pizza.
```

Assistant:

```
Food
```

User:

```
I enjoy watching movies.
```

Assistant:

```
Entertainment
```

User:

```
I am going to the gym after this.
```

Assistant:

```
Health
```

User:

```
I have 20$ in my pocket.
```

Assistant:

```
Wealth
```

In this example, you can specify an "Example" section and then list a series of
examples within the system prompt. This way of providing exemplars in the prompt is
especially useful if your exemplars are long and complex and helps model locate
example shots.

0-shot Prompt
System:

```
You are an AI assistant helping to draft professional reports for enterprise stakeholders. Ensure the report is formatted in rich text, with headings, bullet points, and highlighted important tasks.
```

User:

```
Draft a detailed project update report for our stakeholders, summarizing the project milestones achieved, tasks completed, and future plans.
```

Assistant:

```
# Project Update Report

## Executive Summary
This report provides a comprehensive update on the project milestones achieved, tasks completed, and future plans. Our team has made significant progress, and we are on track to meet the project goals. The following sections outline the details of our accomplishments and upcoming activities.

---

## Project Milestones Achieved

### **1. Project Initiation**
- **Milestone Date:** July 15, 2023
- **Description:** Completed initial project planning and secured stakeholder approval.

### **2. System Design Completion**
- **Milestone Date:** September 30, 2023
- **Description:** Finished the detailed system design and received positive feedback from technical review meetings.

### **3. Prototype Development**
- **Milestone Date:** November 15, 2023
- **Description:** Developed and tested a working prototype of the system.

---

## Tasks Completed

### **1. Requirement Gathering**
- **Description:** Conducted comprehensive stakeholder interviews and collected detailed requirements.
- **Highlighted Important Tasks:**
  - **User Story Mapping:** Mapped out user stories to ensure all user needs are addressed.
  - **Requirement Documentation:** Created detailed requirement specifications.

### **2. System Architecture Design**
- **Description:** Designed the system architecture, focusing on scalability and maintainability.
- **Highlighted Important Tasks:**
  - **Technology Stack Selection:** Chose the appropriate technology stack based on project requirements.
  - **Architecture Diagrams:** Developed detailed architecture diagrams for easy understanding.

### **3. Prototype Development and Testing**
- **Description:** Developed and rigorously tested the prototype.
- **Highlighted Important Tasks:**
  - **Coding:** Implemented core functionalities of the prototype.
  - **Testing:** Conducted unit and integration testing to ensure prototype reliability.

---

## Future Plans

### **1. Full System Development**
- **Description:** Begin the full-scale development of the system based on the approved design and prototype.
- **Highlighted Important Tasks:**
  - **Module Development:** Develop each module as per the design specifications.
  - **Code Reviews:** Implement regular code reviews to maintain code quality.

### **2. User Acceptance Testing (UAT)**
- **Description:** Conduct UAT to ensure the system meets user requirements and is ready for deployment.
- **Highlighted Important Tasks:**
  - **Test Plan Development:** Create detailed UAT plans and test cases.
  - **UAT Execution:** Execute UAT and gather feedback for final adjustments.

### **3. Deployment and Training**
- **Description:** Deploy the system and provide necessary training to end-users.
- **Highlighted Important Tasks:**
  - **Deployment:** Roll out the system to the production environment.
  - **Training Sessions:** Organize training sessions for users to familiarize them with the new system.

---

## Conclusion
Our project has successfully achieved key milestones and completed significant tasks. With the current momentum, we are well-positioned to meet our future objectives. We remain committed to delivering a high-quality system that meets all stakeholder expectations.

---

**Prepared by:**
[Your Name]
[Your Position]
[Date]

**Contact Information:**
[Your Email]
[Your Phone Number]

---

This detailed update aims to keep stakeholders informed and reassured about the project's progress and future direction. For any queries or further information, please do not hesitate to contact me directly.
```

2-shot Prompt
System:

```
You are an AI assistant helping to draft professional reports for enterprise stakeholders. Below are a few examples of well-formatted project update reports to guide your response.

<Example 1>

<b>Project Update Report</b><br>
<i>Date:</i> January 15, 2023<br>
<hr>


<b>Project Milestones Achieved:</b><br>
- Successfully launched the new CRM system.<br>
- Integrated the marketing automation tool.<br>
- Completed the employee training sessions.

<b>Tasks Completed:</b><br>
- Developed the user manual.<br>
- Conducted system testing.<br>
- Prepared the training materials.

<b>Future Plans:</b><br>
- Roll out the CRM system to all departments.<br>
- Schedule follow-up training sessions.<br>
- Monitor system performance and make necessary adjustments.

<hr>
<b>Prepared by:</b><br>
[Your Name]<br>
[Your Position]<br>
[Your Contact Information]

<Example 2>

<b>Project Update Report</b><br>
<i>Date:</i> February 20, 2023<br>
<hr>

<b>Project Milestones Achieved:</b><br>
- Launched the new website.<br>
- Completed the SEO optimization.<br>
- Organized the stakeholder meeting.

<b>Tasks Completed:</b><br>
- Designed the website layout.<br>
- Wrote the content for the website.<br>
- Tested the website functionality

<b>Future Plans:</b><br>
- Implement the analytics tracking.<br>
- Launch the social media campaign.<br>
- Gather feedback from stakeholders.

<hr>
<b>Prepared by:</b><br>
[Your Name]<br>
[Your Position]<br>
[Your Contact Information]
```

User:

```
Draft a detailed project update report for our stakeholders, summarizing the project milestones achieved, tasks completed, and future plans.
```

Assistant:

```
<b>Project Update Report</b><br>
<i>Date:</i> October 5, 2023<br>
<hr>

<b>Project Milestones Achieved:</b><br>
- Successfully completed the implementation of the new enterprise resource planning (ERP) system.<br>
- Conducted and completed the first phase of the data migration process.<br>
- Successfully launched the new inventory management module.

<b>Tasks Completed:</b><br>
- Developed and finalized the comprehensive user training program, including detailed user manuals and video tutorials.<br>
- Conducted extensive system integration testing with all existing systems and ensured seamless interoperability.<br>
- Executed the initial data migration from the legacy system to the new ERP system, resulting in a 95% accuracy rate.

<b>Future Plans:</b><br>
- Roll out the new ERP system to all departments in the next two phases.<br>
- Schedule and conduct follow-up training sessions for all employees.<br>
- Implement the remaining modules of the ERP system, including financial management and human resources.<br>
- Establish a robust monitoring and support framework to ensure smooth system operation and address any issues promptly.

<hr>
<b>Prepared by:</b><br>
[Your Name]<br>
[Your Position]<br>
[Your Contact Information]

---

This detailed report provides a clear and concise overview of the project's progress, highlighting the milestones achieved, tasks completed, and future plans. It ensures stakeholders are well-informed and can make strategic decisions based on the current status of the project.
```
