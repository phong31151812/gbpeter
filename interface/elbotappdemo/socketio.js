var wifi = require('./libs/wifi');
var async = require('async');
var timeConstants = require('./constants/time');

module.exports = (io) => {
    io.on('connection', function (socket) {
        socket.on('Learning_English', function (msg) {
            io.emit('Learning_English', msg);
        });

        // cmt this when run on raspberry pi
        /*var connected = false;
        setInterval(function () {
            connected = !connected;
            io.emit('wifi_status', connected);
        }, 240000 );*/

        // uncmt this when run on raspberry pi
        broadcastConnectionState(io);
        
    });
}

function broadcastConnectionState(io) {
    async.waterfall([
        wifi.checkConnectionState,
    ], function (err, connected) {
        if (err) {
            console.log(err);
        }
        io.emit('wifi_status', connected);
    })
    setTimeout(broadcastConnectionState, timeConstants.CHECK_WIFI_STATUS);
}