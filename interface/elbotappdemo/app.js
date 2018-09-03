var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var connectWifiRouter = require('./routes/connectWifi');
var callPythonRouter = require('./routes/callPython');
var codeditorRouter = require('./routes/codeditor');
var elRouter = require('./routes/el');

var app = express();

var gulp = require('gulp');
var fontAwesome = require('node-font-awesome');
var middleware = require('./middleware');
var expressLayouts = require('express-ejs-layouts');
 
gulp.task('fonts', function() {
  gulp.src(fontAwesome.fonts)
    .pipe(gulp.dest('./app/fonts'));
});

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// app.use('/js', express.static(__dirname + '/node_modules/bootstrap/dist/js')); // redirect bootstrap JS
// app.use('/js', express.static(__dirname + '/node_modules/jquery/dist')); // redirect JS jQuery
// app.use('/css', express.static(__dirname + '/node_modules/bootstrap/dist/css')); // redirect CSS bootstrap
//app.use('/fonts', express.static('./node_modules/font-awesome/fonts'))

// view engine setup
app.set('views', path.join(__dirname, 'views'));
// app.set('view engine', 'jade');

app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.use(expressLayouts);
app.set('layout', 'el/layout');

app.use(middleware.setup);
app.use(middleware.loadConfig);

app.use('/', elRouter);
app.use('/users', usersRouter);

app.use('/connectWifi', connectWifiRouter);
app.use('/callPython', callPythonRouter);
app.use('/codeditor', codeditorRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  // next(createError(404));
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: err
  });
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});


module.exports = app;
