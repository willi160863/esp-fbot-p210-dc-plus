#pragma once

#include "esphome/core/component.h"
#include "esphome/components/ble_client/ble_client.h"
#include "esphome/components/esp32_ble_tracker/esp32_ble_tracker.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/switch/switch.h"

#ifdef USE_NUMBER
#include "esphome/components/number/number.h"
#endif
#ifdef USE_SELECT
#include "esphome/components/select/select.h"
#endif
#ifdef USE_ESP32
#include <esp_gattc_api.h>
namespace esphome { namespace fbot {

static const char *const SERVICE_UUID = "0000a002-0000-1000-8000-00805f9b34fb";
static const char *const WRITE_CHAR_UUID = "0000c304-0000-1000-8000-00805f9b34fb";
static const char *const NOTIFY_CHAR_UUID = "0000c305-0000-1000-8000-00805f9b34fb";

static const uint8_t REG_AC_CHARGE_LIMIT = 13;
static const uint8_t REG_DC_INPUT_MODE = 15;
static const uint8_t REG_DC_CHARGE_CURRENT = 20;
static const uint8_t REG_USB_CONTROL = 24;
static const uint8_t REG_DC_CONTROL = 25;
static const uint8_t REG_AC_CONTROL = 26;
static const uint8_t REG_LIGHT_CONTROL = 27;
static const uint8_t REG_USB_A1_OUT = 30;
static const uint8_t REG_USB_A2_OUT = 31;
static const uint8_t REG_USB_C1_OUT = 34;
static const uint8_t REG_USB_C2_OUT = 35;
static const uint8_t REG_USB_C3_OUT = 36;
static const uint8_t REG_USB_C4_OUT = 37;
static const uint8_t REG_KEY_SOUND = 56;
static const uint8_t REG_AC_SILENT_CONTROL = 57;
static const uint8_t REG_THRESHOLD_DISCHARGE = 66;
static const uint8_t REG_THRESHOLD_CHARGE = 67;

static const uint16_t STATE_USB_BIT = 512;
static const uint16_t STATE_DC_BIT = 1024;
static const uint16_t STATE_AC_BIT = 2048;
static const uint16_t STATE_LIGHT_BIT = 4096;

class Fbot : public esphome::ble_client::BLEClientNode, public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::DATA; }
  void gattc_event_handler(esp_gattc_cb_event_t event, esp_gatt_if_t gattc_if, esp_ble_gattc_cb_param_t *param) override;
  void set_polling_interval(uint32_t interval) { polling_interval_ = interval; }
  void set_settings_polling_interval(uint32_t interval) { settings_polling_interval_ = interval; }
  void set_poll_timeout(uint32_t timeout) { poll_timeout_ms_ = timeout; }
  void set_max_poll_failures(uint8_t max_failures) { max_poll_failures_ = max_failures; }

