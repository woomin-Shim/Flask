/* routing:method 별로
   - GET 요청 -> app.get('/',function(req, res){});
   - POST 요청 -> app.get('/', function(req, res){});

   routing:경로 별
   -user 경로에 GET 요청-응답 
   : app.get('/user', function(req, res){});

   -items 경로에 GET 요청-응답
   : app.get('/items', function(req, res){}); 
   */
var express = require('express');
var app = express();

app.get('/:value', work);
app.use(errorHandler);

app.listen(3000);

function work(req, res, next) {  
    var val = parseInt(req.params.value);

    //check input parameters
    if(!val) {
        var error = new Error('입력값이 숫자가 아닙니다.');
        next(error);  //Call next middleware(errorHandler)
        return;
    }
    res.send('Result : ' + val);
}

function errorHandler(err, req, res, next) {
    res.send('Error 발생');
}