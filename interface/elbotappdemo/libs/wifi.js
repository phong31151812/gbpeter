var Wifi = require('rpi-wifi-connection');
var wifi = new Wifi();
var os = require('os');

exports.getAvailableWifi = function (callback) {
    wifi.scan().then((ssids) => {
        callback(null, ssids);
    })
        .catch((err) => {
            callback(err);
        });
}

exports.checkConnectionState = function (callback) {
    wifi.getState().then((connected) => {
        callback(null, connected);
    })
        .catch((err) => {
            callback(err);
        });
}

exports.connectToNetwork = function (ssid, psk, callback) {
    wifi.connect({ ssid: ssid, psk: psk }).then(() => {
        callback(null, true);
    })
        .catch((err) => {
            callback(err);
        });
}

exports.getLocalIP = function () {
    var networkInterfaces = os.networkInterfaces();
    return networkInterfaces["Ethernet"].find((iface) => iface.family == "IPv4").address;
}