var utils = require('../libs/utils');

exports.getIndexPage = function (req, res, next) {
    res.redirect('/login');
}

exports.getLoginPage = function (req, res, next) {
    if (global.isAuthenticated) {
        res.redirect('/home');
    }
    return res.render('el/login', { err: null });
}

exports.login = function (req, res, next) {
    if (utils.isPwdCorrect(req.body.pwd)) {
        global.isAuthenticated = true;
        res.redirect('/home');
    } else {
        return res.render('el/login', { err: 'Incorrect password.' });
    }
}

exports.logout = function (req, res, next) {
    global.isAuthenticated = false;
    res.redirect('/login');
}

exports.authenticate = function (req, res, next) {
    if (!global.isAuthenticated) {
        return res.redirect('/login');
    }
    next();
}
