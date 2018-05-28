#ifndef RADIO_COUNT_TO_LEDS_H
#define RADIO_COUNT_TO_LEDS_H

typedef nx_struct radio_count_msg {
  nx_uint8_t OrgNodeId;
  nx_uint16_t node_1_rssi;
  nx_int16_t node_2_rssi;
  nx_int16_t node_3_rssi;
  nx_int16_t node_4_rssi;
} radio_count_msg_t;

typedef nx_struct RssiMsg{
  nx_int16_t rssi;
} RssiMsg;

enum {
  AM_RADIO_COUNT_MSG = 6,
  AM_RSSIMSG = 10
};

enum {
  AM_RSSIMSG = 10
};
#endif
