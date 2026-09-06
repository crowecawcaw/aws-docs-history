

# Amazon DynamoDB learning resources and tools
<a name="AdditionalResources"></a>

You can use the following additional resources to understand and work with DynamoDB.

**Topics**
+ [Tools for coding and visualization](#AdditionalResources.Tools)
+ [Prescriptive Guidance articles](#AdditionalResources.PrescriptiveGuidance)
+ [Knowledge Center articles](#AdditionalResources.KnowledgeCenter)
+ [Blog posts, repositories, and guides](#AdditionalResources.Guides)
+ [Data modeling and design pattern presentations](#AdditionalResources.DataModeling)
+ [Training courses](#AdditionalResources.Training)

## Tools for coding and visualization
<a name="AdditionalResources.Tools"></a>

You can use the following coding and visualization tools to work with DynamoDB:
+ [NoSQL Workbench for Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html) – A unified, visual tool that helps you design, create, query, and manage DynamoDB tables. It provides data modeling, data visualization, and query development features.
+ [Dynobase](https://dynobase.dev/) – A desktop tool that makes it easy to see your DynamoDB tables and work with them, create app code, and edit records with real-time validation.
+ [DynamoDB Toolbox](https://github.com/jeremydaly/dynamodb-toolbox) – A project from Jeremy Daly that provides helpful utilities for working with data modeling and JavaScript and Node.js.
+ [DynamoDB Streams Processor](https://github.com/jeremydaly/dynamodb-streams-processor) – A simple tool that you can use to work with [DynamoDB streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html).

## Prescriptive Guidance articles
<a name="AdditionalResources.PrescriptiveGuidance"></a>

AWS Prescriptive Guidance provides time-tested strategies, guides, and patterns to help accelerate your projects. These resources were developed by AWS technology experts and the global community of AWS Partners, based on their years of experience helping customers achieve their business objectives.

**Data modeling and migration**
+ [A hierarchical data model in DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/hierarchical-data-modeling.html)
+ [Modeling data with DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/welcome.html)
+ [Migrate an Oracle database to DynamoDB using AWS DMS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-to-amazon-dynamodb-using-aws-dms.html)

**Global tables**
+ [Using Amazon DynamoDB global tables](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/introduction.html)

**Serverless**
+ [Implement the serverless saga pattern with AWS Step Functions](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-the-serverless-saga-pattern-by-using-aws-step-functions.html)

**SaaS architecture**
+ [Manage tenants across multiple SaaS products on a single control plane](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-tenants-across-multiple-saas-products-on-a-single-control-plane.html)
+ [Tenant onboarding in SaaS architecture for the silo model using C\# and AWS CDK](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/tenant-onboarding-in-saas-architecture-for-the-silo-model-using-c-and-aws-cdk.html)

**Data protection and data movement**
+ [Configure cross-account access to Amazon DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html)
+ [Full table copy options for DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/)
+ [Disaster recovery strategy for databases on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/)

**Miscellaneous**
+ [Help enforce tagging in DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/help-enforce-dynamodb-tagging.html)

**Prescriptive guidance video walkthroughs**
+ [Using Serverless Architecture to Create Data Pipelines](https://youtu.be/JiWHomdh1oI?)
+ [Novartis - Buying Engine: AI-powered Procurement Portal](https://youtu.be/vp8oPiHN4cA)
+ [Veritiv: Enable Insights to Forecast Sales Demand on AWS Data Lakes](https://youtu.be/jg85DzUZ9Ac)
+ [mimik: Hybrid Edge Cloud Leveraging AWS to Support Edge Microservice Mesh](https://youtu.be/-S-R7MWRpaI)
+ [Change Data Capture with Amazon DynamoDB](https://youtu.be/6YVjzD-70p4)

For additional Prescriptive Guidance articles and videos for DynamoDB, see [Prescriptive Guidance](https://tiny.amazon.com/fiui3cog/ForinternaldemoofnewpageExternalURLwillbeneededforlive). 

## Knowledge Center articles
<a name="AdditionalResources.KnowledgeCenter"></a>

The AWS Knowledge Center articles and videos cover the most frequent questions and requests received from AWS customers. The following are some current Knowledge Center articles on specific tasks that relate to DynamoDB:

**Cost optimization**
+ [How do I optimize costs with Amazon DynamoDB?](https://repost.aws/knowledge-center/dynamodb-optimize-costs)

**Throttling and latency**
+ [How can I troubleshoot high latency on an Amazon DynamoDB table?](https://repost.aws/knowledge-center/dynamodb-high-latency)
+ [Why is my DynamoDB table being throttled?](https://repost.aws/knowledge-center/dynamodb-table-throttled)
+ [Why is my on-demand DynamoDB table being throttled?](https://repost.aws/knowledge-center/on-demand-table-throttling-dynamodb)

**Pagination**
+ [How do I implement pagination in DynamoDB](https://repost.aws/knowledge-center/dynamodb-implement-pagination)

**Transactions**
+ [Why is my `TransactWriteItems` API call failing in DynamoDB](https://repost.aws/knowledge-center/dynamodb-transactwriteitems)

**Troubleshooting**

[]()
+ [How do I resolve issues with DynamoDB auto scaling?](https://repost.aws/knowledge-center/dynamodb-auto-scaling)
+ [How do I troubleshoot HTTP 4XX errors in DynamoDB](https://repost.aws/knowledge-center/usererrors-dynamodb-table)

For additional articles and videos for DynamoDB, see the [Knowledge Center articles](https://repost.aws/search/knowledge-center?globalSearch=dynamodb). 

## Blog posts, repositories, and guides
<a name="AdditionalResources.Guides"></a>

In addition to the [DynamoDB Developer Guide](Introduction.md), there are many useful resources for working with DynamoDB. Here are some selected blog posts, repositories, and guides for working with DynamoDB:
+ AWS repository of [DynamoDB code examples](https://github.com/aws-samples/aws-dynamodb-examples) in various AWS SDK languages: [Node.js](https://github.com/aws-samples/aws-dynamodb-examples/tree/master/examples/SDK/node.js), [Java](https://github.com/aws-samples/aws-dynamodb-examples/tree/master/examples/SDK/java), [Python](https://github.com/aws-samples/aws-dynamodb-examples/tree/master/examples/SDK/python), [.Net](https://github.com/aws-samples/aws-dynamodb-examples/tree/master/examples/SDK/dotnet), [Go](https://github.com/aws-samples/aws-dynamodb-examples/tree/master/examples/SDK/golang), and [Rust](https://github.com/aws-samples/aws-dynamodb-examples/tree/master/examples/SDK/rust).
+ [The DynamoDB Book](https://www.dynamodbbook.com/) – A comprehensive guide from [Alex DeBrie](https://twitter.com/alexbdebrie) that teaches a strategy-driven approach to data modeling with DynamoDB.
+ [DynamoDB guide](https://www.dynamodbguide.com/) – An open guide from [Alex DeBrie](https://twitter.com/alexbdebrie) that walks through the basic concepts and advanced features of the DynamoDB NoSQL database. 
+ [How to switch from RDBMS to DynamoDB in 20 easy steps](https://www.jeremydaly.com/how-to-switch-from-rdbms-to-dynamodb-in-20-easy-steps/) – A list of useful steps for learning data modeling from [Jeremy Daly](https://twitter.com/jeremy_daly).
+ [DynamoDB JavaScript DocumentClient cheat sheet](https://github.com/dabit3/dynamodb-documentclient-cheat-sheet) – A cheat sheet to help you get started building applications with DynamoDB in a Node.js or JavaScript environment.
+ [ DynamoDB Core Concept Videos](https://www.youtube.com/playlist?list=PLJo-rJlep0EDNtcDeHDMqsXJcuKMcrC5F) – This playlist covers many of the core concepts of DynamoDB.

## Data modeling and design pattern presentations
<a name="AdditionalResources.DataModeling"></a>

You can use the following resources on data modeling and design patterns to help you get the most out of DynamoDB:
+ [AWS re:Invent 2019: Data modeling with DynamoDB](https://www.youtube.com/watch?v=DIQVJqiSUkE) 
  + A talk by [Alex DeBrie](https://twitter.com/alexbdebrie) that helps you started with the principles of DynamoDB data modeling.
+ [AWS re:Invent 2020: Data modeling with DynamoDB – Part 1](https://www.youtube.com/watch?v=fiP2e-g-r4g)
+ [AWS re:Invent 2020: Data modeling with DynamoDB – Part 2](https://www.youtube.com/watch?v=0uLF1tjI_BI)
+ [AWS re:Invent 2017: Advanced design patterns](https://www.youtube.com/watch?v=jzeKPKpucS0)
+ [AWS re:Invent 2018: Advanced design patterns](https://www.youtube.com/watch?v=HaEPXoXVf2k)
+ [AWS re:Invent 2019: Advanced design patterns](https://www.youtube.com/watch?v=6yqfmXiZTlM)
  + Jeremy Daly shares his [12 key takeaways](https://www.jeremydaly.com/takeaways-from-dynamodb-deep-dive-advanced-design-patterns-dat403/) from this session.
+ [AWS re:Invent 2020: DynamoDB advanced design patterns – Part 1](https://www.youtube.com/watch?v=MF9a1UNOAQo&index=1)
+ [AWS re:Invent 2020: DynamoDB advanced design patterns – Part 2](https://www.youtube.com/watch?v=_KNrRdWD25M&index=2)
+ [DynamoDB Office Hours on Twitch](https://amazondynamodbofficehrs.splashthat.com/)

**Note**  
Each session covers different use cases and examples.

## Training courses
<a name="AdditionalResources.Training"></a>

There are many different training courses and educational options for learning more about DynamoDB. Here are some current examples:
+ [ Developing with Amazon DynamoDB](https://www.aws.training/Details/Curriculum?id=65583) – Designed by AWS to take you from beginner to expert in developing real-world applications with data modeling for Amazon DynamoDB.
+ [DynamoDB deep dive course](https://www.pluralsight.com/courses/aws-dynamodb-deep-dive-2019) – A course from Pluralsight.
+ [Amazon DynamoDB: Building NoSQL database-driven applications](https://www.edx.org/course/amazon-dynamodb-building-nosql-database-driven-app) – A course from the AWS Training and Certification team hosted on edX.