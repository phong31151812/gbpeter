var express = require('express');
var router = express.Router();

var showPage = function(res, errors){
    res.render('callPython', { errors:errors });
}

router.get('/', function (req, res, next) {
	showPage(res, {});
});


const { check, validationResult } = require('express-validator/check')

router.post('/', [
    check('fileName')
        .isLength({ min: 1 })
        .withMessage('fileName is required'),
    check('para1')
        .isLength({ min: 1 })
        .withMessage('para1 is required')
], (req, res) => {
    const errors = validationResult(req)
    if (!errors.isEmpty()) {
        // There are errors. Render the form again with sanitized values/error messages.
        //res.render('genre_form', { title: 'Create Genre', genre: genre, errors: errors.array()});
        //res.send('Error validation');
        showPage(res, errors.mapped());
    }
    else {
		var fileName = req.body.fileName;
        var para1 = req.body.para1;
		// Use child_process.spawn method from
		// child_process module and assign it
		// to variable spawn
		var spawn = require("child_process").spawn;

		// Parameters passed in spawn -
		// 1. type_of_script
		// 2. List containing Path of the script
		//    and arguments for the script

		// E.g.: http://localhost:3000/name?arg=Will
		// So, first name = Mike and last name = Will
    fileName = "../python/" + fileName + ".py";
    console.log(fileName);
		var process = spawn('python',[fileName,
                para1] );
    console.log('ok');

		// Takes stdout data from script which executed
		// with arguments and send this data to res object
		process.stdout.on('data', function(data) {			
			showPage(res, {
                    result: {
                      msg: data.toString()
                    }
                });
		} )
    }
});

module.exports = router;
