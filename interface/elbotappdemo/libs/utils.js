var crypto = require('crypto');
var fs = require('fs');
var path = require('path');
var settingsFilePath = path.join(process.cwd(), 'settings');
var spawn = require("child_process").spawn;

exports.md5Hash = function (input) {
    return crypto.createHash('md5').update(input).digest('hex');
}

exports.isPwdCorrect = function (pwdInput) {
    var settings = this.readSettingFile();
    return this.md5Hash(pwdInput) === settings.pwd;
}

exports.updatePwd = function (newPwd) {
    var settings = this.readSettingFile();
    settings.pwd = this.md5Hash(newPwd);
    return this.writeSettingFile(settings);
}

exports.updateScreen = function (newScreen) {
    var settings = this.readSettingFile();
    settings.screen = newScreen;
    return this.writeSettingFile(settings);
}

exports.readSettingFile = function () {
    var settings = fs.readFileSync(settingsFilePath, { encoding: 'utf-8' });
    return (settings) ? JSON.parse(settings) : settings;
}

exports.writeSettingFile = function (settings) {
    fs.writeFile(settingsFilePath, JSON.stringify(settings), function (err) {
        if (err) return err;
    });
}

exports.callPythonFile = function (filePath, params, callback) {
    var fileName = path.resolve(__dirname, filePath);

    params.unshift(fileName);
    var process = spawn('python', params);

    process.stdout.on('data', function (data) {
        console.log(data);
        callback(data);
    });
}

exports.getNewPath = function (cwd, args) {
    args.shift();
    args.forEach(arg => {
        cwd = path.resolve(cwd, arg);
    });

    return cwd;
}

exports.isPathExists = function (filePath){
    return fs.existsSync(filePath);
}