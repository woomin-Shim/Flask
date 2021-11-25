<?php
//회원정보 디비에 넣고 메인 페이지로 이동하게끔 
    include "./lib/conn_db.php";

    $user_id = $_POST['id'];
    $user_pwd = $_POST['password'];

    /*------ 데이터베이스에 회원 정보 입력 -----------------*/
    $sql = "INSERT INTO user_tbl(id, passwd) ";
    $sql.= "VALUES('$user_id', '$user_pwd')";

    mysqli_query($connect, $sql);
    mysqli_close($connect);
?>


<!DOCTYPE html>
<html>
<head>
	<title>영화 리뷰 로그인</title>
	<link rel="stylesheet" a href="css\style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <form name="login_form" action="add_review.php" method="get">
	    <div class="container">
            <p class='start-input'>
                로그인이 성공적으로 되었습니다.<br>
                영화 리뷰를 시작해보세요.
            </p>
			<input type="submit" type="submit" value=" 영화 리뷰 하러 가기 " class="btn-start" /> &nbsp;&nbsp;
	    </div>
</form>
</body>
</html>