INSTALLBIN = $(DESTDIR)/usr/bin
INSTALLDESKTOP = $(DESTDIR)/usr/share/applications/


all: *
	echo "do nothing.."

install: all
	install -d  $(INSTALLBIN)
	install bin/setxkbmap-gadget $(INSTALLBIN)
	install -d  $(INSTALLDESKTOP)
	install desktop/setxkbmap-gadget.desktop $(INSTALLDESKTOP)

clean: 
	echo "do nothing.."
