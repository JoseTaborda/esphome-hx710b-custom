#pragma once
#include "esphome/components/sensor/sensor.h"
#include "esphome/core/component.h"
#include "esphome/core/hal.h"

namespace esphome {
namespace hx710b {

class HX710BSensor : public sensor::Sensor, public PollingComponent {
 public:
  void set_dout_pin(InternalGPIOPin *pin) { dout_pin_ = pin; }
  void set_clk_pin(InternalGPIOPin *pin) { clk_pin_ = pin; }
  
  void setup() override;
  void dump_config() override;
  void update() override;

 protected:
  InternalGPIOPin *dout_pin_;
  InternalGPIOPin *clk_pin_;
};

}  // namespace hx710b
}  // namespace esphome