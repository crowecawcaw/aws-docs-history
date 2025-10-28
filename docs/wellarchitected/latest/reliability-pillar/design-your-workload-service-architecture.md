# Design your workload service architecture

Build highly scalable and reliable workloads using a
service-oriented architecture (SOA) or a microservices
architecture. Service-oriented architecture (SOA) is the practice
of making software components reusable via service interfaces.
Microservices architecture goes further to make components smaller
and simpler.

Service-oriented architecture (SOA) interfaces use common communication standards so that
they can be rapidly incorporated into new workloads. SOA replaced the practice of building
monolith architectures, which consisted of interdependent, indivisible units.

At AWS, we have always used SOA, but have now embraced building
our systems using microservices. While microservices have several
attractive qualities, the most important benefit for availability
is that microservices are smaller and simpler. They allow you to
differentiate the availability required of different services, and
thereby focus investments more specifically to the microservices
that have the greatest availability needs. For example, to deliver
product information pages on Amazon.com (“detail pages”), hundreds
of microservices are invoked to build discrete portions of the
page. While there are a few services that must be available to
provide the price and the product details, the vast majority of
content on the page can simply be excluded if the service isn’t
available. Even such things as photos and reviews are not required
to provide an experience where a customer can buy a product.

###### Best practices

- [REL03-BP01 Choose how to segment your workload](rel_service_architecture_monolith_soa_microservice.md "rel_service_architecture_monolith_soa_microservice.md")
- [REL03-BP02 Build services focused on specific business domains
  and functionality](rel_service_architecture_business_domains.md "rel_service_architecture_business_domains.md")
- [REL03-BP03 Provide service contracts per API](rel_service_architecture_api_contracts.md "rel_service_architecture_api_contracts.md")
