#include "fbot.h"
#include "esphome/core/log.h"
#ifdef USE_ESP32
namespace esphome { namespace fbot {
static const char *const TAG_P210_DC = "fbot.p210_dc";

void Fbot::control_dc_input_mode(const std::string &value) {
  uint16_t reg_value;
  if (value == "PV/MPPT") reg_value = 0;
  else if (value == "DC Source") reg_value = 1;
  else { ESP_LOGW(TAG_P210_DC, "Unknown DC input mode: %s", value.c_str()); return; }
  ESP_LOGI(TAG_P210_DC, "Setting DC input mode to %s (register 15 = %u)", value.c_str(), reg_value);
  send_control_command(REG_DC_INPUT_MODE, reg_value);
  set_timeout(500, [this]() { send_settings_request(); });
}

void Fbot::set_dc_charge_current(float amps) {
  uint16_t value = static_cast<uint16_t>(amps);
  if (value < 1) value = 1;
  if (value > 20) value = 20;
  ESP_LOGI(TAG_P210_DC, "Setting DC charge current (register 20) to %u A", value);
  send_control_command(REG_DC_CHARGE_CURRENT, value);
  set_timeout(500, [this]() { send_settings_request(); });
}
} }
#endif
