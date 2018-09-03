var utils = require('../libs/utils');
var wifi = require('../libs/wifi');
var screenSettings = require('../screen-settings');
var pathConstants = require('../constants/path');

var async = require('async');
var exec = require('child_process').exec;
var os = require('os');
var cwd = os.homedir();
var fs = require('fs');

exports.getSettingPage = function (req, res, next) {
    res.render('el/settings/index');
}

exports.getSecurityPage = function (req, res, next) {
    res.render('el/settings/security');
}

exports.getSetPwdPage = function (req, res, next) {
    res.render('el/settings/setPassword', {
        err: null
    });
}

exports.setPwd = function (req, res, next) {
    if (req.body.newPwd !== req.body.reNewPwd) {
        res.render('el/settings/setPassword', {
            err: 'New password mismatch.'
        });
    }

    if (utils.isPwdCorrect(req.body.curPwd)) {
        var err = utils.updatePwd(req.body.newPwd);

        if (err) return res.sendStatus(500);
        res.redirect('/login');
    } else {
        res.render('el/settings/setPassword', {
            err: 'Incorrect password.'
        });
    }
};

exports.getConnectWifiPage = function (req, res, next) {
    async.waterfall([
        wifi.getAvailableWifi,
    ], function (err, networks) {
        if (err) {
            console.log(err);
            return res.sendStatus(500);
        }
        res.render('el/settings/connectWifi', {
            networks: networks
        });
    })
}

exports.connectWifi = function (req, res, next) {
    async.waterfall([
        wifi.connectToNetwork,
    ], function (err, connected) {
        if (err) {
            console.log(err);
            return res.send(err);
        }

        if (connected) {
            var ip = wifi.getLocalIP();
            console.log(ip);
            res.send('Connected successfully!\nLocal ip address: ' + ip);
        } else {
            res.send('Wrong password.')
        }
    })
}

exports.getScreenPage = function (req, res, next) {
    res.render('el/settings/screen', {
        screens: screenSettings.screens
    });
}

exports.setScreen = function (req, res, next) {
    var newScreen = screenSettings.screens.find((el) => el.name == req.body.screen);
    var err = utils.updateScreen(newScreen);
    if (err) return res.sendStatus(500);

    res.redirect('/settings/screen');
}

exports.getVolume = function (req, res, next) {
    var path = pathConstants.GET_VOLUME1;

    utils.callPythonFile(path, [], function (data) {
        console.log(data);
        res.status(200).send(data);
    });
}

exports.setVolume = function (req, res, next) {
    var path = pathConstants.SET_VOLUME;
    var params = [req.body.vol]

    utils.callPythonFile(path, params, function (data) {
        res.status(200).send(data);
    });
}

exports.getCmdPage = function (req, res, next) {
    res.render('el/settings/cmd');
}

exports.runCmd = function (req, res, next) {
    var command = req.body.cmd;
    var args = command.split(' ');

    if (args[0] === "cd") {
        var newCwd = utils.getNewPath(cwd, args);

        console.log(newCwd);
        console.log(fs.existsSync(newCwd));
        if (!utils.isPathExists(newCwd)) {
            return res.send("Path does not exists");
        }

        cwd = newCwd;
        return res.send(cwd);
    }

    exec(req.body.cmd, { cwd: cwd }, (err, stdout, stderr) => {
        if (err) {
            return res.send(String(err));
        }
        console.log(`stdout: ${stderr}`);
        res.send(stdout);
    });
}