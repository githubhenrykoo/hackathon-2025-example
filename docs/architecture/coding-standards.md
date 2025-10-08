# Coding Standards

## General Principles
- Write clean, readable, and maintainable code
- Follow consistent naming conventions
- Include meaningful comments for complex logic
- Keep functions small and focused on single responsibility

## JavaScript/Node.js Standards

### Naming Conventions
- **Variables and Functions**: camelCase (`sensorData`, `processMessage`)
- **Constants**: UPPER_SNAKE_CASE (`MQTT_BROKER_URL`, `MAX_RETRY_ATTEMPTS`)
- **Classes**: PascalCase (`SensorDataProcessor`, `MqttClient`)
- **Files**: kebab-case (`sensor-service.js`, `mqtt-client.js`)

### Code Formatting
- Use 2 spaces for indentation
- Maximum line length: 100 characters
- Use semicolons at end of statements
- Use single quotes for strings
- Trailing commas in objects and arrays

### Error Handling
- Always handle errors explicitly
- Use try-catch blocks for async operations
- Log errors with appropriate context
- Return meaningful error messages

```javascript
try {
  const result = await sensorService.getData();
  return result;
} catch (error) {
  logger.error('Failed to get sensor data:', error.message);
  throw new Error('Sensor data unavailable');
}
```

## C++ (ESP32) Standards

### Naming Conventions
- **Variables**: camelCase (`sensorValue`, `wifiConnected`)
- **Functions**: camelCase (`readSensor`, `connectWiFi`)
- **Constants**: UPPER_SNAKE_CASE (`SENSOR_PIN`, `MQTT_PORT`)
- **Classes**: PascalCase (`SensorReader`, `MqttPublisher`)

### Code Organization
- Include guards for header files
- Separate interface (.h) from implementation (.cpp)
- Group related functionality in classes
- Use meaningful variable names

```cpp
#ifndef SENSOR_READER_H
#define SENSOR_READER_H

class SensorReader {
private:
  int sensorPin;
  float lastReading;
  
public:
  SensorReader(int pin);
  float readTemperature();
  bool isDataValid();
};

#endif
```

## Documentation Standards

### Code Comments
- Use JSDoc for JavaScript functions
- Document complex algorithms and business logic
- Explain "why" not just "what"
- Keep comments up-to-date with code changes

```javascript
/**
 * Processes raw sensor data and applies calibration
 * @param {Object} rawData - Raw sensor readings
 * @param {Object} calibration - Calibration parameters
 * @returns {Object} Processed sensor data
 */
function processSensorData(rawData, calibration) {
  // Implementation
}
```

### README Files
- Include setup instructions
- Document API endpoints
- Provide usage examples
- List dependencies and requirements

## Testing Standards
- Write unit tests for all business logic
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)
- Maintain test coverage above 80%

```javascript
describe('SensorService', () => {
  it('should return valid sensor data when sensor is connected', async () => {
    // Arrange
    const mockSensor = { connected: true, value: 25.5 };
    
    // Act
    const result = await sensorService.getData(mockSensor);
    
    // Assert
    expect(result.temperature).toBe(25.5);
    expect(result.isValid).toBe(true);
  });
});
```

## Git Commit Standards
- Use conventional commit format
- Keep commits small and focused
- Write clear commit messages

```
feat: add MQTT client for sensor data transmission
fix: resolve WiFi connection timeout issue
docs: update API documentation for sensor endpoints
```
