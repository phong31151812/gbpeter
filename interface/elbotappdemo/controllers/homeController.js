var utils = require('../libs/utils');
var async = require('async');
var pathConstants = require('../constants/path');

exports.getHomePage = function (req, res, next){
    res.render('el/home');
}

exports.getBattery = function (req, res, next){
    var path = pathConstants.GET_BATTERY1;
    
    utils.callPythonFile(path, [], function(percentage){
        res.status(200).send(percentage);
    });
}