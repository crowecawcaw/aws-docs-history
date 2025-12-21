# Building agentic flows

###### Note

This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Sonic guide, visit [Tool configuration](../nova2-userguide/sonic-tool-configuration.md "../nova2-userguide/sonic-tool-configuration.md").

For more complex use cases, you can implement agentic flows by configuring multiple tools that work together to accomplish tasks. Amazon Nova Sonic can orchestrate these tools based on user requests.

## Knowledge base implementation outline

###### Hotel Reservation Cancellation Agent Example

Here is an example configuration of a hotel reservation cancellation system:

```
toolConfiguration: {
    tools: [
      {
        toolSpec: {
          name: "getReservation",
          description: "Retrieves hotel reservation information based on the guest's name and check-in date",
          inputSchema: {
            json: JSON.stringify({
              type: "object",
              properties: {
                name: {
                  type: "string",
                  description: "Full name of the guest who made the reservation"
                },
                checkInDate: {
                  type: "string",
                  description: "The check-in date for the reservation in YYYY-MM-DD format"
                }
              },
              required: ["name", "checkInDate"]
            })
          }
        }
      },
      {
        toolSpec: {
          name: "cancelReservation",
          description: "Cancels a hotel reservation after confirming the cancellation policy with the guest",
          inputSchema: {
            json: JSON.stringify({
              type: "object",
              properties: {
                reservationId: {
                  type: "string",
                  description: "The unique identifier for the reservation to be cancelled"
                },
                confirmCancellation: {
                  type: "boolean",
                  description: "Confirmation from the guest that they understand the cancellation policy and want to proceed",
                  default: false
                }
              },
              required: ["reservationId", "confirmCancellation"]
            })
          }
        }
      }
    ]
  }
```

###### Hotel Search Agent Example

And here is an example configuration of a hotel search agent:

```
toolSpec: {
    name: "searchHotels",
    description: "Search for hotels by location, star rating, amenities and price range.",
    inputSchema: {
        json: JSON.stringify({
            type: "object",
            properties: {
                location: {
                    type: "string",
                    description: "City or area to search for hotels"
                },
                rating: {
                    type: "number",
                    minimum: 1,
                    maximum: 5,
                    description: "Minimum star rating (1-5)"
                },
                amenities: {
                    type: "array",
                    items: {
                        type: "string"
                    },
                    description: "List of desired amenities"
                },
                price_range: {
                    type: "object",
                    properties: {
                        min: {
                            type: "number",
                            minimum: 0
                        },
                        max: {
                            type: "number",
                            minimum: 0
                        }
                    },
                    description: "Price range per night"
                }
            },
            required: []
        })
    }
}
```
