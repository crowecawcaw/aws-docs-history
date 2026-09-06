

# What Is Authentication?
<a name="WhatIsAuthentication"></a>

Authentication is a process for identifying and verifying who is sending a request. The following diagram shows a simplified version of an authentication process.

![General Process of Authentication](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/images/GenericAuthProcess.png)



**General Process of Authentication**  

|  |  | 
| --- |--- |
|  ![Red circle with number 1 inside, indicating a numerical step or priority.](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/images/callouts/1.png)  | The sender obtains the necessary credential. | 
|  ![Red circle with number 2 inside, likely representing a step or item in a sequence.](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/images/callouts/2.png)  | The sender sends a request with the credential to the recipient. | 
|  ![Red circle with number 3 inside, indicating a step or sequence number.](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/images/callouts/3.png)  | The recipient uses the credential to verify the sender truly sent the request. | 
|  ![Red circle with number 4 inside, likely representing a notification or count indicator.](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/images/callouts/4.png)  | If yes, the recipient processes the request. If no, the recipient rejects the request and responds accordingly. | 

 During authentication, AWS verifies both the identity of the sender and whether the sender is registered to use services offered by AWS. If either test fails, the request is not processed further.

The subsequent sections describe how Amazon SimpleDB implements authentication to protect you and your customers' data.