We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Formulating the Problem

The first step in machine learning is to decide what you want to predict, which is known as the label or
target answer. Imagine a scenario in which you want to manufacture products, but your decision to
manufacture each product depends on its number of potential sales. In this scenario, you want to predict
how many times each product will be purchased (predict number of sales). There are multiple ways to
define this problem by using machine learning. Choosing how to define the problem depends on your use
case or business need.

Do you want to predict the number of purchases your customers will make for each product (in which case
the target is numeric and you’re solving a regression problem)? Or do you want to predict which products
will get more than 10 purchases (in which case the target is binary and you’re solving a binary
classification problem)?

It is important to avoid over-complicating the problem and to frame the simplest solution that meets your
needs. However, it is also important to avoid losing information, especially information in the historical
answers. Here, converting an actual past sales number into a binary variable “over 10” versus “fewer”
would lose valuable information. Investing time in deciding which target makes most sense for you to
predict will save you from building models that don’t answer your question.
