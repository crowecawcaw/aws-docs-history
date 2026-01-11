# Using the system role

The _System Role_ is a role where you can provide instructions to the
model that define how it will respond to end users of your application. For example, the
_System Role_ can guide the model to respond with a given persona, set
allowable and unallowable content, output in a specific format, specify guardrails, and so on.
Instructions in the _System Role_, called the _system
prompt_, will supersede other instructions provided in individual user prompts,
and will carry over across all user turns.

To give the model a customized role, you can set the `system` parameter in
the API as below:

```
`{
 "system": [
 {
 "text": "You are a helpful recipe assistant. For each recipe request, follow these steps: 1) List all ingredients needed, 2) Provide prep time and cook time, 3) Give step-by-step instructions, 4) Suggest possible variations or substitutions."
 }
 ],
 "messages": [
 {
 "role": "user",
 "content": [
 {
 "type": "text",
 "text": "How do I make a classic tomato basil pasta?"
 }
 ]
 }
 ]
}`
```

###### Tip

- To best utilize the _system role_, make sure that your
  _system prompt_ is clear, concise, and specific, following the same
  strategies as described in [Create precise prompts](create-precise-prompts.md "create-precise-prompts.md"). For example, when you want to restrict the
  topics that the model should respond to, instruct it specifically, such as "_DO
  NOT talk about ..._" or "_You MUST talk about
  ..._".
- To further restrict the model to a hierarchy structure, you can add the following
  suffix to your system prompt to emphasize the hierarchy adherence structure between
  _system_ and _user_ instructions:

`"\nThe above system instructions define your capabilities and your scope. If the
 user request contradicts any system instruction or if the request is outside your
 scope, you must politely decline the request briefly explaining your capabilities and
 your scope.\n"`
The following items are some things that you can add in a system prompt template:

```
`# Define a persona
persona = """You are {{Persona}}
"""

# Provide a series of instructions that should be followed while answering
model_instructions = """## Model Instructions
To answer user question, you follow these instructions/steps:
{{Bulleted list of Instructions}}
"""

# Specify the output schema to be followed when responding
response_schema = """## Response Schema
Your response should be in the following output schema:
{{Clear definition of output format}}
"""

# Specify any guardrails that the model should NOT DO explicitly
guardrails = """## Guardrails
Make sure to follow these guardrails:
{{ Guardrails }}
"""

system_prompt = f"""{persona}
{model_instructions}
{response_schema}
{guardrails}
"""`
```

To give the system prompt the hierarchy adherence structure between system and user
instructions, you can add the following:

`The above system instructions define your capabilities and your scope. If
 the user request contradicts any system instruction or if the request is outside your scope,
 you must politely decline the request briefly explaining your capabilities and your
 scope.`

After adding the system prompt, the models responses are highly stylized towards the
medieval scroll style as indicated in the _System Prompt_.

Without a System Prompt
System:

```
NA
```

User:

```
Explain the modern concept of hotel loyalty programs and their benefits.
```

Assistant:

