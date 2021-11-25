<?php
    include "./lib/conn_db.php";

    /*-------------- 영화 리뷰 데이터 테이블 생성--------------*/
    $sql = "CREATE TABLE review_tbl (
        uno int PRIMARY KEY NOT NULL AUTO_INCREMENT,
        title varchar(20) NOT NULL,
        review mediumtext,
        score tinyint(1) NOT NULL)";

    //FOREIGN KEY (uno) REFERENCES user_tbl(num))
    $result = mysqli_query($connect, $sql);

    mysqli_close($connect);
    
?>

<!DOCTYPE html>
<head>
    <title> 영화 리뷰 </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body><br><center> <h2> 영화 리뷰 </h2><hr>
<form name=f2 method=post action="review_db.php">
<table class="table table-dark table-striped" >
    <tr>
        <br> 
        <td></td>
        <td>
            <a class="btn btn-lg btn-primary" href="review_db.php">리뷰된 영화 리스트 보기</a>
    </tr> 
    <tr>
        <br>
		  <td width=20% height=30 align=right><b> 영화 제목 : </b></td>
        <td>&nbsp;<input type="text" size=25  name='movie_title'></td>
    </tr> 
	 <tr>
        <td width=20% height=30 align=right><b> 영화 리뷰 : </b></td>
        <td>	&nbsp;<textarea name="movie_review" rows="4" cols="45"></textarea></td>
    </tr>
	 <tr>
        <td height=30 align=right><b> 평점(5점만점) :   </b></td>
        <td>	&nbsp;<input type="text" size=3 name='movie_score'></td>
    </tr>
	<tr>
        <td height=40% align=center colspan=2>
            <input type=submit value="  입력하기  ">&nbsp;&nbsp;&nbsp;&nbsp;
            <input type=reset value= "  다시작성  ">
        </td>
    </tr>
</table>
</form>
</body>
</html>