var http = require('http');
var server = http.createServer(function(req, res) {
    console.log('Method : ', req.method);
    console.log('url : ', req.url);
    console.log('headers :' );

    res.write('Hello world ');
    res.end();
}).listen(3000);