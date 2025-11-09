# Developer guide

## Customizing the guidance

### Adding New Vehicle Types

- Extend vehicle registration schemas in `modules/cms_ui/source/handlers/`
- Update telemetry processing logic in `modules/flink/`
- Modify UI components in `modules/cms_ui/source/frontend/src/components/`

### Custom Analytics

- Create new Flink processors for custom data analysis
- Add DynamoDB tables for new data types
- Implement API endpoints for data access

## API Reference

The guidance provides REST APIs for:

- Vehicle management and registration
- Fleet operations and monitoring
- Telemetry data access and querying
- User management and authentication
