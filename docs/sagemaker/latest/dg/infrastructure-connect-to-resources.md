# Connect to Amazon SageMaker AI resources from

within a VPC

###### Important

The following information applies to both Amazon SageMaker Studio and Amazon SageMaker Studio Classic. The same concepts of connecting to resources within a VPC apply to both Studio and Studio Classic.

Amazon SageMaker Studio and SageMaker AI notebook instances allow direct internet access by default. SageMaker AI
allows you to download popular packages and notebooks, customize your development
environment, and work efficiently. However, this could provide an opening for unauthorized
access to your data. For example, if you install malicious code on your computer as a
publicly available notebook or source code library, it could access your data. You can
restrict which traffic can access the internet by launching your Studio and SageMaker AI
notebook instances in a [Amazon Virtual Private Cloud (Amazon VPC)](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

An Amazon Virtual Private Cloud is a virtual network dedicated to your AWS account. With an Amazon VPC, you can
control the network access and internet connectivity of your Studio and notebook
instances. You can remove direct internet access to add another layer of security.

The following topics describe how to connect your Studio instances and notebook
instances to resources in a VPC.

###### Topics

- [Connect Amazon SageMaker Studio
  in a VPC to External Resources](studio-updated-and-internet-access.md "studio-updated-and-internet-access.md")
- [Connect Studio notebooks in
  a VPC to external resources](studio-notebooks-and-internet-access.md "studio-notebooks-and-internet-access.md")
- [Connect a Notebook Instance in a
  VPC to External Resources](appendix-notebook-and-internet-access.md "appendix-notebook-and-internet-access.md")
