![nogoogle logo](http://i.imgur.com/Hd8W5Dw.png)
# nogoogle

A simple way of removing Google from your life.

**nogoogle** uses dnsmasq to black-hole all known Google domains. 

## Notes

Don't use this yet.

### OSX

Install dnsmasq:

    brew install dnsmasq

Configure nogoogle:

    cp dnsmasq.conf /usr/local/etc/dnsmasq.conf

Start at boot:

    sudo cp -fv /usr/local/opt/dnsmasq/*.plist /Library/LaunchDaemons

Start now:

    sudo launchctl load /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist

### Ubuntu

Install dnsmasq:

    sudo apt-get install dnsmasq

Configure nogoogle:

    sudo cp dnsmasq.conf /etc/dnsmasq.conf

### Windows

    I don't know. Maybe this as an alternative? http://mayakron.altervista.org/wikibase/show.php?id=AcrylicHome

### Others

    Install dnsmaqs with your package manager of choice, or from source.
