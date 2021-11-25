<?php
    include "./lib/conn_db.php";

    //add_review에서 데이터가 넘어올때만 동작하게 
    if(isset($_POST['movie_title'])) {
        $title = $_POST['movie_title'];
        $review = $_POST['movie_review'];
        $score = $_POST['movie_score'];

        /*-------------- 영화 리뷰 데이터 테이블 생성--------------*/
        $sql = "INSERT INTO review_tbl(title, review, score) 
                VALUES('$title', '$review', '$score')";
    
    
        //FOREIGN KEY (uno) REFERENCES user_tbl(num))
        $result = mysqli_query($connect, $sql);
    }

    //mysqli_close($connect);
    
?>

<html>
    <head>
        <title>영화 리뷰</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <br><br><center><h1>영화 리뷰</h1><br><hr></center>
        <br><h3>영화 제목별로 검색</h3>
        <form action = "search_movie.php" method="get">
            <input type = "search" name="search">
            <input type = "submit" value="검색">&nbsp;&nbsp;&nbsp;
            <a class="btn btn-lg btn-primary" href="add_review.php">리뷰 작성하러 가기</a><br><br>
        <?php
            $sql = "SELECT DISTINCT title, review, score FROM review_tbl
                    ORDER BY uno DESC";  //최근에 등록한 리뷰가 맨 위로 
    
            $result = mysqli_query($connect, $sql);
            mysqli_close($connect);
        ?>
        
        <table class="table table-dark table-striped" >
            <tr><td width=170 align='center'>제목</td>
                <td width=70 align='center'>평점</td>
                <td align='center'>후기</td>
            </tr>
        
            <?php
                while($rows=mysqli_fetch_array($result)) {
                    echo "<tr>";
                    echo "<td align='center'>{$rows['title']}</td>";
                    echo "<td align='center'>{$rows['score']}</td>";
                    echo "<td>{$rows['review']}</td>";
                    echo "</tr>";
                }
            ?>
        </table>
        </form>
    </body>
</html>