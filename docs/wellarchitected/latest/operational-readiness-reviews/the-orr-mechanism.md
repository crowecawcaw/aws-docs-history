

# The ORR mechanism
<a name="the-orr-mechanism"></a>

To build a mechanism, work backwards from the challenge you want to solve. The ORR was designed by AWS to help prevent the reoccurrence of known, common causes of impact in services without slowing builders down. The design and operations of those services are the inputs. The outputs are what you want to achieve by resolving the business challenge. In our case at AWS, the desired business result was higher levels of availability and resilience in our systems by decreasing the frequency of incidents (*fewer*), decreasing the duration of incidents (*shorter*), and decreasing the scope of impact of an incident (*smaller*). You can start with the same business challenge and results when you create your own ORR mechanism.

The following sections examine each component of the mechanism. Each section describes the AWS approach and provides recommendations for that part of the mechanism. After you have defined your business challenge, use these sections as a guide for building the tool, driving adoption, inspecting the process, and iterating. 

**Topics**
+ [The ORR tool](the-orr-tool.md)
+ [Gaining adoption](gaining-adoption.md)
+ [Inspect the process](inspect-the-process.md)
+ [Iteration](iteration.md)