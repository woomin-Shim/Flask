<?php
    include "./lib/conn_db.php";
    //mysqli_close($connect);
?>

<html>
    <head>
        <title>영화 리뷰</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <h1>영화 별 검색</h1>
        <form action = "search_movie.php" method="get">
            <input type = "search" name="search">
            <input type = "submit" value="검색"><br>
        </form>
            <a class="btn btn-lg btn-primary" href="review_db.php">전체 영화 리뷰 보기</a>&nbsp;&nbsp;
	        <a class="btn btn-lg btn-primary" href="add_review.php">리뷰 작성하러 가기</a><br><br>
        <?php
            if(isset($_GET["search"])) {
                $sql = "SELECT DISTINCT title, review, score FROM review_tbl
                        WHERE title LIKE '%".$_GET["search"]."%'";
            }
            else $sql = "SELECT DISTINCT title, review, score FROM review_tbl";
        

            $result = mysqli_query($connect, $sql);
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
        
    </body>
</html>