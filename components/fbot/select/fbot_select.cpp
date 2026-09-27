#include "fbot_select.h"
#include "esphome/core/log.h"
#ifdef USE_ESP32
namespace esphome { namespace fbot {
static const char *const TAG = "fbot.select";
void FbotSelect::setup() {}
void FbotSelect::dump_config() { LOG_SELECT("", "Fbot Select", this); ESP_LOGCONFIG(TAG, "  Type: %s", this->select_type_.c_str()); }
void FbotSelect::control(const std::string &value) {
  if (parent_ == nullptr) { ESP_LOGW(TAG,"No parent set for select"); return; }
  if (!parent_->is_connected()) { ESP_LOGW(TAG,"Cannot change select '%s': device is disconnected",select_type_.c_str()); return; }
  if (select_type_ == "light_mode") parent_->control_light_mode(value);
  else if (select_type_ == "ac_charge_limit") parent_->control_ac_charge_limit(value);
  else if (select_type_ == "dc_input_mode") parent_->control_dc_input_mode(value);
  else { ESP_LOGW(TAG,"Unknown select type: %s",select_type_.c_str()); return; }
  publish_state(value);
}
} }
#endif
