INSTALLBIN = $(DESTDIR)/usr/bin
INSTALLDESKTOP = $(DESTDIR)/usr/share/applications/


all: bin/setxkbmap-gadget

bin/setxkbmap-gadget:
	mkdir -r bin
	cp  src/setxkbmap-gadget.py  bin/setxkbmap-gadget
	chmod 755 bin/setxkbmap-gadget

install: all
	install -d  $(INSTALLBIN)
	install bin/setxkbmap-gadget $(INSTALLBIN)
	install -d  $(INSTALLDESKTOP)
	install desktop/setxkbmap-gadget.desktop $(INSTALLDESKTOP)

clean: 
	rm bin/setxkbmap-gadget
