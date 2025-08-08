#pragma once
#include "esphome/components/sensor/sensor.h"
#include "esphome/core/component.h"
#include "esphome/core/hal.h"

namespace esphome {
namespace hx710b {

class HX710BSensor : public sensor::Sensor, public PollingComponent {
 public:
  void setup() override;
  void dump_config() override;
  void update() override;
  
  void set_dout_pin(GPIOPin *pin) { dout_pin_ = pin; }
  void set_clk_pin(GPIOPin *pin) { clk_pin_ = pin; }

 protected:
  GPIOPin *dout_pin_;
  GPIOPin *clk_pin_;
};

}  // namespace hx710b
}  // namespace esphome