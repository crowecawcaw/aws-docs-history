# AWS RTB Fabric Glossary

## Application

A customer-built software system that connects to RTB Fabric [gateways](#gateway-definition "#gateway-definition") to send or receive real-time bidding requests. Applications are external to RTB Fabric and can be [requester applications](#requester-definition "#requester-definition") that send bid requests or [responder applications](#responder-definition "#responder-definition") that receive and process bid requests. Applications connect to RTB Fabric through gateways, which handle the routing and processing of requests between applications.

## Availability Zone (AZ)

Distinct locations within an AWS Region that are engineered to be isolated from failures
in other AZs.

## Customer

User of the service. Includes [Demand-Side Platforms (DSPs)](#dsp-definition "#dsp-definition") and [Supply-Side Platforms (SSPs)](#ssp-definition "#ssp-definition").

## Demand-Side Platform (DSP)

An adtech system that allows advertisers to buy ad inventory from multiple ad exchanges through one interface. Also known as a buyer. The service helps DSPs to participate effectively in real-time bidding auctions with a high-performance, low-latency infrastructure.

## Flow

Part of a [link](#link-definition "#link-definition") configuration that defines how RTB requests are processed. Created with the `UpdateLinkModuleFlow`. Flows can include [RTB modules](#module-definition "#module-definition") configured for specific behaviors such as additional filtering and enrichment actions. Default flows are created with links, but you can update a flow with additional modules.

## Gateway

RTB Fabric infrastructure components that serve as connection points for customer [applications](#application-definition "#application-definition"). _Requester gateways_ receive requests from requester applications and forward them through [links](#link-definition "#link-definition") to responder gateways. _Responder gateways_ receive requests from requester gateways and forward them to responder applications, then return responses through the same pathway.

## Link

The core component of RTB Fabric that establishes secure, bidirectional communication channels between [gateways](#gateway-definition "#gateway-definition"). Links provide authenticated communication, traffic routing and load balancing, performance monitoring, and security controls. Links can include processing logic through [modules](#module-definition "#module-definition").

## Requester

A customer [application](#application-definition "#application-definition") that sends bid requests to RTB Fabric through a requester [gateway](#gateway-definition "#gateway-definition").

## Resources

[Gateways](#gateway-definition "#gateway-definition"), [links](#link-definition "#link-definition"), [flows](#flow-definition "#flow-definition"), and [RTB modules](#module-definition "#module-definition") that comprise the RTB Fabric infrastructure. Customer [applications](#application-definition "#application-definition") are external to RTB Fabric and connect to these infrastructure resources.

## Responder

A customer [application](#application-definition "#application-definition") that receives bid requests from RTB Fabric through a responder [gateway](#gateway-definition "#gateway-definition") and returns bid responses.

## RTB module

A component that performs specific operations on RTB requests, such as filtering or enrichment. RTB modules can be configured by [Supply-Side Platforms (SSPs)](#ssp-definition "#ssp-definition") or [Demand-Side Platforms (DSPs)](#dsp-definition "#dsp-definition") in their [flows](#flow-definition "#flow-definition"), although they are not required to configure a flow. RTB Fabric provides built-in modules (QPS rate limiter, OpenRTB filter, error masker) available at no additional charge. Modules are configured using the `UpdateLinkModuleFlow` API operation.

## Supply-Side Platform (SSP)

An adtech system that helps publishers manage and sell their ad inventory through programmatic auctions to [Demand-Side Platforms (DSPs)](#dsp-definition "#dsp-definition") and advertising agencies. Also known as a seller. The service helps SSPs with very low latency requirements process high volumes of real-time bid requests and responses.

## Virtual private cloud (VPC)

A logically isolated network in the AWS Cloud. This virtual network resembles a
traditional network that you'd operate in your own data center, with the benefits of using the
scalable infrastructure of AWS. For more information, see [Amazon Virtual Private Cloud (Amazon VPC).](http://aws.amazon.com/vpc/ "http://aws.amazon.com/vpc/")