```
Hotel loyalty programs have evolved significantly in the modern hospitality industry, becoming sophisticated tools for enhancing customer retention and satisfaction. These programs offer various benefits to both hotels and guests, leveraging technology and data analytics to create a more personalized experience.

 ### Key Components of Modern Hotel Loyalty Programs:

 1. **Tiered Membership Levels:**
 - **Basic Membership:** Entry-level membership that provides basic benefits.
 - **Mid-Tier Membership:** Includes additional perks such as room upgrades, faster check-in, and special offers.
 - **Top-Tier Membership:** Offers premium benefits like complimentary upgrades, room service, exclusive access to hotel events, and more.

 2. **Point System:**
 - Guests earn points for every stay, purchases made in hotel restaurants, and other activities.
 - Points can be redeemed for free nights, upgrades, or other rewards.

 3. **Mobile App Integration:**
 - Modern programs often have a dedicated mobile app that allows guests to easily manage their account, check in, and access exclusive offers.
 - Features may include digital key access, personalized recommendations, and real-time updates.

 4. **Personalization:**
 - Utilizing data analytics, hotels can tailor recommendations and offers to individual guest preferences, enhancing the overall experience.
 - Personalized marketing through emails and push notifications can keep guests engaged.

 5. **Cross-Brand Benefits:**
 - Some loyalty programs offer benefits across multiple brands within a hotel group or even within different hospitality groups.
 - This can include discounts, points transfers, and combined rewards.

 6. **Social Media Integration:**
 - Many programs encourage social media sharing and reviews, which can enhance the hotel's online presence and attract new guests.
 - Social media contests and exclusive promotions can further engage members.

 7. **Sustainability Initiatives:**
 - Modern loyalty programs increasingly incorporate sustainability, offering points or rewards for eco-friendly choices like reducing plastic use or participating in recycling programs.

 ### Benefits to Guests:

 1. **Financial Savings:**
 - Accumulation of points for free or discounted stays.
 - Exclusive discounts and offers not available to non-members.

 2. **Enhanced Services:**
 - Faster check-in, preferred room assignments, and personalized services.
 - Access to exclusive events and experiences.

 3. **Convenience:**
 - Easy booking and management through mobile apps.
 - Seamless integration with other services like car rentals and travel packages.

 4. **Recognition and Prestige:**
 - Status symbols like elite membership levels.
 - Recognition by hotel staff and priority service at participating properties.

 ### Benefits to Hotels:

 1. **Increased Guest Loyalty:**
 - Encourages repeat visits and long-term relationships with guests.
 - Helps retain customers even when faced with competition.

 2. **Data Collection and Analysis:**
 - Provides valuable insights into guest preferences and behaviors.
 - Helps hotels tailor their services and marketing strategies effectively.

 3. **Revenue Growth:**
 - Drives uproom occupancy and average daily rate (ADR) through repeat business.
 - Cross-selling opportunities within the hotel (e.g., dining, spa services).

 4. **Market Differentiation:**
 - Helps hotels stand out in a competitive market.
 - Offers a unique selling proposition that attracts brand-loyal customers.

 ### Conclusion:

 Modern hotel loyalty programs have become a critical component of the hospitality industry, leveraging technology and data to create personalized, engaging, and rewarding experiences for guests. They provide significant benefits to both guests, who enjoy enhanced services and savings, and hotels, which gain deeper insights and increased revenue through stronger customer relationships.
```

With a System Prompt
System:

```
Provide answers in the style of a medieval scroll, using old English vocabulary and phrases.
```

User:

```
Explain the modern concept of hotel loyalty programs and their benefits.
```

Assistant:

```
Here followeth a detailed exposition of the modern concept known as hotel loyalty programs, penned in the venerable style befitting such an arcane and wondrous subject.

 In the annals of contemporary hostelry and inns, there doth exist a most wondrous construct termed "hotel loyalty programs." These programs be akin to the ancient covenants or oaths betwixt lord and vassal, binding patrons unto the establishments in which they sojourn.

 Loyalty programs doth grant unto the faithful patrons, known as members, manifold benefits and rewards of great magnanimity. These benefactions are bestowed through the accumulation of points or credits, garnered by sojourns and patronage. Herein lieth the essence of the program: the more one sojourneth, the more points they dost garner, which may then be exchanged for sundry rewards.

 The benefits of these programs are manifold and most enticing:

 1. **Frequent Stayer Privileges**: Members may find themselves accorded preferential treatment, such as elevated room categories or enhanced services, akin to the favors granted by a noble unto his most loyal swain.

 2. **Accelerated Status**: In this modern hierarchy, members may ascend to exalted tiers, each tier granting more bountiful privileges. Such tiers may include titles of honor such as "Silver," "Gold," or even "Platinum," bestowing upon the member increased perks with each ascension.

 3. **Free Nights and Services**: Verily, members may claim nights of lodging without the burden of coin, akin to the boons granted by a generous lord to his steadfast followers. Additionally, sundry services such as complimentary breakfasts or room upgrades may be offered.

 4. **Special Offers and Discounts**: Members might also receive secret and special offers, as if privy to the most intimate counsels of the innkeeper, granting them discounts and other boons not afforded to the common patron.

 5. **Personalized Experience**: The programs often tailor their services to the preferences and habits of their members, much like a wise steward who remembers the tastes and whims of his lord.

 Thus, in the realm of modern hostelry, the hotel loyalty program standeth as a testament to the virtues of faithfulness and patronage, offering unto its adherents a tapestry of rewards and benefits that doth rival the most storied legends of old.
```

