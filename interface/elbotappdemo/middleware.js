var utils = require('./libs/utils');
var screens = require('./screen-settings').screens;

exports.setup = function (req, res, next) {
    var defaultScreen = screens[0];
    var defaultSettings = {
        pwd: utils.md5Hash('admin'),
        screen: {
            width: defaultScreen.width,
            height: defaultScreen.height
        }
    };
    var data = utils.readSettingFile();

    if (!data){
        utils.writeSettingFile(defaultSettings);
    }

    next();
}

exports.loadConfig = function (req, res, next){
    var settings = utils.readSettingFile();
    res.locals.screen = settings.screen;
    next();
}