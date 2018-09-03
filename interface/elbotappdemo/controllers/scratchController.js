var async = require('async');
var utils = require('../libs/utils');
var pathConstants = require('../constants/path');

exports.getScratchPage = function (req, res, next) {
    res.render('el/scratch/index');
}

exports.callPython = function (req, res, next) {
    var path = pathConstants.RUN_SCRATCH;
    var param = [req.body.param];
    
    utils.callPythonFile(path, param, function(data){
        res.status(200).send(data);
    });

   
}