#include "hx710b_sensor.h"

namespace esphome {
namespace hx710b {

void HX710BSensor::setup() {
  this->dout_pin_->setup();
  this->clk_pin_->setup();
  this->clk_pin_->digital_write(false);
}

void HX710BSensor::update() {
  while (this->dout_pin_->digital_read()) {} // Wait for LOW
  
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
  LOG_SENSOR("", "HX710B", this);
}
}
}