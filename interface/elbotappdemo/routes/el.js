var express = require('express');
var router = express.Router();

var loginController = require('../controllers/loginController');
var homeController = require('../controllers/homeController');
var settingController = require('../controllers/settingController');
var scratchController = require('../controllers/scratchController');
var learningEnglishController = require('../controllers/learningEnglishController');

var moment = require('moment');
var Wifi = require('rpi-wifi-connection');
var async = require('async');

router.get('/', loginController.getIndexPage);
router.get('/login', loginController.getLoginPage);
router.post('/login', loginController.login);
router.post('/logout', loginController.logout);
router.all('/*', loginController.authenticate);

router.get('/home', homeController.getHomePage);
router.get('/getBattery', homeController.getBattery);

router.get('/settings', settingController.getSettingPage);
router.get('/settings/security', settingController.getSecurityPage);
router.get('/settings/security/setPassword', settingController.getSetPwdPage);
router.post('/setPassword', settingController.setPwd);
router.get('/settings/connectWifi', settingController.getConnectWifiPage);
router.get('/settings/screen', settingController.getScreenPage);
router.post('/setScreen', settingController.setScreen);
router.get('/settings/getVolume', settingController.getVolume);
router.post('/settings/setVolume', settingController.setVolume);
router.get('/settings/cmd', settingController.getCmdPage);
router.post('/runCmd', settingController.runCmd);

router.post('/connectWifi', settingController.connectWifi);

router.get('/learningEnglish', learningEnglishController.getLearningPage);

router.get('/scratch', scratchController.getScratchPage);
router.post('/scratch/callPython', scratchController.callPython);

module.exports = router;