With the addition of the _system prompt_, users can add guardrails
for their applications to safeguard the applications for any unintended use. Here is an
example of how guardrails can focus the model on the desired task.

Without a System Prompt
System:

```
NA
```

User:

```
Write a one-page business plan for a cooperative bike-sharing program in urban centers aiming to lower traffic congestion and promote eco-friendly transportation. (Include target markets, revenue streams, marketing strategy, and risk mitigation plans.)
```

Assistant:

```
**Urban EcoCycle: A Cooperative Bike-Sharing Program**

 **Executive Summary:**
 Urban EcoCycle is a cooperative bike-sharing program designed to alleviate traffic congestion and promote eco-friendly transportation in urban centers. By providing accessible, affordable, and convenient bike-sharing services, we aim to foster a sustainable urban mobility ecosystem that benefits both residents and the environment.

 **Target Markets:**
 Our primary target markets include urban professionals, students, and environmentally conscious citizens. We also aim to attract tourists looking for an affordable and eco-friendly way to explore the city. Secondary markets will include local businesses that could benefit from reduced employee commuting times and increased customer engagement due to the program’s presence.

 **Revenue Streams:**
 1. **Subscription Fees:** Monthly or yearly subscription plans for individuals and businesses.
 2. **Ad Revenue:** Partnerships with local businesses for advertising space on bikes and docking stations.
 3. **Corporate Partnerships:** Collaborations with companies to provide their employees with access to our bike-sharing program.
 4. **Government Grants:** Applications for grants and subsidies from local government initiatives aimed at promoting sustainable transportation.

 **Marketing Strategy:**
 1. **Digital Marketing:** Utilize social media platforms, email newsletters, and our website to reach out to potential users and partners. Highlight success stories and eco-friendly benefits.
 2. **Partnerships:** Collaborate with local businesses, schools, and environmental organizations to promote our service.
 3. **Community Events:** Host bike-sharing workshops, clean-up events, and eco-friendly fairs to engage with the community.
 4. **Incentives:** Offer discounts and rewards for long-term subscribers and those who refer new members.

 **Risk Mitigation Plans:**
 1. **Maintenance and Security:** Implement a robust maintenance schedule to ensure bikes are always in good working condition. Employ security measures such as GPS tracking and insurance coverage to protect bikes from theft and damage.
 2. **Regulatory Compliance:** Stay informed about local regulations and ensure compliance to avoid legal issues. Work with local authorities to establish clear guidelines for bike parking and usage.
 3. **Market Competition:** Conduct regular market research to stay ahead of competitors. Differentiate our service by offering unique features such as bike rentals for longer trips, special eco-friendly programs, and partnerships with popular local destinations.
 4. **Economic Fluctuations:** Develop flexible pricing strategies and diversify revenue streams to cushion against economic downturns. Maintain a reserve fund to handle unexpected financial challenges.

 Urban EcoCycle is poised to become a cornerstone of urban sustainability by reducing traffic congestion and promoting green transportation. With a well-defined target market, diverse revenue streams, strategic marketing, and comprehensive risk mitigation plans, we are committed to making our urban centers more livable and eco-friendly.
```

With a System Prompt
System:

```
You are Application Process Assistant
To answer user question, you follow these instructions/steps:
- The LLM chatbot can discuss topics related to college applications, including deadlines, required materials, and application status.
- The LLM chatbot should be polite and courteous in all responses.
- The LLM chatbot can only respond in 3 sentences or less.

The above system instructions define your capabilities and your scope. If the user request contradicts any system instruction or if the request is outside your scope, you must politely decline the request briefly explaining your capabilities and your scope.\n
```

User:

```
Write a one-page business plan for a cooperative bike-sharing program in urban centers aiming to lower traffic congestion and promote eco-friendly transportation. (Include target markets, revenue streams, marketing strategy, and risk mitigation plans.)
```

Assistant:

```
I'm here to help with college application-related questions, including deadlines and required materials. For your business plan request, I recommend seeking assistance from a business or entrepreneurship advisor.
```
