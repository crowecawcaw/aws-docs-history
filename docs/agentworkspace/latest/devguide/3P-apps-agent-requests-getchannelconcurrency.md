

# Get the limit of contacts for the agent in Connect Customer agent workspace

Returns a map of `ChannelType`-to-number indicating how many concurrent contacts can an Connect Customer agent workspace agent have on a given channel. 0 represents a disabled channel.

```typescript
async getChannelConcurrency(): Promise<AgentChannelConcurrency>         
```

 **Permissions required:** 

```typescript
User.Configuration.View              
```