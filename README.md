![nogoogle logo](http://i.imgur.com/Hd8W5Dw.png)
# nogoogle

A simple way of removing Google from your life.

## Notes

Don't use this yet.

### OSX

Install:
    brew install dnsmasq

Configure:
    cp dnsmasq.conf /usr/local/etc/dnsmasq.conf

Start at Boot:
    sudo cp -fv /usr/local/opt/dnsmasq/*.plist /Library/LaunchDaemons

Start now:
    sudo launchctl load /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist

### Ubuntu

    apt-get install dnsmasq

### Windows

    I don't know. Maybe this as an alternative? http://mayakron.altervista.org/wikibase/show.php?id=AcrylicHome

### Others

    Install dnsmaqs with your package manager of choice, or from source.
