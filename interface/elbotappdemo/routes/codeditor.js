var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.render('codeditor', { title: 'codeditor' });
});

module.exports = router;
