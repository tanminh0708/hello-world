<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Simple Web Crawler</title>
    <style>
        .error {
            color: red;
        }

        input {
            display: block;
            margin-bottom: 10px;
        }
    </style>
</head>

<body>
    <h1>Một dịch vụ đơn giản để lấy trạng thái trang web</h1>
    <h2>Chỉ cần nhập trang web của bạn ở đây và nhấp vào nút "Gửi"!</h2>

    <form action="#" method="post">
        <input name="url" id="url" type="text" />

        <input type="submit" value="Gửi" />
    </form>
</body>

</html>

<?php
if (isset($_POST['url'])) {
    $command = "curl -I http://" . $_POST['url'];
    exec($command, $output);
    echo '<pre>'; print_r($output); echo '</pre>';
}
?>