  void set_battery_percent_sensor(sensor::Sensor *s) { battery_percent_sensor_=s; }
  void set_battery_percent_s1_sensor(sensor::Sensor *s) { battery_percent_s1_sensor_=s; }
  void set_battery_percent_s2_sensor(sensor::Sensor *s) { battery_percent_s2_sensor_=s; }
  void set_input_power_sensor(sensor::Sensor *s) { input_power_sensor_=s; }
  void set_ac_input_power_sensor(sensor::Sensor *s) { ac_input_power_sensor_=s; }
  void set_dc_input_power_sensor(sensor::Sensor *s) { dc_input_power_sensor_=s; }
  void set_output_power_sensor(sensor::Sensor *s) { output_power_sensor_=s; }
  void set_system_power_sensor(sensor::Sensor *s) { system_power_sensor_=s; }
  void set_total_power_sensor(sensor::Sensor *s) { total_power_sensor_=s; }
  void set_remaining_time_sensor(sensor::Sensor *s) { remaining_time_sensor_=s; }
  void set_threshold_charge_sensor(sensor::Sensor *s) { threshold_charge_sensor_=s; }
  void set_threshold_discharge_sensor(sensor::Sensor *s) { threshold_discharge_sensor_=s; }
  void set_charge_level_sensor(sensor::Sensor *s) { charge_level_sensor_=s; }
  void set_ac_out_voltage_sensor(sensor::Sensor *s) { ac_out_voltage_sensor_=s; }
  void set_ac_out_frequency_sensor(sensor::Sensor *s) { ac_out_frequency_sensor_=s; }
  void set_ac_in_frequency_sensor(sensor::Sensor *s) { ac_in_frequency_sensor_=s; }
  void set_time_to_full_sensor(sensor::Sensor *s) { time_to_full_sensor_=s; }
  void set_usb_a1_power_sensor(sensor::Sensor *s) { usb_a1_power_sensor_=s; }
  void set_usb_a2_power_sensor(sensor::Sensor *s) { usb_a2_power_sensor_=s; }
  void set_usb_c1_power_sensor(sensor::Sensor *s) { usb_c1_power_sensor_=s; }
  void set_usb_c2_power_sensor(sensor::Sensor *s) { usb_c2_power_sensor_=s; }
  void set_usb_c3_power_sensor(sensor::Sensor *s) { usb_c3_power_sensor_=s; }
  void set_usb_c4_power_sensor(sensor::Sensor *s) { usb_c4_power_sensor_=s; }
  void set_dc_input_mode_raw_sensor(sensor::Sensor *s) { dc_input_mode_raw_sensor_=s; }
  void set_dc_charge_current_raw_sensor(sensor::Sensor *s) { dc_charge_current_raw_sensor_=s; }
  void set_ac_charge_appointment_raw_sensor(sensor::Sensor *s) { ac_charge_appointment_raw_sensor_=s; }

  void set_connected_binary_sensor(binary_sensor::BinarySensor *s){connected_binary_sensor_=s;}
  void set_battery_connected_s1_binary_sensor(binary_sensor::BinarySensor *s){battery_connected_s1_binary_sensor_=s;}
  void set_battery_connected_s2_binary_sensor(binary_sensor::BinarySensor *s){battery_connected_s2_binary_sensor_=s;}
  void set_usb_active_binary_sensor(binary_sensor::BinarySensor *s){usb_active_binary_sensor_=s;}
  void set_dc_active_binary_sensor(binary_sensor::BinarySensor *s){dc_active_binary_sensor_=s;}
  void set_ac_active_binary_sensor(binary_sensor::BinarySensor *s){ac_active_binary_sensor_=s;}
  void set_light_active_binary_sensor(binary_sensor::BinarySensor *s){light_active_binary_sensor_=s;}

