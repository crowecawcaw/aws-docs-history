# Provide supporting text

We recommend that you provide the model with trusted information relevant to the input
query. This information, along with the input query, is generally a part of the system
called _retrieval augmented generation (RAG)_. In this process some
relevant, contextual document or information is augmented to the actual user prompt so that
the model gets trustworthy content to generate a relevant and accurate response. Instructing
Amazon Nova to answer using a reference text from a trusted source can guide it to compose its
response based on the provided material and ensure that its response is grounded in accurate
and relevant information, enhancing the reliability and credibility of the generated
content.

Additionally, using a reference text can help avoid hallucinating, thereby improving the
overall quality and trustworthiness of the responses. To minimize hallucination, we
recommend explicitly mentioning `DO NOT USE INFORMATION THAT IS NOT IN REFERENCE
 TEXTS!` in your model instructions.

**Prompt template:**

```
`User: {Query}
Resource: Search Results: {Reference texts}`
```

Providing grounding context helps to prevent the model from hallucinating or
refusing to answer.

| Role | Prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User | **Question:**<br>What were the economic impacts of the COVID-19 pandemic on the<br>United States in 2020?<br>**Reference Text:**<br>In 2020, the United States experienced significant economic<br>impacts due to the COVID-19 pandemic. The U.S. economy contracted by<br>3.5% in 2020, according to the Bureau of Economic Analysis.<br>Unemployment rates surged to 14.7% in April 2020, the highest since<br>the Great Depression, before gradually declining. Small businesses<br>faced severe challenges, with millions of firms closing permanently.<br>Additionally, consumer spending dropped sharply as people reduced<br>non-essential expenditures and saved more. Government intervention<br>played a critical role in mitigating these impacts through stimulus<br>packages and support programs, such as the Paycheck Protection<br>Program (PPP) for small businesses and direct payments to<br>individuals. Despite these measures, the economic recovery remained<br>uneven across different sectors and regions. |
