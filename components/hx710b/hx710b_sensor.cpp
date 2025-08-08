#include "hx710b_sensor.h"

namespace esphome {
namespace hx710b {

void HX710BSensor::setup() {
  this->dout_pin_->setup();
  this->clk_pin_->setup();
  this->clk_pin_->digital_write(false);
  
}

void HX710BSensor::update() {
  while (this->dout_pin_->digital_read()) {}
  
  long data = 0;
  for (int i = 0; i < 24; i++) {
    this->clk_pin_->digital_write(true);
    delayMicroseconds(1);
    data = (data << 1) | this->dout_pin_->digital_read();
    this->clk_pin_->digital_write(false);
    delayMicroseconds(1);
  }
  
  data = data ^ 0x800000;
  this->publish_state(data / 1000.0f);
}

void HX710BSensor::dump_config() {
  ESP_LOGCONFIG(TAG, "HX710B Sensor:");
  LOG_PIN("  DOUT Pin: ", this->dout_pin_);
  LOG_PIN("  CLK Pin: ", this->clk_pin_);
}

void HX710BSensor::set_dout_pin(InternalGPIOPin *pin) { dout_pin_ = pin; }
void HX710BSensor::set_clk_pin(InternalGPIOPin *pin) { clk_pin_ = pin; }

}  // namespace hx710b
}  // namespace esphome