  void set_usb_switch(switch_::Switch *s){usb_switch_=s;} void set_dc_switch(switch_::Switch *s){dc_switch_=s;}
  void set_ac_switch(switch_::Switch *s){ac_switch_=s;} void set_light_switch(switch_::Switch *s){light_switch_=s;}
  void set_ac_silent_switch(switch_::Switch *s){ac_silent_switch_=s;} void set_key_sound_switch(switch_::Switch *s){key_sound_switch_=s;}
#ifdef USE_SELECT
  void set_light_mode_select(select::Select *s){light_mode_select_=s;}
  void set_ac_charge_limit_select(select::Select *s){ac_charge_limit_select_=s;}
  void set_dc_input_mode_select(select::Select *s){dc_input_mode_select_=s;}
#endif
#ifdef USE_NUMBER
  void set_threshold_charge_number(number::Number *n){threshold_charge_number_=n;}
  void set_threshold_discharge_number(number::Number *n){threshold_discharge_number_=n;}
  void set_dc_charge_current_number(number::Number *n){dc_charge_current_number_=n;}
#endif
  void control_usb(bool); void control_dc(bool); void control_ac(bool); void control_light(bool); void control_ac_silent(bool); void control_key_sound(bool);
  void control_light_mode(const std::string&); void control_ac_charge_limit(const std::string&); void control_dc_input_mode(const std::string&);
  void set_threshold_charge(float); void set_threshold_discharge(float); void set_dc_charge_current(float);
  void set_wifi_credentials(const std::string&, const std::string&);
  bool is_connected() const { return connected_; }
 protected:
  uint16_t write_handle_{0}, notify_handle_{0};
  uint32_t polling_interval_{2000}, settings_polling_interval_{60000}, last_poll_time_{0}, last_successful_poll_{0}, last_settings_request_time_{0};
  bool connected_{false}, characteristics_discovered_{false}, settings_received_{false};
  uint8_t consecutive_poll_failures_{0}, max_poll_failures_{3}; uint32_t poll_timeout_ms_{15000};
  sensor::Sensor *battery_percent_sensor_{nullptr};
  sensor::Sensor *battery_percent_s1_sensor_{nullptr};
  sensor::Sensor *battery_percent_s2_sensor_{nullptr};
  sensor::Sensor *input_power_sensor_{nullptr};
  sensor::Sensor *ac_input_power_sensor_{nullptr};
  sensor::Sensor *dc_input_power_sensor_{nullptr};
  sensor::Sensor *output_power_sensor_{nullptr};
  sensor::Sensor *system_power_sensor_{nullptr};
  sensor::Sensor *total_power_sensor_{nullptr};
  sensor::Sensor *remaining_time_sensor_{nullptr};
  sensor::Sensor *threshold_charge_sensor_{nullptr};
  sensor::Sensor *threshold_discharge_sensor_{nullptr};
  sensor::Sensor *charge_level_sensor_{nullptr};
  sensor::Sensor *ac_out_voltage_sensor_{nullptr};
  sensor::Sensor *ac_out_frequency_sensor_{nullptr};
  sensor::Sensor *ac_in_frequency_sensor_{nullptr};
  sensor::Sensor *time_to_full_sensor_{nullptr};
  sensor::Sensor *usb_a1_power_sensor_{nullptr};
  sensor::Sensor *usb_a2_power_sensor_{nullptr};
  sensor::Sensor *usb_c1_power_sensor_{nullptr};
  sensor::Sensor *usb_c2_power_sensor_{nullptr};
  sensor::Sensor *usb_c3_power_sensor_{nullptr};
  sensor::Sensor *usb_c4_power_sensor_{nullptr};
  sensor::Sensor *dc_input_mode_raw_sensor_{nullptr};
  sensor::Sensor *dc_charge_current_raw_sensor_{nullptr};
  sensor::Sensor *ac_charge_appointment_raw_sensor_{nullptr};
  binary_sensor::BinarySensor *connected_binary_sensor_{nullptr},*battery_connected_s1_binary_sensor_{nullptr},*battery_connected_s2_binary_sensor_{nullptr},*usb_active_binary_sensor_{nullptr},*dc_active_binary_sensor_{nullptr},*ac_active_binary_sensor_{nullptr},*light_active_binary_sensor_{nullptr};
  switch_::Switch *usb_switch_{nullptr},*dc_switch_{nullptr},*ac_switch_{nullptr},*light_switch_{nullptr},*ac_silent_switch_{nullptr},*key_sound_switch_{nullptr};
#ifdef USE_NUMBER
  number::Number *threshold_charge_number_{nullptr},*threshold_discharge_number_{nullptr},*dc_charge_current_number_{nullptr};
#endif
#ifdef USE_SELECT
  select::Select *light_mode_select_{nullptr},*ac_charge_limit_select_{nullptr},*dc_input_mode_select_{nullptr};
#endif
  uint16_t calculate_checksum(const uint8_t*,size_t); void generate_command_bytes(uint8_t,uint16_t,uint16_t,uint8_t*);
  void send_read_request(); void send_settings_request(); void send_control_command(uint16_t,uint16_t);
  void parse_notification(const uint8_t*,uint16_t); void parse_settings_notification(const uint8_t*,uint16_t); uint16_t get_register(const uint8_t*,uint16_t,uint16_t);
  void update_connected_state(bool); void reset_sensors_to_unknown(); void check_poll_timeout();
};
} }
#endif
