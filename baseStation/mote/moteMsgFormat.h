
#ifndef MOTE_MSG_FORMAT_H
#define MOTE_MSG_FORMAT_H

typedef nx_struct MESSAGE {
  nx_uint8_t type;
  nx_uint8_t sender;
  nx_uint16_t data;
  nx_uint16_t temp;
} MESSAGE_t;

enum {
  AM_RADIO_COUNT_MSG = 6,
};

#endif
