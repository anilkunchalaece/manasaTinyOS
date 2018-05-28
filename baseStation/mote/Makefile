COMPONENT=MoteC
CFLAGS += -DTOSH_DATA_LENGTH=100
CFLAGS += -I$(TOSDIR)/lib/printf


BUILD_EXTRA_DEPS = MoteMsg.py MoteMsg.class
CLEAN_EXTRA = MoteMsg.py MoteMsg.class MoteMsg.java

MoteMsg.py: moteMsgFormat.h
	mig python -target=$(PLATFORM) $(CFLAGS) -python-classname=MoteMsg moteMsgFormat.h MESSAGE -o $@

MoteMsg.class: MoteMsg.java
	javac MoteMsg.java

MoteMsg.java: moteMsgFormat.h
	mig java -target=$(PLATFORM) $(CFLAGS) -java-classname=MoteMsg moteMsgFormat.h MESSAGE -o $@
include $(MAKERULES)

