# Manage demand and supply resources

| EUCCOST06: How do you optimize cost using existing licenses when appropriate?
|
| --- |
| | You may already have existing license agreements with Microsoft in place. You can use these licenses with AWS EUC services to reduce your cost.
| EUCCOST07: How do you track and identify idle resources to avoid unnecessary charges? |
| --- |
| | Amazon WorkSpaces can be used in AlwaysOn and AutoStop running mode, which correspond to monthly and hourly billing respectively. If deployed your WorkSpaces with monthly billing but are using them less than expected, switching the billing mode can reduce your cost. With Amazon AppStream 2.0, you will likely use app block builders or image builders to generate app blocks and images. These resources are charged hourly or in one second increments with a 15-minute minimum if you keep them running. ###### Best practices <br>• [EUCCOST06-BP01 Explore a bring your own license (BYOL) approach](euccost06-bp01.md "euccost06-bp01.md") <br>• [EUCCOST07-BP01 Use the available cost optimizers for Amazon WorkSpaces and Amazon AppStream 2.0](euccost07-bp01.md "euccost07-bp01.md")
