# Daily Standup - 2025-10-08

## Team Updates

### What we accomplished yesterday
- Completed initial project setup and repository configuration
- Set up basic IoT sensor communication with ESP32
- Created project documentation structure

### Today's Goals
- Implement temperature sensor data collection
- Set up Telegram bot for notifications
- Complete system architecture diagram

### Blockers/Issues
- Waiting for sensor delivery (ETA: tomorrow)
- Need clarification on API rate limits

## Individual Updates

### Henry Koo (@githubhenrykoo)

#### ✅ Completed Yesterday
- Set up GitHub repository with proper structure
- Created initial README with project documentation
- Configured Git submodules for shared libraries

#### 🔄 Ongoing Work
- Task/Feature: IoT Sensor Integration
  - Progress: 70% complete - Basic sensor reading working
  - Reason for continuation: Need to implement error handling and data validation

#### ➡️ Next Steps
- Complete sensor error handling
- Document API endpoints
- Review pull request #3 from Alessandro

#### ⚠️ Error Log
- Fixed: Sensor readings intermittently failing (resolved by updating firmware)
- Pending: Data transmission drops when Wi-Fi signal is weak

---

### Alessandro Rumampuk (@alessandrorumampuk)

#### ✅ Completed Yesterday
- Researched best practices for ESP32 power management
- Created initial PCB design for sensor module
- Documented hardware requirements

#### 🔄 Ongoing Work
- Task/Feature: Power Optimization
  - Progress: 40% complete - Initial measurements taken
  - Reason for continuation: Need to test different sleep modes

#### ➡️ Next Steps
- Test deep sleep mode implementation
- Document power consumption metrics
- Review PCB design with team

#### ⚠️ Error Log
- Issue: High power consumption in active mode (investigating)
- Note: Need to order additional voltage regulators

---

### Duwi Arsana (@duwiarsana)

#### ✅ Completed Yesterday
- Set up development environment for Telegram bot
- Created bot token and basic command handlers
- Documented bot commands and responses

#### 🔄 Ongoing Work
- Task/Feature: Telegram Notification System
  - Progress: 30% complete - Basic commands working
  - Reason for continuation: Need to implement data visualization

#### ➡️ Next Steps
- Add chart generation for sensor data
- Implement user authentication
- Write unit tests for bot commands

#### ⚠️ Error Log
- Fixed: Bot crashes on invalid commands (added error handling)
- Pending: Timezone handling for notifications

## 🎯 Action Items
- [ ] Review and merge PR #3 - Sensor calibration module (Assigned: Henry)
- [ ] Order additional voltage regulators (Assigned: Alessandro)
- [ ] Set up CI/CD pipeline (Assigned: Duwi)
- [ ] Create project presentation outline (Assigned: All)
- [ ] Update project timeline in README (Assigned: Henry)
