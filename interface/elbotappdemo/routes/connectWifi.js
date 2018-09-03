var express = require('express');
var router = express.Router();
/*
var wifi = require('node-wifi');
var async = require("async");
// Initialize wifi module
// Absolutely necessary even to set interface to null
wifi.init({
    iface: null // network interface, choose a random wifi interface if set to null
});

var showPage = function(res, errors){
    var dataNetworks = null;
    
        async.series([
            function (callback) {
                try{
                    wifi.scan(function (err, networks) {
                        if (err) {
                            console.log(err);
                            callback(null, "done");
                        } else {
                            console.log(networks);
                            dataNetworks = networks;
                            callback(null, "done");
                        }
                    });
                }catch(err){
                    callback(null, "done");
                }
            }
        ],
            function (err, result) {
                
                
                res.send('respond the result:' + dataNetworks);
                //res.render('connectWifi', { title: 'Express', dataNetworks: dataNetworks, errors:errors });
            });
        // Scan networks
    
    
        //
}


router.get('/', function (req, res, next) {
    showPage(res, {});
});

const { check, validationResult } = require('express-validator/check')

router.post('/', [
    check('wifi')
        .isLength({ min: 1 })
        .withMessage('wifi is required'),
    check('password')
        .isLength({ min: 1 })
        .withMessage('password is required')
], (req, res) => {
    const errors = validationResult(req)
    if (!errors.isEmpty()) {
        // There are errors. Render the form again with sanitized values/error messages.
        //res.render('genre_form', { title: 'Create Genre', genre: genre, errors: errors.array()});
        //res.send('Error validation');
        showPage(res, errors.mapped());
    }
    else {
        // Connect to a network
        var ssid = req.body.wifi;
        var password = req.body.password;
        wifi.connect({ ssid: ssid, password: password }, function (err) {
            if (err) {
                console.log(err);
                showPage(res, {
                    password: {
                      msg: 'Wrong password'
                    }
                });
            }else{
                res.send('Ket noi thanh cong');
            }
        });
    }
});




var showAllWifi = function(millisecond){
	wifi.scan().then((ssids) => {
	console.log(ssids);
	})
	.catch((error) => {
		console.log(error);
	});
	setTimeout(function () {
	  showAllWifi(millisecond);
	}, millisecond)
}

//showAllWifi(1000);

var connectWifi = function(millisecond){
	wifi.connect({ssid:'HuongThao', psk:'19032015'}).then(() => {
		console.log('Connected to network.');
	})
	.catch((error) => {
		console.log(error);
	});
	setTimeout(function () {
	  connectWifi(millisecond);
	}, millisecond)
}

connectWifi(3000);

/*


/*
iwlist.scan({ iface : 'wlan0', show_hidden : true }, function(err, networks) {
					if (err) {
						console.log(err);
					} else {
						console.log(networks);
					}
				});
/*				
wifi.connect({ ssid : "HuongThao", password : "19032015"}, function(err) {
    if (err) {
        console.log(err);
    }else{
    console.log('Connected');}
});
*/
/*
var wpa_supplicant = require('wireless-tools/wpa_supplicant');
 
var options = {
  interface: 'wlan0',
  ssid: 'HuongThao',
  passphrase: '19032015'
};
 
wpa_supplicant.enable(options, function(err) {
  if (err) {
		console.log(err);
	}else{
	console.log("Ket noi thanh cong");
	}
	
});

*/


var async = require("async");
var Wifi = require('rpi-wifi-connection');
var wifi = new Wifi();

var showPage = function(res, errors){
    var dataNetworks = null;
    
        async.series([
            function (callback) {
                try{
					wifi.scan().then((ssids) => {
						console.log(ssids);
						dataNetworks = ssids;
						callback(null, "done");
					})
					.catch((error) => {
						console.log(error);						
						callback(null, "done");
					});				
                }catch(err){
                    callback(null, "done");
                }
            }
        ],
		function (err, result) {
			//res.send('respond the result:' + dataNetworks);
			res.render('connectWifi', { title: 'Express', dataNetworks: dataNetworks, errors:errors });
		});
        // Scan networks
    
    
        //
}
router.get('/', function (req, res, next) {
    showPage(res, {});
});


const { check, validationResult } = require('express-validator/check')

router.post('/', [
    check('wifi')
        .isLength({ min: 1 })
        .withMessage('wifi is required'),
    check('password')
        .isLength({ min: 1 })
        .withMessage('password is required')
], (req, res) => {
    const errors = validationResult(req)
    if (!errors.isEmpty()) {
        // There are errors. Render the form again with sanitized values/error messages.
        //res.render('genre_form', { title: 'Create Genre', genre: genre, errors: errors.array()});
        //res.send('Error validation');
        showPage(res, errors.mapped());
    }
    else {
        // Connect to a network
        var ssid = req.body.wifi;
        var password = req.body.password;
		wifi.connect({ssid:ssid, psk:password}).then(() => {
			console.log('Connected to network.');
			showPage(res, {
                    status: {
                      msg: 'Kết nối Wifi thành công.'
                    }
                });
		})
		.catch((error) => {
			showPage(res, {
                    password: {
                      msg: 'Wrong password'
                    }
                });
		});
    }
});

module.exports = router;
