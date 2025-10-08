# Unified Project Structure

## Root Directory Structure
```
hackathon-2025-example/
├── README.md
├── package.json
├── .gitignore
├── docs/                    # Documentation
│   ├── prd/                # Product requirements
│   ├── architecture/       # Technical architecture
│   └── stories/            # User stories
├── src/                    # Source code
│   ├── iot/               # IoT/ESP32 code
│   ├── backend/           # Backend services
│   ├── telegram/          # Telegram bot
│   └── pkc/               # PKC integration
├── config/                # Configuration files
├── tests/                 # Test files
└── .bmad-core/           # BMAD framework files
```

## Source Code Organization

### IoT Directory (`src/iot/`)
```
src/iot/
├── esp32-sensors/         # ESP32 sensor code
│   ├── main.cpp          # Main ESP32 application
│   ├── sensors.h         # Sensor interface definitions
│   ├── wifi-config.h     # WiFi configuration
│   └── mqtt-client.h     # MQTT client implementation
└── libraries/            # Custom libraries
```

### Backend Directory (`src/backend/`)
```
src/backend/
├── server.js             # Main server entry point
├── routes/               # API route handlers
│   ├── sensors.js        # Sensor data endpoints
│   └── health.js         # Health check endpoints
├── services/             # Business logic services
│   ├── mqtt-service.js   # MQTT message handling
│   └── data-service.js   # Data processing service
├── models/               # Data models
│   └── sensor-data.js    # Sensor data model
└── middleware/           # Express middleware
    └── auth.js           # Authentication middleware
```

### Telegram Directory (`src/telegram/`)
```
src/telegram/
├── bot.js                # Main bot application
├── commands/             # Bot command handlers
│   ├── start.js          # Start command
│   └── sensors.js        # Sensor data commands
└── utils/                # Utility functions
    └── formatter.js      # Message formatting
```

### PKC Directory (`src/pkc/`)
```
src/pkc/
├── knowledge-container.js # Main PKC implementation
├── processors/           # Data processors
│   └── sensor-processor.js # Sensor data processing
└── storage/              # Storage implementations
    └── file-storage.js   # File-based storage
```

## Configuration Structure (`config/`)
```
config/
├── mqtt.json             # MQTT broker configuration
├── database.json         # Database connection settings
├── telegram.json         # Telegram bot configuration
└── sensors.json          # Sensor configuration
```

## Testing Structure (`tests/`)
```
tests/
├── unit/                 # Unit tests
│   ├── services/         # Service tests
│   └── models/           # Model tests
├── integration/          # Integration tests
└── fixtures/             # Test data fixtures
```

## File Naming Conventions
- **JavaScript files**: kebab-case (e.g., `mqtt-service.js`)
- **Configuration files**: kebab-case with extension (e.g., `mqtt.json`)
- **Test files**: `*.test.js` or `*.spec.js`
- **Documentation**: kebab-case (e.g., `tech-stack.md`)

## Import/Export Patterns
- Use ES6 modules (`import`/`export`) for frontend code
- Use CommonJS (`require`/`module.exports`) for Node.js backend
- Absolute imports from project root using path mapping
