<?php
    include "lib/conn_db.php";

    if(!$db) {  //movie_db에 연결되지 않았다면
        echo " <B> Using movie_db Database fail </B><br> ";
        exit;
    }

    /*--------------- user_tbl 테이블 ----------------------*/
    $sql = "CREATE TABLE user_tbl (
                num int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                id varchar(20) NOT NULL,
                passwd varchar(20) NOT NULL) ";

    $result = mysqli_query($connect, $sql);

    mysqli_close($connect);
?>


<!DOCTYPE html>
<html>
<head>
	<title>영화 리뷰 로그인</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" a href="css\style.css">
</head>
<body>
	<div class="container">
	<img src="image/user.png"/>
		<form name="login_form" action="start.php" method="post">
			<div class="form-input">
				<input type="text" name="id" placeholder="ID를 입력해 주세요"/>	
			</div>
			<div class="form-input">
				<input type="password" name="password" placeholder="password를 입력해 주세요"/>
			</div>
			<input type="submit" type="submit" value=" 로그인 " class="btn-login"/> &nbsp;&nbsp;
		    <input type="reset" name="Reset" value=" 취  소  " class="btn-cancel"/>
		</form>
	</div>
</body>
</html>