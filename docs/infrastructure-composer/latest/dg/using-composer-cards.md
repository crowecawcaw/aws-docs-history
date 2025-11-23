# Configure and modify cards in Infrastructure Composer

In Infrastructure Composer, cards represent resources that you use to design your application architecture. When you configure a card in Infrastructure Composer, you define the details of the resources in your application.
This includes details like a card's **Logical ID** and **Partition key**. The way this information is defined varies between **Enhanced component cards**
and **Standard cards**.

An **Enhanced component card** is A collection of CloudFormation resources that have been combined into a single curated card that enhances ease of use, functionality,
and are designed for a wide variety of use cases. A **Standard IaC resource card** represents a single AWS CloudFormation resource. Each standard IaC resource card,
once dragged onto the canvas, is labeled **Standard component**.

This topic provides details on configuring **Enhanced component cards** and **Standard component cards**.

###### Note

This topic applies to using cards from the Infrastructure Composer Console, the AWS Toolkit for Visual Studio Code extension, and while in Infrastructure Composer in CloudFormation console mode. Lambda-related cards (**Lambda Function** and
**Lambda Layer**) require code builds and packaging solutions that are not available in Infrastructure Composer in CloudFormation console mode. For more information, see
[Using Infrastructure Composer in CloudFormation console mode](using-composer-console-cfn-mode.md "using-composer-console-cfn-mode.md").

###### Topics

- [Enhanced component cards in Infrastructure Composer](using-composer-cards-use-enhanced-component.md "using-composer-cards-use-enhanced-component.md")
- [Standard cards in Infrastructure Composer](using-composer-standard-cards.md "using-composer-standard-cards.md")
